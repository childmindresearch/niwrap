# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_CORRELATE_METADATA = Metadata(
    id="be0ac3e4b1a192ead53f328b4b3ecf125d8d36fe.boutiques",
    name="1dCorrelate",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dCorrelateParameters = typing.TypedDict('V1dCorrelateParameters', {
    "__STYX_TYPE__": typing.Literal["1dCorrelate"],
    "ktaub": bool,
    "nboot": typing.NotRequired[float | None],
    "alpha": typing.NotRequired[float | None],
    "blk": bool,
    "input_files": list[InputPathType],
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
        "1dCorrelate": v_1d_correlate_cargs,
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


class V1dCorrelateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_correlate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_correlate_params(
    input_files: list[InputPathType],
    ktaub: bool = False,
    nboot: float | None = None,
    alpha: float | None = None,
    blk: bool = False,
) -> V1dCorrelateParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input 1D files.
        ktaub: Kendall's tau_b correlation (popular somewhere, maybe).
        nboot: Set the number of bootstrap replicates.
        alpha: Set the 2-sided confidence interval width to '100-A' percent.
        blk: Alternate flag for variable-length block resampling.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dCorrelate",
        "ktaub": ktaub,
        "blk": blk,
        "input_files": input_files,
    }
    if nboot is not None:
        params["nboot"] = nboot
    if alpha is not None:
        params["alpha"] = alpha
    return params


def v_1d_correlate_cargs(
    params: V1dCorrelateParameters,
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
    cargs.append("1dCorrelate")
    if params.get("ktaub"):
        cargs.append("-Ktaub")
    if params.get("nboot") is not None:
        cargs.extend([
            "-nboot",
            str(params.get("nboot"))
        ])
    if params.get("alpha") is not None:
        cargs.extend([
            "-alpha",
            str(params.get("alpha"))
        ])
    if params.get("blk"):
        cargs.append("-blk")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def v_1d_correlate_outputs(
    params: V1dCorrelateParameters,
    execution: Execution,
) -> V1dCorrelateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dCorrelateOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_1d_correlate_execute(
    params: V1dCorrelateParameters,
    execution: Execution,
) -> V1dCorrelateOutputs:
    """
    1dCorrelate calculates the correlation coefficients between columns of input 1D
    files along with confidence intervals via a bootstrap procedure.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dCorrelateOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_1d_correlate_cargs(params, execution)
    ret = v_1d_correlate_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_correlate(
    input_files: list[InputPathType],
    ktaub: bool = False,
    nboot: float | None = None,
    alpha: float | None = None,
    blk: bool = False,
    runner: Runner | None = None,
) -> V1dCorrelateOutputs:
    """
    1dCorrelate calculates the correlation coefficients between columns of input 1D
    files along with confidence intervals via a bootstrap procedure.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input 1D files.
        ktaub: Kendall's tau_b correlation (popular somewhere, maybe).
        nboot: Set the number of bootstrap replicates.
        alpha: Set the 2-sided confidence interval width to '100-A' percent.
        blk: Alternate flag for variable-length block resampling.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dCorrelateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_CORRELATE_METADATA)
    params = v_1d_correlate_params(ktaub=ktaub, nboot=nboot, alpha=alpha, blk=blk, input_files=input_files)
    return v_1d_correlate_execute(params, execution)


__all__ = [
    "V1dCorrelateOutputs",
    "V1dCorrelateParameters",
    "V_1D_CORRELATE_METADATA",
    "v_1d_correlate",
    "v_1d_correlate_params",
]
