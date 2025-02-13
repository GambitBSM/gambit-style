"""
CLI to linter and formatter
===========================
"""

import click

from .format import format_cxx_file, format_python_file, lint_cxx_file, lint_python_file, lint_yaml_file, TidyCXX, ci_cxx_file
from .permission import fix_permission
from .walk import files, is_yaml_file, is_cxx_file, is_python_file


@click.group()
def cli():
    pass


@cli.command()
@click.argument('file_or_dir', required=True, nargs=-1)
def format(file_or_dir):
    """
    Format in place CXX or Python files in FILE_OR_DIR
    """
    for f in files(file_or_dir):
        if is_python_file(f):
            format_python_file(f)
        if is_cxx_file(f):
            format_cxx_file(f)
        fix_permission(f)


@cli.command()
@click.argument('file_or_dir', required=True, nargs=-1)
def lint(file_or_dir):
    """
    Suggest linting for YAML, CXX or Python files in FILE_OR_DIR
    """
    for f in files(file_or_dir):
        if is_python_file(f):
            lint_python_file(f)
        if is_cxx_file(f):
            lint_cxx_file(f)
        if is_yaml_file(f):
            lint_yaml_file(f)


@cli.command()
@click.argument('gambit_dir', required=True)
@click.argument('file_or_dir', required=True, nargs=-1)
def tidy(gambit_dir, file_or_dir):
    """
    Tidy FILE_OR_DIR in gambit project in GAMBIT_DIR
    """
    tidy_cxx = TidyCXX(gambit_dir)
    for f in files(file_or_dir):
        if is_cxx_file(f):
            tidy_cxx.tidy_cxx_file(f)
            tidy_cxx.iwyu_cxx_file(f)


@cli.command()
@click.argument('file_or_dir', required=True, nargs=-1)
def ci(file_or_dir):
    """
    CI compliance check on FILE_OR_DIR
    """
    for f in files(gambit_dir):
        if is_cxx_file(f):
            ci_cxx_file(f)
        if is_python_file(f):
            ci_python_file(f)


if __name__ == '__main__':
    cli()
