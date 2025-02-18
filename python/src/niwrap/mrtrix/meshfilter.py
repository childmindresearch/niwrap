# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MESHFILTER_METADATA = Metadata(
    id="60786a8c6290d7bdf51b9e5b7367257fed09c188.boutiques",
    name="meshfilter",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MeshfilterConfigParameters = typing.TypedDict('MeshfilterConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MeshfilterParameters = typing.TypedDict('MeshfilterParameters', {
    "__STYX_TYPE__": typing.Literal["meshfilter"],
    "smooth_spatial": typing.NotRequired[float | None],
    "smooth_influence": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MeshfilterConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "filter": str,
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
        "meshfilter": meshfilter_cargs,
        "config": meshfilter_config_cargs,
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
        "meshfilter": meshfilter_outputs,
    }.get(t)


def meshfilter_config_params(
    key: str,
    value: str,
) -> MeshfilterConfigParameters:
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


def meshfilter_config_cargs(
    params: MeshfilterConfigParameters,
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


class MeshfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `meshfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output mesh file"""


def meshfilter_params(
    input_: InputPathType,
    filter_: str,
    output: str,
    smooth_spatial: float | None = None,
    smooth_influence: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MeshfilterConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MeshfilterParameters:
    """
    Build parameters.
    
    Args:
        input_: the input mesh file.
        filter_: the filter to apply.Options are: smooth.
        output: the output mesh file.
        smooth_spatial: spatial extent of smoothing (default: 10mm).
        smooth_influence: influence factor for smoothing (default: 10).
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
        "__STYXTYPE__": "meshfilter",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "filter": filter_,
        "output": output,
    }
    if smooth_spatial is not None:
        params["smooth_spatial"] = smooth_spatial
    if smooth_influence is not None:
        params["smooth_influence"] = smooth_influence
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def meshfilter_cargs(
    params: MeshfilterParameters,
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
    cargs.append("meshfilter")
    if params.get("smooth_spatial") is not None:
        cargs.extend([
            "-smooth_spatial",
            str(params.get("smooth_spatial"))
        ])
    if params.get("smooth_influence") is not None:
        cargs.extend([
            "-smooth_influence",
            str(params.get("smooth_influence"))
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
    cargs.append(params.get("filter"))
    cargs.append(params.get("output"))
    return cargs


def meshfilter_outputs(
    params: MeshfilterParameters,
    execution: Execution,
) -> MeshfilterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MeshfilterOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def meshfilter_execute(
    params: MeshfilterParameters,
    execution: Execution,
) -> MeshfilterOutputs:
    """
    Apply filter operations to meshes.
    
    While this command has only one filter operation currently available, it
    nevertheless presents with a comparable interface to the MRtrix3 commands
    maskfilter and mrfilter commands.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MeshfilterOutputs`).
    """
    params = execution.params(params)
    cargs = meshfilter_cargs(params, execution)
    ret = meshfilter_outputs(params, execution)
    execution.run(cargs)
    return ret


def meshfilter(
    input_: InputPathType,
    filter_: str,
    output: str,
    smooth_spatial: float | None = None,
    smooth_influence: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MeshfilterConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MeshfilterOutputs:
    """
    Apply filter operations to meshes.
    
    While this command has only one filter operation currently available, it
    nevertheless presents with a comparable interface to the MRtrix3 commands
    maskfilter and mrfilter commands.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input mesh file.
        filter_: the filter to apply.Options are: smooth.
        output: the output mesh file.
        smooth_spatial: spatial extent of smoothing (default: 10mm).
        smooth_influence: influence factor for smoothing (default: 10).
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
        NamedTuple of outputs (described in `MeshfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MESHFILTER_METADATA)
    params = meshfilter_params(smooth_spatial=smooth_spatial, smooth_influence=smooth_influence, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, filter_=filter_, output=output)
    return meshfilter_execute(params, execution)


__all__ = [
    "MESHFILTER_METADATA",
    "MeshfilterConfigParameters",
    "MeshfilterOutputs",
    "MeshfilterParameters",
    "meshfilter",
    "meshfilter_config_params",
    "meshfilter_params",
]
