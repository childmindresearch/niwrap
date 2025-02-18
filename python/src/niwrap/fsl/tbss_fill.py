# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TBSS_FILL_METADATA = Metadata(
    id="302dc5d0a540004a061db44ab4beabb876bbf335.boutiques",
    name="tbss_fill",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
TbssFillParameters = typing.TypedDict('TbssFillParameters', {
    "__STYX_TYPE__": typing.Literal["tbss_fill"],
    "stats_image": InputPathType,
    "threshold": float,
    "mean_fa": InputPathType,
    "output": str,
    "include_negative_flag": bool,
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
        "tbss_fill": tbss_fill_cargs,
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
        "tbss_fill": tbss_fill_outputs,
    }.get(t)


class TbssFillOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_fill(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filled_skeleton: OutputPathType
    """Filled skeletonized FA image"""


def tbss_fill_params(
    stats_image: InputPathType,
    threshold: float,
    mean_fa: InputPathType,
    output: str,
    include_negative_flag: bool = False,
) -> TbssFillParameters:
    """
    Build parameters.
    
    Args:
        stats_image: Stats image.
        threshold: Threshold value.
        mean_fa: Mean FA image.
        output: Output image.
        include_negative_flag: Include negative stat values (below -threshold).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tbss_fill",
        "stats_image": stats_image,
        "threshold": threshold,
        "mean_fa": mean_fa,
        "output": output,
        "include_negative_flag": include_negative_flag,
    }
    return params


def tbss_fill_cargs(
    params: TbssFillParameters,
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
    cargs.append("tbss_fill")
    cargs.append(execution.input_file(params.get("stats_image")))
    cargs.append(str(params.get("threshold")))
    cargs.append(execution.input_file(params.get("mean_fa")))
    cargs.append(params.get("output"))
    if params.get("include_negative_flag"):
        cargs.append("-n")
    return cargs


def tbss_fill_outputs(
    params: TbssFillParameters,
    execution: Execution,
) -> TbssFillOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TbssFillOutputs(
        root=execution.output_file("."),
        filled_skeleton=execution.output_file(params.get("output")),
    )
    return ret


def tbss_fill_execute(
    params: TbssFillParameters,
    execution: Execution,
) -> TbssFillOutputs:
    """
    Tool for filling skeletonized FA images in TBSS.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TbssFillOutputs`).
    """
    params = execution.params(params)
    cargs = tbss_fill_cargs(params, execution)
    ret = tbss_fill_outputs(params, execution)
    execution.run(cargs)
    return ret


def tbss_fill(
    stats_image: InputPathType,
    threshold: float,
    mean_fa: InputPathType,
    output: str,
    include_negative_flag: bool = False,
    runner: Runner | None = None,
) -> TbssFillOutputs:
    """
    Tool for filling skeletonized FA images in TBSS.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        stats_image: Stats image.
        threshold: Threshold value.
        mean_fa: Mean FA image.
        output: Output image.
        include_negative_flag: Include negative stat values (below -threshold).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TbssFillOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_FILL_METADATA)
    params = tbss_fill_params(stats_image=stats_image, threshold=threshold, mean_fa=mean_fa, output=output, include_negative_flag=include_negative_flag)
    return tbss_fill_execute(params, execution)


__all__ = [
    "TBSS_FILL_METADATA",
    "TbssFillOutputs",
    "TbssFillParameters",
    "tbss_fill",
    "tbss_fill_params",
]
