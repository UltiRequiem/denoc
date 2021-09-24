"""
This is the file that runs when denoc is runned as a module.
"""
import sys

from .utils import (
    compile_all_platforms,
    create_dir,
    is_installed,
    parse_arguments,
    compress_binaries,
)

print("Starting the process...")

if not is_installed("deno"):
    sys.exit("Deno is not installed!")

file, output_dir, compress = parse_arguments()

create_dir(output_dir)

compile_all_platforms(file, output_dir)

if compress:
    compress_binaries(output_dir, "zip")
