# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.936038

import typing

from ..styxdefs import *


VOLUME_REMOVE_ISLANDS_METADATA = Metadata(
    id="c5e32d66758bf8e6c5a01a532c03bc1853929d8a",
    name="volume-remove-islands",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeRemoveIslandsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_remove_islands(...)`.
    """
    volume_out: OutputPathType
    """the output ROI volume"""


def volume_remove_islands(
    runner: Runner,
    volume_in: InputPathType,
    volume_out: InputPathType,
) -> VolumeRemoveIslandsOutputs:
    """
    REMOVE ISLANDS FROM AN ROI VOLUME.
    
    Finds all face-connected parts of the ROI, and zeros out all but the largest
    one.
    
    Args:
        runner: Command runner
        volume_in: the input ROI volume
        volume_out: the output ROI volume
    Returns:
        NamedTuple of outputs (described in `VolumeRemoveIslandsOutputs`).
    """
    execution = runner.start_execution(VOLUME_REMOVE_ISLANDS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-remove-islands")
    cargs.append(execution.input_file(volume_in))
    cargs.append(execution.input_file(volume_out))
    ret = VolumeRemoveIslandsOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret
