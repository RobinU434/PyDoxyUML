# PyDoxyUML

PyDoxyUML is a Python package that collects Python code documentation and creates Doxygen-style documentation, along with generating Unified Modeling Language (UML) diagrams.

## Features

- Automatic generation of Doxygen-style documentation from Python docstrings.
- Extracts code documentation and UML diagram generation in a single package.
- Supports popular UML diagram types, such as class diagrams, sequence diagrams, and more.
- Easy integration with your existing Python projects.
- Command-line interface for seamless usage from the shell.

## Installation

### System Requirements

Before installing PyDoxyUML, make sure you have the following system-level packages installed:

1. **Doxygen**: Doxygen is used to generate the Doxygen-style documentation from Python docstrings. Install it using your system's package manager (e.g., `apt` for Debian/Ubuntu-based systems):

   ```bash
   sudo apt-get update
   sudo apt-get install doxygen
   ```

2. **doxypypy**: Doxypypy is a Python module that converts Python docstrings to Doxygen-compatible comments. Install it using `pip`:

   ```bash
   sudo apt install python3-doxypypy
   ```

### PyDoxyUML Package

You can install the PyDoxyUML package using `pip`, the Python package manager:

```bash
pip install pydoxyuml
```

## Usage

### Generating Doxygen-style Documentation

To generate Doxygen-style documentation for your Python code, simply run the following command:

```bash
pydoxyuml generate-docs --input <paths/to/your/python/files> --output <output/directory>
```

Replace `<path/to/your/python/files>` with the paths to your Python source files and `<output/directory>` with the directory where you want the documentation to be generated.

### Generating UML Diagrams

To generate UML diagrams with `pyreverse` for your Python code, use the following command:

```bash
pydoxyuml generate-uml --input <paths/to/your/python/files> --output <output/directory>
```

Replace `<path/to/your/python/files>` with the paths to your Python source files and `<output/directory>` with the directory where you want the UML diagrams to be generated.

Note: Make sure an `__init__.py` is in every subdirectory with source code you want to have UML diagram of.

### Command-Line Help

To see the full list of available commands and options, use the `--help` flag:

```bash
pydoxyuml --help
```

## Example

Here's an example of how to use PyDoxyUML to generate Doxygen-style documentation and UML diagrams for your Python project:

```bash
pydoxyuml generate-docs --input ./my_project --output ./docs
pydoxyuml generate-uml --input ./my_project --output ./uml_diagrams
```

In this example, we generate Doxygen-style documentation for the Python code in the `my_project` directory and store the output in the `docs` directory. We also generate UML diagrams for the same codebase and save them in the `uml_diagrams` directory.

## Contributing

Contributions are welcome! If you find a bug or have a feature suggestion, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the Apache License Version 2.0 License. See the [LICENSE](LICENSE) file for details.

```

With these instructions in the `README.md` file, users will be informed about the necessary system requirements (Doxygen and doxypypy) before installing and using the PyDoxyUML package. They can then install the system-level dependencies before proceeding with the Python package installation and usage.