# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_REGISTER_TO_LABEL_METADATA = Metadata(
    id="36d8ca89ec62d6d129c91373f3bc303868500379.boutiques",
    name="mris_register_to_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisRegisterToLabelParameters = typing.TypedDict('MrisRegisterToLabelParameters', {
    "__STYX_TYPE__": typing.Literal["mris_register_to_label"],
    "surface": InputPathType,
    "regfile": InputPathType,
    "mri_reg": InputPathType,
    "mov_volume": InputPathType,
    "resolution": float,
    "max_rot": typing.NotRequired[float | None],
    "max_trans": typing.NotRequired[float | None],
    "subject": typing.NotRequired[str | None],
    "label": typing.NotRequired[str | None],
    "out_reg": typing.NotRequired[str | None],
    "downsample": typing.NotRequired[float | None],
    "cost_file": typing.NotRequired[InputPathType | None],
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
        "mris_register_to_label": mris_register_to_label_cargs,
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


class MrisRegisterToLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_register_to_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_register_to_label_params(
    surface: InputPathType,
    regfile: InputPathType,
    mri_reg: InputPathType,
    mov_volume: InputPathType,
    resolution: float,
    max_rot: float | None = None,
    max_trans: float | None = None,
    subject: str | None = None,
    label: str | None = None,
    out_reg: str | None = None,
    downsample: float | None = None,
    cost_file: InputPathType | None = None,
) -> MrisRegisterToLabelParameters:
    """
    Build parameters.
    
    Args:
        surface: Surface file for registration.
        regfile: Registration file.
        mri_reg: Volume for MRI registration.
        mov_volume: Volume on which label points are specified.
        resolution: Resolution for calculations.
        max_rot: Maximum angle (degrees) to search over for rotation.
        max_trans: Maximum translation (mm) to search over.
        subject: Specify name of subject for register.dat file.
        label: Load label and limit calculations to it.
        out_reg: Output registration at lowest cost.
        downsample: Downsample input volume by a factor.
        cost_file: Cost file for registration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_register_to_label",
        "surface": surface,
        "regfile": regfile,
        "mri_reg": mri_reg,
        "mov_volume": mov_volume,
        "resolution": resolution,
    }
    if max_rot is not None:
        params["max_rot"] = max_rot
    if max_trans is not None:
        params["max_trans"] = max_trans
    if subject is not None:
        params["subject"] = subject
    if label is not None:
        params["label"] = label
    if out_reg is not None:
        params["out_reg"] = out_reg
    if downsample is not None:
        params["downsample"] = downsample
    if cost_file is not None:
        params["cost_file"] = cost_file
    return params


def mris_register_to_label_cargs(
    params: MrisRegisterToLabelParameters,
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
    cargs.append("mris_register_to_label")
    cargs.extend([
        "--surf",
        execution.input_file(params.get("surface"))
    ])
    cargs.extend([
        "--reg",
        execution.input_file(params.get("regfile"))
    ])
    cargs.extend([
        "--mri_reg",
        execution.input_file(params.get("mri_reg"))
    ])
    cargs.extend([
        "--mov",
        execution.input_file(params.get("mov_volume"))
    ])
    cargs.extend([
        "--res",
        str(params.get("resolution"))
    ])
    if params.get("max_rot") is not None:
        cargs.extend([
            "--max_rot",
            str(params.get("max_rot"))
        ])
    if params.get("max_trans") is not None:
        cargs.extend([
            "--max_trans",
            str(params.get("max_trans"))
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    if params.get("label") is not None:
        cargs.extend([
            "--label",
            params.get("label")
        ])
    if params.get("out_reg") is not None:
        cargs.extend([
            "--out-reg",
            params.get("out_reg")
        ])
    if params.get("downsample") is not None:
        cargs.extend([
            "--downsample",
            str(params.get("downsample"))
        ])
    if params.get("cost_file") is not None:
        cargs.extend([
            "--cost",
            execution.input_file(params.get("cost_file"))
        ])
    return cargs


def mris_register_to_label_outputs(
    params: MrisRegisterToLabelParameters,
    execution: Execution,
) -> MrisRegisterToLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRegisterToLabelOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_register_to_label_execute(
    params: MrisRegisterToLabelParameters,
    execution: Execution,
) -> MrisRegisterToLabelOutputs:
    """
    Register a surface to a volume using a label.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRegisterToLabelOutputs`).
    """
    cargs = mris_register_to_label_cargs(params, execution)
    ret = mris_register_to_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_register_to_label(
    surface: InputPathType,
    regfile: InputPathType,
    mri_reg: InputPathType,
    mov_volume: InputPathType,
    resolution: float,
    max_rot: float | None = None,
    max_trans: float | None = None,
    subject: str | None = None,
    label: str | None = None,
    out_reg: str | None = None,
    downsample: float | None = None,
    cost_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> MrisRegisterToLabelOutputs:
    """
    Register a surface to a volume using a label.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Surface file for registration.
        regfile: Registration file.
        mri_reg: Volume for MRI registration.
        mov_volume: Volume on which label points are specified.
        resolution: Resolution for calculations.
        max_rot: Maximum angle (degrees) to search over for rotation.
        max_trans: Maximum translation (mm) to search over.
        subject: Specify name of subject for register.dat file.
        label: Load label and limit calculations to it.
        out_reg: Output registration at lowest cost.
        downsample: Downsample input volume by a factor.
        cost_file: Cost file for registration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRegisterToLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REGISTER_TO_LABEL_METADATA)
    params = mris_register_to_label_params(surface=surface, regfile=regfile, mri_reg=mri_reg, mov_volume=mov_volume, resolution=resolution, max_rot=max_rot, max_trans=max_trans, subject=subject, label=label, out_reg=out_reg, downsample=downsample, cost_file=cost_file)
    return mris_register_to_label_execute(params, execution)


__all__ = [
    "MRIS_REGISTER_TO_LABEL_METADATA",
    "MrisRegisterToLabelOutputs",
    "MrisRegisterToLabelParameters",
    "mris_register_to_label",
    "mris_register_to_label_params",
]
