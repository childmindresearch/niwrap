# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SLICEANIMATE_METADATA = Metadata(
    id="099af2c06ac54016e7c1bbb4fcea54e66d3d7c2d.boutiques",
    name="sliceanimate",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SliceanimateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sliceanimate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    animated_gif: OutputPathType
    """Generated animated GIF"""


def sliceanimate(
    output_file: str,
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> SliceanimateOutputs:
    """
    A tool for animating slices of an image using whirlgif.
    
    Author: Various Authors (Hans Dinsen-Hansen, Kevin Kadow, Mark Podlipec)
    
    Args:
        output_file: Output animated GIF file.
        input_files: Input image files for animation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SliceanimateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICEANIMATE_METADATA)
    cargs = []
    cargs.append("sliceanimate")
    cargs.append(output_file)
    cargs.append("--")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = SliceanimateOutputs(
        root=execution.output_file("."),
        animated_gif=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLICEANIMATE_METADATA",
    "SliceanimateOutputs",
    "sliceanimate",
]
