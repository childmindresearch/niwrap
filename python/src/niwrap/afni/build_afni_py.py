# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BUILD_AFNI_PY_METADATA = Metadata(
    id="1431d3090595ab0d8fddc25b853a7cd1f4d39994",
    name="build_afni.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class BuildAfniPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `build_afni_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    command_history_file: OutputPathType
    """Command history file"""
    screen_output_history: OutputPathType
    """Screen output history file"""


def build_afni_py(
    build_root: str,
    clean_root: str | None = None,
    git_branch: str | None = None,
    git_tag: str | None = None,
    git_update: str | None = None,
    make_target: str | None = None,
    makefile: str | None = None,
    package: str | None = None,
    prep_only: bool = False,
    run_cmake: str | None = None,
    run_make: str | None = None,
    verbose_level: float | int | None = None,
    help_: bool = False,
    history: bool = False,
    show_valid_opts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> BuildAfniPyOutputs:
    """
    build_afni.py by AFNI Team.
    
    Compile an AFNI package from the git repository.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/build_afni.py.html
    
    Args:
        build_root: Root directory to use for git and building.
        clean_root: Specify whether to clean up the build_root. Default is yes.
        git_branch: Specify a branch to checkout in git. Default is master.
        git_tag: Specify a tag to checkout in git. Default is LAST_TAG.
        git_update: Specify whether to update git repo. Default is yes.
        make_target: Specify target for make command. Default is itall.
        makefile: Specify an alternate Makefile to build from.
        package: Specify the desired package to build.
        prep_only: Prepare to but do not run (c)make.
        run_cmake: Choose whether to run a cmake build. Default is no.
        run_make: Choose whether to run a make build. Default is yes.
        verbose_level: Set the verbosity level. Default is 1.
        help_: Show help message.
        history: Show module history.
        show_valid_opts: List valid options.
        version: Show the current version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BuildAfniPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BUILD_AFNI_PY_METADATA)
    cargs = []
    cargs.append("build_afni.py")
    cargs.append("-build_root")
    cargs.append(build_root)
    if clean_root is not None:
        cargs.extend(["-clean_root", clean_root])
    if git_branch is not None:
        cargs.extend(["-git_branch", git_branch])
    if git_tag is not None:
        cargs.extend(["-git_tag", git_tag])
    if git_update is not None:
        cargs.extend(["-git_update", git_update])
    if make_target is not None:
        cargs.extend(["-make_target", make_target])
    if makefile is not None:
        cargs.extend(["-makefile", makefile])
    if package is not None:
        cargs.extend(["-package", package])
    if prep_only:
        cargs.append("-prep_only")
    if run_cmake is not None:
        cargs.extend(["-run_cmake", run_cmake])
    if run_make is not None:
        cargs.extend(["-run_make", run_make])
    if verbose_level is not None:
        cargs.extend(["-verb", str(verbose_level)])
    if version:
        cargs.append("-ver")
    ret = BuildAfniPyOutputs(
        root=execution.output_file("."),
        command_history_file=execution.output_file(f"{build_root}/hist_commands.txt", optional=True),
        screen_output_history=execution.output_file(f"{build_root}/screen_output_history.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BUILD_AFNI_PY_METADATA",
    "BuildAfniPyOutputs",
    "build_afni_py",
]
