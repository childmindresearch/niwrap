# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_EDIT_SEGMENTATION_WITH_SURFACES_METADATA = Metadata(
    id="b7676f431b8610a951f255b96b0e4e26a937a332.boutiques",
    name="mri_edit_segmentation_with_surfaces",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriEditSegmentationWithSurfacesParameters = typing.TypedDict('MriEditSegmentationWithSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["mri_edit_segmentation_with_surfaces"],
    "aseg_name": InputPathType,
    "surface_dir": str,
    "norm_volume": InputPathType,
    "output_volume": str,
    "label_file": typing.NotRequired[InputPathType | None],
    "hypo_flag": typing.NotRequired[typing.Literal["1", "0"] | None],
    "cerebellum_flag": typing.NotRequired[typing.Literal["1", "0"] | None],
    "cortex_flag": typing.NotRequired[typing.Literal["1", "0"] | None],
    "annotation_file": typing.NotRequired[InputPathType | None],
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
        "mri_edit_segmentation_with_surfaces": mri_edit_segmentation_with_surfaces_cargs,
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
        "mri_edit_segmentation_with_surfaces": mri_edit_segmentation_with_surfaces_outputs,
    }.get(t)


class MriEditSegmentationWithSurfacesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_edit_segmentation_with_surfaces(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Edited output volume"""


def mri_edit_segmentation_with_surfaces_params(
    aseg_name: InputPathType,
    surface_dir: str,
    norm_volume: InputPathType,
    output_volume: str,
    label_file: InputPathType | None = None,
    hypo_flag: typing.Literal["1", "0"] | None = None,
    cerebellum_flag: typing.Literal["1", "0"] | None = None,
    cortex_flag: typing.Literal["1", "0"] | None = None,
    annotation_file: InputPathType | None = None,
) -> MriEditSegmentationWithSurfacesParameters:
    """
    Build parameters.
    
    Args:
        aseg_name: The aseg file to be edited.
        surface_dir: Directory containing surface files.
        norm_volume: Normalized volume file.
        output_volume: Output volume file.
        label_file: Limit calculations to specified label.
        hypo_flag: Turn hypointensity editing on/off (1=on, 0=off).
        cerebellum_flag: Turn cerebellum editing on/off (1=on, 0=off).
        cortex_flag: Turn cortex editing on/off (1=on, 0=off).
        annotation_file: Compute properties for each label in the annotation\
            file separately.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_edit_segmentation_with_surfaces",
        "aseg_name": aseg_name,
        "surface_dir": surface_dir,
        "norm_volume": norm_volume,
        "output_volume": output_volume,
    }
    if label_file is not None:
        params["label_file"] = label_file
    if hypo_flag is not None:
        params["hypo_flag"] = hypo_flag
    if cerebellum_flag is not None:
        params["cerebellum_flag"] = cerebellum_flag
    if cortex_flag is not None:
        params["cortex_flag"] = cortex_flag
    if annotation_file is not None:
        params["annotation_file"] = annotation_file
    return params


def mri_edit_segmentation_with_surfaces_cargs(
    params: MriEditSegmentationWithSurfacesParameters,
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
    cargs.append("mri_edit_segmentation_with_surfaces")
    cargs.append(execution.input_file(params.get("aseg_name")))
    cargs.append(params.get("surface_dir"))
    cargs.append(execution.input_file(params.get("norm_volume")))
    cargs.append(params.get("output_volume"))
    if params.get("label_file") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("label_file"))
        ])
    if params.get("hypo_flag") is not None:
        cargs.extend([
            "-hypo",
            params.get("hypo_flag")
        ])
    if params.get("cerebellum_flag") is not None:
        cargs.extend([
            "-cerebellum",
            params.get("cerebellum_flag")
        ])
    if params.get("cortex_flag") is not None:
        cargs.extend([
            "-cortex",
            params.get("cortex_flag")
        ])
    if params.get("annotation_file") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("annotation_file"))
        ])
    return cargs


def mri_edit_segmentation_with_surfaces_outputs(
    params: MriEditSegmentationWithSurfacesParameters,
    execution: Execution,
) -> MriEditSegmentationWithSurfacesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriEditSegmentationWithSurfacesOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_edit_segmentation_with_surfaces_execute(
    params: MriEditSegmentationWithSurfacesParameters,
    execution: Execution,
) -> MriEditSegmentationWithSurfacesOutputs:
    """
    This program edits an aseg with the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriEditSegmentationWithSurfacesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_edit_segmentation_with_surfaces_cargs(params, execution)
    ret = mri_edit_segmentation_with_surfaces_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_edit_segmentation_with_surfaces(
    aseg_name: InputPathType,
    surface_dir: str,
    norm_volume: InputPathType,
    output_volume: str,
    label_file: InputPathType | None = None,
    hypo_flag: typing.Literal["1", "0"] | None = None,
    cerebellum_flag: typing.Literal["1", "0"] | None = None,
    cortex_flag: typing.Literal["1", "0"] | None = None,
    annotation_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriEditSegmentationWithSurfacesOutputs:
    """
    This program edits an aseg with the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        aseg_name: The aseg file to be edited.
        surface_dir: Directory containing surface files.
        norm_volume: Normalized volume file.
        output_volume: Output volume file.
        label_file: Limit calculations to specified label.
        hypo_flag: Turn hypointensity editing on/off (1=on, 0=off).
        cerebellum_flag: Turn cerebellum editing on/off (1=on, 0=off).
        cortex_flag: Turn cortex editing on/off (1=on, 0=off).
        annotation_file: Compute properties for each label in the annotation\
            file separately.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEditSegmentationWithSurfacesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EDIT_SEGMENTATION_WITH_SURFACES_METADATA)
    params = mri_edit_segmentation_with_surfaces_params(aseg_name=aseg_name, surface_dir=surface_dir, norm_volume=norm_volume, output_volume=output_volume, label_file=label_file, hypo_flag=hypo_flag, cerebellum_flag=cerebellum_flag, cortex_flag=cortex_flag, annotation_file=annotation_file)
    return mri_edit_segmentation_with_surfaces_execute(params, execution)


__all__ = [
    "MRI_EDIT_SEGMENTATION_WITH_SURFACES_METADATA",
    "MriEditSegmentationWithSurfacesOutputs",
    "MriEditSegmentationWithSurfacesParameters",
    "mri_edit_segmentation_with_surfaces",
    "mri_edit_segmentation_with_surfaces_params",
]
