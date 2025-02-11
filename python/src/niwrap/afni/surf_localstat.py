# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_LOCALSTAT_METADATA = Metadata(
    id="5a51275b28d3b9824220c99fed994126246f2f36.boutiques",
    name="SurfLocalstat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfLocalstatParameters = typing.TypedDict('SurfLocalstatParameters', {
    "__STYX_TYPE__": typing.Literal["SurfLocalstat"],
    "hood": typing.NotRequired[float | None],
    "nbhd_rad": typing.NotRequired[float | None],
    "prefix": str,
    "stat": typing.Literal["mean", "mode", "num", "FWHM", "ALL"],
    "input_dataset": InputPathType,
    "surface": InputPathType,
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
        "SurfLocalstat": surf_localstat_cargs,
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
        "SurfLocalstat": surf_localstat_outputs,
    }.get(t)


class SurfLocalstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_localstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Computed local statistics dataset"""


def surf_localstat_params(
    prefix: str,
    stat_: typing.Literal["mean", "mode", "num", "FWHM", "ALL"],
    input_dataset: InputPathType,
    surface: InputPathType,
    hood: float | None = None,
    nbhd_rad: float | None = None,
) -> SurfLocalstatParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix of output data set.
        stat_: Compute the specified statistic on the values extracted from the\
            region around each voxel. Options: mean, mode, num, FWHM, ALL.
        input_dataset: Input dataset.
        surface: Input GIFTI surface file.
        hood: Neighborhood of nodes within the specified radius R.
        nbhd_rad: Distance from node n as measured by the shortest distance\
            along the mesh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfLocalstat",
        "prefix": prefix,
        "stat": stat_,
        "input_dataset": input_dataset,
        "surface": surface,
    }
    if hood is not None:
        params["hood"] = hood
    if nbhd_rad is not None:
        params["nbhd_rad"] = nbhd_rad
    return params


def surf_localstat_cargs(
    params: SurfLocalstatParameters,
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
    cargs.append("SurfLocalstat")
    if params.get("hood") is not None:
        cargs.extend([
            "-hood",
            str(params.get("hood"))
        ])
    if params.get("nbhd_rad") is not None:
        cargs.extend([
            "-nbhd_rad",
            str(params.get("nbhd_rad"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.extend([
        "-stat",
        params.get("stat")
    ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_dataset"))
    ])
    cargs.extend([
        "-i_gii",
        execution.input_file(params.get("surface"))
    ])
    return cargs


def surf_localstat_outputs(
    params: SurfLocalstatParameters,
    execution: Execution,
) -> SurfLocalstatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfLocalstatOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".niml.dset"),
    )
    return ret


def surf_localstat_execute(
    params: SurfLocalstatParameters,
    execution: Execution,
) -> SurfLocalstatOutputs:
    """
    Compute local statistics on a surface mesh.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfLocalstatOutputs`).
    """
    cargs = surf_localstat_cargs(params, execution)
    ret = surf_localstat_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_localstat(
    prefix: str,
    stat_: typing.Literal["mean", "mode", "num", "FWHM", "ALL"],
    input_dataset: InputPathType,
    surface: InputPathType,
    hood: float | None = None,
    nbhd_rad: float | None = None,
    runner: Runner | None = None,
) -> SurfLocalstatOutputs:
    """
    Compute local statistics on a surface mesh.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix of output data set.
        stat_: Compute the specified statistic on the values extracted from the\
            region around each voxel. Options: mean, mode, num, FWHM, ALL.
        input_dataset: Input dataset.
        surface: Input GIFTI surface file.
        hood: Neighborhood of nodes within the specified radius R.
        nbhd_rad: Distance from node n as measured by the shortest distance\
            along the mesh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfLocalstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_LOCALSTAT_METADATA)
    params = surf_localstat_params(hood=hood, nbhd_rad=nbhd_rad, prefix=prefix, stat_=stat_, input_dataset=input_dataset, surface=surface)
    return surf_localstat_execute(params, execution)


__all__ = [
    "SURF_LOCALSTAT_METADATA",
    "SurfLocalstatOutputs",
    "SurfLocalstatParameters",
    "surf_localstat",
    "surf_localstat_params",
]
