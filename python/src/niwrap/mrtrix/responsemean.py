# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RESPONSEMEAN_METADATA = Metadata(
    id="e6c56f5745cf6a8cbb9c9387ca97dbcce3e44b95.boutiques",
    name="responsemean",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
ResponsemeanParameters = typing.TypedDict('ResponsemeanParameters', {
    "__STYX_TYPE__": typing.Literal["responsemean"],
    "input_response": list[InputPathType],
    "output_response": str,
    "legacy": bool,
    "nocleanup": bool,
    "scratch_dir": typing.NotRequired[InputPathType | None],
    "continue_scratch_dir": typing.NotRequired[list[InputPathType] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[float | None],
    "config": typing.NotRequired[list[str] | None],
    "help": bool,
    "version": bool,
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
        "responsemean": responsemean_cargs,
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
        "responsemean": responsemean_outputs,
    }.get(t)


class ResponsemeanOutputs(typing.NamedTuple):
    """
    Output object returned when calling `responsemean(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_response_file: OutputPathType
    """File containing the averaged tissue response function"""


def responsemean_params(
    input_response: list[InputPathType],
    output_response: str,
    legacy: bool = False,
    nocleanup: bool = False,
    scratch_dir: InputPathType | None = None,
    continue_scratch_dir: list[InputPathType] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: float | None = None,
    config: list[str] | None = None,
    help_: bool = False,
    version: bool = False,
) -> ResponsemeanParameters:
    """
    Build parameters.
    
    Args:
        input_response: Input response functions.
        output_response: Output mean response function.
        legacy: Calculate the mean response function from a set of text files.
        nocleanup: Do not delete intermediate files during script execution,\
            and do not delete scratch directory at script completion.
        scratch_dir: Manually specify the path in which to generate the scratch\
            directory.
        continue_scratch_dir: Continue the script from a previous execution;\
            must provide the scratch directory path.
        info: Display information messages.
        quiet: Do not display information messages or progress status.
        debug: Display debugging messages.
        force: Force overwrite of output files.
        nthreads: Use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: Temporarily set the value of an MRtrix config file entry.
        help_: Display help information and exit.
        version: Display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "responsemean",
        "input_response": input_response,
        "output_response": output_response,
        "legacy": legacy,
        "nocleanup": nocleanup,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
    }
    if scratch_dir is not None:
        params["scratch_dir"] = scratch_dir
    if continue_scratch_dir is not None:
        params["continue_scratch_dir"] = continue_scratch_dir
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def responsemean_cargs(
    params: ResponsemeanParameters,
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
    cargs.append("responsemean")
    cargs.extend([execution.input_file(f) for f in params.get("input_response")])
    cargs.append(params.get("output_response"))
    if params.get("legacy"):
        cargs.append("-legacy")
    if params.get("nocleanup"):
        cargs.append("-nocleanup")
    if params.get("scratch_dir") is not None:
        cargs.extend([
            "-scratch",
            execution.input_file(params.get("scratch_dir"))
        ])
    if params.get("continue_scratch_dir") is not None:
        cargs.extend([
            "-continue",
            *[execution.input_file(f) for f in params.get("continue_scratch_dir")]
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
        cargs.extend([
            "-config",
            *params.get("config")
        ])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    return cargs


def responsemean_outputs(
    params: ResponsemeanParameters,
    execution: Execution,
) -> ResponsemeanOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ResponsemeanOutputs(
        root=execution.output_file("."),
        output_response_file=execution.output_file(params.get("output_response")),
    )
    return ret


def responsemean_execute(
    params: ResponsemeanParameters,
    execution: Execution,
) -> ResponsemeanOutputs:
    """
    Calculate the mean response function from a set of text files.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ResponsemeanOutputs`).
    """
    params = execution.params(params)
    cargs = responsemean_cargs(params, execution)
    ret = responsemean_outputs(params, execution)
    execution.run(cargs)
    return ret


def responsemean(
    input_response: list[InputPathType],
    output_response: str,
    legacy: bool = False,
    nocleanup: bool = False,
    scratch_dir: InputPathType | None = None,
    continue_scratch_dir: list[InputPathType] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: float | None = None,
    config: list[str] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> ResponsemeanOutputs:
    """
    Calculate the mean response function from a set of text files.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_response: Input response functions.
        output_response: Output mean response function.
        legacy: Calculate the mean response function from a set of text files.
        nocleanup: Do not delete intermediate files during script execution,\
            and do not delete scratch directory at script completion.
        scratch_dir: Manually specify the path in which to generate the scratch\
            directory.
        continue_scratch_dir: Continue the script from a previous execution;\
            must provide the scratch directory path.
        info: Display information messages.
        quiet: Do not display information messages or progress status.
        debug: Display debugging messages.
        force: Force overwrite of output files.
        nthreads: Use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: Temporarily set the value of an MRtrix config file entry.
        help_: Display help information and exit.
        version: Display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ResponsemeanOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RESPONSEMEAN_METADATA)
    params = responsemean_params(input_response=input_response, output_response=output_response, legacy=legacy, nocleanup=nocleanup, scratch_dir=scratch_dir, continue_scratch_dir=continue_scratch_dir, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version)
    return responsemean_execute(params, execution)


__all__ = [
    "RESPONSEMEAN_METADATA",
    "ResponsemeanOutputs",
    "ResponsemeanParameters",
    "responsemean",
    "responsemean_params",
]
