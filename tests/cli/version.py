# -*- coding: utf-8 -*-

from fabric.api import local

def test_version():
    """"Test the standard output for –version"""

    local("fbi -v")
    local("clear")
    local("fbi --version")
    local("clear")
    return 0
