# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SAMPLE_PARC_METADATA = Metadata(
    id="63fdac72bbfef323f1126c39c936ff5c938f8b5d.boutiques",
    name="mris_sample_parc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSampleParcParameters = typing.TypedDict('MrisSampleParcParameters', {
    "__STYX_TYPE__": typing.Literal["mris_sample_parc"],
    "subject_name": str,
    "hemisphere": str,
    "parc_name": str,
    "output_annot": str,
    "sdir": typing.NotRequired[str | None],
    "surf": typing.NotRequired[str | None],
    "fix": typing.NotRequired[float | None],
    "replace": typing.NotRequired[float | None],
    "trans": typing.NotRequired[list[float] | None],
    "cortex": typing.NotRequired[str | None],
    "projmm": typing.NotRequired[float | None],
    "proj": typing.NotRequired[float | None],
    "projfrac": typing.NotRequired[float | None],
    "file": typing.NotRequired[str | None],
    "ct": typing.NotRequired[str | None],
    "v_level": typing.NotRequired[float | None],
    "filter": typing.NotRequired[float | None],
    "smooth": typing.NotRequired[float | None],
    "w_size": typing.NotRequired[float | None],
    "thickness": typing.NotRequired[str | None],
    "change_unknown": typing.NotRequired[float | None],
    "help": bool,
    "version": bool,
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
        "mris_sample_parc": mris_sample_parc_cargs,
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
        "mris_sample_parc": mris_sample_parc_outputs,
    }.get(t)


class MrisSampleParcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_sample_parc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output annotation file."""


def mris_sample_parc_params(
    subject_name: str,
    hemisphere: str,
    parc_name: str,
    output_annot: str,
    sdir: str | None = None,
    surf: str | None = None,
    fix: float | None = None,
    replace: float | None = None,
    trans: list[float] | None = None,
    cortex: str | None = None,
    projmm: float | None = None,
    proj: float | None = None,
    projfrac: float | None = None,
    file: str | None = None,
    ct: str | None = None,
    v_level: float | None = None,
    filter_: float | None = None,
    smooth: float | None = None,
    w_size: float | None = None,
    thickness: str | None = None,
    change_unknown: float | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrisSampleParcParameters:
    """
    Build parameters.
    
    Args:
        subject_name: The subject ID.
        hemisphere: Hemisphere: rh or lh.
        parc_name: Parcellation filename.
        output_annot: Output annotation filename.
        sdir: Use as subjects directory (default: $SUBJECTS_DIR).
        surf: Use as surface (default: 'white').
        fix: Fix topology of all labels smaller than the specified number of\
            vertices (default=-1, do all).
        replace: Replace label with deeper ones.
        trans: Translate one label number to another.
        cortex: Mask regions outside of the specified cortex label.
        projmm: Project the specified number of millimeters along surface\
            normal (default=0.0).
        proj: Same as -projmm.
        projfrac: Project the specified percent along surface normal\
            (default=0.5).
        file: Use as translation file (default: 'cma_parcellation_colors.txt').
        ct: Embed color table into output annotation file.
        v_level: Diagnostic level (default=0).
        filter_: Apply mode filter a specified number of times to parcellation\
            (default=0).
        smooth: Smooth surface a specified number of times (default=0).
        w_size: Use window size for sampling (default=7).
        thickness: Use thickness file (default: 'thickness').
        change_unknown: Change largest connected unknown region to specified\
            label (default: don't change).
        help_: Print help info.
        version: Print version info.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_sample_parc",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "parc_name": parc_name,
        "output_annot": output_annot,
        "help": help_,
        "version": version,
    }
    if sdir is not None:
        params["sdir"] = sdir
    if surf is not None:
        params["surf"] = surf
    if fix is not None:
        params["fix"] = fix
    if replace is not None:
        params["replace"] = replace
    if trans is not None:
        params["trans"] = trans
    if cortex is not None:
        params["cortex"] = cortex
    if projmm is not None:
        params["projmm"] = projmm
    if proj is not None:
        params["proj"] = proj
    if projfrac is not None:
        params["projfrac"] = projfrac
    if file is not None:
        params["file"] = file
    if ct is not None:
        params["ct"] = ct
    if v_level is not None:
        params["v_level"] = v_level
    if filter_ is not None:
        params["filter"] = filter_
    if smooth is not None:
        params["smooth"] = smooth
    if w_size is not None:
        params["w_size"] = w_size
    if thickness is not None:
        params["thickness"] = thickness
    if change_unknown is not None:
        params["change_unknown"] = change_unknown
    return params


def mris_sample_parc_cargs(
    params: MrisSampleParcParameters,
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
    cargs.append("mris_sample_parc")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    cargs.append(params.get("parc_name"))
    cargs.append(params.get("output_annot"))
    if params.get("sdir") is not None:
        cargs.extend([
            "-sdir",
            params.get("sdir")
        ])
    if params.get("surf") is not None:
        cargs.extend([
            "-surf",
            params.get("surf")
        ])
    if params.get("fix") is not None:
        cargs.extend([
            "-fix",
            str(params.get("fix"))
        ])
    if params.get("replace") is not None:
        cargs.extend([
            "-replace",
            str(params.get("replace"))
        ])
    if params.get("trans") is not None:
        cargs.extend([
            "-trans",
            *map(str, params.get("trans"))
        ])
    if params.get("cortex") is not None:
        cargs.extend([
            "-cortex",
            params.get("cortex")
        ])
    if params.get("projmm") is not None:
        cargs.extend([
            "-projmm",
            str(params.get("projmm"))
        ])
    if params.get("proj") is not None:
        cargs.extend([
            "-proj",
            str(params.get("proj"))
        ])
    if params.get("projfrac") is not None:
        cargs.extend([
            "-projfrac",
            str(params.get("projfrac"))
        ])
    if params.get("file") is not None:
        cargs.extend([
            "-file",
            params.get("file")
        ])
    if params.get("ct") is not None:
        cargs.extend([
            "-ct",
            params.get("ct")
        ])
    if params.get("v_level") is not None:
        cargs.extend([
            "-v",
            str(params.get("v_level"))
        ])
    if params.get("filter") is not None:
        cargs.extend([
            "-f",
            str(params.get("filter"))
        ])
    if params.get("smooth") is not None:
        cargs.extend([
            "-a",
            str(params.get("smooth"))
        ])
    if params.get("w_size") is not None:
        cargs.extend([
            "-w",
            str(params.get("w_size"))
        ])
    if params.get("thickness") is not None:
        cargs.extend([
            "-t",
            params.get("thickness")
        ])
    if params.get("change_unknown") is not None:
        cargs.extend([
            "-u",
            str(params.get("change_unknown"))
        ])
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mris_sample_parc_outputs(
    params: MrisSampleParcParameters,
    execution: Execution,
) -> MrisSampleParcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSampleParcOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("output_annot")),
    )
    return ret


def mris_sample_parc_execute(
    params: MrisSampleParcParameters,
    execution: Execution,
) -> MrisSampleParcOutputs:
    """
    This program samples a volumetric parcellation onto a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSampleParcOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_sample_parc_cargs(params, execution)
    ret = mris_sample_parc_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_sample_parc(
    subject_name: str,
    hemisphere: str,
    parc_name: str,
    output_annot: str,
    sdir: str | None = None,
    surf: str | None = None,
    fix: float | None = None,
    replace: float | None = None,
    trans: list[float] | None = None,
    cortex: str | None = None,
    projmm: float | None = None,
    proj: float | None = None,
    projfrac: float | None = None,
    file: str | None = None,
    ct: str | None = None,
    v_level: float | None = None,
    filter_: float | None = None,
    smooth: float | None = None,
    w_size: float | None = None,
    thickness: str | None = None,
    change_unknown: float | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrisSampleParcOutputs:
    """
    This program samples a volumetric parcellation onto a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: The subject ID.
        hemisphere: Hemisphere: rh or lh.
        parc_name: Parcellation filename.
        output_annot: Output annotation filename.
        sdir: Use as subjects directory (default: $SUBJECTS_DIR).
        surf: Use as surface (default: 'white').
        fix: Fix topology of all labels smaller than the specified number of\
            vertices (default=-1, do all).
        replace: Replace label with deeper ones.
        trans: Translate one label number to another.
        cortex: Mask regions outside of the specified cortex label.
        projmm: Project the specified number of millimeters along surface\
            normal (default=0.0).
        proj: Same as -projmm.
        projfrac: Project the specified percent along surface normal\
            (default=0.5).
        file: Use as translation file (default: 'cma_parcellation_colors.txt').
        ct: Embed color table into output annotation file.
        v_level: Diagnostic level (default=0).
        filter_: Apply mode filter a specified number of times to parcellation\
            (default=0).
        smooth: Smooth surface a specified number of times (default=0).
        w_size: Use window size for sampling (default=7).
        thickness: Use thickness file (default: 'thickness').
        change_unknown: Change largest connected unknown region to specified\
            label (default: don't change).
        help_: Print help info.
        version: Print version info.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSampleParcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SAMPLE_PARC_METADATA)
    params = mris_sample_parc_params(subject_name=subject_name, hemisphere=hemisphere, parc_name=parc_name, output_annot=output_annot, sdir=sdir, surf=surf, fix=fix, replace=replace, trans=trans, cortex=cortex, projmm=projmm, proj=proj, projfrac=projfrac, file=file, ct=ct, v_level=v_level, filter_=filter_, smooth=smooth, w_size=w_size, thickness=thickness, change_unknown=change_unknown, help_=help_, version=version)
    return mris_sample_parc_execute(params, execution)


__all__ = [
    "MRIS_SAMPLE_PARC_METADATA",
    "MrisSampleParcOutputs",
    "MrisSampleParcParameters",
    "mris_sample_parc",
    "mris_sample_parc_params",
]
