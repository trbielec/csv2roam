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

# Example

data.csv

    col1,col2,col3
    c1r1,c2r1,c3r1
    c1r2,c2r2,c3r2

output.md

    # Data Export
    - col1:: [[c1r1]]
      - col2:: [[c2r1]]
      - col3:: [[c3r1]]
    - col1:: [[c1r2]]
      - col2:: [[c2r2]]
      - col3:: [[c3r2]]
