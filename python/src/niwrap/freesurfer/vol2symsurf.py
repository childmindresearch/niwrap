# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOL2SYMSURF_METADATA = Metadata(
    id="22e164f84127031ad07cd425f37456f6e49f209f.boutiques",
    name="vol2symsurf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Vol2symsurfParameters = typing.TypedDict('Vol2symsurfParameters', {
    "__STYX_TYPE__": typing.Literal["vol2symsurf"],
    "registration_file": InputPathType,
    "input_volume": InputPathType,
    "fwhm": float,
    "output_stem": typing.NotRequired[str | None],
    "regheader": typing.NotRequired[str | None],
    "projection_fraction": typing.NotRequired[float | None],
    "no_diff": bool,
    "laterality_index": bool,
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
        "vol2symsurf": vol2symsurf_cargs,
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
        "vol2symsurf": vol2symsurf_outputs,
    }
    return vt.get(t)


class Vol2symsurfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vol2symsurf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_lh: OutputPathType | None
    """Output for left hemisphere"""
    output_rh: OutputPathType | None
    """Output for right hemisphere"""
    output_lh_rh_difference: OutputPathType | None
    """Output for left-right hemisphere difference"""
    output_li_difference: OutputPathType | None
    """Output for laterality index"""


def vol2symsurf_params(
    registration_file: InputPathType,
    input_volume: InputPathType,
    fwhm: float,
    output_stem: str | None = "instem.fsaverage_sym.smFWHM.lh.hemi",
    regheader: str | None = None,
    projection_fraction: float | None = 0.5,
    no_diff: bool = False,
    laterality_index: bool = False,
) -> Vol2symsurfParameters:
    """
    Build parameters.
    
    Args:
        registration_file: Registration file.
        input_volume: Input volume in NIfTI format.
        fwhm: Full width at half maximum for surface smoothing.
        output_stem: Output stem.
        regheader: Subject for regheader.
        projection_fraction: Projection fraction.
        no_diff: Do not compute left-right hemisphere difference.
        laterality_index: Compute laterality index instead of simple difference.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "vol2symsurf",
        "registration_file": registration_file,
        "input_volume": input_volume,
        "fwhm": fwhm,
        "no_diff": no_diff,
        "laterality_index": laterality_index,
    }
    if output_stem is not None:
        params["output_stem"] = output_stem
    if regheader is not None:
        params["regheader"] = regheader
    if projection_fraction is not None:
        params["projection_fraction"] = projection_fraction
    return params


def vol2symsurf_cargs(
    params: Vol2symsurfParameters,
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
    cargs.append("vol2symsurf")
    cargs.extend([
        "--reg",
        execution.input_file(params.get("registration_file"))
    ])
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--fwhm",
        str(params.get("fwhm"))
    ])
    if params.get("output_stem") is not None:
        cargs.extend([
            "--o",
            params.get("output_stem")
        ])
    if params.get("regheader") is not None:
        cargs.extend([
            "--regheader",
            params.get("regheader")
        ])
    if params.get("projection_fraction") is not None:
        cargs.extend([
            "--projfrac",
            str(params.get("projection_fraction"))
        ])
    if params.get("no_diff"):
        cargs.append("--no-diff")
    if params.get("laterality_index"):
        cargs.append("--li")
    return cargs


def vol2symsurf_outputs(
    params: Vol2symsurfParameters,
    execution: Execution,
) -> Vol2symsurfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Vol2symsurfOutputs(
        root=execution.output_file("."),
        output_lh=execution.output_file(params.get("output_stem") + ".lh.nii") if (params.get("output_stem") is not None) else None,
        output_rh=execution.output_file(params.get("output_stem") + ".rh.nii") if (params.get("output_stem") is not None) else None,
        output_lh_rh_difference=execution.output_file(params.get("output_stem") + ".lh-rh.nii") if (params.get("output_stem") is not None) else None,
        output_li_difference=execution.output_file(params.get("output_stem") + ".li.lh-rh.nii") if (params.get("output_stem") is not None) else None,
    )
    return ret


def vol2symsurf_execute(
    params: Vol2symsurfParameters,
    execution: Execution,
) -> Vol2symsurfOutputs:
    """
    A tool that samples a volume onto the surface of the left-right symmetric
    subject (fsaverage_sym).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Vol2symsurfOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = vol2symsurf_cargs(params, execution)
    ret = vol2symsurf_outputs(params, execution)
    execution.run(cargs)
    return ret


def vol2symsurf(
    registration_file: InputPathType,
    input_volume: InputPathType,
    fwhm: float,
    output_stem: str | None = "instem.fsaverage_sym.smFWHM.lh.hemi",
    regheader: str | None = None,
    projection_fraction: float | None = 0.5,
    no_diff: bool = False,
    laterality_index: bool = False,
    runner: Runner | None = None,
) -> Vol2symsurfOutputs:
    """
    A tool that samples a volume onto the surface of the left-right symmetric
    subject (fsaverage_sym).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        registration_file: Registration file.
        input_volume: Input volume in NIfTI format.
        fwhm: Full width at half maximum for surface smoothing.
        output_stem: Output stem.
        regheader: Subject for regheader.
        projection_fraction: Projection fraction.
        no_diff: Do not compute left-right hemisphere difference.
        laterality_index: Compute laterality index instead of simple difference.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Vol2symsurfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOL2SYMSURF_METADATA)
    params = vol2symsurf_params(registration_file=registration_file, input_volume=input_volume, fwhm=fwhm, output_stem=output_stem, regheader=regheader, projection_fraction=projection_fraction, no_diff=no_diff, laterality_index=laterality_index)
    return vol2symsurf_execute(params, execution)


__all__ = [
    "VOL2SYMSURF_METADATA",
    "Vol2symsurfOutputs",
    "Vol2symsurfParameters",
    "vol2symsurf",
    "vol2symsurf_params",
]
