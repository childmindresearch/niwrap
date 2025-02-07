# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SURFACE_TO_VOL_DISTANCES_METADATA = Metadata(
    id="b436cdee4792f571a6fb7c9b7311696958c3dc2d.boutiques",
    name="mris_surface_to_vol_distances",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSurfaceToVolDistancesParameters = typing.TypedDict('MrisSurfaceToVolDistancesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_surface_to_vol_distances"],
    "average_subject": str,
    "hemisphere": str,
    "subjects": list[str],
    "output_prefix": str,
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
        "mris_surface_to_vol_distances": mris_surface_to_vol_distances_cargs,
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
        "mris_surface_to_vol_distances": mris_surface_to_vol_distances_outputs,
    }.get(t)


class MrisSurfaceToVolDistancesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_surface_to_vol_distances(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_distances: OutputPathType
    """Output file containing surface-to-volume distances."""


def mris_surface_to_vol_distances_params(
    average_subject: str,
    hemisphere: str,
    subjects: list[str],
    output_prefix: str,
) -> MrisSurfaceToVolDistancesParameters:
    """
    Build parameters.
    
    Args:
        average_subject: The average subject.
        hemisphere: Hemisphere identifier (e.g., lh or rh).
        subjects: List of subjects for distance calculation.
        output_prefix: Prefix for output files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_surface_to_vol_distances",
        "average_subject": average_subject,
        "hemisphere": hemisphere,
        "subjects": subjects,
        "output_prefix": output_prefix,
    }
    return params


def mris_surface_to_vol_distances_cargs(
    params: MrisSurfaceToVolDistancesParameters,
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
    cargs.append("mris_surface_to_vol_distances")
    cargs.append(params.get("average_subject"))
    cargs.append(params.get("hemisphere"))
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_prefix"))
    return cargs


def mris_surface_to_vol_distances_outputs(
    params: MrisSurfaceToVolDistancesParameters,
    execution: Execution,
) -> MrisSurfaceToVolDistancesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSurfaceToVolDistancesOutputs(
        root=execution.output_file("."),
        output_distances=execution.output_file(params.get("output_prefix") + "_distances.txt"),
    )
    return ret


def mris_surface_to_vol_distances_execute(
    params: MrisSurfaceToVolDistancesParameters,
    execution: Execution,
) -> MrisSurfaceToVolDistancesOutputs:
    """
    Tool from FreeSurfer to calculate surface-to-volume distances.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSurfaceToVolDistancesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_surface_to_vol_distances_cargs(params, execution)
    ret = mris_surface_to_vol_distances_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_surface_to_vol_distances(
    average_subject: str,
    hemisphere: str,
    subjects: list[str],
    output_prefix: str,
    runner: Runner | None = None,
) -> MrisSurfaceToVolDistancesOutputs:
    """
    Tool from FreeSurfer to calculate surface-to-volume distances.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        average_subject: The average subject.
        hemisphere: Hemisphere identifier (e.g., lh or rh).
        subjects: List of subjects for distance calculation.
        output_prefix: Prefix for output files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSurfaceToVolDistancesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SURFACE_TO_VOL_DISTANCES_METADATA)
    params = mris_surface_to_vol_distances_params(average_subject=average_subject, hemisphere=hemisphere, subjects=subjects, output_prefix=output_prefix)
    return mris_surface_to_vol_distances_execute(params, execution)


__all__ = [
    "MRIS_SURFACE_TO_VOL_DISTANCES_METADATA",
    "MrisSurfaceToVolDistancesOutputs",
    "MrisSurfaceToVolDistancesParameters",
    "mris_surface_to_vol_distances",
    "mris_surface_to_vol_distances_params",
]
