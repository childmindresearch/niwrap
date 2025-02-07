# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ANNOT_TO_SEGMENTATION_METADATA = Metadata(
    id="a6fe77811c128028277a69a99f1e7f945cb0ac57.boutiques",
    name="mris_annot_to_segmentation",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisAnnotToSegmentationParameters = typing.TypedDict('MrisAnnotToSegmentationParameters', {
    "__STYX_TYPE__": typing.Literal["mris_annot_to_segmentation"],
    "subject_name": str,
    "hemi": str,
    "surface": str,
    "annot_file": InputPathType,
    "color_table": InputPathType,
    "output_volume": str,
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
        "mris_annot_to_segmentation": mris_annot_to_segmentation_cargs,
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
        "mris_annot_to_segmentation": mris_annot_to_segmentation_outputs,
    }.get(t)


class MrisAnnotToSegmentationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_annot_to_segmentation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Generated segmentation volume."""


def mris_annot_to_segmentation_params(
    subject_name: str,
    hemi: str,
    surface: str,
    annot_file: InputPathType,
    color_table: InputPathType,
    output_volume: str,
) -> MrisAnnotToSegmentationParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Subject name.
        hemi: Hemisphere (e.g., lh or rh).
        surface: Surface file.
        annot_file: Annotation file.
        color_table: Color table file.
        output_volume: Output volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_annot_to_segmentation",
        "subject_name": subject_name,
        "hemi": hemi,
        "surface": surface,
        "annot_file": annot_file,
        "color_table": color_table,
        "output_volume": output_volume,
    }
    return params


def mris_annot_to_segmentation_cargs(
    params: MrisAnnotToSegmentationParameters,
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
    cargs.append("mris_annot_to_segmentation")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("surface"))
    cargs.append(execution.input_file(params.get("annot_file")))
    cargs.append(execution.input_file(params.get("color_table")))
    cargs.append(params.get("output_volume"))
    return cargs


def mris_annot_to_segmentation_outputs(
    params: MrisAnnotToSegmentationParameters,
    execution: Execution,
) -> MrisAnnotToSegmentationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisAnnotToSegmentationOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mris_annot_to_segmentation_execute(
    params: MrisAnnotToSegmentationParameters,
    execution: Execution,
) -> MrisAnnotToSegmentationOutputs:
    """
    Converts annotation files to segmentation volumes in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisAnnotToSegmentationOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_annot_to_segmentation_cargs(params, execution)
    ret = mris_annot_to_segmentation_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_annot_to_segmentation(
    subject_name: str,
    hemi: str,
    surface: str,
    annot_file: InputPathType,
    color_table: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MrisAnnotToSegmentationOutputs:
    """
    Converts annotation files to segmentation volumes in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name.
        hemi: Hemisphere (e.g., lh or rh).
        surface: Surface file.
        annot_file: Annotation file.
        color_table: Color table file.
        output_volume: Output volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisAnnotToSegmentationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ANNOT_TO_SEGMENTATION_METADATA)
    params = mris_annot_to_segmentation_params(subject_name=subject_name, hemi=hemi, surface=surface, annot_file=annot_file, color_table=color_table, output_volume=output_volume)
    return mris_annot_to_segmentation_execute(params, execution)


__all__ = [
    "MRIS_ANNOT_TO_SEGMENTATION_METADATA",
    "MrisAnnotToSegmentationOutputs",
    "MrisAnnotToSegmentationParameters",
    "mris_annot_to_segmentation",
    "mris_annot_to_segmentation_params",
]
