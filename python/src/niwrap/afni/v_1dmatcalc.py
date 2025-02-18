# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1DMATCALC_METADATA = Metadata(
    id="363bd7932d82bc77c3f5fe6e0307d7efddad15de.boutiques",
    name="1dmatcalc",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dmatcalcParameters = typing.TypedDict('V1dmatcalcParameters', {
    "__STYX_TYPE__": typing.Literal["1dmatcalc"],
    "expression": typing.NotRequired[str | None],
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
        "1dmatcalc": v_1dmatcalc_cargs,
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
        "1dmatcalc": v_1dmatcalc_outputs,
    }.get(t)


class V1dmatcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dmatcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file resulting from the evaluated expression"""


def v_1dmatcalc_params(
    expression: str | None = None,
) -> V1dmatcalcParameters:
    """
    Build parameters.
    
    Args:
        expression: Expression to evaluate the RPN matrix-valued operations.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dmatcalc",
    }
    if expression is not None:
        params["expression"] = expression
    return params


def v_1dmatcalc_cargs(
    params: V1dmatcalcParameters,
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
    cargs.append("1dmatcalc")
    if params.get("expression") is not None:
        cargs.append(params.get("expression"))
    return cargs


def v_1dmatcalc_outputs(
    params: V1dmatcalcParameters,
    execution: Execution,
) -> V1dmatcalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dmatcalcOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[OUTPUT_FILE]"),
    )
    return ret


def v_1dmatcalc_execute(
    params: V1dmatcalcParameters,
    execution: Execution,
) -> V1dmatcalcOutputs:
    """
    A tool to evaluate space-delimited RPN (Reverse Polish Notation) matrix-valued
    expressions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dmatcalcOutputs`).
    """
    params = execution.params(params)
    cargs = v_1dmatcalc_cargs(params, execution)
    ret = v_1dmatcalc_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1dmatcalc(
    expression: str | None = None,
    runner: Runner | None = None,
) -> V1dmatcalcOutputs:
    """
    A tool to evaluate space-delimited RPN (Reverse Polish Notation) matrix-valued
    expressions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        expression: Expression to evaluate the RPN matrix-valued operations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dmatcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DMATCALC_METADATA)
    params = v_1dmatcalc_params(expression=expression)
    return v_1dmatcalc_execute(params, execution)


__all__ = [
    "V1dmatcalcOutputs",
    "V1dmatcalcParameters",
    "V_1DMATCALC_METADATA",
    "v_1dmatcalc",
    "v_1dmatcalc_params",
]
