# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.865331

import typing

from ..styxdefs import *


CIFTI_AVERAGE_ROI_CORRELATION_METADATA = Metadata(
    id="9f0077cce5178429a78be7ace4d618cec77c5a42",
    name="cifti-average-roi-correlation",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiAverageRoiCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average_roi_correlation(...)`.
    """
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_average_roi_correlation(
    runner: Runner,
    cifti_out: InputPathType,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    opt_left_area_surf_left_surf: InputPathType | None = None,
    opt_right_area_surf_right_surf: InputPathType | None = None,
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None,
    opt_cifti_cifti_in: InputPathType | None = None,
) -> CiftiAverageRoiCorrelationOutputs:
    """
    CORRELATE ROI AVERAGE WITH ALL ROWS THEN AVERAGE ACROSS SUBJECTS.
    
    Averages rows for each map of the ROI(s), takes the correlation of each ROI
    average to the rest of the rows in the same file, applies the fisher small z
    transform, then averages the results across all files. ROIs are always
    treated as weighting functions, including negative values. For efficiency,
    ensure that everything that is not intended to be used is zero in the ROI
    map. If -cifti-roi is specified, -left-roi, -right-roi, -cerebellum-roi, and
    -vol-roi must not be specified. If multiple non-cifti ROI files are
    specified, they must have the same number of columns.
    
    Args:
        runner: Command runner
        cifti_out: output cifti file
        opt_cifti_roi_roi_cifti: cifti file containing combined weights: the roi
            cifti file
        opt_left_roi_roi_metric: weights to use for left hempsphere: the left
            roi as a metric file
        opt_right_roi_roi_metric: weights to use for right hempsphere: the right
            roi as a metric file
        opt_cerebellum_roi_roi_metric: weights to use for cerebellum surface:
            the cerebellum roi as a metric file
        opt_vol_roi_roi_vol: voxel weights to use: the roi volume file
        opt_left_area_surf_left_surf: specify the left surface for vertex area
            correction: the left surface file
        opt_right_area_surf_right_surf: specify the right surface for vertex
            area correction: the right surface file
        opt_cerebellum_area_surf_cerebellum_surf: specify the cerebellum surface
            for vertex area correction: the cerebellum surface file
        opt_cifti_cifti_in: specify an input cifti file: a cifti file to average
            across
    Returns:
        NamedTuple of outputs (described in `CiftiAverageRoiCorrelationOutputs`).
    """
    execution = runner.start_execution(CIFTI_AVERAGE_ROI_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-average-roi-correlation")
    cargs.append(execution.input_file(cifti_out))
    if opt_cifti_roi_roi_cifti is not None:
        cargs.extend(["-cifti-roi", execution.input_file(opt_cifti_roi_roi_cifti)])
    if opt_left_roi_roi_metric is not None:
        cargs.extend(["-left-roi", execution.input_file(opt_left_roi_roi_metric)])
    if opt_right_roi_roi_metric is not None:
        cargs.extend(["-right-roi", execution.input_file(opt_right_roi_roi_metric)])
    if opt_cerebellum_roi_roi_metric is not None:
        cargs.extend(["-cerebellum-roi", execution.input_file(opt_cerebellum_roi_roi_metric)])
    if opt_vol_roi_roi_vol is not None:
        cargs.extend(["-vol-roi", execution.input_file(opt_vol_roi_roi_vol)])
    if opt_left_area_surf_left_surf is not None:
        cargs.extend(["-left-area-surf", execution.input_file(opt_left_area_surf_left_surf)])
    if opt_right_area_surf_right_surf is not None:
        cargs.extend(["-right-area-surf", execution.input_file(opt_right_area_surf_right_surf)])
    if opt_cerebellum_area_surf_cerebellum_surf is not None:
        cargs.extend(["-cerebellum-area-surf", execution.input_file(opt_cerebellum_area_surf_cerebellum_surf)])
    if opt_cifti_cifti_in is not None:
        cargs.extend(["-cifti", execution.input_file(opt_cifti_cifti_in)])
    ret = CiftiAverageRoiCorrelationOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret
