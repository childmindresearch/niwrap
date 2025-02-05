# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_RESAMPLE_METADATA = Metadata(
    id="d258d7337c5b1952a178b938bc77164575d3516d.boutiques",
    name="mris_resample",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisResampleParameters = typing.TypedDict('MrisResampleParameters', {
    "__STYX_TYPE__": typing.Literal["mris_resample"],
    "atlas_reg": InputPathType,
    "subject_reg": InputPathType,
    "subject_surf": InputPathType,
    "output": str,
    "annot_in": typing.NotRequired[InputPathType | None],
    "annot_out": typing.NotRequired[str | None],
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
        "mris_resample": mris_resample_cargs,
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
        "mris_resample": mris_resample_outputs,
    }
    return vt.get(t)


class MrisResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    resampled_surface_output: OutputPathType
    """Resampled surface output"""
    resampled_annotation_output: OutputPathType | None
    """Output annotation for the resampled atlas"""


def mris_resample_params(
    atlas_reg: InputPathType,
    subject_reg: InputPathType,
    subject_surf: InputPathType,
    output: str,
    annot_in: InputPathType | None = None,
    annot_out: str | None = None,
) -> MrisResampleParameters:
    """
    Build parameters.
    
    Args:
        atlas_reg: Atlas spherical registration file.
        subject_reg: Subject spherical registration file.
        subject_surf: Subject actual surface.
        output: Output resampled surface.
        annot_in: Input annotation (for the subject). If present, output\
            annotation must be present as well.
        annot_out: Output annotation (for the resampled atlas). If present,\
            input annotation must be present as well.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_resample",
        "atlas_reg": atlas_reg,
        "subject_reg": subject_reg,
        "subject_surf": subject_surf,
        "output": output,
    }
    if annot_in is not None:
        params["annot_in"] = annot_in
    if annot_out is not None:
        params["annot_out"] = annot_out
    return params


def mris_resample_cargs(
    params: MrisResampleParameters,
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
    cargs.append("mris_resample")
    cargs.extend([
        "-atlas_reg",
        execution.input_file(params.get("atlas_reg"))
    ])
    cargs.extend([
        "-subject_reg",
        execution.input_file(params.get("subject_reg"))
    ])
    cargs.extend([
        "-subject_surf",
        execution.input_file(params.get("subject_surf"))
    ])
    cargs.extend([
        "-out",
        params.get("output")
    ])
    if params.get("annot_in") is not None:
        cargs.extend([
            "--annot_in",
            execution.input_file(params.get("annot_in"))
        ])
    if params.get("annot_out") is not None:
        cargs.extend([
            "--annot_out",
            params.get("annot_out")
        ])
    return cargs


def mris_resample_outputs(
    params: MrisResampleParameters,
    execution: Execution,
) -> MrisResampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisResampleOutputs(
        root=execution.output_file("."),
        resampled_surface_output=execution.output_file(params.get("output")),
        resampled_annotation_output=execution.output_file(params.get("annot_out")) if (params.get("annot_out") is not None) else None,
    )
    return ret


def mris_resample_execute(
    params: MrisResampleParameters,
    execution: Execution,
) -> MrisResampleOutputs:
    """
    Resample cortical surfaces in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisResampleOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_resample_cargs(params, execution)
    ret = mris_resample_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_resample(
    atlas_reg: InputPathType,
    subject_reg: InputPathType,
    subject_surf: InputPathType,
    output: str,
    annot_in: InputPathType | None = None,
    annot_out: str | None = None,
    runner: Runner | None = None,
) -> MrisResampleOutputs:
    """
    Resample cortical surfaces in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        atlas_reg: Atlas spherical registration file.
        subject_reg: Subject spherical registration file.
        subject_surf: Subject actual surface.
        output: Output resampled surface.
        annot_in: Input annotation (for the subject). If present, output\
            annotation must be present as well.
        annot_out: Output annotation (for the resampled atlas). If present,\
            input annotation must be present as well.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_RESAMPLE_METADATA)
    params = mris_resample_params(atlas_reg=atlas_reg, subject_reg=subject_reg, subject_surf=subject_surf, output=output, annot_in=annot_in, annot_out=annot_out)
    return mris_resample_execute(params, execution)


__all__ = [
    "MRIS_RESAMPLE_METADATA",
    "MrisResampleOutputs",
    "MrisResampleParameters",
    "mris_resample",
    "mris_resample_params",
]
