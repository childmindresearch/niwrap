# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DUAL_REGRESSION_METADATA = Metadata(
    id="4ca133e6806abb8249af8771d3f5b7613b9bab63.boutiques",
    name="dual_regression",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class DualRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dual_regression(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stage1_output: OutputPathType
    """Output from stage 1 for each subject"""
    stage2_output: OutputPathType
    """Output from stage 2 for each subject"""
    stage3_output: OutputPathType
    """Output from stage 3 for each subject"""
    randomise_output: OutputPathType
    """Output of randomise"""


def dual_regression(
    group_ic_maps: InputPathType,
    des_norm: float,
    design_mat: InputPathType,
    design_con: InputPathType,
    n_perm: float,
    output_directory: str,
    input_files: list[InputPathType],
    thr_flag: bool = False,
    runner: Runner | None = None,
) -> DualRegressionOutputs:
    """
    Dual regression algorithm to investigate group-ICA results.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        group_ic_maps: 4D image containing spatial IC maps (melodic_IC) from\
            the whole-group ICA analysis.
        des_norm: 0 or 1 (1 is recommended). Whether to variance-normalise the\
            timecourses used as the stage-2 regressors.
        design_mat: Design matrix for final cross-subject modelling with\
            randomise.
        design_con: Design contrasts for final cross-subject modelling with\
            randomise.
        n_perm: Number of permutations for randomise; set to 1 for just raw\
            tstat output, set to 0 to not run randomise at all.
        output_directory: This directory will be created to hold all output and\
            logfiles.
        input_files: List of all subjects' preprocessed, standard-space 4D\
            datasets.
        thr_flag: Perform thresholded dual regression to obtain unbiased\
            timeseries for connectomics analyses (e.g., with FSLnets).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DualRegressionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DUAL_REGRESSION_METADATA)
    cargs = []
    cargs.append("dual_regression")
    cargs.append(execution.input_file(group_ic_maps))
    cargs.append(str(des_norm))
    cargs.append(execution.input_file(design_mat))
    cargs.append(execution.input_file(design_con))
    cargs.append(str(n_perm))
    if thr_flag:
        cargs.append("--thr")
    cargs.append(output_directory)
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = DualRegressionOutputs(
        root=execution.output_file("."),
        stage1_output=execution.output_file(output_directory + "/dr_stage1_subject[SUBJECT_INDEX].nii.gz"),
        stage2_output=execution.output_file(output_directory + "/dr_stage2_subject[SUBJECT_INDEX].nii.gz"),
        stage3_output=execution.output_file(output_directory + "/dr_stage3_subject[SUBJECT_INDEX].nii.gz"),
        randomise_output=execution.output_file(output_directory + "/dr_randomise"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DUAL_REGRESSION_METADATA",
    "DualRegressionOutputs",
    "dual_regression",
]
