#!/usr/bin/env python

from distutils.core import setup
import glob
from pathlib import Path

revealjsdata = glob.glob("mdslides/reveal.js/**", recursive=True)
revealjsdata = [str(Path(p).relative_to("mdslides")) for p in revealjsdata]

setup(name='MarkdownSlides',
      version='1.1',
      description='Write modern slides with markdown.',
      packages=['mdslides'],
      entry_points={'console_scripts': ['mdslides=mdslides.__main__:main']},
      package_data={'mdslides': revealjsdata},
      )
