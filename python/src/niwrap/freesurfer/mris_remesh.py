# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_REMESH_METADATA = Metadata(
    id="f5ca57ee0b80f57d1998800d04224821e0092cc6.boutiques",
    name="mris_remesh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisRemeshParameters = typing.TypedDict('MrisRemeshParameters', {
    "__STYX_TYPE__": typing.Literal["mris_remesh"],
    "input": InputPathType,
    "output": str,
    "edge_length": typing.NotRequired[float | None],
    "num_vertices": typing.NotRequired[float | None],
    "face_area": typing.NotRequired[float | None],
    "remesh": bool,
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
        "mris_remesh": mris_remesh_cargs,
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
        "mris_remesh": mris_remesh_outputs,
    }
    return vt.get(t)


class MrisRemeshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_remesh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    remeshed_output: OutputPathType
    """Remeshed output surface file"""


def mris_remesh_params(
    input_: InputPathType,
    output: str,
    edge_length: float | None = None,
    num_vertices: float | None = None,
    face_area: float | None = None,
    remesh: bool = False,
    iterations: float | None = None,
) -> MrisRemeshParameters:
    """
    Build parameters.
    
    Args:
        input_: Input surface file.
        output: Output surface file.
        edge_length: Target average edge length in mm for remeshed surface.
        num_vertices: Target number of vertices for remeshed surface.
        face_area: Desired average face area in mm².
        remesh: Improve the quality while only reducing vertices by a small\
            amount.
        iterations: Number of remeshing iterations (default is 5).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_remesh",
        "input": input_,
        "output": output,
        "remesh": remesh,
    }
    if edge_length is not None:
        params["edge_length"] = edge_length
    if num_vertices is not None:
        params["num_vertices"] = num_vertices
    if face_area is not None:
        params["face_area"] = face_area
    if iterations is not None:
        params["iterations"] = iterations
    return params


def mris_remesh_cargs(
    params: MrisRemeshParameters,
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
    cargs.append("mris_remesh")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input"))
    ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    if params.get("edge_length") is not None:
        cargs.extend([
            "--edge-len",
            str(params.get("edge_length"))
        ])
    if params.get("num_vertices") is not None:
        cargs.extend([
            "--nvert",
            str(params.get("num_vertices"))
        ])
    if params.get("face_area") is not None:
        cargs.extend([
            "--desired-face-area",
            str(params.get("face_area"))
        ])
    if params.get("remesh"):
        cargs.append("--remesh")
    if params.get("iterations") is not None:
        cargs.extend([
            "--iters",
            str(params.get("iterations"))
        ])
    return cargs


def mris_remesh_outputs(
    params: MrisRemeshParameters,
    execution: Execution,
) -> MrisRemeshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRemeshOutputs(
        root=execution.output_file("."),
        remeshed_output=execution.output_file(params.get("output")),
    )
    return ret


def mris_remesh_execute(
    params: MrisRemeshParameters,
    execution: Execution,
) -> MrisRemeshOutputs:
    """
    Remeshes a surface to a desired edge length, number of vertices, or average face
    area.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRemeshOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_remesh_cargs(params, execution)
    ret = mris_remesh_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_remesh(
    input_: InputPathType,
    output: str,
    edge_length: float | None = None,
    num_vertices: float | None = None,
    face_area: float | None = None,
    remesh: bool = False,
    iterations: float | None = None,
    runner: Runner | None = None,
) -> MrisRemeshOutputs:
    """
    Remeshes a surface to a desired edge length, number of vertices, or average face
    area.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_: Input surface file.
        output: Output surface file.
        edge_length: Target average edge length in mm for remeshed surface.
        num_vertices: Target number of vertices for remeshed surface.
        face_area: Desired average face area in mm².
        remesh: Improve the quality while only reducing vertices by a small\
            amount.
        iterations: Number of remeshing iterations (default is 5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRemeshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REMESH_METADATA)
    params = mris_remesh_params(input_=input_, output=output, edge_length=edge_length, num_vertices=num_vertices, face_area=face_area, remesh=remesh, iterations=iterations)
    return mris_remesh_execute(params, execution)


__all__ = [
    "MRIS_REMESH_METADATA",
    "MrisRemeshOutputs",
    "MrisRemeshParameters",
    "mris_remesh",
    "mris_remesh_params",
]
