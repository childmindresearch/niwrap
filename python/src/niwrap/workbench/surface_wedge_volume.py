# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_WEDGE_VOLUME_METADATA = Metadata(
    id="9c9de0e85b0353439f7a299bed43ec6fd12e6aa8",
    name="surface-wedge-volume",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceWedgeVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_wedge_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric: OutputPathType
    """the output metric"""


def surface_wedge_volume(
    inner_surface: InputPathType,
    outer_surface: InputPathType,
    metric: str,
    runner: Runner = None,
) -> SurfaceWedgeVolumeOutputs:
    """
    surface-wedge-volume by Washington University School of Medicin.
    
    Measure per-vertex volume between surfaces.
    
    Compute the volume of each vertex's area from one surface to another. The
    surfaces must have vertex correspondence, and have consistent triangle
    orientation.
    
    Args:
        inner_surface: the inner surface.
        outer_surface: the outer surface.
        metric: the output metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceWedgeVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_WEDGE_VOLUME_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-wedge-volume")
    cargs.append(execution.input_file(inner_surface))
    cargs.append(execution.input_file(outer_surface))
    cargs.append(metric)
    ret = SurfaceWedgeVolumeOutputs(
        root=execution.output_file("."),
        metric=execution.output_file(f"{metric}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_WEDGE_VOLUME_METADATA",
    "SurfaceWedgeVolumeOutputs",
    "surface_wedge_volume",
]
