# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:56.041899

import typing

from ..styxdefs import *


SPLIT_METADATA = Metadata(
    id="862ef8a3c22ea14581181f7076b9e56f4a7ac890",
    name="Split",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SplitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `split(...)`.
    """
    out_folder: OutputPathType
    """Output folder with multiple files."""


def split(
    runner: Runner,
    in_file: InputPathType,
    out_base_name: str | None = None,
    dimension: typing.Literal["t", "x", "y", "z"] = "t",
) -> SplitOutputs:
    """
    Split, as implemented in Nipype (module: nipype.interfaces.fsl, interface:
    Split).
    Uses FSL Fslsplit command to separate a volume into images in time, x, y or
    z dimension.
    
    Args:
        runner: Command runner
        in_file: Input image to split along dimension (default: time).
        out_base_name: Output prefix
        dimension: 't' or 'x' or 'y' or 'z'. Dimension to mean across.
    Returns:
        NamedTuple of outputs (described in `SplitOutputs`).
    """
    execution = runner.start_execution(SPLIT_METADATA)
    cargs = []
    cargs.append("fslsplit")
    cargs.append(execution.input_file(in_file))
    if out_base_name is not None:
        cargs.append(
            "out/" +
            out_base_name +
            ""
        )
    cargs.append(("-" + dimension))
    ret = SplitOutputs(
        out_folder=execution.output_file(f"out/"),
    )
    execution.run(cargs)
    return ret
