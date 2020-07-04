Write presentations using markdown and export them to a portable HTML format
with Reveal.js. This program appropriately inserts markdown files into
Reveal.js files, completely avoiding the need to edit HTML files directly.

# Usage:

Markdown as usual, except:

- Use `!!!` to mark slide breaks.
- Comments are marked with `%`.
- Options for Reveal.js are defined with `% option: value`.
- The theme and code themes are specified like so: `% THEME = white`, `% CODE_THEME = zenburn`.

Everything else is passed to Reveal.js verbatim so check out their documentation,
specially the [markdown section](https://revealjs.com/markdown/). Check the
accompanying `presentation.md` for a quick introduction.

# Features

Some of Reveal.js's features are:

- LaTeX syntax.
- Automatic animations.
- Background videos and images.

MathJax is bundled in this repository, so web browsers do not need internet
connection to display the presentations.

# Instructions

1. Clone the repository.
2. Run the program with your own markdown file. You can use `--include F` to
include files or folders with media.
3. Open `reveal.js/index.html` in a web browser.

For example, to compile the example presentation:

```
git clone https://gitlab.com/da_doomer/markdown-revealjs-presentation.git
cd markdown-revealjs-presentation
python make.py presentation.md --include media
```
