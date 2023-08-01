from argparse import ArgumentParser
import argparse


def setup_parser_generate_docs(parser: ArgumentParser) -> ArgumentParser:
    """setup parser for generate-docs command

    Args:
        parser (ArgumentParser): _description_

    Returns:
        ArgumentParser: _description_
    """
    parser.add_argument(
        "--input",
        nargs="+",
        type=str,
        help="Collection of paths to the files you want to document",
        required=True,
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to directory where you want to save your documentation with folders 'html/', 'latex/', ...",
        required=True,
    )
    parser.add_argument(
        "--doxyfile",
        type=str,
        help="Path to Doxyfile. Is required if the corresponding Doxyfile is not in the current directory.",
    )
    parser.add_argument(
        "--title",
        type=str,
        default="Example Project",
        help="Title for project you want to document.",
    )
    parser.add_argument(
        "--style-sheet", type=str, help="Absolute path to html style sheet."
    )
    return parser


def setup_parser_generate_uml(parser: ArgumentParser) -> ArgumentParser:
    """setup parser for generate-uml command

    Args:
        parser (ArgumentParser): parser object

    Returns:
        ArgumentParser: setup parser object
    """
    parser.add_argument(
        "--input",
        nargs="+",
        type=str,
        help="Collection of paths to the files you want to document",
        required=True,
    )
    parser.add_argument(
        "--output",
        type=str,
        default="uml",
        help="Path to directory where you want to save your documentation with folder 'uml/'",
    )
    parser.add_argument(
        "--recursion-depth",
        type=int,
        default=1,
        help="how deep the algorithm will go to discover local parent directories for generating UML diagrams.",
    )
    parser.add_argument(
        "--format",
        type=str,
        default="png",
        choices=["png", "jpg", "puml", "plantuml", "dot", "gv", "mmd", "html"],
        help="Output format for uml diagrams. *.<format>",
    )
    parser.add_argument(
        "--colorized",
        action="store_true",
        help="Flag activates colorized UML generation",
    )
    return parser


def setup_parser(parser: ArgumentParser) -> ArgumentParser:
    """add command to parser and setup argument for individual commands

    Args:
        parser (ArgumentParser): _description_

    Returns:
        ArgumentParser: _description_
    """
    sub_parser = parser.add_subparsers(dest="command", title="command")
    parser_generate_docs = sub_parser.add_parser(
        "generate-docs",
        help="Generate Doxygen-style documentation",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_generate_docs = setup_parser_generate_docs(parser_generate_docs)

    parser_generate_uml = sub_parser.add_parser(
        "generate-uml",
        help="Generate UML diagrams",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser_generate_uml = setup_parser_generate_uml(parser_generate_uml)

    parser.add_argument(
        "--log-level",
        choices=["critical", "error", "warning", "info", "debug", "notset"],
        type=str,
        help="sets log level",
        default="warning",
    )

    return parser
