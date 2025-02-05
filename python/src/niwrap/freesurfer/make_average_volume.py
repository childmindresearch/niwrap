# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_AVERAGE_VOLUME_METADATA = Metadata(
    id="52d00009c5f5db471f13423dea8699f07efa357d.boutiques",
    name="make_average_volume",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MakeAverageVolumeParameters = typing.TypedDict('MakeAverageVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["make_average_volume"],
    "subjects": list[str],
    "fsgd": typing.NotRequired[InputPathType | None],
    "out": typing.NotRequired[str | None],
    "topdir": typing.NotRequired[str | None],
    "xform": typing.NotRequired[str | None],
    "sdir": typing.NotRequired[str | None],
    "force_flag": bool,
    "keep_all_orig_flag": bool,
    "no_aseg_flag": bool,
    "ctab": typing.NotRequired[str | None],
    "ctab_default_flag": bool,
    "echo_flag": bool,
    "nocleanup_flag": bool,
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
        "make_average_volume": make_average_volume_cargs,
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


class MakeAverageVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_average_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def make_average_volume_params(
    subjects: list[str],
    fsgd: InputPathType | None = None,
    out: str | None = None,
    topdir: str | None = None,
    xform: str | None = None,
    sdir: str | None = None,
    force_flag: bool = False,
    keep_all_orig_flag: bool = False,
    no_aseg_flag: bool = False,
    ctab: str | None = None,
    ctab_default_flag: bool = False,
    echo_flag: bool = False,
    nocleanup_flag: bool = False,
) -> MakeAverageVolumeParameters:
    """
    Build parameters.
    
    Args:
        subjects: List of subjects to include in the average.
        fsgd: File containing subject list for averaging.
        out: Output average subject name. Default is 'average'.
        topdir: Directory to put data and link to SUBJECTS_DIR.
        xform: Transformation name to use, default is talairach.xfm.
        sdir: Use specified SUBJECTS_DIR instead of the environment's one.
        force_flag: Overwrite existing average subject data.
        keep_all_orig_flag: Concatenate all original volumes into\
            mri/orig.all.mgz.
        no_aseg_flag: Do not create 'average' aseg.
        ctab: Embed colortable into segmentations.
        ctab_default_flag: Embed FreeSurferColorLUT.txt into segmentations.
        echo_flag: Enable command echo for debugging.
        nocleanup_flag: Do not delete temporary files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make_average_volume",
        "subjects": subjects,
        "force_flag": force_flag,
        "keep_all_orig_flag": keep_all_orig_flag,
        "no_aseg_flag": no_aseg_flag,
        "ctab_default_flag": ctab_default_flag,
        "echo_flag": echo_flag,
        "nocleanup_flag": nocleanup_flag,
    }
    if fsgd is not None:
        params["fsgd"] = fsgd
    if out is not None:
        params["out"] = out
    if topdir is not None:
        params["topdir"] = topdir
    if xform is not None:
        params["xform"] = xform
    if sdir is not None:
        params["sdir"] = sdir
    if ctab is not None:
        params["ctab"] = ctab
    return params


def make_average_volume_cargs(
    params: MakeAverageVolumeParameters,
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
    cargs.append("make_average_volume")
    cargs.extend([
        "--subjects",
        *params.get("subjects")
    ])
    if params.get("fsgd") is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(params.get("fsgd"))
        ])
    if params.get("out") is not None:
        cargs.extend([
            "--out",
            params.get("out")
        ])
    if params.get("topdir") is not None:
        cargs.extend([
            "--topdir",
            params.get("topdir")
        ])
    if params.get("xform") is not None:
        cargs.extend([
            "--xform",
            params.get("xform")
        ])
    if params.get("sdir") is not None:
        cargs.extend([
            "--sdir",
            params.get("sdir")
        ])
    if params.get("force_flag"):
        cargs.append("--force")
    if params.get("keep_all_orig_flag"):
        cargs.append("--keep-all-orig")
    if params.get("no_aseg_flag"):
        cargs.append("--no-aseg")
    if params.get("ctab") is not None:
        cargs.extend([
            "--ctab",
            params.get("ctab")
        ])
    if params.get("ctab_default_flag"):
        cargs.append("--ctab-default")
    if params.get("echo_flag"):
        cargs.append("--echo")
    if params.get("nocleanup_flag"):
        cargs.append("--nocleanup")
    return cargs


def make_average_volume_outputs(
    params: MakeAverageVolumeParameters,
    execution: Execution,
) -> MakeAverageVolumeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeAverageVolumeOutputs(
        root=execution.output_file("."),
    )
    return ret


def make_average_volume_execute(
    params: MakeAverageVolumeParameters,
    execution: Execution,
) -> MakeAverageVolumeOutputs:
    """
    Creates average volumes from a set of subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeAverageVolumeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = make_average_volume_cargs(params, execution)
    ret = make_average_volume_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_average_volume(
    subjects: list[str],
    fsgd: InputPathType | None = None,
    out: str | None = None,
    topdir: str | None = None,
    xform: str | None = None,
    sdir: str | None = None,
    force_flag: bool = False,
    keep_all_orig_flag: bool = False,
    no_aseg_flag: bool = False,
    ctab: str | None = None,
    ctab_default_flag: bool = False,
    echo_flag: bool = False,
    nocleanup_flag: bool = False,
    runner: Runner | None = None,
) -> MakeAverageVolumeOutputs:
    """
    Creates average volumes from a set of subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subjects to include in the average.
        fsgd: File containing subject list for averaging.
        out: Output average subject name. Default is 'average'.
        topdir: Directory to put data and link to SUBJECTS_DIR.
        xform: Transformation name to use, default is talairach.xfm.
        sdir: Use specified SUBJECTS_DIR instead of the environment's one.
        force_flag: Overwrite existing average subject data.
        keep_all_orig_flag: Concatenate all original volumes into\
            mri/orig.all.mgz.
        no_aseg_flag: Do not create 'average' aseg.
        ctab: Embed colortable into segmentations.
        ctab_default_flag: Embed FreeSurferColorLUT.txt into segmentations.
        echo_flag: Enable command echo for debugging.
        nocleanup_flag: Do not delete temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeAverageVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_AVERAGE_VOLUME_METADATA)
    params = make_average_volume_params(subjects=subjects, fsgd=fsgd, out=out, topdir=topdir, xform=xform, sdir=sdir, force_flag=force_flag, keep_all_orig_flag=keep_all_orig_flag, no_aseg_flag=no_aseg_flag, ctab=ctab, ctab_default_flag=ctab_default_flag, echo_flag=echo_flag, nocleanup_flag=nocleanup_flag)
    return make_average_volume_execute(params, execution)


__all__ = [
    "MAKE_AVERAGE_VOLUME_METADATA",
    "MakeAverageVolumeOutputs",
    "MakeAverageVolumeParameters",
    "make_average_volume",
    "make_average_volume_params",
]
