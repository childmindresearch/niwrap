# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOXEL2FIXEL_METADATA = Metadata(
    id="5eac19f16617dbecc2080fd5f4f07d1eac6e92da.boutiques",
    name="voxel2fixel",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Voxel2fixelConfigParameters = typing.TypedDict('Voxel2fixelConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Voxel2fixelParameters = typing.TypedDict('Voxel2fixelParameters', {
    "__STYX_TYPE__": typing.Literal["voxel2fixel"],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Voxel2fixelConfigParameters] | None],
    "help": bool,
    "version": bool,
    "image_in": InputPathType,
    "fixel_directory_in": InputPathType,
    "fixel_directory_out": str,
    "fixel_data_out": str,
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
        "voxel2fixel": voxel2fixel_cargs,
        "config": voxel2fixel_config_cargs,
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
    vt = {}
    return vt.get(t)


def voxel2fixel_config_params(
    key: str,
    value: str,
) -> Voxel2fixelConfigParameters:
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


def voxel2fixel_config_cargs(
    params: Voxel2fixelConfigParameters,
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


class Voxel2fixelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `voxel2fixel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def voxel2fixel_params(
    image_in: InputPathType,
    fixel_directory_in: InputPathType,
    fixel_directory_out: str,
    fixel_data_out: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Voxel2fixelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Voxel2fixelParameters:
    """
    Build parameters.
    
    Args:
        image_in: the input image.
        fixel_directory_in: the input fixel directory. Used to define the\
            fixels and their directions.
        fixel_directory_out: the fixel directory where the output will be\
            written. This can be the same as the input directory if desired.
        fixel_data_out: the name of the fixel data image.
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
        "__STYXTYPE__": "voxel2fixel",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "image_in": image_in,
        "fixel_directory_in": fixel_directory_in,
        "fixel_directory_out": fixel_directory_out,
        "fixel_data_out": fixel_data_out,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def voxel2fixel_cargs(
    params: Voxel2fixelParameters,
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
    cargs.append("voxel2fixel")
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
    cargs.append(execution.input_file(params.get("image_in")))
    cargs.append(execution.input_file(params.get("fixel_directory_in")))
    cargs.append(params.get("fixel_directory_out"))
    cargs.append(params.get("fixel_data_out"))
    return cargs


def voxel2fixel_outputs(
    params: Voxel2fixelParameters,
    execution: Execution,
) -> Voxel2fixelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Voxel2fixelOutputs(
        root=execution.output_file("."),
    )
    return ret


def voxel2fixel_execute(
    params: Voxel2fixelParameters,
    execution: Execution,
) -> Voxel2fixelOutputs:
    """
    Map the scalar value in each voxel to all fixels within that voxel.
    
    This command is designed to enable CFE-based statistical analysis to be
    performed on voxel-wise measures.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Voxel2fixelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = voxel2fixel_cargs(params, execution)
    ret = voxel2fixel_outputs(params, execution)
    execution.run(cargs)
    return ret


def voxel2fixel(
    image_in: InputPathType,
    fixel_directory_in: InputPathType,
    fixel_directory_out: str,
    fixel_data_out: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Voxel2fixelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Voxel2fixelOutputs:
    """
    Map the scalar value in each voxel to all fixels within that voxel.
    
    This command is designed to enable CFE-based statistical analysis to be
    performed on voxel-wise measures.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        image_in: the input image.
        fixel_directory_in: the input fixel directory. Used to define the\
            fixels and their directions.
        fixel_directory_out: the fixel directory where the output will be\
            written. This can be the same as the input directory if desired.
        fixel_data_out: the name of the fixel data image.
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
        NamedTuple of outputs (described in `Voxel2fixelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOXEL2FIXEL_METADATA)
    params = voxel2fixel_params(info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, image_in=image_in, fixel_directory_in=fixel_directory_in, fixel_directory_out=fixel_directory_out, fixel_data_out=fixel_data_out)
    return voxel2fixel_execute(params, execution)


__all__ = [
    "VOXEL2FIXEL_METADATA",
    "Voxel2fixelConfigParameters",
    "Voxel2fixelOutputs",
    "Voxel2fixelParameters",
    "voxel2fixel",
    "voxel2fixel_config_params",
    "voxel2fixel_params",
]
