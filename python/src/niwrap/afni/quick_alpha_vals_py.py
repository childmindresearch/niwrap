# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

QUICK_ALPHA_VALS_PY_METADATA = Metadata(
    id="467c10597885378ee65e5261792a6d6f5203efb5.boutiques",
    name="quick.alpha.vals.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
QuickAlphaValsPyParameters = typing.TypedDict('QuickAlphaValsPyParameters', {
    "__STYX_TYPE__": typing.Literal["quick.alpha.vals.py"],
    "niter": typing.NotRequired[int | None],
    "max_file": InputPathType,
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
        "quick.alpha.vals.py": quick_alpha_vals_py_cargs,
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
        "quick.alpha.vals.py": quick_alpha_vals_py_outputs,
    }.get(t)


class QuickAlphaValsPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quick_alpha_vals_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    alpha_table: OutputPathType
    """Generated alpha table file"""


def quick_alpha_vals_py_params(
    max_file: InputPathType,
    niter: int | None = None,
) -> QuickAlphaValsPyParameters:
    """
    Build parameters.
    
    Args:
        max_file: File containing maximum z values.
        niter: Number of iterations that should be in the z file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "quick.alpha.vals.py",
        "max_file": max_file,
    }
    if niter is not None:
        params["niter"] = niter
    return params


def quick_alpha_vals_py_cargs(
    params: QuickAlphaValsPyParameters,
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
    cargs.append("quick.alpha.vals.py")
    if params.get("niter") is not None:
        cargs.extend([
            "-niter",
            str(params.get("niter"))
        ])
    cargs.append(execution.input_file(params.get("max_file")))
    return cargs


def quick_alpha_vals_py_outputs(
    params: QuickAlphaValsPyParameters,
    execution: Execution,
) -> QuickAlphaValsPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = QuickAlphaValsPyOutputs(
        root=execution.output_file("."),
        alpha_table=execution.output_file("alpha_table.txt"),
    )
    return ret


def quick_alpha_vals_py_execute(
    params: QuickAlphaValsPyParameters,
    execution: Execution,
) -> QuickAlphaValsPyOutputs:
    """
    Generate an alpha table from slow_surf_clustsim.py results.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `QuickAlphaValsPyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = quick_alpha_vals_py_cargs(params, execution)
    ret = quick_alpha_vals_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def quick_alpha_vals_py(
    max_file: InputPathType,
    niter: int | None = None,
    runner: Runner | None = None,
) -> QuickAlphaValsPyOutputs:
    """
    Generate an alpha table from slow_surf_clustsim.py results.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        max_file: File containing maximum z values.
        niter: Number of iterations that should be in the z file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuickAlphaValsPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUICK_ALPHA_VALS_PY_METADATA)
    params = quick_alpha_vals_py_params(niter=niter, max_file=max_file)
    return quick_alpha_vals_py_execute(params, execution)


__all__ = [
    "QUICK_ALPHA_VALS_PY_METADATA",
    "QuickAlphaValsPyOutputs",
    "QuickAlphaValsPyParameters",
    "quick_alpha_vals_py",
    "quick_alpha_vals_py_params",
]
