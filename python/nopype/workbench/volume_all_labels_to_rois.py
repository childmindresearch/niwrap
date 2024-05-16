# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.699428

import typing

from ..styxdefs import *


VOLUME_ALL_LABELS_TO_ROIS_METADATA = Metadata(
    id="6f9daa807160b730014f1f84aa28de77a42e1b78",
    name="volume-all-labels-to-rois",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeAllLabelsToRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_all_labels_to_rois(...)`.
    """
    volume_out: OutputPathType
    """the output volume file"""


def volume_all_labels_to_rois(
    runner: Runner,
    label_in: InputPathType,
    map_: str,
    volume_out: InputPathType,
) -> VolumeAllLabelsToRoisOutputs:
    """
    MAKE ROIS FROM ALL LABELS IN A VOLUME FRAME.
    
    The output volume has a frame for each label in the specified input frame,
    other than the ??? label, each of which contains an ROI of all voxels that
    are set to the corresponding label.
    
    Args:
        runner: Command runner
        label_in: the input volume label file
        map_: the number or name of the label map to use
        volume_out: the output volume file
    Returns:
        NamedTuple of outputs (described in `VolumeAllLabelsToRoisOutputs`).
    """
    execution = runner.start_execution(VOLUME_ALL_LABELS_TO_ROIS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-all-labels-to-rois")
    cargs.append(execution.input_file(label_in))
    cargs.append(map_)
    cargs.append(execution.input_file(volume_out))
    ret = VolumeAllLabelsToRoisOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret
