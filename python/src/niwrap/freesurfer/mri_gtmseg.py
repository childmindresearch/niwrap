# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_GTMSEG_METADATA = Metadata(
    id="2c164b92c884894655aa369148327d84b308bec1.boutiques",
    name="mri_gtmseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriGtmsegParameters = typing.TypedDict('MriGtmsegParameters', {
    "__STYX_TYPE__": typing.Literal["mri_gtmseg"],
    "output_volume": str,
    "source_subject": str,
    "internal_usf": typing.NotRequired[float | None],
    "apas_file": typing.NotRequired[InputPathType | None],
    "context_annotation": typing.NotRequired[list[str] | None],
    "subseg_wm": bool,
    "wm_annotation": typing.NotRequired[list[str] | None],
    "dmax": typing.NotRequired[float | None],
    "keep_hypo": bool,
    "keep_cc": bool,
    "ctab": typing.NotRequired[InputPathType | None],
    "lhminmax": typing.NotRequired[list[float] | None],
    "rhminmax": typing.NotRequired[list[float] | None],
    "output_usf": typing.NotRequired[float | None],
    "threads": typing.NotRequired[float | None],
    "threads_max": bool,
    "threads_max_1": bool,
    "debug": bool,
    "check_opts": bool,
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
        "mri_gtmseg": mri_gtmseg_cargs,
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


class MriGtmsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gtmseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_gtmseg_params(
    output_volume: str,
    source_subject: str,
    internal_usf: float | None = None,
    apas_file: InputPathType | None = None,
    context_annotation: list[str] | None = None,
    subseg_wm: bool = False,
    wm_annotation: list[str] | None = None,
    dmax: float | None = None,
    keep_hypo: bool = False,
    keep_cc: bool = False,
    ctab: InputPathType | None = None,
    lhminmax: list[float] | None = None,
    rhminmax: list[float] | None = None,
    output_usf: float | None = None,
    threads: float | None = None,
    threads_max: bool = False,
    threads_max_1: bool = False,
    debug: bool = False,
    check_opts: bool = False,
) -> MriGtmsegParameters:
    """
    Build parameters.
    
    Args:
        output_volume: Output volume (output will be subject/mri/outvol).
        source_subject: Source subject.
        internal_usf: Upsampling factor (default 2).
        apas_file: Defines extra-cerebral and subcortical segmentations\
            (apas+head.mgz).
        context_annotation: Use annotation to segment cortex\
            (aparc.annot,1000,2000).
        subseg_wm: Turn on segmenting of WM into smaller parts (off by default).
        wm_annotation: Use annotation to subsegment white matter.
        dmax: Distance from cortex for white matter segmentation to be\
            considered 'unsegmented' (default 5.000000).
        keep_hypo: Do not convert white matter hypointensities to a white\
            matter label.
        keep_cc: Do not convert corpus callosum to a white matter label.
        ctab: Copy items in ctab.lut into master ctab merging or overwriting\
            what is there.
        lhminmax: For defining left hemisphere ribbon in APAS (default: 1000\
            1900).
        rhminmax: For defining right hemisphere ribbon in APAS (default: 2000\
            2900).
        output_usf: Set actual output resolution. Default is to be the same as\
            the --internal-usf.
        threads: Use N threads (with Open MP).
        threads_max: Use the maximum allowable number of threads for this\
            computer.
        threads_max_1: Use one less than the maximum allowable number of\
            threads for this computer.
        debug: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_gtmseg",
        "output_volume": output_volume,
        "source_subject": source_subject,
        "subseg_wm": subseg_wm,
        "keep_hypo": keep_hypo,
        "keep_cc": keep_cc,
        "threads_max": threads_max,
        "threads_max_1": threads_max_1,
        "debug": debug,
        "check_opts": check_opts,
    }
    if internal_usf is not None:
        params["internal_usf"] = internal_usf
    if apas_file is not None:
        params["apas_file"] = apas_file
    if context_annotation is not None:
        params["context_annotation"] = context_annotation
    if wm_annotation is not None:
        params["wm_annotation"] = wm_annotation
    if dmax is not None:
        params["dmax"] = dmax
    if ctab is not None:
        params["ctab"] = ctab
    if lhminmax is not None:
        params["lhminmax"] = lhminmax
    if rhminmax is not None:
        params["rhminmax"] = rhminmax
    if output_usf is not None:
        params["output_usf"] = output_usf
    if threads is not None:
        params["threads"] = threads
    return params


def mri_gtmseg_cargs(
    params: MriGtmsegParameters,
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
    cargs.append("mri_gtmseg")
    cargs.extend([
        "--o",
        params.get("output_volume")
    ])
    cargs.extend([
        "--s",
        params.get("source_subject")
    ])
    if params.get("internal_usf") is not None:
        cargs.extend([
            "--internal-usf",
            str(params.get("internal_usf"))
        ])
    if params.get("apas_file") is not None:
        cargs.extend([
            "--apas",
            execution.input_file(params.get("apas_file"))
        ])
    if params.get("context_annotation") is not None:
        cargs.extend([
            "--ctx-annot",
            *params.get("context_annotation")
        ])
    if params.get("subseg_wm"):
        cargs.append("--subseg-wm")
    if params.get("wm_annotation") is not None:
        cargs.extend([
            "--wm-annot",
            *params.get("wm_annotation")
        ])
    if params.get("dmax") is not None:
        cargs.extend([
            "--dmax",
            str(params.get("dmax"))
        ])
    if params.get("keep_hypo"):
        cargs.append("--keep-hypo")
    if params.get("keep_cc"):
        cargs.append("--keep-cc")
    if params.get("ctab") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("ctab"))
        ])
    if params.get("lhminmax") is not None:
        cargs.extend([
            "--lhminmax",
            *map(str, params.get("lhminmax"))
        ])
    if params.get("rhminmax") is not None:
        cargs.extend([
            "--rhminmax",
            *map(str, params.get("rhminmax"))
        ])
    if params.get("output_usf") is not None:
        cargs.extend([
            "--output-usf",
            str(params.get("output_usf"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("threads_max"):
        cargs.append("--threads-max")
    if params.get("threads_max_1"):
        cargs.append("--threads-max-1")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("check_opts"):
        cargs.append("--checkopts")
    return cargs


def mri_gtmseg_outputs(
    params: MriGtmsegParameters,
    execution: Execution,
) -> MriGtmsegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriGtmsegOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_gtmseg_execute(
    params: MriGtmsegParameters,
    execution: Execution,
) -> MriGtmsegOutputs:
    """
    Creates a segmentation that can be used with the geometric transfer matrix
    (GTM).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriGtmsegOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_gtmseg_cargs(params, execution)
    ret = mri_gtmseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_gtmseg(
    output_volume: str,
    source_subject: str,
    internal_usf: float | None = None,
    apas_file: InputPathType | None = None,
    context_annotation: list[str] | None = None,
    subseg_wm: bool = False,
    wm_annotation: list[str] | None = None,
    dmax: float | None = None,
    keep_hypo: bool = False,
    keep_cc: bool = False,
    ctab: InputPathType | None = None,
    lhminmax: list[float] | None = None,
    rhminmax: list[float] | None = None,
    output_usf: float | None = None,
    threads: float | None = None,
    threads_max: bool = False,
    threads_max_1: bool = False,
    debug: bool = False,
    check_opts: bool = False,
    runner: Runner | None = None,
) -> MriGtmsegOutputs:
    """
    Creates a segmentation that can be used with the geometric transfer matrix
    (GTM).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_volume: Output volume (output will be subject/mri/outvol).
        source_subject: Source subject.
        internal_usf: Upsampling factor (default 2).
        apas_file: Defines extra-cerebral and subcortical segmentations\
            (apas+head.mgz).
        context_annotation: Use annotation to segment cortex\
            (aparc.annot,1000,2000).
        subseg_wm: Turn on segmenting of WM into smaller parts (off by default).
        wm_annotation: Use annotation to subsegment white matter.
        dmax: Distance from cortex for white matter segmentation to be\
            considered 'unsegmented' (default 5.000000).
        keep_hypo: Do not convert white matter hypointensities to a white\
            matter label.
        keep_cc: Do not convert corpus callosum to a white matter label.
        ctab: Copy items in ctab.lut into master ctab merging or overwriting\
            what is there.
        lhminmax: For defining left hemisphere ribbon in APAS (default: 1000\
            1900).
        rhminmax: For defining right hemisphere ribbon in APAS (default: 2000\
            2900).
        output_usf: Set actual output resolution. Default is to be the same as\
            the --internal-usf.
        threads: Use N threads (with Open MP).
        threads_max: Use the maximum allowable number of threads for this\
            computer.
        threads_max_1: Use one less than the maximum allowable number of\
            threads for this computer.
        debug: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGtmsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GTMSEG_METADATA)
    params = mri_gtmseg_params(output_volume=output_volume, source_subject=source_subject, internal_usf=internal_usf, apas_file=apas_file, context_annotation=context_annotation, subseg_wm=subseg_wm, wm_annotation=wm_annotation, dmax=dmax, keep_hypo=keep_hypo, keep_cc=keep_cc, ctab=ctab, lhminmax=lhminmax, rhminmax=rhminmax, output_usf=output_usf, threads=threads, threads_max=threads_max, threads_max_1=threads_max_1, debug=debug, check_opts=check_opts)
    return mri_gtmseg_execute(params, execution)


__all__ = [
    "MRI_GTMSEG_METADATA",
    "MriGtmsegOutputs",
    "mri_gtmseg",
    "mri_gtmseg_params",
]
