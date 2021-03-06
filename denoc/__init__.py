"""
This file defines denoc as a module.
"""

from .core import main
import warnings

__package_name__ = "denoc"
__version__ = "1.1.1"
__authors__ = ["Eliaz Bobadilla <eliaz.bobadilladev@gmail.com>"]
__author_email__ = "eliaz.bobadilladev@gmail.com"
__url__ = "https://github.com/UltiRequiem/denoc"

warnings.warn(
    "denoc is deprecated, check ulti.js.org/denoc for more information",
    DeprecationWarning,
)
