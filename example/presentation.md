[comment]: # (This presentation was made with markdown-slides)
[comment]: # (This is a CommonMark compliant comment. It will not be included in the presentation.)
[comment]: # (Compile this presentation with --include media)

[comment]: # (Set the theme:)
[comment]: # (THEME = white)
[comment]: # (CODE_THEME = zenburn)

[comment]: # (Pass optional settings to reveal.js:)
[comment]: # (controls: false)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
[comment]: # (respondToHashChanges: false)

John Doe | College University | July 3, 2020

# Great Title

[comment]: # (A comment starting with three or more !!! marks a slide break.)
[comment]: # (!!!)

This presentation was made with [markdown-slides](https://gitlab.com/da_doomer/markdown-slides).

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

Use background videos and **text formatting**,
everything *without breaking* your markdown files.

[comment]: # (!!! data-background-video="media/video.mp4", data-background-video-loop data-background-video-muted data-background-opacity="0.2")

## Pictures

![picture of spaghetti](media/image0.gif) <!-- .element: style="height:30vw; image-rendering: crisp-edges;" -->

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