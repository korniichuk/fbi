# -*- coding: utf-8 -*-

from fabric.api import local

def test_init():
    """Test init command"""

    # No keys location
    print("Init. No keys location:")
    local("rm -r --force ~/.ssh")
    local("fbi init")
    local("rm -r --force ~/.ssh")
    local("clear")
    # Keys location dir --> private key file --> ask replace file --> y
    print("Init. Keys location dir --> private key file --> " \
          "ask replace file --> y:")
    local("rm -r --force ~/.ssh")
    local("fbi init")
    local("echo 'y' | fbi init")
    local("rm -r --force ~/.ssh")
    local("clear")
    # Keys location dir --> private key file --> ask replace file --> n
    print("Init. Keys location dir --> private key file --> " \
          "ask replace file --> n:")
    local("rm -r --force ~/.ssh")
    local("fbi init")
    try:
        local("echo 'n' | fbi init")
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("clear")
    # Keys location dir --> private key dir --> ask remove dir --> y
    print("Init. Keys location dir --> private key dir --> " \
          "ask remove dir --> y:")
    local("rm -r --force ~/.ssh")
    local("fbi init")
    local("rm -r --force ~/.ssh/private")
    local("mkdir --parents ~/.ssh/private")
    local("echo 'y' | fbi init")
    local("rm -r --force ~/.ssh")
    local("clear")
    # Keys location dir --> private key dir --> ask remove dir --> n
    print("Init. Keys location dir --> private key dir --> " \
          "ask remove dir --> n:")
    local("rm -r --force ~/.ssh")
    local("fbi init")
    local("rm -r --force ~/.ssh/private")
    local("mkdir --parents ~/.ssh/private")
    try:
        local("echo 'n' | fbi init")
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("clear")
    # Keys location file --> ask remove keys location --> y
    print("Init. Keys location file --> ask remove keys location --> y:")
    local("rm -r --force ~/.ssh")
    local("touch ~/.ssh")
    local("echo 'y' | fbi init")
    local("rm -r --force ~/.ssh")
    local("clear")
    # Keys location file --> ask remove keys location --> n
    print("Init. Keys location file --> ask remove keys location --> n:")
    local("rm -r --force ~/.ssh")
    local("touch ~/.ssh")
    try:
        local("echo 'n' | fbi init")
    except BaseException:
        pass
    local("rm -r --force ~/.ssh")
    local("clear")
    return 0
