% This is a comment. It will not be included in the presentation.
%
% Set the theme:
% THEME = white
% CODE_THEME = zenburn
%
% You can pass options to reveal.js like below:
% controls: false
% keyboard: true
% markdown: { smartypants: true }
% hash: false
%
% Compile the presentation with --include media

John Doe | College University | July 3, 2020

# Great Title

% Three or more tildes mark a slide break.
~~~

## Great advances

- Progress is being made
- A nice equation was proposed

`$$ J(\theta_0,\theta_1) = \sum_{i=0} $$`

~~~

Code has insights we must explain:

```js [1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```

% section attributes for the just-ending slide can be specified:
~~~ data-background-color="aquamarine"


We are justifying the background video, as it is an important feature
of **our** work, and *we can even write more*.

~~~ data-background-video="media/video.mp4", data-background-video-loop data-background-video-muted data-background-opacity="0.2"

## Results

![picture of spaghetti](media/image0.gif) <!-- .element: style="height:50vw; image-rendering: crisp-edges;" -->

The image caption.

~~~

More details will be in the paper, but we can still write a little bit of text here.

Just be sure to not bore your audience too much, as this is just an example
presentation without any real content. The goal is to show how it is displayed,
even though its source code is easy to read.

~~~

## Conclusions

- We found interesting things
- It is possible to find things

~~~ data-auto-animate

## Conclusions

- We found interesting things
- It is possible to find things
- We discovered stuff

~~~ data-auto-animate

```js [1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```
<!-- .element: data-id="code" -->

~~~ data-auto-animate

```js [5]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
c(5);
```
<!-- .element: data-id="code" -->

We changed the code <!-- .element: class="fragment" data-fragment-index="1" -->

~~~ data-auto-animate
