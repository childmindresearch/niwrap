# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DJUNCT_OVERLAP_CHECK_METADATA = Metadata(
    id="61eef1d6dc1535a1dc4452ab3c3b8b5da02a1e6d.boutiques",
    name="@djunct_overlap_check",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VDjunctOverlapCheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_overlap_check(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__djunct_overlap_check(
    ulay: InputPathType,
    olay: InputPathType,
    prefix: str,
    box_focus_slices: InputPathType | None = None,
    montgap: float | None = None,
    montcolor: str | None = None,
    cbar: str | None = None,
    opacity: float | None = None,
    zerocolor: str | None = None,
    set_dicom_xyz: list[float] | None = None,
    ulay_range: list[float] | None = None,
    ulay_range_nz: list[float] | None = None,
    montx: float | None = None,
    monty: float | None = None,
    montx_cat: float | None = None,
    monty_cat: float | None = None,
    label_mode: str | None = None,
    pbar_posonly_off: bool = False,
    edgy_ulay: bool = False,
    set_dicom_xyz_off: bool = False,
    no_cor: bool = False,
    no_axi: bool = False,
    no_sag: bool = False,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> VDjunctOverlapCheckOutputs:
    """
    A helper script for visualizing overlap between datasets in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ulay: Dataset to use as the underlay (background).
        olay: Dataset to use as the overlay (foreground).
        prefix: Prefix for the output files.
        box_focus_slices: Dataset for box focus slices.
        montgap: Gap between montage slices.
        montcolor: Color of the montage gap.
        cbar: Colorbar for the overlay.
        opacity: Opacity of the overlay.
        zerocolor: Color for zero values.
        set_dicom_xyz: Set DICOM coordinates for slice location.
        ulay_range: Range for underlay values.
        ulay_range_nz: Range for non-zero underlay values.
        montx: Number of panels in X direction in montage.
        monty: Number of panels in Y direction in montage.
        montx_cat: Number of X panes per image in montage.
        monty_cat: Number of Y panes per image in montage.
        label_mode: Label mode.
        pbar_posonly_off: Turn off position-only p-bar.
        edgy_ulay: Edgify the underlay.
        set_dicom_xyz_off: Turn off DICOM coordinates setting.
        no_cor: Skip coronal slices.
        no_axi: Skip axial slices.
        no_sag: Skip sagittal slices.
        no_clean: Do not clean up temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctOverlapCheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_OVERLAP_CHECK_METADATA)
    cargs = []
    cargs.append("@djunct_overlap_check")
    cargs.append(execution.input_file(ulay))
    cargs.append(execution.input_file(olay))
    cargs.append(prefix)
    if box_focus_slices is not None:
        cargs.append(execution.input_file(box_focus_slices))
    if montgap is not None:
        cargs.extend([
            "-montgap",
            str(montgap)
        ])
    if montcolor is not None:
        cargs.extend([
            "-montcolor",
            montcolor
        ])
    if cbar is not None:
        cargs.extend([
            "-cbar",
            cbar
        ])
    if opacity is not None:
        cargs.extend([
            "-opacity",
            str(opacity)
        ])
    if zerocolor is not None:
        cargs.extend([
            "-zerocolor",
            zerocolor
        ])
    if set_dicom_xyz is not None:
        cargs.extend([
            "-set_dicom_xyz",
            *map(str, set_dicom_xyz)
        ])
    if ulay_range is not None:
        cargs.extend([
            "-ulay_range",
            *map(str, ulay_range)
        ])
    if ulay_range_nz is not None:
        cargs.extend([
            "-ulay_range_nz",
            *map(str, ulay_range_nz)
        ])
    if montx is not None:
        cargs.extend([
            "-montx",
            str(montx)
        ])
    if monty is not None:
        cargs.extend([
            "-monty",
            str(monty)
        ])
    if montx_cat is not None:
        cargs.extend([
            "-montx_cat",
            str(montx_cat)
        ])
    if monty_cat is not None:
        cargs.extend([
            "-monty_cat",
            str(monty_cat)
        ])
    if label_mode is not None:
        cargs.extend([
            "-label_mode",
            label_mode
        ])
    if pbar_posonly_off:
        cargs.append("-pbar_posonly_off")
    if edgy_ulay:
        cargs.append("-edgy_ulay")
    if set_dicom_xyz_off:
        cargs.append("-set_dicom_xyz_off")
    if no_cor:
        cargs.append("-no_cor")
    if no_axi:
        cargs.append("-no_axi")
    if no_sag:
        cargs.append("-no_sag")
    if no_clean:
        cargs.append("-no_clean")
    ret = VDjunctOverlapCheckOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDjunctOverlapCheckOutputs",
    "V__DJUNCT_OVERLAP_CHECK_METADATA",
    "v__djunct_overlap_check",
]
