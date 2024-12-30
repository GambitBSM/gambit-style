# gambit-style

## Install

    pipx install git+https://github.com/GambitBSM/gambit-style

## Use
```bash
gambit-style format GAMBIT_DIRECTORY  # to format in place 
gambit-style lint GAMBIT_DIRECTORY  # to provide lint suggestions
```

You can also run these commands on folders, files or lists of files, e.g.,
```bash
gambit-style format .  # format here
gambit-style format this_file.cpp  # only one file
gambit-style format this_file.cpp and_that_file.py  # a list of files and folders
```

Formatting should apply gambit formatting rules to all appropriate files:

- Format C/CXX files by `clang-format
- PEP8 format Python files by `autopep8`
- Fix file permissions

Linting should provide yamllint, pylint and cpplint suggestions (though note that the cpplint suggestions follow google style guidelines):

## Ignored files

Any `contrib` and `build` directories and any files starting with `.` or inside paths containing directories starting with `.` are ignored.
