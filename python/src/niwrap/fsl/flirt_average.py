# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FLIRT_AVERAGE_METADATA = Metadata(
    id="0cc7b938efcdc9cb9d1e15e1453b173b6ccc4af1.boutiques",
    name="flirt_average",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FlirtAverageParameters = typing.TypedDict('FlirtAverageParameters', {
    "__STYX_TYPE__": typing.Literal["flirt_average"],
    "ninputs": int,
    "input1": InputPathType,
    "input2": InputPathType,
    "output_file": str,
    "reference_image": typing.NotRequired[InputPathType | None],
    "flirt_options": typing.NotRequired[str | None],
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
        "flirt_average": flirt_average_cargs,
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
        "flirt_average": flirt_average_outputs,
    }.get(t)


class FlirtAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flirt_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Averaged output image"""


def flirt_average_params(
    ninputs: int,
    input1: InputPathType,
    input2: InputPathType,
    output_file: str,
    reference_image: InputPathType | None = None,
    flirt_options: str | None = None,
) -> FlirtAverageParameters:
    """
    Build parameters.
    
    Args:
        ninputs: Number of input images.
        input1: First input image (e.g. rawT1_1.nii.gz).
        input2: Second input image (e.g. rawT1_2.nii.gz).
        output_file: Output image (e.g. averageT1.nii.gz).
        reference_image: Reference image to use instead of first input.
        flirt_options: Options to be passed to FLIRT.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "flirt_average",
        "ninputs": ninputs,
        "input1": input1,
        "input2": input2,
        "output_file": output_file,
    }
    if reference_image is not None:
        params["reference_image"] = reference_image
    if flirt_options is not None:
        params["flirt_options"] = flirt_options
    return params


def flirt_average_cargs(
    params: FlirtAverageParameters,
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
    cargs.append("flirt_average")
    cargs.append(str(params.get("ninputs")))
    cargs.append(execution.input_file(params.get("input1")))
    cargs.append(execution.input_file(params.get("input2")))
    cargs.append("...")
    cargs.append(params.get("output_file"))
    if params.get("reference_image") is not None:
        cargs.extend([
            "-FAref",
            execution.input_file(params.get("reference_image"))
        ])
    if params.get("flirt_options") is not None:
        cargs.append(params.get("flirt_options"))
    return cargs


def flirt_average_outputs(
    params: FlirtAverageParameters,
    execution: Execution,
) -> FlirtAverageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FlirtAverageOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("output_file") + ".nii.gz"),
    )
    return ret


def flirt_average_execute(
    params: FlirtAverageParameters,
    execution: Execution,
) -> FlirtAverageOutputs:
    """
    Averages multiple input images after linear registration (FLIRT).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FlirtAverageOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = flirt_average_cargs(params, execution)
    ret = flirt_average_outputs(params, execution)
    execution.run(cargs)
    return ret


def flirt_average(
    ninputs: int,
    input1: InputPathType,
    input2: InputPathType,
    output_file: str,
    reference_image: InputPathType | None = None,
    flirt_options: str | None = None,
    runner: Runner | None = None,
) -> FlirtAverageOutputs:
    """
    Averages multiple input images after linear registration (FLIRT).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        ninputs: Number of input images.
        input1: First input image (e.g. rawT1_1.nii.gz).
        input2: Second input image (e.g. rawT1_2.nii.gz).
        output_file: Output image (e.g. averageT1.nii.gz).
        reference_image: Reference image to use instead of first input.
        flirt_options: Options to be passed to FLIRT.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FlirtAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FLIRT_AVERAGE_METADATA)
    params = flirt_average_params(ninputs=ninputs, input1=input1, input2=input2, output_file=output_file, reference_image=reference_image, flirt_options=flirt_options)
    return flirt_average_execute(params, execution)


__all__ = [
    "FLIRT_AVERAGE_METADATA",
    "FlirtAverageOutputs",
    "FlirtAverageParameters",
    "flirt_average",
    "flirt_average_params",
]
