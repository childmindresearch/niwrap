# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DCOPY_METADATA = Metadata(
    id="4b8187d004c6f4ba95518e709ad1f9b3eb4ed322.boutiques",
    name="3dcopy",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dcopyParameters = typing.TypedDict('V3dcopyParameters', {
    "__STYX_TYPE__": typing.Literal["3dcopy"],
    "verbose": bool,
    "denote": bool,
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
        "3dcopy": v_3dcopy_cargs,
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


class V3dcopyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dcopy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3dcopy_params(
    verbose: bool = False,
    denote: bool = False,
) -> V3dcopyParameters:
    """
    Build parameters.
    
    Args:
        verbose: Print progress reports.
        denote: Remove any Notes from the file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dcopy",
        "verbose": verbose,
        "denote": denote,
    }
    return params


def v_3dcopy_cargs(
    params: V3dcopyParameters,
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
    cargs.append("3dcopy")
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("denote"):
        cargs.append("-denote")
    cargs.append("{OLD_PREFIX}+{VIEW}")
    cargs.append("{NEW_PREFIX}")
    return cargs


def v_3dcopy_outputs(
    params: V3dcopyParameters,
    execution: Execution,
) -> V3dcopyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dcopyOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3dcopy_execute(
    params: V3dcopyParameters,
    execution: Execution,
) -> V3dcopyOutputs:
    """
    3dcopy copies datasets with or without altering prefixes and converting formats.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dcopyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3dcopy_cargs(params, execution)
    ret = v_3dcopy_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dcopy(
    verbose: bool = False,
    denote: bool = False,
    runner: Runner | None = None,
) -> V3dcopyOutputs:
    """
    3dcopy copies datasets with or without altering prefixes and converting formats.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        verbose: Print progress reports.
        denote: Remove any Notes from the file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dcopyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DCOPY_METADATA)
    params = v_3dcopy_params(verbose=verbose, denote=denote)
    return v_3dcopy_execute(params, execution)


__all__ = [
    "V3dcopyOutputs",
    "V3dcopyParameters",
    "V_3DCOPY_METADATA",
    "v_3dcopy",
    "v_3dcopy_params",
]
