# -*- coding: utf-8 -*-

from os.path import expanduser

from fabric.api import local
from keys import getpassword

def test_getpassword():
    """Test getpassword method"""

    rel_path = ".key/netezza.enc"
    tilde_path = "~/.key/netezza.enc"
    abs_path = expanduser(tilde_path)

    # getpassword() --> no cipher file --> _error_NoCipher
    print("getpassword() --> no cipher file --> _error_NoCipher")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    try:
        passwd = getpassword(tilde_path)
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    # getpassword() --> cipher file --> no private key --> _error_NoPrivateKey
    print("getpassword() --> cipher file --> no private key --> "
          "_error_NoPrivateKey")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("keys init")
    local("keys encode %s" % abs_path) # TODO
    local("rm -r --force ~/.ssh")
    try:
        passwd = getpassword(tilde_path)
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    # getpassword() --> wrong cipher file --> private key --> 
    # _error_DecryptionError
    print("getpassword() --> wrong cipher file --> private key --> " \
          "_error_DecryptionError")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("keys init")
    local("mkdir --parents ~/.key")
    local("touch %s" % abs_path)
    try:
        passwd = getpassword(tilde_path)
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    # getpassword() --> cipher file --> private key
    print("getpassword() --> cipher file --> private key:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("keys init")
    local("keys encode %s" % abs_path) # TODO
    passwd = getpassword(tilde_path)
    passwd = getpassword(abs_path)
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    return 0
