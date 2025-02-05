# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMSTACK_METADATA = Metadata(
    id="4d6200fa2e1b9b6bfc0d03b2731f1be8201a7a22.boutiques",
    name="imstack",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ImstackParameters = typing.TypedDict('ImstackParameters', {
    "__STYX_TYPE__": typing.Literal["imstack"],
    "image_files": list[InputPathType],
    "data_type": typing.NotRequired[typing.Literal["short", "float"] | None],
    "output_prefix": typing.NotRequired[str | None],
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
        "imstack": imstack_cargs,
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
        "imstack": imstack_outputs,
    }
    return vt.get(t)


class ImstackOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imstack(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_data_file: OutputPathType | None
    """Output data file"""
    output_header_file: OutputPathType | None
    """Output header file"""


def imstack_params(
    image_files: list[InputPathType],
    data_type: typing.Literal["short", "float"] | None = None,
    output_prefix: str | None = None,
) -> ImstackParameters:
    """
    Build parameters.
    
    Args:
        image_files: Input image filenames.
        data_type: Converts the output data file to be 'type', which is either\
            'short' or 'float'. The default type is the type of the first image.
        output_prefix: Names the output files to be 'name'.b'type' and\
            'name'.hdr. The default name is 'obi-wan-kenobi'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imstack",
        "image_files": image_files,
    }
    if data_type is not None:
        params["data_type"] = data_type
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    return params


def imstack_cargs(
    params: ImstackParameters,
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
    cargs.append("imstack")
    cargs.extend([execution.input_file(f) for f in params.get("image_files")])
    if params.get("data_type") is not None:
        cargs.extend([
            "-datum",
            params.get("data_type")
        ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    return cargs


def imstack_outputs(
    params: ImstackParameters,
    execution: Execution,
) -> ImstackOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImstackOutputs(
        root=execution.output_file("."),
        output_data_file=execution.output_file(params.get("output_prefix") + ".b" + params.get("data_type")) if (params.get("output_prefix") is not None and params.get("data_type") is not None) else None,
        output_header_file=execution.output_file(params.get("output_prefix") + ".hdr") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def imstack_execute(
    params: ImstackParameters,
    execution: Execution,
) -> ImstackOutputs:
    """
    Stacks up a set of 2D images into one big file (a la MGH).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImstackOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = imstack_cargs(params, execution)
    ret = imstack_outputs(params, execution)
    execution.run(cargs)
    return ret


def imstack(
    image_files: list[InputPathType],
    data_type: typing.Literal["short", "float"] | None = None,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> ImstackOutputs:
    """
    Stacks up a set of 2D images into one big file (a la MGH).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        image_files: Input image filenames.
        data_type: Converts the output data file to be 'type', which is either\
            'short' or 'float'. The default type is the type of the first image.
        output_prefix: Names the output files to be 'name'.b'type' and\
            'name'.hdr. The default name is 'obi-wan-kenobi'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImstackOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMSTACK_METADATA)
    params = imstack_params(image_files=image_files, data_type=data_type, output_prefix=output_prefix)
    return imstack_execute(params, execution)


__all__ = [
    "IMSTACK_METADATA",
    "ImstackOutputs",
    "ImstackParameters",
    "imstack",
    "imstack_params",
]
