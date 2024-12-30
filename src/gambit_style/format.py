"""
Format Python or C/C++ file
===========================
"""

import subprocess

import clang_format
import autopep8
import cpplint
from pylint.lint import Run as PyLintRun


def format_cxx_file(path_to_file):
    """
    @param path_to_file Absolute file path
    """
    subprocess.call([clang_format._get_executable(
        "clang-format"), "-i", path_to_file])


def format_python_file(path_to_file):
    """
    @param path_to_file Absolute file path
    """
    options = autopep8.parse_args([path_to_file])
    options.in_place = True
    autopep8.fix_file(path_to_file, options)


def lint_cxx_file(path_to_file):
    """
    @param path_to_file Absolute file path
    """
    cpplint.ProcessFile(path_to_file, 1)


def lint_python_file(path_to_file):
    """
    @param path_to_file Absolute file path
    """
    PyLintRun([path_to_file], exit=False)


def lint_yaml_file(path_to_file):
    """
    @param path_to_file Absolute file path
    """
    subprocess.call(["yamllint", path_to_file])
