#!/usr/bin/env python

import argparse
import pathlib
import shutil
import subprocess

from colores import colorized_print, CYAN

SUPPORTED_PLATFORMS = [
    "x86_64-unknown-linux-gnu",
    "aarch64-apple-darwin",
    "x86_64-apple-darwin",
    "x86_64-pc-windows-msvc",
]


def parse_arguments():
    parser = argparse.ArgumentParser(
        "Compile Javascript or TypeScript file to all platforms with Deno."
    )

    parser.add_argument("file", help="The file to compile.")

    parser.add_argument(
        "--outputDir",
        help="The directory to put the generated binary files.",
        default="deno_builds",
    )

    parser.add_argument(
        "--compress",
        help="Compress the build directory?",
        default=False,
    )

    args = parser.parse_args()

    return args.file, args.outputDir, args.compress


def create_dir(directory_to_create: str) -> None:
    pathlib.Path(directory_to_create).mkdir(exist_ok=True)


def is_installed(program: str) -> bool:
    return (
        subprocess.call(
            ["which", program], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        == 0
    )


def compress_binaries(directory: str, format_file: str) -> None:
    colorized_print("Compressing binaries...", CYAN)
    shutil.make_archive(directory, format_file, directory)


def compile_all_platforms(file: str, directory: str) -> None:
    for platform in SUPPORTED_PLATFORMS:
        error = subprocess.call(
            [
                "deno",
                "compile",
                "--allow-all",
                "--output",
                f"{directory}/{platform}" if directory else platform,
                file,
                "--target",
                platform,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        successful_message = f"{file} compiled successfully for {platform}!"
        error_message = f"There was an error while compiling {file} for {platform}."

        colorized_print(successful_message if not error else error_message)
