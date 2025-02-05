# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VOL2LABEL_METADATA = Metadata(
    id="f532cfda1529b1b6a60e84bccee64a9686213a07.boutiques",
    name="mri_vol2label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriVol2labelParameters = typing.TypedDict('MriVol2labelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_vol2label"],
    "input": InputPathType,
    "label_id": typing.NotRequired[float | None],
    "threshold": typing.NotRequired[float | None],
    "label_file": str,
    "vol_file": typing.NotRequired[str | None],
    "surf_subject_hemi": typing.NotRequired[str | None],
    "surf_path": typing.NotRequired[str | None],
    "opt_params": typing.NotRequired[str | None],
    "remove_holes": bool,
    "dilations": typing.NotRequired[float | None],
    "erosions": typing.NotRequired[float | None],
    "help": bool,
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
        "mri_vol2label": mri_vol2label_cargs,
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
        "mri_vol2label": mri_vol2label_outputs,
    }
    return vt.get(t)


class MriVol2labelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_vol2label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """Generated label file."""
    output_volume_file: OutputPathType | None
    """Generated label volume file."""


def mri_vol2label_params(
    input_: InputPathType,
    label_file: str,
    label_id: float | None = None,
    threshold: float | None = None,
    vol_file: str | None = None,
    surf_subject_hemi: str | None = None,
    surf_path: str | None = None,
    opt_params: str | None = None,
    remove_holes: bool = False,
    dilations: float | None = None,
    erosions: float | None = None,
    help_: bool = False,
) -> MriVol2labelParameters:
    """
    Build parameters.
    
    Args:
        input_: Input volume or surface overlay.
        label_file: Name of output label file.
        label_id: Value to match in the input.
        threshold: Threshold the input to make label (i.e., input > threshold)\
            instead of using Label ID.
        vol_file: Write label volume in this file.
        surf_subject_hemi: Interpret input as surface overlay with the given\
            subject and hemisphere (optionally with surface).
        surf_path: Specify surface path instead of subject/hemi.
        opt_params: Treats input as a probability map. Format: target delta\
            valmap.
        remove_holes: Remove holes in label and islands (with --surf only).
        dilations: Dilate label (with --surf only).
        erosions: Erode label (with --surf only).
        help_: Print out help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_vol2label",
        "input": input_,
        "label_file": label_file,
        "remove_holes": remove_holes,
        "help": help_,
    }
    if label_id is not None:
        params["label_id"] = label_id
    if threshold is not None:
        params["threshold"] = threshold
    if vol_file is not None:
        params["vol_file"] = vol_file
    if surf_subject_hemi is not None:
        params["surf_subject_hemi"] = surf_subject_hemi
    if surf_path is not None:
        params["surf_path"] = surf_path
    if opt_params is not None:
        params["opt_params"] = opt_params
    if dilations is not None:
        params["dilations"] = dilations
    if erosions is not None:
        params["erosions"] = erosions
    return params


def mri_vol2label_cargs(
    params: MriVol2labelParameters,
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
    cargs.append("mri_vol2label")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input"))
    ])
    if params.get("label_id") is not None:
        cargs.extend([
            "--id",
            str(params.get("label_id"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("threshold"))
        ])
    cargs.extend([
        "--l",
        params.get("label_file")
    ])
    if params.get("vol_file") is not None:
        cargs.extend([
            "--v",
            params.get("vol_file")
        ])
    if params.get("surf_subject_hemi") is not None:
        cargs.extend([
            "--surf",
            params.get("surf_subject_hemi")
        ])
    if params.get("surf_path") is not None:
        cargs.extend([
            "--surf-path",
            params.get("surf_path")
        ])
    if params.get("opt_params") is not None:
        cargs.extend([
            "--opt",
            params.get("opt_params")
        ])
    if params.get("remove_holes"):
        cargs.append("--remove-holes-islands")
    if params.get("dilations") is not None:
        cargs.extend([
            "--dilate",
            str(params.get("dilations"))
        ])
    if params.get("erosions") is not None:
        cargs.extend([
            "--erode",
            str(params.get("erosions"))
        ])
    if params.get("help"):
        cargs.append("--help")
    return cargs


def mri_vol2label_outputs(
    params: MriVol2labelParameters,
    execution: Execution,
) -> MriVol2labelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriVol2labelOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(params.get("label_file")),
        output_volume_file=execution.output_file(params.get("vol_file")) if (params.get("vol_file") is not None) else None,
    )
    return ret


def mri_vol2label_execute(
    params: MriVol2labelParameters,
    execution: Execution,
) -> MriVol2labelOutputs:
    """
    Converts values in a volume or surface overlay to a label using specified
    parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriVol2labelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_vol2label_cargs(params, execution)
    ret = mri_vol2label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_vol2label(
    input_: InputPathType,
    label_file: str,
    label_id: float | None = None,
    threshold: float | None = None,
    vol_file: str | None = None,
    surf_subject_hemi: str | None = None,
    surf_path: str | None = None,
    opt_params: str | None = None,
    remove_holes: bool = False,
    dilations: float | None = None,
    erosions: float | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriVol2labelOutputs:
    """
    Converts values in a volume or surface overlay to a label using specified
    parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_: Input volume or surface overlay.
        label_file: Name of output label file.
        label_id: Value to match in the input.
        threshold: Threshold the input to make label (i.e., input > threshold)\
            instead of using Label ID.
        vol_file: Write label volume in this file.
        surf_subject_hemi: Interpret input as surface overlay with the given\
            subject and hemisphere (optionally with surface).
        surf_path: Specify surface path instead of subject/hemi.
        opt_params: Treats input as a probability map. Format: target delta\
            valmap.
        remove_holes: Remove holes in label and islands (with --surf only).
        dilations: Dilate label (with --surf only).
        erosions: Erode label (with --surf only).
        help_: Print out help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVol2labelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOL2LABEL_METADATA)
    params = mri_vol2label_params(input_=input_, label_id=label_id, threshold=threshold, label_file=label_file, vol_file=vol_file, surf_subject_hemi=surf_subject_hemi, surf_path=surf_path, opt_params=opt_params, remove_holes=remove_holes, dilations=dilations, erosions=erosions, help_=help_)
    return mri_vol2label_execute(params, execution)


__all__ = [
    "MRI_VOL2LABEL_METADATA",
    "MriVol2labelOutputs",
    "MriVol2labelParameters",
    "mri_vol2label",
    "mri_vol2label_params",
]
