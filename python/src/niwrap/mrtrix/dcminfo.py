# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DCMINFO_METADATA = Metadata(
    id="2f0ac96cc78649201507f26a2cd825cd37394362.boutiques",
    name="dcminfo",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
DcminfoTagParameters = typing.TypedDict('DcminfoTagParameters', {
    "__STYX_TYPE__": typing.Literal["tag"],
    "group": str,
    "element": str,
})
DcminfoConfigParameters = typing.TypedDict('DcminfoConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
DcminfoParameters = typing.TypedDict('DcminfoParameters', {
    "__STYX_TYPE__": typing.Literal["dcminfo"],
    "all": bool,
    "csa": bool,
    "phoenix": bool,
    "tag": typing.NotRequired[list[DcminfoTagParameters] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[DcminfoConfigParameters] | None],
    "help": bool,
    "version": bool,
    "file": InputPathType,
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
        "dcminfo": dcminfo_cargs,
        "tag": dcminfo_tag_cargs,
        "config": dcminfo_config_cargs,
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
    }.get(t)


def dcminfo_tag_params(
    group: str,
    element: str,
) -> DcminfoTagParameters:
    """
    Build parameters.
    
    Args:
        group: print field specified by the group & element tags supplied. Tags\
            should be supplied as Hexadecimal (i.e. as they appear in the -all\
            listing).
        element: print field specified by the group & element tags supplied.\
            Tags should be supplied as Hexadecimal (i.e. as they appear in the -all\
            listing).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tag",
        "group": group,
        "element": element,
    }
    return params


def dcminfo_tag_cargs(
    params: DcminfoTagParameters,
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
    cargs.append("-tag")
    cargs.append(params.get("group"))
    cargs.append(params.get("element"))
    return cargs


def dcminfo_config_params(
    key: str,
    value: str,
) -> DcminfoConfigParameters:
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


def dcminfo_config_cargs(
    params: DcminfoConfigParameters,
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


class DcminfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcminfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dcminfo_params(
    file: InputPathType,
    all_: bool = False,
    csa: bool = False,
    phoenix: bool = False,
    tag: list[DcminfoTagParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DcminfoConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> DcminfoParameters:
    """
    Build parameters.
    
    Args:
        file: the DICOM file to be scanned.
        all_: print all DICOM fields.
        csa: print all Siemens CSA fields (excluding Phoenix unless requested).
        phoenix: print Siemens Phoenix protocol information.
        tag: print field specified by the group & element tags supplied. Tags\
            should be supplied as Hexadecimal (i.e. as they appear in the -all\
            listing).
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
        "__STYXTYPE__": "dcminfo",
        "all": all_,
        "csa": csa,
        "phoenix": phoenix,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "file": file,
    }
    if tag is not None:
        params["tag"] = tag
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dcminfo_cargs(
    params: DcminfoParameters,
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
    cargs.append("dcminfo")
    if params.get("all"):
        cargs.append("-all")
    if params.get("csa"):
        cargs.append("-csa")
    if params.get("phoenix"):
        cargs.append("-phoenix")
    if params.get("tag") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("tag")] for a in c])
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
    cargs.append(execution.input_file(params.get("file")))
    return cargs


def dcminfo_outputs(
    params: DcminfoParameters,
    execution: Execution,
) -> DcminfoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DcminfoOutputs(
        root=execution.output_file("."),
    )
    return ret


def dcminfo_execute(
    params: DcminfoParameters,
    execution: Execution,
) -> DcminfoOutputs:
    """
    Output DICOM fields in human-readable format.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DcminfoOutputs`).
    """
    cargs = dcminfo_cargs(params, execution)
    ret = dcminfo_outputs(params, execution)
    execution.run(cargs)
    return ret


def dcminfo(
    file: InputPathType,
    all_: bool = False,
    csa: bool = False,
    phoenix: bool = False,
    tag: list[DcminfoTagParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DcminfoConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DcminfoOutputs:
    """
    Output DICOM fields in human-readable format.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        file: the DICOM file to be scanned.
        all_: print all DICOM fields.
        csa: print all Siemens CSA fields (excluding Phoenix unless requested).
        phoenix: print Siemens Phoenix protocol information.
        tag: print field specified by the group & element tags supplied. Tags\
            should be supplied as Hexadecimal (i.e. as they appear in the -all\
            listing).
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
        NamedTuple of outputs (described in `DcminfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMINFO_METADATA)
    params = dcminfo_params(all_=all_, csa=csa, phoenix=phoenix, tag=tag, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, file=file)
    return dcminfo_execute(params, execution)


__all__ = [
    "DCMINFO_METADATA",
    "DcminfoConfigParameters",
    "DcminfoOutputs",
    "DcminfoParameters",
    "DcminfoTagParameters",
    "dcminfo",
    "dcminfo_config_params",
    "dcminfo_params",
    "dcminfo_tag_params",
]
