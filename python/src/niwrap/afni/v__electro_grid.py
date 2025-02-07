# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__ELECTRO_GRID_METADATA = Metadata(
    id="8d964e948445e43b1078948d73794b4d6f87e09a.boutiques",
    name="@ElectroGrid",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VElectroGridParameters = typing.TypedDict('VElectroGridParameters', {
    "__STYX_TYPE__": typing.Literal["@ElectroGrid"],
    "strip": typing.NotRequired[int | None],
    "grid": typing.NotRequired[list[int] | None],
    "prefix": typing.NotRequired[str | None],
    "coords": typing.NotRequired[InputPathType | None],
    "with_markers": bool,
    "echo": bool,
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
        "@ElectroGrid": v__electro_grid_cargs,
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
        "@ElectroGrid": v__electro_grid_outputs,
    }.get(t)


class VElectroGridOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__electro_grid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType | None
    """Output surface file"""


def v__electro_grid_params(
    strip: int | None = None,
    grid: list[int] | None = None,
    prefix: str | None = None,
    coords: InputPathType | None = None,
    with_markers: bool = False,
    echo: bool = False,
) -> VElectroGridParameters:
    """
    Build parameters.
    
    Args:
        strip: Make an Nx strip (array) of electrodes.
        grid: Make an Nx by Ny grid of electrodes. A node at (i,j) has a node\
            ID = i+Nx*j with 0<=i<Nx and 0<=j<=Ny.
        prefix: Use PREFIX for the output surface.
        coords: Specify the coordinates of the nodes on the grid, or the array.\
            XYZ.1D should have three columns, with each row specifying the\
            coordinates of one node.
        with_markers: Add markers to the surface at each electrode.
        echo: Set echo.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ElectroGrid",
        "with_markers": with_markers,
        "echo": echo,
    }
    if strip is not None:
        params["strip"] = strip
    if grid is not None:
        params["grid"] = grid
    if prefix is not None:
        params["prefix"] = prefix
    if coords is not None:
        params["coords"] = coords
    return params


def v__electro_grid_cargs(
    params: VElectroGridParameters,
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
    cargs.append("@ElectroGrid")
    if params.get("strip") is not None:
        cargs.extend([
            "-strip",
            str(params.get("strip"))
        ])
    if params.get("grid") is not None:
        cargs.extend([
            "-grid",
            *map(str, params.get("grid"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("coords") is not None:
        cargs.extend([
            "-coords",
            execution.input_file(params.get("coords"))
        ])
    if params.get("with_markers"):
        cargs.append("-with_markers")
    if params.get("echo"):
        cargs.append("-echo")
    return cargs


def v__electro_grid_outputs(
    params: VElectroGridParameters,
    execution: Execution,
) -> VElectroGridOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VElectroGridOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file(params.get("prefix") + ".gii") if (params.get("prefix") is not None) else None,
    )
    return ret


def v__electro_grid_execute(
    params: VElectroGridParameters,
    execution: Execution,
) -> VElectroGridOutputs:
    """
    Creates a mesh representation of an electrode grid for use with SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VElectroGridOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__electro_grid_cargs(params, execution)
    ret = v__electro_grid_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__electro_grid(
    strip: int | None = None,
    grid: list[int] | None = None,
    prefix: str | None = None,
    coords: InputPathType | None = None,
    with_markers: bool = False,
    echo: bool = False,
    runner: Runner | None = None,
) -> VElectroGridOutputs:
    """
    Creates a mesh representation of an electrode grid for use with SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        strip: Make an Nx strip (array) of electrodes.
        grid: Make an Nx by Ny grid of electrodes. A node at (i,j) has a node\
            ID = i+Nx*j with 0<=i<Nx and 0<=j<=Ny.
        prefix: Use PREFIX for the output surface.
        coords: Specify the coordinates of the nodes on the grid, or the array.\
            XYZ.1D should have three columns, with each row specifying the\
            coordinates of one node.
        with_markers: Add markers to the surface at each electrode.
        echo: Set echo.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VElectroGridOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ELECTRO_GRID_METADATA)
    params = v__electro_grid_params(strip=strip, grid=grid, prefix=prefix, coords=coords, with_markers=with_markers, echo=echo)
    return v__electro_grid_execute(params, execution)


__all__ = [
    "VElectroGridOutputs",
    "VElectroGridParameters",
    "V__ELECTRO_GRID_METADATA",
    "v__electro_grid",
    "v__electro_grid_params",
]
