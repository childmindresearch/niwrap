# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SIENA_DIFF_METADATA = Metadata(
    id="e8aca2fd67e31bd3e2c0994ac03b8c6a57e6de78.boutiques",
    name="siena_diff",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SienaDiffParameters = typing.TypedDict('SienaDiffParameters', {
    "__STYX_TYPE__": typing.Literal["siena_diff"],
    "input1_basename": str,
    "input2_basename": str,
    "debug_flag": bool,
    "no_seg_flag": bool,
    "self_corr_factor": typing.NotRequired[float | None],
    "ignore_z_flow_flag": bool,
    "apply_std_mask_flag": bool,
    "segment_options": typing.NotRequired[str | None],
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
        "siena_diff": siena_diff_cargs,
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
        "siena_diff": siena_diff_outputs,
    }.get(t)


class SienaDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `siena_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def siena_diff_params(
    input1_basename: str,
    input2_basename: str,
    debug_flag: bool = False,
    no_seg_flag: bool = False,
    self_corr_factor: float | None = None,
    ignore_z_flow_flag: bool = False,
    apply_std_mask_flag: bool = False,
    segment_options: str | None = None,
) -> SienaDiffParameters:
    """
    Build parameters.
    
    Args:
        input1_basename: Input image 1 basename.
        input2_basename: Input image 2 basename.
        debug_flag: Debug - generate edge images and don't remove temporary\
            images.
        no_seg_flag: Don't segment grey+white separately (because there is poor\
            grey-white contrast).
        self_corr_factor: Apply self-calibrating correction factor.
        ignore_z_flow_flag: Ignore flow in z (may be beneficial if top of brain\
            is missing).
        apply_std_mask_flag: Apply <input1_basename>_stdmask to brain edge\
            points.
        segment_options: Options to be passed to segmentation (type 'fast' to\
            get these).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "siena_diff",
        "input1_basename": input1_basename,
        "input2_basename": input2_basename,
        "debug_flag": debug_flag,
        "no_seg_flag": no_seg_flag,
        "ignore_z_flow_flag": ignore_z_flow_flag,
        "apply_std_mask_flag": apply_std_mask_flag,
    }
    if self_corr_factor is not None:
        params["self_corr_factor"] = self_corr_factor
    if segment_options is not None:
        params["segment_options"] = segment_options
    return params


def siena_diff_cargs(
    params: SienaDiffParameters,
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
    cargs.append("siena_diff")
    cargs.append(params.get("input1_basename"))
    cargs.append(params.get("input2_basename"))
    if params.get("debug_flag"):
        cargs.append("-d")
    if params.get("no_seg_flag"):
        cargs.append("-2")
    if params.get("self_corr_factor") is not None:
        cargs.extend([
            "-c",
            str(params.get("self_corr_factor"))
        ])
    if params.get("ignore_z_flow_flag"):
        cargs.append("-i")
    if params.get("apply_std_mask_flag"):
        cargs.append("-m")
    if params.get("segment_options") is not None:
        cargs.extend([
            "-s",
            params.get("segment_options")
        ])
    return cargs


def siena_diff_outputs(
    params: SienaDiffParameters,
    execution: Execution,
) -> SienaDiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SienaDiffOutputs(
        root=execution.output_file("."),
    )
    return ret


def siena_diff_execute(
    params: SienaDiffParameters,
    execution: Execution,
) -> SienaDiffOutputs:
    """
    SIENA_diff: Analysis of longitudinal brain image differences.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SienaDiffOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = siena_diff_cargs(params, execution)
    ret = siena_diff_outputs(params, execution)
    execution.run(cargs)
    return ret


def siena_diff(
    input1_basename: str,
    input2_basename: str,
    debug_flag: bool = False,
    no_seg_flag: bool = False,
    self_corr_factor: float | None = None,
    ignore_z_flow_flag: bool = False,
    apply_std_mask_flag: bool = False,
    segment_options: str | None = None,
    runner: Runner | None = None,
) -> SienaDiffOutputs:
    """
    SIENA_diff: Analysis of longitudinal brain image differences.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input1_basename: Input image 1 basename.
        input2_basename: Input image 2 basename.
        debug_flag: Debug - generate edge images and don't remove temporary\
            images.
        no_seg_flag: Don't segment grey+white separately (because there is poor\
            grey-white contrast).
        self_corr_factor: Apply self-calibrating correction factor.
        ignore_z_flow_flag: Ignore flow in z (may be beneficial if top of brain\
            is missing).
        apply_std_mask_flag: Apply <input1_basename>_stdmask to brain edge\
            points.
        segment_options: Options to be passed to segmentation (type 'fast' to\
            get these).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENA_DIFF_METADATA)
    params = siena_diff_params(input1_basename=input1_basename, input2_basename=input2_basename, debug_flag=debug_flag, no_seg_flag=no_seg_flag, self_corr_factor=self_corr_factor, ignore_z_flow_flag=ignore_z_flow_flag, apply_std_mask_flag=apply_std_mask_flag, segment_options=segment_options)
    return siena_diff_execute(params, execution)


__all__ = [
    "SIENA_DIFF_METADATA",
    "SienaDiffOutputs",
    "SienaDiffParameters",
    "siena_diff",
    "siena_diff_params",
]
