# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CUTOFFCALC_METADATA = Metadata(
    id="983f28efabc0fcccbe86a104805496b9be754f5e.boutiques",
    name="cutoffcalc",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
CutoffcalcParameters = typing.TypedDict('CutoffcalcParameters', {
    "__STYX_TYPE__": typing.Literal["cutoffcalc"],
    "input_design": InputPathType,
    "threshold": typing.NotRequired[float | None],
    "tr": typing.NotRequired[float | None],
    "lower_limit": typing.NotRequired[float | None],
    "example_sigma": typing.NotRequired[float | None],
    "verbose_flag": bool,
    "debug_flag": bool,
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
        "cutoffcalc": cutoffcalc_cargs,
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
        "cutoffcalc": cutoffcalc_outputs,
    }.get(t)


class CutoffcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cutoffcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    example_output: OutputPathType
    """Filtered output file if example sigma is provided"""


def cutoffcalc_params(
    input_design: InputPathType,
    threshold: float | None = 0.9,
    tr: float | None = 3.0,
    lower_limit: float | None = 90.0,
    example_sigma: float | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
) -> CutoffcalcParameters:
    """
    Build parameters.
    
    Args:
        input_design: Input design matrix (e.g. design.mat).
        threshold: Threshold for retained variance (default=0.9).
        tr: Time between successive data points (default=3.0s).
        lower_limit: Lower limit on period due to autocorr estimation\
            (default=90s).
        example_sigma: Example sigma (in sec) to produce output called\
            example_filt.mtx.
        verbose_flag: Switch on diagnostic messages.
        debug_flag: Switch on debugging messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cutoffcalc",
        "input_design": input_design,
        "verbose_flag": verbose_flag,
        "debug_flag": debug_flag,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if tr is not None:
        params["tr"] = tr
    if lower_limit is not None:
        params["lower_limit"] = lower_limit
    if example_sigma is not None:
        params["example_sigma"] = example_sigma
    return params


def cutoffcalc_cargs(
    params: CutoffcalcParameters,
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
    cargs.append("cutoffcalc")
    cargs.append("-i " + execution.input_file(params.get("input_design")))
    if params.get("threshold") is not None:
        cargs.append("-t " + str(params.get("threshold")))
    if params.get("tr") is not None:
        cargs.append("--tr " + str(params.get("tr")))
    if params.get("lower_limit") is not None:
        cargs.append("--limit " + str(params.get("lower_limit")))
    if params.get("example_sigma") is not None:
        cargs.append("--example_sig " + str(params.get("example_sigma")))
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("debug_flag"):
        cargs.append("--debug")
    return cargs


def cutoffcalc_outputs(
    params: CutoffcalcParameters,
    execution: Execution,
) -> CutoffcalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CutoffcalcOutputs(
        root=execution.output_file("."),
        example_output=execution.output_file("example_filt.mtx"),
    )
    return ret


def cutoffcalc_execute(
    params: CutoffcalcParameters,
    execution: Execution,
) -> CutoffcalcOutputs:
    """
    Calculates the minimal period for the highpass filter that still preserves a
    specified amount of variance in all the design matrix regressors.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CutoffcalcOutputs`).
    """
    params = execution.params(params)
    cargs = cutoffcalc_cargs(params, execution)
    ret = cutoffcalc_outputs(params, execution)
    execution.run(cargs)
    return ret


def cutoffcalc(
    input_design: InputPathType,
    threshold: float | None = 0.9,
    tr: float | None = 3.0,
    lower_limit: float | None = 90.0,
    example_sigma: float | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> CutoffcalcOutputs:
    """
    Calculates the minimal period for the highpass filter that still preserves a
    specified amount of variance in all the design matrix regressors.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_design: Input design matrix (e.g. design.mat).
        threshold: Threshold for retained variance (default=0.9).
        tr: Time between successive data points (default=3.0s).
        lower_limit: Lower limit on period due to autocorr estimation\
            (default=90s).
        example_sigma: Example sigma (in sec) to produce output called\
            example_filt.mtx.
        verbose_flag: Switch on diagnostic messages.
        debug_flag: Switch on debugging messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CutoffcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CUTOFFCALC_METADATA)
    params = cutoffcalc_params(input_design=input_design, threshold=threshold, tr=tr, lower_limit=lower_limit, example_sigma=example_sigma, verbose_flag=verbose_flag, debug_flag=debug_flag)
    return cutoffcalc_execute(params, execution)


__all__ = [
    "CUTOFFCALC_METADATA",
    "CutoffcalcOutputs",
    "CutoffcalcParameters",
    "cutoffcalc",
    "cutoffcalc_params",
]
