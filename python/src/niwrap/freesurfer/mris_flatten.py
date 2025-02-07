# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_FLATTEN_METADATA = Metadata(
    id="c7d351c53d00767efc2edd450d96b67b497b34f9.boutiques",
    name="mris_flatten",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisFlattenParameters = typing.TypedDict('MrisFlattenParameters', {
    "__STYX_TYPE__": typing.Literal["mris_flatten"],
    "input_patch": InputPathType,
    "output_patch": str,
    "iterations": typing.NotRequired[float | None],
    "distances": typing.NotRequired[list[float] | None],
    "dilations": typing.NotRequired[float | None],
    "random_seed": typing.NotRequired[float | None],
    "copy_coords": typing.NotRequired[str | None],
    "norand": bool,
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
        "mris_flatten": mris_flatten_cargs,
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
        "mris_flatten": mris_flatten_outputs,
    }.get(t)


class MrisFlattenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_flatten(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_patch_file: OutputPathType
    """Output flattened surface patch"""


def mris_flatten_params(
    input_patch: InputPathType,
    output_patch: str,
    iterations: float | None = None,
    distances: list[float] | None = None,
    dilations: float | None = None,
    random_seed: float | None = None,
    copy_coords: str | None = None,
    norand: bool = False,
) -> MrisFlattenParameters:
    """
    Build parameters.
    
    Args:
        input_patch: Input surface patch.
        output_patch: Output flattened surface patch.
        iterations: Write out the surface every # of iterations.
        distances: Specify size of neighborhood and number of vertices at each\
            distance to be used in the optimization.
        dilations: Specify the number of times to dilate the ripped edges to\
            ensure a clean cut.
        random_seed: Set the random seed to a specific value so that flattening\
            is repeatable.
        copy_coords: Copy xyz coords from surface before flattening.
        norand: Set the random seed to 0 so that flattening is repeatable.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_flatten",
        "input_patch": input_patch,
        "output_patch": output_patch,
        "norand": norand,
    }
    if iterations is not None:
        params["iterations"] = iterations
    if distances is not None:
        params["distances"] = distances
    if dilations is not None:
        params["dilations"] = dilations
    if random_seed is not None:
        params["random_seed"] = random_seed
    if copy_coords is not None:
        params["copy_coords"] = copy_coords
    return params


def mris_flatten_cargs(
    params: MrisFlattenParameters,
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
    cargs.append("mris_flatten")
    cargs.append(execution.input_file(params.get("input_patch")))
    cargs.append(params.get("output_patch"))
    if params.get("iterations") is not None:
        cargs.extend([
            "-w",
            str(params.get("iterations"))
        ])
    if params.get("distances") is not None:
        cargs.extend([
            "-distances",
            *map(str, params.get("distances"))
        ])
    if params.get("dilations") is not None:
        cargs.extend([
            "-dilate",
            str(params.get("dilations"))
        ])
    if params.get("random_seed") is not None:
        cargs.extend([
            "-seed",
            str(params.get("random_seed"))
        ])
    if params.get("copy_coords") is not None:
        cargs.extend([
            "-copy-coords",
            params.get("copy_coords")
        ])
    if params.get("norand"):
        cargs.append("-norand")
    return cargs


def mris_flatten_outputs(
    params: MrisFlattenParameters,
    execution: Execution,
) -> MrisFlattenOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisFlattenOutputs(
        root=execution.output_file("."),
        output_patch_file=execution.output_file(params.get("output_patch")),
    )
    return ret


def mris_flatten_execute(
    params: MrisFlattenParameters,
    execution: Execution,
) -> MrisFlattenOutputs:
    """
    This program will flatten a surface patch.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisFlattenOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_flatten_cargs(params, execution)
    ret = mris_flatten_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_flatten(
    input_patch: InputPathType,
    output_patch: str,
    iterations: float | None = None,
    distances: list[float] | None = None,
    dilations: float | None = None,
    random_seed: float | None = None,
    copy_coords: str | None = None,
    norand: bool = False,
    runner: Runner | None = None,
) -> MrisFlattenOutputs:
    """
    This program will flatten a surface patch.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_patch: Input surface patch.
        output_patch: Output flattened surface patch.
        iterations: Write out the surface every # of iterations.
        distances: Specify size of neighborhood and number of vertices at each\
            distance to be used in the optimization.
        dilations: Specify the number of times to dilate the ripped edges to\
            ensure a clean cut.
        random_seed: Set the random seed to a specific value so that flattening\
            is repeatable.
        copy_coords: Copy xyz coords from surface before flattening.
        norand: Set the random seed to 0 so that flattening is repeatable.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisFlattenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_FLATTEN_METADATA)
    params = mris_flatten_params(input_patch=input_patch, output_patch=output_patch, iterations=iterations, distances=distances, dilations=dilations, random_seed=random_seed, copy_coords=copy_coords, norand=norand)
    return mris_flatten_execute(params, execution)


__all__ = [
    "MRIS_FLATTEN_METADATA",
    "MrisFlattenOutputs",
    "MrisFlattenParameters",
    "mris_flatten",
    "mris_flatten_params",
]
