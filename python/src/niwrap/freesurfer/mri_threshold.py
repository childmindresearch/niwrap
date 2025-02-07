# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_THRESHOLD_METADATA = Metadata(
    id="18dd783d6c61c6360f3439c48e74d88d1a862887.boutiques",
    name="mri_threshold",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriThresholdParameters = typing.TypedDict('MriThresholdParameters', {
    "__STYX_TYPE__": typing.Literal["mri_threshold"],
    "input_vol": InputPathType,
    "threshold": float,
    "output_vol": str,
    "binarize": typing.NotRequired[float | None],
    "upper_threshold": bool,
    "frame_number": typing.NotRequired[float | None],
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
        "mri_threshold": mri_threshold_cargs,
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
        "mri_threshold": mri_threshold_outputs,
    }.get(t)


class MriThresholdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_threshold(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vol_file: OutputPathType
    """Thresholded output volume"""


def mri_threshold_params(
    input_vol: InputPathType,
    threshold: float,
    output_vol: str,
    binarize: float | None = None,
    upper_threshold: bool = False,
    frame_number: float | None = None,
) -> MriThresholdParameters:
    """
    Build parameters.
    
    Args:
        input_vol: Input volume file.
        threshold: Threshold value for the volume.
        output_vol: Output volume file.
        binarize: Binarize the output volume with specified bval.
        upper_threshold: Upper threshold the volume instead of lower\
            thresholding.
        frame_number: Apply thresholding to a specific frame indexed by fnum.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_threshold",
        "input_vol": input_vol,
        "threshold": threshold,
        "output_vol": output_vol,
        "upper_threshold": upper_threshold,
    }
    if binarize is not None:
        params["binarize"] = binarize
    if frame_number is not None:
        params["frame_number"] = frame_number
    return params


def mri_threshold_cargs(
    params: MriThresholdParameters,
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
    cargs.append("mri_threshold")
    cargs.append(execution.input_file(params.get("input_vol")))
    cargs.append(str(params.get("threshold")))
    cargs.append(params.get("output_vol"))
    if params.get("binarize") is not None:
        cargs.extend([
            "-B",
            str(params.get("binarize"))
        ])
    if params.get("upper_threshold"):
        cargs.append("-U")
    if params.get("frame_number") is not None:
        cargs.extend([
            "-F",
            str(params.get("frame_number"))
        ])
    return cargs


def mri_threshold_outputs(
    params: MriThresholdParameters,
    execution: Execution,
) -> MriThresholdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriThresholdOutputs(
        root=execution.output_file("."),
        output_vol_file=execution.output_file(params.get("output_vol")),
    )
    return ret


def mri_threshold_execute(
    params: MriThresholdParameters,
    execution: Execution,
) -> MriThresholdOutputs:
    """
    This program will lower threshold an input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriThresholdOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_threshold_cargs(params, execution)
    ret = mri_threshold_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_threshold(
    input_vol: InputPathType,
    threshold: float,
    output_vol: str,
    binarize: float | None = None,
    upper_threshold: bool = False,
    frame_number: float | None = None,
    runner: Runner | None = None,
) -> MriThresholdOutputs:
    """
    This program will lower threshold an input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input volume file.
        threshold: Threshold value for the volume.
        output_vol: Output volume file.
        binarize: Binarize the output volume with specified bval.
        upper_threshold: Upper threshold the volume instead of lower\
            thresholding.
        frame_number: Apply thresholding to a specific frame indexed by fnum.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriThresholdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_THRESHOLD_METADATA)
    params = mri_threshold_params(input_vol=input_vol, threshold=threshold, output_vol=output_vol, binarize=binarize, upper_threshold=upper_threshold, frame_number=frame_number)
    return mri_threshold_execute(params, execution)


__all__ = [
    "MRI_THRESHOLD_METADATA",
    "MriThresholdOutputs",
    "MriThresholdParameters",
    "mri_threshold",
    "mri_threshold_params",
]
