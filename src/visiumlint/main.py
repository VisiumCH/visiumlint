"""visiumlint main module."""
# pylint: disable=duplicate-code
import sys
from subprocess import run

import typer


def lint(check_lint: bool = typer.Option(False, "--check", help="Enable check mode.")) -> None:
    """Implement the logic of the lint command."""
    if check_lint:
        check_lint = "--check"
    else:
        check_lint = ""

    run(["sh", "-c", "echo 'Running black'"], check=False)
    black_returncode = run(["sh", "-c", f"black {check_lint} . --line-length 120"], check=False).returncode

    run(["sh", "-c", "echo Running isort"], check=False)
    isort_returncode = run(
        ["sh", "-c", f"isort {check_lint} --gitignore . --line-length 120 --profile black"], check=False
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


def main() -> None:
    """Typer entrypoint."""
    typer.run(lint)
