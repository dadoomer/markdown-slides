#!/bin/python3.8
from pathlib import Path
import argparse
from zipfile import ZipFile
import shutil

parser = argparse.ArgumentParser(description='Convert a markdown file to a reveal.js presentation.')
parser.add_argument('FILE', type=str, help="Markdown file.")
parser.add_argument('--include', metavar="RESOURCE", help="Directory or file to include. This option can be used multiple times.", default=[], action="append")
args = parser.parse_args()

markdown_file = Path(args.FILE)

magic_word = "DATA"
options_word = "Reveal.initialize({"
theme_word = '<link rel="stylesheet" href="dist/theme'
code_theme_word = '<link rel="stylesheet" href="plugin/highlight'

section_template = "<section data-markdown {}><textarea data-template>\n{}\n</textarea></section>"
#section_template = "<section data-markdown {}>\n{}\n</section>"
theme_template = '<link rel="stylesheet" href="dist/theme/{}.css" id="theme">'
code_theme_template = '<link rel="stylesheet" href="plugin/highlight/{}.css" id="highlight-theme">'

revealjs_zip = Path("./reveal.js.zip")
revealjs_dir = Path("./reveal.js")
index_file_original = revealjs_dir / "index.html"
index_file_new = revealjs_dir / "index.html"

slide_delimitator = "~~~"
comment_char = "%"

default_attributes = ""
default_theme = "black"
default_code_theme = "monokai"

# Open markdown file
with open(markdown_file) as f: presentation_markdown = list(f)

# Build presentation
def de_comment(l):
    i = 0
    while i < len(l) and l[i] == comment_char: i+=1
    return l[i:]

def de_delimitate(l):
    i = 0
    while i < len(l) and l[i] == slide_delimitator[0]: i+=1
    return l[i:]

def get_value(l):
    return l.split("=")[-1]

def is_comment(l):
    return len(l) > 0 and l[0] == comment_char

def is_option(l):
    l = l.strip()
    return is_comment(l) and "" not in set(l.split(":")) and len(l.split(":")) >= 2

def is_theme(l):
    return "THEME" in l

def is_code_theme(l):
    return "CODE_THEME" in l

presentation = list()
slide = list()
options = list()
theme = default_theme
code_theme = default_code_theme
for l in presentation_markdown:
    if is_code_theme(l):
        code_theme = get_value(l).strip()
        continue

    if is_theme(l):
        theme = get_value(l).strip()
        continue

    if is_option(l):
        options.append(de_comment(l).strip()+",")
        continue

    if is_comment(l):
        continue

    if slide_delimitator in l:
        attributes = " ".join(de_delimitate(l).strip().split(","))
        presentation.append(section_template.format(attributes, "".join(slide)))
        slide = list()
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
