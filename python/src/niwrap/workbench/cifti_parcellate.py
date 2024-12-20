# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_PARCELLATE_METADATA = Metadata(
    id="f83818e02af7839749e8a5ba0f709f710eeb6881.boutiques",
    name="cifti-parcellate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiParcellateSpatialWeights:
    """
    use voxel volume and either vertex areas or metric files as weights.
    """
    opt_left_area_surf_left_surf: InputPathType | None = None
    """use a surface for left vertex areas: the left surface to use, areas are
    in mm^2"""
    opt_right_area_surf_right_surf: InputPathType | None = None
    """use a surface for right vertex areas: the right surface to use, areas are
    in mm^2"""
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None
    """use a surface for cerebellum vertex areas: the cerebellum surface to use,
    areas are in mm^2"""
    opt_left_area_metric_left_metric: InputPathType | None = None
    """use a metric file for left vertex weights: metric file containing left
    vertex weights"""
    opt_right_area_metric_right_metric: InputPathType | None = None
    """use a metric file for right vertex weights: metric file containing right
    vertex weights"""
    opt_cerebellum_area_metric_cerebellum_metric: InputPathType | None = None
    """use a metric file for cerebellum vertex weights: metric file containing
    cerebellum vertex weights"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-spatial-weights")
        if self.opt_left_area_surf_left_surf is not None:
            cargs.extend([
                "-left-area-surf",
                execution.input_file(self.opt_left_area_surf_left_surf)
            ])
        if self.opt_right_area_surf_right_surf is not None:
            cargs.extend([
                "-right-area-surf",
                execution.input_file(self.opt_right_area_surf_right_surf)
            ])
        if self.opt_cerebellum_area_surf_cerebellum_surf is not None:
            cargs.extend([
                "-cerebellum-area-surf",
                execution.input_file(self.opt_cerebellum_area_surf_cerebellum_surf)
            ])
        if self.opt_left_area_metric_left_metric is not None:
            cargs.extend([
                "-left-area-metric",
                execution.input_file(self.opt_left_area_metric_left_metric)
            ])
        if self.opt_right_area_metric_right_metric is not None:
            cargs.extend([
                "-right-area-metric",
                execution.input_file(self.opt_right_area_metric_right_metric)
            ])
        if self.opt_cerebellum_area_metric_cerebellum_metric is not None:
            cargs.extend([
                "-cerebellum-area-metric",
                execution.input_file(self.opt_cerebellum_area_metric_cerebellum_metric)
            ])
        return cargs


@dataclasses.dataclass
class CiftiParcellateExcludeOutliers:
    """
    exclude non-numeric values and outliers from each parcel by standard
    deviation.
    """
    sigma_below: float
    """number of standard deviations below the mean to include"""
    sigma_above: float
    """number of standard deviations above the mean to include"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-exclude-outliers")
        cargs.append(str(self.sigma_below))
        cargs.append(str(self.sigma_above))
        return cargs


class CiftiParcellateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_parcellate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""
    opt_nonempty_mask_out_mask_out: OutputPathType | None
    """output a matching pscalar file that has 0s in empty parcels, and 1s
    elsewhere: the output mask file"""


def cifti_parcellate(
    cifti_in: InputPathType,
    cifti_label: InputPathType,
    direction: str,
    cifti_out: str,
    spatial_weights: CiftiParcellateSpatialWeights | None = None,
    opt_cifti_weights_weight_cifti: InputPathType | None = None,
    opt_method_method: str | None = None,
    exclude_outliers: CiftiParcellateExcludeOutliers | None = None,
    opt_only_numeric: bool = False,
    opt_fill_value_value: float | None = None,
    opt_nonempty_mask_out_mask_out: str | None = None,
    opt_legacy_mode: bool = False,
    opt_include_empty: bool = False,
    runner: Runner | None = None,
) -> CiftiParcellateOutputs:
    """
    Parcellate a cifti file.
    
    Each label (other than the unlabeled key) in the cifti label file will be
    treated as a parcel, and all rows or columns of data within the parcel are
    averaged together to form the parcel's output row or column. If -legacy-mode
    is specified, parcels will be defined as the overlap between a label and the
    data, with no errors for missing data vertices or voxels, and empty parcels
    discarded. The direction can be either an integer starting from 1, or the
    strings 'ROW' or 'COLUMN'. For dtseries or dscalar, use COLUMN. If you are
    parcellating a dconn in both directions, parcellating by ROW first will use
    much less memory.
    
    NOTE: the parcels in the output file are sorted by the numeric label keys,
    in ascending order.
    
    The parameter to the -method option must be one of the following:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    
    The -*-weights options are mutually exclusive and may only be used with MEAN
    (default), SUM, STDEV, SAMPSTDEV, VARIANCE, MEDIAN, or MODE (default for
    label data).
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the cifti file to parcellate.
        cifti_label: a cifti label file to use for the parcellation.
        direction: which mapping to parcellate (integer, ROW, or COLUMN).
        cifti_out: output cifti file.
        spatial_weights: use voxel volume and either vertex areas or metric\
            files as weights.
        opt_cifti_weights_weight_cifti: use a cifti file containing weights:\
            the weights to use, as a cifti file.
        opt_method_method: specify method of parcellation (default MEAN, or\
            MODE if label data): the method to use to assign parcel values from the\
            values of member brainordinates.
        exclude_outliers: exclude non-numeric values and outliers from each\
            parcel by standard deviation.
        opt_only_numeric: exclude non-numeric values.
        opt_fill_value_value: specify value to use in empty parcels (default\
            0): the value to fill empty parcels with.
        opt_nonempty_mask_out_mask_out: output a matching pscalar file that has\
            0s in empty parcels, and 1s elsewhere: the output mask file.
        opt_legacy_mode: use the old behavior, parcels are defined by the\
            intersection between labels and valid data, and empty parcels are\
            discarded.
        opt_include_empty: deprecated: now the default behavior.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiParcellateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_PARCELLATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-parcellate")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(execution.input_file(cifti_label))
    cargs.append(direction)
    cargs.append(cifti_out)
    if spatial_weights is not None:
        cargs.extend(spatial_weights.run(execution))
    if opt_cifti_weights_weight_cifti is not None:
        cargs.extend([
            "-cifti-weights",
            execution.input_file(opt_cifti_weights_weight_cifti)
        ])
    if opt_method_method is not None:
        cargs.extend([
            "-method",
            opt_method_method
        ])
    if exclude_outliers is not None:
        cargs.extend(exclude_outliers.run(execution))
    if opt_only_numeric:
        cargs.append("-only-numeric")
    if opt_fill_value_value is not None:
        cargs.extend([
            "-fill-value",
            str(opt_fill_value_value)
        ])
    if opt_nonempty_mask_out_mask_out is not None:
        cargs.extend([
            "-nonempty-mask-out",
            opt_nonempty_mask_out_mask_out
        ])
    if opt_legacy_mode:
        cargs.append("-legacy-mode")
    if opt_include_empty:
        cargs.append("-include-empty")
    ret = CiftiParcellateOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
        opt_nonempty_mask_out_mask_out=execution.output_file(opt_nonempty_mask_out_mask_out) if (opt_nonempty_mask_out_mask_out is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_PARCELLATE_METADATA",
    "CiftiParcellateExcludeOutliers",
    "CiftiParcellateOutputs",
    "CiftiParcellateSpatialWeights",
    "cifti_parcellate",
]
