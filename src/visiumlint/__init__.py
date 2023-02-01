import typer

from subprocess import call


def lint(folders:list[str] = typer.Option("", help="Last name of person to greet.")):
    call([ 'sh','-c', "echo 'Running black'"])
    call([ 'sh','-c', 'black --check .'])
    call([ 'sh','-c', 'echo Running isort'])
    call([ 'sh','-c', 'isort --check --gitignore .'])
    call([ 'sh','-c', 'echo Running pylint'])
    call([ 'sh','-c', 'pylint *.py'])
    call([ 'sh','-c', 'echo Running pydocstyle'])
    call([ 'sh','-c', 'pydocstyle .'])
    call([ 'sh','-c', 'echo Running mypy' ])
    call([ 'sh','-c', '! mypy . --disallow-untyped-defs --disallow-incomplete-defs | grep "Function is missing" || false'])