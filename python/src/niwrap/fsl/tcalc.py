# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCALC_METADATA = Metadata(
    id="f811e9be21119eee4df1778a355c771fb0361c10.boutiques",
    name="tcalc",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
TcalcParameters = typing.TypedDict('TcalcParameters', {
    "__STYX_TYPE__": typing.Literal["tcalc"],
    "input_image": InputPathType,
    "output_image": str,
    "echo_time": typing.NotRequired[float | None],
    "repetition_time": typing.NotRequired[float | None],
    "mrpar_file": typing.NotRequired[InputPathType | None],
    "num_voxel_x": typing.NotRequired[float | None],
    "num_voxel_y": typing.NotRequired[float | None],
    "num_voxel_z": typing.NotRequired[float | None],
    "voxel_size_x": typing.NotRequired[float | None],
    "voxel_size_y": typing.NotRequired[float | None],
    "voxel_size_z": typing.NotRequired[float | None],
    "start_position": typing.NotRequired[float | None],
    "noise_sigma": typing.NotRequired[float | None],
    "save_flag": bool,
    "verbose_flag": bool,
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
        "tcalc": tcalc_cargs,
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
        "tcalc": tcalc_outputs,
    }
    return vt.get(t)


class TcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """The output image generated after resampling"""
    original_output_image_file: OutputPathType
    """The original non-resampled output image, if save flag is used"""


def tcalc_params(
    input_image: InputPathType,
    output_image: str,
    echo_time: float | None = None,
    repetition_time: float | None = None,
    mrpar_file: InputPathType | None = None,
    num_voxel_x: float | None = None,
    num_voxel_y: float | None = None,
    num_voxel_z: float | None = None,
    voxel_size_x: float | None = None,
    voxel_size_y: float | None = None,
    voxel_size_z: float | None = None,
    start_position: float | None = None,
    noise_sigma: float | None = None,
    save_flag: bool = False,
    verbose_flag: bool = False,
) -> TcalcParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image (4D phantom for theoretical calculations).
        output_image: Output image.
        echo_time: Echo Time (TE) in seconds [e.g., T1-weighted images for 3T\
            TE=0.01 s].
        repetition_time: Repetition Time (TR) in seconds [e.g., T1-weighted\
            images for 3T TR=0.7 s].
        mrpar_file: MRpar File.
        num_voxel_x: Number of Voxels along X (default: phantom).
        num_voxel_y: Number of Voxels along Y (default: phantom).
        num_voxel_z: Number of Voxels along Z (default: phantom).
        voxel_size_x: Size of voxels along X (default: phantom).
        voxel_size_y: Size of voxels along Y (default: phantom).
        voxel_size_z: Size of voxels along Z i.e., number of slices (default:\
            phantom).
        start_position: Starting position of the volume in mm (default = 0mm).
        noise_sigma: Add noise with given sigma (default: 0 i.e., no noise).
        save_flag: Save original non-resample output image.
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tcalc",
        "input_image": input_image,
        "output_image": output_image,
        "save_flag": save_flag,
        "verbose_flag": verbose_flag,
    }
    if echo_time is not None:
        params["echo_time"] = echo_time
    if repetition_time is not None:
        params["repetition_time"] = repetition_time
    if mrpar_file is not None:
        params["mrpar_file"] = mrpar_file
    if num_voxel_x is not None:
        params["num_voxel_x"] = num_voxel_x
    if num_voxel_y is not None:
        params["num_voxel_y"] = num_voxel_y
    if num_voxel_z is not None:
        params["num_voxel_z"] = num_voxel_z
    if voxel_size_x is not None:
        params["voxel_size_x"] = voxel_size_x
    if voxel_size_y is not None:
        params["voxel_size_y"] = voxel_size_y
    if voxel_size_z is not None:
        params["voxel_size_z"] = voxel_size_z
    if start_position is not None:
        params["start_position"] = start_position
    if noise_sigma is not None:
        params["noise_sigma"] = noise_sigma
    return params


def tcalc_cargs(
    params: TcalcParameters,
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
    cargs.append("tcalc")
    cargs.append("-i")
    cargs.extend([
        "--input",
        execution.input_file(params.get("input_image"))
    ])
    cargs.append("-o")
    cargs.extend([
        "--output",
        params.get("output_image")
    ])
    if params.get("echo_time") is not None:
        cargs.extend([
            "--te",
            str(params.get("echo_time"))
        ])
    if params.get("repetition_time") is not None:
        cargs.extend([
            "--tr",
            str(params.get("repetition_time"))
        ])
    if params.get("mrpar_file") is not None:
        cargs.extend([
            "--mrpar",
            execution.input_file(params.get("mrpar_file"))
        ])
    if params.get("num_voxel_x") is not None:
        cargs.extend([
            "--nx",
            str(params.get("num_voxel_x"))
        ])
    if params.get("num_voxel_y") is not None:
        cargs.extend([
            "--ny",
            str(params.get("num_voxel_y"))
        ])
    if params.get("num_voxel_z") is not None:
        cargs.extend([
            "--nz",
            str(params.get("num_voxel_z"))
        ])
    if params.get("voxel_size_x") is not None:
        cargs.extend([
            "--dx",
            str(params.get("voxel_size_x"))
        ])
    if params.get("voxel_size_y") is not None:
        cargs.extend([
            "--dy",
            str(params.get("voxel_size_y"))
        ])
    if params.get("voxel_size_z") is not None:
        cargs.extend([
            "--dz",
            str(params.get("voxel_size_z"))
        ])
    if params.get("start_position") is not None:
        cargs.extend([
            "--zstart",
            str(params.get("start_position"))
        ])
    if params.get("noise_sigma") is not None:
        cargs.extend([
            "--sigma",
            str(params.get("noise_sigma"))
        ])
    if params.get("save_flag"):
        cargs.append("--save")
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    return cargs


def tcalc_outputs(
    params: TcalcParameters,
    execution: Execution,
) -> TcalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TcalcOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")),
        original_output_image_file=execution.output_file(params.get("output_image") + "_original"),
    )
    return ret


def tcalc_execute(
    params: TcalcParameters,
    execution: Execution,
) -> TcalcOutputs:
    """
    Resample a 4D phantom for theoretical calculations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TcalcOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tcalc_cargs(params, execution)
    ret = tcalc_outputs(params, execution)
    execution.run(cargs)
    return ret


def tcalc(
    input_image: InputPathType,
    output_image: str,
    echo_time: float | None = None,
    repetition_time: float | None = None,
    mrpar_file: InputPathType | None = None,
    num_voxel_x: float | None = None,
    num_voxel_y: float | None = None,
    num_voxel_z: float | None = None,
    voxel_size_x: float | None = None,
    voxel_size_y: float | None = None,
    voxel_size_z: float | None = None,
    start_position: float | None = None,
    noise_sigma: float | None = None,
    save_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> TcalcOutputs:
    """
    Resample a 4D phantom for theoretical calculations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input image (4D phantom for theoretical calculations).
        output_image: Output image.
        echo_time: Echo Time (TE) in seconds [e.g., T1-weighted images for 3T\
            TE=0.01 s].
        repetition_time: Repetition Time (TR) in seconds [e.g., T1-weighted\
            images for 3T TR=0.7 s].
        mrpar_file: MRpar File.
        num_voxel_x: Number of Voxels along X (default: phantom).
        num_voxel_y: Number of Voxels along Y (default: phantom).
        num_voxel_z: Number of Voxels along Z (default: phantom).
        voxel_size_x: Size of voxels along X (default: phantom).
        voxel_size_y: Size of voxels along Y (default: phantom).
        voxel_size_z: Size of voxels along Z i.e., number of slices (default:\
            phantom).
        start_position: Starting position of the volume in mm (default = 0mm).
        noise_sigma: Add noise with given sigma (default: 0 i.e., no noise).
        save_flag: Save original non-resample output image.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCALC_METADATA)
    params = tcalc_params(input_image=input_image, output_image=output_image, echo_time=echo_time, repetition_time=repetition_time, mrpar_file=mrpar_file, num_voxel_x=num_voxel_x, num_voxel_y=num_voxel_y, num_voxel_z=num_voxel_z, voxel_size_x=voxel_size_x, voxel_size_y=voxel_size_y, voxel_size_z=voxel_size_z, start_position=start_position, noise_sigma=noise_sigma, save_flag=save_flag, verbose_flag=verbose_flag)
    return tcalc_execute(params, execution)


__all__ = [
    "TCALC_METADATA",
    "TcalcOutputs",
    "TcalcParameters",
    "tcalc",
    "tcalc_params",
]
