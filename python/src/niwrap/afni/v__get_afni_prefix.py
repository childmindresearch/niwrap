# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__GET_AFNI_PREFIX_METADATA = Metadata(
    id="ae0f36ac76fa0ee57fb99900eaf3197e4b29bbf6.boutiques",
    name="@GetAfniPrefix",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VGetAfniPrefixParameters = typing.TypedDict('VGetAfniPrefixParameters', {
    "__STYX_TYPE__": typing.Literal["@GetAfniPrefix"],
    "name": InputPathType,
    "suffix": typing.NotRequired[str | None],
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
        "@GetAfniPrefix": v__get_afni_prefix_cargs,
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
        "@GetAfniPrefix": v__get_afni_prefix_outputs,
    }.get(t)


class VGetAfniPrefixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_prefix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__get_afni_prefix_params(
    name: InputPathType,
    suffix: str | None = None,
) -> VGetAfniPrefixParameters:
    """
    Build parameters.
    
    Args:
        name: Input file path for which the AFNI prefix will be extracted.
        suffix: Suffix string to append to the returned prefix.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@GetAfniPrefix",
        "name": name,
    }
    if suffix is not None:
        params["suffix"] = suffix
    return params


def v__get_afni_prefix_cargs(
    params: VGetAfniPrefixParameters,
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
    cargs.append("@GetAfniPrefix")
    cargs.append(execution.input_file(params.get("name")))
    if params.get("suffix") is not None:
        cargs.append(params.get("suffix"))
    return cargs


def v__get_afni_prefix_outputs(
    params: VGetAfniPrefixParameters,
    execution: Execution,
) -> VGetAfniPrefixOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VGetAfniPrefixOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__get_afni_prefix_execute(
    params: VGetAfniPrefixParameters,
    execution: Execution,
) -> VGetAfniPrefixOutputs:
    """
    A tool to extract AFNI prefix from a given file path.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VGetAfniPrefixOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__get_afni_prefix_cargs(params, execution)
    ret = v__get_afni_prefix_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__get_afni_prefix(
    name: InputPathType,
    suffix: str | None = None,
    runner: Runner | None = None,
) -> VGetAfniPrefixOutputs:
    """
    A tool to extract AFNI prefix from a given file path.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        name: Input file path for which the AFNI prefix will be extracted.
        suffix: Suffix string to append to the returned prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniPrefixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_PREFIX_METADATA)
    params = v__get_afni_prefix_params(name=name, suffix=suffix)
    return v__get_afni_prefix_execute(params, execution)


__all__ = [
    "VGetAfniPrefixOutputs",
    "VGetAfniPrefixParameters",
    "V__GET_AFNI_PREFIX_METADATA",
    "v__get_afni_prefix",
    "v__get_afni_prefix_params",
]
