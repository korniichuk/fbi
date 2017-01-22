# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from sys import argv, exit

import settings
from decode import decode
from encode import encode
from init import init

def main():
    """Main function"""

    args = parse_command_line_args()
    args.function_name(args)

def parse_command_line_args():
    """Parse command line arguments"""

    # Create top parser
    parser = ArgumentParser(
            prog="fbi", description=settings.argparse["_parser"],
            add_help=True)
    parser.add_argument("-v", "--version", action="version",
                        version="fbi 0.1a7")
    # Create subparsers for the top parser
    subparsers = parser.add_subparsers(title=settings.argparse["_subparsers"])
    # Create the parser for the "decode" subcommand
    parser_decode = subparsers.add_parser(
            "decode", description=settings.argparse["_parser_decode"],
            help=settings.argparse["_parser_decode"])
    parser_decode.add_argument("path", action="store", nargs=1,
                                metavar="PATH")
    parser_decode.set_defaults(function_name=decode)
    # Create the parser for the "encode" subcommand
    parser_encode = subparsers.add_parser(
            "encode", description=settings.argparse["_parser_encode"],
            help=settings.argparse["_parser_encode"])
    parser_encode.add_argument("path", action="store", nargs=1,
                                metavar="PATH")
    parser_encode.set_defaults(function_name=encode)
    # Create the parser for the "init" subcommand
    parser_init = subparsers.add_parser(
            "init", description=settings.argparse["_parser_init"],
            help=settings.argparse["_parser_init"])
    parser_init.set_defaults(function_name=init)
    if len(argv) == 1:
        parser.print_help()
        exit(0) # Clean exit without any errors/problems
    return parser.parse_args()
