# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_FIND_FLAT_REGIONS_METADATA = Metadata(
    id="5c7cb3d5470380e27f2e79106dbfa81d9cc3d3a9.boutiques",
    name="mris_find_flat_regions",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisFindFlatRegionsParameters = typing.TypedDict('MrisFindFlatRegionsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_find_flat_regions"],
    "surface": InputPathType,
    "wfile": str,
    "threshold": typing.NotRequired[float | None],
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
        "mris_find_flat_regions": mris_find_flat_regions_cargs,
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
        "mris_find_flat_regions": mris_find_flat_regions_outputs,
    }.get(t)


class MrisFindFlatRegionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_find_flat_regions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """Output label file with regions where the surface is almost perpendicular
    to one of the cardinal axes"""


def mris_find_flat_regions_params(
    surface: InputPathType,
    wfile: str,
    threshold: float | None = 0.99,
) -> MrisFindFlatRegionsParameters:
    """
    Build parameters.
    
    Args:
        surface: Surface input file.
        wfile: Output label file.
        threshold: Threshold to use (default=0.990).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_find_flat_regions",
        "surface": surface,
        "wfile": wfile,
    }
    if threshold is not None:
        params["threshold"] = threshold
    return params


def mris_find_flat_regions_cargs(
    params: MrisFindFlatRegionsParameters,
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
    cargs.append("mris_find_flat_regions")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(params.get("wfile"))
    if params.get("threshold") is not None:
        cargs.extend([
            "-t",
            str(params.get("threshold"))
        ])
    return cargs


def mris_find_flat_regions_outputs(
    params: MrisFindFlatRegionsParameters,
    execution: Execution,
) -> MrisFindFlatRegionsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisFindFlatRegionsOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(params.get("wfile")),
    )
    return ret


def mris_find_flat_regions_execute(
    params: MrisFindFlatRegionsParameters,
    execution: Execution,
) -> MrisFindFlatRegionsOutputs:
    """
    Compute regions in which the surface is almost perpendicular to one of the
    cardinal axes and write the results to a label file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisFindFlatRegionsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_find_flat_regions_cargs(params, execution)
    ret = mris_find_flat_regions_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_find_flat_regions(
    surface: InputPathType,
    wfile: str,
    threshold: float | None = 0.99,
    runner: Runner | None = None,
) -> MrisFindFlatRegionsOutputs:
    """
    Compute regions in which the surface is almost perpendicular to one of the
    cardinal axes and write the results to a label file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Surface input file.
        wfile: Output label file.
        threshold: Threshold to use (default=0.990).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisFindFlatRegionsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_FIND_FLAT_REGIONS_METADATA)
    params = mris_find_flat_regions_params(surface=surface, wfile=wfile, threshold=threshold)
    return mris_find_flat_regions_execute(params, execution)


__all__ = [
    "MRIS_FIND_FLAT_REGIONS_METADATA",
    "MrisFindFlatRegionsOutputs",
    "MrisFindFlatRegionsParameters",
    "mris_find_flat_regions",
    "mris_find_flat_regions_params",
]
