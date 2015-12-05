__author__ = 'TonySun'
"""
some common functions shared by all scripts
"""

import os
# get absolute path of a file. Compatible in all OSs
def getAbsPath(path):
    """
    find absolute path given a relative file path
    :param path: relative path
    :return: absolute path
    """
    script_dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(script_dir, path)
    return abs_file_path
