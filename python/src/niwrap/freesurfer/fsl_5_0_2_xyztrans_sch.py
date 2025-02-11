# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_5_0_2_XYZTRANS_SCH_METADATA = Metadata(
    id="97a334fb37fbd008c00e7f8cd6895c30829fe6b3.boutiques",
    name="fsl.5.0.2.xyztrans.sch",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Fsl502XyztransSchParameters = typing.TypedDict('Fsl502XyztransSchParameters', {
    "__STYX_TYPE__": typing.Literal["fsl.5.0.2.xyztrans.sch"],
    "term_option": typing.NotRequired[str | None],
    "version_flag": bool,
    "no_scrollback_flag": bool,
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
        "fsl.5.0.2.xyztrans.sch": fsl_5_0_2_xyztrans_sch_cargs,
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


class Fsl502XyztransSchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_5_0_2_xyztrans_sch(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_5_0_2_xyztrans_sch_params(
    term_option: str | None = None,
    version_flag: bool = False,
    no_scrollback_flag: bool = False,
) -> Fsl502XyztransSchParameters:
    """
    Build parameters.
    
    Args:
        term_option: Use this instead of the $TERM environment variable.
        version_flag: Print the curses library version used.
        no_scrollback_flag: Do not try to clear the scrollback buffer.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl.5.0.2.xyztrans.sch",
        "version_flag": version_flag,
        "no_scrollback_flag": no_scrollback_flag,
    }
    if term_option is not None:
        params["term_option"] = term_option
    return params


def fsl_5_0_2_xyztrans_sch_cargs(
    params: Fsl502XyztransSchParameters,
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
    cargs.append("fsl.5.0.2.xyztrans.sch")
    if params.get("term_option") is not None:
        cargs.extend([
            "-T",
            params.get("term_option")
        ])
    if params.get("version_flag"):
        cargs.append("-V")
    if params.get("no_scrollback_flag"):
        cargs.append("-x")
    return cargs


def fsl_5_0_2_xyztrans_sch_outputs(
    params: Fsl502XyztransSchParameters,
    execution: Execution,
) -> Fsl502XyztransSchOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fsl502XyztransSchOutputs(
        root=execution.output_file("."),
    )
    return ret


def fsl_5_0_2_xyztrans_sch_execute(
    params: Fsl502XyztransSchParameters,
    execution: Execution,
) -> Fsl502XyztransSchOutputs:
    """
    A script with unclear functionality, potentially related to terminal operations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fsl502XyztransSchOutputs`).
    """
    cargs = fsl_5_0_2_xyztrans_sch_cargs(params, execution)
    ret = fsl_5_0_2_xyztrans_sch_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_5_0_2_xyztrans_sch(
    term_option: str | None = None,
    version_flag: bool = False,
    no_scrollback_flag: bool = False,
    runner: Runner | None = None,
) -> Fsl502XyztransSchOutputs:
    """
    A script with unclear functionality, potentially related to terminal operations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        term_option: Use this instead of the $TERM environment variable.
        version_flag: Print the curses library version used.
        no_scrollback_flag: Do not try to clear the scrollback buffer.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fsl502XyztransSchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_5_0_2_XYZTRANS_SCH_METADATA)
    params = fsl_5_0_2_xyztrans_sch_params(term_option=term_option, version_flag=version_flag, no_scrollback_flag=no_scrollback_flag)
    return fsl_5_0_2_xyztrans_sch_execute(params, execution)


__all__ = [
    "FSL_5_0_2_XYZTRANS_SCH_METADATA",
    "Fsl502XyztransSchOutputs",
    "Fsl502XyztransSchParameters",
    "fsl_5_0_2_xyztrans_sch",
    "fsl_5_0_2_xyztrans_sch_params",
]
