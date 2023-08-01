from argparse import ArgumentParser
import ast
import glob
import os
from typing import Any, Iterable, Iterator, List

from pydoxyuml.documenter import Documenter


def setup_parser(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument(
        "--recursion-level",
        type=int,
        default=3,
        help="how deep the algorithm will go to discover local parent directories",
    )

    parser.add_argument(
        "module_dirs",
        nargs="+",
        type=str,
        help="paths to modules you want to create the uml diagrams from",
    )

    return parser


def unpack(s):
    """converts list into a string with ' ' as separator and without brackets

    Args:
        s (Iterable[str]): list to convert to string

    Returns:
        str: list in str format
    """
    return " ".join(map(str, s))


def find_submodules(root_directory: str) -> List[str]:
    """find all submodules in root directory and have and '__init__.py' file inside

    Args:
        root_directory (str): directory to check for submodule

    Returns:
        List[str]: all subdirectories with '__init__.py' inside
    """
    result_dirs = []
    for dir_path, _, file_names in os.walk(root_directory):
        if "__init__.py" in file_names:
            result_dirs.append(dir_path)
    return result_dirs


def convert_to_file_path(import_str: str) -> str:
    """converts an import statement into a file path

    Args:
        import_str (str): import statement

    Returns:
        str: file path
    """
    return import_str.replace(".", "/").rstrip(".") + ".py"


"""
# BASE IMPORT COLLECTOR
def get_imports(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), file_path)

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.append(name.name)
        if isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ""
            for name in node.names:
                module_str = f"{module}.{name.name}"
                module_str = module_str.lstrip(".")
                imports.append(module_str)
    return imports
"""


class LocalImportFilter:
    """filter determine if a given directory path is a local directory"""

    def __init__(self) -> None:
        self.local_directories = list(filter(self._is_directory, os.listdir()))
        """List[str]: path to local directories"""

    def __call__(self, import_str: str) -> bool:
        dir = import_str.split(".")[0]
        return dir in self.local_directories

    def __str__(self) -> str:
        return unpack(self.local_directories)

    @staticmethod
    def _is_directory(name: str) -> bool:
        """given name is a directory and not a file

        Args:
            name (str): path to either a directory or a file.

        Returns:
            bool: true if there is no '.' and therefor no file ending inside name. False otherwise
        """
        return "." not in name


class UMLDocumenter(Documenter):
    def __init__(
        self,
        input: Iterable[str],
        output: str,
        format: str,
        colorized: bool = True,
        recursion_depth: int = 1,
    ) -> None:
        super().__init__(input, output)
        self._local_dir_filter = LocalImportFilter()
        self._format = format
        self._colorized = colorized
        self._recursion_depth = recursion_depth
        self._imports = []

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self._create_directory(self._output)
        for module_path in self._input:
            imports = self._get_imports_from_submodules(module_path)
            self._imports.extend(imports)
            project_name = module_path.rstrip("/").replace("/", "_")
            command = self._generate_command(project_name, imports)
            self._execute_command(command)

        # if there are multiple modules given -> create a complete UML diagram
        if len(self._input) > 1:
            command = self._generate_command("complete", self._imports)
            self._execute_command(command)

    def _generate_command(self, project_name: str, imports: Iterable[str]) -> str:
        command = f"pyreverse -o {self._format} -p {project_name} -d {self._output} {unpack(imports)}"
        if self._colorized:
            command += " --colorized"
        return command

    def _get_imports_from_submodules(self, module_path: str) -> Iterable[str]:
        """iterates through all python files in all subdirectories

        Args:
            module_path (str): root directory

        Returns:
            Iterable[str]: all files imported by the root directory until recursion depth is reached
        """
        imports = []
        for sub_module_path in find_submodules(module_path):
            for python_file_name in glob.glob(sub_module_path + "/*.py"):
                imports.append(python_file_name)
                imports.extend(
                    self._get_recursive_imports(python_file_name, self._recursion_depth)
                )
        return imports

    def _get_recursive_imports(
        self, python_file_name: str, recursion_level: int
    ) -> Iterable[str]:
        """get all local python files imported by python_file_name until recursion_level == 0 is reached

        Args:
            python_file_name (str): python file to inspect
            recursion_level (int): how many levels deeper to go

        Returns:
            Iterable[str]: list of local python files imported from python_file_name
        """
        # end condition
        if recursion_level <= 0:
            return []

        with open(python_file_name, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read(), python_file_name)

        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                continue
                local_imports = filter(
                    self._local_dir_filter, map(lambda x: x.name, node.names)
                )
                local_files = map(lambda x: convert_to_file_path(x), local_imports)
                # TODO: not tested feature
                imports.extend(
                    list(
                        map(
                            lambda x: self._get_recursive_imports(
                                x, recursion_level - 1
                            ),
                            local_files,
                        )
                    )
                )
            if isinstance(node, ast.ImportFrom) and self._local_dir_filter(node.module):
                file_path = convert_to_file_path(node.module)
                imports.append(file_path)
                imports.extend(
                    self._get_recursive_imports(file_path, recursion_level - 1)
                )

        # filter for empty lists
        imports = list(filter(lambda x: len(x) > 0, imports))
        return imports


if __name__ == "__main__":
    parser = setup_parser(ArgumentParser())
    args = parser.parse_args()

    UMLDocumenter(**vars(args))()

    # main(args.module_dirs)
