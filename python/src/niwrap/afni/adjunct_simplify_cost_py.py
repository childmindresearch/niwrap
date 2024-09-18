# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_SIMPLIFY_COST_PY_METADATA = Metadata(
    id="28763ae4c27632e0897a1ce4d2b959e057a6e685.boutiques",
    name="adjunct_simplify_cost.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctSimplifyCostPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_simplify_cost_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_simplify_cost_py(
    cost_function: str,
    runner: Runner | None = None,
) -> AdjunctSimplifyCostPyOutputs:
    """
    Simplifies a cost function name by removing the '+' and anything following it.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_simplify_cost.py.html
    
    Args:
        cost_function: The cost function name to be simplified.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctSimplifyCostPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_SIMPLIFY_COST_PY_METADATA)
    cargs = []
    cargs.append("adjunct_simplify_cost.py")
    cargs.append(cost_function)
    ret = AdjunctSimplifyCostPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_SIMPLIFY_COST_PY_METADATA",
    "AdjunctSimplifyCostPyOutputs",
    "adjunct_simplify_cost_py",
]