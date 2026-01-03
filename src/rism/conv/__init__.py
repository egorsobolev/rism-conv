# -*- coding: utf-8 -*-
import argparse
from pathlib import Path

from .amber import AmberConverter  # noqa: F401
from .base import get_converters


def main():
    converters = get_converters()

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='format', required=True,
                                       help='format-specific help')

    for frm, conv_cls in converters.items():
        ap = subparsers.add_parser(frm, help=conv_cls.help)
        conv_cls.arguments(ap)

    parser.add_argument("rtxt", type=Path, nargs='?',
                        help="RISM molecule file")

    args = parser.parse_args()
    conv = converters[args.format](args)
    conv.to_rtxt(args.rtxt)


if __name__ == "__main__":
    main()
