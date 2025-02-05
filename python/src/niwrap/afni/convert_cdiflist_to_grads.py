# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_CDIFLIST_TO_GRADS_METADATA = Metadata(
    id="881be0d2d254f2047a6c704bea01fe398f0290f3.boutiques",
    name="convert_cdiflist_to_grads",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ConvertCdiflistToGradsParameters = typing.TypedDict('ConvertCdiflistToGradsParameters', {
    "__STYX_TYPE__": typing.Literal["convert_cdiflist_to_grads"],
    "cdiflist": InputPathType,
    "bval_max": float,
    "prefix": str,
    "ver": bool,
    "date": bool,
    "help": bool,
    "hview": bool,
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
        "convert_cdiflist_to_grads": convert_cdiflist_to_grads_cargs,
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
        "convert_cdiflist_to_grads": convert_cdiflist_to_grads_outputs,
    }
    return vt.get(t)


class ConvertCdiflistToGradsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_cdiflist_to_grads(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_rvec: OutputPathType
    """Row-format of gradients (unit magnitude)."""
    output_bval: OutputPathType
    """Row-format of bvals."""
    output_cvec: OutputPathType
    """Col-format of gradients (scaled by b-values)."""


def convert_cdiflist_to_grads_params(
    cdiflist: InputPathType,
    bval_max: float,
    prefix: str,
    ver: bool = False,
    date: bool = False,
    help_: bool = False,
    hview: bool = False,
) -> ConvertCdiflistToGradsParameters:
    """
    Build parameters.
    
    Args:
        cdiflist: Name(s) of cdiflist text file output by GE scanners when\
            acquiring DWIs.
        bval_max: Max bvalue used, which provides a reference value for scaling\
            everything else.
        prefix: Output basename for the subsequent grad and bvalue files\
            (suffix and extensions will be added).
        ver: Display current version.
        date: Display release/editing date of current version.
        help_: Display help in terminal.
        hview: Display help in terminal.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "convert_cdiflist_to_grads",
        "cdiflist": cdiflist,
        "bval_max": bval_max,
        "prefix": prefix,
        "ver": ver,
        "date": date,
        "help": help_,
        "hview": hview,
    }
    return params


def convert_cdiflist_to_grads_cargs(
    params: ConvertCdiflistToGradsParameters,
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
    cargs.append("convert_cdiflist_to_grads.py")
    cargs.extend([
        "-cdiflist",
        execution.input_file(params.get("cdiflist"))
    ])
    cargs.extend([
        "-bval_max",
        str(params.get("bval_max"))
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("ver"):
        cargs.append("-ver")
    if params.get("date"):
        cargs.append("-date")
    if params.get("help"):
        cargs.append("-help")
    if params.get("hview"):
        cargs.append("-h")
    return cargs


def convert_cdiflist_to_grads_outputs(
    params: ConvertCdiflistToGradsParameters,
    execution: Execution,
) -> ConvertCdiflistToGradsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertCdiflistToGradsOutputs(
        root=execution.output_file("."),
        output_rvec=execution.output_file(params.get("prefix") + "_rvec.dat"),
        output_bval=execution.output_file(params.get("prefix") + "_bval.dat"),
        output_cvec=execution.output_file(params.get("prefix") + "_cvec.dat"),
    )
    return ret


def convert_cdiflist_to_grads_execute(
    params: ConvertCdiflistToGradsParameters,
    execution: Execution,
) -> ConvertCdiflistToGradsOutputs:
    """
    This program reads in a GE cdiflist and outputs gradient file and file of
    bvalues for subsequent processing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertCdiflistToGradsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = convert_cdiflist_to_grads_cargs(params, execution)
    ret = convert_cdiflist_to_grads_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_cdiflist_to_grads(
    cdiflist: InputPathType,
    bval_max: float,
    prefix: str,
    ver: bool = False,
    date: bool = False,
    help_: bool = False,
    hview: bool = False,
    runner: Runner | None = None,
) -> ConvertCdiflistToGradsOutputs:
    """
    This program reads in a GE cdiflist and outputs gradient file and file of
    bvalues for subsequent processing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        cdiflist: Name(s) of cdiflist text file output by GE scanners when\
            acquiring DWIs.
        bval_max: Max bvalue used, which provides a reference value for scaling\
            everything else.
        prefix: Output basename for the subsequent grad and bvalue files\
            (suffix and extensions will be added).
        ver: Display current version.
        date: Display release/editing date of current version.
        help_: Display help in terminal.
        hview: Display help in terminal.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertCdiflistToGradsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_CDIFLIST_TO_GRADS_METADATA)
    params = convert_cdiflist_to_grads_params(cdiflist=cdiflist, bval_max=bval_max, prefix=prefix, ver=ver, date=date, help_=help_, hview=hview)
    return convert_cdiflist_to_grads_execute(params, execution)


__all__ = [
    "CONVERT_CDIFLIST_TO_GRADS_METADATA",
    "ConvertCdiflistToGradsOutputs",
    "ConvertCdiflistToGradsParameters",
    "convert_cdiflist_to_grads",
    "convert_cdiflist_to_grads_params",
]
