# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FUGUE_METADATA = Metadata(
    id="e92886e40bebff1fca6ad036e63b3a6f487c4e4c.boutiques",
    name="fugue",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FugueParameters = typing.TypedDict('FugueParameters', {
    "__STYX_TYPE__": typing.Literal["fugue"],
    "asym_se_time": typing.NotRequired[float | None],
    "despike_2dfilter": bool,
    "despike_threshold": typing.NotRequired[float | None],
    "dwell_time": typing.NotRequired[float | None],
    "dwell_to_asym_ratio": typing.NotRequired[float | None],
    "fmap_in_file": typing.NotRequired[InputPathType | None],
    "fmap_out_file": typing.NotRequired[str | None],
    "forward_warping": bool,
    "fourier_order": typing.NotRequired[int | None],
    "icorr": bool,
    "icorr_only": bool,
    "in_file": typing.NotRequired[InputPathType | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "median_2dfilter": bool,
    "no_extend": bool,
    "no_gap_fill": bool,
    "nokspace": bool,
    "output_type": typing.NotRequired[typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None],
    "pava": bool,
    "phase_conjugate": bool,
    "phasemap_in_file": typing.NotRequired[InputPathType | None],
    "poly_order": typing.NotRequired[int | None],
    "save_fmap": bool,
    "save_shift": bool,
    "save_unmasked_fmap": bool,
    "save_unmasked_shift": bool,
    "shift_in_file": typing.NotRequired[InputPathType | None],
    "shift_out_file": typing.NotRequired[str | None],
    "smooth2d": typing.NotRequired[float | None],
    "smooth3d": typing.NotRequired[float | None],
    "unwarp_direction": typing.NotRequired[typing.Literal["x", "y", "z", "x-", "y-", "z-"] | None],
    "unwarped_file": typing.NotRequired[str | None],
    "warped_file": typing.NotRequired[str | None],
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
        "fugue": fugue_cargs,
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
        "fugue": fugue_outputs,
    }
    return vt.get(t)


class FugueOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fugue(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fmap_out_file_outfile: OutputPathType | None
    """Fieldmap file."""
    shift_out_file_outfile: OutputPathType | None
    """Voxel shift map file."""
    unwarped_file_outfile: OutputPathType | None
    """Unwarped file."""
    warped_file_outfile: OutputPathType | None
    """Forward warped file."""


def fugue_params(
    asym_se_time: float | None = None,
    despike_2dfilter: bool = False,
    despike_threshold: float | None = None,
    dwell_time: float | None = None,
    dwell_to_asym_ratio: float | None = None,
    fmap_in_file: InputPathType | None = None,
    fmap_out_file: str | None = None,
    forward_warping: bool = False,
    fourier_order: int | None = None,
    icorr: bool = False,
    icorr_only: bool = False,
    in_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    median_2dfilter: bool = False,
    no_extend: bool = False,
    no_gap_fill: bool = False,
    nokspace: bool = False,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    pava: bool = False,
    phase_conjugate: bool = False,
    phasemap_in_file: InputPathType | None = None,
    poly_order: int | None = None,
    save_fmap: bool = False,
    save_shift: bool = False,
    save_unmasked_fmap: bool = False,
    save_unmasked_shift: bool = False,
    shift_in_file: InputPathType | None = None,
    shift_out_file: str | None = None,
    smooth2d: float | None = None,
    smooth3d: float | None = None,
    unwarp_direction: typing.Literal["x", "y", "z", "x-", "y-", "z-"] | None = None,
    unwarped_file: str | None = None,
    warped_file: str | None = None,
) -> FugueParameters:
    """
    Build parameters.
    
    Args:
        asym_se_time: Set the fieldmap asymmetric spin echo time (sec).
        despike_2dfilter: Apply a 2d de-spiking filter.
        despike_threshold: Specify the threshold for de-spiking (default=3.0).
        dwell_time: Set the epi dwell time per phase-encode line - same as echo\
            spacing - (sec).
        dwell_to_asym_ratio: Set the dwell to asym time ratio.
        fmap_in_file: Filename for loading fieldmap (rad/s).
        fmap_out_file: Filename for saving fieldmap (rad/s).
        forward_warping: Apply forward warping instead of unwarping.
        fourier_order: Apply fourier (sinusoidal) fitting of order n.
        icorr: Apply intensity correction to unwarping (pixel shift method\
            only).
        icorr_only: Apply intensity correction only.
        in_file: Filename of input volume.
        mask_file: Filename for loading valid mask.
        median_2dfilter: Apply 2d median filtering.
        no_extend: Do not apply rigid-body extrapolation to the fieldmap.
        no_gap_fill: Do not apply gap-filling measure to the fieldmap.
        nokspace: Do not use k-space forward warping.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        pava: Apply monotonic enforcement via pava.
        phase_conjugate: Apply phase conjugate method of unwarping.
        phasemap_in_file: Filename for input phase image.
        poly_order: Apply polynomial fitting of order n.
        save_fmap: Write field map volume.
        save_shift: Write pixel shift volume.
        save_unmasked_fmap: Saves the unmasked fieldmap when using --savefmap.
        save_unmasked_shift: Saves the unmasked shiftmap when using\
            --saveshift.
        shift_in_file: Filename for reading pixel shift volume.
        shift_out_file: Filename for saving pixel shift volume.
        smooth2d: Apply 2d gaussian smoothing of sigma n (in mm).
        smooth3d: Apply 3d gaussian smoothing of sigma n (in mm).
        unwarp_direction: 'x' or 'y' or 'z' or 'x-' or 'y-' or 'z-'. Specifies\
            direction of warping (default y).
        unwarped_file: Apply unwarping and save as filename.
        warped_file: Apply forward warping and save as filename.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fugue",
        "despike_2dfilter": despike_2dfilter,
        "forward_warping": forward_warping,
        "icorr": icorr,
        "icorr_only": icorr_only,
        "median_2dfilter": median_2dfilter,
        "no_extend": no_extend,
        "no_gap_fill": no_gap_fill,
        "nokspace": nokspace,
        "pava": pava,
        "phase_conjugate": phase_conjugate,
        "save_fmap": save_fmap,
        "save_shift": save_shift,
        "save_unmasked_fmap": save_unmasked_fmap,
        "save_unmasked_shift": save_unmasked_shift,
    }
    if asym_se_time is not None:
        params["asym_se_time"] = asym_se_time
    if despike_threshold is not None:
        params["despike_threshold"] = despike_threshold
    if dwell_time is not None:
        params["dwell_time"] = dwell_time
    if dwell_to_asym_ratio is not None:
        params["dwell_to_asym_ratio"] = dwell_to_asym_ratio
    if fmap_in_file is not None:
        params["fmap_in_file"] = fmap_in_file
    if fmap_out_file is not None:
        params["fmap_out_file"] = fmap_out_file
    if fourier_order is not None:
        params["fourier_order"] = fourier_order
    if in_file is not None:
        params["in_file"] = in_file
    if mask_file is not None:
        params["mask_file"] = mask_file
    if output_type is not None:
        params["output_type"] = output_type
    if phasemap_in_file is not None:
        params["phasemap_in_file"] = phasemap_in_file
    if poly_order is not None:
        params["poly_order"] = poly_order
    if shift_in_file is not None:
        params["shift_in_file"] = shift_in_file
    if shift_out_file is not None:
        params["shift_out_file"] = shift_out_file
    if smooth2d is not None:
        params["smooth2d"] = smooth2d
    if smooth3d is not None:
        params["smooth3d"] = smooth3d
    if unwarp_direction is not None:
        params["unwarp_direction"] = unwarp_direction
    if unwarped_file is not None:
        params["unwarped_file"] = unwarped_file
    if warped_file is not None:
        params["warped_file"] = warped_file
    return params


def fugue_cargs(
    params: FugueParameters,
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
    cargs.append("fugue")
    if params.get("asym_se_time") is not None:
        cargs.append("--asym=" + str(params.get("asym_se_time")))
    if params.get("despike_2dfilter"):
        cargs.append("--despike")
    if params.get("despike_threshold") is not None:
        cargs.append("--despikethreshold=" + str(params.get("despike_threshold")))
    if params.get("dwell_time") is not None:
        cargs.append("--dwell=" + str(params.get("dwell_time")))
    if params.get("dwell_to_asym_ratio") is not None:
        cargs.append("--dwelltoasym=" + str(params.get("dwell_to_asym_ratio")))
    if params.get("fmap_in_file") is not None:
        cargs.append("--loadfmap=" + execution.input_file(params.get("fmap_in_file")))
    if params.get("fmap_out_file") is not None:
        cargs.append("--savefmap=" + params.get("fmap_out_file"))
    if params.get("forward_warping"):
        cargs.append("--forward_warping")
    if params.get("fourier_order") is not None:
        cargs.append("--fourier=" + str(params.get("fourier_order")))
    if params.get("icorr"):
        cargs.append("--icorr")
    if params.get("icorr_only"):
        cargs.append("--icorronly")
    if params.get("in_file") is not None:
        cargs.append("--in=" + execution.input_file(params.get("in_file")))
    if params.get("mask_file") is not None:
        cargs.append("--mask=" + execution.input_file(params.get("mask_file")))
    if params.get("median_2dfilter"):
        cargs.append("--median")
    if params.get("no_extend"):
        cargs.append("--noextend")
    if params.get("no_gap_fill"):
        cargs.append("--nofill")
    if params.get("nokspace"):
        cargs.append("--nokspace")
    if params.get("output_type") is not None:
        cargs.append(params.get("output_type"))
    if params.get("pava"):
        cargs.append("--pava")
    if params.get("phase_conjugate"):
        cargs.append("--phaseconj")
    if params.get("phasemap_in_file") is not None:
        cargs.append("--phasemap=" + execution.input_file(params.get("phasemap_in_file")))
    if params.get("poly_order") is not None:
        cargs.append("--poly=" + str(params.get("poly_order")))
    if params.get("save_fmap"):
        cargs.append("--save_fmap")
    if params.get("save_shift"):
        cargs.append("--save_shift")
    if params.get("save_unmasked_fmap"):
        cargs.append("--unmaskfmap")
    if params.get("save_unmasked_shift"):
        cargs.append("--unmaskshift")
    if params.get("shift_in_file") is not None:
        cargs.append("--loadshift=" + execution.input_file(params.get("shift_in_file")))
    if params.get("shift_out_file") is not None:
        cargs.append("--saveshift=" + params.get("shift_out_file"))
    if params.get("smooth2d") is not None:
        cargs.append("--smooth2=" + str(params.get("smooth2d")))
    if params.get("smooth3d") is not None:
        cargs.append("--smooth3=" + str(params.get("smooth3d")))
    if params.get("unwarp_direction") is not None:
        cargs.append("--unwarpdir=" + params.get("unwarp_direction"))
    if params.get("unwarped_file") is not None:
        cargs.append("--unwarp=" + params.get("unwarped_file"))
    if params.get("warped_file") is not None:
        cargs.append("--warp=" + params.get("warped_file"))
    return cargs


def fugue_outputs(
    params: FugueParameters,
    execution: Execution,
) -> FugueOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FugueOutputs(
        root=execution.output_file("."),
        fmap_out_file_outfile=execution.output_file(params.get("fmap_out_file")) if (params.get("fmap_out_file") is not None) else None,
        shift_out_file_outfile=execution.output_file(params.get("shift_out_file")) if (params.get("shift_out_file") is not None) else None,
        unwarped_file_outfile=execution.output_file(params.get("unwarped_file")) if (params.get("unwarped_file") is not None) else None,
        warped_file_outfile=execution.output_file(params.get("warped_file")) if (params.get("warped_file") is not None) else None,
    )
    return ret


def fugue_execute(
    params: FugueParameters,
    execution: Execution,
) -> FugueOutputs:
    """
    FMRIB's Utility for Geometric Unwarping of EPIs.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FugueOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fugue_cargs(params, execution)
    ret = fugue_outputs(params, execution)
    execution.run(cargs)
    return ret


def fugue(
    asym_se_time: float | None = None,
    despike_2dfilter: bool = False,
    despike_threshold: float | None = None,
    dwell_time: float | None = None,
    dwell_to_asym_ratio: float | None = None,
    fmap_in_file: InputPathType | None = None,
    fmap_out_file: str | None = None,
    forward_warping: bool = False,
    fourier_order: int | None = None,
    icorr: bool = False,
    icorr_only: bool = False,
    in_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    median_2dfilter: bool = False,
    no_extend: bool = False,
    no_gap_fill: bool = False,
    nokspace: bool = False,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    pava: bool = False,
    phase_conjugate: bool = False,
    phasemap_in_file: InputPathType | None = None,
    poly_order: int | None = None,
    save_fmap: bool = False,
    save_shift: bool = False,
    save_unmasked_fmap: bool = False,
    save_unmasked_shift: bool = False,
    shift_in_file: InputPathType | None = None,
    shift_out_file: str | None = None,
    smooth2d: float | None = None,
    smooth3d: float | None = None,
    unwarp_direction: typing.Literal["x", "y", "z", "x-", "y-", "z-"] | None = None,
    unwarped_file: str | None = None,
    warped_file: str | None = None,
    runner: Runner | None = None,
) -> FugueOutputs:
    """
    FMRIB's Utility for Geometric Unwarping of EPIs.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        asym_se_time: Set the fieldmap asymmetric spin echo time (sec).
        despike_2dfilter: Apply a 2d de-spiking filter.
        despike_threshold: Specify the threshold for de-spiking (default=3.0).
        dwell_time: Set the epi dwell time per phase-encode line - same as echo\
            spacing - (sec).
        dwell_to_asym_ratio: Set the dwell to asym time ratio.
        fmap_in_file: Filename for loading fieldmap (rad/s).
        fmap_out_file: Filename for saving fieldmap (rad/s).
        forward_warping: Apply forward warping instead of unwarping.
        fourier_order: Apply fourier (sinusoidal) fitting of order n.
        icorr: Apply intensity correction to unwarping (pixel shift method\
            only).
        icorr_only: Apply intensity correction only.
        in_file: Filename of input volume.
        mask_file: Filename for loading valid mask.
        median_2dfilter: Apply 2d median filtering.
        no_extend: Do not apply rigid-body extrapolation to the fieldmap.
        no_gap_fill: Do not apply gap-filling measure to the fieldmap.
        nokspace: Do not use k-space forward warping.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        pava: Apply monotonic enforcement via pava.
        phase_conjugate: Apply phase conjugate method of unwarping.
        phasemap_in_file: Filename for input phase image.
        poly_order: Apply polynomial fitting of order n.
        save_fmap: Write field map volume.
        save_shift: Write pixel shift volume.
        save_unmasked_fmap: Saves the unmasked fieldmap when using --savefmap.
        save_unmasked_shift: Saves the unmasked shiftmap when using\
            --saveshift.
        shift_in_file: Filename for reading pixel shift volume.
        shift_out_file: Filename for saving pixel shift volume.
        smooth2d: Apply 2d gaussian smoothing of sigma n (in mm).
        smooth3d: Apply 3d gaussian smoothing of sigma n (in mm).
        unwarp_direction: 'x' or 'y' or 'z' or 'x-' or 'y-' or 'z-'. Specifies\
            direction of warping (default y).
        unwarped_file: Apply unwarping and save as filename.
        warped_file: Apply forward warping and save as filename.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FugueOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FUGUE_METADATA)
    params = fugue_params(asym_se_time=asym_se_time, despike_2dfilter=despike_2dfilter, despike_threshold=despike_threshold, dwell_time=dwell_time, dwell_to_asym_ratio=dwell_to_asym_ratio, fmap_in_file=fmap_in_file, fmap_out_file=fmap_out_file, forward_warping=forward_warping, fourier_order=fourier_order, icorr=icorr, icorr_only=icorr_only, in_file=in_file, mask_file=mask_file, median_2dfilter=median_2dfilter, no_extend=no_extend, no_gap_fill=no_gap_fill, nokspace=nokspace, output_type=output_type, pava=pava, phase_conjugate=phase_conjugate, phasemap_in_file=phasemap_in_file, poly_order=poly_order, save_fmap=save_fmap, save_shift=save_shift, save_unmasked_fmap=save_unmasked_fmap, save_unmasked_shift=save_unmasked_shift, shift_in_file=shift_in_file, shift_out_file=shift_out_file, smooth2d=smooth2d, smooth3d=smooth3d, unwarp_direction=unwarp_direction, unwarped_file=unwarped_file, warped_file=warped_file)
    return fugue_execute(params, execution)


__all__ = [
    "FUGUE_METADATA",
    "FugueOutputs",
    "FugueParameters",
    "fugue",
    "fugue_params",
]
