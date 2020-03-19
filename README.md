# csv2roam

Converts CSV file to nested markdown format supported by Roam Research


# Installation

If you don't use `pipx`, you're missing out.
Here are [installation instructions](https://github.com/pipxproject/pipx/).

On macOS:

    $ brew install pipx
    $ pipx ensurepath

    $ pipx install .

Or

    pipx install git+https://github.com/trbielec/csv2roam.git


# Usage

Usage:


    csv2roam [OPTIONS] INPUT OUTPUT

    example: csv2roam -r -c data.csv output.md

    Converts CSV file to nested markdown format supported by Roam Research

    Options:
    -r, --root-page    Create [[page]] for root values (first column)
    -c, --child-pages  Create [[page]] for child values
    --help             Show this message and exit.
