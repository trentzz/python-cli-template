"""
CLI module
"""

import argparse

from example_python_cli.basic import Basic


def cli() -> None:
    """
    Entry point for the CLI
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Name of the person to greet")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

    basic = Basic()
    basic.run()
