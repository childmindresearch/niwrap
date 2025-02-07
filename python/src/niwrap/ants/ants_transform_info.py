# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_TRANSFORM_INFO_METADATA = Metadata(
    id="db110d69e8361c7a0293d1d70937a09c146e535a.boutiques",
    name="antsTransformInfo",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsTransformInfoParameters = typing.TypedDict('AntsTransformInfoParameters', {
    "__STYX_TYPE__": typing.Literal["antsTransformInfo"],
    "transform_file": InputPathType,
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
        "antsTransformInfo": ants_transform_info_cargs,
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
        "antsTransformInfo": ants_transform_info_outputs,
    }.get(t)


class AntsTransformInfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_transform_info(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_info: OutputPathType
    """Information of the provided transform file."""


def ants_transform_info_params(
    transform_file: InputPathType,
) -> AntsTransformInfoParameters:
    """
    Build parameters.
    
    Args:
        transform_file: The transform file to read. Supported formats include\
            HDF5, MINC, Matlab, and Txt.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsTransformInfo",
        "transform_file": transform_file,
    }
    return params


def ants_transform_info_cargs(
    params: AntsTransformInfoParameters,
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
    cargs.append("antsTransformInfo")
    cargs.extend([
        "--file",
        execution.input_file(params.get("transform_file"))
    ])
    return cargs


def ants_transform_info_outputs(
    params: AntsTransformInfoParameters,
    execution: Execution,
) -> AntsTransformInfoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsTransformInfoOutputs(
        root=execution.output_file("."),
        output_info=execution.output_file("transform_info.txt"),
    )
    return ret


def ants_transform_info_execute(
    params: AntsTransformInfoParameters,
    execution: Execution,
) -> AntsTransformInfoOutputs:
    """
    Provide information about an ITK transform file.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsTransformInfoOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ants_transform_info_cargs(params, execution)
    ret = ants_transform_info_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_transform_info(
    transform_file: InputPathType,
    runner: Runner | None = None,
) -> AntsTransformInfoOutputs:
    """
    Provide information about an ITK transform file.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        transform_file: The transform file to read. Supported formats include\
            HDF5, MINC, Matlab, and Txt.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsTransformInfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_TRANSFORM_INFO_METADATA)
    params = ants_transform_info_params(transform_file=transform_file)
    return ants_transform_info_execute(params, execution)


__all__ = [
    "ANTS_TRANSFORM_INFO_METADATA",
    "AntsTransformInfoOutputs",
    "AntsTransformInfoParameters",
    "ants_transform_info",
    "ants_transform_info_params",
]
