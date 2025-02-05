# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RMZ_METADATA = Metadata(
    id="22b10eb7b144fa126d7ddab3cdc645947980a96b.boutiques",
    name="rmz",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
RmzParameters = typing.TypedDict('RmzParameters', {
    "__STYX_TYPE__": typing.Literal["rmz"],
    "quiet": bool,
    "hash_flag": typing.NotRequired[float | None],
    "keep_flag": bool,
    "filenames": list[InputPathType],
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
        "rmz": rmz_cargs,
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


class RmzOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rmz(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rmz_params(
    filenames: list[InputPathType],
    quiet: bool = False,
    hash_flag: float | None = None,
    keep_flag: bool = False,
) -> RmzParameters:
    """
    Build parameters.
    
    Args:
        filenames: Files to zero out and remove.
        quiet: Quiet mode.
        hash_flag: Number of times to zero out the files.
        keep_flag: Keep the files instead of removing them.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rmz",
        "quiet": quiet,
        "keep_flag": keep_flag,
        "filenames": filenames,
    }
    if hash_flag is not None:
        params["hash_flag"] = hash_flag
    return params


def rmz_cargs(
    params: RmzParameters,
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
    cargs.append("rmz")
    if params.get("quiet"):
        cargs.append("-q")
    if params.get("hash_flag") is not None:
        cargs.extend([
            "-#",
            str(params.get("hash_flag"))
        ])
    if params.get("keep_flag"):
        cargs.append("-k")
    cargs.extend([execution.input_file(f) for f in params.get("filenames")])
    return cargs


def rmz_outputs(
    params: RmzParameters,
    execution: Execution,
) -> RmzOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RmzOutputs(
        root=execution.output_file("."),
    )
    return ret


def rmz_execute(
    params: RmzParameters,
    execution: Execution,
) -> RmzOutputs:
    """
    Zeros out files before removing them.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RmzOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = rmz_cargs(params, execution)
    ret = rmz_outputs(params, execution)
    execution.run(cargs)
    return ret


def rmz(
    filenames: list[InputPathType],
    quiet: bool = False,
    hash_flag: float | None = None,
    keep_flag: bool = False,
    runner: Runner | None = None,
) -> RmzOutputs:
    """
    Zeros out files before removing them.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        filenames: Files to zero out and remove.
        quiet: Quiet mode.
        hash_flag: Number of times to zero out the files.
        keep_flag: Keep the files instead of removing them.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RmzOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RMZ_METADATA)
    params = rmz_params(quiet=quiet, hash_flag=hash_flag, keep_flag=keep_flag, filenames=filenames)
    return rmz_execute(params, execution)


__all__ = [
    "RMZ_METADATA",
    "RmzOutputs",
    "RmzParameters",
    "rmz",
    "rmz_params",
]
