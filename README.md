# PyDoxyUML

PyDoxyUML is a Python package that collects Python code documentation (in google template) and creates Doxygen-style documentation, along with generating Unified Modeling Language (UML) diagrams.

## Features

- Automatic generation of Doxygen-style documentation from Python docstrings.
- Extracts code documentation and UML diagram generation in a single package.
- Supports popular UML diagram formats: "png", "jpg", "puml", "plantuml", "dot", "gv", "mmd", "html".
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

For visualization you will need graphviz

   ```bash
   sudo apt install graphviz
   ```

2. **doxypypy**: Doxypypy is a Python module that converts Python docstrings to Doxygen-compatible comments. Install it using `pip`:

   ```bash
   sudo apt install python3-doxypypy
   ```

3. **TexLive**: (Optional) Install TexLive for latex generated output

    ```bash
    sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra
    ```

### PyDoxyUML Package

You can install the PyDoxyUML package by cloning this repository and calling:

```bash
pip install .
```

inside the repository root directory.

TODO:
You can install the PyDoxyUML package using `pip`, the Python package manager:

```bash
pip install pydoxyuml
```

## Usage

### Documenting Python Code with Docstrings (Google Template)

PyDoxyUML utilizes Python docstrings to automatically generate Doxygen-style documentation. Following the Google docstring template is a widely used convention to document Python code. Here's a brief explanation of the Google docstring template:

Function Docstring

```python
def function_name(param1, param2):
    """One-line summary of the function.

    A longer, more detailed description of the function if necessary.

    Args:
        param1 (type): Description of param1.
        param2 (type): Description of param2.

    Returns:
        return_type: Description of the return value.

    Raises:
        ExceptionType: Description of when this exception is raised (if applicable).

    Examples:
        Provide examples of how to use the function.
    """
    # Function implementation here
    return something
```

Class Docstring:

```python
class MyClass:
    """One-line summary of the class.

    A longer, more detailed description of the class if necessary.

    Attributes:
        attribute1 (type): Description of attribute1.
        attribute2 (type): Description of attribute2.

    Methods:
        method1: Description of method1.
        method2: Description of method2.
    """
    # Class implementation here
```

Module Docstring:

```python
"""One-line summary of the module.

A longer, more detailed description of the module if necessary.

This module provides functionality for ...
"""
# Module implementation here
```

Make sure to document your functions, classes, and modules using this docstring format. PyDoxyUML will extract the relevant information from these docstrings to generate the Doxygen-style documentation.

For documenting formulas as latex code use:

For block equations:

```python
\f[
   \frac{1}{2}
\f]
```

For inline term

```python
\f$\frac{1}{2}\f$
```

### Generating Doxygen-style Documentation

To generate Doxygen-style documentation for your Python code, simply run the following command:

```bash
pydoxyuml generate-docs --input <paths/to/your/python/files> --output <output/directory>
```

Replace `<path/to/your/python/files>` with the paths to your Python source files and `<output/directory>` with the directory where you want the documentation to be generated.

We provide a template [`Doxyfile`](./pydoxyuml/Doxyfile) as a default `Doxyfile`. If you want to create your own `Doxyfile` it is recommended to use the template a start and further employ your own changes.

For polishing your html output you can use repositories like: [doxygen-awesome-css](https://github.com/jothepro/doxygen-awesome-css) and reference to the corresponding style sheet.

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