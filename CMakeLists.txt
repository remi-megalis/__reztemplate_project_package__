cmake_minimum_required(VERSION 2.8)

include(RezBuild)

file(GLOB_RECURSE py_files "python/*.py")
rez_install_python(
    py
    FILES ${py_files}
    DESTINATION .
    LOCAL_SYMLINK
)

file(GLOB_RECURSE py_files "config/*")
rez_install_python(
    py
    FILES ${py_files}
    DESTINATION .
    LOCAL_SYMLINK
)

file(GLOB_RECURSE py_files "ocio/*")
rez_install_python(
    py
    FILES ${py_files}
    DESTINATION .
    LOCAL_SYMLINK
)

file(GLOB_RECURSE bin_files "bin/*")
rez_install_files(
    ${bin_files}
    DESTINATION .
    EXECUTABLE
)