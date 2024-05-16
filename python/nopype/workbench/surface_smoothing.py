# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.910447

import typing

from ..styxdefs import *


SURFACE_SMOOTHING_METADATA = Metadata(
    id="d0efcfca152b018584aace9c65c1fcf169a7c42f",
    name="surface-smoothing",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_smoothing(...)`.
    """
    surface_out: OutputPathType
    """output surface file"""


def surface_smoothing(
    runner: Runner,
    surface_in: InputPathType,
    smoothing_strength: float | int,
    smoothing_iterations: float | int,
    surface_out: InputPathType,
) -> SurfaceSmoothingOutputs:
    """
    SURFACE SMOOTHING.
    
    Smooths a surface by averaging vertex coordinates with those of the
    neighboring vertices.
    
    Args:
        runner: Command runner
        surface_in: the surface file to smooth
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0])
        smoothing_iterations: smoothing iterations
        surface_out: output surface file
    Returns:
        NamedTuple of outputs (described in `SurfaceSmoothingOutputs`).
    """
    execution = runner.start_execution(SURFACE_SMOOTHING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-smoothing")
    cargs.append(execution.input_file(surface_in))
    cargs.append(str(smoothing_strength))
    cargs.append(str(smoothing_iterations))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceSmoothingOutputs(
        surface_out=execution.output_file(f"{surface_out}"),
    )
    execution.run(cargs)
    return ret
