# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RUN_MESH_UTILS_METADATA = Metadata(
    id="81dd15d0b8d878045c3e7c5b559acdbb407ac87f.boutiques",
    name="run_mesh_utils",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class RunMeshUtilsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_mesh_utils(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """Output image file"""


def run_mesh_utils(
    base_mesh: InputPathType,
    output_image: str,
    input_image: InputPathType | None = None,
    second_input_image: InputPathType | None = None,
    weighting_image_force: InputPathType | None = None,
    runner: Runner | None = None,
) -> RunMeshUtilsOutputs:
    """
    A tool for various mesh operations as part of FSL.
    
    Author: University of Oxford (Brian Patenaude)
    
    Args:
        base_mesh: Filename of base mesh.
        output_image: Filename of output image.
        input_image: Filename of input image.
        second_input_image: Filename of second input image.
        weighting_image_force: Weighting image force.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunMeshUtilsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_MESH_UTILS_METADATA)
    cargs = []
    cargs.append("run_mesh_utils")
    cargs.append(execution.input_file(base_mesh))
    cargs.extend([
        "-o",
        output_image
    ])
    if input_image is not None:
        cargs.extend([
            "-i",
            execution.input_file(input_image)
        ])
    if second_input_image is not None:
        cargs.extend([
            "-j",
            execution.input_file(second_input_image)
        ])
    if weighting_image_force is not None:
        cargs.extend([
            "-p",
            execution.input_file(weighting_image_force)
        ])
    cargs.append("[OPTIONAL_PARAMS...]")
    ret = RunMeshUtilsOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(output_image),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RUN_MESH_UTILS_METADATA",
    "RunMeshUtilsOutputs",
    "run_mesh_utils",
]