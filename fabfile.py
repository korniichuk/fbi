#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""The fbi utility fabric file"""

from fabric.api import local

def git():
    """Setup Git"""

    local("git remote rm origin")
    local("git remote add origin https://korniichuk@" \
          "github.com/korniichuk/fbi.git")

def live():
    """Upload package to PyPI Live"""

    local("python setup.py register -r pypi")
    local("python setup.py sdist --format=gztar upload -r pypi")

def test():
    """Upload package to PyPI Test"""

    local("python setup.py register -r pypitest")
    local("python setup.py sdist --format=gztar upload -r pypitest")
