"""visiumlint main module."""
# pylint: disable=duplicate-code
import sys
from subprocess import run

import typer


def lint(fix: bool = typer.Option(False, "--fix")) -> None:
    """Implement the logic of the lint command."""
    if fix:
        check = ""
    else:
        check = "--check"

    run(["sh", "-c", "echo 'Running black'"], check=False)
    black_returncode = run(["sh", "-c", f"black {check} . --line-length 120"], check=False).returncode

    run(["sh", "-c", "echo Running isort"], check=False)
    isort_returncode = run(
        ["sh", "-c", f"isort {check} --gitignore . --line-length 120 --profile black"], check=False
    ).returncode

    run(["sh", "-c", "echo Running pylint"], check=False)
    pylint_returncode = run(
        [
            "sh",
            "-c",
            "pylint . --recursive=y --load-plugins=pylint.extensions.docstyle,pylint.extensions.docparams --disable=fixme,too-few-public-methods",
            "--variable-rgx",
            "^[a-z][a-z0-9_]*$",
            "--argument-rgx",
            "^[a-z][a-z0-9_]*$",
            "--max-line-length",
            "120",
        ],
        check=False,
    ).returncode

    run(["sh", "-c", "echo Running pydocstyle"], check=False)
    pydocstyle_returncode = run(
        ["sh", "-c", "pydocstyle .", "--add-ignore", "D107, D104, D103", "--convention", "google"], check=False
    ).returncode

    run(["sh", "-c", "echo Running mypy"], check=False)
    mypy_returncode = run(
        [
            "sh",
            "-c",
            '! mypy . --disallow-untyped-defs --disallow-incomplete-defs | grep "Function is missing" || false',
        ],
        check=False,
    ).returncode

    if (
        black_returncode != 0
        or isort_returncode != 0
        or pylint_returncode != 0
        or pydocstyle_returncode != 0
        or mypy_returncode != 0
    ):
        sys.exit(1)


if __name__ == "__main__":
    typer.run(lint)
