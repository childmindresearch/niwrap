# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_MOTION_CORRECT_FSL_METADATA = Metadata(
    id="e4429f150e08917f7317e164c448c83b94352eed.boutiques",
    name="mri_motion_correct.fsl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriMotionCorrectFslParameters = typing.TypedDict('MriMotionCorrectFslParameters', {
    "__STYX_TYPE__": typing.Literal["mri_motion_correct.fsl"],
    "input_image": InputPathType,
    "output_image": str,
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
        "mri_motion_correct.fsl": mri_motion_correct_fsl_cargs,
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
        "mri_motion_correct.fsl": mri_motion_correct_fsl_outputs,
    }.get(t)


class MriMotionCorrectFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_motion_correct_fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_output: OutputPathType
    """Motion corrected output MRI image"""


def mri_motion_correct_fsl_params(
    input_image: InputPathType,
    output_image: str,
) -> MriMotionCorrectFslParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input MRI image to be motion corrected.
        output_image: Output corrected MRI image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_motion_correct.fsl",
        "input_image": input_image,
        "output_image": output_image,
    }
    return params


def mri_motion_correct_fsl_cargs(
    params: MriMotionCorrectFslParameters,
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
    cargs.append("mri_motion_correct.fsl")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    cargs.append("[OPTIONS]")
    return cargs


def mri_motion_correct_fsl_outputs(
    params: MriMotionCorrectFslParameters,
    execution: Execution,
) -> MriMotionCorrectFslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMotionCorrectFslOutputs(
        root=execution.output_file("."),
        corrected_output=execution.output_file(params.get("output_image") + ".nii.gz"),
    )
    return ret


def mri_motion_correct_fsl_execute(
    params: MriMotionCorrectFslParameters,
    execution: Execution,
) -> MriMotionCorrectFslOutputs:
    """
    Tool for motion correction of MRI images using FSL.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMotionCorrectFslOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_motion_correct_fsl_cargs(params, execution)
    ret = mri_motion_correct_fsl_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_motion_correct_fsl(
    input_image: InputPathType,
    output_image: str,
    runner: Runner | None = None,
) -> MriMotionCorrectFslOutputs:
    """
    Tool for motion correction of MRI images using FSL.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input MRI image to be motion corrected.
        output_image: Output corrected MRI image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMotionCorrectFslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MOTION_CORRECT_FSL_METADATA)
    params = mri_motion_correct_fsl_params(input_image=input_image, output_image=output_image)
    return mri_motion_correct_fsl_execute(params, execution)


__all__ = [
    "MRI_MOTION_CORRECT_FSL_METADATA",
    "MriMotionCorrectFslOutputs",
    "MriMotionCorrectFslParameters",
    "mri_motion_correct_fsl",
    "mri_motion_correct_fsl_params",
]
