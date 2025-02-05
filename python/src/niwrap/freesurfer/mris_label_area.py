# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_LABEL_AREA_METADATA = Metadata(
    id="af4ae64d94b43274563c0c9b58c9131bb1103886.boutiques",
    name="mris_label_area",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisLabelAreaParameters = typing.TypedDict('MrisLabelAreaParameters', {
    "__STYX_TYPE__": typing.Literal["mris_label_area"],
    "pct_flag": bool,
    "log_file": typing.NotRequired[str | None],
    "brain_vol": typing.NotRequired[str | None],
    "subject_name": str,
    "hemi": str,
    "surf_name": str,
    "annot_name": str,
    "labels": list[str],
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
        "mris_label_area": mris_label_area_cargs,
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


class MrisLabelAreaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label_area(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_label_area_params(
    subject_name: str,
    hemi: str,
    surf_name: str,
    annot_name: str,
    labels: list[str],
    pct_flag: bool = False,
    log_file: str | None = None,
    brain_vol: str | None = None,
) -> MrisLabelAreaParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject.
        hemi: Hemisphere, typically 'lh' or 'rh'.
        surf_name: Surface name.
        annot_name: Annotation name.
        labels: Labels to calculate area for.
        pct_flag: Compute brain area as a percentage of all brain labels.
        log_file: Log results to file (use %d to include label number).
        brain_vol: Load brain volume and use it to normalize areas.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_label_area",
        "pct_flag": pct_flag,
        "subject_name": subject_name,
        "hemi": hemi,
        "surf_name": surf_name,
        "annot_name": annot_name,
        "labels": labels,
    }
    if log_file is not None:
        params["log_file"] = log_file
    if brain_vol is not None:
        params["brain_vol"] = brain_vol
    return params


def mris_label_area_cargs(
    params: MrisLabelAreaParameters,
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
    cargs.append("mris_label_area")
    if params.get("pct_flag"):
        cargs.append("-p")
    if params.get("log_file") is not None:
        cargs.extend([
            "-l",
            params.get("log_file")
        ])
    if params.get("brain_vol") is not None:
        cargs.extend([
            "-b",
            params.get("brain_vol")
        ])
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("surf_name"))
    cargs.append(params.get("annot_name"))
    cargs.extend(params.get("labels"))
    return cargs


def mris_label_area_outputs(
    params: MrisLabelAreaParameters,
    execution: Execution,
) -> MrisLabelAreaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisLabelAreaOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_label_area_execute(
    params: MrisLabelAreaParameters,
    execution: Execution,
) -> MrisLabelAreaOutputs:
    """
    Compute the area of specific labels on a surface of a brain hemisphere in
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisLabelAreaOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_label_area_cargs(params, execution)
    ret = mris_label_area_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_label_area(
    subject_name: str,
    hemi: str,
    surf_name: str,
    annot_name: str,
    labels: list[str],
    pct_flag: bool = False,
    log_file: str | None = None,
    brain_vol: str | None = None,
    runner: Runner | None = None,
) -> MrisLabelAreaOutputs:
    """
    Compute the area of specific labels on a surface of a brain hemisphere in
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemi: Hemisphere, typically 'lh' or 'rh'.
        surf_name: Surface name.
        annot_name: Annotation name.
        labels: Labels to calculate area for.
        pct_flag: Compute brain area as a percentage of all brain labels.
        log_file: Log results to file (use %d to include label number).
        brain_vol: Load brain volume and use it to normalize areas.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabelAreaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL_AREA_METADATA)
    params = mris_label_area_params(pct_flag=pct_flag, log_file=log_file, brain_vol=brain_vol, subject_name=subject_name, hemi=hemi, surf_name=surf_name, annot_name=annot_name, labels=labels)
    return mris_label_area_execute(params, execution)


__all__ = [
    "MRIS_LABEL_AREA_METADATA",
    "MrisLabelAreaOutputs",
    "MrisLabelAreaParameters",
    "mris_label_area",
    "mris_label_area_params",
]
