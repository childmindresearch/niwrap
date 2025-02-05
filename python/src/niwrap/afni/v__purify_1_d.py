# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__PURIFY_1_D_METADATA = Metadata(
    id="f151d6221d30e4482e4401cc1da254b8c8b2ea5b.boutiques",
    name="@Purify_1D",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VPurify1DParameters = typing.TypedDict('VPurify1DParameters', {
    "__STYX_TYPE__": typing.Literal["@Purify_1D"],
    "sub_brick": typing.NotRequired[str | None],
    "suffix": typing.NotRequired[str | None],
    "input_files": list[InputPathType],
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
        "@Purify_1D": v__purify_1_d_cargs,
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


class VPurify1DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__purify_1_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__purify_1_d_params(
    input_files: list[InputPathType],
    sub_brick: str | None = None,
    suffix: str | None = None,
) -> VPurify1DParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input 1D dataset files.
        sub_brick: The sub-brick selection mode to output a select number of\
            columns, following AFNI conventions.
        suffix: STRING is attached to the output prefix which is formed from\
            the input names.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@Purify_1D",
        "input_files": input_files,
    }
    if sub_brick is not None:
        params["sub_brick"] = sub_brick
    if suffix is not None:
        params["suffix"] = suffix
    return params


def v__purify_1_d_cargs(
    params: VPurify1DParameters,
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
    cargs.append("@Purify_1D")
    if params.get("sub_brick") is not None:
        cargs.extend([
            "-sub",
            params.get("sub_brick")
        ])
    if params.get("suffix") is not None:
        cargs.extend([
            "-suf",
            params.get("suffix")
        ])
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def v__purify_1_d_outputs(
    params: VPurify1DParameters,
    execution: Execution,
) -> VPurify1DOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VPurify1DOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__purify_1_d_execute(
    params: VPurify1DParameters,
    execution: Execution,
) -> VPurify1DOutputs:
    """
    Purifies a series of 1D files for faster I/O into matlab.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VPurify1DOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__purify_1_d_cargs(params, execution)
    ret = v__purify_1_d_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__purify_1_d(
    input_files: list[InputPathType],
    sub_brick: str | None = None,
    suffix: str | None = None,
    runner: Runner | None = None,
) -> VPurify1DOutputs:
    """
    Purifies a series of 1D files for faster I/O into matlab.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input 1D dataset files.
        sub_brick: The sub-brick selection mode to output a select number of\
            columns, following AFNI conventions.
        suffix: STRING is attached to the output prefix which is formed from\
            the input names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VPurify1DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__PURIFY_1_D_METADATA)
    params = v__purify_1_d_params(sub_brick=sub_brick, suffix=suffix, input_files=input_files)
    return v__purify_1_d_execute(params, execution)


__all__ = [
    "VPurify1DOutputs",
    "VPurify1DParameters",
    "V__PURIFY_1_D_METADATA",
    "v__purify_1_d",
    "v__purify_1_d_params",
]
