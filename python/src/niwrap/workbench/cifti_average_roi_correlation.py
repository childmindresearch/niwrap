# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_AVERAGE_ROI_CORRELATION_METADATA = Metadata(
    id="4e93dbb235efd9147415e8e4f6af7d0489e693d7",
    name="cifti-average-roi-correlation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiAverageRoiCorrelationCiftiRoi:
    """
    cifti file containing combined weights
    """
    opt_in_memory: bool = False
    """cache the roi in memory so that it isn't re-read for each input cifti"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        if self.opt_in_memory:
            cargs.append("-in-memory")
        return cargs


@dataclasses.dataclass
class CiftiAverageRoiCorrelationCifti:
    """
    specify an input cifti file
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


class CiftiAverageRoiCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average_roi_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_average_roi_correlation(
    cifti_out: InputPathType,
    cifti_roi: CiftiAverageRoiCorrelationCiftiRoi | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    opt_left_area_surf_left_surf: InputPathType | None = None,
    opt_right_area_surf_right_surf: InputPathType | None = None,
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None,
    cifti: list[CiftiAverageRoiCorrelationCifti] = None,
    runner: Runner = None,
) -> CiftiAverageRoiCorrelationOutputs:
    """
    cifti-average-roi-correlation by Washington University School of Medicin.
    
    Correlate roi average with all rows then average across subjects.
    
    Averages rows for each map of the ROI(s), takes the correlation of each ROI
    average to the rest of the rows in the same file, applies the fisher small z
    transform, then averages the results across all files. ROIs are always
    treated as weighting functions, including negative values. For efficiency,
    ensure that everything that is not intended to be used is zero in the ROI
    map. If -cifti-roi is specified, -left-roi, -right-roi, -cerebellum-roi, and
    -vol-roi must not be specified. If multiple non-cifti ROI files are
    specified, they must have the same number of columns.
    
    Args:
        cifti_out: output cifti file.
        cifti_roi: cifti file containing combined weights.
        opt_left_roi_roi_metric: weights to use for left hempsphere: the left\
            roi as a metric file.
        opt_right_roi_roi_metric: weights to use for right hempsphere: the\
            right roi as a metric file.
        opt_cerebellum_roi_roi_metric: weights to use for cerebellum surface:\
            the cerebellum roi as a metric file.
        opt_vol_roi_roi_vol: voxel weights to use: the roi volume file.
        opt_left_area_surf_left_surf: specify the left surface for vertex area\
            correction: the left surface file.
        opt_right_area_surf_right_surf: specify the right surface for vertex\
            area correction: the right surface file.
        opt_cerebellum_area_surf_cerebellum_surf: specify the cerebellum\
            surface for vertex area correction: the cerebellum surface file.
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiAverageRoiCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_AVERAGE_ROI_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-average-roi-correlation")
    cargs.append(execution.input_file(cifti_out))
    if cifti_roi is not None:
        cargs.extend(["-cifti-roi", *cifti_roi.run(execution)])
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
    if cifti is not None:
        cargs.extend(["-cifti", *[a for c in [s.run(execution) for s in cifti] for a in c]])
    ret = CiftiAverageRoiCorrelationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_AVERAGE_ROI_CORRELATION_METADATA",
    "CiftiAverageRoiCorrelationCifti",
    "CiftiAverageRoiCorrelationCiftiRoi",
    "CiftiAverageRoiCorrelationOutputs",
    "cifti_average_roi_correlation",
]