# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__ROI_CORR_MAT_METADATA = Metadata(
    id="d30a28b9afde46895088e3c1489b3ceaf2e8ab86.boutiques",
    name="@ROI_Corr_Mat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VRoiCorrMatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__roi_corr_mat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    matrix_1d: OutputPathType
    """Correlation matrix in .1D format"""
    matrix_brick: OutputPathType
    """Correlation matrix in .BRIK format"""


def v__roi_corr_mat(
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
) -> VRoiCorrMatOutputs:
    """
    Script to produce an NxN ROI correlation matrix of N ROIs.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
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
        NamedTuple of outputs (described in `VRoiCorrMatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ROI_CORR_MAT_METADATA)
    cargs = []
    cargs.append("@ROI_Corr_Mat")
    cargs.extend([
        "-ts",
        execution.input_file(ts_vol)
    ])
    cargs.extend([
        "-roi",
        execution.input_file(roi_vol)
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if roisel is not None:
        cargs.extend([
            "-roisel",
            execution.input_file(roisel)
        ])
    if zval:
        cargs.append("-zval")
    if mat_opt is not None:
        cargs.extend([
            "-mat",
            mat_opt
        ])
    if dirty:
        cargs.append("-dirty")
    if keep_tmp:
        cargs.append("-keep_tmp")
    if echo:
        cargs.append("-echo")
    if verb:
        cargs.append("-verb")
    ret = VRoiCorrMatOutputs(
        root=execution.output_file("."),
        matrix_1d=execution.output_file(prefix + "_matrix.1D"),
        matrix_brick=execution.output_file(prefix + "_matrix.BRIK"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VRoiCorrMatOutputs",
    "V__ROI_CORR_MAT_METADATA",
    "v__roi_corr_mat",
]
