"""
Walk GAMBIT directory
=====================
"""

import os

import autopep8


IGNORE = [".github", "contrib"]
CXX_FILE_EXTENSIONS = [".cpp", ".cxx", ".hpp", ".hxx", ".c", ".h"]
YAML_FILE_EXTENSIONS = [".yaml", ".yml"]


is_python_file = autopep8.is_python_file


def is_cxx_file(path_to_file):
    _, file_extension = os.path.splitext(path_to_file)
    return file_extension in CXX_FILE_EXTENSIONS


def is_yaml_file(path_to_file):
    _, file_extension = os.path.splitext(path_to_file)
    return file_extension in YAML_FILE_EXTENSIONS


def walk(dir_):
    for subdir, dirs, files in os.walk(dir_, topdown=True):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for f in files:
            yield os.path.join(subdir, f)


def files(file_or_dir):
    if os.path.isfile(file_or_dir):
        return [file_or_dir]

    if os.path.isdir(file_or_dir):
        return walk(file_or_dir)

    if isinstance(file_or_dir, list):
        return file_or_dir

    raise RuntimeError(f"Could not understand {file_or_dir}")
