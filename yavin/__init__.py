"""Package for yavin"""
# System
import sys

__project__ = 'Yavin'
__version__ = '1.0.0'

CLI = 'yavin'
MAIN = 'yavin.main:main'
VERSION = '{0} v{1}'.format(__project__, __version__)
DESCRIPTION = 'Create clients and servers that demonstrate the MQTT protocol'

MIN_PYTHON_VERSION = 3, 4

if not sys.version_info >= MIN_PYTHON_VERSION:
    exit("Python {}.{}+ is required.".format(*MIN_PYTHON_VERSION))

import logging

logger = logging.getLogger(__name__)

# Local
# try:
    # from .subpackage import ModuleName
# except ImportError:
    # pass
