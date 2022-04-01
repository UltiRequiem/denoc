# Deprecated

This would make more sense if it was written using Deno, or a compiled language
like Go or Rust.

Email me to `eliaz.bobadilladev@gmail.com` if you create a similar tool, so I
will link it here.

> If no one does, I will try to do it in my free time later,
> [sponsor me](https://patreon.com/ultirequiem) 😩

# Denoc

Compile Deno executables and compress them for all platforms easily 🚀

## Install

You can install [denoc](https://pypi.org/project/denoc) from PyPI like any other
package:

```bash
pip install denoc
```

From Github 👇

```bash
pip install git+https:/github.com/UltiRequiem/denoc
```

## Usage

### Basic usage

```bash
denoc compileMe.ts
```

This will make a directory (`deno_builds`) with executables for all the
supported platforms.

Optional flags:

```bash
denoc --outputDir deno_dir_output --compress True file.ts
```

- `outputDir`: The directory where the binaries will be, by default the
  directory is _deno_build_

- `compress`: Compress the binaries directory

### Build and Publish on GitHub Actions

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

## Authors

[Eliaz Bobadilla (a.k.a UltiRequiem)](https://ultirequiem.com) - Creator and
Maintainer 💪

See also the full list of
[contributors](https://github.com/UltiRequiem/denoc/contributors) who
participated in this project.

## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available,
see the [tags](https://github.com/UltiRequiem/denoc/tags).

## Licence

Licensed under the MIT License.
