# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ROI_CORR_MAT_METADATA = Metadata(
    id="91bac0506bf3240099589fe71e983e19e3deb671",
    name="ROI_Corr_Mat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class RoiCorrMatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `roi_corr_mat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    matrix_1d: OutputPathType
    """Correlation matrix in .1D format"""
    matrix_brick: OutputPathType
    """Correlation matrix in .BRIK format"""


def roi_corr_mat(
    ts_vol: InputPathType,
    roi_vol: InputPathType,
    prefix: str,
    roisel: InputPathType | None = None,
    zval: bool = False,
    mat_opt: str | None = None,
    dirty: bool = False,
    keep_tmp: bool = False,
    echo: bool = False,
    verb: bool = False,
    runner: Runner | None = None,
) -> RoiCorrMatOutputs:
    """
    ROI_Corr_Mat by AFNI Team.
    
    Script to produce an NxN ROI correlation matrix of N ROIs.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ROI_Corr_Mat.html
    
    Args:
        ts_vol: Time series volume.
        roi_vol: ROI volume.
        prefix: Use output for a prefix.
        roisel: Force processing of ROI label (integers) listed in ROISEL 1D\
            file.
        zval: Output a zscore version of the correlation matrix.
        mat_opt: Output matrix in different manners.
        dirty: Keep temporary files.
        keep_tmp: Keep temporary files.
        echo: Set echo (echo all commands to screen).
        verb: Verbose flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RoiCorrMatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ROI_CORR_MAT_METADATA)
    cargs = []
    cargs.append("@ROI_Corr_Mat")
    cargs.append("<-ts")
    cargs.append("TimeSeriesVol>")
    cargs.append("<-roi")
    cargs.append("ROIVol>")
    cargs.append("<-prefix")
    cargs.append("output>")
    cargs.append("[<-roisel")
    cargs.append("ROISEL>]")
    cargs.append("[-zval]")
    cargs.append("[-mat")
    cargs.append("FULL,")
    cargs.append("TRI,")
    cargs.append("TRI_ND]")
    cargs.append("[-verb]")
    cargs.append("[-dirty]")
    ret = RoiCorrMatOutputs(
        root=execution.output_file("."),
        matrix_1d=execution.output_file(f"{prefix}_matrix.1D", optional=True),
        matrix_brick=execution.output_file(f"{prefix}_matrix.BRIK", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ROI_CORR_MAT_METADATA",
    "RoiCorrMatOutputs",
    "roi_corr_mat",
]
