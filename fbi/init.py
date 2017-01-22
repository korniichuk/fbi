# -*- coding: utf-8 -*-

from os import remove
from os.path import exists, expanduser, isdir, isfile, join
from shutil import rmtree
from subprocess import CalledProcessError, check_call
from sys import exit

import settings
from accessory import create_directory
from salt import create_salt

def create_private_key(private_key_abs_path):
    """Create private key.
    Input:
        private_key_abs_path -- private key abs path.

    """

    command = ["openssl", "genrsa", "-out", private_key_abs_path, "4096"]
    try:
        check_call(command, shell=False)
    except CalledProcessError as exception:
        msg = "_error_CreatePrivateKey"
        print(settings.messages[msg] % (private_key_abs_path, str(exception)))
        exit(1)
    else:
        return 0

def create_public_key(private_key_abs_path, public_key_abs_path):
    """Create public key.
    Input:
        private_key_abs_path -- private key abs path,
        public_key_abs_path -- public key abs path.

    """

    command = ["pyrsa-priv2pub", "-i", private_key_abs_path, "-o",
               public_key_abs_path]
    try:
        check_call(command, shell=False)
    except CalledProcessError as exception:
        msg = "_error_CreatePublicKey"
        print(settings.messages[msg] % (private_key_abs_path,
                public_key_abs_path, str(exception)))
        exit(1)
    else:
        return 0

def init(args):
    """Init the fbi utility"""

    mode = settings.cfg.getint("security", "mode")

    # Create keys
    keys_location_rel_path = settings.cfg.get("keys",
                                              "keys_location_rel_path")
    keys_location_abs_path = expanduser(keys_location_rel_path)
    private_key_file_name = settings.cfg.get("keys", "private_key_file_name")
    public_key_file_name = settings.cfg.get("keys", "public_key_file_name")
    private_key_abs_path = join(keys_location_abs_path, private_key_file_name)
    public_key_abs_path = join(keys_location_abs_path, public_key_file_name)
    if exists(keys_location_abs_path):
        if isdir(keys_location_abs_path):
            if exists(private_key_abs_path):
                if isfile(private_key_abs_path):
                    msg = "_ask_replace_file"
                    print(settings.messages[msg] % private_key_abs_path)
                    try:
                        answer = raw_input()
                    except NameError:
                        answer = input()
                    answer_lower = answer.strip().lower()
                    if ((answer_lower == 'y') or (answer_lower == 'yes') or
                        (answer_lower == 'yep')):
                        # Create private key
                        create_private_key(private_key_abs_path)
                        # Create public key
                        create_public_key(private_key_abs_path,
                                          public_key_abs_path)
                        # Create salt
                        create_salt()
                    else:
                        msg = "_error_InitFileExistsError"
                        print(settings.messages[msg] % private_key_abs_path)
                        exit(1)
                elif isdir(private_key_abs_path):
                    msg = "_ask_remove_dir"
                    print(settings.messages[msg] % private_key_abs_path)
                    try:
                        answer = raw_input()
                    except NameError:
                        answer = input()
                    answer_lower = answer.strip().lower()
                    if ((answer_lower == 'y') or (answer_lower == 'yes') or
                        (answer_lower == 'yep')):
                        # Remove dir
                        rmtree(private_key_abs_path)
                        msg = "_removed_dir"
                        print(settings.messages[msg] % private_key_abs_path)
                        # Create private key
                        create_private_key(private_key_abs_path)
                        # Create public key
                        create_public_key(private_key_abs_path,
                                          public_key_abs_path)
                        # Create salt
                        create_salt()
                    else:
                        msg = "_error_InitIsADirectoryError"
                        print(settings.messages[msg] % private_key_abs_path)
                        exit(1)
            else:
                # Create private key
                create_private_key(private_key_abs_path)
                # Create public key
                create_public_key(private_key_abs_path, public_key_abs_path)
                # Create salt
                create_salt()
        elif isfile(keys_location_abs_path):
            msg = "_ask_remove_keys_location"
            print(settings.messages[msg] % keys_location_abs_path)
            try:
                answer = raw_input()
            except NameError:
                answer = input()
            answer_lower = answer.strip().lower()
            if ((answer_lower == 'y') or (answer_lower == 'yes') or
                (answer_lower == 'yep')):
                remove(keys_location_abs_path)
                msg = "_removed_file"
                print(settings.messages[msg] % keys_location_abs_path)
                create_directory(keys_location_abs_path, mode)
                # Create private key
                create_private_key(private_key_abs_path)
                # Create public key
                create_public_key(private_key_abs_path, public_key_abs_path)
                # Create salt
                create_salt()
            else:
                msg = "_error_InitializationNotADirectoryError"
                print(settings.messages[msg] % keys_location_abs_path)
                exit(1)
    else:
        create_directory(keys_location_abs_path, mode)
        # Create private key
        create_private_key(private_key_abs_path)
        # Create public key
        create_public_key(private_key_abs_path, public_key_abs_path)
        # Create salt
        create_salt()
    print(settings.messages["_inited"])
    return 0
