# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_COMPUTE_VOLUME_INTENSITIES_METADATA = Metadata(
    id="45ae774d2336d807239cb10e6ca5a797474fe7bd.boutiques",
    name="mri_compute_volume_intensities",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriComputeVolumeIntensitiesParameters = typing.TypedDict('MriComputeVolumeIntensitiesParameters', {
    "__STYX_TYPE__": typing.Literal["mri_compute_volume_intensities"],
    "input_intensity": InputPathType,
    "volume_fraction_stem": str,
    "output_volume": str,
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
        "mri_compute_volume_intensities": mri_compute_volume_intensities_cargs,
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
        "mri_compute_volume_intensities": mri_compute_volume_intensities_outputs,
    }
    return vt.get(t)


class MriComputeVolumeIntensitiesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_volume_intensities(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Computed output volume file"""


def mri_compute_volume_intensities_params(
    input_intensity: InputPathType,
    volume_fraction_stem: str,
    output_volume: str,
) -> MriComputeVolumeIntensitiesParameters:
    """
    Build parameters.
    
    Args:
        input_intensity: Input intensity volume.
        volume_fraction_stem: Volume fraction stem.
        output_volume: Output volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_compute_volume_intensities",
        "input_intensity": input_intensity,
        "volume_fraction_stem": volume_fraction_stem,
        "output_volume": output_volume,
    }
    return params


def mri_compute_volume_intensities_cargs(
    params: MriComputeVolumeIntensitiesParameters,
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
    cargs.append("mri_compute_volume_intensities")
    cargs.append(execution.input_file(params.get("input_intensity")))
    cargs.append(params.get("volume_fraction_stem"))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_compute_volume_intensities_outputs(
    params: MriComputeVolumeIntensitiesParameters,
    execution: Execution,
) -> MriComputeVolumeIntensitiesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriComputeVolumeIntensitiesOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_compute_volume_intensities_execute(
    params: MriComputeVolumeIntensitiesParameters,
    execution: Execution,
) -> MriComputeVolumeIntensitiesOutputs:
    """
    A tool to compute volume intensities for a given input intensity volume and
    volume fraction stem.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriComputeVolumeIntensitiesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_compute_volume_intensities_cargs(params, execution)
    ret = mri_compute_volume_intensities_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_compute_volume_intensities(
    input_intensity: InputPathType,
    volume_fraction_stem: str,
    output_volume: str,
    runner: Runner | None = None,
) -> MriComputeVolumeIntensitiesOutputs:
    """
    A tool to compute volume intensities for a given input intensity volume and
    volume fraction stem.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_intensity: Input intensity volume.
        volume_fraction_stem: Volume fraction stem.
        output_volume: Output volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeVolumeIntensitiesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_VOLUME_INTENSITIES_METADATA)
    params = mri_compute_volume_intensities_params(input_intensity=input_intensity, volume_fraction_stem=volume_fraction_stem, output_volume=output_volume)
    return mri_compute_volume_intensities_execute(params, execution)


__all__ = [
    "MRI_COMPUTE_VOLUME_INTENSITIES_METADATA",
    "MriComputeVolumeIntensitiesOutputs",
    "MriComputeVolumeIntensitiesParameters",
    "mri_compute_volume_intensities",
    "mri_compute_volume_intensities_params",
]
