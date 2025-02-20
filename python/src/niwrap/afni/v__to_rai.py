# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__TO_RAI_METADATA = Metadata(
    id="ae5bb83cce00bf51d61da1e1b21d495548f69a92.boutiques",
    name="@ToRAI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VToRaiParameters = typing.TypedDict('VToRaiParameters', {
    "__STYX_TYPE__": typing.Literal["@ToRAI"],
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
        "@ToRAI": v__to_rai_cargs,
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
    }.get(t)


class VToRaiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__to_rai(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__to_rai_params(
) -> VToRaiParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ToRAI",
    }
    return params


def v__to_rai_cargs(
    params: VToRaiParameters,
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
    cargs.append("@ToRAI")
    cargs.append("<-xyz")
    cargs.append("X")
    cargs.append("Y")
    cargs.append("Z>")
    cargs.append("<-or")
    cargs.append("ORIENT>")
    return cargs


def v__to_rai_outputs(
    params: VToRaiParameters,
    execution: Execution,
) -> VToRaiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VToRaiOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__to_rai_execute(
    params: VToRaiParameters,
    execution: Execution,
) -> VToRaiOutputs:
    """
    Tool to change the ORIENT coordinates to RAI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VToRaiOutputs`).
    """
    params = execution.params(params)
    cargs = v__to_rai_cargs(params, execution)
    ret = v__to_rai_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__to_rai(
    runner: Runner | None = None,
) -> VToRaiOutputs:
    """
    Tool to change the ORIENT coordinates to RAI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VToRaiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__TO_RAI_METADATA)
    params = v__to_rai_params(
    )
    return v__to_rai_execute(params, execution)


__all__ = [
    "VToRaiOutputs",
    "VToRaiParameters",
    "V__TO_RAI_METADATA",
    "v__to_rai",
    "v__to_rai_params",
]
