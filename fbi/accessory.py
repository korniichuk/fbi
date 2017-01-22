# -*- coding: utf-8 -*-

from errno import EACCES, ENOTDIR
from os import getcwd, makedirs, remove, strerror
from os.path import dirname, expanduser, isfile, join

import settings

def create_directory(dir_abs_path, mode=None):
    """Recursive directory creation function
    os.chmod work only for last directory

    """

    if mode == None:
        mode = settings.cfg.getint("security", "mode")
    try:
        makedirs(dir_abs_path, mode)
    except Exception as exception:
        error_code = exception.errno
        if error_code == EACCES: # 13 (Python 3 PermissionError)
            raise Exception(settings.messages["_critical_NoRoot"])
        elif error_code == ENOTDIR: # 20 (Python 3 NotADirectoryError)
            path = dir_abs_path
            while path != '/':
                if isfile(path):
                    try:
                        remove(path)
                    except Exception as exception:
                         error_code = exception.errno
                         if error_code == EACCES: # 13 (Python 3
                                                  # PermissionError)
                             msg = "_critical_NoRoot"
                             raise Exception(settings.messages[msg])
                         else:
                             msg = "_critical_Oops"
                             raise Exception(settings.messages[msg] %
                                     strerror(error_code))
                path = dirname(path)
            try:
                makedirs(dir_abs_path, mode)
            except Exception as exception:
                error_code = exception.errno
                if error_code == EACCES: # 13 (Python 3 PermissionError)
                    raise Exception(settings.messages["_critical_NoRoot"])
                else:
                    msg = "_critical_Oops"
                    raise Exception(settings.messages[msg] %
                            strerror(error_code))
        else:
            msg = "_critical_Oops"
            raise Exception(settings.messages[msg] % strerror(error_code))
    return 0

def get_abs_path(path):
    """Get abs path"""

    if path.startswith('~'):
        abs_path = expanduser(path)
    elif not path.startswith('/'):
        abs_path = join(getcwd(), path)
    else:
        abs_path = path
    return abs_path
