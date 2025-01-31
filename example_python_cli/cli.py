"""
CLI module
"""

import argparse

from example_python_cli.basic import Basic


def cli() -> None:
    """
    Entry point for the CLI
    """
    parser = argparse.ArgumentParser(
        description="A script demonstrating argparse usage with various argument types."
    )

    # Positional argument (required)
    parser.add_argument("name", help="Name of the person to greet")

    # Optional arguments
    parser.add_argument("-a", "--age", type=int, help="Age of the person")
    parser.add_argument("-c", "--city", type=str, default="Unknown", help="City of the person")

    # Required optional argument
    parser.add_argument("-e", "--email", help="Email address", required=True)

    parser.add_argument(
        "-m", "--married", action="store_true", help="Marital status (flag, defaults to False)"
    )
    parser.add_argument(
        "-s", "--score", type=float, default=0.0, help="Score value as a floating-point number"
    )
    parser.add_argument("-l", "--languages", nargs="+", help="List of programming languages known")
    parser.add_argument(
        "-d", "--debug", action="store_const", const=True, default=False, help="Enable debug mode"
    )

    # Choice argument
    parser.add_argument(
        "--mode",
        choices=["easy", "medium", "hard"],
        default="medium",
        help="Select a mode (easy/medium/hard)",
    )

    # Mutually exclusive arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--verbose", action="store_true", help="Enable verbose mode")
    group.add_argument("--quiet", action="store_true", help="Enable quiet mode")

    # Parsing arguments
    args = parser.parse_args()

    basic = Basic(
        name=args.name,
        age=args.age,
        city=args.city,
        email=args.email,
        married=args.married,
        score=args.score,
        languages=args.languages,
        debug=args.debug,
        mode=args.mode,
        verbose=args.verbose,
        quiet=args.quiet,
    )
    basic.run()
