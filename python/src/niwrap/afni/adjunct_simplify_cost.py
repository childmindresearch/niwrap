# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_SIMPLIFY_COST_METADATA = Metadata(
    id="0291c293f6b2eaf6626f15fdc0c7c7079ef500e7.boutiques",
    name="adjunct_simplify_cost",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AdjunctSimplifyCostParameters = typing.TypedDict('AdjunctSimplifyCostParameters', {
    "__STYX_TYPE__": typing.Literal["adjunct_simplify_cost"],
    "cost_function": str,
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
        "adjunct_simplify_cost": adjunct_simplify_cost_cargs,
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


class AdjunctSimplifyCostOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_simplify_cost(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_simplify_cost_params(
    cost_function: str,
) -> AdjunctSimplifyCostParameters:
    """
    Build parameters.
    
    Args:
        cost_function: The cost function name to be simplified.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "adjunct_simplify_cost",
        "cost_function": cost_function,
    }
    return params


def adjunct_simplify_cost_cargs(
    params: AdjunctSimplifyCostParameters,
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
    cargs.append("adjunct_simplify_cost.py")
    cargs.append(params.get("cost_function"))
    return cargs


def adjunct_simplify_cost_outputs(
    params: AdjunctSimplifyCostParameters,
    execution: Execution,
) -> AdjunctSimplifyCostOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AdjunctSimplifyCostOutputs(
        root=execution.output_file("."),
    )
    return ret


def adjunct_simplify_cost_execute(
    params: AdjunctSimplifyCostParameters,
    execution: Execution,
) -> AdjunctSimplifyCostOutputs:
    """
    Simplifies a cost function name by removing the '+' and anything following it.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AdjunctSimplifyCostOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = adjunct_simplify_cost_cargs(params, execution)
    ret = adjunct_simplify_cost_outputs(params, execution)
    execution.run(cargs)
    return ret


def adjunct_simplify_cost(
    cost_function: str,
    runner: Runner | None = None,
) -> AdjunctSimplifyCostOutputs:
    """
    Simplifies a cost function name by removing the '+' and anything following it.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        cost_function: The cost function name to be simplified.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctSimplifyCostOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_SIMPLIFY_COST_METADATA)
    params = adjunct_simplify_cost_params(cost_function=cost_function)
    return adjunct_simplify_cost_execute(params, execution)


__all__ = [
    "ADJUNCT_SIMPLIFY_COST_METADATA",
    "AdjunctSimplifyCostOutputs",
    "AdjunctSimplifyCostParameters",
    "adjunct_simplify_cost",
    "adjunct_simplify_cost_params",
]
