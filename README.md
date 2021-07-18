![logo](logos/wide.png)

**Using markdown, write simple but beautiful presentations with math,
animations and media, which can be visualized in a web browser even without
an internet connection, or exported to PDF.**

See the official [git repository hosted on Gitlab](https://gitlab.com/da_doomer/markdown-slides) or the [Github mirror](https://github.com/dadoomer/markdown-slides).

This program appropriately inserts markdown files into Reveal.js files,
completely avoiding the need to edit HTML files directly.

# Live demo

**See for yourself**: check out the [live demo](https://da_doomer.gitlab.io/markdown-slides) (and the source file [`presentation.md`](example/presentation.md)).

![](https://user-images.githubusercontent.com/122831/126051928-0209a791-3846-4e61-aae7-8ca0dcc9f41a.png)

# Installation

```bash
python -m pip install git+https://gitlab.com/da_doomer/markdown-slides.git
```

Don't have python? Your version of python not working?

Here's a fearless, conflict-free python install that Just Works™ on a bash shell:

```bash
curl -sS https://webinstall.dev/pyenv | bash
export PATH=~/.pyenv/bin:"$PATH"
export PATH=~/.pyenv/shims:"$PATH"
```

```bash
# Install v3.9.1, which works with mdslides
pyenv install -v 3.9.1

# Switch to python 3.9.1, conflict free
pyenv global 3.9.1

# Install and use mdslides

# Switch to your original system python
pyenv global system
```

# Usage

```bash
mdslides [-h] [--include RESOURCE] [--pdf] FILE
```

where

- `RESOURCE`: any file or directory that should be included (e.g. a directory with pictures and videos)

- `FILE`: input markdown file.

Notes:

 - PDF exporting requires chromium (see [PDF exporting on
	 reveal-js](https://revealjs.com/pdf-export/)).


## QuickStart Example

1. Download the example [presentation.md](https://raw.githubusercontent.com/dadoomer/markdown-slides/master/example/presentation.md) folder.
   ```bash
    wget "https://gitlab.com/da_doomer/markdown-slides/-/archive/master/markdown-slides-master.zip?path=example"; unzip markdown-slides-master.zip\?path=example; cd markdown-slides-master-example/example;
   ```
2. Render the slide deck into a web page
   ```bash
   mdslides ./presentation.md
   ```
3. Open the slides in your browser (or publish to github pages)
   ```bash
   open ./presentation/index.html
   ```

# Syntax:

You will probably only need to break slides:

```md
# My title
A subtitle maybe

[comment]: # (!!!)

Second slide. Easy :D
```

Other options are documented in the example presentation [`presentation.md`](example/presentation.md).

If you need a quick refresher on markdown see e.g.
[this cheatsheet](https://www.markdownguide.org/cheat-sheet/), the
[CommonMark reference page](https://commonmark.org/help/), or this
[Gfm tutorial](https://guides.github.com/features/mastering-markdown/).

You will not have to break your markdown files to use this program. Control
Reveal.js' theme and options using CommonMark-compliant comments.

Everything but slide-break comments and option comments is passed to Reveal.js verbatim. Check out their documentation, especially the [markdown section](https://revealjs.com/markdown/).

# Features

Some of Reveal.js's features are:

- LaTeX math syntax.
- Automatic animations.
- Background videos and images.

Everything is bundled in this repository so web browsers do not need internet
connection to display the presentations.

# Troubleshooting

If you encounter any issues or have some questions, open an [issue on Gitlab](https://gitlab.com/da_doomer/markdown-slides/-/issues) or [on Github](https://github.com/dadoomer/markdown-slides/issues).
