# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PEAKS2AMP_METADATA = Metadata(
    id="90ed8fa8022a8bb67e41e995c1aaf7cea334db02.boutiques",
    name="peaks2amp",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Peaks2ampConfigParameters = typing.TypedDict('Peaks2ampConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Peaks2ampParameters = typing.TypedDict('Peaks2ampParameters', {
    "__STYX_TYPE__": typing.Literal["peaks2amp"],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Peaks2ampConfigParameters] | None],
    "help": bool,
    "version": bool,
    "directions": InputPathType,
    "amplitudes": str,
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
        "peaks2amp": peaks2amp_cargs,
        "config": peaks2amp_config_cargs,
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
        "peaks2amp": peaks2amp_outputs,
    }
    return vt.get(t)


def peaks2amp_config_params(
    key: str,
    value: str,
) -> Peaks2ampConfigParameters:
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


def peaks2amp_config_cargs(
    params: Peaks2ampConfigParameters,
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


class Peaks2ampOutputs(typing.NamedTuple):
    """
    Output object returned when calling `peaks2amp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    amplitudes: OutputPathType
    """the output amplitudes image."""


def peaks2amp_params(
    directions: InputPathType,
    amplitudes: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Peaks2ampConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Peaks2ampParameters:
    """
    Build parameters.
    
    Args:
        directions: the input directions image. Each volume corresponds to the\
            x, y & z component of each direction vector in turn.
        amplitudes: the output amplitudes image.
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
        "__STYXTYPE__": "peaks2amp",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "directions": directions,
        "amplitudes": amplitudes,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def peaks2amp_cargs(
    params: Peaks2ampParameters,
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
    cargs.append("peaks2amp")
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
    cargs.append(execution.input_file(params.get("directions")))
    cargs.append(params.get("amplitudes"))
    return cargs


def peaks2amp_outputs(
    params: Peaks2ampParameters,
    execution: Execution,
) -> Peaks2ampOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Peaks2ampOutputs(
        root=execution.output_file("."),
        amplitudes=execution.output_file(params.get("amplitudes")),
    )
    return ret


def peaks2amp_execute(
    params: Peaks2ampParameters,
    execution: Execution,
) -> Peaks2ampOutputs:
    """
    Extract amplitudes from a peak directions image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Peaks2ampOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = peaks2amp_cargs(params, execution)
    ret = peaks2amp_outputs(params, execution)
    execution.run(cargs)
    return ret


def peaks2amp(
    directions: InputPathType,
    amplitudes: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Peaks2ampConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Peaks2ampOutputs:
    """
    Extract amplitudes from a peak directions image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        directions: the input directions image. Each volume corresponds to the\
            x, y & z component of each direction vector in turn.
        amplitudes: the output amplitudes image.
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
        NamedTuple of outputs (described in `Peaks2ampOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PEAKS2AMP_METADATA)
    params = peaks2amp_params(info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, directions=directions, amplitudes=amplitudes)
    return peaks2amp_execute(params, execution)


__all__ = [
    "PEAKS2AMP_METADATA",
    "Peaks2ampConfigParameters",
    "Peaks2ampOutputs",
    "Peaks2ampParameters",
    "peaks2amp",
    "peaks2amp_config_params",
    "peaks2amp_params",
]
