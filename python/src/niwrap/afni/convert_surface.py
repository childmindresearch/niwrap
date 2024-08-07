# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CONVERT_SURFACE_METADATA = Metadata(
    id="39673a316b600ba234b2c1ce484429acf840262c",
    name="ConvertSurface",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ConvertSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """The converted output surface file."""


def convert_surface(
    input_surface: str,
    output_surface: str,
    surface_volume: str | None = None,
    transform_tlrc: bool = False,
    mni_rai: bool = False,
    mni_lpi: bool = False,
    xmat_1_d: str | None = None,
    ixmat_1_d: str | None = None,
    seed: str | None = None,
    native: bool = False,
    runner: Runner | None = None,
) -> ConvertSurfaceOutputs:
    """
    ConvertSurface by AFNI Team.
    
    Reads in a surface and writes it out in another format. Only fields
    pertinent to SUMA are preserved.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/ConvertSurface.html
    
    Args:
        input_surface: Specifies the input surface.
        output_surface: Specifies the output surface.
        surface_volume: Specifies a surface volume.
        transform_tlrc: Apply Talairach transform.
        mni_rai: Turn AFNI tlrc coordinates (RAI) into MNI coord space in RAI.
        mni_lpi: Turn AFNI tlrc coordinates (RAI) into MNI coord space in LPI.
        xmat_1_d: Apply transformation specified in 1D file.
        ixmat_1_d: Apply inverse transformation specified in 1D file.
        seed: Specify SEED to seed the random number generator for random\
            matrix generation.
        native: Write the output surface in the coordinate system native to its\
            format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_SURFACE_METADATA)
    cargs = []
    cargs.append("ConvertSurface")
    cargs.extend(["-i", input_surface])
    cargs.extend(["-o", output_surface])
    if surface_volume is not None:
        cargs.extend(["-sv", surface_volume])
    if transform_tlrc:
        cargs.append("-tlrc")
    if mni_lpi:
        cargs.append("-MNI_lpi")
    if ixmat_1_d is not None:
        cargs.extend(["-ixmat_1D", ixmat_1_d])
    if native:
        cargs.append("-native")
    ret = ConvertSurfaceOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(f"{output_surface}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_SURFACE_METADATA",
    "ConvertSurfaceOutputs",
    "convert_surface",
]
