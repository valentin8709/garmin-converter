#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Garmin Converter.

Use: try -h or --help for more information.

Description: Convert FIT Garmin format to GPX using fit2gpx library.

"""

import os
import argparse

from pathlib import Path
from fit2gpx import Converter


def getopts() -> argparse.Namespace:
    """Catch parameters for validity checking and parsing."""
    parser = argparse.ArgumentParser(
        description="""
        Description: Convert FIT Garmin format to GPX using fit2gpx library."""
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        metavar="input_file",
        help="FIT file to convert",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        metavar="output_file",
        help="file to write into GPX format",
    )

    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="recursive input to convert GPX files from a folder",
    )

    args: argparse.Namespace = parser.parse_args()

    return args


def convert_files(input_data: Path, output_data: Path, recursive: bool):
    """Convert one or multiple FIT files into GPX.

    Parameters
    ----------
    input_data: Path
        input file or folder to convert (must be / include FIT files)
    output_data: Path
        output file or folder to write GPX file(s)
    recursive: bool
        enable recursive convertion or single file run

    """
    conv = Converter()
    gpx = None

    if recursive:
        gpx = conv.fit_to_gpx_bulk(dir_in=input_data.as_posix(), dir_out=output_data.as_posix())
    else:
        conv.fit_to_gpx(f_in=input_data.as_posix(), f_out=output_data.as_posix())

    return gpx


def main() -> int:
    """Run Garmin Converter on specified file."""
    opts: argparse.Namespace = getopts()
    input_data: Path = Path(opts.input)
    output_data: Path = Path(opts.output)
    recursive: bool = opts.recursive

    # Check for arg consistency
    if input_data.is_file():
        print(f"Error: file {input_data} does not exist")
        return os.EX_NOINPUT
    if input_data.is_dir() and not recursive:
        print("Error: file expected as input, not directory")
        return os.EX_OSFILE

    if recursive:
        if input_data.is_file():
            print("Error: directory expected as input")
            return os.EX_NOINPUT
        if not output_data.is_dir:
            print("Error: directory expected as output")
            return os.EX_NOINPUT
    else:
        if output_data.exists():
            print(f"Error: file {output_data} already exists, cannot overwrite it")
            return os.EX_OSFILE

    # Parse FIT file(s)
    gpx_file = convert_files(input_data, output_data, recursive)

    return os.EX_OK


if __name__ == "__main__":
    main()
