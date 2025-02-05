# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BIANCA_METADATA = Metadata(
    id="faece12893f9764ba2ed673c9b5a6791f2ed9a43.boutiques",
    name="bianca",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
BiancaParameters = typing.TypedDict('BiancaParameters', {
    "__STYX_TYPE__": typing.Literal["bianca"],
    "master_file": InputPathType,
    "label_feature_num": float,
    "brain_mask_feature_num": float,
    "query_subject_num": float,
    "feature_subset": typing.NotRequired[str | None],
    "mat_feature_num": typing.NotRequired[float | None],
    "spatial_weight": typing.NotRequired[float | None],
    "patch_sizes": typing.NotRequired[str | None],
    "patch_3d": bool,
    "select_pts": typing.NotRequired[str | None],
    "training_pts": typing.NotRequired[str | None],
    "non_les_pts": typing.NotRequired[str | None],
    "save_classifier_data": typing.NotRequired[str | None],
    "verbose_flag": bool,
    "out_name": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "bianca": bianca_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "bianca": bianca_outputs,
    }
    return vt.get(t)


class BiancaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bianca(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    base_output: OutputPathType | None
    """Base output file generated by BIANCA"""


def bianca_params(
    master_file: InputPathType,
    label_feature_num: float,
    brain_mask_feature_num: float,
    query_subject_num: float,
    feature_subset: str | None = None,
    mat_feature_num: float | None = None,
    spatial_weight: float | None = 1,
    patch_sizes: str | None = None,
    patch_3d: bool = False,
    select_pts: str | None = "any",
    training_pts: str | None = None,
    non_les_pts: str | None = None,
    save_classifier_data: str | None = None,
    verbose_flag: bool = False,
    out_name: str | None = "output_bianca",
) -> BiancaParameters:
    """
    Build parameters.
    
    Args:
        master_file: Name of the master file.
        label_feature_num: Column number (in the master file) of the manual\
            masks (or any placeholder name for query subjects).
        brain_mask_feature_num: Column number (in the master file) of images to\
            derive non-zero mask from.
        query_subject_num: Row number of query subject (in masterlistfile).
        feature_subset: Set of column numbers (comma separated and no spaces)\
            for features/images to use (default: use all available modalities as\
            intensity features). The image used to derive non-zero mask from must\
            be part of the features subset.
        mat_feature_num: Column number of matrix files (in masterlistfile).\
            Needed to extract spatial features (MNI coordinates).
        spatial_weight: Weighting for spatial coordinates (default = 1, i.e.,\
            variance-normalized MNI coordinates). Requires --matfeaturenum to be\
            specified.
        patch_sizes: List of patch sizes for local averaging.
        patch_3d: Use 3D patches (default is 2D).
        select_pts: "any" (default) or "surround" or "noborder".
        training_pts: Number (max) of (lesion) points to use (per training\
            subject) or "equalpoints" to select all lesion points and equal number\
            of non-lesion points.
        non_les_pts: Number (max) of non-lesion points to use. If not specified\
            will be set to the same amount of lesion points.
        save_classifier_data: Save training data to file.
        verbose_flag: Use verbose mode.
        out_name: Specify (base) output name of files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bianca",
        "master_file": master_file,
        "label_feature_num": label_feature_num,
        "brain_mask_feature_num": brain_mask_feature_num,
        "query_subject_num": query_subject_num,
        "patch_3d": patch_3d,
        "verbose_flag": verbose_flag,
    }
    if feature_subset is not None:
        params["feature_subset"] = feature_subset
    if mat_feature_num is not None:
        params["mat_feature_num"] = mat_feature_num
    if spatial_weight is not None:
        params["spatial_weight"] = spatial_weight
    if patch_sizes is not None:
        params["patch_sizes"] = patch_sizes
    if select_pts is not None:
        params["select_pts"] = select_pts
    if training_pts is not None:
        params["training_pts"] = training_pts
    if non_les_pts is not None:
        params["non_les_pts"] = non_les_pts
    if save_classifier_data is not None:
        params["save_classifier_data"] = save_classifier_data
    if out_name is not None:
        params["out_name"] = out_name
    return params


def bianca_cargs(
    params: BiancaParameters,
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
    cargs.append("bianca")
    cargs.append("--singlefile=" + execution.input_file(params.get("master_file")))
    cargs.append("--labelfeaturenum=" + str(params.get("label_feature_num")))
    cargs.append("--brainmaskfeaturenum=" + str(params.get("brain_mask_feature_num")))
    cargs.append("--querysubjectnum=" + str(params.get("query_subject_num")))
    if params.get("feature_subset") is not None:
        cargs.extend([
            "--featuresubset",
            params.get("feature_subset")
        ])
    if params.get("mat_feature_num") is not None:
        cargs.extend([
            "--matfeaturenum",
            str(params.get("mat_feature_num"))
        ])
    if params.get("spatial_weight") is not None:
        cargs.extend([
            "--spatialweight",
            str(params.get("spatial_weight"))
        ])
    if params.get("patch_sizes") is not None:
        cargs.extend([
            "--patchsizes",
            params.get("patch_sizes")
        ])
    if params.get("patch_3d"):
        cargs.append("--patch3D")
    if params.get("select_pts") is not None:
        cargs.extend([
            "--selectpts",
            params.get("select_pts")
        ])
    if params.get("training_pts") is not None:
        cargs.extend([
            "--trainingpts",
            params.get("training_pts")
        ])
    if params.get("non_les_pts") is not None:
        cargs.extend([
            "--nonlespts",
            params.get("non_les_pts")
        ])
    if params.get("save_classifier_data") is not None:
        cargs.extend([
            "--saveclassifierdata",
            params.get("save_classifier_data")
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("out_name") is not None:
        cargs.extend([
            "-o",
            params.get("out_name")
        ])
    return cargs


def bianca_outputs(
    params: BiancaParameters,
    execution: Execution,
) -> BiancaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BiancaOutputs(
        root=execution.output_file("."),
        base_output=execution.output_file(params.get("out_name") + "_bianca") if (params.get("out_name") is not None) else None,
    )
    return ret


def bianca_execute(
    params: BiancaParameters,
    execution: Execution,
) -> BiancaOutputs:
    """
    BIANCA: Brain Intensity AbNormality Classification Algorithm.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BiancaOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = bianca_cargs(params, execution)
    ret = bianca_outputs(params, execution)
    execution.run(cargs)
    return ret


def bianca(
    master_file: InputPathType,
    label_feature_num: float,
    brain_mask_feature_num: float,
    query_subject_num: float,
    feature_subset: str | None = None,
    mat_feature_num: float | None = None,
    spatial_weight: float | None = 1,
    patch_sizes: str | None = None,
    patch_3d: bool = False,
    select_pts: str | None = "any",
    training_pts: str | None = None,
    non_les_pts: str | None = None,
    save_classifier_data: str | None = None,
    verbose_flag: bool = False,
    out_name: str | None = "output_bianca",
    runner: Runner | None = None,
) -> BiancaOutputs:
    """
    BIANCA: Brain Intensity AbNormality Classification Algorithm.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        master_file: Name of the master file.
        label_feature_num: Column number (in the master file) of the manual\
            masks (or any placeholder name for query subjects).
        brain_mask_feature_num: Column number (in the master file) of images to\
            derive non-zero mask from.
        query_subject_num: Row number of query subject (in masterlistfile).
        feature_subset: Set of column numbers (comma separated and no spaces)\
            for features/images to use (default: use all available modalities as\
            intensity features). The image used to derive non-zero mask from must\
            be part of the features subset.
        mat_feature_num: Column number of matrix files (in masterlistfile).\
            Needed to extract spatial features (MNI coordinates).
        spatial_weight: Weighting for spatial coordinates (default = 1, i.e.,\
            variance-normalized MNI coordinates). Requires --matfeaturenum to be\
            specified.
        patch_sizes: List of patch sizes for local averaging.
        patch_3d: Use 3D patches (default is 2D).
        select_pts: "any" (default) or "surround" or "noborder".
        training_pts: Number (max) of (lesion) points to use (per training\
            subject) or "equalpoints" to select all lesion points and equal number\
            of non-lesion points.
        non_les_pts: Number (max) of non-lesion points to use. If not specified\
            will be set to the same amount of lesion points.
        save_classifier_data: Save training data to file.
        verbose_flag: Use verbose mode.
        out_name: Specify (base) output name of files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BiancaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BIANCA_METADATA)
    params = bianca_params(master_file=master_file, label_feature_num=label_feature_num, brain_mask_feature_num=brain_mask_feature_num, query_subject_num=query_subject_num, feature_subset=feature_subset, mat_feature_num=mat_feature_num, spatial_weight=spatial_weight, patch_sizes=patch_sizes, patch_3d=patch_3d, select_pts=select_pts, training_pts=training_pts, non_les_pts=non_les_pts, save_classifier_data=save_classifier_data, verbose_flag=verbose_flag, out_name=out_name)
    return bianca_execute(params, execution)


__all__ = [
    "BIANCA_METADATA",
    "BiancaOutputs",
    "BiancaParameters",
    "bianca",
    "bianca_params",
]
