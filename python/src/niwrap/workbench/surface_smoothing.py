# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


SURFACE_SMOOTHING_METADATA = Metadata(
    id="b5c34814840a8341b4177335aae09e164d8ce54d",
    name="surface-smoothing",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """output surface file"""


def surface_smoothing(
    surface_in: InputPathType,
    smoothing_strength: float | int,
    smoothing_iterations: int,
    surface_out: InputPathType,
    runner: Runner = None,
) -> SurfaceSmoothingOutputs:
    """
    surface-smoothing by Washington University School of Medicin.
    
    Surface smoothing.
    
    Smooths a surface by averaging vertex coordinates with those of the
    neighboring vertices.
    
    Args:
        surface_in: the surface file to smooth
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0])
        smoothing_iterations: smoothing iterations
        surface_out: output surface file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_SMOOTHING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-smoothing")
    cargs.append(execution.input_file(surface_in))
    cargs.append(str(smoothing_strength))
    cargs.append(str(smoothing_iterations))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceSmoothingOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_SMOOTHING_METADATA",
    "SurfaceSmoothingOutputs",
    "surface_smoothing",
]
