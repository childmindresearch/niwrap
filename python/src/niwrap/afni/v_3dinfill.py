# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DINFILL_METADATA = Metadata(
    id="263217e116d12496939583b1c3c4001f87f5e06c.boutiques",
    name="3dinfill",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dinfillParameters = typing.TypedDict('V3dinfillParameters', {
    "__STYX_TYPE__": typing.Literal["3dinfill"],
    "input": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "niter": typing.NotRequired[float | None],
    "blend": typing.NotRequired[typing.Literal["MODE", "AVG", "AUTO", "SOLID", "SOLID_CLEAN"] | None],
    "minhits": typing.NotRequired[float | None],
    "ed": typing.NotRequired[list[float] | None],
    "mask": typing.NotRequired[InputPathType | None],
    "mask_range": typing.NotRequired[list[float] | None],
    "mrange": typing.NotRequired[list[float] | None],
    "cmask": typing.NotRequired[str | None],
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
        "3dinfill": v_3dinfill_cargs,
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
        "3dinfill": v_3dinfill_outputs,
    }.get(t)


class V3dinfillOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dinfill(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_filled: OutputPathType | None
    """Filled volume output"""


def v_3dinfill_params(
    input_: InputPathType,
    prefix: str | None = None,
    niter: float | None = None,
    blend: typing.Literal["MODE", "AVG", "AUTO", "SOLID", "SOLID_CLEAN"] | None = None,
    minhits: float | None = None,
    ed: list[float] | None = None,
    mask: InputPathType | None = None,
    mask_range: list[float] | None = None,
    mrange: list[float] | None = None,
    cmask: str | None = None,
) -> V3dinfillParameters:
    """
    Build parameters.
    
    Args:
        input_: Fill volume dataset.
        prefix: Use PREF for output prefix.
        niter: Do not allow the fill function to do more than NITER passes.
        blend: Method for assigning a value to a hole.
        minhits: Criterion for considering a zero voxel to be a hole. Can only\
            be used with -blend SOLID.
        ed: Erode N times then dilate N times to get rid of hanging chunks.\
            Values filled in by this process get value V.
        mask: Provide mask dataset to select subset of input.
        mask_range: Specify the range of values to consider from mask dataset.
        mrange: Alias for -mask_range option.
        cmask: Provide cmask expression. Voxels where expression is 0 are\
            excluded from computations.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dinfill",
        "input": input_,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if niter is not None:
        params["niter"] = niter
    if blend is not None:
        params["blend"] = blend
    if minhits is not None:
        params["minhits"] = minhits
    if ed is not None:
        params["ed"] = ed
    if mask is not None:
        params["mask"] = mask
    if mask_range is not None:
        params["mask_range"] = mask_range
    if mrange is not None:
        params["mrange"] = mrange
    if cmask is not None:
        params["cmask"] = cmask
    return params


def v_3dinfill_cargs(
    params: V3dinfillParameters,
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
    cargs.append("3dinfill")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input"))
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("niter") is not None:
        cargs.extend([
            "-Niter",
            str(params.get("niter"))
        ])
    if params.get("blend") is not None:
        cargs.extend([
            "-blend",
            params.get("blend")
        ])
    if params.get("minhits") is not None:
        cargs.extend([
            "-minhits",
            str(params.get("minhits"))
        ])
    if params.get("ed") is not None:
        cargs.extend([
            "-ed",
            *map(str, params.get("ed"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("mask_range") is not None:
        cargs.extend([
            "-mask_range",
            *map(str, params.get("mask_range"))
        ])
    if params.get("mrange") is not None:
        cargs.extend([
            "-mrange",
            *map(str, params.get("mrange"))
        ])
    if params.get("cmask") is not None:
        cargs.extend([
            "-cmask",
            params.get("cmask")
        ])
    return cargs


def v_3dinfill_outputs(
    params: V3dinfillParameters,
    execution: Execution,
) -> V3dinfillOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dinfillOutputs(
        root=execution.output_file("."),
        output_filled=execution.output_file(params.get("prefix") + "_filled.nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3dinfill_execute(
    params: V3dinfillParameters,
    execution: Execution,
) -> V3dinfillOutputs:
    """
    A program to fill holes in volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dinfillOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dinfill_cargs(params, execution)
    ret = v_3dinfill_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dinfill(
    input_: InputPathType,
    prefix: str | None = None,
    niter: float | None = None,
    blend: typing.Literal["MODE", "AVG", "AUTO", "SOLID", "SOLID_CLEAN"] | None = None,
    minhits: float | None = None,
    ed: list[float] | None = None,
    mask: InputPathType | None = None,
    mask_range: list[float] | None = None,
    mrange: list[float] | None = None,
    cmask: str | None = None,
    runner: Runner | None = None,
) -> V3dinfillOutputs:
    """
    A program to fill holes in volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Fill volume dataset.
        prefix: Use PREF for output prefix.
        niter: Do not allow the fill function to do more than NITER passes.
        blend: Method for assigning a value to a hole.
        minhits: Criterion for considering a zero voxel to be a hole. Can only\
            be used with -blend SOLID.
        ed: Erode N times then dilate N times to get rid of hanging chunks.\
            Values filled in by this process get value V.
        mask: Provide mask dataset to select subset of input.
        mask_range: Specify the range of values to consider from mask dataset.
        mrange: Alias for -mask_range option.
        cmask: Provide cmask expression. Voxels where expression is 0 are\
            excluded from computations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dinfillOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DINFILL_METADATA)
    params = v_3dinfill_params(input_=input_, prefix=prefix, niter=niter, blend=blend, minhits=minhits, ed=ed, mask=mask, mask_range=mask_range, mrange=mrange, cmask=cmask)
    return v_3dinfill_execute(params, execution)


__all__ = [
    "V3dinfillOutputs",
    "V3dinfillParameters",
    "V_3DINFILL_METADATA",
    "v_3dinfill",
    "v_3dinfill_params",
]
