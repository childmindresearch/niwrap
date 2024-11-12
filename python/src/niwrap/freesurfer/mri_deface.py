# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_DEFACE_METADATA = Metadata(
    id="3c5f529687f2b3d58e2f151ffcd47a04e323d8ea.boutiques",
    name="mri_deface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriDefaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_deface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    defaced_output_file: OutputPathType
    """The resulting defaced MRI volume."""


def mri_deface(
    input_volume: InputPathType,
    brain_template: InputPathType,
    face_template: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriDefaceOutputs:
    """
    MRI Deface utility for removing facial features from MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: The input volume to be defaced (e.g. anatomical MRI\
            image).
        brain_template: Template volume of the brain to be used for defacing.
        face_template: Template volume of the face to be used for defacing.
        output_volume: The output volume path for the defaced image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriDefaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_DEFACE_METADATA)
    cargs = []
    cargs.append("mri_deface")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(brain_template))
    cargs.append(execution.input_file(face_template))
    cargs.append(output_volume)
    ret = MriDefaceOutputs(
        root=execution.output_file("."),
        defaced_output_file=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_DEFACE_METADATA",
    "MriDefaceOutputs",
    "mri_deface",
]