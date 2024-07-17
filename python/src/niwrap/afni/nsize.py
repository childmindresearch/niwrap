# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

NSIZE_METADATA = Metadata(
    id="8d3ddcfa6f14f561aab2595cc7caf39642d3d921",
    name="nsize",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class NsizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nsize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    image_out_file: OutputPathType
    """Zero padded output image file"""


def nsize(
    image_in: InputPathType,
    image_out: str,
    runner: Runner | None = None,
) -> NsizeOutputs:
    """
    nsize by AFNI Team.
    
    Zero pads an input image to the nearest larger NxN dimensions.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/nsize.html
    
    Args:
        image_in: Input image file.
        image_out: Output padded image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NsizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NSIZE_METADATA)
    cargs = []
    cargs.append("nsize")
    cargs.append(execution.input_file(image_in))
    cargs.append(image_out)
    ret = NsizeOutputs(
        root=execution.output_file("."),
        image_out_file=execution.output_file(f"{image_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NSIZE_METADATA",
    "NsizeOutputs",
    "nsize",
]
