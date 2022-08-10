![logo](logos/wide.png)

**Using markdown, write simple but beautiful presentations with math,
animations and media, which can be visualized in a web browser or exported to
PDF.**

See the official [git repository hosted on Gitlab](https://gitlab.com/da_doomer/markdown-slides) or the [Github mirror](https://github.com/dadoomer/markdown-slides).

This program appropriately inserts markdown files into Reveal.js files,
completely avoiding the need to edit HTML files directly.

# Live demo

**See for yourself**: check out the [live demo](https://da_doomer.gitlab.io/markdown-slides) (and the source file [`presentation.md`](example/presentation.md)).

![](https://user-images.githubusercontent.com/122831/126127604-45c8d817-560a-4d88-9344-7767777d8a83.gif)

# Installation

```bash
python -m pip install git+https://gitlab.com/da_doomer/markdown-slides.git
```

Markdown-slides works with Python >= 3.8.

Don't have python? Your version of python not working? Scroll down to [fearless, conflict-free Python installation](#fearless-conflict-free-python-installation).

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

1. Install markdown-slides

2. Download the example [presentation.md](https://raw.githubusercontent.com/dadoomer/markdown-slides/master/example/presentation.md) folder
   ```bash
    wget "https://gitlab.com/da_doomer/markdown-slides/-/archive/master/markdown-slides-master.zip?path=example"; unzip markdown-slides-master.zip\?path=example; cd markdown-slides-master-example/example;
   ```
3. Render the slide deck into a web page, including the `media` folder
   ```bash
   mdslides ./presentation.md --include media
   ```
4. Open the slides in your browser (or publish to github pages)
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

Keep in mind you need an Internet connection to render equations (see [issue #9](https://gitlab.com/da_doomer/markdown-slides/-/issues/9)).

# Troubleshooting

If you encounter any issues or have some questions, open an [issue on Gitlab](https://gitlab.com/da_doomer/markdown-slides/-/issues) or [on Github](https://github.com/dadoomer/markdown-slides/issues).

Comments and pull requests are very welcome!

## Fearless, Conflict-free Python installation

Markdown-slides works with Python 3.9 or newer.

Here's a fearless, conflict-free python install that Just Works™ in bash, zsh, and fish:

1. [Webi](https://webinstall.dev) will install `pyenv` (the python version manager) to `~/.pyenv`, where it won't conflict with your system python, or any projects:
   ```bash
   curl -sS https://webinstall.dev/pyenv | bash
   ```
2. After installation you'll need to **CLOSE and RE-OPEN** your terminal, or update your `PATH`:
   ```bash
   export PATH=~/.pyenv/bin:"$PATH"
   export PATH=~/.pyenv/shims:"$PATH"
   ```
3. Now you can install Python v3.9.1 (safely in `~/.pyenv`):
   ```bash
   # Install v3.9.1, which works with mdslides
   pyenv install -v 3.9.1
   ```
4. When you need to use `mdslides`, use `pyenv` to set your SHELL's python to 3.9.1:
   (and you can set it right back afterwards)
   ```bash
   # Switch to python 3.9.1, conflict free
   pyenv global 3.9.1

   # Install and use mdslides

   # Switch to your original system python
   pyenv global system
   ```

**Bonus**: You can tell `pyenv` to automatically pick Python 3.9.1 whenever you're in your slides folder:

```bash
cd ./path/to/my/presentations/
pyenv local 3.9.1

# the presentations folder is now set to use python 3.9.1
cat ./.python-version # 3.9.1
python --version
Python 3.9.1

cd -
python --version
Python x.x.x
```
