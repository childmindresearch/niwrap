# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_DECONVOLVE_METADATA = Metadata(
    id="3c5bd8bab8c9c3f4b4586c2e6fc553ef1b03f1e4.boutiques",
    name="3dDeconvolve",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dDeconvolveParameters = typing.TypedDict('V3dDeconvolveParameters', {
    "__STYX_TYPE__": typing.Literal["3dDeconvolve"],
    "input_dataset": InputPathType,
    "mask_dataset": typing.NotRequired[InputPathType | None],
    "num_stimts": typing.NotRequired[int | None],
    "stim_file": typing.NotRequired[str | None],
    "stim_label": typing.NotRequired[str | None],
    "stim_base": bool,
    "stim_times": typing.NotRequired[str | None],
    "iresp": typing.NotRequired[str | None],
    "fitts": typing.NotRequired[str | None],
    "fout": bool,
    "tout": bool,
    "bucket": typing.NotRequired[str | None],
    "cbucket": typing.NotRequired[str | None],
    "x1D": typing.NotRequired[str | None],
    "jobs": typing.NotRequired[int | None],
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
        "3dDeconvolve": v_3d_deconvolve_cargs,
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
        "3dDeconvolve": v_3d_deconvolve_outputs,
    }.get(t)


class V3dDeconvolveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_deconvolve(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    bucket_output: OutputPathType | None
    """Main output bucket dataset in AFNI format."""
    cbucket_output: OutputPathType | None
    """Regression coefficients stored in a dataset."""
    iresp_output: OutputPathType | None
    """Estimated Impulse Response dataset."""
    fitts_output: OutputPathType | None
    """Fitted Time Series dataset in AFNI format."""
    x1d_file: OutputPathType | None
    """X-matrix output file in .1D format."""


def v_3d_deconvolve_params(
    input_dataset: InputPathType,
    mask_dataset: InputPathType | None = None,
    num_stimts: int | None = None,
    stim_file: str | None = None,
    stim_label: str | None = None,
    stim_base: bool = False,
    stim_times: str | None = None,
    iresp: str | None = None,
    fitts: str | None = None,
    fout: bool = False,
    tout: bool = False,
    bucket: str | None = None,
    cbucket: str | None = None,
    x1_d: str | None = None,
    jobs: int | None = None,
) -> V3dDeconvolveParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Filename of 3D+time input dataset.
        mask_dataset: Filename of 3D mask dataset.
        num_stimts: Number of input stimulus time series.
        stim_file: Filename of kth time series input stimulus.
        stim_label: Label for kth input stimulus.
        stim_base: Kth input stimulus is part of the baseline model.
        stim_times: Deconvolution response model for kth stimulus.
        iresp: Prefix for 3D+time output dataset which will contain the kth\
            estimated impulse response.
        fitts: Prefix for 3D+time output dataset which will contain the (full\
            model) time series fit to the input data.
        fout: Flag to output the F-statistics for each stimulus.
        tout: Flag to output the t-statistics.
        bucket: Create one AFNI 'bucket' dataset containing various parameters\
            of interest.
        cbucket: Save the regression coefficients (no statistics) into a\
            dataset.
        x1_d: Save X matrix to a .xmat.1D (ASCII) file.
        jobs: Run the program with multiple jobs (sub-processes).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dDeconvolve",
        "input_dataset": input_dataset,
        "stim_base": stim_base,
        "fout": fout,
        "tout": tout,
    }
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    if num_stimts is not None:
        params["num_stimts"] = num_stimts
    if stim_file is not None:
        params["stim_file"] = stim_file
    if stim_label is not None:
        params["stim_label"] = stim_label
    if stim_times is not None:
        params["stim_times"] = stim_times
    if iresp is not None:
        params["iresp"] = iresp
    if fitts is not None:
        params["fitts"] = fitts
    if bucket is not None:
        params["bucket"] = bucket
    if cbucket is not None:
        params["cbucket"] = cbucket
    if x1_d is not None:
        params["x1D"] = x1_d
    if jobs is not None:
        params["jobs"] = jobs
    return params


def v_3d_deconvolve_cargs(
    params: V3dDeconvolveParameters,
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
    cargs.append("3dDeconvolve")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_dataset"))
    ])
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dataset"))
        ])
    if params.get("num_stimts") is not None:
        cargs.extend([
            "-num_stimts",
            str(params.get("num_stimts"))
        ])
    if params.get("stim_file") is not None:
        cargs.extend([
            "-stim_file",
            params.get("stim_file")
        ])
    if params.get("stim_label") is not None:
        cargs.extend([
            "-stim_label",
            params.get("stim_label")
        ])
    if params.get("stim_base"):
        cargs.append("-stim_base")
    if params.get("stim_times") is not None:
        cargs.extend([
            "-stim_times",
            params.get("stim_times")
        ])
    if params.get("iresp") is not None:
        cargs.extend([
            "-iresp",
            params.get("iresp")
        ])
    if params.get("fitts") is not None:
        cargs.extend([
            "-fitts",
            params.get("fitts")
        ])
    if params.get("fout"):
        cargs.append("-fout")
    if params.get("tout"):
        cargs.append("-tout")
    if params.get("bucket") is not None:
        cargs.extend([
            "-bucket",
            params.get("bucket")
        ])
    if params.get("cbucket") is not None:
        cargs.extend([
            "-cbucket",
            params.get("cbucket")
        ])
    if params.get("x1D") is not None:
        cargs.extend([
            "-x1D",
            params.get("x1D")
        ])
    if params.get("jobs") is not None:
        cargs.extend([
            "-jobs",
            str(params.get("jobs"))
        ])
    return cargs


def v_3d_deconvolve_outputs(
    params: V3dDeconvolveParameters,
    execution: Execution,
) -> V3dDeconvolveOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dDeconvolveOutputs(
        root=execution.output_file("."),
        bucket_output=execution.output_file(params.get("bucket") + ".HEAD") if (params.get("bucket") is not None) else None,
        cbucket_output=execution.output_file(params.get("cbucket") + ".HEAD") if (params.get("cbucket") is not None) else None,
        iresp_output=execution.output_file(params.get("iresp") + ".HEAD") if (params.get("iresp") is not None) else None,
        fitts_output=execution.output_file(params.get("fitts") + ".HEAD") if (params.get("fitts") is not None) else None,
        x1d_file=execution.output_file(params.get("x1D") + ".1D") if (params.get("x1D") is not None) else None,
    )
    return ret


def v_3d_deconvolve_execute(
    params: V3dDeconvolveParameters,
    execution: Execution,
) -> V3dDeconvolveOutputs:
    """
    Program to calculate the deconvolution of a measurement 3D+time dataset with a
    specified input stimulus time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dDeconvolveOutputs`).
    """
    cargs = v_3d_deconvolve_cargs(params, execution)
    ret = v_3d_deconvolve_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_deconvolve(
    input_dataset: InputPathType,
    mask_dataset: InputPathType | None = None,
    num_stimts: int | None = None,
    stim_file: str | None = None,
    stim_label: str | None = None,
    stim_base: bool = False,
    stim_times: str | None = None,
    iresp: str | None = None,
    fitts: str | None = None,
    fout: bool = False,
    tout: bool = False,
    bucket: str | None = None,
    cbucket: str | None = None,
    x1_d: str | None = None,
    jobs: int | None = None,
    runner: Runner | None = None,
) -> V3dDeconvolveOutputs:
    """
    Program to calculate the deconvolution of a measurement 3D+time dataset with a
    specified input stimulus time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Filename of 3D+time input dataset.
        mask_dataset: Filename of 3D mask dataset.
        num_stimts: Number of input stimulus time series.
        stim_file: Filename of kth time series input stimulus.
        stim_label: Label for kth input stimulus.
        stim_base: Kth input stimulus is part of the baseline model.
        stim_times: Deconvolution response model for kth stimulus.
        iresp: Prefix for 3D+time output dataset which will contain the kth\
            estimated impulse response.
        fitts: Prefix for 3D+time output dataset which will contain the (full\
            model) time series fit to the input data.
        fout: Flag to output the F-statistics for each stimulus.
        tout: Flag to output the t-statistics.
        bucket: Create one AFNI 'bucket' dataset containing various parameters\
            of interest.
        cbucket: Save the regression coefficients (no statistics) into a\
            dataset.
        x1_d: Save X matrix to a .xmat.1D (ASCII) file.
        jobs: Run the program with multiple jobs (sub-processes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDeconvolveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DECONVOLVE_METADATA)
    params = v_3d_deconvolve_params(input_dataset=input_dataset, mask_dataset=mask_dataset, num_stimts=num_stimts, stim_file=stim_file, stim_label=stim_label, stim_base=stim_base, stim_times=stim_times, iresp=iresp, fitts=fitts, fout=fout, tout=tout, bucket=bucket, cbucket=cbucket, x1_d=x1_d, jobs=jobs)
    return v_3d_deconvolve_execute(params, execution)


__all__ = [
    "V3dDeconvolveOutputs",
    "V3dDeconvolveParameters",
    "V_3D_DECONVOLVE_METADATA",
    "v_3d_deconvolve",
    "v_3d_deconvolve_params",
]
