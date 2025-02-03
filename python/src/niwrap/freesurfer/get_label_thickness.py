# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GET_LABEL_THICKNESS_METADATA = Metadata(
    id="dee540c5d6addffa9eea35a7fd1572afd491a587.boutiques",
    name="get_label_thickness",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
GetLabelThicknessParameters = typing.TypedDict('GetLabelThicknessParameters', {
    "__STYX_TYPE__": typing.Literal["get_label_thickness"],
    "infile": InputPathType,
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
        "get_label_thickness": get_label_thickness_cargs,
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


class GetLabelThicknessOutputs(typing.NamedTuple):
    """
    Output object returned when calling `get_label_thickness(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def get_label_thickness_params(
    infile: InputPathType,
) -> GetLabelThicknessParameters:
    """
    Build parameters.
    
    Args:
        infile: Input file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "get_label_thickness",
        "infile": infile,
    }
    return params


def get_label_thickness_cargs(
    params: GetLabelThicknessParameters,
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
    cargs.append("get_label_thickness")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append("[OPTIONS]")
    return cargs


def get_label_thickness_outputs(
    params: GetLabelThicknessParameters,
    execution: Execution,
) -> GetLabelThicknessOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GetLabelThicknessOutputs(
        root=execution.output_file("."),
    )
    return ret


def get_label_thickness_execute(
    params: GetLabelThicknessParameters,
    execution: Execution,
) -> GetLabelThicknessOutputs:
    """
    Tool to calculate label thickness.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GetLabelThicknessOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = get_label_thickness_cargs(params, execution)
    ret = get_label_thickness_outputs(params, execution)
    execution.run(cargs)
    return ret


def get_label_thickness(
    infile: InputPathType,
    runner: Runner | None = None,
) -> GetLabelThicknessOutputs:
    """
    Tool to calculate label thickness.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetLabelThicknessOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GET_LABEL_THICKNESS_METADATA)
    params = get_label_thickness_params(infile=infile)
    return get_label_thickness_execute(params, execution)


__all__ = [
    "GET_LABEL_THICKNESS_METADATA",
    "GetLabelThicknessOutputs",
    "get_label_thickness",
    "get_label_thickness_params",
]
