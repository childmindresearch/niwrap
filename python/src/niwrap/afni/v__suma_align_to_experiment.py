# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SUMA_ALIGN_TO_EXPERIMENT_METADATA = Metadata(
    id="0c4071b2f2b071ae9084d5a06a826979d1aed8cc",
    name="SUMA_AlignToExperiment",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SumaAlignToExperimentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `suma_align_to_experiment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aligned_volume: OutputPathType
    """Output volume after alignment."""
    additional_followers: OutputPathType
    """Output followers dataset after transforming."""


def suma_align_to_experiment(
    exp_anat: InputPathType,
    surf_anat: InputPathType,
    dxyz: float | int | None = None,
    out_dxyz: float | int | None = None,
    wd: bool = False,
    al: bool = False,
    al_opt: str | None = None,
    ok_change_view: bool = False,
    strip_skull: str | None = None,
    skull_strip_opt: str | None = None,
    align_centers: bool = False,
    init_xform: InputPathType | None = None,
    ea_clip_below: float | int | None = None,
    prefix: str | None = None,
    surf_anat_followers: str | None = None,
    followers_interp: str | None = None,
    atlas_followers: bool = False,
    echo: bool = False,
    keep_tmp: bool = False,
    overwrite_resp: str | None = None,
    runner: Runner | None = None,
) -> SumaAlignToExperimentOutputs:
    """
    SUMA_AlignToExperiment by AFNI Team.
    
    Creates a version of Surface Anatomy that is registered to Experiment
    Anatomy.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@SUMA_AlignToExperiment.html
    
    Args:
        exp_anat: Name of high resolution anatomical data set in register with\
            experimental data.
        surf_anat: Path and name of high resolution antomical data set used to\
            create the surface.
        dxyz: Optional parameter to downsample anatomical volumes to dxyz mm\
            voxel resolution before registration.
        out_dxyz: Output the final aligned volume at a cubic voxelsize of\
            DXYZmm.
        wd: Use 3dWarpDrive's general affine transform (12 param) instead of\
            3dvolreg's 6 parameters.
        al: Use 3dAllineate to do the 12 parameter alignment. Cost function is\
            'lpa'.
        al_opt: Specify set of options to pass to 3dAllineate.
        ok_change_view: Be quiet when view of registered volume is changed to\
            match that of the Experiment_Anatomy.
        strip_skull: Use 3dSkullStrip to remove non-brain tissue.
        skull_strip_opt: Pass the options to 3dSkullStrip.
        align_centers: Add an additional transformation to align the volume\
            centers.
        init_xform: Apply affine transform file to Surface_Anatomy before\
            beginning registration.
        ea_clip_below: Set slices below CLPmm in 'Experiment Anatomy' to zero.
        prefix: Prefix for the output volume.
        surf_anat_followers: Apply the same alignment transform to additional\
            datasets.
        followers_interp: Set the interpolation mode for the follower datasets.
        atlas_followers: Automatically set the followers to be atlases in the\
            directory of -surf_anat.
        echo: Echo all commands to terminal for debugging.
        keep_tmp: Keep temporary files for debugging.
        overwrite_resp: Answer 'overwrite' questions automatically.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SumaAlignToExperimentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SUMA_ALIGN_TO_EXPERIMENT_METADATA)
    cargs = []
    cargs.append("@SUMA_AlignToExperiment")
    cargs.append("<-exp_anat")
    cargs.append("$$exp_anat$$>")
    cargs.append("<-surf_anat")
    cargs.append("$$surf_anat$$>")
    cargs.append("$$dxyz$$")
    cargs.append("$$wd$$")
    cargs.append("$$prefix$$")
    cargs.append("$$EA_clip_below$$")
    cargs.append("$$align_centers$$")
    cargs.append("$$ok_change_view$$")
    cargs.append("$$strip_skull$$")
    ret = SumaAlignToExperimentOutputs(
        root=execution.output_file("."),
        aligned_volume=execution.output_file(f"[PREFIX]_Alnd_Exp.nii.gz"),
        additional_followers=execution.output_file(f"[PREFIX]_Alnd_Exp_Fdset.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SUMA_ALIGN_TO_EXPERIMENT_METADATA",
    "SumaAlignToExperimentOutputs",
    "suma_align_to_experiment",
]
