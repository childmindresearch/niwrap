# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMCALC_METADATA = Metadata(
    id="619429e3eb3a18d69af5e0d47edb5f5289323a19.boutiques",
    name="imcalc",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ImcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType | None
    """Output image file produced after applying the expression to input
    images"""


def imcalc(
    expression: str,
    datum_type: str | None = None,
    image_inputs: list[InputPathType] | None = None,
    output_name: str | None = None,
    runner: Runner | None = None,
) -> ImcalcOutputs:
    """
    Tool for arithmetic operations on 2D images, pixel-by-pixel.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        expression: Apply the expression within quotes to the input images, one\
            voxel at a time, to produce the output image. (e.g., "sqrt(a*b)" to\
            compute the geometric mean).
        datum_type: Coerce the output data to be stored as the given type:\
            byte, short, or float. Default is the datum of the first input image on\
            the command line.
        image_inputs: Read image 'dname' and call the voxel values 'a' in the\
            expression. 'a' may be any letter from 'a' to 'z'. If some letter name\
            is used in the expression but not present in one of the image options\
            here, then that variable is set to 0.
        output_name: Use 'name' for the output image filename. Default is\
            'imcalc.out'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMCALC_METADATA)
    cargs = []
    cargs.append("imcalc")
    if datum_type is not None:
        cargs.extend([
            "-datum type",
            datum_type
        ])
    if image_inputs is not None:
        cargs.extend([
            "-a",
            *[execution.input_file(f) for f in image_inputs]
        ])
    cargs.extend([
        "-expr",
        expression
    ])
    if output_name is not None:
        cargs.extend([
            "-output",
            output_name
        ])
    ret = ImcalcOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(output_name) if (output_name is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMCALC_METADATA",
    "ImcalcOutputs",
    "imcalc",
]
