#!/usr/bin/env python

from distutils.core import setup
import glob
from pathlib import Path

revealjsdata = glob.glob("mdslides/reveal.js/**", recursive=True)
highlightjsdata = glob.glob("mdslides/cdn-release/**", recursive=True)
katexdata = glob.glob("mdslides/KaTeX/**", recursive=True)

mdslidesdata = revealjsdata + katexdata + highlightjsdata + ["mdslides/index_template.html"]
mdslidesdata = [str(Path(p).relative_to("mdslides")) for p in mdslidesdata]

setup(name='MarkdownSlides',
      python_requires='>=3.8',
      version='1.4',
      description='Write modern slides with markdown.',
      packages=['mdslides'],
      entry_points={'console_scripts': ['mdslides=mdslides.__main__:main']},
      package_data={'mdslides': mdslidesdata},
      )
