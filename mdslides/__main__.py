#!/bin/python3.8
from pathlib import Path
import argparse
import shutil
import subprocess
import re


def main():
    parser = argparse.ArgumentParser(
            description='Convert a markdown file to a reveal.js presentation.'
        )
    parser.add_argument('FILE', type=str, help="Markdown file.")
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
    args = parser.parse_args()
    export_to_pdf = args.pdf
    export_to_html = not export_to_pdf

    # TODO: export to pdf, change name of output folder

    import pathlib
    resource_path = pathlib.Path(__file__).parent.absolute()
    target_path = pathlib.Path().absolute()

    revealjs_origin = resource_path/"reveal.js"
    math_origin = resource_path/"KaTeX"
    markdown_file = Path(args.FILE)
    revealjs_dir = target_path/markdown_file.stem
    math_dir = revealjs_dir/"KaTeX"
    index_file_original = resource_path/"index_template.html"
    index_file_new = target_path/revealjs_dir/"index.html"

    def pdf_chromium_export(index_html_path: Path, output_pdf_path: Path):
        command = [
            'chromium',
            '--headless',
            '--print-to-pdf={}'.format(output_pdf_path),
            index_html_path.resolve().as_uri()+'?print-pdf',
        ]
        subprocess.run(command)

    magic_word = "DATA"
    title_word = "TITLE"
    options_word = "Reveal.initialize({"
    theme_word = '<link rel="stylesheet" href="dist/theme'
    code_theme_word = '<link rel="stylesheet" href="plugin/highlight'

    title_template = "<title>{}</title>"
    section_template = "<section data-markdown {}><textarea data-template>\n{}\n</textarea></section>"
    #section_template = "<section data-markdown {}>\n{}\n</section>"
    theme_template = '<link rel="stylesheet" href="dist/theme/{}.css" id="theme">'
    code_theme_template = '<link rel="stylesheet" href="plugin/highlight/{}.css" id="highlight-theme">'

    option_re = r"\[comment\]: # \([ ]*(\w+)[ ]*:[ ]*(\w+)[ ]*\)"
    option_re = re.compile(option_re)
    delimiter_re = r"\[comment\]: # \(\!\!\![ ]*(.*)\)"
    delimiter_re = re.compile(delimiter_re)
    theme_re = r"\[comment\]: # \([ ]*THEME[ ]*=[ ]*(\w+)[ ]*\)"
    theme_re = re.compile(theme_re)
    code_theme_re = r"\[comment\]: # \([ ]*CODE_THEME[ ]*=[ ]*(\w+)[ ]*\)"
    code_theme_re = re.compile(code_theme_re)
    title_re = r"#[#]*[ ]*(.*)"
    title_re = re.compile(title_re)

    default_attributes = ""
    default_theme = "white"
    default_code_theme = "zenburn"
    default_options = {
            "controls": "false",
            "markdown": "{smartypants: true}",
        }

    # Open markdown file
    with open(markdown_file) as f:
        presentation_markdown = list(f)

    # Build presentation
    presentation = list()
    slide = list()
    options = ["{} : {},".format(key, val)
               for key, val in default_options.items()]
    theme = default_theme
    code_theme = default_code_theme
    attributes = default_attributes
    title = None
    for line in presentation_markdown:
        line = line[:-1]

        # Is the line setting an option?
        m = option_re.match(line)
        if m is not None:
            options.append("{} : {},".format(m.group(1), m.group(2)))
            continue

        # Is the line a slide break?
        m = delimiter_re.match(line)
        if m is not None:
            attributes = default_attributes + " " + m.group(1)
            presentation.append(
                    section_template.format(attributes, "\n".join(slide))
                )
            slide = list()
            continue

        # Is the line setting a theme?
        m = theme_re.match(line)
        if m is not None:
            theme = m.group(1)
            continue

        # Is the line setting a code theme?
        m = code_theme_re.match(line)
        if m is not None:
            code_theme = m.group(1)
            continue

        # Is the line the first heading?
        m = title_re.match(line)
        if m is not None:
            h1 = m.group(1)
            if title is None:
                title = h1

        # Else, we assume the line is markdown
        slide.append(line)

    # Did the user forget to insert the final slide break?
    if len(slide) > 0:
        presentation.append(
                section_template.format(default_attributes, "\n".join(slide))
            )

    # Replacement strings
    if title is None:
        title = "Slides"
    title = title_template.format(title)
    presentation = "\n".join(presentation + [""])
    options = "\n".join([options_word] + options + [""])
    theme = theme_template.format(theme)
    code_theme = code_theme_template.format(code_theme)

    # Copy revealjs dir
    if not revealjs_dir.exists():
        shutil.copytree(revealjs_origin, revealjs_dir)
        shutil.copytree(math_origin, math_dir)

    # Read html
    with open(index_file_original, "r") as f:
        index_html = list(f)

    # Replace title
    index_html = [line if title_word not in line else title
                  for line in index_html]
    # Replace theme
    index_html = [line if theme_word not in line else theme
                  for line in index_html]
    # Replace code theme
    index_html = [line if code_theme_word not in line else code_theme
                  for line in index_html]
    # Replace presentation
    index_html = [line if magic_word not in line else presentation
                  for line in index_html]
    # Replace options
    index_html = [line if options_word not in line else options
                  for line in index_html]

    with open(index_file_new, "w") as f:
        f.write("".join(index_html))

    # Copy include files
    for path in [Path(p) for p in args.include]:
        if path.is_dir:
            shutil.copytree(
                    path, revealjs_dir/path.parts[-1], dirs_exist_ok=True
                )
        else:
            shutil.copy(path, revealjs_dir/path.parts[-1], exist_ok=True)

    # Export to PDF if needed
    if export_to_pdf:
        try:
            pdf_chromium_export(
                    index_file_new, markdown_file.with_suffix('.pdf')
                )
            print("Wrote {}".format(markdown_file.with_suffix('.pdf')))

        except Exception as e:
            print("Chromium exporting failed")
            print(e)
            print("Make sure chromium is installed and in your path")

    if export_to_html:
        # Change output folder name
        print("Done. Open {} with your web browser".format(
                revealjs_dir/"index.html")
              )


if __name__ == "__main__":
    main()
