# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ABOVERLAP_METADATA = Metadata(
    id="ce33e10c4b1ac12e30e9f2905df1b25512061469.boutiques",
    name="3dABoverlap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAboverlapParameters = typing.TypedDict('V3dAboverlapParameters', {
    "__STYX_TYPE__": typing.Literal["3dABoverlap"],
    "dataset_a": InputPathType,
    "dataset_b": InputPathType,
    "no_automask": bool,
    "quiet": bool,
    "verbose": bool,
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
        "3dABoverlap": v_3d_aboverlap_cargs,
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


class V3dAboverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_aboverlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_aboverlap_params(
    dataset_a: InputPathType,
    dataset_b: InputPathType,
    no_automask: bool = False,
    quiet: bool = False,
    verbose: bool = False,
) -> V3dAboverlapParameters:
    """
    Build parameters.
    
    Args:
        dataset_a: First input dataset.
        dataset_b: Second input dataset.
        no_automask: Consider input datasets as masks (automask does not work\
            on mask datasets).
        quiet: Be as quiet as possible (without being entirely mute).
        verbose: Print out some progress reports (to stderr).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dABoverlap",
        "dataset_a": dataset_a,
        "dataset_b": dataset_b,
        "no_automask": no_automask,
        "quiet": quiet,
        "verbose": verbose,
    }
    return params


def v_3d_aboverlap_cargs(
    params: V3dAboverlapParameters,
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
    cargs.append("3dABoverlap")
    cargs.append(execution.input_file(params.get("dataset_a")))
    cargs.append(execution.input_file(params.get("dataset_b")))
    if params.get("no_automask"):
        cargs.append("-no_automask")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("verbose"):
        cargs.append("-verb")
    return cargs


def v_3d_aboverlap_outputs(
    params: V3dAboverlapParameters,
    execution: Execution,
) -> V3dAboverlapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAboverlapOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_aboverlap_execute(
    params: V3dAboverlapParameters,
    execution: Execution,
) -> V3dAboverlapOutputs:
    """
    Counts various metrics about how the automasks of datasets A and B overlap or
    don't overlap.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAboverlapOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_aboverlap_cargs(params, execution)
    ret = v_3d_aboverlap_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_aboverlap(
    dataset_a: InputPathType,
    dataset_b: InputPathType,
    no_automask: bool = False,
    quiet: bool = False,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dAboverlapOutputs:
    """
    Counts various metrics about how the automasks of datasets A and B overlap or
    don't overlap.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset_a: First input dataset.
        dataset_b: Second input dataset.
        no_automask: Consider input datasets as masks (automask does not work\
            on mask datasets).
        quiet: Be as quiet as possible (without being entirely mute).
        verbose: Print out some progress reports (to stderr).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAboverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ABOVERLAP_METADATA)
    params = v_3d_aboverlap_params(dataset_a=dataset_a, dataset_b=dataset_b, no_automask=no_automask, quiet=quiet, verbose=verbose)
    return v_3d_aboverlap_execute(params, execution)


__all__ = [
    "V3dAboverlapOutputs",
    "V3dAboverlapParameters",
    "V_3D_ABOVERLAP_METADATA",
    "v_3d_aboverlap",
    "v_3d_aboverlap_params",
]
