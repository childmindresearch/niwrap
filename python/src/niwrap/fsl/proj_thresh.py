# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PROJ_THRESH_METADATA = Metadata(
    id="2118a504958e3891bd47708738d41c67d1537eb5.boutiques",
    name="proj_thresh",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
ProjThreshParameters = typing.TypedDict('ProjThreshParameters', {
    "__STYX_TYPE__": typing.Literal["proj_thresh"],
    "input_paths": list[InputPathType],
    "threshold": float,
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
        "proj_thresh": proj_thresh_cargs,
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


class ProjThreshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `proj_thresh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def proj_thresh_params(
    input_paths: list[InputPathType],
    threshold: float,
) -> ProjThreshParameters:
    """
    Build parameters.
    
    Args:
        input_paths: Paths to volume or surface files. Please use either\
            volumes or surfaces but not both.
        threshold: Threshold value to be applied.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "proj_thresh",
        "input_paths": input_paths,
        "threshold": threshold,
    }
    return params


def proj_thresh_cargs(
    params: ProjThreshParameters,
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
    cargs.append("proj_thresh")
    cargs.extend([execution.input_file(f) for f in params.get("input_paths")])
    cargs.append(str(params.get("threshold")))
    return cargs


def proj_thresh_outputs(
    params: ProjThreshParameters,
    execution: Execution,
) -> ProjThreshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ProjThreshOutputs(
        root=execution.output_file("."),
    )
    return ret


def proj_thresh_execute(
    params: ProjThreshParameters,
    execution: Execution,
) -> ProjThreshOutputs:
    """
    A tool to apply a threshold to either volumes or surfaces.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ProjThreshOutputs`).
    """
    cargs = proj_thresh_cargs(params, execution)
    ret = proj_thresh_outputs(params, execution)
    execution.run(cargs)
    return ret


def proj_thresh(
    input_paths: list[InputPathType],
    threshold: float,
    runner: Runner | None = None,
) -> ProjThreshOutputs:
    """
    A tool to apply a threshold to either volumes or surfaces.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_paths: Paths to volume or surface files. Please use either\
            volumes or surfaces but not both.
        threshold: Threshold value to be applied.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ProjThreshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PROJ_THRESH_METADATA)
    params = proj_thresh_params(input_paths=input_paths, threshold=threshold)
    return proj_thresh_execute(params, execution)


__all__ = [
    "PROJ_THRESH_METADATA",
    "ProjThreshOutputs",
    "ProjThreshParameters",
    "proj_thresh",
    "proj_thresh_params",
]
