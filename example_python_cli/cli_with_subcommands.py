"""
CLI module
"""
import argparse
from typing import Any

from example_python_cli.subcommand_one import SubcommandOne
from example_python_cli.subcommand_two import SubcommandTwo


def subcommand_one_handler(args: Any) -> None:
    subcommand_one = SubcommandOne()
    subcommand_one.run()

def subcommand_two_handler(args: Any) -> None:
    subcommand_two = SubcommandTwo()
    subcommand_two.run()


def cli() -> None:
    """
    Entry point for the CLI
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of the person to greet')
    args = parser.parse_args()
    print(f'Hello, {args.name}!')