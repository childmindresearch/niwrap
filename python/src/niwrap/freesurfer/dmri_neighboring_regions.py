# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_NEIGHBORING_REGIONS_METADATA = Metadata(
    id="0178eb527b86ea0845721b0e3a911c76330df23a.boutiques",
    name="dmri_neighboringRegions",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriNeighboringRegionsParameters = typing.TypedDict('DmriNeighboringRegionsParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_neighboringRegions"],
    "input_file": InputPathType,
    "output_file": str,
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
        "dmri_neighboringRegions": dmri_neighboring_regions_cargs,
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
        "dmri_neighboringRegions": dmri_neighboring_regions_outputs,
    }
    return vt.get(t)


class DmriNeighboringRegionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_neighboring_regions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_file: OutputPathType
    """Resulting output file from dmri_neighboringRegions"""


def dmri_neighboring_regions_params(
    input_file: InputPathType,
    output_file: str,
) -> DmriNeighboringRegionsParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input image file (e.g. img.nii.gz).
        output_file: Output result file (e.g. result.nii.gz).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_neighboringRegions",
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def dmri_neighboring_regions_cargs(
    params: DmriNeighboringRegionsParameters,
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
    cargs.append("dmri_neighboringRegions")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    return cargs


def dmri_neighboring_regions_outputs(
    params: DmriNeighboringRegionsParameters,
    execution: Execution,
) -> DmriNeighboringRegionsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriNeighboringRegionsOutputs(
        root=execution.output_file("."),
        result_file=execution.output_file(params.get("output_file")),
    )
    return ret


def dmri_neighboring_regions_execute(
    params: DmriNeighboringRegionsParameters,
    execution: Execution,
) -> DmriNeighboringRegionsOutputs:
    """
    A tool for diffusion MRI analysis involving neighboring regions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriNeighboringRegionsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dmri_neighboring_regions_cargs(params, execution)
    ret = dmri_neighboring_regions_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_neighboring_regions(
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> DmriNeighboringRegionsOutputs:
    """
    A tool for diffusion MRI analysis involving neighboring regions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input image file (e.g. img.nii.gz).
        output_file: Output result file (e.g. result.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriNeighboringRegionsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_NEIGHBORING_REGIONS_METADATA)
    params = dmri_neighboring_regions_params(input_file=input_file, output_file=output_file)
    return dmri_neighboring_regions_execute(params, execution)


__all__ = [
    "DMRI_NEIGHBORING_REGIONS_METADATA",
    "DmriNeighboringRegionsOutputs",
    "DmriNeighboringRegionsParameters",
    "dmri_neighboring_regions",
    "dmri_neighboring_regions_params",
]
