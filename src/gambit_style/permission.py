"""
Fix file permissions
====================
"""

import os


FILE_EXTENSIONS = ['.c', '.h', '.C', '.H', '.cpp', '.hpp', '.cc', '.hh',
                   '.c++', '.h++', '.cxx', '.hxx', '.txt', '.dat', '.slha', '.yaml']
# Commonly known as 664
PERMISSION = 0o100664


def fix_permission(path_to_file):
    """
    Fix the file permission to 664

    @param path_to_file Absolute file path
    """
    _, file_extension = os.path.splitext(path_to_file)
    if file_extension in FILE_EXTENSIONS:
        os.chmod(path_to_file, PERMISSION)
