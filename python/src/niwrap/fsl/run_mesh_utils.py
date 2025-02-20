# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_MESH_UTILS_METADATA = Metadata(
    id="f37cf2d8f5013ba6fbfc7ef807691e24ce397261.boutiques",
    name="run_mesh_utils",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


RunMeshUtilsParameters = typing.TypedDict('RunMeshUtilsParameters', {
    "__STYX_TYPE__": typing.Literal["run_mesh_utils"],
    "base_mesh": InputPathType,
    "output_image": str,
    "input_image": typing.NotRequired[InputPathType | None],
    "second_input_image": typing.NotRequired[InputPathType | None],
    "weighting_image_force": typing.NotRequired[InputPathType | None],
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
        "run_mesh_utils": run_mesh_utils_cargs,
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
        "run_mesh_utils": run_mesh_utils_outputs,
    }.get(t)


class RunMeshUtilsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_mesh_utils(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """Output image file"""


def run_mesh_utils_params(
    base_mesh: InputPathType,
    output_image: str,
    input_image: InputPathType | None = None,
    second_input_image: InputPathType | None = None,
    weighting_image_force: InputPathType | None = None,
) -> RunMeshUtilsParameters:
    """
    Build parameters.
    
    Args:
        base_mesh: Filename of base mesh.
        output_image: Filename of output image.
        input_image: Filename of input image.
        second_input_image: Filename of second input image.
        weighting_image_force: Weighting image force.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_mesh_utils",
        "base_mesh": base_mesh,
        "output_image": output_image,
    }
    if input_image is not None:
        params["input_image"] = input_image
    if second_input_image is not None:
        params["second_input_image"] = second_input_image
    if weighting_image_force is not None:
        params["weighting_image_force"] = weighting_image_force
    return params


def run_mesh_utils_cargs(
    params: RunMeshUtilsParameters,
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
    cargs.append("run_mesh_utils")
    cargs.append(execution.input_file(params.get("base_mesh")))
    cargs.extend([
        "-o",
        params.get("output_image")
    ])
    if params.get("input_image") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("input_image"))
        ])
    if params.get("second_input_image") is not None:
        cargs.extend([
            "-j",
            execution.input_file(params.get("second_input_image"))
        ])
    if params.get("weighting_image_force") is not None:
        cargs.extend([
            "-p",
            execution.input_file(params.get("weighting_image_force"))
        ])
    cargs.append("[OPTIONAL_PARAMS...]")
    return cargs


def run_mesh_utils_outputs(
    params: RunMeshUtilsParameters,
    execution: Execution,
) -> RunMeshUtilsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunMeshUtilsOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")),
    )
    return ret


def run_mesh_utils_execute(
    params: RunMeshUtilsParameters,
    execution: Execution,
) -> RunMeshUtilsOutputs:
    """
    A tool for various mesh operations as part of FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunMeshUtilsOutputs`).
    """
    params = execution.params(params)
    cargs = run_mesh_utils_cargs(params, execution)
    ret = run_mesh_utils_outputs(params, execution)
    execution.run(cargs)
    return ret


def run_mesh_utils(
    base_mesh: InputPathType,
    output_image: str,
    input_image: InputPathType | None = None,
    second_input_image: InputPathType | None = None,
    weighting_image_force: InputPathType | None = None,
    runner: Runner | None = None,
) -> RunMeshUtilsOutputs:
    """
    A tool for various mesh operations as part of FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        base_mesh: Filename of base mesh.
        output_image: Filename of output image.
        input_image: Filename of input image.
        second_input_image: Filename of second input image.
        weighting_image_force: Weighting image force.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunMeshUtilsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_MESH_UTILS_METADATA)
    params = run_mesh_utils_params(
        base_mesh=base_mesh,
        output_image=output_image,
        input_image=input_image,
        second_input_image=second_input_image,
        weighting_image_force=weighting_image_force,
    )
    return run_mesh_utils_execute(params, execution)


__all__ = [
    "RUN_MESH_UTILS_METADATA",
    "RunMeshUtilsOutputs",
    "RunMeshUtilsParameters",
    "run_mesh_utils",
    "run_mesh_utils_params",
]
