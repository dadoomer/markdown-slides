[comment]: # (This presentation was made with markdown-slides)
[comment]: # (This is a CommonMark compliant comment. It will not be included in the presentation.)
[comment]: # (Compile this presentation with the command below)
[comment]: # (mdslides presentation.md --include media)

[comment]: # (Set the theme:)
[comment]: # (THEME = white)
[comment]: # (CODE_THEME = base16/zenburn)
[comment]: # (The list of themes is at https://revealjs.com/themes/)
[comment]: # (The list of code themes is at https://highlightjs.org/)

[comment]: # "You can also use quotes instead of parenthesis"
[comment]: # "THEME = white"

[comment]: # (Pass optional settings to reveal.js:)
[comment]: # (controls: true)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
[comment]: # (respondToHashChanges: false)
[comment]: # (Other settings are documented at https://revealjs.com/config/)

John Doe | College University | July 3, 2020

# Great Title

[comment]: # (A comment starting with three or more !!! marks a slide break.)
[comment]: # (!!!)

This is a sample presentation to showcase [markdown-slides](https://gitlab.com/da_doomer/markdown-slides). The source markdown file is [presentation.md](https://gitlab.com/da_doomer/markdown-slides/-/blob/master/example/presentation.md).

[comment]: # (!!!)

Use markdown to harness the power of Reveal.js.

[comment]: # (!!!)

## Lists and math

- Using markdown to write presentations
- Easy lists
- LaTeX math syntax

`$$ J(\theta_0,\theta_1) = \sum_{i=0} $$`

[comment]: # (!!!)

Code syntax highlighting and animations:

```js [1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```

Notice the background color change.

[comment]: # (section attributes for the just-ending slide can be specified:)
[comment]: # (!!! data-background-color="aquamarine")

Use background videos, background pictures and **text formatting**,
everything *without breaking* your markdown files.

[comment]: # (!!! data-background-video="media/video.mp4", data-background-video-loop data-background-video-muted data-background-opacity="0.2")
[comment]: # (Other background options: https://revealjs.com/backgrounds/)

## Pictures

![picture of spaghetti](media/image0.gif) <!-- .element: style="height:50vh; max-width:80vw; image-rendering: crisp-edges;" -->

Showcase media including images, videos and animations.

[comment]: # (!!!)

## Animations

- This is an example list
- Just to showcase Reveal.js' animations

[comment]: # (!!! data-auto-animate)

## Animations

- This is an example list
- Just to showcase Reveal.js' animations
- This item will be automatically faded-in

[comment]: # (!!! data-auto-animate)

```js [1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```
<!-- .element: data-id="code" -->

[comment]: # (!!! data-auto-animate)

```js [5]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
c(5);
```
<!-- .element: data-id="code" -->

Animate code as well <!-- .element: class="fragment" data-fragment-index="1" -->

[comment]: # (!!! data-auto-animate)

Insert Youtube videos.

<iframe width="560" height="315" src="https://www.youtube.com/embed/KPfzRSBzNX4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[comment]: # (!!!)

Insert local videos.

<iframe width="560" height="315" src="media/video.mp4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[comment]: # (!!!)

Download [markdown-slides](https://gitlab.com/da_doomer/markdown-slides)!

[comment]: # (!!!)

A couple more examples follow.

[comment]: # (!!!)

![logo](media/wide.png)

***use markdown to write slides***

Author Name

[comment]: # (!!!)

[comment]: # (!!! data-background-image="media/inkscape.png" data-background-size="contain")

Press down on your keyboard or swipe down.

[comment]: # (|||)

**Vertical slides!**

(thanks [@porvik!](https://gitlab.com/da_doomer/markdown-slides/-/issues/8))

[comment]: # (|||)

As many vertical slides as you like.

[comment]: # (!!!)

Add tables:

| Insert | Tables |
| ------ | ------ |
| A row  | Another|
| text   | more   |

[comment]: # (!!!)

## Vertical separator

----------

Some other text.

[comment]: # (!!!)

You can also use in-line HTML.

<div style="font-size: 1em;">
small
</div>

<div style="font-size: 5em;">
large
</div>
