# -*- coding: utf-8 -*-

from fabric.api import local

def test_help():
    """Test the standard output for –help"""

    local("keys")
    local("clear")
    local("keys -h")
    local("clear")
    local("keys --help")
    local("clear")
    local("keys decode -h")
    local("clear")
    local("keys decode --help")
    local("clear")
    local("keys encode -h")
    local("clear")
    local("keys encode --help")
    local("clear")
    local("keys init -h")
    local("clear")
    local("keys init --help")
    local("clear")
    return 0
