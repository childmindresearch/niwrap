# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CA_LABEL_METADATA = Metadata(
    id="c0e789089e779577ca1a230a4a3e0792c8cbc29d.boutiques",
    name="mri_ca_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriCaLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_ca_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vol: OutputPathType
    """Output labeled volume."""


def mri_ca_label(
    input_volumes: list[InputPathType],
    transform_file: InputPathType,
    gca_file: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriCaLabelOutputs:
    """
    MRI cortical annotation labeler using atlas prior (GCA).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volumes: Input MRI volumes.
        transform_file: Transform file for the registration.
        gca_file: GCA file for the atlas.
        output_volume: Output labeled volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCaLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CA_LABEL_METADATA)
    cargs = []
    cargs.append("mri_ca_label")
    cargs.extend([execution.input_file(f) for f in input_volumes])
    cargs.append(execution.input_file(transform_file))
    cargs.append(execution.input_file(gca_file))
    cargs.append(output_volume)
    cargs.append("[OPTIONS]")
    ret = MriCaLabelOutputs(
        root=execution.output_file("."),
        output_vol=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_CA_LABEL_METADATA",
    "MriCaLabelOutputs",
    "mri_ca_label",
]