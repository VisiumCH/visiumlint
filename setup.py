"""Setup script for visiumlint."""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visiumlint",
    version="0.0.2",
    author="Visium SA",
    description="Visium linting tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VisiumCH/visium-lint",
    packages=setuptools.find_packages(),
    install_requires=[
        "black",
        "isort",
        "mypy",
        "pydocstyle",
        "pylint",
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "visiumlint = visiumlint.main:lint",
        ],
    },
)
