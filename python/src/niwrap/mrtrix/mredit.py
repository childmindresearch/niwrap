# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MREDIT_METADATA = Metadata(
    id="930fabdd0dfa28ab193511318650c392dd3867c2.boutiques",
    name="mredit",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MreditPlaneParameters = typing.TypedDict('MreditPlaneParameters', {
    "__STYX_TYPE__": typing.Literal["plane"],
    "axis": int,
    "coord": list[int],
    "value": float,
})
MreditSphereParameters = typing.TypedDict('MreditSphereParameters', {
    "__STYX_TYPE__": typing.Literal["sphere"],
    "position": list[float],
    "radius": float,
    "value": float,
})
MreditVoxelParameters = typing.TypedDict('MreditVoxelParameters', {
    "__STYX_TYPE__": typing.Literal["voxel"],
    "position": list[float],
    "value": float,
})
MreditConfigParameters = typing.TypedDict('MreditConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MreditParameters = typing.TypedDict('MreditParameters', {
    "__STYX_TYPE__": typing.Literal["mredit"],
    "plane": typing.NotRequired[list[MreditPlaneParameters] | None],
    "sphere": typing.NotRequired[list[MreditSphereParameters] | None],
    "voxel": typing.NotRequired[list[MreditVoxelParameters] | None],
    "scanner": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MreditConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "output": typing.NotRequired[str | None],
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
        "mredit": mredit_cargs,
        "plane": mredit_plane_cargs,
        "sphere": mredit_sphere_cargs,
        "voxel": mredit_voxel_cargs,
        "config": mredit_config_cargs,
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
        "mredit": mredit_outputs,
    }
    return vt.get(t)


def mredit_plane_params(
    axis: int,
    coord: list[int],
    value: float,
) -> MreditPlaneParameters:
    """
    Build parameters.
    
    Args:
        axis: fill one or more planes on a particular image axis.
        coord: fill one or more planes on a particular image axis.
        value: fill one or more planes on a particular image axis.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "plane",
        "axis": axis,
        "coord": coord,
        "value": value,
    }
    return params


def mredit_plane_cargs(
    params: MreditPlaneParameters,
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
    cargs.append("-plane")
    cargs.append(str(params.get("axis")))
    cargs.extend(map(str, params.get("coord")))
    cargs.append(str(params.get("value")))
    return cargs


def mredit_sphere_params(
    position: list[float],
    radius: float,
    value: float,
) -> MreditSphereParameters:
    """
    Build parameters.
    
    Args:
        position: draw a sphere with radius in mm.
        radius: draw a sphere with radius in mm.
        value: draw a sphere with radius in mm.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sphere",
        "position": position,
        "radius": radius,
        "value": value,
    }
    return params


def mredit_sphere_cargs(
    params: MreditSphereParameters,
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
    cargs.append("-sphere")
    cargs.extend(map(str, params.get("position")))
    cargs.append(str(params.get("radius")))
    cargs.append(str(params.get("value")))
    return cargs


def mredit_voxel_params(
    position: list[float],
    value: float,
) -> MreditVoxelParameters:
    """
    Build parameters.
    
    Args:
        position: change the image value within a single voxel.
        value: change the image value within a single voxel.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "voxel",
        "position": position,
        "value": value,
    }
    return params


def mredit_voxel_cargs(
    params: MreditVoxelParameters,
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
    cargs.append("-voxel")
    cargs.extend(map(str, params.get("position")))
    cargs.append(str(params.get("value")))
    return cargs


def mredit_config_params(
    key: str,
    value: str,
) -> MreditConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def mredit_config_cargs(
    params: MreditConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class MreditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mredit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType | None
    """the (optional) output image"""


def mredit_params(
    input_: InputPathType,
    plane: list[MreditPlaneParameters] | None = None,
    sphere: list[MreditSphereParameters] | None = None,
    voxel: list[MreditVoxelParameters] | None = None,
    scanner: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MreditConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    output: str | None = None,
) -> MreditParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image.
        plane: fill one or more planes on a particular image axis.
        sphere: draw a sphere with radius in mm.
        voxel: change the image value within a single voxel.
        scanner: indicate that coordinates are specified in scanner space,\
            rather than as voxel coordinates.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        output: the (optional) output image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mredit",
        "scanner": scanner,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
    }
    if plane is not None:
        params["plane"] = plane
    if sphere is not None:
        params["sphere"] = sphere
    if voxel is not None:
        params["voxel"] = voxel
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    if output is not None:
        params["output"] = output
    return params


def mredit_cargs(
    params: MreditParameters,
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
    cargs.append("mredit")
    if params.get("plane") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("plane")] for a in c])
    if params.get("sphere") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("sphere")] for a in c])
    if params.get("voxel") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("voxel")] for a in c])
    if params.get("scanner"):
        cargs.append("-scanner")
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("input")))
    if params.get("output") is not None:
        cargs.append(params.get("output"))
    return cargs


def mredit_outputs(
    params: MreditParameters,
    execution: Execution,
) -> MreditOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MreditOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")) if (params.get("output") is not None) else None,
    )
    return ret


def mredit_execute(
    params: MreditParameters,
    execution: Execution,
) -> MreditOutputs:
    """
    Directly edit the intensities within an image from the command-line.
    
    A range of options are provided to enable direct editing of voxel
    intensities based on voxel / real-space coordinates. If only one image path
    is provided, the image will be edited in-place (use at own risk); if input
    and output image paths are provided, the output will contain the edited
    image, and the original image will not be modified in any way.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MreditOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mredit_cargs(params, execution)
    ret = mredit_outputs(params, execution)
    execution.run(cargs)
    return ret


def mredit(
    input_: InputPathType,
    plane: list[MreditPlaneParameters] | None = None,
    sphere: list[MreditSphereParameters] | None = None,
    voxel: list[MreditVoxelParameters] | None = None,
    scanner: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MreditConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    output: str | None = None,
    runner: Runner | None = None,
) -> MreditOutputs:
    """
    Directly edit the intensities within an image from the command-line.
    
    A range of options are provided to enable direct editing of voxel
    intensities based on voxel / real-space coordinates. If only one image path
    is provided, the image will be edited in-place (use at own risk); if input
    and output image paths are provided, the output will contain the edited
    image, and the original image will not be modified in any way.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image.
        plane: fill one or more planes on a particular image axis.
        sphere: draw a sphere with radius in mm.
        voxel: change the image value within a single voxel.
        scanner: indicate that coordinates are specified in scanner space,\
            rather than as voxel coordinates.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        output: the (optional) output image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MreditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MREDIT_METADATA)
    params = mredit_params(plane=plane, sphere=sphere, voxel=voxel, scanner=scanner, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, output=output)
    return mredit_execute(params, execution)


__all__ = [
    "MREDIT_METADATA",
    "MreditConfigParameters",
    "MreditOutputs",
    "MreditParameters",
    "MreditPlaneParameters",
    "MreditSphereParameters",
    "MreditVoxelParameters",
    "mredit",
    "mredit_config_params",
    "mredit_params",
    "mredit_plane_params",
    "mredit_sphere_params",
    "mredit_voxel_params",
]
