# -*- coding: utf-8 -*-

from ConfigParser import RawConfigParser
from os.path import exists, isdir, join
from site import getsitepackages

def create_dictionary(file_abs_path):
    """Create dictionary.
    Input:
        file_abs_path -- file abs path.
    Output:
        dictionary -- dictionary.

    """

    dictionary = {}

    with open(file_abs_path, 'r') as f:
        lines = f.read().splitlines()
    for i in range(0, len(lines), 2):
        dictionary[lines[i]] = lines[i+1]
    return dictionary

def init():
    """Inint vars"""

    global argparse # Strings for -h --help
    global cfg # cfg obj
    global messages # Strings for output

    # Create cfg obj
    module_name = "fbi"
    for dir_path in getsitepackages():
        module_location = join(dir_path, module_name)
        if exists(module_location) and isdir(module_location):
            break
    fbi_cfg_abs_path = join(module_location, "config/fbi.cfg")
    cfg = RawConfigParser()
    cfg.read(fbi_cfg_abs_path)
    # Create argparse dict
    config_argparse_rel_path = cfg.get("main", "config_argparse_rel_path")
    config_argparse_abs_path = join(module_location, config_argparse_rel_path)
    argparse = create_dictionary(config_argparse_abs_path)
    # Create messages dict
    config_messages_rel_path = cfg.get("main", "config_messages_rel_path")
    config_messages_abs_path = join(module_location, config_messages_rel_path)
    messages = create_dictionary(config_messages_abs_path)
