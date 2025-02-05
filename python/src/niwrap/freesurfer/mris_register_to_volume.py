# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_REGISTER_TO_VOLUME_METADATA = Metadata(
    id="9bdc925a77ef7d3c8dc9cd1fecb43c21110eb66b.boutiques",
    name="mris_register_to_volume",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisRegisterToVolumeParameters = typing.TypedDict('MrisRegisterToVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["mris_register_to_volume"],
    "surface": str,
    "pial": str,
    "pial_only": typing.NotRequired[str | None],
    "reg": str,
    "noglobal": bool,
    "median": bool,
    "mri_reg": str,
    "tx_mmd": typing.NotRequired[list[float] | None],
    "ty_mmd": typing.NotRequired[list[float] | None],
    "tz_mmd": typing.NotRequired[list[float] | None],
    "ax_mmd": typing.NotRequired[list[float] | None],
    "ay_mmd": typing.NotRequired[list[float] | None],
    "az_mmd": typing.NotRequired[list[float] | None],
    "cost": typing.NotRequired[str | None],
    "interp": typing.NotRequired[str | None],
    "noise": typing.NotRequired[float | None],
    "seed": typing.NotRequired[float | None],
    "skip": typing.NotRequired[list[float] | None],
    "sigma": typing.NotRequired[list[float] | None],
    "cnr": bool,
    "max_rot": typing.NotRequired[float | None],
    "max_trans": typing.NotRequired[float | None],
    "border": typing.NotRequired[float | None],
    "subject": typing.NotRequired[str | None],
    "dilate": typing.NotRequired[float | None],
    "patch": typing.NotRequired[str | None],
    "label": typing.NotRequired[str | None],
    "out_reg": typing.NotRequired[str | None],
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
        "mris_register_to_volume": mris_register_to_volume_cargs,
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
    vt = {}
    return vt.get(t)


class MrisRegisterToVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_register_to_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_register_to_volume_params(
    surface: str,
    pial: str,
    reg: str,
    mri_reg: str,
    pial_only: str | None = None,
    noglobal: bool = False,
    median: bool = False,
    tx_mmd: list[float] | None = None,
    ty_mmd: list[float] | None = None,
    tz_mmd: list[float] | None = None,
    ax_mmd: list[float] | None = None,
    ay_mmd: list[float] | None = None,
    az_mmd: list[float] | None = None,
    cost: str | None = None,
    interp: str | None = None,
    noise: float | None = None,
    seed: float | None = None,
    skip: list[float] | None = None,
    sigma: list[float] | None = None,
    cnr: bool = False,
    max_rot: float | None = None,
    max_trans: float | None = None,
    border: float | None = None,
    subject: str | None = None,
    dilate: float | None = None,
    patch: str | None = None,
    label: str | None = None,
    out_reg: str | None = None,
) -> MrisRegisterToVolumeParameters:
    """
    Build parameters.
    
    Args:
        surface: The main surface file.
        pial: Pial surface name.
        reg: Registration file.
        mri_reg: MRI volume registration file.
        pial_only: Pial surface name (only).
        noglobal: Do not use global optimization.
        median: Use median filtering.
        tx_mmd: Translation in x (min, max, delta).
        ty_mmd: Translation in y (min, max, delta).
        tz_mmd: Translation in z (min, max, delta).
        ax_mmd: Rotation about x (min, max, delta).
        ay_mmd: Rotation about y (min, max, delta).
        az_mmd: Rotation about z (min, max, delta).
        cost: Cost file.
        interp: Interpolation type: trilinear or nearest.
        noise: Add noise with stddev for testing sensitivity.
        seed: Random seed for use with noise.
        skip: Number of vertices to skip.
        sigma: Size of blurring kernels to use.
        cnr: Use CNR-based similarity function.
        max_rot: Max angle (degrees) to search over.
        max_trans: Max translation (mm) to search over.
        border: Size of the border region to ignore.
        subject: Specify name of subject (for register.dat file).
        dilate: Dilate ripflags ndil times.
        patch: Load patch and limit calculations.
        label: Load label and limit calculations.
        out_reg: Output registration at lowest cost.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_register_to_volume",
        "surface": surface,
        "pial": pial,
        "reg": reg,
        "noglobal": noglobal,
        "median": median,
        "mri_reg": mri_reg,
        "cnr": cnr,
    }
    if pial_only is not None:
        params["pial_only"] = pial_only
    if tx_mmd is not None:
        params["tx_mmd"] = tx_mmd
    if ty_mmd is not None:
        params["ty_mmd"] = ty_mmd
    if tz_mmd is not None:
        params["tz_mmd"] = tz_mmd
    if ax_mmd is not None:
        params["ax_mmd"] = ax_mmd
    if ay_mmd is not None:
        params["ay_mmd"] = ay_mmd
    if az_mmd is not None:
        params["az_mmd"] = az_mmd
    if cost is not None:
        params["cost"] = cost
    if interp is not None:
        params["interp"] = interp
    if noise is not None:
        params["noise"] = noise
    if seed is not None:
        params["seed"] = seed
    if skip is not None:
        params["skip"] = skip
    if sigma is not None:
        params["sigma"] = sigma
    if max_rot is not None:
        params["max_rot"] = max_rot
    if max_trans is not None:
        params["max_trans"] = max_trans
    if border is not None:
        params["border"] = border
    if subject is not None:
        params["subject"] = subject
    if dilate is not None:
        params["dilate"] = dilate
    if patch is not None:
        params["patch"] = patch
    if label is not None:
        params["label"] = label
    if out_reg is not None:
        params["out_reg"] = out_reg
    return params


def mris_register_to_volume_cargs(
    params: MrisRegisterToVolumeParameters,
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
    cargs.append("mris_register_to_volume")
    cargs.extend([
        "--surf",
        params.get("surface")
    ])
    cargs.extend([
        "--pial",
        params.get("pial")
    ])
    if params.get("pial_only") is not None:
        cargs.extend([
            "--pial_only",
            params.get("pial_only")
        ])
    cargs.extend([
        "--reg",
        params.get("reg")
    ])
    if params.get("noglobal"):
        cargs.append("--noglobal")
    if params.get("median"):
        cargs.append("--median")
    cargs.extend([
        "--mri_reg",
        params.get("mri_reg")
    ])
    if params.get("tx_mmd") is not None:
        cargs.extend([
            "--tx-mmd",
            *map(str, params.get("tx_mmd"))
        ])
    if params.get("ty_mmd") is not None:
        cargs.extend([
            "--ty-mmd",
            *map(str, params.get("ty_mmd"))
        ])
    if params.get("tz_mmd") is not None:
        cargs.extend([
            "--tz-mmd",
            *map(str, params.get("tz_mmd"))
        ])
    if params.get("ax_mmd") is not None:
        cargs.extend([
            "--ax-mmd",
            *map(str, params.get("ax_mmd"))
        ])
    if params.get("ay_mmd") is not None:
        cargs.extend([
            "--ay-mmd",
            *map(str, params.get("ay_mmd"))
        ])
    if params.get("az_mmd") is not None:
        cargs.extend([
            "--az-mmd",
            *map(str, params.get("az_mmd"))
        ])
    if params.get("cost") is not None:
        cargs.extend([
            "--cost",
            params.get("cost")
        ])
    if params.get("interp") is not None:
        cargs.extend([
            "--interp",
            params.get("interp")
        ])
    if params.get("noise") is not None:
        cargs.extend([
            "--noise",
            str(params.get("noise"))
        ])
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("skip") is not None:
        cargs.extend([
            "--skip",
            *map(str, params.get("skip"))
        ])
    if params.get("sigma") is not None:
        cargs.extend([
            "--sigma",
            *map(str, params.get("sigma"))
        ])
    if params.get("cnr"):
        cargs.append("--CNR")
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
    if params.get("border") is not None:
        cargs.extend([
            "--border",
            str(params.get("border"))
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    if params.get("dilate") is not None:
        cargs.extend([
            "--dilate",
            str(params.get("dilate"))
        ])
    if params.get("patch") is not None:
        cargs.extend([
            "--patch",
            params.get("patch")
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
    return cargs


def mris_register_to_volume_outputs(
    params: MrisRegisterToVolumeParameters,
    execution: Execution,
) -> MrisRegisterToVolumeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRegisterToVolumeOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_register_to_volume_execute(
    params: MrisRegisterToVolumeParameters,
    execution: Execution,
) -> MrisRegisterToVolumeOutputs:
    """
    Aligns cortical surfaces to a volumetric template.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRegisterToVolumeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_register_to_volume_cargs(params, execution)
    ret = mris_register_to_volume_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_register_to_volume(
    surface: str,
    pial: str,
    reg: str,
    mri_reg: str,
    pial_only: str | None = None,
    noglobal: bool = False,
    median: bool = False,
    tx_mmd: list[float] | None = None,
    ty_mmd: list[float] | None = None,
    tz_mmd: list[float] | None = None,
    ax_mmd: list[float] | None = None,
    ay_mmd: list[float] | None = None,
    az_mmd: list[float] | None = None,
    cost: str | None = None,
    interp: str | None = None,
    noise: float | None = None,
    seed: float | None = None,
    skip: list[float] | None = None,
    sigma: list[float] | None = None,
    cnr: bool = False,
    max_rot: float | None = None,
    max_trans: float | None = None,
    border: float | None = None,
    subject: str | None = None,
    dilate: float | None = None,
    patch: str | None = None,
    label: str | None = None,
    out_reg: str | None = None,
    runner: Runner | None = None,
) -> MrisRegisterToVolumeOutputs:
    """
    Aligns cortical surfaces to a volumetric template.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: The main surface file.
        pial: Pial surface name.
        reg: Registration file.
        mri_reg: MRI volume registration file.
        pial_only: Pial surface name (only).
        noglobal: Do not use global optimization.
        median: Use median filtering.
        tx_mmd: Translation in x (min, max, delta).
        ty_mmd: Translation in y (min, max, delta).
        tz_mmd: Translation in z (min, max, delta).
        ax_mmd: Rotation about x (min, max, delta).
        ay_mmd: Rotation about y (min, max, delta).
        az_mmd: Rotation about z (min, max, delta).
        cost: Cost file.
        interp: Interpolation type: trilinear or nearest.
        noise: Add noise with stddev for testing sensitivity.
        seed: Random seed for use with noise.
        skip: Number of vertices to skip.
        sigma: Size of blurring kernels to use.
        cnr: Use CNR-based similarity function.
        max_rot: Max angle (degrees) to search over.
        max_trans: Max translation (mm) to search over.
        border: Size of the border region to ignore.
        subject: Specify name of subject (for register.dat file).
        dilate: Dilate ripflags ndil times.
        patch: Load patch and limit calculations.
        label: Load label and limit calculations.
        out_reg: Output registration at lowest cost.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRegisterToVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REGISTER_TO_VOLUME_METADATA)
    params = mris_register_to_volume_params(surface=surface, pial=pial, pial_only=pial_only, reg=reg, noglobal=noglobal, median=median, mri_reg=mri_reg, tx_mmd=tx_mmd, ty_mmd=ty_mmd, tz_mmd=tz_mmd, ax_mmd=ax_mmd, ay_mmd=ay_mmd, az_mmd=az_mmd, cost=cost, interp=interp, noise=noise, seed=seed, skip=skip, sigma=sigma, cnr=cnr, max_rot=max_rot, max_trans=max_trans, border=border, subject=subject, dilate=dilate, patch=patch, label=label, out_reg=out_reg)
    return mris_register_to_volume_execute(params, execution)


__all__ = [
    "MRIS_REGISTER_TO_VOLUME_METADATA",
    "MrisRegisterToVolumeOutputs",
    "MrisRegisterToVolumeParameters",
    "mris_register_to_volume",
    "mris_register_to_volume_params",
]
