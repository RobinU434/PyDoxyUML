from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="pydoxyuml",
    version="0.1",
    description="PyDoxyUML - Collect Python code documentation and generate UML diagrams",
    author="Robin Uhrich",
    author_email="robin.uhrich@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pydoxyuml = pydoxyuml.__main__:main",
        ],
    },
    install_requires=requirements,
    package_data={
        "pydoxyuml": ["Doxyfile"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",  # Updated license classifier
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # Updated license information
    license="Apache License, Version 2.0",
)
