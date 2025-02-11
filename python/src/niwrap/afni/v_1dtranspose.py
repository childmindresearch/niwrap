# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1DTRANSPOSE_METADATA = Metadata(
    id="8aeb8ffe1bc2def81876ed4d22208279a8077957.boutiques",
    name="1dtranspose",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dtransposeParameters = typing.TypedDict('V1dtransposeParameters', {
    "__STYX_TYPE__": typing.Literal["1dtranspose"],
    "infile": InputPathType,
    "outfile": typing.NotRequired[str | None],
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
        "1dtranspose": v_1dtranspose_cargs,
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
        "1dtranspose": v_1dtranspose_outputs,
    }.get(t)


class V1dtransposeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dtranspose(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Transposed output file"""


def v_1dtranspose_params(
    infile: InputPathType,
    outfile: str | None = None,
) -> V1dtransposeParameters:
    """
    Build parameters.
    
    Args:
        infile: Input file (e.g. data.1D).
        outfile: Output file (e.g. transposed_data.1D), or '-' to write to\
            stdout.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dtranspose",
        "infile": infile,
    }
    if outfile is not None:
        params["outfile"] = outfile
    return params


def v_1dtranspose_cargs(
    params: V1dtransposeParameters,
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
    cargs.append("1dtranspose")
    cargs.append(execution.input_file(params.get("infile")))
    if params.get("outfile") is not None:
        cargs.append(params.get("outfile"))
    return cargs


def v_1dtranspose_outputs(
    params: V1dtransposeParameters,
    execution: Execution,
) -> V1dtransposeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dtransposeOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("outfile")) if (params.get("outfile") is not None) else None,
    )
    return ret


def v_1dtranspose_execute(
    params: V1dtransposeParameters,
    execution: Execution,
) -> V1dtransposeOutputs:
    """
    Transpose an AFNI *.1D file (ASCII list of numbers arranged in columns).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dtransposeOutputs`).
    """
    cargs = v_1dtranspose_cargs(params, execution)
    ret = v_1dtranspose_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1dtranspose(
    infile: InputPathType,
    outfile: str | None = None,
    runner: Runner | None = None,
) -> V1dtransposeOutputs:
    """
    Transpose an AFNI *.1D file (ASCII list of numbers arranged in columns).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input file (e.g. data.1D).
        outfile: Output file (e.g. transposed_data.1D), or '-' to write to\
            stdout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dtransposeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DTRANSPOSE_METADATA)
    params = v_1dtranspose_params(infile=infile, outfile=outfile)
    return v_1dtranspose_execute(params, execution)


__all__ = [
    "V1dtransposeOutputs",
    "V1dtransposeParameters",
    "V_1DTRANSPOSE_METADATA",
    "v_1dtranspose",
    "v_1dtranspose_params",
]
