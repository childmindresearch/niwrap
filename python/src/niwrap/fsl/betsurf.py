# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BETSURF_METADATA = Metadata(
    id="8759b3f32e4b1fca0178e3fed0a2b1719da58c7f",
    name="betsurf",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:6.0.5",
)


class BetsurfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `betsurf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_mask: OutputPathType
    """Generated binary mask"""
    output_outline: OutputPathType
    """Generated surface outline"""
    output_skull: OutputPathType
    """Generated skull mask"""


def betsurf(
    t1_image: InputPathType,
    bet_mesh: InputPathType,
    t1_to_standard_mat: InputPathType,
    output_prefix: str,
    t2_image: InputPathType | None = None,
    help_flag: bool = False,
    verbose_flag: bool = False,
    t1only_flag: bool = False,
    outline_flag: bool = False,
    mask_flag: bool = False,
    skull_mask_flag: bool = False,
    increased_precision: int | None = None,
    runner: Runner | None = None,
) -> BetsurfOutputs:
    """
    betsurf by FMRIB Analysis Group, Oxford.
    
    BET Surface Finder to extract brain surfaces using T1 and T2 images.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET
    
    Args:
        t1_image: T1-weighted MRI image.
        bet_mesh: BET Mesh File (.vtk).
        t1_to_standard_mat: Transformation matrix file from T1 to standard\
            space.
        output_prefix: Output prefix for generated files.
        t2_image: T2-weighted MRI image (optional if using --t1only flag).
        help_flag: Displays help message and exits.
        verbose_flag: Switch on diagnostic messages.
        t1only_flag: Extraction with T1 only.
        outline_flag: Generates all surface outlines.
        mask_flag: Generates binary masks from the meshes.
        skull_mask_flag: Generates skull binary mask.
        increased_precision: Retessellates the meshes the indicated number of\
            times (int).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BetsurfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BETSURF_METADATA)
    cargs = []
    cargs.append("betsurf")
    cargs.append("[OPTIONS]")
    cargs.append("<t1>")
    cargs.append("[<t2>]")
    cargs.append("<bet_mesh.vtk>")
    cargs.append("<t1_to_standard.mat>")
    cargs.append("<output>")
    ret = BetsurfOutputs(
        root=execution.output_file("."),
        output_mask=execution.output_file(f"{output_prefix}_mask.nii.gz", optional=True),
        output_outline=execution.output_file(f"{output_prefix}_outline.nii.gz", optional=True),
        output_skull=execution.output_file(f"{output_prefix}_skull.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BETSURF_METADATA",
    "BetsurfOutputs",
    "betsurf",
]
