import sys

from colores import colorized_print, CYAN, RED

from .utils import (
    compile_all_platforms,
    create_dir,
    is_installed,
    parse_arguments,
    compress_binaries,
)


def main():
    colorized_print("Starting the process...", CYAN)

    if not is_installed("deno"):
        colorized_print("Deno is not installed!", RED)
        sys.exit()

    file, output_dir, compress = parse_arguments()

    create_dir(output_dir)

    compile_all_platforms(file, output_dir)

    if compress:
        compress_binaries(output_dir, "zip")

    colorized_print("Done!", CYAN)
