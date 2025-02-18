# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BALLOON_METADATA = Metadata(
    id="d38a0b74f4c93d5365bdded27c362f4ddc6e6b5f.boutiques",
    name="balloon",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
BalloonParameters = typing.TypedDict('BalloonParameters', {
    "__STYX_TYPE__": typing.Literal["balloon"],
    "tr": float,
    "num_scans": int,
    "event_times": InputPathType,
    "t_fall": typing.NotRequired[list[float] | None],
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
        "balloon": balloon_cargs,
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


class BalloonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `balloon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def balloon_params(
    tr: float,
    num_scans: int,
    event_times: InputPathType,
    t_fall: list[float] | None = None,
) -> BalloonParameters:
    """
    Build parameters.
    
    Args:
        tr: Scan repetition time in seconds (TR), the interval at which the\
            output curve will be sampled.
        num_scans: Number of scans (N), the output curve will comprise this\
            number of samples.
        event_times: The name of a file containing the event timings, in\
            seconds, as ASCII strings separated by white space, with time 0 being\
            the time at which the initial scan occurred.
        t_fall: Haemodynamic fall time in seconds (typically between 4s and\
            6s).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "balloon",
        "tr": tr,
        "num_scans": num_scans,
        "event_times": event_times,
    }
    if t_fall is not None:
        params["t_fall"] = t_fall
    return params


def balloon_cargs(
    params: BalloonParameters,
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
    cargs.append("balloon")
    cargs.append(str(params.get("tr")))
    cargs.append(str(params.get("num_scans")))
    cargs.append(execution.input_file(params.get("event_times")))
    if params.get("t_fall") is not None:
        cargs.extend(map(str, params.get("t_fall")))
    return cargs


def balloon_outputs(
    params: BalloonParameters,
    execution: Execution,
) -> BalloonOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BalloonOutputs(
        root=execution.output_file("."),
    )
    return ret


def balloon_execute(
    params: BalloonParameters,
    execution: Execution,
) -> BalloonOutputs:
    """
    Simulation of haemodynamic response using the balloon model. Based on the
    theoretical model proposed by Buxton et al. (1998).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BalloonOutputs`).
    """
    params = execution.params(params)
    cargs = balloon_cargs(params, execution)
    ret = balloon_outputs(params, execution)
    execution.run(cargs)
    return ret


def balloon(
    tr: float,
    num_scans: int,
    event_times: InputPathType,
    t_fall: list[float] | None = None,
    runner: Runner | None = None,
) -> BalloonOutputs:
    """
    Simulation of haemodynamic response using the balloon model. Based on the
    theoretical model proposed by Buxton et al. (1998).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        tr: Scan repetition time in seconds (TR), the interval at which the\
            output curve will be sampled.
        num_scans: Number of scans (N), the output curve will comprise this\
            number of samples.
        event_times: The name of a file containing the event timings, in\
            seconds, as ASCII strings separated by white space, with time 0 being\
            the time at which the initial scan occurred.
        t_fall: Haemodynamic fall time in seconds (typically between 4s and\
            6s).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BalloonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BALLOON_METADATA)
    params = balloon_params(tr=tr, num_scans=num_scans, event_times=event_times, t_fall=t_fall)
    return balloon_execute(params, execution)


__all__ = [
    "BALLOON_METADATA",
    "BalloonOutputs",
    "BalloonParameters",
    "balloon",
    "balloon_params",
]
