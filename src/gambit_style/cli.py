"""
CLI to linter and formatter
===========================
"""

import click

from .format import format_cxx_file, format_python_file, lint_cxx_file, lint_python_file, lint_yaml_file
from .permission import fix_permission
from .walk import files, is_yaml_file, is_cxx_file, is_python_file


@click.group()
def cli():
    pass


@cli.command()
@click.argument('file_or_dir', required=True)
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
@click.argument('file_or_dir', required=True)
def lint(file_or_dir):
    """
    Lint (i.e. detect potential bugs and style issues and show suggestions) YAML, CXX or Python files in FILE_OR_DIR
    """
    for f in files(file_or_dir):
        if is_python_file(f):
            lint_python_file(f)
        if is_cxx_file(f):
            lint_cxx_file(f)
        if is_yaml_file(f):
            lint_yaml_file(f)


if __name__ == '__main__':
    cli()