# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MM_METADATA = Metadata(
    id="a5f0fd0df34d3464fbfc708013a6765ded373c4d.boutiques",
    name="mm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MmParameters = typing.TypedDict('MmParameters', {
    "__STYX_TYPE__": typing.Literal["mm"],
    "spatial_data_file": InputPathType,
    "mask_file": InputPathType,
    "verbose_flag": bool,
    "debug_level": typing.NotRequired[str | None],
    "timing_flag": bool,
    "example_epi_file": typing.NotRequired[InputPathType | None],
    "log_directory": typing.NotRequired[str | None],
    "nonspatial_flag": bool,
    "fix_mrf_precision_flag": bool,
    "mrf_prec_start": typing.NotRequired[float | None],
    "mrf_prec_multiplier": typing.NotRequired[float | None],
    "init_multiplier": typing.NotRequired[float | None],
    "no_update_theta_flag": bool,
    "zfstat_flag": bool,
    "phi": typing.NotRequired[float | None],
    "niters": typing.NotRequired[float | None],
    "threshold": typing.NotRequired[float | None],
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
        "mm": mm_cargs,
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
        "mm": mm_outputs,
    }.get(t)


class MmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mm_params(
    spatial_data_file: InputPathType,
    mask_file: InputPathType,
    verbose_flag: bool = False,
    debug_level: str | None = None,
    timing_flag: bool = False,
    example_epi_file: InputPathType | None = None,
    log_directory: str | None = None,
    nonspatial_flag: bool = False,
    fix_mrf_precision_flag: bool = False,
    mrf_prec_start: float | None = None,
    mrf_prec_multiplier: float | None = None,
    init_multiplier: float | None = None,
    no_update_theta_flag: bool = False,
    zfstat_flag: bool = False,
    phi: float | None = None,
    niters: float | None = None,
    threshold: float | None = None,
) -> MmParameters:
    """
    Build parameters.
    
    Args:
        spatial_data_file: Spatial map data file.
        mask_file: Mask file.
        verbose_flag: Switch on diagnostic messages.
        debug_level: Set debug level.
        timing_flag: Turn timing on.
        example_epi_file: Example EPI data file.
        log_directory: Log directory.
        nonspatial_flag: Nonspatial mixture model.
        fix_mrf_precision_flag: Fix MRF precision to mrfprecstart throughout.
        mrf_prec_start: MRF precision initial value (default is 10).
        mrf_prec_multiplier: Update multiplier for MRF precision (default is\
            -1, do not multiply).
        init_multiplier: Init multiplier (default is 0.3).
        no_update_theta_flag: Turn off updating of distribution parameters\
            after non-spatial fit.
        zfstat_flag: Turn on zfstat mode - this enforces no deactivation class.
        phi: Phi (default is 0.05).
        niters: Number of iterations (default is -1: auto stop).
        threshold: Threshold for use when displaying classification maps in\
            MM.html report (default is 0.5, -1 indicates no thresholding).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mm",
        "spatial_data_file": spatial_data_file,
        "mask_file": mask_file,
        "verbose_flag": verbose_flag,
        "timing_flag": timing_flag,
        "nonspatial_flag": nonspatial_flag,
        "fix_mrf_precision_flag": fix_mrf_precision_flag,
        "no_update_theta_flag": no_update_theta_flag,
        "zfstat_flag": zfstat_flag,
    }
    if debug_level is not None:
        params["debug_level"] = debug_level
    if example_epi_file is not None:
        params["example_epi_file"] = example_epi_file
    if log_directory is not None:
        params["log_directory"] = log_directory
    if mrf_prec_start is not None:
        params["mrf_prec_start"] = mrf_prec_start
    if mrf_prec_multiplier is not None:
        params["mrf_prec_multiplier"] = mrf_prec_multiplier
    if init_multiplier is not None:
        params["init_multiplier"] = init_multiplier
    if phi is not None:
        params["phi"] = phi
    if niters is not None:
        params["niters"] = niters
    if threshold is not None:
        params["threshold"] = threshold
    return params


def mm_cargs(
    params: MmParameters,
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
    cargs.append("mm")
    cargs.extend([
        "--sdf",
        execution.input_file(params.get("spatial_data_file"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask_file"))
    ])
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    if params.get("debug_level") is not None:
        cargs.extend([
            "--debug",
            params.get("debug_level")
        ])
    if params.get("timing_flag"):
        cargs.append("--timingon")
    if params.get("example_epi_file") is not None:
        cargs.extend([
            "--edf",
            execution.input_file(params.get("example_epi_file"))
        ])
    if params.get("log_directory") is not None:
        cargs.extend([
            "--logdir",
            params.get("log_directory")
        ])
    if params.get("nonspatial_flag"):
        cargs.append("--ns")
    if params.get("fix_mrf_precision_flag"):
        cargs.append("--fmp")
    if params.get("mrf_prec_start") is not None:
        cargs.extend([
            "--mps",
            str(params.get("mrf_prec_start"))
        ])
    if params.get("mrf_prec_multiplier") is not None:
        cargs.extend([
            "--mpm",
            str(params.get("mrf_prec_multiplier"))
        ])
    if params.get("init_multiplier") is not None:
        cargs.extend([
            "--im",
            str(params.get("init_multiplier"))
        ])
    if params.get("no_update_theta_flag"):
        cargs.append("--nut")
    if params.get("zfstat_flag"):
        cargs.append("--zfstatmode")
    if params.get("phi") is not None:
        cargs.extend([
            "--phi",
            str(params.get("phi"))
        ])
    if params.get("niters") is not None:
        cargs.extend([
            "--ni",
            str(params.get("niters"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "--th",
            str(params.get("threshold"))
        ])
    return cargs


def mm_outputs(
    params: MmParameters,
    execution: Execution,
) -> MmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MmOutputs(
        root=execution.output_file("."),
    )
    return ret


def mm_execute(
    params: MmParameters,
    execution: Execution,
) -> MmOutputs:
    """
    FSL's MM: mixture modelling.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MmOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mm_cargs(params, execution)
    ret = mm_outputs(params, execution)
    execution.run(cargs)
    return ret


def mm(
    spatial_data_file: InputPathType,
    mask_file: InputPathType,
    verbose_flag: bool = False,
    debug_level: str | None = None,
    timing_flag: bool = False,
    example_epi_file: InputPathType | None = None,
    log_directory: str | None = None,
    nonspatial_flag: bool = False,
    fix_mrf_precision_flag: bool = False,
    mrf_prec_start: float | None = None,
    mrf_prec_multiplier: float | None = None,
    init_multiplier: float | None = None,
    no_update_theta_flag: bool = False,
    zfstat_flag: bool = False,
    phi: float | None = None,
    niters: float | None = None,
    threshold: float | None = None,
    runner: Runner | None = None,
) -> MmOutputs:
    """
    FSL's MM: mixture modelling.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        spatial_data_file: Spatial map data file.
        mask_file: Mask file.
        verbose_flag: Switch on diagnostic messages.
        debug_level: Set debug level.
        timing_flag: Turn timing on.
        example_epi_file: Example EPI data file.
        log_directory: Log directory.
        nonspatial_flag: Nonspatial mixture model.
        fix_mrf_precision_flag: Fix MRF precision to mrfprecstart throughout.
        mrf_prec_start: MRF precision initial value (default is 10).
        mrf_prec_multiplier: Update multiplier for MRF precision (default is\
            -1, do not multiply).
        init_multiplier: Init multiplier (default is 0.3).
        no_update_theta_flag: Turn off updating of distribution parameters\
            after non-spatial fit.
        zfstat_flag: Turn on zfstat mode - this enforces no deactivation class.
        phi: Phi (default is 0.05).
        niters: Number of iterations (default is -1: auto stop).
        threshold: Threshold for use when displaying classification maps in\
            MM.html report (default is 0.5, -1 indicates no thresholding).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MM_METADATA)
    params = mm_params(spatial_data_file=spatial_data_file, mask_file=mask_file, verbose_flag=verbose_flag, debug_level=debug_level, timing_flag=timing_flag, example_epi_file=example_epi_file, log_directory=log_directory, nonspatial_flag=nonspatial_flag, fix_mrf_precision_flag=fix_mrf_precision_flag, mrf_prec_start=mrf_prec_start, mrf_prec_multiplier=mrf_prec_multiplier, init_multiplier=init_multiplier, no_update_theta_flag=no_update_theta_flag, zfstat_flag=zfstat_flag, phi=phi, niters=niters, threshold=threshold)
    return mm_execute(params, execution)


__all__ = [
    "MM_METADATA",
    "MmOutputs",
    "MmParameters",
    "mm",
    "mm_params",
]
