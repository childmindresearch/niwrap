# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

APARC2FEAT_METADATA = Metadata(
    id="40a686bfd13826d8c5472e46b643ff5ee20464a4.boutiques",
    name="aparc2feat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Aparc2featParameters = typing.TypedDict('Aparc2featParameters', {
    "__STYX_TYPE__": typing.Literal["aparc2feat"],
    "feat_directories": str,
    "featdirfile": typing.NotRequired[InputPathType | None],
    "hemi": typing.NotRequired[str | None],
    "annot": typing.NotRequired[str | None],
    "annot_a2005s_flag": bool,
    "annot_a2009s_flag": bool,
    "debug_flag": bool,
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
        "aparc2feat": aparc2feat_cargs,
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
        "aparc2feat": aparc2feat_outputs,
    }
    return vt.get(t)


class Aparc2featOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aparc2feat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lh_aparc_output: OutputPathType
    """Output Left Hemisphere aparc in nifti format."""
    rh_aparc_output: OutputPathType
    """Output Right Hemisphere aparc in nifti format."""


def aparc2feat_params(
    feat_directories: str,
    featdirfile: InputPathType | None = None,
    hemi: str | None = None,
    annot: str | None = None,
    annot_a2005s_flag: bool = False,
    annot_a2009s_flag: bool = False,
    debug_flag: bool = False,
) -> Aparc2featParameters:
    """
    Build parameters.
    
    Args:
        feat_directories: FEAT output directory. Multiple --feat arguments can\
            be supplied.
        featdirfile: File with a list of FEAT directories. Multiple\
            --featdirfile flags are allowed.
        hemi: Resample hemisphere only (default is both rh and lh).
        annot: Specify something other than aparc.
        annot_a2005s_flag: Specify annotation = aparc.a2005s.
        annot_a2009s_flag: Specify annotation = aparc.a2009s.
        debug_flag: Turn on debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "aparc2feat",
        "feat_directories": feat_directories,
        "annot_a2005s_flag": annot_a2005s_flag,
        "annot_a2009s_flag": annot_a2009s_flag,
        "debug_flag": debug_flag,
    }
    if featdirfile is not None:
        params["featdirfile"] = featdirfile
    if hemi is not None:
        params["hemi"] = hemi
    if annot is not None:
        params["annot"] = annot
    return params


def aparc2feat_cargs(
    params: Aparc2featParameters,
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
    cargs.append("aparc2feat")
    cargs.extend([
        "--feat",
        params.get("feat_directories")
    ])
    if params.get("featdirfile") is not None:
        cargs.extend([
            "--featdirfile",
            execution.input_file(params.get("featdirfile"))
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("annot") is not None:
        cargs.extend([
            "--annot",
            params.get("annot")
        ])
    if params.get("annot_a2005s_flag"):
        cargs.append("--a2005s")
    if params.get("annot_a2009s_flag"):
        cargs.append("--a2009s")
    if params.get("debug_flag"):
        cargs.append("--debug")
    return cargs


def aparc2feat_outputs(
    params: Aparc2featParameters,
    execution: Execution,
) -> Aparc2featOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Aparc2featOutputs(
        root=execution.output_file("."),
        lh_aparc_output=execution.output_file(params.get("feat_directories") + "/reg/freesurfer/lh.aparc.nii.gz"),
        rh_aparc_output=execution.output_file(params.get("feat_directories") + "/reg/freesurfer/rh.aparc.nii.gz"),
    )
    return ret


def aparc2feat_execute(
    params: Aparc2featParameters,
    execution: Execution,
) -> Aparc2featOutputs:
    """
    Resamples the FreeSurfer automatic cortical segmentation to the FEAT functional
    space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Aparc2featOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = aparc2feat_cargs(params, execution)
    ret = aparc2feat_outputs(params, execution)
    execution.run(cargs)
    return ret


def aparc2feat(
    feat_directories: str,
    featdirfile: InputPathType | None = None,
    hemi: str | None = None,
    annot: str | None = None,
    annot_a2005s_flag: bool = False,
    annot_a2009s_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> Aparc2featOutputs:
    """
    Resamples the FreeSurfer automatic cortical segmentation to the FEAT functional
    space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat_directories: FEAT output directory. Multiple --feat arguments can\
            be supplied.
        featdirfile: File with a list of FEAT directories. Multiple\
            --featdirfile flags are allowed.
        hemi: Resample hemisphere only (default is both rh and lh).
        annot: Specify something other than aparc.
        annot_a2005s_flag: Specify annotation = aparc.a2005s.
        annot_a2009s_flag: Specify annotation = aparc.a2009s.
        debug_flag: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Aparc2featOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APARC2FEAT_METADATA)
    params = aparc2feat_params(feat_directories=feat_directories, featdirfile=featdirfile, hemi=hemi, annot=annot, annot_a2005s_flag=annot_a2005s_flag, annot_a2009s_flag=annot_a2009s_flag, debug_flag=debug_flag)
    return aparc2feat_execute(params, execution)


__all__ = [
    "APARC2FEAT_METADATA",
    "Aparc2featOutputs",
    "Aparc2featParameters",
    "aparc2feat",
    "aparc2feat_params",
]
