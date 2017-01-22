# -*- coding: utf-8 -*-

import random
from os import chmod
from os.path import expanduser, join

import settings

def create_salt():
    """Create salt"""

    # Prepare salt
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt_length = settings.cfg.getint("salt", "salt_length")
    salt = ''.join([random.choice(alphabet) for i in range(salt_length)])
    # Write salt
    salt_location_rel_path = settings.cfg.get("salt", "salt_location_rel_path")
    salt_location_abs_path = expanduser(salt_location_rel_path)
    salt_file_name = settings.cfg.get("salt", "salt_file_name")
    salt_abs_path = join(salt_location_abs_path, salt_file_name)
    with open(salt_abs_path, 'w') as f:
        f.write(salt)
    # Set access permissions to salt
    mode = settings.cfg.getint("security", "mode")
    chmod(salt_abs_path, mode)
    return 0

def get_salt():
    """Get salt"""

    salt_location_rel_path = settings.cfg.get("salt", "salt_location_rel_path")
    salt_location_abs_path = expanduser(salt_location_rel_path)
    salt_file_name = settings.cfg.get("salt", "salt_file_name")
    salt_abs_path = join(salt_location_abs_path, salt_file_name)
    with open(salt_abs_path, 'r') as f:
        salt = f.read()
    return salt
