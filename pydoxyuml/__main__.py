from argparse import ArgumentParser
import argparse

from pydoxyuml.generate_uml import UMLDocumenter
from pydoxyuml.genreate_doxy_doc import DoxyDocumenter
from pydoxyuml.utils.logging import set_log_level
from pydoxyuml.utils.parser import setup_parser


def main():
    parser = ArgumentParser(
        description="PyDoxyUML - Collect Python code documentation and generate Doxygen docs + UML diagrams",
    )
    parser = setup_parser(parser)

    args_dict = vars(parser.parse_args())
    set_log_level(args_dict.pop("log_level"))
    command = args_dict.pop("command")
    if command == "generate-docs":
        generator = DoxyDocumenter(**args_dict)
    elif command == "generate-uml":
        generator = UMLDocumenter(**args_dict)
    else:
        parser.print_help()
        exit()

    generator()


if __name__ == "__main__":
    main()
