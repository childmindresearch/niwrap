# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


VOLUME_FILL_HOLES_METADATA = Metadata(
    id="4d7ac9c22920a6808ced9079431f362acbb2a465",
    name="volume-fill-holes",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeFillHolesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_fill_holes(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output ROI volume"""


def volume_fill_holes(
    volume_in: InputPathType,
    volume_out: InputPathType,
    runner: Runner = None,
) -> VolumeFillHolesOutputs:
    """
    volume-fill-holes by Washington University School of Medicin.
    
    Fill holes in an roi volume.
    
    Finds all face-connected parts that are not included in the ROI, and fills
    all but the largest one with ones.
    
    Args:
        volume_in: the input ROI volume
        volume_out: the output ROI volume
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeFillHolesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_FILL_HOLES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-fill-holes")
    cargs.append(execution.input_file(volume_in))
    cargs.append(execution.input_file(volume_out))
    ret = VolumeFillHolesOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_FILL_HOLES_METADATA",
    "VolumeFillHolesOutputs",
    "volume_fill_holes",
]
