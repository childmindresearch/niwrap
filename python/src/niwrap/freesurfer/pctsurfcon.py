# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PCTSURFCON_METADATA = Metadata(
    id="0e082a082c6b181a71427db52d685c35d4270743.boutiques",
    name="pctsurfcon",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
PctsurfconParameters = typing.TypedDict('PctsurfconParameters', {
    "__STYX_TYPE__": typing.Literal["pctsurfcon"],
    "subject": str,
    "fsvol": typing.NotRequired[str | None],
    "outbase": typing.NotRequired[str | None],
    "lh_only": bool,
    "rh_only": bool,
    "gm_proj_frac": typing.NotRequired[float | None],
    "gm_proj_abs": typing.NotRequired[float | None],
    "wm_proj_abs": typing.NotRequired[float | None],
    "neg": bool,
    "no_mask": bool,
    "pial": bool,
    "tmp": typing.NotRequired[str | None],
    "nocleanup": bool,
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
        "pctsurfcon": pctsurfcon_cargs,
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


class PctsurfconOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pctsurfcon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def pctsurfcon_params(
    subject: str,
    fsvol: str | None = None,
    outbase: str | None = None,
    lh_only: bool = False,
    rh_only: bool = False,
    gm_proj_frac: float | None = None,
    gm_proj_abs: float | None = None,
    wm_proj_abs: float | None = None,
    neg: bool = False,
    no_mask: bool = False,
    pial: bool = False,
    tmp: str | None = None,
    nocleanup: bool = False,
) -> PctsurfconParameters:
    """
    Build parameters.
    
    Args:
        subject: FreeSurfer subject name.
        fsvol: Use fsvol instead of rawavg.
        outbase: Use outbase instead of w-g.pct (?h.w-g.pct.mgh).
        lh_only: Compute left hemisphere only.
        rh_only: Compute right hemisphere only.
        gm_proj_frac: GM projection fraction (default 0.3).
        gm_proj_abs: GM projection distance (default is to use frac).
        wm_proj_abs: WM projection distance (default is 1 mm).
        neg: Compute G-W instead of W-G.
        no_mask: Do not mask out non-cortical regions.
        pial: Use pial surface as base to compute gray/CSF contrast.
        tmp: Temporary directory (implies --nocleanup).
        nocleanup: Do not delete temporary files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pctsurfcon",
        "subject": subject,
        "lh_only": lh_only,
        "rh_only": rh_only,
        "neg": neg,
        "no_mask": no_mask,
        "pial": pial,
        "nocleanup": nocleanup,
    }
    if fsvol is not None:
        params["fsvol"] = fsvol
    if outbase is not None:
        params["outbase"] = outbase
    if gm_proj_frac is not None:
        params["gm_proj_frac"] = gm_proj_frac
    if gm_proj_abs is not None:
        params["gm_proj_abs"] = gm_proj_abs
    if wm_proj_abs is not None:
        params["wm_proj_abs"] = wm_proj_abs
    if tmp is not None:
        params["tmp"] = tmp
    return params


def pctsurfcon_cargs(
    params: PctsurfconParameters,
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
    cargs.append("pctsurfcon")
    cargs.extend([
        "-s",
        "-" + params.get("subject")
    ])
    if params.get("fsvol") is not None:
        cargs.extend([
            "--fsvol",
            params.get("fsvol")
        ])
    if params.get("outbase") is not None:
        cargs.extend([
            "--b",
            params.get("outbase")
        ])
    if params.get("lh_only"):
        cargs.append("--lh-only")
    if params.get("rh_only"):
        cargs.append("--rh-only")
    if params.get("gm_proj_frac") is not None:
        cargs.extend([
            "--gm-proj-frac",
            str(params.get("gm_proj_frac"))
        ])
    if params.get("gm_proj_abs") is not None:
        cargs.extend([
            "--gm-proj-abs",
            str(params.get("gm_proj_abs"))
        ])
    if params.get("wm_proj_abs") is not None:
        cargs.extend([
            "--wm-proj-abs",
            str(params.get("wm_proj_abs"))
        ])
    if params.get("neg"):
        cargs.append("--neg")
    if params.get("no_mask"):
        cargs.append("--no-mask")
    if params.get("pial"):
        cargs.append("--pial")
    if params.get("tmp") is not None:
        cargs.extend([
            "--tmp",
            params.get("tmp")
        ])
    if params.get("nocleanup"):
        cargs.append("--nocleanup")
    return cargs


def pctsurfcon_outputs(
    params: PctsurfconParameters,
    execution: Execution,
) -> PctsurfconOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PctsurfconOutputs(
        root=execution.output_file("."),
    )
    return ret


def pctsurfcon_execute(
    params: PctsurfconParameters,
    execution: Execution,
) -> PctsurfconOutputs:
    """
    Compute surface-wise gray/white matter contrast.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PctsurfconOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = pctsurfcon_cargs(params, execution)
    ret = pctsurfcon_outputs(params, execution)
    execution.run(cargs)
    return ret


def pctsurfcon(
    subject: str,
    fsvol: str | None = None,
    outbase: str | None = None,
    lh_only: bool = False,
    rh_only: bool = False,
    gm_proj_frac: float | None = None,
    gm_proj_abs: float | None = None,
    wm_proj_abs: float | None = None,
    neg: bool = False,
    no_mask: bool = False,
    pial: bool = False,
    tmp: str | None = None,
    nocleanup: bool = False,
    runner: Runner | None = None,
) -> PctsurfconOutputs:
    """
    Compute surface-wise gray/white matter contrast.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject name.
        fsvol: Use fsvol instead of rawavg.
        outbase: Use outbase instead of w-g.pct (?h.w-g.pct.mgh).
        lh_only: Compute left hemisphere only.
        rh_only: Compute right hemisphere only.
        gm_proj_frac: GM projection fraction (default 0.3).
        gm_proj_abs: GM projection distance (default is to use frac).
        wm_proj_abs: WM projection distance (default is 1 mm).
        neg: Compute G-W instead of W-G.
        no_mask: Do not mask out non-cortical regions.
        pial: Use pial surface as base to compute gray/CSF contrast.
        tmp: Temporary directory (implies --nocleanup).
        nocleanup: Do not delete temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PctsurfconOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PCTSURFCON_METADATA)
    params = pctsurfcon_params(subject=subject, fsvol=fsvol, outbase=outbase, lh_only=lh_only, rh_only=rh_only, gm_proj_frac=gm_proj_frac, gm_proj_abs=gm_proj_abs, wm_proj_abs=wm_proj_abs, neg=neg, no_mask=no_mask, pial=pial, tmp=tmp, nocleanup=nocleanup)
    return pctsurfcon_execute(params, execution)


__all__ = [
    "PCTSURFCON_METADATA",
    "PctsurfconOutputs",
    "pctsurfcon",
    "pctsurfcon_params",
]
