# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VESSEL_SEGMENT_METADATA = Metadata(
    id="6f3e4e326255b57c2dfda638c29cce61255996ef.boutiques",
    name="mri_vessel_segment",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriVesselSegmentParameters = typing.TypedDict('MriVesselSegmentParameters', {
    "__STYX_TYPE__": typing.Literal["mri_vessel_segment"],
    "t1_image": InputPathType,
    "t2_image": InputPathType,
    "aseg_file": InputPathType,
    "output_file": str,
    "shape_flag": bool,
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
        "mri_vessel_segment": mri_vessel_segment_cargs,
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
        "mri_vessel_segment": mri_vessel_segment_outputs,
    }
    return vt.get(t)


class MriVesselSegmentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_vessel_segment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_output: OutputPathType
    """Segmented vessel output file"""


def mri_vessel_segment_params(
    t1_image: InputPathType,
    t2_image: InputPathType,
    aseg_file: InputPathType,
    output_file: str,
    shape_flag: bool = False,
) -> MriVesselSegmentParameters:
    """
    Build parameters.
    
    Args:
        t1_image: T1-weighted input image.
        t2_image: T2-weighted input image.
        aseg_file: Anatomical segmentation file.
        output_file: Output file.
        shape_flag: Use shape constraints during segmentation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_vessel_segment",
        "t1_image": t1_image,
        "t2_image": t2_image,
        "aseg_file": aseg_file,
        "output_file": output_file,
        "shape_flag": shape_flag,
    }
    return params


def mri_vessel_segment_cargs(
    params: MriVesselSegmentParameters,
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
    cargs.append("mri_vessel_segment")
    cargs.extend([
        "-t1",
        execution.input_file(params.get("t1_image"))
    ])
    cargs.extend([
        "-t2",
        execution.input_file(params.get("t2_image"))
    ])
    cargs.extend([
        "-aseg",
        execution.input_file(params.get("aseg_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    if params.get("shape_flag"):
        cargs.append("--shape")
    return cargs


def mri_vessel_segment_outputs(
    params: MriVesselSegmentParameters,
    execution: Execution,
) -> MriVesselSegmentOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriVesselSegmentOutputs(
        root=execution.output_file("."),
        segmented_output=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_vessel_segment_execute(
    params: MriVesselSegmentParameters,
    execution: Execution,
) -> MriVesselSegmentOutputs:
    """
    MRI vessel segmentation tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriVesselSegmentOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_vessel_segment_cargs(params, execution)
    ret = mri_vessel_segment_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_vessel_segment(
    t1_image: InputPathType,
    t2_image: InputPathType,
    aseg_file: InputPathType,
    output_file: str,
    shape_flag: bool = False,
    runner: Runner | None = None,
) -> MriVesselSegmentOutputs:
    """
    MRI vessel segmentation tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_image: T1-weighted input image.
        t2_image: T2-weighted input image.
        aseg_file: Anatomical segmentation file.
        output_file: Output file.
        shape_flag: Use shape constraints during segmentation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVesselSegmentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VESSEL_SEGMENT_METADATA)
    params = mri_vessel_segment_params(t1_image=t1_image, t2_image=t2_image, aseg_file=aseg_file, output_file=output_file, shape_flag=shape_flag)
    return mri_vessel_segment_execute(params, execution)


__all__ = [
    "MRI_VESSEL_SEGMENT_METADATA",
    "MriVesselSegmentOutputs",
    "MriVesselSegmentParameters",
    "mri_vessel_segment",
    "mri_vessel_segment_params",
]
