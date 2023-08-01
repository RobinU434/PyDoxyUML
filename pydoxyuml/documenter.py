from abc import ABC, abstractmethod
import logging
import os
from typing import Any, List


class Documenter(ABC):
    def __init__(self, input: List[str], output: str) -> None:
        super().__init__()

        self._input = input
        """List[str]: list of input module root directories"""
        self._output = output.rstrip("/") + "/"
        """str: directory where to store documentation. Format <directory>/"""

    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)

    def _create_directory(self, directory: str):
        """creates output directory"""
        command = f"mkdir -p {directory}"
        self._execute_command(command)

    def _create_directories(self, directories: List[str]):
        """creates a bunch of given directories

        Args:
            directories (List[str]): _description_
        """
        for directory in directories:
            self._create_directory(directory)

    def _copy(self, source: str, destination: str):
        """copies file form source to destination

        Args:
            source (str): path to source file
            destination (str): path to destination
        """
        command = f"cp {source} {destination}"
        self._execute_command(command)

    @staticmethod
    def _execute_command(command: str):
        logging.debug(command)
        os.system(command)
