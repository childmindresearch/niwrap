# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_APPLY_WARPFIELD_METADATA = Metadata(
    id="7e425f3a8f3f9c436978db3980ba2c4bea2843b2",
    name="surface-apply-warpfield",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceApplyWarpfieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_apply_warpfield(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surf: OutputPathType
    """the output transformed surface"""


def surface_apply_warpfield(
    in_surf: InputPathType,
    warpfield: str,
    out_surf: str,
    opt_fnirt_forward_warp: str | None = None,
    runner: Runner = None,
) -> SurfaceApplyWarpfieldOutputs:
    """
    surface-apply-warpfield by Washington University School of Medicin.
    
    Apply warpfield to surface file.
    
    NOTE: warping a surface requires the INVERSE of the warpfield used to warp
    the volume it lines up with. The header of the forward warp is needed by the
    -fnirt option in order to correctly interpret the displacements in the fnirt
    warpfield.
    
    If the -fnirt option is not present, the warpfield must be a nifti 'world'
    warpfield, which can be obtained with the -convert-warpfield command.
    
    Args:
        in_surf: the surface to transform.
        warpfield: the INVERSE warpfield.
        out_surf: the output transformed surface.
        opt_fnirt_forward_warp: MUST be used if using a fnirt warpfield: the\
            forward warpfield.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceApplyWarpfieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_APPLY_WARPFIELD_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-apply-warpfield")
    cargs.append(execution.input_file(in_surf))
    cargs.append(warpfield)
    cargs.append(out_surf)
    if opt_fnirt_forward_warp is not None:
        cargs.extend(["-fnirt", opt_fnirt_forward_warp])
    ret = SurfaceApplyWarpfieldOutputs(
        root=execution.output_file("."),
        out_surf=execution.output_file(f"{out_surf}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_APPLY_WARPFIELD_METADATA",
    "SurfaceApplyWarpfieldOutputs",
    "surface_apply_warpfield",
]
