# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCENE_FILE_RELOCATE_METADATA = Metadata(
    id="4d5785c213ba8c43cc0d1cb433a896970dc23e80.boutiques",
    name="scene-file-relocate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SceneFileRelocateParameters = typing.TypedDict('SceneFileRelocateParameters', {
    "__STYX_TYPE__": typing.Literal["scene-file-relocate"],
    "input_scene": str,
    "output_scene": str,
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
        "scene-file-relocate": scene_file_relocate_cargs,
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


class SceneFileRelocateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_relocate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_relocate_params(
    input_scene: str,
    output_scene: str,
) -> SceneFileRelocateParameters:
    """
    Build parameters.
    
    Args:
        input_scene: the scene file to use.
        output_scene: output - the new scene file to create.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "scene-file-relocate",
        "input_scene": input_scene,
        "output_scene": output_scene,
    }
    return params


def scene_file_relocate_cargs(
    params: SceneFileRelocateParameters,
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
    cargs.append("wb_command")
    cargs.append("-scene-file-relocate")
    cargs.append(params.get("input_scene"))
    cargs.append(params.get("output_scene"))
    return cargs


def scene_file_relocate_outputs(
    params: SceneFileRelocateParameters,
    execution: Execution,
) -> SceneFileRelocateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SceneFileRelocateOutputs(
        root=execution.output_file("."),
    )
    return ret


def scene_file_relocate_execute(
    params: SceneFileRelocateParameters,
    execution: Execution,
) -> SceneFileRelocateOutputs:
    """
    Recreate scene file in new location.
    
    Scene files contain internal relative paths, such that moving or copying a
    scene file will cause it to lose track of the files it refers to. This
    command makes a modified copy of the scene file, changing the relative paths
    to refer to the new relative locations of the files.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SceneFileRelocateOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = scene_file_relocate_cargs(params, execution)
    ret = scene_file_relocate_outputs(params, execution)
    execution.run(cargs)
    return ret


def scene_file_relocate(
    input_scene: str,
    output_scene: str,
    runner: Runner | None = None,
) -> SceneFileRelocateOutputs:
    """
    Recreate scene file in new location.
    
    Scene files contain internal relative paths, such that moving or copying a
    scene file will cause it to lose track of the files it refers to. This
    command makes a modified copy of the scene file, changing the relative paths
    to refer to the new relative locations of the files.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_scene: the scene file to use.
        output_scene: output - the new scene file to create.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SceneFileRelocateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCENE_FILE_RELOCATE_METADATA)
    params = scene_file_relocate_params(input_scene=input_scene, output_scene=output_scene)
    return scene_file_relocate_execute(params, execution)


__all__ = [
    "SCENE_FILE_RELOCATE_METADATA",
    "SceneFileRelocateOutputs",
    "SceneFileRelocateParameters",
    "scene_file_relocate",
    "scene_file_relocate_params",
]
