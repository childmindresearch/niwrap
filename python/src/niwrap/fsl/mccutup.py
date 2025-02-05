# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MCCUTUP_METADATA = Metadata(
    id="3bcabc27a5688982bd8610840860d2e83796bc90.boutiques",
    name="mccutup",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MccutupParameters = typing.TypedDict('MccutupParameters', {
    "__STYX_TYPE__": typing.Literal["mccutup"],
    "input": InputPathType,
    "output_file": typing.NotRequired[str | None],
    "param1": typing.NotRequired[str | None],
    "param2": typing.NotRequired[str | None],
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
        "mccutup": mccutup_cargs,
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
        "mccutup": mccutup_outputs,
    }
    return vt.get(t)


class MccutupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mccutup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType | None
    """Output file"""


def mccutup_params(
    input_: InputPathType,
    output_file: str | None = None,
    param1: str | None = None,
    param2: str | None = None,
) -> MccutupParameters:
    """
    Build parameters.
    
    Args:
        input_: Input file.
        output_file: Specify output file name.
        param1: Parameter 1 description.
        param2: Parameter 2 description.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mccutup",
        "input": input_,
    }
    if output_file is not None:
        params["output_file"] = output_file
    if param1 is not None:
        params["param1"] = param1
    if param2 is not None:
        params["param2"] = param2
    return params


def mccutup_cargs(
    params: MccutupParameters,
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
    cargs.append("mccutup")
    cargs.append(execution.input_file(params.get("input")))
    if params.get("output_file") is not None:
        cargs.extend([
            "--output",
            params.get("output_file")
        ])
    if params.get("param1") is not None:
        cargs.extend([
            "--param1",
            params.get("param1")
        ])
    if params.get("param2") is not None:
        cargs.extend([
            "--param2",
            params.get("param2")
        ])
    return cargs


def mccutup_outputs(
    params: MccutupParameters,
    execution: Execution,
) -> MccutupOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MccutupOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def mccutup_execute(
    params: MccutupParameters,
    execution: Execution,
) -> MccutupOutputs:
    """
    FSL mccutup tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MccutupOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mccutup_cargs(params, execution)
    ret = mccutup_outputs(params, execution)
    execution.run(cargs)
    return ret


def mccutup(
    input_: InputPathType,
    output_file: str | None = None,
    param1: str | None = None,
    param2: str | None = None,
    runner: Runner | None = None,
) -> MccutupOutputs:
    """
    FSL mccutup tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_: Input file.
        output_file: Specify output file name.
        param1: Parameter 1 description.
        param2: Parameter 2 description.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MccutupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MCCUTUP_METADATA)
    params = mccutup_params(input_=input_, output_file=output_file, param1=param1, param2=param2)
    return mccutup_execute(params, execution)


__all__ = [
    "MCCUTUP_METADATA",
    "MccutupOutputs",
    "MccutupParameters",
    "mccutup",
    "mccutup_params",
]
