# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIGLOSS_METADATA = Metadata(
    id="925adf9e97058d87551f4f3a27c9b5b1c1c21397.boutiques",
    name="sigloss",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SiglossParameters = typing.TypedDict('SiglossParameters', {
    "__STYX_TYPE__": typing.Literal["sigloss"],
    "input_b0map": InputPathType,
    "output_sigloss": str,
    "input_mask": typing.NotRequired[InputPathType | None],
    "echo_time": typing.NotRequired[float | None],
    "slice_direction": typing.NotRequired[typing.Literal["x", "y", "z"] | None],
    "verbose_flag": bool,
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
        "sigloss": sigloss_cargs,
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


class SiglossOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sigloss(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def sigloss_params(
    input_b0map: InputPathType,
    output_sigloss: str,
    input_mask: InputPathType | None = None,
    echo_time: float | None = None,
    slice_direction: typing.Literal["x", "y", "z"] | None = None,
    verbose_flag: bool = False,
) -> SiglossParameters:
    """
    Build parameters.
    
    Args:
        input_b0map: Input b0 map image filename (in rad/s).
        output_sigloss: Output signal loss image filename.
        input_mask: Input mask filename.
        echo_time: Echo time (in seconds).
        slice_direction: Slice direction (either x, y or z).
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sigloss",
        "input_b0map": input_b0map,
        "output_sigloss": output_sigloss,
        "verbose_flag": verbose_flag,
    }
    if input_mask is not None:
        params["input_mask"] = input_mask
    if echo_time is not None:
        params["echo_time"] = echo_time
    if slice_direction is not None:
        params["slice_direction"] = slice_direction
    return params


def sigloss_cargs(
    params: SiglossParameters,
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
    cargs.append("sigloss")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_b0map"))
    ])
    cargs.extend([
        "-s",
        params.get("output_sigloss")
    ])
    if params.get("input_mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("input_mask"))
        ])
    if params.get("echo_time") is not None:
        cargs.extend([
            "--te",
            str(params.get("echo_time"))
        ])
    if params.get("slice_direction") is not None:
        cargs.extend([
            "-d",
            params.get("slice_direction")
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def sigloss_outputs(
    params: SiglossParameters,
    execution: Execution,
) -> SiglossOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SiglossOutputs(
        root=execution.output_file("."),
    )
    return ret


def sigloss_execute(
    params: SiglossParameters,
    execution: Execution,
) -> SiglossOutputs:
    """
    Estimates signal loss from a field map (in rad/s).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SiglossOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = sigloss_cargs(params, execution)
    ret = sigloss_outputs(params, execution)
    execution.run(cargs)
    return ret


def sigloss(
    input_b0map: InputPathType,
    output_sigloss: str,
    input_mask: InputPathType | None = None,
    echo_time: float | None = None,
    slice_direction: typing.Literal["x", "y", "z"] | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> SiglossOutputs:
    """
    Estimates signal loss from a field map (in rad/s).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_b0map: Input b0 map image filename (in rad/s).
        output_sigloss: Output signal loss image filename.
        input_mask: Input mask filename.
        echo_time: Echo time (in seconds).
        slice_direction: Slice direction (either x, y or z).
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SiglossOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIGLOSS_METADATA)
    params = sigloss_params(input_b0map=input_b0map, output_sigloss=output_sigloss, input_mask=input_mask, echo_time=echo_time, slice_direction=slice_direction, verbose_flag=verbose_flag)
    return sigloss_execute(params, execution)


__all__ = [
    "SIGLOSS_METADATA",
    "SiglossOutputs",
    "SiglossParameters",
    "sigloss",
    "sigloss_params",
]
