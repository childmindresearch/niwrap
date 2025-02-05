# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DRENAME_METADATA = Metadata(
    id="3c508d8f5e6d69689dd267857ef13efbf3693249.boutiques",
    name="3drename",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3drenameParameters = typing.TypedDict('V3drenameParameters', {
    "__STYX_TYPE__": typing.Literal["3drename"],
    "old_prefix": str,
    "new_prefix": str,
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
        "3drename": v_3drename_cargs,
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


class V3drenameOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3drename(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3drename_params(
    old_prefix: str,
    new_prefix: str,
) -> V3drenameParameters:
    """
    Build parameters.
    
    Args:
        old_prefix: Old prefix of the datasets to rename.
        new_prefix: New prefix for the datasets.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3drename",
        "old_prefix": old_prefix,
        "new_prefix": new_prefix,
    }
    return params


def v_3drename_cargs(
    params: V3drenameParameters,
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
    cargs.append("3drename")
    cargs.append(params.get("old_prefix"))
    cargs.append(params.get("new_prefix"))
    return cargs


def v_3drename_outputs(
    params: V3drenameParameters,
    execution: Execution,
) -> V3drenameOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3drenameOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3drename_execute(
    params: V3drenameParameters,
    execution: Execution,
) -> V3drenameOutputs:
    """
    Tool to rename AFNI datasets by changing the dataset prefix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3drenameOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3drename_cargs(params, execution)
    ret = v_3drename_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3drename(
    old_prefix: str,
    new_prefix: str,
    runner: Runner | None = None,
) -> V3drenameOutputs:
    """
    Tool to rename AFNI datasets by changing the dataset prefix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        old_prefix: Old prefix of the datasets to rename.
        new_prefix: New prefix for the datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3drenameOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DRENAME_METADATA)
    params = v_3drename_params(old_prefix=old_prefix, new_prefix=new_prefix)
    return v_3drename_execute(params, execution)


__all__ = [
    "V3drenameOutputs",
    "V3drenameParameters",
    "V_3DRENAME_METADATA",
    "v_3drename",
    "v_3drename_params",
]
