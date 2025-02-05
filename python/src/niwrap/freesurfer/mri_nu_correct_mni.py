# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_NU_CORRECT_MNI_METADATA = Metadata(
    id="4aed4300ad41fe97f4d8b814e65b6654469e83cc.boutiques",
    name="mri_nu_correct.mni",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriNuCorrectMniParameters = typing.TypedDict('MriNuCorrectMniParameters', {
    "__STYX_TYPE__": typing.Literal["mri_nu_correct.mni"],
    "input_volume": InputPathType,
    "output_volume": str,
    "iterations": float,
    "proto_iterations": typing.NotRequired[float | None],
    "mask_volume": typing.NotRequired[InputPathType | None],
    "stop_threshold": typing.NotRequired[float | None],
    "uchar_transform": typing.NotRequired[InputPathType | None],
    "ants_n3": bool,
    "ants_n4": bool,
    "no_uchar": bool,
    "ants_n4_replace_zeros": bool,
    "cm_flag": bool,
    "debug_flag": bool,
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
        "mri_nu_correct.mni": mri_nu_correct_mni_cargs,
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
        "mri_nu_correct.mni": mri_nu_correct_mni_outputs,
    }
    return vt.get(t)


class MriNuCorrectMniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_nu_correct_mni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_output: OutputPathType
    """Corrected output volume."""


def mri_nu_correct_mni_params(
    input_volume: InputPathType,
    output_volume: str,
    iterations: float,
    proto_iterations: float | None = None,
    mask_volume: InputPathType | None = None,
    stop_threshold: float | None = None,
    uchar_transform: InputPathType | None = None,
    ants_n3: bool = False,
    ants_n4: bool = False,
    no_uchar: bool = False,
    ants_n4_replace_zeros: bool = False,
    cm_flag: bool = False,
    debug_flag: bool = False,
) -> MriNuCorrectMniParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume. Can be any format accepted by mri_convert.
        output_volume: Output volume. Can be any format accepted by\
            mri_convert.
        iterations: Number of iterations to run nu_correct. Default is 4.
        proto_iterations: Passes as argument of the -iterations flag of\
            nu_correct.
        mask_volume: Brainmask volume. Can be any format accepted by\
            mri_convert.
        stop_threshold: Threshold for stopping iteration. Suggest values\
            between 0.01 to 0.0001.
        uchar_transform: Use mri_make_uchar instead of conforming.
        ants_n3: Run N3 using ANTS N3BiasFieldCorrection.
        ants_n4: Run N4 using ANTS N4BiasFieldCorrection.
        no_uchar: Do not use mri_make_uchar (default).
        ants_n4_replace_zeros: Replace 0s with small random numbers then remove\
            after nu correction.
        cm_flag: For use with data that is higher than 1mm resolution.
        debug_flag: Turn on debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_nu_correct.mni",
        "input_volume": input_volume,
        "output_volume": output_volume,
        "iterations": iterations,
        "ants_n3": ants_n3,
        "ants_n4": ants_n4,
        "no_uchar": no_uchar,
        "ants_n4_replace_zeros": ants_n4_replace_zeros,
        "cm_flag": cm_flag,
        "debug_flag": debug_flag,
    }
    if proto_iterations is not None:
        params["proto_iterations"] = proto_iterations
    if mask_volume is not None:
        params["mask_volume"] = mask_volume
    if stop_threshold is not None:
        params["stop_threshold"] = stop_threshold
    if uchar_transform is not None:
        params["uchar_transform"] = uchar_transform
    return params


def mri_nu_correct_mni_cargs(
    params: MriNuCorrectMniParameters,
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
    cargs.append("mri_nu_correct.mni")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--o",
        params.get("output_volume")
    ])
    cargs.extend([
        "--n",
        str(params.get("iterations"))
    ])
    if params.get("proto_iterations") is not None:
        cargs.extend([
            "--proto-iters",
            str(params.get("proto_iterations"))
        ])
    if params.get("mask_volume") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_volume"))
        ])
    if params.get("stop_threshold") is not None:
        cargs.extend([
            "--stop",
            str(params.get("stop_threshold"))
        ])
    if params.get("uchar_transform") is not None:
        cargs.extend([
            "--uchar",
            execution.input_file(params.get("uchar_transform"))
        ])
    if params.get("ants_n3"):
        cargs.append("--ants-n3")
    if params.get("ants_n4"):
        cargs.append("--ants-n4")
    if params.get("no_uchar"):
        cargs.append("--no-uchar")
    if params.get("ants_n4_replace_zeros"):
        cargs.append("--ants-n4-replace-zeros")
    if params.get("cm_flag"):
        cargs.append("--cm")
    if params.get("debug_flag"):
        cargs.append("--debug")
    return cargs


def mri_nu_correct_mni_outputs(
    params: MriNuCorrectMniParameters,
    execution: Execution,
) -> MriNuCorrectMniOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriNuCorrectMniOutputs(
        root=execution.output_file("."),
        corrected_output=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_nu_correct_mni_execute(
    params: MriNuCorrectMniParameters,
    execution: Execution,
) -> MriNuCorrectMniOutputs:
    """
    Wrapper for nu_correct, used for correcting intensity non-uniformity (bias
    fields).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriNuCorrectMniOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_nu_correct_mni_cargs(params, execution)
    ret = mri_nu_correct_mni_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_nu_correct_mni(
    input_volume: InputPathType,
    output_volume: str,
    iterations: float,
    proto_iterations: float | None = None,
    mask_volume: InputPathType | None = None,
    stop_threshold: float | None = None,
    uchar_transform: InputPathType | None = None,
    ants_n3: bool = False,
    ants_n4: bool = False,
    no_uchar: bool = False,
    ants_n4_replace_zeros: bool = False,
    cm_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> MriNuCorrectMniOutputs:
    """
    Wrapper for nu_correct, used for correcting intensity non-uniformity (bias
    fields).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume. Can be any format accepted by mri_convert.
        output_volume: Output volume. Can be any format accepted by\
            mri_convert.
        iterations: Number of iterations to run nu_correct. Default is 4.
        proto_iterations: Passes as argument of the -iterations flag of\
            nu_correct.
        mask_volume: Brainmask volume. Can be any format accepted by\
            mri_convert.
        stop_threshold: Threshold for stopping iteration. Suggest values\
            between 0.01 to 0.0001.
        uchar_transform: Use mri_make_uchar instead of conforming.
        ants_n3: Run N3 using ANTS N3BiasFieldCorrection.
        ants_n4: Run N4 using ANTS N4BiasFieldCorrection.
        no_uchar: Do not use mri_make_uchar (default).
        ants_n4_replace_zeros: Replace 0s with small random numbers then remove\
            after nu correction.
        cm_flag: For use with data that is higher than 1mm resolution.
        debug_flag: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriNuCorrectMniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_NU_CORRECT_MNI_METADATA)
    params = mri_nu_correct_mni_params(input_volume=input_volume, output_volume=output_volume, iterations=iterations, proto_iterations=proto_iterations, mask_volume=mask_volume, stop_threshold=stop_threshold, uchar_transform=uchar_transform, ants_n3=ants_n3, ants_n4=ants_n4, no_uchar=no_uchar, ants_n4_replace_zeros=ants_n4_replace_zeros, cm_flag=cm_flag, debug_flag=debug_flag)
    return mri_nu_correct_mni_execute(params, execution)


__all__ = [
    "MRI_NU_CORRECT_MNI_METADATA",
    "MriNuCorrectMniOutputs",
    "MriNuCorrectMniParameters",
    "mri_nu_correct_mni",
    "mri_nu_correct_mni_params",
]
