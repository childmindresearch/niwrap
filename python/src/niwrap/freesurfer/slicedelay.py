# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SLICEDELAY_METADATA = Metadata(
    id="e0e78eeb6a32014e4f62ce730e136633e9ef9494.boutiques",
    name="slicedelay",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SlicedelayParameters = typing.TypedDict('SlicedelayParameters', {
    "__STYX_TYPE__": typing.Literal["slicedelay"],
    "slicedelayfile": str,
    "nslices": float,
    "order": typing.Literal["up", "down", "odd", "even", "siemens"],
    "ngroups": float,
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
        "slicedelay": slicedelay_cargs,
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
        "slicedelay": slicedelay_outputs,
    }.get(t)


class SlicedelayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicedelay(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    slicedelayfile: OutputPathType
    """The generated slice delay file"""


def slicedelay_params(
    slicedelayfile: str,
    nslices: float,
    order: typing.Literal["up", "down", "odd", "even", "siemens"],
    ngroups: float,
) -> SlicedelayParameters:
    """
    Build parameters.
    
    Args:
        slicedelayfile: Output file for the custom slice delay.
        nslices: Total number of slices in the volume.
        order: Order of slices (up, down, odd, even, siemens).
        ngroups: Number of slice groups for SMS.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "slicedelay",
        "slicedelayfile": slicedelayfile,
        "nslices": nslices,
        "order": order,
        "ngroups": ngroups,
    }
    return params


def slicedelay_cargs(
    params: SlicedelayParameters,
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
    cargs.append("slicedelay")
    cargs.extend([
        "--o",
        params.get("slicedelayfile")
    ])
    cargs.extend([
        "--nslices",
        str(params.get("nslices"))
    ])
    cargs.extend([
        "--order",
        params.get("order")
    ])
    cargs.extend([
        "--ngroups",
        str(params.get("ngroups"))
    ])
    return cargs


def slicedelay_outputs(
    params: SlicedelayParameters,
    execution: Execution,
) -> SlicedelayOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SlicedelayOutputs(
        root=execution.output_file("."),
        slicedelayfile=execution.output_file(params.get("slicedelayfile")),
    )
    return ret


def slicedelay_execute(
    params: SlicedelayParameters,
    execution: Execution,
) -> SlicedelayOutputs:
    """
    Creates an FSL custom slice delay file for use with slicetimer for slice-time
    correction of fMRI.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SlicedelayOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = slicedelay_cargs(params, execution)
    ret = slicedelay_outputs(params, execution)
    execution.run(cargs)
    return ret


def slicedelay(
    slicedelayfile: str,
    nslices: float,
    order: typing.Literal["up", "down", "odd", "even", "siemens"],
    ngroups: float,
    runner: Runner | None = None,
) -> SlicedelayOutputs:
    """
    Creates an FSL custom slice delay file for use with slicetimer for slice-time
    correction of fMRI.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        slicedelayfile: Output file for the custom slice delay.
        nslices: Total number of slices in the volume.
        order: Order of slices (up, down, odd, even, siemens).
        ngroups: Number of slice groups for SMS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicedelayOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICEDELAY_METADATA)
    params = slicedelay_params(slicedelayfile=slicedelayfile, nslices=nslices, order=order, ngroups=ngroups)
    return slicedelay_execute(params, execution)


__all__ = [
    "SLICEDELAY_METADATA",
    "SlicedelayOutputs",
    "SlicedelayParameters",
    "slicedelay",
    "slicedelay_params",
]
