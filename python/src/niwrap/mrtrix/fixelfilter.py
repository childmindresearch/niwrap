# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIXELFILTER_METADATA = Metadata(
    id="de612300fec8260dbe9407acf8595be232354182.boutiques",
    name="fixelfilter",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
FixelfilterConfigParameters = typing.TypedDict('FixelfilterConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
FixelfilterVariousStringParameters = typing.TypedDict('FixelfilterVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
FixelfilterVariousFileParameters = typing.TypedDict('FixelfilterVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
FixelfilterVariousStringParameters_ = typing.TypedDict('FixelfilterVariousStringParameters_', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
FixelfilterVariousFileParameters_ = typing.TypedDict('FixelfilterVariousFileParameters_', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
FixelfilterParameters = typing.TypedDict('FixelfilterParameters', {
    "__STYX_TYPE__": typing.Literal["fixelfilter"],
    "matrix": InputPathType,
    "threshold_value": typing.NotRequired[float | None],
    "threshold_connectivity": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
    "minweight": typing.NotRequired[float | None],
    "mask": typing.NotRequired[InputPathType | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[FixelfilterConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": typing.Union[FixelfilterVariousStringParameters, FixelfilterVariousFileParameters],
    "filter": str,
    "output": typing.Union[FixelfilterVariousStringParameters_, FixelfilterVariousFileParameters_],
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
        "fixelfilter": fixelfilter_cargs,
        "config": fixelfilter_config_cargs,
        "VariousString": fixelfilter_various_string_cargs,
        "VariousFile": fixelfilter_various_file_cargs,
        "VariousString": fixelfilter_various_string_cargs_,
        "VariousFile": fixelfilter_various_file_cargs_,
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


def fixelfilter_config_params(
    key: str,
    value: str,
) -> FixelfilterConfigParameters:
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


def fixelfilter_config_cargs(
    params: FixelfilterConfigParameters,
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


def fixelfilter_various_string_params(
    obj: str,
) -> FixelfilterVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def fixelfilter_various_string_cargs(
    params: FixelfilterVariousStringParameters,
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
    cargs.append(params.get("obj"))
    return cargs


def fixelfilter_various_file_params(
    obj: InputPathType,
) -> FixelfilterVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def fixelfilter_various_file_cargs(
    params: FixelfilterVariousFileParameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def fixelfilter_various_string_params_(
    obj: str,
) -> FixelfilterVariousStringParameters_:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def fixelfilter_various_string_cargs_(
    params: FixelfilterVariousStringParameters_,
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
    cargs.append(params.get("obj"))
    return cargs


def fixelfilter_various_file_params_(
    obj: InputPathType,
) -> FixelfilterVariousFileParameters_:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def fixelfilter_various_file_cargs_(
    params: FixelfilterVariousFileParameters_,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


class FixelfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fixelfilter_params(
    matrix: InputPathType,
    input_: typing.Union[FixelfilterVariousStringParameters, FixelfilterVariousFileParameters],
    filter_: str,
    output: typing.Union[FixelfilterVariousStringParameters_, FixelfilterVariousFileParameters_],
    threshold_value: float | None = None,
    threshold_connectivity: float | None = None,
    fwhm: float | None = None,
    minweight: float | None = None,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelfilterConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> FixelfilterParameters:
    """
    Build parameters.
    
    Args:
        matrix: provide a fixel-fixel connectivity matrix for filtering\
            operations that require it.
        input_: the input: either a fixel data file, or a fixel directory (see\
            Description).
        filter_: the filtering operation to perform; options are: connect,\
            smooth.
        output: the output: either a fixel data file, or a fixel directory (see\
            Description).
        threshold_value: specify a threshold for the input fixel data file\
            values (default = 0.5).
        threshold_connectivity: specify a fixel-fixel connectivity threshold\
            for connected-component analysis (default = 0.10000000000000001).
        fwhm: the full-width half-maximum (FWHM) of the spatial component of\
            the smoothing filter (default = 10mm).
        minweight: apply a minimum threshold to smoothing weights (default =\
            0.01).
        mask: only perform smoothing within a specified binary fixel mask.
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
        "__STYXTYPE__": "fixelfilter",
        "matrix": matrix,
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
    if threshold_value is not None:
        params["threshold_value"] = threshold_value
    if threshold_connectivity is not None:
        params["threshold_connectivity"] = threshold_connectivity
    if fwhm is not None:
        params["fwhm"] = fwhm
    if minweight is not None:
        params["minweight"] = minweight
    if mask is not None:
        params["mask"] = mask
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def fixelfilter_cargs(
    params: FixelfilterParameters,
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
    cargs.append("fixelfilter")
    cargs.extend([
        "-matrix",
        execution.input_file(params.get("matrix"))
    ])
    if params.get("threshold_value") is not None:
        cargs.extend([
            "-threshold_value",
            str(params.get("threshold_value"))
        ])
    if params.get("threshold_connectivity") is not None:
        cargs.extend([
            "-threshold_connectivity",
            str(params.get("threshold_connectivity"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "-fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("minweight") is not None:
        cargs.extend([
            "-minweight",
            str(params.get("minweight"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
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
    cargs.extend(dyn_cargs(params.get("input")["__STYXTYPE__"])(params.get("input"), execution))
    cargs.append(params.get("filter"))
    cargs.extend(dyn_cargs(params.get("output")["__STYXTYPE__"])(params.get("output"), execution))
    return cargs


def fixelfilter_outputs(
    params: FixelfilterParameters,
    execution: Execution,
) -> FixelfilterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FixelfilterOutputs(
        root=execution.output_file("."),
    )
    return ret


def fixelfilter_execute(
    params: FixelfilterParameters,
    execution: Execution,
) -> FixelfilterOutputs:
    """
    Perform filtering operations on fixel-based data.
    
    If the first input to the command is a specific fixel data file, then a
    filtered version of only that file will be generated by the command.
    Alternatively, if the input is the location of a fixel directory, then the
    command will create a duplicate of the fixel directory, and apply the
    specified filter operation to all fixel data files within the directory.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FixelfilterOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fixelfilter_cargs(params, execution)
    ret = fixelfilter_outputs(params, execution)
    execution.run(cargs)
    return ret


def fixelfilter(
    matrix: InputPathType,
    input_: typing.Union[FixelfilterVariousStringParameters, FixelfilterVariousFileParameters],
    filter_: str,
    output: typing.Union[FixelfilterVariousStringParameters_, FixelfilterVariousFileParameters_],
    threshold_value: float | None = None,
    threshold_connectivity: float | None = None,
    fwhm: float | None = None,
    minweight: float | None = None,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelfilterConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> FixelfilterOutputs:
    """
    Perform filtering operations on fixel-based data.
    
    If the first input to the command is a specific fixel data file, then a
    filtered version of only that file will be generated by the command.
    Alternatively, if the input is the location of a fixel directory, then the
    command will create a duplicate of the fixel directory, and apply the
    specified filter operation to all fixel data files within the directory.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        matrix: provide a fixel-fixel connectivity matrix for filtering\
            operations that require it.
        input_: the input: either a fixel data file, or a fixel directory (see\
            Description).
        filter_: the filtering operation to perform; options are: connect,\
            smooth.
        output: the output: either a fixel data file, or a fixel directory (see\
            Description).
        threshold_value: specify a threshold for the input fixel data file\
            values (default = 0.5).
        threshold_connectivity: specify a fixel-fixel connectivity threshold\
            for connected-component analysis (default = 0.10000000000000001).
        fwhm: the full-width half-maximum (FWHM) of the spatial component of\
            the smoothing filter (default = 10mm).
        minweight: apply a minimum threshold to smoothing weights (default =\
            0.01).
        mask: only perform smoothing within a specified binary fixel mask.
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
        NamedTuple of outputs (described in `FixelfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELFILTER_METADATA)
    params = fixelfilter_params(matrix=matrix, threshold_value=threshold_value, threshold_connectivity=threshold_connectivity, fwhm=fwhm, minweight=minweight, mask=mask, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, filter_=filter_, output=output)
    return fixelfilter_execute(params, execution)


__all__ = [
    "FIXELFILTER_METADATA",
    "FixelfilterOutputs",
    "fixelfilter",
    "fixelfilter_config_params",
    "fixelfilter_params",
    "fixelfilter_various_file_params",
    "fixelfilter_various_file_params_",
    "fixelfilter_various_string_params",
    "fixelfilter_various_string_params_",
]
