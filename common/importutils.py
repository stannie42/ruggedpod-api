"""
Import related utilities and helper functions.
"""

import sys


def import_module(import_str):
    """Import a module."""
    __import__(import_str)
    return sys.modules[import_str]


def try_import(import_str, default=None):
    """Try to import a module and if it fails return default."""
    try:
        return import_module(import_str)
    except ImportError:
        return default


def exit_if_module_missing(import_str):
    """Try to import a module and exit if the module is missing"""
    try:
        return import_module(import_str)
    except ImportError:
        sys.exit('Module %s must be installed to run this program'
                 ' in non-mock mode.' % import_str)
