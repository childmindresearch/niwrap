# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOXEL2MESH_METADATA = Metadata(
    id="61319a325faead4ced930defcbdd82b99a6a72af.boutiques",
    name="voxel2mesh",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Voxel2meshConfigParameters = typing.TypedDict('Voxel2meshConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Voxel2meshParameters = typing.TypedDict('Voxel2meshParameters', {
    "__STYX_TYPE__": typing.Literal["voxel2mesh"],
    "blocky": bool,
    "threshold": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Voxel2meshConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "output": str,
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
        "voxel2mesh": voxel2mesh_cargs,
        "config": voxel2mesh_config_cargs,
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
        "voxel2mesh": voxel2mesh_outputs,
    }.get(t)


def voxel2mesh_config_params(
    key: str,
    value: str,
) -> Voxel2meshConfigParameters:
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


def voxel2mesh_config_cargs(
    params: Voxel2meshConfigParameters,
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


class Voxel2meshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `voxel2mesh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output mesh file."""


def voxel2mesh_params(
    input_: InputPathType,
    output: str,
    blocky: bool = False,
    threshold: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Voxel2meshConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Voxel2meshParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image.
        output: the output mesh file.
        blocky: generate a 'blocky' mesh that precisely represents the voxel\
            edges.
        threshold: manually set the intensity threshold for the Marching Cubes\
            algorithm.
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "voxel2mesh",
        "blocky": blocky,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def voxel2mesh_cargs(
    params: Voxel2meshParameters,
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
    cargs.append("voxel2mesh")
    if params.get("blocky"):
        cargs.append("-blocky")
    if params.get("threshold") is not None:
        cargs.extend([
            "-threshold",
            str(params.get("threshold"))
        ])
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
    cargs.append(params.get("output"))
    return cargs


def voxel2mesh_outputs(
    params: Voxel2meshParameters,
    execution: Execution,
) -> Voxel2meshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Voxel2meshOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def voxel2mesh_execute(
    params: Voxel2meshParameters,
    execution: Execution,
) -> Voxel2meshOutputs:
    """
    Generate a surface mesh representation from a voxel image.
    
    This command utilises the Marching Cubes algorithm to generate a polygonal
    surface that represents the isocontour(s) of the input image at a particular
    intensity. By default, an appropriate threshold will be determined
    automatically from the input image, however the intensity value of the
    isocontour(s) can instead be set manually using the -threhsold option.
    
    If the -blocky option is used, then the Marching Cubes algorithm will not be
    used. Instead, the input image will be interpreted as a binary mask image,
    and polygonal surfaces will be generated at the outer faces of the voxel
    clusters within the mask.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Voxel2meshOutputs`).
    """
    params = execution.params(params)
    cargs = voxel2mesh_cargs(params, execution)
    ret = voxel2mesh_outputs(params, execution)
    execution.run(cargs)
    return ret


def voxel2mesh(
    input_: InputPathType,
    output: str,
    blocky: bool = False,
    threshold: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Voxel2meshConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Voxel2meshOutputs:
    """
    Generate a surface mesh representation from a voxel image.
    
    This command utilises the Marching Cubes algorithm to generate a polygonal
    surface that represents the isocontour(s) of the input image at a particular
    intensity. By default, an appropriate threshold will be determined
    automatically from the input image, however the intensity value of the
    isocontour(s) can instead be set manually using the -threhsold option.
    
    If the -blocky option is used, then the Marching Cubes algorithm will not be
    used. Instead, the input image will be interpreted as a binary mask image,
    and polygonal surfaces will be generated at the outer faces of the voxel
    clusters within the mask.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image.
        output: the output mesh file.
        blocky: generate a 'blocky' mesh that precisely represents the voxel\
            edges.
        threshold: manually set the intensity threshold for the Marching Cubes\
            algorithm.
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
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Voxel2meshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOXEL2MESH_METADATA)
    params = voxel2mesh_params(blocky=blocky, threshold=threshold, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, output=output)
    return voxel2mesh_execute(params, execution)


__all__ = [
    "VOXEL2MESH_METADATA",
    "Voxel2meshConfigParameters",
    "Voxel2meshOutputs",
    "Voxel2meshParameters",
    "voxel2mesh",
    "voxel2mesh_config_params",
    "voxel2mesh_params",
]
