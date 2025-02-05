# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SBTIV_METADATA = Metadata(
    id="f635fd3b0d71913a55d64eab8618d5ffd1066300.boutiques",
    name="sbtiv",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SbtivParameters = typing.TypedDict('SbtivParameters', {
    "__STYX_TYPE__": typing.Literal["sbtiv"],
    "input_file": InputPathType,
    "output_file": typing.NotRequired[str | None],
    "labels_file": typing.NotRequired[InputPathType | None],
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
        "sbtiv": sbtiv_cargs,
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
        "sbtiv": sbtiv_outputs,
    }
    return vt.get(t)


class SbtivOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sbtiv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Intracranial stats output file."""


def sbtiv_params(
    input_file: InputPathType,
    output_file: str | None = None,
    labels_file: InputPathType | None = None,
) -> SbtivParameters:
    """
    Build parameters.
    
    Args:
        input_file: Volume stats input file.
        output_file: Intracranial stats output file.
        labels_file: File containing a list of intracranial structure\
            labelnames to include in the calculation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sbtiv",
        "input_file": input_file,
    }
    if output_file is not None:
        params["output_file"] = output_file
    if labels_file is not None:
        params["labels_file"] = labels_file
    return params


def sbtiv_cargs(
    params: SbtivParameters,
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
    cargs.append("sbtiv")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("output_file") is not None:
        cargs.extend([
            "-o",
            params.get("output_file")
        ])
    if params.get("labels_file") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("labels_file"))
        ])
    return cargs


def sbtiv_outputs(
    params: SbtivParameters,
    execution: Execution,
) -> SbtivOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SbtivOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def sbtiv_execute(
    params: SbtivParameters,
    execution: Execution,
) -> SbtivOutputs:
    """
    Tool to calculate the total intracranial volume of a subject by summing
    individual volumes computed by samseg.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SbtivOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = sbtiv_cargs(params, execution)
    ret = sbtiv_outputs(params, execution)
    execution.run(cargs)
    return ret


def sbtiv(
    input_file: InputPathType,
    output_file: str | None = None,
    labels_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> SbtivOutputs:
    """
    Tool to calculate the total intracranial volume of a subject by summing
    individual volumes computed by samseg.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Volume stats input file.
        output_file: Intracranial stats output file.
        labels_file: File containing a list of intracranial structure\
            labelnames to include in the calculation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SbtivOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SBTIV_METADATA)
    params = sbtiv_params(input_file=input_file, output_file=output_file, labels_file=labels_file)
    return sbtiv_execute(params, execution)


__all__ = [
    "SBTIV_METADATA",
    "SbtivOutputs",
    "SbtivParameters",
    "sbtiv",
    "sbtiv_params",
]
