# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BEDPOSTX_GPU_METADATA = Metadata(
    id="3f3bab4175d1d6a22bab71654c926ae73e0864f3.boutiques",
    name="bedpostx_gpu",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
BedpostxGpuParameters = typing.TypedDict('BedpostxGpuParameters', {
    "__STYX_TYPE__": typing.Literal["bedpostx_gpu"],
    "subject_dir": str,
    "gpu_queue": typing.NotRequired[str | None],
    "num_jobs": typing.NotRequired[float | None],
    "num_fibers": typing.NotRequired[float | None],
    "ard_weight": typing.NotRequired[float | None],
    "burnin_period": typing.NotRequired[float | None],
    "num_jumps": typing.NotRequired[float | None],
    "sample_every": typing.NotRequired[float | None],
    "deconv_model": typing.NotRequired[float | None],
    "grad_nonlinear": bool,
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
        "bedpostx_gpu": bedpostx_gpu_cargs,
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
    }.get(t)


class BedpostxGpuOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bedpostx_gpu(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bedpostx_gpu_params(
    subject_dir: str,
    gpu_queue: str | None = None,
    num_jobs: float | None = None,
    num_fibers: float | None = None,
    ard_weight: float | None = None,
    burnin_period: float | None = None,
    num_jumps: float | None = None,
    sample_every: float | None = None,
    deconv_model: float | None = None,
    grad_nonlinear: bool = False,
) -> BedpostxGpuParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Directory containing the subject's DWI data and associated\
            files (bvals, bvecs, data, nodif_brain_mask).
        gpu_queue: Name of the GPU(s) queue. Default: --coprocessor=cuda to let\
            fsl_sub decide on the queue.
        num_jobs: Number of jobs to queue. The data is divided into this number\
            of parts, useful for a GPU cluster. Default: 4.
        num_fibers: Number of fibres per voxel. Default: 3.
        ard_weight: Automatic Relevance Determination (ARD) weight. More weight\
            means fewer secondary fibres per voxel. Default: 1.
        burnin_period: Burn-in period. Default: 1000.
        num_jumps: Number of jumps. Default: 1250.
        sample_every: Sample every N steps. Default: 25.
        deconv_model: Deconvolution model. 1: with sticks, 2: with sticks with\
            a range of diffusivities (default), 3: with zeppelins.
        grad_nonlinear: Consider gradient nonlinearities. Default: off.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bedpostx_gpu",
        "subject_dir": subject_dir,
        "grad_nonlinear": grad_nonlinear,
    }
    if gpu_queue is not None:
        params["gpu_queue"] = gpu_queue
    if num_jobs is not None:
        params["num_jobs"] = num_jobs
    if num_fibers is not None:
        params["num_fibers"] = num_fibers
    if ard_weight is not None:
        params["ard_weight"] = ard_weight
    if burnin_period is not None:
        params["burnin_period"] = burnin_period
    if num_jumps is not None:
        params["num_jumps"] = num_jumps
    if sample_every is not None:
        params["sample_every"] = sample_every
    if deconv_model is not None:
        params["deconv_model"] = deconv_model
    return params


def bedpostx_gpu_cargs(
    params: BedpostxGpuParameters,
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
    cargs.append("bedpostx_gpu")
    cargs.append(params.get("subject_dir"))
    if params.get("gpu_queue") is not None:
        cargs.extend([
            "-Q",
            params.get("gpu_queue")
        ])
    if params.get("num_jobs") is not None:
        cargs.extend([
            "-NJOBS",
            str(params.get("num_jobs"))
        ])
    if params.get("num_fibers") is not None:
        cargs.extend([
            "-n",
            str(params.get("num_fibers"))
        ])
    if params.get("ard_weight") is not None:
        cargs.extend([
            "-w",
            str(params.get("ard_weight"))
        ])
    if params.get("burnin_period") is not None:
        cargs.extend([
            "-b",
            str(params.get("burnin_period"))
        ])
    if params.get("num_jumps") is not None:
        cargs.extend([
            "-j",
            str(params.get("num_jumps"))
        ])
    if params.get("sample_every") is not None:
        cargs.extend([
            "-s",
            str(params.get("sample_every"))
        ])
    if params.get("deconv_model") is not None:
        cargs.extend([
            "-model",
            str(params.get("deconv_model"))
        ])
    if params.get("grad_nonlinear"):
        cargs.append("-g")
    return cargs


def bedpostx_gpu_outputs(
    params: BedpostxGpuParameters,
    execution: Execution,
) -> BedpostxGpuOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BedpostxGpuOutputs(
        root=execution.output_file("."),
    )
    return ret


def bedpostx_gpu_execute(
    params: BedpostxGpuParameters,
    execution: Execution,
) -> BedpostxGpuOutputs:
    """
    Probabilistic tractography and diffusion MRI fitting tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BedpostxGpuOutputs`).
    """
    cargs = bedpostx_gpu_cargs(params, execution)
    ret = bedpostx_gpu_outputs(params, execution)
    execution.run(cargs)
    return ret


def bedpostx_gpu(
    subject_dir: str,
    gpu_queue: str | None = None,
    num_jobs: float | None = None,
    num_fibers: float | None = None,
    ard_weight: float | None = None,
    burnin_period: float | None = None,
    num_jumps: float | None = None,
    sample_every: float | None = None,
    deconv_model: float | None = None,
    grad_nonlinear: bool = False,
    runner: Runner | None = None,
) -> BedpostxGpuOutputs:
    """
    Probabilistic tractography and diffusion MRI fitting tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        subject_dir: Directory containing the subject's DWI data and associated\
            files (bvals, bvecs, data, nodif_brain_mask).
        gpu_queue: Name of the GPU(s) queue. Default: --coprocessor=cuda to let\
            fsl_sub decide on the queue.
        num_jobs: Number of jobs to queue. The data is divided into this number\
            of parts, useful for a GPU cluster. Default: 4.
        num_fibers: Number of fibres per voxel. Default: 3.
        ard_weight: Automatic Relevance Determination (ARD) weight. More weight\
            means fewer secondary fibres per voxel. Default: 1.
        burnin_period: Burn-in period. Default: 1000.
        num_jumps: Number of jumps. Default: 1250.
        sample_every: Sample every N steps. Default: 25.
        deconv_model: Deconvolution model. 1: with sticks, 2: with sticks with\
            a range of diffusivities (default), 3: with zeppelins.
        grad_nonlinear: Consider gradient nonlinearities. Default: off.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BedpostxGpuOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BEDPOSTX_GPU_METADATA)
    params = bedpostx_gpu_params(subject_dir=subject_dir, gpu_queue=gpu_queue, num_jobs=num_jobs, num_fibers=num_fibers, ard_weight=ard_weight, burnin_period=burnin_period, num_jumps=num_jumps, sample_every=sample_every, deconv_model=deconv_model, grad_nonlinear=grad_nonlinear)
    return bedpostx_gpu_execute(params, execution)


__all__ = [
    "BEDPOSTX_GPU_METADATA",
    "BedpostxGpuOutputs",
    "BedpostxGpuParameters",
    "bedpostx_gpu",
    "bedpostx_gpu_params",
]
