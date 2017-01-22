# -*- coding: utf-8 -*-

from getpass import getpass
from os import chmod, remove
from os.path import dirname, exists, expanduser, isdir, isfile, join
from shutil import rmtree
from sys import exit

import rsa

import settings
from accessory import create_directory, get_abs_path
from init import init
from salt import get_salt

def create_cipher(public_key, cipher_abs_path, mode):
    """Create cipher"""

    # Ask password
    passwd = getpass(settings.messages["_ask_passwd"])
    # Read salt
    salt = get_salt()
    # Prepare cipher
    data = salt + passwd
    cipher = rsa.encrypt(data, public_key)
    # Write cipher
    with open(cipher_abs_path, 'w') as f:
        f.write(cipher)
    # Set access permissions to cipher
    chmod(cipher_abs_path, mode)

def encode(args):
    """Encode password in a file"""

    path = args.path[0]
    mode = settings.cfg.getint("security", "mode")

    # Prepare public key
    public_key, public_key_abs_path = get_public_key(args)
    # Prepare cipher abs path
    cipher_abs_path = get_abs_path(path)
    cipher_location = dirname(cipher_abs_path)
    if exists(cipher_location):
        if isdir(cipher_location):
            if exists(cipher_abs_path):
                if isfile(cipher_abs_path):
                    msg = "_ask_replace_file"
                    print(settings.messages[msg] % cipher_abs_path)
                    try:
                        answer = raw_input()
                    except NameError:
                        answer = input()
                    answer_lower = answer.strip().lower()
                    if ((answer_lower == 'y') or (answer_lower == 'yes') or
                        (answer_lower == 'yep')):
                        # Create cipher
                        create_cipher(public_key, cipher_abs_path, mode)
                    else:
                        msg = "_error_EncodeFileExistsError"
                        print(settings.messages[msg] % cipher_abs_path)
                        exit(1)
                elif isdir(cipher_abs_path):
                    msg = "_ask_remove_dir"
                    print(settings.messages[msg] % cipher_abs_path)
                    try:
                        answer = raw_input()
                    except NameError:
                        answer = input()
                    answer_lower = answer.strip().lower()
                    if ((answer_lower == 'y') or (answer_lower == 'yes') or
                        (answer_lower == 'yep')):
                        # Remove dir
                        rmtree(cipher_abs_path)
                        msg = "_removed_dir"
                        print(settings.messages[msg] % cipher_abs_path)
                        # Create cipher
                        create_cipher(public_key, cipher_abs_path, mode)
                    else:
                        msg = "_error_EncodeIsADirectoryError"
                        print(settings.messages[msg] % cipher_abs_path)
                        exit(1)
            else:
                # Create cipher
                create_cipher(public_key, cipher_abs_path, mode)
        elif isfile(cipher_location):
            # Cipher location is not a directory
            msg = "_ask_remove_cipher_location"
            print(settings.messages[msg] % cipher_location)
            try:
                answer = raw_input()
            except NameError:
                answer = input()
            answer_lower = answer.strip().lower()
            if ((answer_lower == 'y') or (answer_lower == 'yes') or
                (answer_lower == 'yep')):
                remove(cipher_location)
                print(settings.messages["_removed_file"] % cipher_location)
                # Create cipher location dir
                create_directory(cipher_location, mode, messages)
                # Create cipher
                create_cipher(public_key, cipher_abs_path, mode)
            else:
                msg = "_error_EncodeNotADirectoryError"
                print(settings.messages[msg] % cipher_location)
                exit(1)
    else:
        # Create cipher location dir
        create_directory(cipher_location, mode)
        # Create cipher
        create_cipher(public_key, cipher_abs_path, mode)
    msg = "_encoded"
    print(settings.messages[msg] % (cipher_abs_path, public_key_abs_path))
    return 0

def get_public_key(args):
    """Get public key"""

    keys_location_rel_path = settings.cfg.get("keys",
                                              "keys_location_rel_path")
    keys_location_abs_path = expanduser(keys_location_rel_path)
    public_key_file_name = settings.cfg.get("keys", "public_key_file_name")
    public_key_abs_path = join(keys_location_abs_path, public_key_file_name)
    if exists(public_key_abs_path) and isfile(public_key_abs_path):
        with open(public_key_abs_path, 'r') as f:
            public_key_data = f.read()
            public_key = rsa.PublicKey.load_pkcs1(public_key_data)
        return public_key, public_key_abs_path
    else:
        print(settings.messages["_ask_init_fbi_utility"])
        try:
            answer = raw_input()
        except NameError:
            answer = input()
        answer_lower = answer.strip().lower()
        if ((answer_lower == 'y') or (answer_lower == 'yes') or
            (answer_lower == 'yep')):
            # Init the fbi utility
            init(args)
            with open(public_key_abs_path, 'r') as f:
                public_key_data = f.read()
                public_key = rsa.PublicKey.load_pkcs1(public_key_data)
            return public_key, public_key_abs_path
        else:
            print(settings.messages["_error_EncodeFbiUtilityNotInited"])
            exit(1)
