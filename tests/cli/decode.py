# -*- coding: utf-8 -*-

from os.path import expanduser

from fabric.api import local

def test_decode():
    """Test decode command"""

    rel_path = ".key/netezza.enc"
    tilde_path = "~/.key/netezza.enc"
    abs_path = expanduser(tilde_path)

    # No cipher file --> _error_NoCipher
    print("Decode. No cipher file --> _error_NoCipher:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    try:
        local("keys decode %s" % abs_path)
    except BaseException:
        pass
    try:
        local("keys decode %s" % tilde_path)
    except BaseException:
        pass
    try:
        local("cd ~; keys decode %s" % rel_path)
    except BaseException:
        pass
    local("clear")
    # Cipher file --> no private key --> _error_NoPrivateKey
    print("Decode. Cipher file --> no private key --> _error_NoPrivateKey:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("keys init")
    local("keys encode %s" % abs_path) # TODO
    local("rm -r --force ~/.ssh")
    try:
        local("keys decode %s" % abs_path)
    except BaseException:
        pass
    local("rm -r --force ~/.key")
    local("clear")
    # Wrong cipher file --> private key --> _error_DecryptionError
    print("Decode. Wrong cipher file --> private key --> " \
          "_error_DecryptionError:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("keys init")
    local("mkdir --parents ~/.key")
    local("touch %s" % abs_path)
    try:
        local("keys decode %s" % abs_path)
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    # Cipher file --> private key
    print("Decode. Cipher file --> private key:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("keys init")
    local("keys encode %s" % abs_path) # TODO
    local("keys decode %s" % abs_path)
    local("keys decode %s" % tilde_path)
    local("cd ~; keys decode %s" % rel_path)
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    return 0
