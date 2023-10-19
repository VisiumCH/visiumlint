"""visiumlint main module."""
# pylint: disable=duplicate-code
import sys
from pathlib import Path
from subprocess import run
from typing import List

import typer


def lint(
    paths: List[Path] = typer.Argument(default=None, help="Paths of files and directories to visiumlint."),
    check_lint: bool = typer.Option(False, "--check", help="Enable check mode."),
    hook: bool = typer.Option(False, "--hook", help="Enable hook mode."),
) -> None:
    """Implement the logic of the lint command."""
    if not paths:
        paths = [Path(".")]
    if check_lint:
        check_lint = "--check"
    else:
        check_lint = ""

    paths = " ".join([str(path) for path in paths if path.is_file() or path.is_dir()])

    run(["sh", "-c", "echo 'Running black'"], check=False)
    black_returncode = run(["sh", "-c", f"black {paths} {check_lint} --line-length 120"], check=False).returncode

    run(["sh", "-c", "echo Running isort"], check=False)
    isort_returncode = run(
        ["sh", "-c", f"isort {check_lint} --gitignore {paths} --line-length 120 --profile black"], check=False
    ).returncode

    if not hook:
        run(["sh", "-c", "echo Running pylint"], check=False)
        pylint_returncode = run(
            [
                "sh",
                "-c",
                f"pylint {paths} --max-line-length 120 --argument-rgx=^[a-z][a-z0-9_]*$ --variable-rgx=^[a-z][a-z0-9_]*$ --recursive=y --load-plugins=pylint.extensions.docstyle,pylint.extensions.docparams --disable=fixme,too-few-public-methods",
            ],
            check=False,
        ).returncode
    else:
        pylint_returncode = 0

    run(["sh", "-c", "echo Running pydocstyle"], check=False)
    pydocstyle_returncode = run(
        ["sh", "-c", f"pydocstyle {paths} --add-ignore=D107,D104,D103 --convention=google"],
        check=False,
    ).returncode

    run(["sh", "-c", "echo Running mypy"], check=False)
    mypy_returncode = run(
        [
            "sh",
            "-c",
            f'! mypy {paths} --disallow-untyped-defs --disallow-incomplete-defs | grep "Function is missing" || false',
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


if __name__ == "__main__":
    main()
