# -*- coding: utf-8 -*-

from os.path import exists, expanduser, isfile, join
from sys import exit

import rsa

import settings
from accessory import get_abs_path
from salt import get_salt

def decode(args):
    """Decode password from a file"""

    path = args.path[0]

    # Prepare cipher abs path
    cipher_abs_path = get_abs_path(path)
    # Read cipher
    if exists(cipher_abs_path) and isfile(cipher_abs_path):
        with open(cipher_abs_path, 'r') as f:
            cipher = f.read()
    else:
        print(settings.messages["_error_NoCipher"] % cipher_abs_path)
        exit(1)
    # Read private_key
    keys_location_rel_path = settings.cfg.get("keys",
                                              "keys_location_rel_path")
    keys_location_abs_path = expanduser(keys_location_rel_path)
    private_key_file_name = settings.cfg.get("keys", "private_key_file_name")
    private_key_abs_path = join(keys_location_abs_path, private_key_file_name)
    if exists(private_key_abs_path) and isfile(private_key_abs_path):
        with open(private_key_abs_path, 'r') as f:
            private_key_data = f.read()
            private_key = rsa.PrivateKey.load_pkcs1(private_key_data)
    else:
        print(settings.messages["_error_NoPrivateKey"] % private_key_abs_path)
        exit(1)
    # Read salt
    salt = get_salt()
    # Decode cipher
    try:
        data = rsa.decrypt(cipher, private_key)
    except Exception:
        print(settings.messages["_error_DecodeError"] % (cipher_abs_path,
                                                private_key_abs_path))
        exit(1)
    else:
        passwd = data[len(salt):]
        print(settings.messages["_decoded"] % (cipher_abs_path,
                                               private_key_abs_path))
        print(settings.messages["_passwd"] % passwd)
        return 0
