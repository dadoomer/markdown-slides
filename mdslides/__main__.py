"""Module for calling mdslides as an executable."""
import pathlib
from pathlib import Path
import argparse
import shutil
import re
from typing import List
from typing import Union
from .pdf import export as pdf_export

DATA_WORD = "DATA"
TITLE_WORD = "TITLE"
OPTIONS_WORD = "Reveal.initialize({"
THEME_WORD = '<link rel="stylesheet" href="dist/theme'
CODE_THEME_WORD = '<link rel="stylesheet" href="plugin/highlight'

TITLE_TEMPLATE = "<title>{}</title>"
SECTION_TEMPLATE = "<section data-markdown {}><textarea data-template>\n{}\n</textarea></section>"
VERTICAL_SECTION_TEMPLATE = "<section>\n{}\n</section>"
THEME_TEMPLATE = '<link rel="stylesheet" href="dist/theme/{}.css" id="theme">'
CODE_THEME_TEMPLATE = '<link rel="stylesheet" href="plugin/highlight/{}.min.css" id="highlight-theme">'

# Read both comment formats (first one is CommonMark compliant, second one
# is common format).
# [comment]: (stuff)
# [comment]: "stuff"
# [comment]: 'stuff'
RE_TEMPLATE = r"\[comment\]: # [(\"\']{0}[)\"\']"
OPTION_RE_PATTERN = r"[ ]*(\S+)[ ]*:[ ]*(\S+)[ ]*"
DELIMITER_RE_PATTERN = r"\!\!\![ ]*(.*)"
VERTICAL_DELIMITER_RE_PATTERN = r"\|\|\|[ ]*(.*)"
THEME_RE_PATTERN = r"[ ]*THEME[ ]*=[ ]*(\S+)[ ]*"
CODE_THEME_RE_PATTERN = r"[ ]*CODE_THEME[ ]*=[ ]*(\S+)[ ]*"
TITLE_RE_PATTERN = r"#[#]*[ ]*(.*)"
option_re = re.compile(RE_TEMPLATE.format(OPTION_RE_PATTERN))
delimiter_re = re.compile(RE_TEMPLATE.format(DELIMITER_RE_PATTERN))
vertical_delimiter_re = re.compile(RE_TEMPLATE.format(VERTICAL_DELIMITER_RE_PATTERN))
theme_re = re.compile(RE_TEMPLATE.format(THEME_RE_PATTERN))
code_theme_re = re.compile(RE_TEMPLATE.format(CODE_THEME_RE_PATTERN))
title_re = re.compile(TITLE_RE_PATTERN)

DEFAULT_ATTRIBUTES = ""
DEFAULT_THEME = "white"
DEFAULT_CODE_THEME = "base16/zenburn"
DEFAULT_OPTIONS = {
        "controls": "false",
        "markdown": "{smartypants: true}",
    }


REVEALJS_CRITICAL_PATHS = ["dist", "plugin", "LICENSE"]


def build_slides(
        markdown_file: Path,
        include_paths: List[Path],
        export_to_pdf: Path,
        target_path: Path,
        ):
    """Build slides in the given markdown file."""
    revealjs_dir = target_path
    resource_path = pathlib.Path(__file__).parent.absolute()

    revealjs_origin = resource_path/"reveal.js"
    index_file_original = resource_path/"index_template.html"
    index_file_new = revealjs_dir/"index.html"
    highlight_path = resource_path/"cdn-release"/"build"/"styles"

    # Open markdown file
    with open(markdown_file) as f_p:
        presentation_markdown = list(f_p)

    # Build presentation
    presentation = list()
    slide: List[str] = list()
    vertical_slide: List[str] = list()
    options = ["{} : {},".format(key, val)
               for key, val in DEFAULT_OPTIONS.items()]
    theme = DEFAULT_THEME
    code_theme_name = DEFAULT_CODE_THEME
    attributes = DEFAULT_ATTRIBUTES
    title = None
    for line in presentation_markdown:
        line = line[:-1]

        # Is the line setting an option?
        match = option_re.match(line)
        if match is not None:
            options.append("{} : {},".format(match.group(1), match.group(2)))
            continue

        # Is the line a slide break?
        match = delimiter_re.match(line)
        if match is not None:
            attributes = DEFAULT_ATTRIBUTES + " " + match.group(1)
            if vertical_slide:
                vertical_slide.append(
                    SECTION_TEMPLATE.format(attributes, "\n".join(slide))
                )
                presentation.append(
                    VERTICAL_SECTION_TEMPLATE.format("\n".join(vertical_slide))
                 )
                vertical_slide = list()
            else:
                presentation.append(
                    SECTION_TEMPLATE.format(attributes, "\n".join(slide))
                )
            slide = list()
            continue

        # Is the line a vertical slide break?
        match = vertical_delimiter_re.match(line)
        if match is not None:
            attributes = DEFAULT_ATTRIBUTES + " " + match.group(1)
            vertical_slide.append(
                SECTION_TEMPLATE.format(attributes, "\n".join(slide))
            )
            slide = list()
            continue

        # Is the line setting a theme?
        match = theme_re.match(line)
        if match is not None:
            theme = match.group(1)
            continue

        # Is the line setting a code theme?
        match = code_theme_re.match(line)
        if match is not None:
            code_theme_name = match.group(1)
            continue

        # Is the line the first heading?
        match = title_re.match(line)
        if match is not None:
            header = match.group(1)
            if title is None:
                title = header

        # Else, we assume the line is markdown
        slide.append(line)

    # Did the user forget to insert the final slide break?
    if vertical_slide:
        presentation.append(
            VERTICAL_SECTION_TEMPLATE.format("\n".join(vertical_slide))
         )
    if len(slide) > 0:
        presentation.append(
                SECTION_TEMPLATE.format(DEFAULT_ATTRIBUTES, "\n".join(slide))
            )

    # Replacement strings
    if title is None:
        title = "Slides"
    title = TITLE_TEMPLATE.format(title)
    presentation_str = "\n".join(presentation + [""])
    options_str = "\n".join([OPTIONS_WORD] + options + [""])
    theme = THEME_TEMPLATE.format(theme)
    code_theme = CODE_THEME_TEMPLATE.format(code_theme_name.split("/")[-1])

    # Copy and write needed files to the output directory
    critical_paths: List[Path] = list()

    # Copy revealjs dir
    if revealjs_dir.exists():
        shutil.rmtree(revealjs_dir)
    shutil.copytree(revealjs_origin, revealjs_dir)
    critical_paths.extend(
            revealjs_dir/path for path in REVEALJS_CRITICAL_PATHS
        )

    # Read html
    with open(index_file_original, "r") as f_p:
        index_html = list(f_p)

    # Replace title
    index_html = [line if TITLE_WORD not in line else title
                  for line in index_html]
    # Replace theme
    index_html = [line if THEME_WORD not in line else theme
                  for line in index_html]
    # Replace code theme
    index_html = [line if CODE_THEME_WORD not in line else code_theme
                  for line in index_html]
    # Replace presentation
    index_html = [line if DATA_WORD not in line else presentation_str
                  for line in index_html]
    # Replace options
    index_html = [line if OPTIONS_WORD not in line else options_str
                  for line in index_html]

    # Copy index file
    with open(index_file_new, "w") as f_p:
        f_p.write("".join(index_html))
        critical_paths.append(index_file_new)

    # Copy include files
    for path in include_paths:
        include_target_path = revealjs_dir/path.parts[-1]
        if path.is_dir():
            shutil.copytree(path, include_target_path, dirs_exist_ok=True)
        else:
            shutil.copy(path, include_target_path)
        critical_paths.append(include_target_path)

    # Remove unused reveal development files
    for path in revealjs_dir.glob("*"):
        if path not in critical_paths:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

    # Copy selected highlight style
    highlight_css = (highlight_path/code_theme_name).with_suffix(".min.css")
    shutil.copy(highlight_css, revealjs_dir/"plugin"/"highlight")

    # Export to PDF if needed
    if export_to_pdf:
        pdf_export(
                index_file_new, markdown_file.with_suffix('.pdf')
            )
        print("Wrote {}".format(markdown_file.with_suffix('.pdf')))

    print("Done. Open {} with your web browser".format(
        revealjs_dir/"index.html")
        )


def main():
    """Command-line callable function."""
    parser = argparse.ArgumentParser(
            description='Convert a markdown file to a reveal.js presentation.'
        )
    parser.add_argument('FILE', type=Path, help="Markdown file.")
    parser.add_argument(
            '--include',
            metavar="RESOURCE",
            help="Directory or file to include. "
            "This option can be used multiple times.",
            default=[],
            action="append"
        )
    parser.add_argument(
            '--pdf',
            help="Export a pdf file (requires chromium installed).",
            action="store_true"
        )
    parser.add_argument(
            '--output_dir',
            metavar="OUTPUT_DIR",
            help="Output directory. "
            "Defaults to a directory with the same name as the input "
            "markdown file with no suffix, created in the working directory.",
            type=Path,
            default=None,
        )
    args = parser.parse_args()
    markdown_file = args.FILE
    if args.output_dir is None:
        target_path = pathlib.Path().absolute()/markdown_file.stem
    else:
        target_path = Path(args.output_dir).absolute()
    build_slides(
            export_to_pdf=args.pdf,
            markdown_file=markdown_file,
            include_paths=[Path(p) for p in args.include],
            target_path=target_path,
        )


if __name__ == "__main__":
    main()
