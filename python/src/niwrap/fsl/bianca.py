# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BIANCA_METADATA = Metadata(
    id="13866c00abaab58fff532241d5de1e8e8d96e044",
    name="bianca",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class BiancaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bianca(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    base_output: OutputPathType | None
    """Base output file generated by BIANCA"""


def bianca(
    master_file: InputPathType,
    query_subject_num: float | int,
    brain_mask_feature_num: float | int,
    label_feature_num: float | int,
    training_nums: str | None = None,
    load_classifier_data: str | None = None,
    out_name: str | None = "output_bianca",
    feature_subset: str | None = None,
    mat_feature_num: float | int | None = None,
    spatial_weight: float | int | None = 1,
    patch_sizes: str | None = None,
    patch_3d: bool = False,
    select_pts: str | None = "any",
    training_pts: str | None = None,
    non_les_pts: str | None = None,
    save_classifier_data: str | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> BiancaOutputs:
    """
    bianca by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    BIANCA: Brain Intensity AbNormality Classification Algorithm.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BIANCA
    
    Args:
        master_file: Name of the master file.
        query_subject_num: Row number of query subject (in masterlistfile).
        brain_mask_feature_num: Column number (in the master file) of images to\
            derive non-zero mask from.
        label_feature_num: Column number (in the master file) of the manual\
            masks (or any placeholder name for query subjects).
        training_nums: Subjects to be used in training. List of row numbers\
            (comma separated, no spaces) or 'all' to use all the subjects in the\
            master file.
        load_classifier_data: Load training data from file.
        out_name: Specify (base) output name of files.
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
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BiancaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BIANCA_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/bianca")
    cargs.append(
        "--singlefile=" +
        execution.input_file(master_file) +
        ""
    )
    cargs.append(
        "--labelfeaturenum=" +
        str(label_feature_num) +
        ""
    )
    cargs.append(
        "--brainmaskfeaturenum=" +
        str(brain_mask_feature_num) +
        ""
    )
    cargs.append(
        "--querysubjectnum=" +
        str(query_subject_num) +
        ""
    )
    if feature_subset is not None:
        cargs.extend(["--featuresubset", feature_subset])
    if mat_feature_num is not None:
        cargs.extend(["--matfeaturenum", str(mat_feature_num)])
    if spatial_weight is not None:
        cargs.extend(["--spatialweight", str(spatial_weight)])
    if patch_sizes is not None:
        cargs.extend(["--patchsizes", patch_sizes])
    if patch_3d:
        cargs.append("--patch3D")
    if select_pts is not None:
        cargs.extend(["--selectpts", select_pts])
    if training_pts is not None:
        cargs.extend(["--trainingpts", training_pts])
    if non_les_pts is not None:
        cargs.extend(["--nonlespts", non_les_pts])
    if save_classifier_data is not None:
        cargs.extend(["--saveclassifierdata", save_classifier_data])
    if verbose_flag:
        cargs.append("-v")
    cargs.append("-o")
    if out_name is not None:
        cargs.extend(["-o", out_name])
    ret = BiancaOutputs(
        root=execution.output_file("."),
        base_output=execution.output_file(f"{out_name}_bianca", optional=True) if out_name is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BIANCA_METADATA",
    "BiancaOutputs",
    "bianca",
]
