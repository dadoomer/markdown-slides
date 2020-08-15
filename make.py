#!/bin/python3.8
from pathlib import Path
import argparse
from zipfile import ZipFile
import shutil
import subprocess
import re

parser = argparse.ArgumentParser(description='Convert a markdown file to a reveal.js presentation.')
parser.add_argument('FILE', type=str, help="Markdown file.")
parser.add_argument('--include', metavar="RESOURCE", help="Directory or file to include. This option can be used multiple times.", default=[], action="append")
parser.add_argument('--pdf', help="Export a pdf file (requires chromium installed).", action="store_true")
args = parser.parse_args()

# TODO: export to pdf, change name of output folder

markdown_file = Path(args.FILE)
export_to_pdf = args.pdf
export_to_html = not export_to_pdf

def pdf_chromium_export(index_html_path : Path, output_pdf_path : Path):
    command = [
        'chromium',
        '--headless',
        '--print-to-pdf={}'.format(output_pdf_path),
        index_html_path.resolve().as_uri()+'?print-pdf',
    ]
    subprocess.run(command)

magic_word = "DATA"
options_word = "Reveal.initialize({"
theme_word = '<link rel="stylesheet" href="dist/theme'
code_theme_word = '<link rel="stylesheet" href="plugin/highlight'

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

revealjs_zip = Path("./reveal.js.zip")
revealjs_dir = Path("./reveal.js")
index_file_original = revealjs_dir / "index.html"
index_file_new = revealjs_dir / "index.html"

slide_delimitator = "!!!"
comment_char = "%"

default_attributes = ""
default_theme = "black"
default_code_theme = "monokai"

# Open markdown file
with open(markdown_file) as f: presentation_markdown = list(f)

# Build presentation
presentation = list()
slide = list()
options = list()
theme = default_theme
code_theme = default_code_theme
attributes = default_attributes
for l in presentation_markdown:
    #l = l.strip()
    l = l[:-1]

    m = option_re.match(l)
    if m is not None:
        options.append("{} : {},".format(m.group(1), m.group(2)))
        continue

    m = delimiter_re.match(l)
    if m is not None:
        attributes = default_attributes + " " + m.group(1)
        presentation.append(section_template.format(attributes, "\n".join(slide)))
        slide = list()
        continue

    m = theme_re.match(l)
    if m is not None:
        theme = m.group(1)
        continue

    m = code_theme_re.match(l)
    if m is not None:
        code_theme = m.group(1)
        continue

    slide.append(l)

if len(slide) > 0:
    presentation.append(section_template.format(attributes, "".join(slide)))

# Replacement strings
presentation = "\n".join(presentation + [""])
options = "\n".join([options_word] + options + [""])
theme = theme_template.format(theme)
code_theme = code_theme_template.format(code_theme)

# Extract zip
shutil.rmtree(revealjs_dir, ignore_errors=True)
with ZipFile(revealjs_zip) as revealjs:
    revealjs.extractall(path=revealjs_dir)

# Read html
with open(index_file_original, "r") as f:
    index_html = list(f)

# Replace theme
index_html = [l if theme_word not in l else theme for l in index_html]
# Replace code theme
index_html = [l if code_theme_word not in l else code_theme for l in index_html]
# Replace presentation
index_html = [l if magic_word not in l else presentation for l in index_html]
# Replace options
index_html = [l if options_word not in l else options for l in index_html]

with open(index_file_new, "w") as f:
    f.write("".join(index_html))

# Copy include files
for path in [Path(p) for p in args.include]:
    if path.is_dir:
        shutil.copytree(path, revealjs_dir/path.parts[-1])
    else:
        shutil.copy(path, revealjs_dir/path.parts[-1])

# Export to PDF if needed
if export_to_pdf:
    try:
        pdf_chromium_export(index_file_new, markdown_file.with_suffix('.pdf'))
        print("Wrote {}".format(markdown_file.with_suffix('.pdf')))

    except Exception as e:
        print("Chromium exporting failed")
        print(e)
        print("Make sure chromium is installed and in your path")

if export_to_html:
    # Change output folder name
    revealjs_new_dir = markdown_file.parent/markdown_file.with_suffix('')
    shutil.rmtree(revealjs_new_dir, ignore_errors=True)
    revealjs_dir.rename(revealjs_new_dir)
    print("Done. Open {} with your web browser".format(revealjs_new_dir/"index.html"))

if not export_to_html:
    shutil.rmtree(revealjs_dir, ignore_errors=True)
