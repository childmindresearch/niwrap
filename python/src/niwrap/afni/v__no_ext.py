# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__NO_EXT_METADATA = Metadata(
    id="e146bd1bed02e711ff41cccbd0a20832085fd087.boutiques",
    name="@NoExt",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VNoExtParameters = typing.TypedDict('VNoExtParameters', {
    "__STYX_TYPE__": typing.Literal["@NoExt"],
    "extensions": typing.NotRequired[list[str] | None],
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
        "@NoExt": v__no_ext_cargs,
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
        "@NoExt": v__no_ext_outputs,
    }.get(t)


class VNoExtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__no_ext(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """File name with specified extensions removed"""


def v__no_ext_params(
    extensions: list[str] | None = None,
) -> VNoExtParameters:
    """
    Build parameters.
    
    Args:
        extensions: Extensions to be removed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@NoExt",
    }
    if extensions is not None:
        params["extensions"] = extensions
    return params


def v__no_ext_cargs(
    params: VNoExtParameters,
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
    cargs.append("@NoExt")
    cargs.append("<inputfile>")
    if params.get("extensions") is not None:
        cargs.extend(params.get("extensions"))
    return cargs


def v__no_ext_outputs(
    params: VNoExtParameters,
    execution: Execution,
) -> VNoExtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VNoExtOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("output"),
    )
    return ret


def v__no_ext_execute(
    params: VNoExtParameters,
    execution: Execution,
) -> VNoExtOutputs:
    """
    Tool for removing specified extensions from filenames.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VNoExtOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__no_ext_cargs(params, execution)
    ret = v__no_ext_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__no_ext(
    extensions: list[str] | None = None,
    runner: Runner | None = None,
) -> VNoExtOutputs:
    """
    Tool for removing specified extensions from filenames.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        extensions: Extensions to be removed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VNoExtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__NO_EXT_METADATA)
    params = v__no_ext_params(extensions=extensions)
    return v__no_ext_execute(params, execution)


__all__ = [
    "VNoExtOutputs",
    "VNoExtParameters",
    "V__NO_EXT_METADATA",
    "v__no_ext",
    "v__no_ext_params",
]
