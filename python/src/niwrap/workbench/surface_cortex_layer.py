# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_CORTEX_LAYER_METADATA = Metadata(
    id="6a041b109a3dbe6936b952ecb53a3579fd004c3a",
    name="surface-cortex-layer",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceCortexLayerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_cortex_layer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surface: OutputPathType
    """the output surface"""
    placement_metric: OutputPathType
    """output metric"""


def surface_cortex_layer(
    white_surface: InputPathType,
    pial_surface: InputPathType,
    location: float | int,
    out_surface: str,
    placement_metric: str,
    opt_placement_out: bool = False,
    runner: Runner | None = None,
) -> SurfaceCortexLayerOutputs:
    """
    surface-cortex-layer by Washington University School of Medicin.
    
    Create surface approximating a cortical layer.
    
    The input surfaces must have vertex correspondence. The output surface is
    generated by placing vertices between the two surfaces such that the
    enclosed volume within any small patch of the new and white surfaces is the
    given fraction of the volume of the same patch between the pial and white
    surfaces (i.e., specifying 0 would give the white surface, 1 would give the
    pial surface). .
    
    Args:
        white_surface: the white matter surface.
        pial_surface: the pial surface.
        location: what volume fraction to place the layer at.
        out_surface: the output surface.
        placement_metric: output metric.
        opt_placement_out: output the placement as a volume fraction from pial\
            to white.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCortexLayerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CORTEX_LAYER_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-cortex-layer")
    cargs.append(execution.input_file(white_surface))
    cargs.append(execution.input_file(pial_surface))
    cargs.append(str(location))
    cargs.append(out_surface)
    if opt_placement_out:
        cargs.append("-placement-out")
    cargs.append(placement_metric)
    ret = SurfaceCortexLayerOutputs(
        root=execution.output_file("."),
        out_surface=execution.output_file(f"{out_surface}"),
        placement_metric=execution.output_file(f"{placement_metric}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_CORTEX_LAYER_METADATA",
    "SurfaceCortexLayerOutputs",
    "surface_cortex_layer",
]
