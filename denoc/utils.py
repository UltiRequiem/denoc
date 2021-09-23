#!/usr/bin/env python

import subprocess
import argparse


def parse_arguments() -> str:
    parser = argparse.ArgumentParser(
        "Compile Javascript or TypeScript file to all plataforms with Deno."
    )

    parser.add_argument("file", type=str, help="The file to compile.", required=True)

    args = parser.parse_args()

    return args.file


supported_platforms = [
    "x86_64-unknown-linux-gnu",
    "aarch64-apple-darwin",
    "x86_64-apple-darwin",
    "x86_64-pc-windows-msvc",
]


def deno_is_installed():
    return subprocess.call(["which", "deno"])


def compile_all_platforms(file):
    for platform in supported_platforms:
        subprocess.run(
            ["deno", "compile", "--target", platform, "--output", platform, file]
        )
