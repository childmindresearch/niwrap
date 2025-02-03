# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DJUNCT_EDGY_ALIGN_CHECK_METADATA = Metadata(
    id="b256b5bb4b47e9c6b85c30cb947f43710826ac49.boutiques",
    name="@djunct_edgy_align_check",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDjunctEdgyAlignCheckParameters = typing.TypedDict('VDjunctEdgyAlignCheckParameters', {
    "__STYX_TYPE__": typing.Literal["@djunct_edgy_align_check"],
    "ULAY": str,
    "OLAY": str,
    "PREFIX": str,
    "set_dicom_xyz": typing.NotRequired[list[float] | None],
    "box_focus_slices": typing.NotRequired[str | None],
    "montgap": typing.NotRequired[float | None],
    "montcolor": typing.NotRequired[str | None],
    "cbar": typing.NotRequired[str | None],
    "save_ftype": typing.NotRequired[str | None],
    "umin_fac": typing.NotRequired[float | None],
    "montx": typing.NotRequired[float | None],
    "monty": typing.NotRequired[float | None],
    "use_olay_grid": typing.NotRequired[str | None],
    "label_mode": typing.NotRequired[str | None],
    "ulay_range": typing.NotRequired[list[float] | None],
    "ulay_range_nz": typing.NotRequired[list[float] | None],
    "ulay_range_am": typing.NotRequired[list[float] | None],
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
        "@djunct_edgy_align_check": v__djunct_edgy_align_check_cargs,
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
    vt = {}
    return vt.get(t)


class VDjunctEdgyAlignCheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_edgy_align_check(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__djunct_edgy_align_check_params(
    ulay: str,
    olay: str,
    prefix: str,
    set_dicom_xyz: list[float] | None = None,
    box_focus_slices: str | None = None,
    montgap: float | None = None,
    montcolor: str | None = None,
    cbar: str | None = None,
    save_ftype: str | None = None,
    umin_fac: float | None = None,
    montx: float | None = None,
    monty: float | None = None,
    use_olay_grid: str | None = None,
    label_mode: str | None = None,
    ulay_range: list[float] | None = None,
    ulay_range_nz: list[float] | None = None,
    ulay_range_am: list[float] | None = None,
) -> VDjunctEdgyAlignCheckParameters:
    """
    Build parameters.
    
    Args:
        ulay: ULAY dataset.
        olay: OLAY dataset.
        prefix: Prefix for output files.
        set_dicom_xyz: DICOM coordinates {XX YY ZZ}.
        box_focus_slices: Dataset to focus slices.
        montgap: Gap between slices in montage.
        montcolor: Color for montage.
        cbar: Color bar for overlay.
        save_ftype: File type to save.
        umin_fac: Scaling factor for underlay minimum.
        montx: Number of slices in X-direction for montage.
        monty: Number of slices in Y-direction for montage.
        use_olay_grid: Grid interpolation method for overlay.
        label_mode: Mode for labeling.
        ulay_range: Range for underlay {umin umax}.
        ulay_range_nz: Range for non-zero underlay {umin umax}.
        ulay_range_am: Range for auto-mask underlay {umin umax}.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@djunct_edgy_align_check",
        "ULAY": ulay,
        "OLAY": olay,
        "PREFIX": prefix,
    }
    if set_dicom_xyz is not None:
        params["set_dicom_xyz"] = set_dicom_xyz
    if box_focus_slices is not None:
        params["box_focus_slices"] = box_focus_slices
    if montgap is not None:
        params["montgap"] = montgap
    if montcolor is not None:
        params["montcolor"] = montcolor
    if cbar is not None:
        params["cbar"] = cbar
    if save_ftype is not None:
        params["save_ftype"] = save_ftype
    if umin_fac is not None:
        params["umin_fac"] = umin_fac
    if montx is not None:
        params["montx"] = montx
    if monty is not None:
        params["monty"] = monty
    if use_olay_grid is not None:
        params["use_olay_grid"] = use_olay_grid
    if label_mode is not None:
        params["label_mode"] = label_mode
    if ulay_range is not None:
        params["ulay_range"] = ulay_range
    if ulay_range_nz is not None:
        params["ulay_range_nz"] = ulay_range_nz
    if ulay_range_am is not None:
        params["ulay_range_am"] = ulay_range_am
    return params


def v__djunct_edgy_align_check_cargs(
    params: VDjunctEdgyAlignCheckParameters,
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
    cargs.append("@djunct_edgy_align_check")
    cargs.append(params.get("ULAY"))
    cargs.append(params.get("OLAY"))
    cargs.append(params.get("PREFIX"))
    if params.get("set_dicom_xyz") is not None:
        cargs.extend(map(str, params.get("set_dicom_xyz")))
    if params.get("box_focus_slices") is not None:
        cargs.append(params.get("box_focus_slices"))
    if params.get("montgap") is not None:
        cargs.append(str(params.get("montgap")))
    if params.get("montcolor") is not None:
        cargs.append(params.get("montcolor"))
    if params.get("cbar") is not None:
        cargs.append(params.get("cbar"))
    if params.get("save_ftype") is not None:
        cargs.append(params.get("save_ftype"))
    if params.get("umin_fac") is not None:
        cargs.append(str(params.get("umin_fac")))
    if params.get("montx") is not None:
        cargs.append(str(params.get("montx")))
    if params.get("monty") is not None:
        cargs.append(str(params.get("monty")))
    if params.get("use_olay_grid") is not None:
        cargs.append(params.get("use_olay_grid"))
    if params.get("label_mode") is not None:
        cargs.append(params.get("label_mode"))
    cargs.append("[help_flag]")
    cargs.append("[ver_flag]")
    cargs.append("[echo_flag]")
    cargs.append("[sharpen_ulay_off_flag]")
    cargs.append("[mask_olay_edges_flag]")
    cargs.append("[no_cor_flag]")
    cargs.append("[no_sag_flag]")
    cargs.append("[no_axi_flag]")
    cargs.append("[no_clean_flag]")
    if params.get("ulay_range") is not None:
        cargs.extend(map(str, params.get("ulay_range")))
    if params.get("ulay_range_nz") is not None:
        cargs.extend(map(str, params.get("ulay_range_nz")))
    if params.get("ulay_range_am") is not None:
        cargs.extend(map(str, params.get("ulay_range_am")))
    return cargs


def v__djunct_edgy_align_check_outputs(
    params: VDjunctEdgyAlignCheckParameters,
    execution: Execution,
) -> VDjunctEdgyAlignCheckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDjunctEdgyAlignCheckOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__djunct_edgy_align_check_execute(
    params: VDjunctEdgyAlignCheckParameters,
    execution: Execution,
) -> VDjunctEdgyAlignCheckOutputs:
    """
    Helper script for various tasks, heavily modeled on RW Cox's '@snapshot_volreg'
    script.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDjunctEdgyAlignCheckOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__djunct_edgy_align_check_cargs(params, execution)
    ret = v__djunct_edgy_align_check_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__djunct_edgy_align_check(
    ulay: str,
    olay: str,
    prefix: str,
    set_dicom_xyz: list[float] | None = None,
    box_focus_slices: str | None = None,
    montgap: float | None = None,
    montcolor: str | None = None,
    cbar: str | None = None,
    save_ftype: str | None = None,
    umin_fac: float | None = None,
    montx: float | None = None,
    monty: float | None = None,
    use_olay_grid: str | None = None,
    label_mode: str | None = None,
    ulay_range: list[float] | None = None,
    ulay_range_nz: list[float] | None = None,
    ulay_range_am: list[float] | None = None,
    runner: Runner | None = None,
) -> VDjunctEdgyAlignCheckOutputs:
    """
    Helper script for various tasks, heavily modeled on RW Cox's '@snapshot_volreg'
    script.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ulay: ULAY dataset.
        olay: OLAY dataset.
        prefix: Prefix for output files.
        set_dicom_xyz: DICOM coordinates {XX YY ZZ}.
        box_focus_slices: Dataset to focus slices.
        montgap: Gap between slices in montage.
        montcolor: Color for montage.
        cbar: Color bar for overlay.
        save_ftype: File type to save.
        umin_fac: Scaling factor for underlay minimum.
        montx: Number of slices in X-direction for montage.
        monty: Number of slices in Y-direction for montage.
        use_olay_grid: Grid interpolation method for overlay.
        label_mode: Mode for labeling.
        ulay_range: Range for underlay {umin umax}.
        ulay_range_nz: Range for non-zero underlay {umin umax}.
        ulay_range_am: Range for auto-mask underlay {umin umax}.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctEdgyAlignCheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_EDGY_ALIGN_CHECK_METADATA)
    params = v__djunct_edgy_align_check_params(ulay=ulay, olay=olay, prefix=prefix, set_dicom_xyz=set_dicom_xyz, box_focus_slices=box_focus_slices, montgap=montgap, montcolor=montcolor, cbar=cbar, save_ftype=save_ftype, umin_fac=umin_fac, montx=montx, monty=monty, use_olay_grid=use_olay_grid, label_mode=label_mode, ulay_range=ulay_range, ulay_range_nz=ulay_range_nz, ulay_range_am=ulay_range_am)
    return v__djunct_edgy_align_check_execute(params, execution)


__all__ = [
    "VDjunctEdgyAlignCheckOutputs",
    "V__DJUNCT_EDGY_ALIGN_CHECK_METADATA",
    "v__djunct_edgy_align_check",
    "v__djunct_edgy_align_check_params",
]
