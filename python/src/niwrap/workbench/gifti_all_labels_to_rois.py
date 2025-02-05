# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GIFTI_ALL_LABELS_TO_ROIS_METADATA = Metadata(
    id="c161705a58523c71238aee0100d0a0020c221135.boutiques",
    name="gifti-all-labels-to-rois",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
GiftiAllLabelsToRoisParameters = typing.TypedDict('GiftiAllLabelsToRoisParameters', {
    "__STYX_TYPE__": typing.Literal["gifti-all-labels-to-rois"],
    "label_in": InputPathType,
    "map": str,
    "metric_out": str,
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
        "gifti-all-labels-to-rois": gifti_all_labels_to_rois_cargs,
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
        "gifti-all-labels-to-rois": gifti_all_labels_to_rois_outputs,
    }
    return vt.get(t)


class GiftiAllLabelsToRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_all_labels_to_rois(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def gifti_all_labels_to_rois_params(
    label_in: InputPathType,
    map_: str,
    metric_out: str,
) -> GiftiAllLabelsToRoisParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input gifti label file.
        map_: the number or name of the label map to use.
        metric_out: the output metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gifti-all-labels-to-rois",
        "label_in": label_in,
        "map": map_,
        "metric_out": metric_out,
    }
    return params


def gifti_all_labels_to_rois_cargs(
    params: GiftiAllLabelsToRoisParameters,
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
    cargs.append("wb_command")
    cargs.append("-gifti-all-labels-to-rois")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("map"))
    cargs.append(params.get("metric_out"))
    return cargs


def gifti_all_labels_to_rois_outputs(
    params: GiftiAllLabelsToRoisParameters,
    execution: Execution,
) -> GiftiAllLabelsToRoisOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GiftiAllLabelsToRoisOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def gifti_all_labels_to_rois_execute(
    params: GiftiAllLabelsToRoisParameters,
    execution: Execution,
) -> GiftiAllLabelsToRoisOutputs:
    """
    Make rois from all labels in a gifti column.
    
    The output metric file has a column for each label in the specified input
    map, other than the ??? label, each of which contains an ROI of all vertices
    that are set to the corresponding label.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GiftiAllLabelsToRoisOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = gifti_all_labels_to_rois_cargs(params, execution)
    ret = gifti_all_labels_to_rois_outputs(params, execution)
    execution.run(cargs)
    return ret


def gifti_all_labels_to_rois(
    label_in: InputPathType,
    map_: str,
    metric_out: str,
    runner: Runner | None = None,
) -> GiftiAllLabelsToRoisOutputs:
    """
    Make rois from all labels in a gifti column.
    
    The output metric file has a column for each label in the specified input
    map, other than the ??? label, each of which contains an ROI of all vertices
    that are set to the corresponding label.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input gifti label file.
        map_: the number or name of the label map to use.
        metric_out: the output metric file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GiftiAllLabelsToRoisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GIFTI_ALL_LABELS_TO_ROIS_METADATA)
    params = gifti_all_labels_to_rois_params(label_in=label_in, map_=map_, metric_out=metric_out)
    return gifti_all_labels_to_rois_execute(params, execution)


__all__ = [
    "GIFTI_ALL_LABELS_TO_ROIS_METADATA",
    "GiftiAllLabelsToRoisOutputs",
    "GiftiAllLabelsToRoisParameters",
    "gifti_all_labels_to_rois",
    "gifti_all_labels_to_rois_params",
]
