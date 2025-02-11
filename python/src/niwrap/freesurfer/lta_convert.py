# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LTA_CONVERT_METADATA = Metadata(
    id="daaa6767af53c23e0e3f62c31924d12dbc6e0eaa.boutiques",
    name="lta_convert",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
LtaConvertParameters = typing.TypedDict('LtaConvertParameters', {
    "__STYX_TYPE__": typing.Literal["lta_convert"],
    "in_vox": typing.NotRequired[InputPathType | None],
    "out_vox": typing.NotRequired[str | None],
    "invert": bool,
    "ltavox2vox": bool,
    "ltatkreg": bool,
    "src_geometry": typing.NotRequired[InputPathType | None],
    "trg_geometry": typing.NotRequired[InputPathType | None],
    "trg_conform": bool,
    "subject_name": typing.NotRequired[str | None],
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
        "lta_convert": lta_convert_cargs,
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
        "lta_convert": lta_convert_outputs,
    }.get(t)


class LtaConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `lta_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform_file: OutputPathType | None
    """Output transformed file."""


def lta_convert_params(
    in_vox: InputPathType | None = None,
    out_vox: str | None = None,
    invert: bool = False,
    ltavox2vox: bool = False,
    ltatkreg: bool = False,
    src_geometry: InputPathType | None = None,
    trg_geometry: InputPathType | None = None,
    trg_conform: bool = False,
    subject_name: str | None = None,
) -> LtaConvertParameters:
    """
    Build parameters.
    
    Args:
        in_vox: Input transform in source image space (inverse VOX2VOX).
        out_vox: Output transform in source image space (inverse VOX2VOX).
        invert: Inverts transform.
        ltavox2vox: Output type VOX2VOX (default RAS2RAS) with --ltaout.
        ltatkreg: Output type REGISTER_DAT (default RAS2RAS) with --ltaout.
        src_geometry: Specify src image geometry (mov volume for\
            TKREG/register.dat).
        trg_geometry: Specify trg image geometry.
        trg_conform: Conform trg image geometry (COR standard).
        subject_name: Specify subject name (overrides if input has subject name\
            defined).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "lta_convert",
        "invert": invert,
        "ltavox2vox": ltavox2vox,
        "ltatkreg": ltatkreg,
        "trg_conform": trg_conform,
    }
    if in_vox is not None:
        params["in_vox"] = in_vox
    if out_vox is not None:
        params["out_vox"] = out_vox
    if src_geometry is not None:
        params["src_geometry"] = src_geometry
    if trg_geometry is not None:
        params["trg_geometry"] = trg_geometry
    if subject_name is not None:
        params["subject_name"] = subject_name
    return params


def lta_convert_cargs(
    params: LtaConvertParameters,
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
    cargs.append("lta_convert")
    if params.get("in_vox") is not None:
        cargs.extend([
            "--invox",
            execution.input_file(params.get("in_vox"))
        ])
    if params.get("out_vox") is not None:
        cargs.extend([
            "--outvox",
            params.get("out_vox")
        ])
    if params.get("invert"):
        cargs.append("--invert")
    if params.get("ltavox2vox"):
        cargs.append("--ltavox2vox")
    if params.get("ltatkreg"):
        cargs.append("--ltatkreg")
    if params.get("src_geometry") is not None:
        cargs.extend([
            "--src",
            execution.input_file(params.get("src_geometry"))
        ])
    if params.get("trg_geometry") is not None:
        cargs.extend([
            "--trg",
            execution.input_file(params.get("trg_geometry"))
        ])
    if params.get("trg_conform"):
        cargs.append("--trgconform")
    if params.get("subject_name") is not None:
        cargs.extend([
            "--subject",
            params.get("subject_name")
        ])
    return cargs


def lta_convert_outputs(
    params: LtaConvertParameters,
    execution: Execution,
) -> LtaConvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LtaConvertOutputs(
        root=execution.output_file("."),
        output_transform_file=execution.output_file(params.get("out_vox")) if (params.get("out_vox") is not None) else None,
    )
    return ret


def lta_convert_execute(
    params: LtaConvertParameters,
    execution: Execution,
) -> LtaConvertOutputs:
    """
    This program converts between different linear transform formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LtaConvertOutputs`).
    """
    cargs = lta_convert_cargs(params, execution)
    ret = lta_convert_outputs(params, execution)
    execution.run(cargs)
    return ret


def lta_convert(
    in_vox: InputPathType | None = None,
    out_vox: str | None = None,
    invert: bool = False,
    ltavox2vox: bool = False,
    ltatkreg: bool = False,
    src_geometry: InputPathType | None = None,
    trg_geometry: InputPathType | None = None,
    trg_conform: bool = False,
    subject_name: str | None = None,
    runner: Runner | None = None,
) -> LtaConvertOutputs:
    """
    This program converts between different linear transform formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        in_vox: Input transform in source image space (inverse VOX2VOX).
        out_vox: Output transform in source image space (inverse VOX2VOX).
        invert: Inverts transform.
        ltavox2vox: Output type VOX2VOX (default RAS2RAS) with --ltaout.
        ltatkreg: Output type REGISTER_DAT (default RAS2RAS) with --ltaout.
        src_geometry: Specify src image geometry (mov volume for\
            TKREG/register.dat).
        trg_geometry: Specify trg image geometry.
        trg_conform: Conform trg image geometry (COR standard).
        subject_name: Specify subject name (overrides if input has subject name\
            defined).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LtaConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LTA_CONVERT_METADATA)
    params = lta_convert_params(in_vox=in_vox, out_vox=out_vox, invert=invert, ltavox2vox=ltavox2vox, ltatkreg=ltatkreg, src_geometry=src_geometry, trg_geometry=trg_geometry, trg_conform=trg_conform, subject_name=subject_name)
    return lta_convert_execute(params, execution)


__all__ = [
    "LTA_CONVERT_METADATA",
    "LtaConvertOutputs",
    "LtaConvertParameters",
    "lta_convert",
    "lta_convert_params",
]
