# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RBOX_METADATA = Metadata(
    id="4f43f8ba19b6a24114997ab42bf7e5c5e5484c74.boutiques",
    name="rbox",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


RboxParameters = typing.TypedDict('RboxParameters', {
    "__STYX_TYPE__": typing.Literal["rbox"],
    "number_points": str,
    "dimension": typing.NotRequired[str | None],
    "integer_coordinates": bool,
    "bounding_box": typing.NotRequired[float | None],
    "offset": typing.NotRequired[float | None],
    "user_seed": typing.NotRequired[float | None],
    "mesh_lattice": typing.NotRequired[list[str] | None],
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
        "rbox": rbox_cargs,
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
    }.get(t)


class RboxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rbox(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rbox_params(
    number_points: str,
    dimension: str | None = None,
    integer_coordinates: bool = False,
    bounding_box: float | None = None,
    offset: float | None = None,
    user_seed: float | None = None,
    mesh_lattice: list[str] | None = None,
) -> RboxParameters:
    """
    Build parameters.
    
    Args:
        number_points: Number of random points in cube, lens, spiral, sphere or\
            grid.
        dimension: Dimension (e.g., D3 for 3-d).
        integer_coordinates: Print integer coordinates, default 'Bn' is 1e+06.
        bounding_box: Bounding box coordinates, default 0.5.
        offset: Offset coordinates by n.
        user_seed: Use n as the random number seed.
        mesh_lattice: Lattice (Mesh) rotated by [n,-m,0], [m,n,0], [0,0,r], ...
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rbox",
        "number_points": number_points,
        "integer_coordinates": integer_coordinates,
    }
    if dimension is not None:
        params["dimension"] = dimension
    if bounding_box is not None:
        params["bounding_box"] = bounding_box
    if offset is not None:
        params["offset"] = offset
    if user_seed is not None:
        params["user_seed"] = user_seed
    if mesh_lattice is not None:
        params["mesh_lattice"] = mesh_lattice
    return params


def rbox_cargs(
    params: RboxParameters,
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
    cargs.append("rbox")
    cargs.append(params.get("number_points"))
    if params.get("dimension") is not None:
        cargs.append(params.get("dimension"))
    if params.get("integer_coordinates"):
        cargs.append("z")
    if params.get("bounding_box") is not None:
        cargs.extend([
            "B",
            str(params.get("bounding_box"))
        ])
    if params.get("offset") is not None:
        cargs.extend([
            "O",
            str(params.get("offset"))
        ])
    if params.get("user_seed") is not None:
        cargs.extend([
            "t",
            str(params.get("user_seed"))
        ])
    if params.get("mesh_lattice") is not None:
        cargs.extend([
            "M",
            *params.get("mesh_lattice")
        ])
    return cargs


def rbox_outputs(
    params: RboxParameters,
    execution: Execution,
) -> RboxOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RboxOutputs(
        root=execution.output_file("."),
    )
    return ret


def rbox_execute(
    params: RboxParameters,
    execution: Execution,
) -> RboxOutputs:
    """
    Generate various point distributions. Default is random in cube.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RboxOutputs`).
    """
    params = execution.params(params)
    cargs = rbox_cargs(params, execution)
    ret = rbox_outputs(params, execution)
    execution.run(cargs)
    return ret


def rbox(
    number_points: str,
    dimension: str | None = None,
    integer_coordinates: bool = False,
    bounding_box: float | None = None,
    offset: float | None = None,
    user_seed: float | None = None,
    mesh_lattice: list[str] | None = None,
    runner: Runner | None = None,
) -> RboxOutputs:
    """
    Generate various point distributions. Default is random in cube.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        number_points: Number of random points in cube, lens, spiral, sphere or\
            grid.
        dimension: Dimension (e.g., D3 for 3-d).
        integer_coordinates: Print integer coordinates, default 'Bn' is 1e+06.
        bounding_box: Bounding box coordinates, default 0.5.
        offset: Offset coordinates by n.
        user_seed: Use n as the random number seed.
        mesh_lattice: Lattice (Mesh) rotated by [n,-m,0], [m,n,0], [0,0,r], ...
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RboxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RBOX_METADATA)
    params = rbox_params(
        number_points=number_points,
        dimension=dimension,
        integer_coordinates=integer_coordinates,
        bounding_box=bounding_box,
        offset=offset,
        user_seed=user_seed,
        mesh_lattice=mesh_lattice,
    )
    return rbox_execute(params, execution)


__all__ = [
    "RBOX_METADATA",
    "RboxOutputs",
    "RboxParameters",
    "rbox",
    "rbox_params",
]
