# -*- coding: utf-8 -*-

from os.path import expanduser

from fabric.api import local

def test_encode():
    """Test encode command"""

    rel_path = ".key/netezza.enc"
    tilde_path = "~/.key/netezza.enc"
    abs_path = expanduser(tilde_path)

    # No public key --> ask init fbi --> n
    print("Encode. No public key --> ask init fbi --> n:")
    local("rm -r --force ~/.ssh")
    try:
        local("echo 'n' | fbi encode %s" % abs_path)
    except BaseException:
        pass
    try:
        local("echo 'n' | fbi encode %s" % tilde_path)
    except BaseException:
        pass
    try:
        local("cd ~; echo 'n' | fbi encode %s" % rel_path)
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("clear")
    # No public key --> ask init fbi --> y --> no cipher location
    print("Encode. No public key --> ask init fbi --> y --> " \
          "no cipher location:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("echo 'y' | fbi encode %s" % abs_path) # TODO
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("echo 'y' | fbi encode %s" % tilde_path) # TODO
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("cd ~; echo 'y' | fbi encode %s" % rel_path) # TODO
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    # Public key file --> cipher location dir --> cipher file --> 
    # ask replace file --> n
    print("Encode. Public key file --> cipher location dir --> " \
          "cipher file --> ask replace file --> n:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("fbi init")
    local("mkdir --parents ~/.key")
    local("touch %s" % abs_path)
    try:
        local("echo 'n' | fbi encode %s" % abs_path)
    except BaseException:
        pass
    try:
        local("echo 'n' | fbi encode %s" % tilde_path)
    except BaseException:
        pass
    try:
        local("cd ~; echo 'n' | fbi encode %s" % rel_path)
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    # Public key file --> cipher location dir --> cipher file -->
    # ask replace file --> y
    print("Encode. Public key file --> cipher location dir --> " \
          "cipher file --> ask replace file --> y:")
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("fbi init")
    local("mkdir --parents ~/.key")
    local("touch %s" % abs_path)
    local("echo 'y' | fbi encode %s" % abs_path) # TODO
    local("echo 'y' | fbi encode %s" % tilde_path) # TODO
    local("cd ~; echo 'y' | fbi encode %s" % rel_path) # TODO
    local("rm -r --force ~/.ssh")
    local("rm -r --force ~/.key")
    local("clear")
    return 0
