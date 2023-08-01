import glob
import logging
from typing import Any, List, Union
import pkg_resources
from pydoxyuml.documenter import Documenter


class DoxyDocumenter(Documenter):
    def __init__(
        self, input: List[str], output: str, doxyfile: str, title: str, style_sheet: str
    ) -> None:
        super().__init__(input, output)
        self._doxyfile = self._load_doxyfile(doxyfile)
        """List[str]: variable contains content of doxyfile"""
        self._tmp_dir = self._output + "tmp/"
        self._title = title
        self._style_sheet_path = style_sheet

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self._create_directory(self._output)
        # create tmp/ directory
        self._create_directory(self._tmp_dir)

        # create same folder structure in tmp/ as for given projects
        for module_path in self._input:
            python_files = glob.glob(
                module_path.rstrip("/") + "/**/*.py", recursive=True
            )
            directories = set(
                map(
                    lambda x: self._tmp_dir
                    + ("/".join(x.split("/")[:-1]).lstrip("../")),
                    python_files,
                )
            )
            self._create_directories(directories)
            self._call_doxypypy(python_files)

        self._alter_doxyfile()
        self._generate_documentation()
        # self._cleanup()

    def _load_doxyfile(self, doxyfile: Union[None, str]):
        if doxyfile is None:
            return self._load_text_file(
                pkg_resources.resource_filename("pydoxyuml", "Doxyfile")
            )
        else:
            return self._load_text_file(doxyfile)

    @staticmethod
    def _load_text_file(path: str) -> List[str]:
        with open(path, "r") as file:
            lines = file.readlines()
        return lines

    @staticmethod
    def _write_text_file(path: str, content: List[str]):
        """write given lines into textfile

        Args:
            path (str): where to write the text file
            content (str):
        """
        with open(path, "w") as file:
            file.writelines(content)

    def _call_doxypypy(self, python_files: List[str]):
        """call doxypypy on a given list of files to copy in self._output/tmp directory

        Args:
            python_files (List[str]): list of python files to apply to doxypypy on and add into self._output/tmp directory
        """
        for python_file in python_files:
            command = f"doxypypy -a -c {python_file} > {self._tmp_dir+python_file.lstrip('../')}"
            self._execute_command(command)

    def _alter_doxyfile(self):
        """alter Doxyfile at:
        - Project_NAME
        - INPUT
        - OUTPUT_DIRECTORY
        """
        title_str = "PROJECT_NAME           = Example Project"
        input_str = "INPUT                  ="
        output_str = "OUTPUT_DIRECTORY       ="
        # TODO: insert HTML Style sheet
        html_style_sheet_str = "HTML_EXTRA_STYLESHEET  ="
        index_to_remove = []
        for line_idx in range(len(self._doxyfile)):
            # alter title
            if (
                input_str in self._doxyfile[line_idx]
                and self._tmp_dir not in self._doxyfile[line_idx]
            ):
                self._doxyfile[line_idx] = self._add_doxy_content(
                    self._doxyfile[line_idx], f" {self._tmp_dir}"
                )
                print(self._doxyfile[line_idx])
                logging.debug("altered input directory")
            # alter title to custom
            elif title_str in self._doxyfile[line_idx]:
                self._doxyfile[line_idx].replace("Example Project", self._title)
                logging.debug("altered title")
            elif (
                output_str in self._doxyfile[line_idx]
                and output_str not in self._doxyfile[line_idx]
            ):
                self._doxyfile[line_idx] = self._add_doxy_content(
                    self._doxyfile[line_idx], f" {self._output}"
                )
                logging.debug("altered output directory")
            elif html_style_sheet_str in self._doxyfile[line_idx]:
                if self._style_sheet_path is None:
                    index_to_remove.append(line_idx)
                else:
                    self._doxyfile[line_idx] = self._add_doxy_content(
                        self._doxyfile[line_idx], self._style_sheet_path
                    )

        # remove indices
        for index in index_to_remove[::-1]:
            self._doxyfile.pop(index)

        self._write_text_file(self._output + "Doxyfile", self._doxyfile)

    @staticmethod
    def _add_doxy_content(line: str, content: str) -> str:
        """adds line at the back of a given line but before '\\n'

        Args:
            line (str): line to alter
            content (str): content to add after = but before '\\n'

        Returns:
            str: altered line
        """
        line = line.rstrip("\n")
        line += f" {content}"
        line += "\n"
        return line

    def _generate_documentation(self):
        # command = f"export INCLUDE={self._tmp_dir}"
        # self._execute_command(command)
        command = f"doxygen {self._output +'Doxyfile'}"
        self._execute_command(command)

    def _cleanup(self):
        # remove self._tmp directory
        command = f"rm -r {self._tmp_dir}"
        self._execute_command(command)
