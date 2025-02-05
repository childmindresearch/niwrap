# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_MESH_SUBDIVIDE_METADATA = Metadata(
    id="fb137b14730056953d8eae8a55716f7ac7551282.boutiques",
    name="mris_mesh_subdivide",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisMeshSubdivideParameters = typing.TypedDict('MrisMeshSubdivideParameters', {
    "__STYX_TYPE__": typing.Literal["mris_mesh_subdivide"],
    "input_surface": InputPathType,
    "output_surface": str,
    "subdivision_method": typing.NotRequired[typing.Literal["butterfly", "loop", "linear"] | None],
    "iterations": typing.NotRequired[float | None],
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
        "mris_mesh_subdivide": mris_mesh_subdivide_cargs,
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
        "mris_mesh_subdivide": mris_mesh_subdivide_outputs,
    }
    return vt.get(t)


class MrisMeshSubdivideOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_mesh_subdivide(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    subdivided_surface: OutputPathType
    """The subdivided mesh surface output file"""


def mris_mesh_subdivide_params(
    input_surface: InputPathType,
    output_surface: str,
    subdivision_method: typing.Literal["butterfly", "loop", "linear"] | None = None,
    iterations: float | None = None,
) -> MrisMeshSubdivideParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Name of input surface file.
        output_surface: Name for output surface file (outputs to same directory\
            as input if path not provided).
        subdivision_method: Subdivision method: options are 'butterfly'\
            (default), 'loop', or 'linear'.
        iterations: Number of subdivision iterations.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_mesh_subdivide",
        "input_surface": input_surface,
        "output_surface": output_surface,
    }
    if subdivision_method is not None:
        params["subdivision_method"] = subdivision_method
    if iterations is not None:
        params["iterations"] = iterations
    return params


def mris_mesh_subdivide_cargs(
    params: MrisMeshSubdivideParameters,
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
    cargs.append("mris_mesh_subdivide")
    cargs.extend([
        "--surf",
        execution.input_file(params.get("input_surface"))
    ])
    cargs.extend([
        "--out",
        params.get("output_surface")
    ])
    if params.get("subdivision_method") is not None:
        cargs.extend([
            "--method",
            params.get("subdivision_method")
        ])
    if params.get("iterations") is not None:
        cargs.extend([
            "--iter",
            str(params.get("iterations"))
        ])
    return cargs


def mris_mesh_subdivide_outputs(
    params: MrisMeshSubdivideParameters,
    execution: Execution,
) -> MrisMeshSubdivideOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMeshSubdivideOutputs(
        root=execution.output_file("."),
        subdivided_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_mesh_subdivide_execute(
    params: MrisMeshSubdivideParameters,
    execution: Execution,
) -> MrisMeshSubdivideOutputs:
    """
    This program will subdivide a triangular mesh surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMeshSubdivideOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_mesh_subdivide_cargs(params, execution)
    ret = mris_mesh_subdivide_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_mesh_subdivide(
    input_surface: InputPathType,
    output_surface: str,
    subdivision_method: typing.Literal["butterfly", "loop", "linear"] | None = None,
    iterations: float | None = None,
    runner: Runner | None = None,
) -> MrisMeshSubdivideOutputs:
    """
    This program will subdivide a triangular mesh surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Name of input surface file.
        output_surface: Name for output surface file (outputs to same directory\
            as input if path not provided).
        subdivision_method: Subdivision method: options are 'butterfly'\
            (default), 'loop', or 'linear'.
        iterations: Number of subdivision iterations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMeshSubdivideOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MESH_SUBDIVIDE_METADATA)
    params = mris_mesh_subdivide_params(input_surface=input_surface, output_surface=output_surface, subdivision_method=subdivision_method, iterations=iterations)
    return mris_mesh_subdivide_execute(params, execution)


__all__ = [
    "MRIS_MESH_SUBDIVIDE_METADATA",
    "MrisMeshSubdivideOutputs",
    "MrisMeshSubdivideParameters",
    "mris_mesh_subdivide",
    "mris_mesh_subdivide_params",
]
