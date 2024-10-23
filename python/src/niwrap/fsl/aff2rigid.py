# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFF2RIGID_METADATA = Metadata(
    id="cfdce16816cf612ff4eb9e1cabfa00e80da0d647.boutiques",
    name="aff2rigid",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class Aff2rigidOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aff2rigid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def aff2rigid(
    input_transform: InputPathType,
    output_transform: str,
    runner: Runner | None = None,
) -> Aff2rigidOutputs:
    """
    Tool for converting affine transformations to rigid transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_transform: Input FLIRT transform (12 DOF) from the input image to\
            standard space.
        output_transform: Output matrix which will convert the input image to\
            standard space using a 6 DOF transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Aff2rigidOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFF2RIGID_METADATA)
    cargs = []
    cargs.append("aff2rigid")
    cargs.append(execution.input_file(input_transform))
    cargs.append(output_transform)
    ret = Aff2rigidOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFF2RIGID_METADATA",
    "Aff2rigidOutputs",
    "aff2rigid",
]
