# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DIFF_FILES_METADATA = Metadata(
    id="edd2d42b0097cf74079def4a47b5ad005afd8f78.boutiques",
    name="@diff.files",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDiffFilesParameters = typing.TypedDict('VDiffFilesParameters', {
    "__STYX_TYPE__": typing.Literal["@diff.files"],
    "files": list[str],
    "old_dir": str,
    "diff_opts": typing.NotRequired[str | None],
    "diff_prog": typing.NotRequired[str | None],
    "ignore_missing": bool,
    "longlist": bool,
    "save": bool,
    "show": bool,
    "xxdiff": bool,
    "X_flag": bool,
    "verbosity": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "@diff.files": v__diff_files_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {}
    return vt.get(t)


class VDiffFilesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__diff_files(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__diff_files_params(
    files: list[str],
    old_dir: str,
    diff_opts: str | None = None,
    diff_prog: str | None = None,
    ignore_missing: bool = False,
    longlist: bool = False,
    save: bool = False,
    show: bool = False,
    xxdiff: bool = False,
    x_flag: bool = False,
    verbosity: float | None = None,
) -> VDiffFilesParameters:
    """
    Build parameters.
    
    Args:
        files: List of files to compare.
        old_dir: Directory containing the files to compare against.
        diff_opts: Add options to diff command (e.g., -w).
        diff_prog: Display diffs using a specified program (e.g., meld, xxdiff).
        ignore_missing: Continue even if files are missing.
        longlist: Run 'ls -l' on both directories instead of listing files.
        save: Create PDFs of diffs.
        show: Show diffs using 'diff'.
        xxdiff: Show diffs using 'xxdiff'.
        x_flag: Implies -xxdiff and -ignore_missing.
        verbosity: Set verbosity level (2 or 3).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@diff.files",
        "files": files,
        "old_dir": old_dir,
        "ignore_missing": ignore_missing,
        "longlist": longlist,
        "save": save,
        "show": show,
        "xxdiff": xxdiff,
        "X_flag": x_flag,
    }
    if diff_opts is not None:
        params["diff_opts"] = diff_opts
    if diff_prog is not None:
        params["diff_prog"] = diff_prog
    if verbosity is not None:
        params["verbosity"] = verbosity
    return params


def v__diff_files_cargs(
    params: VDiffFilesParameters,
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
    cargs.append("@diff.files")
    cargs.extend(params.get("files"))
    cargs.append(params.get("old_dir"))
    if params.get("diff_opts") is not None:
        cargs.extend([
            "-diff_opts",
            params.get("diff_opts")
        ])
    if params.get("diff_prog") is not None:
        cargs.extend([
            "-diff_prog",
            params.get("diff_prog")
        ])
    if params.get("ignore_missing"):
        cargs.append("-ignore_missing")
    if params.get("longlist"):
        cargs.append("-longlist")
    if params.get("save"):
        cargs.append("-save")
    if params.get("show"):
        cargs.append("-show")
    if params.get("xxdiff"):
        cargs.append("-xxdiff")
    if params.get("X_flag"):
        cargs.append("-X")
    if params.get("verbosity") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbosity"))
        ])
    return cargs


def v__diff_files_outputs(
    params: VDiffFilesParameters,
    execution: Execution,
) -> VDiffFilesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDiffFilesOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__diff_files_execute(
    params: VDiffFilesParameters,
    execution: Execution,
) -> VDiffFilesOutputs:
    """
    Show file differences (between specified files and those in another directory).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDiffFilesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__diff_files_cargs(params, execution)
    ret = v__diff_files_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__diff_files(
    files: list[str],
    old_dir: str,
    diff_opts: str | None = None,
    diff_prog: str | None = None,
    ignore_missing: bool = False,
    longlist: bool = False,
    save: bool = False,
    show: bool = False,
    xxdiff: bool = False,
    x_flag: bool = False,
    verbosity: float | None = None,
    runner: Runner | None = None,
) -> VDiffFilesOutputs:
    """
    Show file differences (between specified files and those in another directory).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        files: List of files to compare.
        old_dir: Directory containing the files to compare against.
        diff_opts: Add options to diff command (e.g., -w).
        diff_prog: Display diffs using a specified program (e.g., meld, xxdiff).
        ignore_missing: Continue even if files are missing.
        longlist: Run 'ls -l' on both directories instead of listing files.
        save: Create PDFs of diffs.
        show: Show diffs using 'diff'.
        xxdiff: Show diffs using 'xxdiff'.
        x_flag: Implies -xxdiff and -ignore_missing.
        verbosity: Set verbosity level (2 or 3).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDiffFilesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DIFF_FILES_METADATA)
    params = v__diff_files_params(files=files, old_dir=old_dir, diff_opts=diff_opts, diff_prog=diff_prog, ignore_missing=ignore_missing, longlist=longlist, save=save, show=show, xxdiff=xxdiff, x_flag=x_flag, verbosity=verbosity)
    return v__diff_files_execute(params, execution)


__all__ = [
    "VDiffFilesOutputs",
    "VDiffFilesParameters",
    "V__DIFF_FILES_METADATA",
    "v__diff_files",
    "v__diff_files_params",
]
