# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_PROC_ALIGN_ANAT_PAIR_METADATA = Metadata(
    id="b81d41214e66c7f77b2bbc885c2f23369ad68254.boutiques",
    name="fat_proc_align_anat_pair",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatProcAlignAnatPairParameters = typing.TypedDict('FatProcAlignAnatPairParameters', {
    "__STYX_TYPE__": typing.Literal["fat_proc_align_anat_pair"],
    "input_t1w": InputPathType,
    "input_t2w": InputPathType,
    "output_prefix": str,
    "output_grid": typing.NotRequired[float | None],
    "input_t2w_mask": typing.NotRequired[InputPathType | None],
    "do_ss_tmp_t1w": bool,
    "warp": typing.NotRequired[str | None],
    "matrix": typing.NotRequired[InputPathType | None],
    "workdir": typing.NotRequired[str | None],
    "no_cmd_out": bool,
    "no_clean": bool,
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
        "fat_proc_align_anat_pair": fat_proc_align_anat_pair_cargs,
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
        "fat_proc_align_anat_pair": fat_proc_align_anat_pair_outputs,
    }
    return vt.get(t)


class FatProcAlignAnatPairOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_align_anat_pair(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aligned_t1w: OutputPathType
    """Aligned T1w volume"""
    qc_snapshot_t1w_on_t2w: OutputPathType
    """QC snapshot of the T1w volume overlaying the T2w volume"""
    qc_snapshot_t1w_edges_on_t2w: OutputPathType
    """QC snapshot of the T1w edges overlaying the T2w volume"""


def fat_proc_align_anat_pair_params(
    input_t1w: InputPathType,
    input_t2w: InputPathType,
    output_prefix: str,
    output_grid: float | None = None,
    input_t2w_mask: InputPathType | None = None,
    do_ss_tmp_t1w: bool = False,
    warp: str | None = None,
    matrix: InputPathType | None = None,
    workdir: str | None = None,
    no_cmd_out: bool = False,
    no_clean: bool = False,
) -> FatProcAlignAnatPairParameters:
    """
    Build parameters.
    
    Args:
        input_t1w: T1-weighted volume.
        input_t2w: T2-weighted volume.
        output_prefix: Output prefix for files and snapshots.
        output_grid: Specify output T1w volume's final resolution (isotropic).
        input_t2w_mask: Input a mask to apply to the T2w volume for alignment.
        do_ss_tmp_t1w: Apply skullstripping to the T1w volume during an\
            intermediate step.
        warp: Specify the degrees of freedom for warping using options from\
            3dAllineate.
        matrix: Apply a pre-made matrix from 3dAllineate.
        workdir: Specify a working directory.
        no_cmd_out: Do not save the command line call and the location where it\
            was run.
        no_clean: Do not delete the temporary working directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_proc_align_anat_pair",
        "input_t1w": input_t1w,
        "input_t2w": input_t2w,
        "output_prefix": output_prefix,
        "do_ss_tmp_t1w": do_ss_tmp_t1w,
        "no_cmd_out": no_cmd_out,
        "no_clean": no_clean,
    }
    if output_grid is not None:
        params["output_grid"] = output_grid
    if input_t2w_mask is not None:
        params["input_t2w_mask"] = input_t2w_mask
    if warp is not None:
        params["warp"] = warp
    if matrix is not None:
        params["matrix"] = matrix
    if workdir is not None:
        params["workdir"] = workdir
    return params


def fat_proc_align_anat_pair_cargs(
    params: FatProcAlignAnatPairParameters,
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
    cargs.append("fat_proc_align_anat_pair")
    cargs.extend([
        "-in_t1w",
        execution.input_file(params.get("input_t1w"))
    ])
    cargs.extend([
        "-in_t2w",
        execution.input_file(params.get("input_t2w"))
    ])
    cargs.extend([
        "-prefix",
        params.get("output_prefix")
    ])
    if params.get("output_grid") is not None:
        cargs.extend([
            "-newgrid",
            str(params.get("output_grid"))
        ])
    if params.get("input_t2w_mask") is not None:
        cargs.extend([
            "-in_t2w_mask",
            execution.input_file(params.get("input_t2w_mask"))
        ])
    if params.get("do_ss_tmp_t1w"):
        cargs.append("-do_ss_tmp_t1w")
    if params.get("warp") is not None:
        cargs.extend([
            "-warp",
            params.get("warp")
        ])
    if params.get("matrix") is not None:
        cargs.extend([
            "-matrix",
            execution.input_file(params.get("matrix"))
        ])
    if params.get("workdir") is not None:
        cargs.extend([
            "-workdir",
            params.get("workdir")
        ])
    if params.get("no_cmd_out"):
        cargs.append("-no_cmd_out")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    return cargs


def fat_proc_align_anat_pair_outputs(
    params: FatProcAlignAnatPairParameters,
    execution: Execution,
) -> FatProcAlignAnatPairOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatProcAlignAnatPairOutputs(
        root=execution.output_file("."),
        aligned_t1w=execution.output_file(params.get("output_prefix") + "_t1w_aligned.nii.gz"),
        qc_snapshot_t1w_on_t2w=execution.output_file(params.get("output_prefix") + "_QC_T1w_over_T2w.png"),
        qc_snapshot_t1w_edges_on_t2w=execution.output_file(params.get("output_prefix") + "_QC_T1w_edges_over_T2w.png"),
    )
    return ret


def fat_proc_align_anat_pair_execute(
    params: FatProcAlignAnatPairParameters,
    execution: Execution,
) -> FatProcAlignAnatPairOutputs:
    """
    A tool for aligning a T1w anatomical image to a T2w anatomical image using
    solid-body parameters (translation and rotation).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatProcAlignAnatPairOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fat_proc_align_anat_pair_cargs(params, execution)
    ret = fat_proc_align_anat_pair_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_proc_align_anat_pair(
    input_t1w: InputPathType,
    input_t2w: InputPathType,
    output_prefix: str,
    output_grid: float | None = None,
    input_t2w_mask: InputPathType | None = None,
    do_ss_tmp_t1w: bool = False,
    warp: str | None = None,
    matrix: InputPathType | None = None,
    workdir: str | None = None,
    no_cmd_out: bool = False,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> FatProcAlignAnatPairOutputs:
    """
    A tool for aligning a T1w anatomical image to a T2w anatomical image using
    solid-body parameters (translation and rotation).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_t1w: T1-weighted volume.
        input_t2w: T2-weighted volume.
        output_prefix: Output prefix for files and snapshots.
        output_grid: Specify output T1w volume's final resolution (isotropic).
        input_t2w_mask: Input a mask to apply to the T2w volume for alignment.
        do_ss_tmp_t1w: Apply skullstripping to the T1w volume during an\
            intermediate step.
        warp: Specify the degrees of freedom for warping using options from\
            3dAllineate.
        matrix: Apply a pre-made matrix from 3dAllineate.
        workdir: Specify a working directory.
        no_cmd_out: Do not save the command line call and the location where it\
            was run.
        no_clean: Do not delete the temporary working directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcAlignAnatPairOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_ALIGN_ANAT_PAIR_METADATA)
    params = fat_proc_align_anat_pair_params(input_t1w=input_t1w, input_t2w=input_t2w, output_prefix=output_prefix, output_grid=output_grid, input_t2w_mask=input_t2w_mask, do_ss_tmp_t1w=do_ss_tmp_t1w, warp=warp, matrix=matrix, workdir=workdir, no_cmd_out=no_cmd_out, no_clean=no_clean)
    return fat_proc_align_anat_pair_execute(params, execution)


__all__ = [
    "FAT_PROC_ALIGN_ANAT_PAIR_METADATA",
    "FatProcAlignAnatPairOutputs",
    "FatProcAlignAnatPairParameters",
    "fat_proc_align_anat_pair",
    "fat_proc_align_anat_pair_params",
]
