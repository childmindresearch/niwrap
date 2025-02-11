# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

THICKDIFFMAP_METADATA = Metadata(
    id="386d35dd120f181e0cd722b783b2ab7dab134ec4.boutiques",
    name="thickdiffmap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ThickdiffmapParameters = typing.TypedDict('ThickdiffmapParameters', {
    "__STYX_TYPE__": typing.Literal["thickdiffmap"],
    "subjscan1": InputPathType,
    "subjscan2": InputPathType,
    "commonsubj": str,
    "hemi": str,
    "steps": typing.NotRequired[list[str] | None],
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
        "thickdiffmap": thickdiffmap_cargs,
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
    }.get(t)


class ThickdiffmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `thickdiffmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def thickdiffmap_params(
    subjscan1: InputPathType,
    subjscan2: InputPathType,
    commonsubj: str,
    hemi: str,
    steps: list[str] | None = None,
) -> ThickdiffmapParameters:
    """
    Build parameters.
    
    Args:
        subjscan1: First scan of a subject.
        subjscan2: Second (later) scan of the same subject.
        commonsubj: Subject to use as the common template.
        hemi: Hemisphere to process.
        steps: Stages of processing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "thickdiffmap",
        "subjscan1": subjscan1,
        "subjscan2": subjscan2,
        "commonsubj": commonsubj,
        "hemi": hemi,
    }
    if steps is not None:
        params["steps"] = steps
    return params


def thickdiffmap_cargs(
    params: ThickdiffmapParameters,
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
    cargs.append("thickdiffmap")
    cargs.append(execution.input_file(params.get("subjscan1")))
    cargs.append(execution.input_file(params.get("subjscan2")))
    cargs.append(params.get("commonsubj"))
    cargs.append(params.get("hemi"))
    if params.get("steps") is not None:
        cargs.extend(params.get("steps"))
    return cargs


def thickdiffmap_outputs(
    params: ThickdiffmapParameters,
    execution: Execution,
) -> ThickdiffmapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ThickdiffmapOutputs(
        root=execution.output_file("."),
    )
    return ret


def thickdiffmap_execute(
    params: ThickdiffmapParameters,
    execution: Execution,
) -> ThickdiffmapOutputs:
    """
    Compute and analyze cortical thickness difference maps.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ThickdiffmapOutputs`).
    """
    cargs = thickdiffmap_cargs(params, execution)
    ret = thickdiffmap_outputs(params, execution)
    execution.run(cargs)
    return ret


def thickdiffmap(
    subjscan1: InputPathType,
    subjscan2: InputPathType,
    commonsubj: str,
    hemi: str,
    steps: list[str] | None = None,
    runner: Runner | None = None,
) -> ThickdiffmapOutputs:
    """
    Compute and analyze cortical thickness difference maps.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjscan1: First scan of a subject.
        subjscan2: Second (later) scan of the same subject.
        commonsubj: Subject to use as the common template.
        hemi: Hemisphere to process.
        steps: Stages of processing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ThickdiffmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(THICKDIFFMAP_METADATA)
    params = thickdiffmap_params(subjscan1=subjscan1, subjscan2=subjscan2, commonsubj=commonsubj, hemi=hemi, steps=steps)
    return thickdiffmap_execute(params, execution)


__all__ = [
    "THICKDIFFMAP_METADATA",
    "ThickdiffmapOutputs",
    "ThickdiffmapParameters",
    "thickdiffmap",
    "thickdiffmap_params",
]
