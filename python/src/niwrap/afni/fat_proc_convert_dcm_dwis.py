# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_PROC_CONVERT_DCM_DWIS_METADATA = Metadata(
    id="9b9610517874019289f1b6f2dec8529be62fcd51.boutiques",
    name="fat_proc_convert_dcm_dwis",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatProcConvertDcmDwisParameters = typing.TypedDict('FatProcConvertDcmDwisParameters', {
    "__STYX_TYPE__": typing.Literal["fat_proc_convert_dcm_dwis"],
    "dicom_dir": str,
    "output_prefix": str,
    "nifti_files": typing.NotRequired[list[InputPathType] | None],
    "bvec_files": typing.NotRequired[list[InputPathType] | None],
    "bval_files": typing.NotRequired[list[InputPathType] | None],
    "work_dir": typing.NotRequired[str | None],
    "orientation": typing.NotRequired[str | None],
    "origin_xyz": typing.NotRequired[list[float] | None],
    "flip_x": bool,
    "flip_y": bool,
    "flip_z": bool,
    "no_flip": bool,
    "qc_prefix": typing.NotRequired[str | None],
    "reorient_off": bool,
    "no_clean": bool,
    "no_cmd_out": bool,
    "no_qc_view": bool,
    "do_movie": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "fat_proc_convert_dcm_dwis": fat_proc_convert_dcm_dwis_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "fat_proc_convert_dcm_dwis": fat_proc_convert_dcm_dwis_outputs,
    }.get(t)


class FatProcConvertDcmDwisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_convert_dcm_dwis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_nifti: OutputPathType
    """A NIFTI file with N volumes."""
    output_rvec: OutputPathType
    """A row-wise (3xN) bvec file of the (unit-magnitude) gradient
    orientations."""
    output_bval: OutputPathType
    """A row-wise (1xN) bval file of the gradient magnitudes."""
    output_mat_a: OutputPathType
    """A column-wise (Nx6) AFNI-style matrix file of the (scaled) b-matrix
    values."""
    output_mat_t: OutputPathType
    """A column-wise (Nx6) TORTOISE-style matrix file of the (scaled) b-matrix
    values."""
    output_cvec: OutputPathType
    """A column-wise (Nx3) bvec file of the (b-magn scaled) gradient
    orientations."""


def fat_proc_convert_dcm_dwis_params(
    dicom_dir: str,
    output_prefix: str,
    nifti_files: list[InputPathType] | None = None,
    bvec_files: list[InputPathType] | None = None,
    bval_files: list[InputPathType] | None = None,
    work_dir: str | None = None,
    orientation: str | None = None,
    origin_xyz: list[float] | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    no_flip: bool = False,
    qc_prefix: str | None = None,
    reorient_off: bool = False,
    no_clean: bool = False,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
    do_movie: str | None = None,
) -> FatProcConvertDcmDwisParameters:
    """
    Build parameters.
    
    Args:
        dicom_dir: Directory of DICOM files of the DWI data with 'AP' phase\
            encoding. Can contain a wildcard expression for several directories.
        output_prefix: Prefix (and path) for output data (e.g., *.nii.gz,\
            *.bvec, *.bval files). Required.
        nifti_files: One or more NIFTI files of DWIs.
        bvec_files: One or more row-wise, gradient (unit-magnitude) files\
            (e.g., *.bvec).
        bval_files: One or more bvalue files (e.g., *.bval).
        work_dir: Optional working directory for intermediate files.
        orientation: Optional chance to reset orientation of the volume files\
            (default is currently 'RAI').
        origin_xyz: Explicit origin coordinates (X, Y, Z).
        flip_x: Flip gradients along the X-axis.
        flip_y: Flip gradients along the Y-axis.
        flip_z: Flip gradients along the Z-axis.
        no_flip: Prevent flipping of gradients (default).
        qc_prefix: Set the prefix for QC image files separately (default is\
            '').
        reorient_off: Turn off reorigin calculation and reorientation.
        no_clean: Do not remove the working directory of intermediate files\
            (default is to delete it).
        no_cmd_out: Do not save the command line call and location where it was\
            run.
        no_qc_view: Do not generate QC image files.
        do_movie: Generate a movie of the newly created dataset (AGIF or MPEG).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_proc_convert_dcm_dwis",
        "dicom_dir": dicom_dir,
        "output_prefix": output_prefix,
        "flip_x": flip_x,
        "flip_y": flip_y,
        "flip_z": flip_z,
        "no_flip": no_flip,
        "reorient_off": reorient_off,
        "no_clean": no_clean,
        "no_cmd_out": no_cmd_out,
        "no_qc_view": no_qc_view,
    }
    if nifti_files is not None:
        params["nifti_files"] = nifti_files
    if bvec_files is not None:
        params["bvec_files"] = bvec_files
    if bval_files is not None:
        params["bval_files"] = bval_files
    if work_dir is not None:
        params["work_dir"] = work_dir
    if orientation is not None:
        params["orientation"] = orientation
    if origin_xyz is not None:
        params["origin_xyz"] = origin_xyz
    if qc_prefix is not None:
        params["qc_prefix"] = qc_prefix
    if do_movie is not None:
        params["do_movie"] = do_movie
    return params


def fat_proc_convert_dcm_dwis_cargs(
    params: FatProcConvertDcmDwisParameters,
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
    cargs.append("fat_proc_convert_dcm_dwis")
    cargs.append(params.get("dicom_dir"))
    cargs.append(params.get("output_prefix"))
    if params.get("nifti_files") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("nifti_files")])
    if params.get("bvec_files") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("bvec_files")])
    if params.get("bval_files") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("bval_files")])
    if params.get("work_dir") is not None:
        cargs.append(params.get("work_dir"))
    if params.get("orientation") is not None:
        cargs.append(params.get("orientation"))
    if params.get("origin_xyz") is not None:
        cargs.extend(map(str, params.get("origin_xyz")))
    if params.get("flip_x"):
        cargs.append("-flip_x")
    if params.get("flip_y"):
        cargs.append("-flip_y")
    if params.get("flip_z"):
        cargs.append("-flip_z")
    if params.get("no_flip"):
        cargs.append("-no_flip")
    if params.get("qc_prefix") is not None:
        cargs.append(params.get("qc_prefix"))
    if params.get("reorient_off"):
        cargs.append("-reorig_reorient_off")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("no_cmd_out"):
        cargs.append("-no_cmd_out")
    if params.get("no_qc_view"):
        cargs.append("-no_qc_view")
    if params.get("do_movie") is not None:
        cargs.extend([
            "-do_movie",
            params.get("do_movie")
        ])
    return cargs


def fat_proc_convert_dcm_dwis_outputs(
    params: FatProcConvertDcmDwisParameters,
    execution: Execution,
) -> FatProcConvertDcmDwisOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatProcConvertDcmDwisOutputs(
        root=execution.output_file("."),
        output_nifti=execution.output_file(params.get("output_prefix") + ".nii.gz"),
        output_rvec=execution.output_file(params.get("output_prefix") + ".rvec"),
        output_bval=execution.output_file(params.get("output_prefix") + ".bval"),
        output_mat_a=execution.output_file(params.get("output_prefix") + "_matA.dat"),
        output_mat_t=execution.output_file(params.get("output_prefix") + "_matT.dat"),
        output_cvec=execution.output_file(params.get("output_prefix") + "_cvec.dat"),
    )
    return ret


def fat_proc_convert_dcm_dwis_execute(
    params: FatProcConvertDcmDwisParameters,
    execution: Execution,
) -> FatProcConvertDcmDwisOutputs:
    """
    Convert sets of DWIs in DICOM format into 'nicer' volume+grad format, reorient
    volumetric data, and glue together multiple sessions/directories of data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatProcConvertDcmDwisOutputs`).
    """
    cargs = fat_proc_convert_dcm_dwis_cargs(params, execution)
    ret = fat_proc_convert_dcm_dwis_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_proc_convert_dcm_dwis(
    dicom_dir: str,
    output_prefix: str,
    nifti_files: list[InputPathType] | None = None,
    bvec_files: list[InputPathType] | None = None,
    bval_files: list[InputPathType] | None = None,
    work_dir: str | None = None,
    orientation: str | None = None,
    origin_xyz: list[float] | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    no_flip: bool = False,
    qc_prefix: str | None = None,
    reorient_off: bool = False,
    no_clean: bool = False,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
    do_movie: str | None = None,
    runner: Runner | None = None,
) -> FatProcConvertDcmDwisOutputs:
    """
    Convert sets of DWIs in DICOM format into 'nicer' volume+grad format, reorient
    volumetric data, and glue together multiple sessions/directories of data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dicom_dir: Directory of DICOM files of the DWI data with 'AP' phase\
            encoding. Can contain a wildcard expression for several directories.
        output_prefix: Prefix (and path) for output data (e.g., *.nii.gz,\
            *.bvec, *.bval files). Required.
        nifti_files: One or more NIFTI files of DWIs.
        bvec_files: One or more row-wise, gradient (unit-magnitude) files\
            (e.g., *.bvec).
        bval_files: One or more bvalue files (e.g., *.bval).
        work_dir: Optional working directory for intermediate files.
        orientation: Optional chance to reset orientation of the volume files\
            (default is currently 'RAI').
        origin_xyz: Explicit origin coordinates (X, Y, Z).
        flip_x: Flip gradients along the X-axis.
        flip_y: Flip gradients along the Y-axis.
        flip_z: Flip gradients along the Z-axis.
        no_flip: Prevent flipping of gradients (default).
        qc_prefix: Set the prefix for QC image files separately (default is\
            '').
        reorient_off: Turn off reorigin calculation and reorientation.
        no_clean: Do not remove the working directory of intermediate files\
            (default is to delete it).
        no_cmd_out: Do not save the command line call and location where it was\
            run.
        no_qc_view: Do not generate QC image files.
        do_movie: Generate a movie of the newly created dataset (AGIF or MPEG).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcConvertDcmDwisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_CONVERT_DCM_DWIS_METADATA)
    params = fat_proc_convert_dcm_dwis_params(dicom_dir=dicom_dir, output_prefix=output_prefix, nifti_files=nifti_files, bvec_files=bvec_files, bval_files=bval_files, work_dir=work_dir, orientation=orientation, origin_xyz=origin_xyz, flip_x=flip_x, flip_y=flip_y, flip_z=flip_z, no_flip=no_flip, qc_prefix=qc_prefix, reorient_off=reorient_off, no_clean=no_clean, no_cmd_out=no_cmd_out, no_qc_view=no_qc_view, do_movie=do_movie)
    return fat_proc_convert_dcm_dwis_execute(params, execution)


__all__ = [
    "FAT_PROC_CONVERT_DCM_DWIS_METADATA",
    "FatProcConvertDcmDwisOutputs",
    "FatProcConvertDcmDwisParameters",
    "fat_proc_convert_dcm_dwis",
    "fat_proc_convert_dcm_dwis_params",
]
