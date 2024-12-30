# Install

    pipx install git+https://github.com/GambitBSM/gambit-style

# Use

    gambit-style format GAMBIT_DIRECTORY  # to format in place 
    gambit-style lint GAMBIT_DIRECTORY  # to provide lint suggestions
    
You can also run these commands on folders, files or lists of files, e.g.,

    gambit-style format .  # format here
    gambit-style format this_file.cpp
    gambit-style format this_file.cpp and_that_file.py

Formatting should apply gambit formatting rules to all appropriate files:

- clang-format C/CXX files
- PEP8 format Python files
- Fix file permissions

Linting should provide yamllint, pylint and cpplint suggestions (though note that the cpplint suggestions follow google style guidelines):

# Ignoring files

When running over a GAMBIT directory, contrib and any paths or folders tarting with . are ignored.
