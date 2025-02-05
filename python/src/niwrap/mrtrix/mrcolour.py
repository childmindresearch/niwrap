# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRCOLOUR_METADATA = Metadata(
    id="5c34d1664fe214212552914265860aab8fddd651.boutiques",
    name="mrcolour",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MrcolourConfigParameters = typing.TypedDict('MrcolourConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MrcolourParameters = typing.TypedDict('MrcolourParameters', {
    "__STYX_TYPE__": typing.Literal["mrcolour"],
    "upper": typing.NotRequired[float | None],
    "lower": typing.NotRequired[float | None],
    "colour": typing.NotRequired[list[float] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrcolourConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "map": str,
    "output": str,
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
        "mrcolour": mrcolour_cargs,
        "config": mrcolour_config_cargs,
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
        "mrcolour": mrcolour_outputs,
    }
    return vt.get(t)


def mrcolour_config_params(
    key: str,
    value: str,
) -> MrcolourConfigParameters:
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


def mrcolour_config_cargs(
    params: MrcolourConfigParameters,
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


class MrcolourOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrcolour(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image"""


def mrcolour_params(
    input_: InputPathType,
    map_: str,
    output: str,
    upper: float | None = None,
    lower: float | None = None,
    colour: list[float] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcolourConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrcolourParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image.
        map_: the colourmap to apply; choices are:\
            gray,hot,cool,jet,inferno,viridis,pet,colour,rgb.
        output: the output image.
        upper: manually set the upper intensity of the colour mapping.
        lower: manually set the lower intensity of the colour mapping.
        colour: set the target colour for use of the 'colour' map (three\
            comma-separated floating-point values).
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
        "__STYXTYPE__": "mrcolour",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "map": map_,
        "output": output,
    }
    if upper is not None:
        params["upper"] = upper
    if lower is not None:
        params["lower"] = lower
    if colour is not None:
        params["colour"] = colour
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrcolour_cargs(
    params: MrcolourParameters,
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
    cargs.append("mrcolour")
    if params.get("upper") is not None:
        cargs.extend([
            "-upper",
            str(params.get("upper"))
        ])
    if params.get("lower") is not None:
        cargs.extend([
            "-lower",
            str(params.get("lower"))
        ])
    if params.get("colour") is not None:
        cargs.extend([
            "-colour",
            ",".join(map(str, params.get("colour")))
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
    cargs.append(params.get("map"))
    cargs.append(params.get("output"))
    return cargs


def mrcolour_outputs(
    params: MrcolourParameters,
    execution: Execution,
) -> MrcolourOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrcolourOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def mrcolour_execute(
    params: MrcolourParameters,
    execution: Execution,
) -> MrcolourOutputs:
    """
    Apply a colour map to an image.
    
    Under typical usage, this command will receive as input ad 3D greyscale
    image, and output a 4D image with 3 volumes corresponding to red-green-blue
    components; other use cases are possible, and are described in more detail
    below.
    
    By default, the command will automatically determine the maximum and minimum
    intensities of the input image, and use that information to set the upper
    and lower bounds of the applied colourmap. This behaviour can be overridden
    by manually specifying these bounds using the -upper and -lower options
    respectively.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrcolourOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mrcolour_cargs(params, execution)
    ret = mrcolour_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrcolour(
    input_: InputPathType,
    map_: str,
    output: str,
    upper: float | None = None,
    lower: float | None = None,
    colour: list[float] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcolourConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrcolourOutputs:
    """
    Apply a colour map to an image.
    
    Under typical usage, this command will receive as input ad 3D greyscale
    image, and output a 4D image with 3 volumes corresponding to red-green-blue
    components; other use cases are possible, and are described in more detail
    below.
    
    By default, the command will automatically determine the maximum and minimum
    intensities of the input image, and use that information to set the upper
    and lower bounds of the applied colourmap. This behaviour can be overridden
    by manually specifying these bounds using the -upper and -lower options
    respectively.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image.
        map_: the colourmap to apply; choices are:\
            gray,hot,cool,jet,inferno,viridis,pet,colour,rgb.
        output: the output image.
        upper: manually set the upper intensity of the colour mapping.
        lower: manually set the lower intensity of the colour mapping.
        colour: set the target colour for use of the 'colour' map (three\
            comma-separated floating-point values).
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
        NamedTuple of outputs (described in `MrcolourOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRCOLOUR_METADATA)
    params = mrcolour_params(upper=upper, lower=lower, colour=colour, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, map_=map_, output=output)
    return mrcolour_execute(params, execution)


__all__ = [
    "MRCOLOUR_METADATA",
    "MrcolourConfigParameters",
    "MrcolourOutputs",
    "MrcolourParameters",
    "mrcolour",
    "mrcolour_config_params",
    "mrcolour_params",
]
