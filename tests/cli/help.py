# -*- coding: utf-8 -*-

from fabric.api import local

def test_help():
    """Test the standard output for –help"""

    local("fbi")
    local("clear")
    local("fbi -h")
    local("clear")
    local("fbi --help")
    local("clear")
    local("fbi decode -h")
    local("clear")
    local("fbi decode --help")
    local("clear")
    local("fbi encode -h")
    local("clear")
    local("fbi encode --help")
    local("clear")
    local("fbi init -h")
    local("clear")
    local("fbi init --help")
    local("clear")
    return 0
