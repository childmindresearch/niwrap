# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


VOLUME_ALL_LABELS_TO_ROIS_METADATA = Metadata(
    id="1a228c317bc85c474029f5c5ed5bdae11cc081a7",
    name="volume-all-labels-to-rois",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeAllLabelsToRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_all_labels_to_rois(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume file"""


def volume_all_labels_to_rois(
    label_in: InputPathType,
    map_: str,
    volume_out: InputPathType,
    runner: Runner = None,
) -> VolumeAllLabelsToRoisOutputs:
    """
    volume-all-labels-to-rois by Washington University School of Medicin.
    
    Make rois from all labels in a volume frame.
    
    The output volume has a frame for each label in the specified input frame,
    other than the ??? label, each of which contains an ROI of all voxels that
    are set to the corresponding label.
    
    Args:
        label_in: the input volume label file
        map_: the number or name of the label map to use
        volume_out: the output volume file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeAllLabelsToRoisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_ALL_LABELS_TO_ROIS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-all-labels-to-rois")
    cargs.append(execution.input_file(label_in))
    cargs.append(map_)
    cargs.append(execution.input_file(volume_out))
    ret = VolumeAllLabelsToRoisOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_ALL_LABELS_TO_ROIS_METADATA",
    "VolumeAllLabelsToRoisOutputs",
    "volume_all_labels_to_rois",
]
