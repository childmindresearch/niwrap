# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VIENA_QUANT_METADATA = Metadata(
    id="51ebcfad9ed201b8538ee2a9ad0b420654d85cea.boutiques",
    name="viena_quant",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
VienaQuantParameters = typing.TypedDict('VienaQuantParameters', {
    "__STYX_TYPE__": typing.Literal["viena_quant"],
    "input1": InputPathType,
    "input2": InputPathType,
    "ventricle_mask": InputPathType,
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
        "viena_quant": viena_quant_cargs,
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
        "viena_quant": viena_quant_outputs,
    }.get(t)


class VienaQuantOutputs(typing.NamedTuple):
    """
    Output object returned when calling `viena_quant(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_quantification: OutputPathType
    """Output quantification result"""


def viena_quant_params(
    input1: InputPathType,
    input2: InputPathType,
    ventricle_mask: InputPathType,
) -> VienaQuantParameters:
    """
    Build parameters.
    
    Args:
        input1: Input image 1 (e.g. img1.nii.gz).
        input2: Input image 2 (e.g. img2.nii.gz).
        ventricle_mask: Ventricle mask (e.g. mask.nii.gz).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "viena_quant",
        "input1": input1,
        "input2": input2,
        "ventricle_mask": ventricle_mask,
    }
    return params


def viena_quant_cargs(
    params: VienaQuantParameters,
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
    cargs.append("viena_quant")
    cargs.append(execution.input_file(params.get("input1")))
    cargs.append(execution.input_file(params.get("input2")))
    cargs.append(execution.input_file(params.get("ventricle_mask")))
    return cargs


def viena_quant_outputs(
    params: VienaQuantParameters,
    execution: Execution,
) -> VienaQuantOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VienaQuantOutputs(
        root=execution.output_file("."),
        output_quantification=execution.output_file("output_quantification.nii.gz"),
    )
    return ret


def viena_quant_execute(
    params: VienaQuantParameters,
    execution: Execution,
) -> VienaQuantOutputs:
    """
    Automated brain ventricle quantification tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VienaQuantOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = viena_quant_cargs(params, execution)
    ret = viena_quant_outputs(params, execution)
    execution.run(cargs)
    return ret


def viena_quant(
    input1: InputPathType,
    input2: InputPathType,
    ventricle_mask: InputPathType,
    runner: Runner | None = None,
) -> VienaQuantOutputs:
    """
    Automated brain ventricle quantification tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input1: Input image 1 (e.g. img1.nii.gz).
        input2: Input image 2 (e.g. img2.nii.gz).
        ventricle_mask: Ventricle mask (e.g. mask.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VienaQuantOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VIENA_QUANT_METADATA)
    params = viena_quant_params(input1=input1, input2=input2, ventricle_mask=ventricle_mask)
    return viena_quant_execute(params, execution)


__all__ = [
    "VIENA_QUANT_METADATA",
    "VienaQuantOutputs",
    "VienaQuantParameters",
    "viena_quant",
    "viena_quant_params",
]
