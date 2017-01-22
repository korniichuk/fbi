# -*- coding: utf-8 -*-

from fabric.api import local

def test_version():
    """"Test the standard output for –version"""

    local("keys -v")
    local("clear")
    local("keys --version")
    local("clear")
    return 0
