# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GROUPSTATS_METADATA = Metadata(
    id="b3ed2b7c0070683b40d589d0c64dbdd96b53715f.boutiques",
    name="groupstats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
GroupstatsParameters = typing.TypedDict('GroupstatsParameters', {
    "__STYX_TYPE__": typing.Literal["groupstats"],
    "outdir": str,
    "subjectfile": typing.NotRequired[InputPathType | None],
    "fwhm": typing.NotRequired[list[float] | None],
    "subject_dir": typing.NotRequired[str | None],
    "mapname": typing.NotRequired[str | None],
    "srcsurfreg": typing.NotRequired[str | None],
    "keep53": bool,
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
        "groupstats": groupstats_cargs,
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
        "groupstats": groupstats_outputs,
    }
    return vt.get(t)


class GroupstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `groupstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated by groupstats."""


def groupstats_params(
    outdir: str,
    subjectfile: InputPathType | None = None,
    fwhm: list[float] | None = None,
    subject_dir: str | None = None,
    mapname: str | None = None,
    srcsurfreg: str | None = None,
    keep53: bool = False,
) -> GroupstatsParameters:
    """
    Build parameters.
    
    Args:
        outdir: Output folder.
        subjectfile: Subject list file.
        fwhm: Specify smoothing level(s).
        subject_dir: Subject directory.
        mapname: Use the given map name.
        srcsurfreg: Source surface registration (default is sphere.reg).
        keep53: Keep 5.3 aseg names (e.g., Thalamus-Proper).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "groupstats",
        "outdir": outdir,
        "keep53": keep53,
    }
    if subjectfile is not None:
        params["subjectfile"] = subjectfile
    if fwhm is not None:
        params["fwhm"] = fwhm
    if subject_dir is not None:
        params["subject_dir"] = subject_dir
    if mapname is not None:
        params["mapname"] = mapname
    if srcsurfreg is not None:
        params["srcsurfreg"] = srcsurfreg
    return params


def groupstats_cargs(
    params: GroupstatsParameters,
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
    cargs.append("groupstats")
    cargs.extend([
        "--o",
        params.get("outdir")
    ])
    if params.get("subjectfile") is not None:
        cargs.extend([
            "--f",
            execution.input_file(params.get("subjectfile"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            *map(str, params.get("fwhm"))
        ])
    if params.get("subject_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subject_dir")
        ])
    if params.get("mapname") is not None:
        cargs.extend([
            "--m",
            params.get("mapname")
        ])
    if params.get("srcsurfreg") is not None:
        cargs.extend([
            "--srcsurfreg",
            params.get("srcsurfreg")
        ])
    if params.get("keep53"):
        cargs.append("--keep53")
    return cargs


def groupstats_outputs(
    params: GroupstatsParameters,
    execution: Execution,
) -> GroupstatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GroupstatsOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(params.get("outdir") + "/<output_file>.ext"),
    )
    return ret


def groupstats_execute(
    params: GroupstatsParameters,
    execution: Execution,
) -> GroupstatsOutputs:
    """
    A script for comprehensive group analysis on both maps and ROI results within
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GroupstatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = groupstats_cargs(params, execution)
    ret = groupstats_outputs(params, execution)
    execution.run(cargs)
    return ret


def groupstats(
    outdir: str,
    subjectfile: InputPathType | None = None,
    fwhm: list[float] | None = None,
    subject_dir: str | None = None,
    mapname: str | None = None,
    srcsurfreg: str | None = None,
    keep53: bool = False,
    runner: Runner | None = None,
) -> GroupstatsOutputs:
    """
    A script for comprehensive group analysis on both maps and ROI results within
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        outdir: Output folder.
        subjectfile: Subject list file.
        fwhm: Specify smoothing level(s).
        subject_dir: Subject directory.
        mapname: Use the given map name.
        srcsurfreg: Source surface registration (default is sphere.reg).
        keep53: Keep 5.3 aseg names (e.g., Thalamus-Proper).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GroupstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GROUPSTATS_METADATA)
    params = groupstats_params(outdir=outdir, subjectfile=subjectfile, fwhm=fwhm, subject_dir=subject_dir, mapname=mapname, srcsurfreg=srcsurfreg, keep53=keep53)
    return groupstats_execute(params, execution)


__all__ = [
    "GROUPSTATS_METADATA",
    "GroupstatsOutputs",
    "GroupstatsParameters",
    "groupstats",
    "groupstats_params",
]
