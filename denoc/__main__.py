"""
This is the file that runs when grepy is runned as a module.
"""
import sys

from .utils import compile_all_platforms, deno_is_installed, parse_arguments


if not deno_is_installed():
    sys.exit("Deno is not installed!")


file = parse_arguments()

compile_all_platforms(file)
