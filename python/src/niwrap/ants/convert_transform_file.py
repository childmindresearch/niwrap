# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_TRANSFORM_FILE_METADATA = Metadata(
    id="224c137774aff43d94d1fecb5c8b4a19ae81816c.boutiques",
    name="ConvertTransformFile",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
ConvertTransformFileParameters = typing.TypedDict('ConvertTransformFileParameters', {
    "__STYX_TYPE__": typing.Literal["ConvertTransformFile"],
    "dimensions": int,
    "input_transform_file": InputPathType,
    "output_transform_file": str,
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
        "ConvertTransformFile": convert_transform_file_cargs,
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
    vt = {}
    return vt.get(t)


class ConvertTransformFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_transform_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def convert_transform_file_params(
    dimensions: int,
    input_transform_file: InputPathType,
    output_transform_file: str,
) -> ConvertTransformFileParameters:
    """
    Build parameters.
    
    Args:
        dimensions: Dimensionality of the transform file.
        input_transform_file: Path to the input transform file.
        output_transform_file: Path for the output transform file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ConvertTransformFile",
        "dimensions": dimensions,
        "input_transform_file": input_transform_file,
        "output_transform_file": output_transform_file,
    }
    return params


def convert_transform_file_cargs(
    params: ConvertTransformFileParameters,
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
    cargs.append("ConvertTransformFile")
    cargs.append(str(params.get("dimensions")))
    cargs.append(execution.input_file(params.get("input_transform_file")))
    cargs.append(params.get("output_transform_file"))
    cargs.append("[OPTIONS]")
    return cargs


def convert_transform_file_outputs(
    params: ConvertTransformFileParameters,
    execution: Execution,
) -> ConvertTransformFileOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertTransformFileOutputs(
        root=execution.output_file("."),
    )
    return ret


def convert_transform_file_execute(
    params: ConvertTransformFileParameters,
    execution: Execution,
) -> ConvertTransformFileOutputs:
    """
    Utility to read in a transform file (presumed to be in binary format) and output
    it in various formats. Default output is legacy human-readable text format.
    Without any options, the output filename extension must be .txt or .tfm to
    signify a text-formatted transform file.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertTransformFileOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = convert_transform_file_cargs(params, execution)
    ret = convert_transform_file_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_transform_file(
    dimensions: int,
    input_transform_file: InputPathType,
    output_transform_file: str,
    runner: Runner | None = None,
) -> ConvertTransformFileOutputs:
    """
    Utility to read in a transform file (presumed to be in binary format) and output
    it in various formats. Default output is legacy human-readable text format.
    Without any options, the output filename extension must be .txt or .tfm to
    signify a text-formatted transform file.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimensions: Dimensionality of the transform file.
        input_transform_file: Path to the input transform file.
        output_transform_file: Path for the output transform file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertTransformFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_TRANSFORM_FILE_METADATA)
    params = convert_transform_file_params(dimensions=dimensions, input_transform_file=input_transform_file, output_transform_file=output_transform_file)
    return convert_transform_file_execute(params, execution)


__all__ = [
    "CONVERT_TRANSFORM_FILE_METADATA",
    "ConvertTransformFileOutputs",
    "ConvertTransformFileParameters",
    "convert_transform_file",
    "convert_transform_file_params",
]
