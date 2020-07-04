Write presentations using markdown and export them to a portable HTML format
with Reveal.js. This program appropriately inserts markdown files into
Reveal.js files, completely avoiding the need to edit HTML files directly.

# Usage:

You will not have to break your markdown files to use this program: metadata
is read from CommonMark compliant comment lines:

```md
[comment]: # (This is a CommonMark compliant comment. It will not be included in the presentation.)

# A nice title

Normal *markdown* stuff. Using this program is as simple as inserting slide
breaks. Below is a slide break.

[comment:] (!!!)

Continue writing markdown as usual, maybe even some nice equations:

`$$f(x) = 2^x$$`
```

You can also control Reveal.js options using comments:

```md
[comment]: # (Set the theme:)
[comment]: # (THEME = white)
[comment]: # (CODE_THEME = white)

[comment]: # (Pass optional settings to reveal.js:)
[comment]: # (controls: false)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
```

Everything but slide-break comments and option comments is passed to Reveal.js verbatim. Check out their documentation, especially the [markdown
section](https://revealjs.com/markdown/). Review the accompanying
`presentation.md` for a quick introduction.

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
