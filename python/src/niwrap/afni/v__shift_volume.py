# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SHIFT_VOLUME_METADATA = Metadata(
    id="8632323dd36a0ba5f059c998ffcd7826b058d4be.boutiques",
    name="@Shift_Volume",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VShiftVolumeParameters = typing.TypedDict('VShiftVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["@Shift_Volume"],
    "rai_shift_vector": typing.NotRequired[list[float] | None],
    "mni_anat_to_mni": bool,
    "mni_to_mni_anat": bool,
    "dset": InputPathType,
    "no_cp": bool,
    "prefix": str,
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
        "@Shift_Volume": v__shift_volume_cargs,
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
        "@Shift_Volume": v__shift_volume_outputs,
    }.get(t)


class VShiftVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__shift_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Shifted output dataset."""


def v__shift_volume_params(
    dset: InputPathType,
    prefix: str,
    rai_shift_vector: list[float] | None = None,
    mni_anat_to_mni: bool = False,
    mni_to_mni_anat: bool = False,
    no_cp: bool = False,
) -> VShiftVolumeParameters:
    """
    Build parameters.
    
    Args:
        dset: Input dataset, typically an anatomical dataset to be aligned to\
            BASE.
        prefix: Prefix for the output dataset.
        rai_shift_vector: Move dataset by dR, dA, dI mm (RAI coordinate system).
        mni_anat_to_mni: Move dataset from MNI Anatomical space to MNI space\
            (equivalent to -rai_shift 0 -4 -5).
        mni_to_mni_anat: Move dataset from MNI space to MNI Anatomical space\
            (equivalent to -rai_shift 0 4 5).
        no_cp: Do not create new data, shift the existing ones (use with\
            caution).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@Shift_Volume",
        "mni_anat_to_mni": mni_anat_to_mni,
        "mni_to_mni_anat": mni_to_mni_anat,
        "dset": dset,
        "no_cp": no_cp,
        "prefix": prefix,
    }
    if rai_shift_vector is not None:
        params["rai_shift_vector"] = rai_shift_vector
    return params


def v__shift_volume_cargs(
    params: VShiftVolumeParameters,
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
    cargs.append("@Shift_Volume")
    if params.get("rai_shift_vector") is not None:
        cargs.extend([
            "-rai_shift",
            *map(str, params.get("rai_shift_vector"))
        ])
    if params.get("mni_anat_to_mni"):
        cargs.append("-MNI_Anat_to_MNI")
    if params.get("mni_to_mni_anat"):
        cargs.append("-MNI_to_MNI_Anat")
    cargs.extend([
        "-dset",
        execution.input_file(params.get("dset"))
    ])
    if params.get("no_cp"):
        cargs.append("-no_cp")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    return cargs


def v__shift_volume_outputs(
    params: VShiftVolumeParameters,
    execution: Execution,
) -> VShiftVolumeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VShiftVolumeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".nii.gz"),
    )
    return ret


def v__shift_volume_execute(
    params: VShiftVolumeParameters,
    execution: Execution,
) -> VShiftVolumeOutputs:
    """
    Tool to shift a dataset in the RAI coordinate system or between MNI anatomical
    space and MNI space.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VShiftVolumeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__shift_volume_cargs(params, execution)
    ret = v__shift_volume_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__shift_volume(
    dset: InputPathType,
    prefix: str,
    rai_shift_vector: list[float] | None = None,
    mni_anat_to_mni: bool = False,
    mni_to_mni_anat: bool = False,
    no_cp: bool = False,
    runner: Runner | None = None,
) -> VShiftVolumeOutputs:
    """
    Tool to shift a dataset in the RAI coordinate system or between MNI anatomical
    space and MNI space.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Input dataset, typically an anatomical dataset to be aligned to\
            BASE.
        prefix: Prefix for the output dataset.
        rai_shift_vector: Move dataset by dR, dA, dI mm (RAI coordinate system).
        mni_anat_to_mni: Move dataset from MNI Anatomical space to MNI space\
            (equivalent to -rai_shift 0 -4 -5).
        mni_to_mni_anat: Move dataset from MNI space to MNI Anatomical space\
            (equivalent to -rai_shift 0 4 5).
        no_cp: Do not create new data, shift the existing ones (use with\
            caution).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VShiftVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SHIFT_VOLUME_METADATA)
    params = v__shift_volume_params(rai_shift_vector=rai_shift_vector, mni_anat_to_mni=mni_anat_to_mni, mni_to_mni_anat=mni_to_mni_anat, dset=dset, no_cp=no_cp, prefix=prefix)
    return v__shift_volume_execute(params, execution)


__all__ = [
    "VShiftVolumeOutputs",
    "VShiftVolumeParameters",
    "V__SHIFT_VOLUME_METADATA",
    "v__shift_volume",
    "v__shift_volume_params",
]
