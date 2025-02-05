# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLSWAPDIM_FSL_METADATA = Metadata(
    id="7302b08bc4d86f9914f7a8203cbaf36cc9515b0c.boutiques",
    name="fslswapdim.fsl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FslswapdimFslParameters = typing.TypedDict('FslswapdimFslParameters', {
    "__STYX_TYPE__": typing.Literal["fslswapdim.fsl"],
    "input_file": InputPathType,
    "axis_a": str,
    "axis_b": str,
    "axis_c": str,
    "output_file": typing.NotRequired[str | None],
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
        "fslswapdim.fsl": fslswapdim_fsl_cargs,
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
    vt = {
        "fslswapdim.fsl": fslswapdim_fsl_outputs,
    }
    return vt.get(t)


class FslswapdimFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslswapdim_fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType | None
    """Output image with swapped dimensions"""


def fslswapdim_fsl_params(
    input_file: InputPathType,
    axis_a: str,
    axis_b: str,
    axis_c: str,
    output_file: str | None = None,
) -> FslswapdimFslParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input image file.
        axis_a: New X-axis in terms of the old axes; can be one of -x, x, y,\
            -y, z, -z or RL, LR, AP, PA, SI, IS.
        axis_b: New Y-axis in terms of the old axes; can be one of -x, x, y,\
            -y, z, -z or RL, LR, AP, PA, SI, IS.
        axis_c: New Z-axis in terms of the old axes; can be one of -x, x, y,\
            -y, z, -z or RL, LR, AP, PA, SI, IS.
        output_file: Output image file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslswapdim.fsl",
        "input_file": input_file,
        "axis_a": axis_a,
        "axis_b": axis_b,
        "axis_c": axis_c,
    }
    if output_file is not None:
        params["output_file"] = output_file
    return params


def fslswapdim_fsl_cargs(
    params: FslswapdimFslParameters,
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
    cargs.append("fslswapdim")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("axis_a"))
    cargs.append(params.get("axis_b"))
    cargs.append(params.get("axis_c"))
    if params.get("output_file") is not None:
        cargs.append(params.get("output_file"))
    return cargs


def fslswapdim_fsl_outputs(
    params: FslswapdimFslParameters,
    execution: Execution,
) -> FslswapdimFslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslswapdimFslOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def fslswapdim_fsl_execute(
    params: FslswapdimFslParameters,
    execution: Execution,
) -> FslswapdimFslOutputs:
    """
    FSLSwapdim allows swapping and flipping of dimensions of an image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslswapdimFslOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslswapdim_fsl_cargs(params, execution)
    ret = fslswapdim_fsl_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslswapdim_fsl(
    input_file: InputPathType,
    axis_a: str,
    axis_b: str,
    axis_c: str,
    output_file: str | None = None,
    runner: Runner | None = None,
) -> FslswapdimFslOutputs:
    """
    FSLSwapdim allows swapping and flipping of dimensions of an image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input image file.
        axis_a: New X-axis in terms of the old axes; can be one of -x, x, y,\
            -y, z, -z or RL, LR, AP, PA, SI, IS.
        axis_b: New Y-axis in terms of the old axes; can be one of -x, x, y,\
            -y, z, -z or RL, LR, AP, PA, SI, IS.
        axis_c: New Z-axis in terms of the old axes; can be one of -x, x, y,\
            -y, z, -z or RL, LR, AP, PA, SI, IS.
        output_file: Output image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslswapdimFslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSWAPDIM_FSL_METADATA)
    params = fslswapdim_fsl_params(input_file=input_file, axis_a=axis_a, axis_b=axis_b, axis_c=axis_c, output_file=output_file)
    return fslswapdim_fsl_execute(params, execution)


__all__ = [
    "FSLSWAPDIM_FSL_METADATA",
    "FslswapdimFslOutputs",
    "FslswapdimFslParameters",
    "fslswapdim_fsl",
    "fslswapdim_fsl_params",
]
