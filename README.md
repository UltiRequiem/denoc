# Denoc

![CodeQL](https://github.com/UltiRequiem/denoc/workflows/CodeQL/badge.svg)
![Pylint](https://github.com/UltiRequiem/denoc/workflows/Pylint/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/denoc)](https://pypi.org/project/denoc)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/denoc?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/denoc?color=blue&label=Total%20Lines)

Compile Deno executables and compress them for all platforms easily.

## Install

You can install [denoc](https://pypi.org/project/denoc) from PyPI like any other package:

```bash
pip install denoc
```

To get the last version:

```bash
pip install git+https:/github.com/UltiRequiem/denoc
```

If you use Linux, you may need to install this with sudo to be able to access the command throughout your system.

## Usage

Basic usage:

```bash
denoc compileMe.ts
```

This will make a directory (`deno_builds`) with executables for all the supported platforms.

Optional flags:

```bash
denoc --outputDir deno_dir_output --compress True file.ts
```

- `outputDir`: The directory where the binaries will be, by default the directory is *deno_build*

- `compress`: Compress the binaries directory

### Usage Example

- Build and Publish GitHub Action

```yaml
name: Compile

on:
  push:
    tags:
      - "*"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - uses: denoland/setup-deno@v1
        with:
          deno-version: v1.x

      - name: Install denoc
        run: pip install denoc

      - name: Build for all platforms
        run: denoc cli.ts

      - name: Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            deno_builds/x86_64-unknown-linux-gnu
            deno_builds/aarch64-apple-darwin 
            deno_builds/x86_64-apple-darwin
            deno_builds/x86_64-pc-windows-msvc.exe
          token: ${{ secrets.GITHUB_TOKEN }}
```

### License

[This project](https://pypi.org/project/denoc) is licensed under the [MIT License](./LICENSE.md).
