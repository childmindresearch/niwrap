# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TRFIX_METADATA = Metadata(
    id="a34882bc067ee157a81c8d48c065fa3edac1cdc8.boutiques",
    name="3dTRfix",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dTrfixParameters = typing.TypedDict('V3dTrfixParameters', {
    "__STYX_TYPE__": typing.Literal["3dTRfix"],
    "input_file": InputPathType,
    "tr_list": typing.NotRequired[InputPathType | None],
    "time_list": typing.NotRequired[InputPathType | None],
    "prefix": str,
    "output_tr": typing.NotRequired[float | None],
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
        "3dTRfix": v_3d_trfix_cargs,
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
        "3dTRfix": v_3d_trfix_outputs,
    }.get(t)


class V3dTrfixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_trfix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file_head: OutputPathType
    """Output dataset header file"""
    output_file_brik: OutputPathType
    """Output dataset brik file"""


def v_3d_trfix_params(
    input_file: InputPathType,
    prefix: str,
    tr_list: InputPathType | None = None,
    time_list: InputPathType | None = None,
    output_tr: float | None = None,
) -> V3dTrfixParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input dataset.
        prefix: Prefix name for output dataset.
        tr_list: File of time gaps between sub-bricks in input dataset.
        time_list: File with times at each sub-brick in the input dataset.
        output_tr: TR value for output dataset (in seconds).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTRfix",
        "input_file": input_file,
        "prefix": prefix,
    }
    if tr_list is not None:
        params["tr_list"] = tr_list
    if time_list is not None:
        params["time_list"] = time_list
    if output_tr is not None:
        params["output_tr"] = output_tr
    return params


def v_3d_trfix_cargs(
    params: V3dTrfixParameters,
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
    cargs.append("3dTRfix")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("tr_list") is not None:
        cargs.extend([
            "-TRlist",
            execution.input_file(params.get("tr_list"))
        ])
    if params.get("time_list") is not None:
        cargs.extend([
            "-TIMElist",
            execution.input_file(params.get("time_list"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("output_tr") is not None:
        cargs.extend([
            "-TRout",
            str(params.get("output_tr"))
        ])
    return cargs


def v_3d_trfix_outputs(
    params: V3dTrfixParameters,
    execution: Execution,
) -> V3dTrfixOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTrfixOutputs(
        root=execution.output_file("."),
        output_file_head=execution.output_file(params.get("prefix") + "+orig.HEAD"),
        output_file_brik=execution.output_file(params.get("prefix") + "+orig.BRIK"),
    )
    return ret


def v_3d_trfix_execute(
    params: V3dTrfixParameters,
    execution: Execution,
) -> V3dTrfixOutputs:
    """
    Re-sample dataset with irregular time grid to regular time grid via linear
    interpolation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTrfixOutputs`).
    """
    cargs = v_3d_trfix_cargs(params, execution)
    ret = v_3d_trfix_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_trfix(
    input_file: InputPathType,
    prefix: str,
    tr_list: InputPathType | None = None,
    time_list: InputPathType | None = None,
    output_tr: float | None = None,
    runner: Runner | None = None,
) -> V3dTrfixOutputs:
    """
    Re-sample dataset with irregular time grid to regular time grid via linear
    interpolation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input dataset.
        prefix: Prefix name for output dataset.
        tr_list: File of time gaps between sub-bricks in input dataset.
        time_list: File with times at each sub-brick in the input dataset.
        output_tr: TR value for output dataset (in seconds).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTrfixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TRFIX_METADATA)
    params = v_3d_trfix_params(input_file=input_file, tr_list=tr_list, time_list=time_list, prefix=prefix, output_tr=output_tr)
    return v_3d_trfix_execute(params, execution)


__all__ = [
    "V3dTrfixOutputs",
    "V3dTrfixParameters",
    "V_3D_TRFIX_METADATA",
    "v_3d_trfix",
    "v_3d_trfix_params",
]
