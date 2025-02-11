# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__DJUNCT_4D_IMAGER_METADATA = Metadata(
    id="3dd204eaacbae468c095a2b5730ff8d05c57b1e8.boutiques",
    name="@djunct_4d_imager",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDjunct4dImagerParameters = typing.TypedDict('VDjunct4dImagerParameters', {
    "__STYX_TYPE__": typing.Literal["@djunct_4d_imager"],
    "inset": InputPathType,
    "prefix": str,
    "do_movie": typing.NotRequired[typing.Literal["MPEG", "AGIF"] | None],
    "no_clean": bool,
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
        "@djunct_4d_imager": v__djunct_4d_imager_cargs,
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
        "@djunct_4d_imager": v__djunct_4d_imager_outputs,
    }.get(t)


class VDjunct4dImagerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_4d_imager(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    onescl_png: OutputPathType
    """Output montage image with constant brightness range"""
    sepscl_png: OutputPathType
    """Output montage image with varying brightness range"""
    onescl_mpeg: OutputPathType
    """Output movie with constant brightness range (one slice at a time)"""
    sepscl_mpeg: OutputPathType
    """Output movie with varying brightness range (one slice at a time)"""
    onescl_gif: OutputPathType
    """Output animated GIF with constant brightness range (one slice at a
    time)"""
    sepscl_gif: OutputPathType
    """Output animated GIF with varying brightness range (one slice at a
    time)"""


def v__djunct_4d_imager_params(
    inset: InputPathType,
    prefix: str,
    do_movie: typing.Literal["MPEG", "AGIF"] | None = None,
    no_clean: bool = False,
) -> VDjunct4dImagerParameters:
    """
    Build parameters.
    
    Args:
        inset: ULay dataset, probably 4D (required).
        prefix: Prefix for output files (required).
        do_movie: Specify type of movie file. Options: MPEG, AGIF.
        no_clean: Keep the final intermediate files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@djunct_4d_imager",
        "inset": inset,
        "prefix": prefix,
        "no_clean": no_clean,
    }
    if do_movie is not None:
        params["do_movie"] = do_movie
    return params


def v__djunct_4d_imager_cargs(
    params: VDjunct4dImagerParameters,
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
    cargs.append("@djunct_4d_imager")
    cargs.append(execution.input_file(params.get("inset")))
    cargs.append(params.get("prefix"))
    if params.get("do_movie") is not None:
        cargs.extend([
            "-do_movie",
            params.get("do_movie")
        ])
    if params.get("no_clean"):
        cargs.append("-no_clean")
    return cargs


def v__djunct_4d_imager_outputs(
    params: VDjunct4dImagerParameters,
    execution: Execution,
) -> VDjunct4dImagerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDjunct4dImagerOutputs(
        root=execution.output_file("."),
        onescl_png=execution.output_file(params.get("prefix") + "_onescl.png"),
        sepscl_png=execution.output_file(params.get("prefix") + "_sepscl.png"),
        onescl_mpeg=execution.output_file(params.get("prefix") + "_onescl.mpg"),
        sepscl_mpeg=execution.output_file(params.get("prefix") + "_sepscl.mpg"),
        onescl_gif=execution.output_file(params.get("prefix") + "_onescl.gif"),
        sepscl_gif=execution.output_file(params.get("prefix") + "_sepscl.gif"),
    )
    return ret


def v__djunct_4d_imager_execute(
    params: VDjunct4dImagerParameters,
    execution: Execution,
) -> VDjunct4dImagerOutputs:
    """
    The program is useful for viewing the same slice across the 'time' dimension of
    a 4D data set.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDjunct4dImagerOutputs`).
    """
    cargs = v__djunct_4d_imager_cargs(params, execution)
    ret = v__djunct_4d_imager_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__djunct_4d_imager(
    inset: InputPathType,
    prefix: str,
    do_movie: typing.Literal["MPEG", "AGIF"] | None = None,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> VDjunct4dImagerOutputs:
    """
    The program is useful for viewing the same slice across the 'time' dimension of
    a 4D data set.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inset: ULay dataset, probably 4D (required).
        prefix: Prefix for output files (required).
        do_movie: Specify type of movie file. Options: MPEG, AGIF.
        no_clean: Keep the final intermediate files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunct4dImagerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_4D_IMAGER_METADATA)
    params = v__djunct_4d_imager_params(inset=inset, prefix=prefix, do_movie=do_movie, no_clean=no_clean)
    return v__djunct_4d_imager_execute(params, execution)


__all__ = [
    "VDjunct4dImagerOutputs",
    "VDjunct4dImagerParameters",
    "V__DJUNCT_4D_IMAGER_METADATA",
    "v__djunct_4d_imager",
    "v__djunct_4d_imager_params",
]
