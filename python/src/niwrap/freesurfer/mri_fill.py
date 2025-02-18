# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_FILL_METADATA = Metadata(
    id="45567bfdadd532485f2ed2b4fee5ffc3e7f9d609.boutiques",
    name="mri_fill",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriFillParameters = typing.TypedDict('MriFillParameters', {
    "__STYX_TYPE__": typing.Literal["mri_fill"],
    "input_mr_dir": str,
    "output_mr_dir": str,
    "threshold": typing.NotRequired[float | None],
    "xform_name": typing.NotRequired[str | None],
    "segmentation_file": typing.NotRequired[InputPathType | None],
    "atlas_file": typing.NotRequired[InputPathType | None],
    "fill_ven": bool,
    "seed_cc_tal": typing.NotRequired[list[float] | None],
    "seed_pons_tal": typing.NotRequired[list[float] | None],
    "seed_lh_tal": typing.NotRequired[list[float] | None],
    "seed_rh_tal": typing.NotRequired[list[float] | None],
    "seed_cc_vox": typing.NotRequired[list[float] | None],
    "seed_pons_vox": typing.NotRequired[list[float] | None],
    "auto_man_files": typing.NotRequired[list[str] | None],
    "no_auto_man": bool,
    "pointset_args": typing.NotRequired[list[str] | None],
    "ctab_file": typing.NotRequired[InputPathType | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_fill": mri_fill_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_fill": mri_fill_outputs,
    }.get(t)


class MriFillOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fill(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filled_volume: OutputPathType
    """The filled volume for the cortical reconstruction, used for subsequent
    surface tessellation"""


def mri_fill_params(
    input_mr_dir: str,
    output_mr_dir: str,
    threshold: float | None = None,
    xform_name: str | None = None,
    segmentation_file: InputPathType | None = None,
    atlas_file: InputPathType | None = None,
    fill_ven: bool = False,
    seed_cc_tal: list[float] | None = None,
    seed_pons_tal: list[float] | None = None,
    seed_lh_tal: list[float] | None = None,
    seed_rh_tal: list[float] | None = None,
    seed_cc_vox: list[float] | None = None,
    seed_pons_vox: list[float] | None = None,
    auto_man_files: list[str] | None = None,
    no_auto_man: bool = False,
    pointset_args: list[str] | None = None,
    ctab_file: InputPathType | None = None,
) -> MriFillParameters:
    """
    Build parameters.
    
    Args:
        input_mr_dir: Input MR directory.
        output_mr_dir: Output MR directory.
        threshold: Specify fill_holes threshold (default=1).
        xform_name: Use xform dst offset to get an accurate Talairach volume.
        segmentation_file: ASEG volume used to perform fill.
        atlas_file: Specify atlas to use for auto-filling.
        fill_ven: Fill ventricles.
        seed_cc_tal: Talairach coords of the seed for the corpus callosum\
            (three numerical values required).
        seed_pons_tal: Talairach coords of the seed for the pons (three\
            numerical values required).
        seed_lh_tal: Talairach coords of the white matter seed for the left\
            hemisphere (three numerical values required).
        seed_rh_tal: Talairach coords of the white matter seed for the right\
            hemisphere (three numerical values required).
        seed_cc_vox: Voxel coords of the seed for the corpus callosum (three\
            numerical values required).
        seed_pons_vox: Voxel coords of the seed for the pons (three numerical\
            values required).
        auto_man_files: Get edits based on the difference between auto and man\
            and apply to the output.
        no_auto_man: Turns off the -auto-man option.
        pointset_args: Stand-alone option: takes one or more pointsets and\
            fills in all the voxels that intersect lines connecting any two points\
            within a given point set.
        ctab_file: Embed color table in the output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_fill",
        "input_mr_dir": input_mr_dir,
        "output_mr_dir": output_mr_dir,
        "fill_ven": fill_ven,
        "no_auto_man": no_auto_man,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if xform_name is not None:
        params["xform_name"] = xform_name
    if segmentation_file is not None:
        params["segmentation_file"] = segmentation_file
    if atlas_file is not None:
        params["atlas_file"] = atlas_file
    if seed_cc_tal is not None:
        params["seed_cc_tal"] = seed_cc_tal
    if seed_pons_tal is not None:
        params["seed_pons_tal"] = seed_pons_tal
    if seed_lh_tal is not None:
        params["seed_lh_tal"] = seed_lh_tal
    if seed_rh_tal is not None:
        params["seed_rh_tal"] = seed_rh_tal
    if seed_cc_vox is not None:
        params["seed_cc_vox"] = seed_cc_vox
    if seed_pons_vox is not None:
        params["seed_pons_vox"] = seed_pons_vox
    if auto_man_files is not None:
        params["auto_man_files"] = auto_man_files
    if pointset_args is not None:
        params["pointset_args"] = pointset_args
    if ctab_file is not None:
        params["ctab_file"] = ctab_file
    return params


def mri_fill_cargs(
    params: MriFillParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mri_fill")
    cargs.append(params.get("input_mr_dir"))
    cargs.append(params.get("output_mr_dir"))
    if params.get("threshold") is not None:
        cargs.extend([
            "-T",
            str(params.get("threshold"))
        ])
    if params.get("xform_name") is not None:
        cargs.extend([
            "-xform",
            params.get("xform_name")
        ])
    if params.get("segmentation_file") is not None:
        cargs.extend([
            "-segmentation",
            execution.input_file(params.get("segmentation_file"))
        ])
    if params.get("atlas_file") is not None:
        cargs.extend([
            "-atlas",
            execution.input_file(params.get("atlas_file"))
        ])
    if params.get("fill_ven"):
        cargs.append("-fillven")
    if params.get("seed_cc_tal") is not None:
        cargs.extend([
            "-C",
            *map(str, params.get("seed_cc_tal"))
        ])
    if params.get("seed_pons_tal") is not None:
        cargs.extend([
            "-P",
            *map(str, params.get("seed_pons_tal"))
        ])
    if params.get("seed_lh_tal") is not None:
        cargs.extend([
            "-lh",
            *map(str, params.get("seed_lh_tal"))
        ])
    if params.get("seed_rh_tal") is not None:
        cargs.extend([
            "-rh",
            *map(str, params.get("seed_rh_tal"))
        ])
    if params.get("seed_cc_vox") is not None:
        cargs.extend([
            "-CV",
            *map(str, params.get("seed_cc_vox"))
        ])
    if params.get("seed_pons_vox") is not None:
        cargs.extend([
            "-PV",
            *map(str, params.get("seed_pons_vox"))
        ])
    if params.get("auto_man_files") is not None:
        cargs.extend([
            "-auto-man",
            *params.get("auto_man_files")
        ])
    if params.get("no_auto_man"):
        cargs.append("-no-auto-man")
    if params.get("pointset_args") is not None:
        cargs.extend([
            "-pointset",
            *params.get("pointset_args")
        ])
    if params.get("ctab_file") is not None:
        cargs.extend([
            "-ctab",
            execution.input_file(params.get("ctab_file"))
        ])
    return cargs


def mri_fill_outputs(
    params: MriFillParameters,
    execution: Execution,
) -> MriFillOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFillOutputs(
        root=execution.output_file("."),
        filled_volume=execution.output_file(params.get("output_mr_dir") + "/filled"),
    )
    return ret


def mri_fill_execute(
    params: MriFillParameters,
    execution: Execution,
) -> MriFillOutputs:
    """
    Tool for creating hemispheric cutting planes and filling white matter for
    surface tessellation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFillOutputs`).
    """
    params = execution.params(params)
    cargs = mri_fill_cargs(params, execution)
    ret = mri_fill_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_fill(
    input_mr_dir: str,
    output_mr_dir: str,
    threshold: float | None = None,
    xform_name: str | None = None,
    segmentation_file: InputPathType | None = None,
    atlas_file: InputPathType | None = None,
    fill_ven: bool = False,
    seed_cc_tal: list[float] | None = None,
    seed_pons_tal: list[float] | None = None,
    seed_lh_tal: list[float] | None = None,
    seed_rh_tal: list[float] | None = None,
    seed_cc_vox: list[float] | None = None,
    seed_pons_vox: list[float] | None = None,
    auto_man_files: list[str] | None = None,
    no_auto_man: bool = False,
    pointset_args: list[str] | None = None,
    ctab_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriFillOutputs:
    """
    Tool for creating hemispheric cutting planes and filling white matter for
    surface tessellation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_mr_dir: Input MR directory.
        output_mr_dir: Output MR directory.
        threshold: Specify fill_holes threshold (default=1).
        xform_name: Use xform dst offset to get an accurate Talairach volume.
        segmentation_file: ASEG volume used to perform fill.
        atlas_file: Specify atlas to use for auto-filling.
        fill_ven: Fill ventricles.
        seed_cc_tal: Talairach coords of the seed for the corpus callosum\
            (three numerical values required).
        seed_pons_tal: Talairach coords of the seed for the pons (three\
            numerical values required).
        seed_lh_tal: Talairach coords of the white matter seed for the left\
            hemisphere (three numerical values required).
        seed_rh_tal: Talairach coords of the white matter seed for the right\
            hemisphere (three numerical values required).
        seed_cc_vox: Voxel coords of the seed for the corpus callosum (three\
            numerical values required).
        seed_pons_vox: Voxel coords of the seed for the pons (three numerical\
            values required).
        auto_man_files: Get edits based on the difference between auto and man\
            and apply to the output.
        no_auto_man: Turns off the -auto-man option.
        pointset_args: Stand-alone option: takes one or more pointsets and\
            fills in all the voxels that intersect lines connecting any two points\
            within a given point set.
        ctab_file: Embed color table in the output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFillOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FILL_METADATA)
    params = mri_fill_params(input_mr_dir=input_mr_dir, output_mr_dir=output_mr_dir, threshold=threshold, xform_name=xform_name, segmentation_file=segmentation_file, atlas_file=atlas_file, fill_ven=fill_ven, seed_cc_tal=seed_cc_tal, seed_pons_tal=seed_pons_tal, seed_lh_tal=seed_lh_tal, seed_rh_tal=seed_rh_tal, seed_cc_vox=seed_cc_vox, seed_pons_vox=seed_pons_vox, auto_man_files=auto_man_files, no_auto_man=no_auto_man, pointset_args=pointset_args, ctab_file=ctab_file)
    return mri_fill_execute(params, execution)


__all__ = [
    "MRI_FILL_METADATA",
    "MriFillOutputs",
    "MriFillParameters",
    "mri_fill",
    "mri_fill_params",
]
