"""
Format Python or C/C++ file
===========================
"""

import os
import subprocess

import clang_format
import clang_tidy
import autopep8
import cpplint
from pylint.lint import Run as PyLintRun

from .contrib import iwyu_tool


class TidyCXX:
    def __init__(self, path):
        """
        @param path Path to project
        """
        env = os.environ.copy()
        env["CXX"] = "clang++"
        self.build_dir = os.path.join(path, "tidy_build")
        subprocess.call(["cmake", f"-B{self.build_dir}", f"-S{path}",
                        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"], env=env)

    def tidy_cxx_file(self, file_name):
        """
        @param file_name Python file to be checked
        """
        return subprocess.call([clang_tidy._get_executable("clang-tidy"), "-p", self.build_dir, "-fix", file_name])

    def iwyu_cxx_file(self, file_name):
        """
        @param file_name Python file to be checked
        """
        iwyu_tool.main(self.build_dir, [file_name],
                       True, lambda output: output, 1, 0, [])


def format_cxx_file(file_name):
    """
    @param file_name CXX file to be formatted
    """
    subprocess.call([clang_format._get_executable(
        "clang-format"), "-i", file_name])


def format_python_file(file_name):
    """
    @param file_name Python file to be formatted
    """
    options = autopep8.parse_args([file_name])
    options.in_place = True
    autopep8.fix_file(file_name, options)


def lint_cxx_file(file_name):
    """
    @param file_name CXX file to be linted
    """
    cpplint.ProcessFile(file_name, 1)


def lint_python_file(file_name):
    """
    @param file_name Python file to be linted
    """
    PyLintRun([file_name], exit=False)


def lint_yaml_file(file_name):
    """
    @param file_name YAML file to be linted
    """
    subprocess.call(["yamllint", file_name])
