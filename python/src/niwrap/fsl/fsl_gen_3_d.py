# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_GEN_3_D_METADATA = Metadata(
    id="fd2e6bded9b2d20b56a7d58ba0bcbb3059c157ec.boutiques",
    name="fsl_gen_3D",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslGen3DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_gen_3_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_snapshot: OutputPathType
    """Generated 3D snapshot of the structural image"""


def fsl_gen_3_d(
    infile: InputPathType,
    outfile: InputPathType,
    runner: Runner | None = None,
) -> FslGen3DOutputs:
    """
    Tool to generate a 3D snapshot of a structural image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input structural image (e.g. input.nii.gz).
        outfile: Output 3D snapshot image (e.g. output.png).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslGen3DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_GEN_3_D_METADATA)
    cargs = []
    cargs.append("fsl_gen_3D")
    cargs.append(execution.input_file(infile))
    cargs.append(execution.input_file(outfile))
    ret = FslGen3DOutputs(
        root=execution.output_file("."),
        output_snapshot=execution.output_file(pathlib.Path(outfile).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_GEN_3_D_METADATA",
    "FslGen3DOutputs",
    "fsl_gen_3_d",
]
