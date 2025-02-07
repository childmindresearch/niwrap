# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

APPLY_MORPH_METADATA = Metadata(
    id="a7cb7e420a1c51fbb13f7cd6c2a1a9581804bf02.boutiques",
    name="applyMorph",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ApplyMorphParameters = typing.TypedDict('ApplyMorphParameters', {
    "__STYX_TYPE__": typing.Literal["applyMorph"],
    "inputs": list[InputPathType],
    "template": InputPathType,
    "transform": InputPathType,
    "zlib_buffer": typing.NotRequired[float | None],
    "dbg_coords": typing.NotRequired[list[float] | None],
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
        "applyMorph": apply_morph_cargs,
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
        "applyMorph": apply_morph_outputs,
    }.get(t)


class ApplyMorphOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apply_morph(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def apply_morph_params(
    inputs: list[InputPathType],
    template: InputPathType,
    transform: InputPathType,
    zlib_buffer: float | None = None,
    dbg_coords: list[float] | None = None,
) -> ApplyMorphParameters:
    """
    Build parameters.
    
    Args:
        inputs: Input files.
        template: Template volume.
        transform: Transform file.
        zlib_buffer: Zlib buffer pre-allocation multiplier.
        dbg_coords: Debugging coordinates.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "applyMorph",
        "inputs": inputs,
        "template": template,
        "transform": transform,
    }
    if zlib_buffer is not None:
        params["zlib_buffer"] = zlib_buffer
    if dbg_coords is not None:
        params["dbg_coords"] = dbg_coords
    return params


def apply_morph_cargs(
    params: ApplyMorphParameters,
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
    cargs.append("applyMorph")
    cargs.extend([execution.input_file(f) for f in params.get("inputs")])
    cargs.extend([
        "--template",
        execution.input_file(params.get("template"))
    ])
    cargs.extend([
        "--transform",
        execution.input_file(params.get("transform"))
    ])
    if params.get("zlib_buffer") is not None:
        cargs.extend([
            "--zlib_buffer",
            str(params.get("zlib_buffer"))
        ])
    if params.get("dbg_coords") is not None:
        cargs.extend([
            "--dbg_coords",
            *map(str, params.get("dbg_coords"))
        ])
    return cargs


def apply_morph_outputs(
    params: ApplyMorphParameters,
    execution: Execution,
) -> ApplyMorphOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ApplyMorphOutputs(
        root=execution.output_file("."),
    )
    return ret


def apply_morph_execute(
    params: ApplyMorphParameters,
    execution: Execution,
) -> ApplyMorphOutputs:
    """
    A tool for applying a morph to a volume using a template and a transform.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ApplyMorphOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = apply_morph_cargs(params, execution)
    ret = apply_morph_outputs(params, execution)
    execution.run(cargs)
    return ret


def apply_morph(
    inputs: list[InputPathType],
    template: InputPathType,
    transform: InputPathType,
    zlib_buffer: float | None = None,
    dbg_coords: list[float] | None = None,
    runner: Runner | None = None,
) -> ApplyMorphOutputs:
    """
    A tool for applying a morph to a volume using a template and a transform.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inputs: Input files.
        template: Template volume.
        transform: Transform file.
        zlib_buffer: Zlib buffer pre-allocation multiplier.
        dbg_coords: Debugging coordinates.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApplyMorphOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APPLY_MORPH_METADATA)
    params = apply_morph_params(inputs=inputs, template=template, transform=transform, zlib_buffer=zlib_buffer, dbg_coords=dbg_coords)
    return apply_morph_execute(params, execution)


__all__ = [
    "APPLY_MORPH_METADATA",
    "ApplyMorphOutputs",
    "ApplyMorphParameters",
    "apply_morph",
    "apply_morph_params",
]
