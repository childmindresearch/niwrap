# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BUILD_AFNI_PY_METADATA = Metadata(
    id="8b01bbfc26acb4a73b16110f6849bc381629f972.boutiques",
    name="build_afni.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
BuildAfniPyParameters = typing.TypedDict('BuildAfniPyParameters', {
    "__STYX_TYPE__": typing.Literal["build_afni.py"],
    "build_root": str,
    "clean_root": typing.NotRequired[str | None],
    "git_branch": typing.NotRequired[str | None],
    "git_tag": typing.NotRequired[str | None],
    "git_update": typing.NotRequired[str | None],
    "make_target": typing.NotRequired[str | None],
    "makefile": typing.NotRequired[str | None],
    "package": typing.NotRequired[str | None],
    "prep_only": bool,
    "run_cmake": typing.NotRequired[str | None],
    "run_make": typing.NotRequired[str | None],
    "verbose_level": typing.NotRequired[float | None],
    "version": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "build_afni.py": build_afni_py_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "build_afni.py": build_afni_py_outputs,
    }.get(t)


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


def build_afni_py_params(
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
    verbose_level: float | None = None,
    version: bool = False,
) -> BuildAfniPyParameters:
    """
    Build parameters.
    
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
        version: Show the current version.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "build_afni.py",
        "build_root": build_root,
        "prep_only": prep_only,
        "version": version,
    }
    if clean_root is not None:
        params["clean_root"] = clean_root
    if git_branch is not None:
        params["git_branch"] = git_branch
    if git_tag is not None:
        params["git_tag"] = git_tag
    if git_update is not None:
        params["git_update"] = git_update
    if make_target is not None:
        params["make_target"] = make_target
    if makefile is not None:
        params["makefile"] = makefile
    if package is not None:
        params["package"] = package
    if run_cmake is not None:
        params["run_cmake"] = run_cmake
    if run_make is not None:
        params["run_make"] = run_make
    if verbose_level is not None:
        params["verbose_level"] = verbose_level
    return params


def build_afni_py_cargs(
    params: BuildAfniPyParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("build_afni.py")
    cargs.extend([
        "-build_root",
        params.get("build_root")
    ])
    if params.get("clean_root") is not None:
        cargs.extend([
            "-clean_root",
            params.get("clean_root")
        ])
    if params.get("git_branch") is not None:
        cargs.extend([
            "-git_branch",
            params.get("git_branch")
        ])
    if params.get("git_tag") is not None:
        cargs.extend([
            "-git_tag",
            params.get("git_tag")
        ])
    if params.get("git_update") is not None:
        cargs.extend([
            "-git_update",
            params.get("git_update")
        ])
    if params.get("make_target") is not None:
        cargs.extend([
            "-make_target",
            params.get("make_target")
        ])
    if params.get("makefile") is not None:
        cargs.extend([
            "-makefile",
            params.get("makefile")
        ])
    if params.get("package") is not None:
        cargs.extend([
            "-package",
            params.get("package")
        ])
    if params.get("prep_only"):
        cargs.append("-prep_only")
    if params.get("run_cmake") is not None:
        cargs.extend([
            "-run_cmake",
            params.get("run_cmake")
        ])
    if params.get("run_make") is not None:
        cargs.extend([
            "-run_make",
            params.get("run_make")
        ])
    if params.get("verbose_level") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbose_level"))
        ])
    if params.get("version"):
        cargs.append("-ver")
    return cargs


def build_afni_py_outputs(
    params: BuildAfniPyParameters,
    execution: Execution,
) -> BuildAfniPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BuildAfniPyOutputs(
        root=execution.output_file("."),
        command_history_file=execution.output_file(params.get("build_root") + "/hist_commands.txt"),
        screen_output_history=execution.output_file(params.get("build_root") + "/screen_output_history.txt"),
    )
    return ret


def build_afni_py_execute(
    params: BuildAfniPyParameters,
    execution: Execution,
) -> BuildAfniPyOutputs:
    """
    Compile an AFNI package from the git repository.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BuildAfniPyOutputs`).
    """
    cargs = build_afni_py_cargs(params, execution)
    ret = build_afni_py_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    verbose_level: float | None = None,
    version: bool = False,
    runner: Runner | None = None,
) -> BuildAfniPyOutputs:
    """
    Compile an AFNI package from the git repository.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
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
        version: Show the current version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BuildAfniPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BUILD_AFNI_PY_METADATA)
    params = build_afni_py_params(build_root=build_root, clean_root=clean_root, git_branch=git_branch, git_tag=git_tag, git_update=git_update, make_target=make_target, makefile=makefile, package=package, prep_only=prep_only, run_cmake=run_cmake, run_make=run_make, verbose_level=verbose_level, version=version)
    return build_afni_py_execute(params, execution)


__all__ = [
    "BUILD_AFNI_PY_METADATA",
    "BuildAfniPyOutputs",
    "BuildAfniPyParameters",
    "build_afni_py",
    "build_afni_py_params",
]
