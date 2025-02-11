# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ASEG2FEAT_METADATA = Metadata(
    id="a171951e01eefa6d930d2f5fc71421003b6f23e3.boutiques",
    name="aseg2feat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Aseg2featParameters = typing.TypedDict('Aseg2featParameters', {
    "__STYX_TYPE__": typing.Literal["aseg2feat"],
    "feat": str,
    "featdirfile": typing.NotRequired[InputPathType | None],
    "seg": typing.NotRequired[str | None],
    "aparc_aseg": bool,
    "svstats": bool,
    "standard": bool,
    "debug": bool,
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
        "aseg2feat": aseg2feat_cargs,
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
        "aseg2feat": aseg2feat_outputs,
    }.get(t)


class Aseg2featOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aseg2feat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """Result segmentation in FEAT functional space."""
    stats_output: OutputPathType
    """Directory where results are saved when using --svstats."""


def aseg2feat_params(
    feat: str,
    featdirfile: InputPathType | None = None,
    seg: str | None = None,
    aparc_aseg: bool = False,
    svstats: bool = False,
    standard: bool = False,
    debug: bool = False,
    help_: bool = False,
    version: bool = False,
) -> Aseg2featParameters:
    """
    Build parameters.
    
    Args:
        feat: FEAT output directory. Multiple --feat arguments can be supplied.
        featdirfile: File with a list of FEAT directories. Can be used in\
            conjunction with --feat.
        seg: Change segmentation volume, default is aseg.
        aparc_aseg: Use aparc+aseg.mgz. Same as --seg aparc+aseg.mgz.
        svstats: Save result in featdir/stats instead of featdir/reg/freesurfer.
        standard: Map results to standard space instead of native functional\
            space. Implies --svstats.
        debug: Turn on debugging.
        help_: Print help and exit.
        version: Print version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "aseg2feat",
        "feat": feat,
        "aparc_aseg": aparc_aseg,
        "svstats": svstats,
        "standard": standard,
        "debug": debug,
        "help": help_,
        "version": version,
    }
    if featdirfile is not None:
        params["featdirfile"] = featdirfile
    if seg is not None:
        params["seg"] = seg
    return params


def aseg2feat_cargs(
    params: Aseg2featParameters,
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
    cargs.append("aseg2feat")
    cargs.extend([
        "--feat",
        params.get("feat")
    ])
    if params.get("featdirfile") is not None:
        cargs.extend([
            "--featdirfile",
            execution.input_file(params.get("featdirfile"))
        ])
    if params.get("seg") is not None:
        cargs.extend([
            "--seg",
            params.get("seg")
        ])
    if params.get("aparc_aseg"):
        cargs.append("--aparc+aseg")
    if params.get("svstats"):
        cargs.append("--svstats")
    if params.get("standard"):
        cargs.append("--standard")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def aseg2feat_outputs(
    params: Aseg2featParameters,
    execution: Execution,
) -> Aseg2featOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Aseg2featOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(params.get("feat") + "/reg/freesurfer/aseg.nii.gz"),
        stats_output=execution.output_file(params.get("feat") + "/stats"),
    )
    return ret


def aseg2feat_execute(
    params: Aseg2featParameters,
    execution: Execution,
) -> Aseg2featOutputs:
    """
    Resamples the FreeSurfer automatic subcortical segmentation (aseg) to the FEAT
    functional space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Aseg2featOutputs`).
    """
    cargs = aseg2feat_cargs(params, execution)
    ret = aseg2feat_outputs(params, execution)
    execution.run(cargs)
    return ret


def aseg2feat(
    feat: str,
    featdirfile: InputPathType | None = None,
    seg: str | None = None,
    aparc_aseg: bool = False,
    svstats: bool = False,
    standard: bool = False,
    debug: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Aseg2featOutputs:
    """
    Resamples the FreeSurfer automatic subcortical segmentation (aseg) to the FEAT
    functional space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat: FEAT output directory. Multiple --feat arguments can be supplied.
        featdirfile: File with a list of FEAT directories. Can be used in\
            conjunction with --feat.
        seg: Change segmentation volume, default is aseg.
        aparc_aseg: Use aparc+aseg.mgz. Same as --seg aparc+aseg.mgz.
        svstats: Save result in featdir/stats instead of featdir/reg/freesurfer.
        standard: Map results to standard space instead of native functional\
            space. Implies --svstats.
        debug: Turn on debugging.
        help_: Print help and exit.
        version: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Aseg2featOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ASEG2FEAT_METADATA)
    params = aseg2feat_params(feat=feat, featdirfile=featdirfile, seg=seg, aparc_aseg=aparc_aseg, svstats=svstats, standard=standard, debug=debug, help_=help_, version=version)
    return aseg2feat_execute(params, execution)


__all__ = [
    "ASEG2FEAT_METADATA",
    "Aseg2featOutputs",
    "Aseg2featParameters",
    "aseg2feat",
    "aseg2feat_params",
]
