# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_SURF_MASK_METADATA = Metadata(
    id="193cfbe86177c2e59f981d82cc4cdbc7636aea67",
    name="3dSurfMask",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dSurfMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_surf_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_mask: OutputPathType
    """Main output mask dataset."""
    distance_dataset: OutputPathType
    """Dataset reflecting voxel shortest distances to the surface."""


def v_3d_surf_mask(
    surface_type: str,
    surface_file: InputPathType,
    prefix: str,
    grid_parent: InputPathType,
    fill_method: str | None = None,
    surface_volume: InputPathType | None = None,
    mask_only: bool = False,
    flip_orientation: bool = False,
    no_distance: bool = False,
    runner: Runner | None = None,
) -> V3dSurfMaskOutputs:
    """
    3dSurfMask by AFNI Team.
    
    Creates volumetric datasets marking voxels based on their location relative
    to a surface.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSurfMask.html
    
    Args:
        surface_type: Specify input surface.
        surface_file: Specify input surface filename.
        prefix: Prefix of output dataset.
        grid_parent: Specifies the grid for the output volume.
        fill_method: Fill method: SLOW or FAST (default: FAST).
        surface_volume: Specify the surface volume.
        mask_only: Produce an output dataset where voxels are 1 inside the\
            surface and 0 outside.
        flip_orientation: Flip triangle winding of surface mesh.
        no_distance: Do not compute the distances, just the mask from the first\
            step.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSurfMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SURF_MASK_METADATA)
    cargs = []
    cargs.append("3dSurfMask")
    cargs.append("<-i_TYPE")
    cargs.append("SURFACE>")
    cargs.append("<-prefix")
    cargs.append("PREFIX>")
    cargs.append("<-grid_parent")
    cargs.append("GRID_VOL>")
    cargs.append("[<fill_method>")
    cargs.append("<SURF_VOL>")
    cargs.append("<mask_only>")
    cargs.append("<flip_orientation>")
    cargs.append("<no_dist>]")
    ret = V3dSurfMaskOutputs(
        root=execution.output_file("."),
        output_mask=execution.output_file(f"{prefix}.m+orig.BRIK"),
        distance_dataset=execution.output_file(f"{prefix}.d+orig.BRIK", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSurfMaskOutputs",
    "V_3D_SURF_MASK_METADATA",
    "v_3d_surf_mask",
]
