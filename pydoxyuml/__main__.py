from argparse import ArgumentParser
import sys

from pydoxyuml.generate_uml import UMLDocumenter
from pydoxyuml.genreate_doxy_doc import DoxyDocumenter
from pydoxyuml.utils.logging import set_log_level
from pydoxyuml.utils.parser import setup_parser

"""PyDoxyUML - Collect Python code documentation and generate Doxygen docs + UML diagrams

Either to create doxygen documentation
pydoxyuml generate-docs --input ./my_project --output ./docs

Or to create UML diagrams
pydoxyuml generate-uml --input ./my_project --output ./uml_diagrams

"""


def main():
    """main function

    Calls either DoxygenDocumenter or UMLDocumenter
    """
    parser = ArgumentParser(
        description="PyDoxyUML - Collect Python code documentation and generate\
            Doxygen docs + UML diagrams",
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
        sys.exit()

    generator()


if __name__ == "__main__":
    main()
