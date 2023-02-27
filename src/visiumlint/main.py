"""visiumlint main module."""
from subprocess import call


def lint() -> None:
    """Implement the logic of the lint command."""
    call(["sh", "-c", "echo 'Running black'"])
    call(["sh", "-c", "black --check . --line-length 120"])

    call(["sh", "-c", "echo Running isort"])
    call(["sh", "-c", "isort --check --gitignore . --line-length 120 --profile black"])

    call(["sh", "-c", "echo Running pylint"])
    call(
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
        ]
    )

    call(["sh", "-c", "echo Running pydocstyle"])
    call(["sh", "-c", "pydocstyle .", "--add-ignore", "D107, D104, D103", "--convention", "google"])

    call(["sh", "-c", "echo Running mypy"])
    call(
        [
            "sh",
            "-c",
            '! mypy . --disallow-untyped-defs --disallow-incomplete-defs | grep "Function is missing" || false',
        ]
    )
