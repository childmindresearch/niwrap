# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_MORPH_STATS_METADATA = Metadata(
    id="099da71ba5e21f2b547c57eee2eaadeb2784a79c.boutiques",
    name="mris_morph_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisMorphStatsParameters = typing.TypedDict('MrisMorphStatsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_morph_stats"],
    "subject_name": str,
    "hemisphere": typing.Literal["lh", "rh"],
    "morphed_surface": InputPathType,
    "output_name": str,
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
        "mris_morph_stats": mris_morph_stats_cargs,
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
        "mris_morph_stats": mris_morph_stats_outputs,
    }
    return vt.get(t)


class MrisMorphStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_morph_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stats_output: OutputPathType
    """Generated statistics of the surface-based deformation field."""


def mris_morph_stats_params(
    subject_name: str,
    hemisphere: typing.Literal["lh", "rh"],
    morphed_surface: InputPathType,
    output_name: str,
) -> MrisMorphStatsParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Hemisphere, either 'lh' for left hemisphere or 'rh' for\
            right hemisphere.
        morphed_surface: Morphed surface file.
        output_name: Name of the output to be generated.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_morph_stats",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "morphed_surface": morphed_surface,
        "output_name": output_name,
    }
    return params


def mris_morph_stats_cargs(
    params: MrisMorphStatsParameters,
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
    cargs.append("mris_morph_stats")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    cargs.append(execution.input_file(params.get("morphed_surface")))
    cargs.append(params.get("output_name"))
    return cargs


def mris_morph_stats_outputs(
    params: MrisMorphStatsParameters,
    execution: Execution,
) -> MrisMorphStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMorphStatsOutputs(
        root=execution.output_file("."),
        stats_output=execution.output_file(params.get("output_name")),
    )
    return ret


def mris_morph_stats_execute(
    params: MrisMorphStatsParameters,
    execution: Execution,
) -> MrisMorphStatsOutputs:
    """
    This program generates statistics which characterize a surface-based deformation
    field.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMorphStatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_morph_stats_cargs(params, execution)
    ret = mris_morph_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_morph_stats(
    subject_name: str,
    hemisphere: typing.Literal["lh", "rh"],
    morphed_surface: InputPathType,
    output_name: str,
    runner: Runner | None = None,
) -> MrisMorphStatsOutputs:
    """
    This program generates statistics which characterize a surface-based deformation
    field.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Hemisphere, either 'lh' for left hemisphere or 'rh' for\
            right hemisphere.
        morphed_surface: Morphed surface file.
        output_name: Name of the output to be generated.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMorphStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MORPH_STATS_METADATA)
    params = mris_morph_stats_params(subject_name=subject_name, hemisphere=hemisphere, morphed_surface=morphed_surface, output_name=output_name)
    return mris_morph_stats_execute(params, execution)


__all__ = [
    "MRIS_MORPH_STATS_METADATA",
    "MrisMorphStatsOutputs",
    "MrisMorphStatsParameters",
    "mris_morph_stats",
    "mris_morph_stats_params",
]
