# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MESH2VOXEL_METADATA = Metadata(
    id="28b90b1b324afdb41ad9cab0242950bac08d3bdd.boutiques",
    name="mesh2voxel",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Mesh2voxelConfigParameters = typing.TypedDict('Mesh2voxelConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Mesh2voxelParameters = typing.TypedDict('Mesh2voxelParameters', {
    "__STYX_TYPE__": typing.Literal["mesh2voxel"],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Mesh2voxelConfigParameters] | None],
    "help": bool,
    "version": bool,
    "source": InputPathType,
    "template": InputPathType,
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
        "mesh2voxel": mesh2voxel_cargs,
        "config": mesh2voxel_config_cargs,
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
        "mesh2voxel": mesh2voxel_outputs,
        "config": mesh2voxel_config_outputs,
    }.get(t)


def mesh2voxel_config_params(
    key: str,
    value: str,
) -> Mesh2voxelConfigParameters:
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


def mesh2voxel_config_cargs(
    params: Mesh2voxelConfigParameters,
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


class Mesh2voxelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mesh2voxel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image"""


def mesh2voxel_params(
    source: InputPathType,
    template: InputPathType,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Mesh2voxelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Mesh2voxelParameters:
    """
    Build parameters.
    
    Args:
        source: the mesh file; note vertices must be defined in realspace\
            coordinates.
        template: the template image.
        output: the output image.
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
        "__STYXTYPE__": "mesh2voxel",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "source": source,
        "template": template,
        "output": output,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mesh2voxel_cargs(
    params: Mesh2voxelParameters,
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
    cargs.append("mesh2voxel")
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
    cargs.append(execution.input_file(params.get("source")))
    cargs.append(execution.input_file(params.get("template")))
    cargs.append(params.get("output"))
    return cargs


def mesh2voxel_outputs(
    params: Mesh2voxelParameters,
    execution: Execution,
) -> Mesh2voxelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Mesh2voxelOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def mesh2voxel_execute(
    params: Mesh2voxelParameters,
    execution: Execution,
) -> Mesh2voxelOutputs:
    """
    Convert a mesh surface to a partial volume estimation image.
    
    
    
    References:
    
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A.
    Anatomically-constrained tractography: Improved diffusion MRI streamlines
    tractography through effective use of anatomical information. NeuroImage,
    2012, 62, 1924-1938.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Mesh2voxelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mesh2voxel_cargs(params, execution)
    ret = mesh2voxel_outputs(params, execution)
    execution.run(cargs)
    return ret


def mesh2voxel(
    source: InputPathType,
    template: InputPathType,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Mesh2voxelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Mesh2voxelOutputs:
    """
    Convert a mesh surface to a partial volume estimation image.
    
    
    
    References:
    
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A.
    Anatomically-constrained tractography: Improved diffusion MRI streamlines
    tractography through effective use of anatomical information. NeuroImage,
    2012, 62, 1924-1938.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        source: the mesh file; note vertices must be defined in realspace\
            coordinates.
        template: the template image.
        output: the output image.
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
        NamedTuple of outputs (described in `Mesh2voxelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MESH2VOXEL_METADATA)
    params = mesh2voxel_params(info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, source=source, template=template, output=output)
    return mesh2voxel_execute(params, execution)


__all__ = [
    "MESH2VOXEL_METADATA",
    "Mesh2voxelConfigParameters",
    "Mesh2voxelOutputs",
    "Mesh2voxelParameters",
    "mesh2voxel",
    "mesh2voxel_config_params",
    "mesh2voxel_params",
]
