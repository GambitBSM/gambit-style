# gambit-style

## Install

    pipx install git+https://github.com/GambitBSM/gambit-style

## Use
```bash
gambit-style format GAMBIT_FILES_OR_DIRECTORY  # to format in place 
gambit-style lint GAMBIT_FILES_OR_DIRECTORY  # to provide lint suggestions
gambit-style tidy GAMBIT_DIRECTORY GAMBIT_FILES_OR_DIRECTORY  # to tidy code using cmake information
gambit-style ci GAMBIT_FILES_OR_DIRECTORY  # CI check on compliance
```

You can also run these commands on folders, files or lists of files, e.g.,
```bash
gambit-style format .  # format here
gambit-style format this_file.cpp  # only one file
gambit-style format this_file.cpp and_that_file.py  # a list of files and folders
```

Formatting should apply gambit formatting rules to all appropriate files:

- Format C/CXX files by `clang-format`
- PEP8 format Python files by `autopep8`
- Fix file permissions

Tidying, on the other hand, should:

- Analyse files using `clang-tidy` and apply suggestions in place
- Analyse files using `include-what-you-use` but not apply suggestions (as it is quite opinionated)

Linting should provide 

- yamllint
- pylint
- cpplint

suggestions (though note that the cpplint suggestions follow google style guidelines and some filters are disabled).

Finally, the CI checks use

- clang-format
- flake8

## Ignored files

Any `contrib` and `build` directories and any files starting with `.` or inside paths containing directories starting with `.` are ignored.
