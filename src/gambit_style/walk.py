"""
Walk GAMBIT directory
=====================
"""

import os
import warnings

import autopep8


IGNORE_DIR = ["contrib", "build"]
IGNORE_FILE = []

CXX_FILE_EXTENSIONS = [".cpp", ".cxx", ".hpp", ".hxx", ".c", ".h"]
YAML_FILE_EXTENSIONS = [".yaml", ".yml"]


is_python_file = autopep8.is_python_file


def is_cxx_file(path_to_file):
    _, file_extension = os.path.splitext(path_to_file)
    return file_extension in CXX_FILE_EXTENSIONS


def is_yaml_file(path_to_file):
    _, file_extension = os.path.splitext(path_to_file)
    return file_extension in YAML_FILE_EXTENSIONS


def is_dotfile(file_or_dir):
    abs_ = os.path.abspath(file_or_dir)
    return any(n.startswith(".") for n in abs_.split(os.sep))


def ignore_dir(path):
    return path in IGNORE_DIR or is_dotfile(path)


def ignore_file(path_to_file):
    return path_to_file in IGNORE_FILE or is_dotfile(path_to_file)


def walk(dir_):
    for subdir, dirs, files in os.walk(dir_, topdown=True):
        dirs[:] = [d for d in dirs if not ignore_dir(d)]
        for f in files:
            path_to_file = os.path.join(subdir, f)
            if not ignore_file(path_to_file):
                yield path_to_file


def files(file_or_dir):
    if isinstance(file_or_dir, (list, tuple)):
        for f in file_or_dir:
            yield from files(f)
    elif ignore_file(file_or_dir):
        warnings.warn(f"Ignored {file_or_dir}")
    elif os.path.isfile(file_or_dir):
        yield file_or_dir
    elif os.path.isdir(file_or_dir):
        yield from walk(file_or_dir)
    else:
        raise RuntimeError(f"Could not open {file_or_dir}")
