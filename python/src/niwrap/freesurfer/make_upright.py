# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_UPRIGHT_METADATA = Metadata(
    id="f69f1f73df7f80db3bbc666008c56b37f2fb8894.boutiques",
    name="make_upright",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MakeUprightParameters = typing.TypedDict('MakeUprightParameters', {
    "__STYX_TYPE__": typing.Literal["make_upright"],
    "input_image": InputPathType,
    "output_image": str,
    "transformation_map": InputPathType,
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
        "make_upright": make_upright_cargs,
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
        "make_upright": make_upright_outputs,
    }.get(t)


class MakeUprightOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_upright(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_image: OutputPathType
    """Registered upright MRI image"""


def make_upright_params(
    input_image: InputPathType,
    output_image: str,
    transformation_map: InputPathType,
) -> MakeUprightParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input MRI image file in .mgz format.
        output_image: Output MRI image file in .mgz format.
        transformation_map: Transformation map file in .lta format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make_upright",
        "input_image": input_image,
        "output_image": output_image,
        "transformation_map": transformation_map,
    }
    return params


def make_upright_cargs(
    params: MakeUprightParameters,
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
    cargs.append("make_upright")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    cargs.append(execution.input_file(params.get("transformation_map")))
    return cargs


def make_upright_outputs(
    params: MakeUprightParameters,
    execution: Execution,
) -> MakeUprightOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeUprightOutputs(
        root=execution.output_file("."),
        registered_image=execution.output_file(params.get("output_image")),
    )
    return ret


def make_upright_execute(
    params: MakeUprightParameters,
    execution: Execution,
) -> MakeUprightOutputs:
    """
    Registers MRI input to the left/right reversed version using mri_robust_register
    and making use of the half-way space, resulting in an upright, forward facing
    head position.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeUprightOutputs`).
    """
    cargs = make_upright_cargs(params, execution)
    ret = make_upright_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_upright(
    input_image: InputPathType,
    output_image: str,
    transformation_map: InputPathType,
    runner: Runner | None = None,
) -> MakeUprightOutputs:
    """
    Registers MRI input to the left/right reversed version using mri_robust_register
    and making use of the half-way space, resulting in an upright, forward facing
    head position.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input MRI image file in .mgz format.
        output_image: Output MRI image file in .mgz format.
        transformation_map: Transformation map file in .lta format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeUprightOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_UPRIGHT_METADATA)
    params = make_upright_params(input_image=input_image, output_image=output_image, transformation_map=transformation_map)
    return make_upright_execute(params, execution)


__all__ = [
    "MAKE_UPRIGHT_METADATA",
    "MakeUprightOutputs",
    "MakeUprightParameters",
    "make_upright",
    "make_upright_params",
]
