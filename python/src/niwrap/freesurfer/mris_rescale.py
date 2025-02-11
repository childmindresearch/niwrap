# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_RESCALE_METADATA = Metadata(
    id="dc82fd3ed28ce8af91d50743abd00b226c549b2e.boutiques",
    name="mris_rescale",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisRescaleParameters = typing.TypedDict('MrisRescaleParameters', {
    "__STYX_TYPE__": typing.Literal["mris_rescale"],
    "input_surface": InputPathType,
    "output_surface": str,
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
        "mris_rescale": mris_rescale_cargs,
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
        "mris_rescale": mris_rescale_outputs,
    }.get(t)


class MrisRescaleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_rescale(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    rescaled_output_surface: OutputPathType
    """The file containing the rescaled surface."""


def mris_rescale_params(
    input_surface: InputPathType,
    output_surface: str,
) -> MrisRescaleParameters:
    """
    Build parameters.
    
    Args:
        input_surface: The input surface file to be rescaled.
        output_surface: The output surface file after rescaling.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_rescale",
        "input_surface": input_surface,
        "output_surface": output_surface,
    }
    return params


def mris_rescale_cargs(
    params: MrisRescaleParameters,
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
    cargs.append("mris_rescale")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(params.get("output_surface"))
    return cargs


def mris_rescale_outputs(
    params: MrisRescaleParameters,
    execution: Execution,
) -> MrisRescaleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRescaleOutputs(
        root=execution.output_file("."),
        rescaled_output_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_rescale_execute(
    params: MrisRescaleParameters,
    execution: Execution,
) -> MrisRescaleOutputs:
    """
    This program will rescale a surface representation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRescaleOutputs`).
    """
    cargs = mris_rescale_cargs(params, execution)
    ret = mris_rescale_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_rescale(
    input_surface: InputPathType,
    output_surface: str,
    runner: Runner | None = None,
) -> MrisRescaleOutputs:
    """
    This program will rescale a surface representation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: The input surface file to be rescaled.
        output_surface: The output surface file after rescaling.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRescaleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_RESCALE_METADATA)
    params = mris_rescale_params(input_surface=input_surface, output_surface=output_surface)
    return mris_rescale_execute(params, execution)


__all__ = [
    "MRIS_RESCALE_METADATA",
    "MrisRescaleOutputs",
    "MrisRescaleParameters",
    "mris_rescale",
    "mris_rescale_params",
]
