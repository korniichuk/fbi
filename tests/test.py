#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local

from cli.decode import test_decode
from cli.encode import test_encode
from cli.help import test_help
from cli.init import test_init
from cli.version import test_version
from client.getpassword import test_getpassword

def main():
    """Main function"""

    test_help()
    test_version()
    test_init()
    test_encode()
    test_decode()
    test_getpassword()
    print("Success.")

main()
