# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__NP_METADATA = Metadata(
    id="19475e309cca046197768d1ade01d7e521898bd3.boutiques",
    name="@np",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VNpParameters = typing.TypedDict('VNpParameters', {
    "__STYX_TYPE__": typing.Literal["@np"],
    "prefix": str,
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
        "@np": v__np_cargs,
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
        "@np": v__np_outputs,
    }.get(t)


class VNpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__np(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output text file with the appropriate new prefix."""


def v__np_params(
    prefix: str,
) -> VNpParameters:
    """
    Build parameters.
    
    Args:
        prefix: The prefix to be checked.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@np",
        "prefix": prefix,
    }
    return params


def v__np_cargs(
    params: VNpParameters,
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
    cargs.append("@np")
    cargs.append(params.get("prefix"))
    return cargs


def v__np_outputs(
    params: VNpParameters,
    execution: Execution,
) -> VNpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VNpOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("appropriate_prefix.txt"),
    )
    return ret


def v__np_execute(
    params: VNpParameters,
    execution: Execution,
) -> VNpOutputs:
    """
    Finds an appropriate new prefix to use, given the files you already have in your
    directory. It automatically creates a valid prefix when you are repeatedly
    running similar commands but do not want to delete previous output.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VNpOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__np_cargs(params, execution)
    ret = v__np_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__np(
    prefix: str,
    runner: Runner | None = None,
) -> VNpOutputs:
    """
    Finds an appropriate new prefix to use, given the files you already have in your
    directory. It automatically creates a valid prefix when you are repeatedly
    running similar commands but do not want to delete previous output.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: The prefix to be checked.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VNpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__NP_METADATA)
    params = v__np_params(prefix=prefix)
    return v__np_execute(params, execution)


__all__ = [
    "VNpOutputs",
    "VNpParameters",
    "V__NP_METADATA",
    "v__np",
    "v__np_params",
]
