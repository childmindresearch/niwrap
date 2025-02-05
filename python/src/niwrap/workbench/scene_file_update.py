# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCENE_FILE_UPDATE_METADATA = Metadata(
    id="b6179bfd334c9b44420e1478f7f7ccaab55f5073.boutiques",
    name="scene-file-update",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SceneFileUpdateCopyMapOnePaletteParameters = typing.TypedDict('SceneFileUpdateCopyMapOnePaletteParameters', {
    "__STYX_TYPE__": typing.Literal["copy_map_one_palette"],
    "data_file_name_suffix": str,
})
SceneFileUpdateDataFileAddParameters = typing.TypedDict('SceneFileUpdateDataFileAddParameters', {
    "__STYX_TYPE__": typing.Literal["data_file_add"],
    "name_of_data_file": str,
})
SceneFileUpdateDataFileRemoveParameters = typing.TypedDict('SceneFileUpdateDataFileRemoveParameters', {
    "__STYX_TYPE__": typing.Literal["data_file_remove"],
    "name_of_data_file": str,
})
SceneFileUpdateParameters = typing.TypedDict('SceneFileUpdateParameters', {
    "__STYX_TYPE__": typing.Literal["scene-file-update"],
    "input_scene_file": str,
    "output_scene_file": str,
    "scene_name_or_number": str,
    "opt_fix_map_palette_settings": bool,
    "opt_remove_missing_files": bool,
    "opt_error": bool,
    "opt_verbose": bool,
    "copy_map_one_palette": typing.NotRequired[list[SceneFileUpdateCopyMapOnePaletteParameters] | None],
    "data_file_add": typing.NotRequired[list[SceneFileUpdateDataFileAddParameters] | None],
    "data_file_remove": typing.NotRequired[list[SceneFileUpdateDataFileRemoveParameters] | None],
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
        "scene-file-update": scene_file_update_cargs,
        "copy_map_one_palette": scene_file_update_copy_map_one_palette_cargs,
        "data_file_add": scene_file_update_data_file_add_cargs,
        "data_file_remove": scene_file_update_data_file_remove_cargs,
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


def scene_file_update_copy_map_one_palette_params(
    data_file_name_suffix: str,
) -> SceneFileUpdateCopyMapOnePaletteParameters:
    """
    Build parameters.
    
    Args:
        data_file_name_suffix: Name of palette mapped data file (cifti, metric,\
            volume).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "copy_map_one_palette",
        "data_file_name_suffix": data_file_name_suffix,
    }
    return params


def scene_file_update_copy_map_one_palette_cargs(
    params: SceneFileUpdateCopyMapOnePaletteParameters,
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
    cargs.append("-copy-map-one-palette")
    cargs.append(params.get("data_file_name_suffix"))
    return cargs


def scene_file_update_data_file_add_params(
    name_of_data_file: str,
) -> SceneFileUpdateDataFileAddParameters:
    """
    Build parameters.
    
    Args:
        name_of_data_file: Name of data file. If a data file not in the current\
            directory, it is best to use an absolute path (a relative path may\
            work). Instead of a data file, this value may be the name of a text\
            file (must end in ".txt") that contains the names of one or more data\
            files, one per line.\
            Example on UNIX to create a text file containing all CIFTI scalar\
            files in the current directory with absolute paths:\
            ls -d $PWD/*dscalar.nii > file.txt.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "data_file_add",
        "name_of_data_file": name_of_data_file,
    }
    return params


def scene_file_update_data_file_add_cargs(
    params: SceneFileUpdateDataFileAddParameters,
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
    cargs.append("-data-file-add")
    cargs.append(params.get("name_of_data_file"))
    return cargs


def scene_file_update_data_file_remove_params(
    name_of_data_file: str,
) -> SceneFileUpdateDataFileRemoveParameters:
    """
    Build parameters.
    
    Args:
        name_of_data_file: Name of data file. If a data file not in the current\
            directory, it is best to use an absolute path (a relative path may\
            work). Instead of a data file, this value may be the name of a text\
            file (must end in ".txt") that contains the names of one or more data\
            files, one per line.\
            Example on UNIX to create a text file containing all CIFTI scalar\
            files in the current directory with absolute paths:\
            ls -d $PWD/*dscalar.nii > file.txt.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "data_file_remove",
        "name_of_data_file": name_of_data_file,
    }
    return params


def scene_file_update_data_file_remove_cargs(
    params: SceneFileUpdateDataFileRemoveParameters,
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
    cargs.append("-data-file-remove")
    cargs.append(params.get("name_of_data_file"))
    return cargs


class SceneFileUpdateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_update(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_update_params(
    input_scene_file: str,
    output_scene_file: str,
    scene_name_or_number: str,
    opt_fix_map_palette_settings: bool = False,
    opt_remove_missing_files: bool = False,
    opt_error: bool = False,
    opt_verbose: bool = False,
    copy_map_one_palette: list[SceneFileUpdateCopyMapOnePaletteParameters] | None = None,
    data_file_add: list[SceneFileUpdateDataFileAddParameters] | None = None,
    data_file_remove: list[SceneFileUpdateDataFileRemoveParameters] | None = None,
) -> SceneFileUpdateParameters:
    """
    Build parameters.
    
    Args:
        input_scene_file: the input scene file.
        output_scene_file: the new scene file to create.
        scene_name_or_number: name or number (starting at one) of the scene in\
            the scene file.
        opt_fix_map_palette_settings: Fix palette settings for files with\
            change in number of maps.
        opt_remove_missing_files: Remove missing files from SpecFile.
        opt_error: Abort command if there is an error performing any of the\
            operations on the scene file.
        opt_verbose: Print names of files that have palettes updated.
        copy_map_one_palette: Copy palettes settings from first map to all maps\
            in a data file.
        data_file_add: Add a data file to scene's loaded files.
        data_file_remove: Remove a data file from scene's loaded files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "scene-file-update",
        "input_scene_file": input_scene_file,
        "output_scene_file": output_scene_file,
        "scene_name_or_number": scene_name_or_number,
        "opt_fix_map_palette_settings": opt_fix_map_palette_settings,
        "opt_remove_missing_files": opt_remove_missing_files,
        "opt_error": opt_error,
        "opt_verbose": opt_verbose,
    }
    if copy_map_one_palette is not None:
        params["copy_map_one_palette"] = copy_map_one_palette
    if data_file_add is not None:
        params["data_file_add"] = data_file_add
    if data_file_remove is not None:
        params["data_file_remove"] = data_file_remove
    return params


def scene_file_update_cargs(
    params: SceneFileUpdateParameters,
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
    cargs.append("-scene-file-update")
    cargs.append(params.get("input_scene_file"))
    cargs.append(params.get("output_scene_file"))
    cargs.append(params.get("scene_name_or_number"))
    if params.get("opt_fix_map_palette_settings"):
        cargs.append("-fix-map-palette-settings")
    if params.get("opt_remove_missing_files"):
        cargs.append("-remove-missing-files")
    if params.get("opt_error"):
        cargs.append("-error")
    if params.get("opt_verbose"):
        cargs.append("-verbose")
    if params.get("copy_map_one_palette") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("copy_map_one_palette")] for a in c])
    if params.get("data_file_add") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("data_file_add")] for a in c])
    if params.get("data_file_remove") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("data_file_remove")] for a in c])
    return cargs


def scene_file_update_outputs(
    params: SceneFileUpdateParameters,
    execution: Execution,
) -> SceneFileUpdateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SceneFileUpdateOutputs(
        root=execution.output_file("."),
    )
    return ret


def scene_file_update_execute(
    params: SceneFileUpdateParameters,
    execution: Execution,
) -> SceneFileUpdateOutputs:
    """
    Update scene file.
    
    This command will update a scene for specific changes in data files.
    
    "-fix-map-palette-settings" will find all data files that have had a change
    in the number of maps since the scene scene was created. If the file has its
    "Apply to All Maps" property enabled, the palette setting in the first map
    is copied to all maps in the file. Note: This modifies the palette settings
    for the file in the scene (data file is NOT modified).
    
    "-copy-map-one-palette" will copy the palette settings from the first map to
    all other maps in a data file. This option is typically used when the number
    of maps in a data file changes. It changes the palette settings in the scene
    that are applied to the data file when the scene is loaded (the data file is
    not modified). The name of the data file specified on the command line is
    matched to the end of file names in the scene. This allows matching multiple
    files if their names end with the same characters. It also allows including
    a relative path when there is more than one file with the same name but in
    different paths and only one of the files to be updated.
    
    "-remove-missing-files" Any files that fail to load when the scene is read
    will be removed from the scene. Thus, if one deletes files prior to running
    with this option, the deleted files are removed from the scene.
    
    "-error" If this option is provided and there is an error while performing
    any of the scene operations, the command will immediately cease processing
    and the output scene file will not be created. Otherwise any errors will be
    listed after the command finishes.
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SceneFileUpdateOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = scene_file_update_cargs(params, execution)
    ret = scene_file_update_outputs(params, execution)
    execution.run(cargs)
    return ret


def scene_file_update(
    input_scene_file: str,
    output_scene_file: str,
    scene_name_or_number: str,
    opt_fix_map_palette_settings: bool = False,
    opt_remove_missing_files: bool = False,
    opt_error: bool = False,
    opt_verbose: bool = False,
    copy_map_one_palette: list[SceneFileUpdateCopyMapOnePaletteParameters] | None = None,
    data_file_add: list[SceneFileUpdateDataFileAddParameters] | None = None,
    data_file_remove: list[SceneFileUpdateDataFileRemoveParameters] | None = None,
    runner: Runner | None = None,
) -> SceneFileUpdateOutputs:
    """
    Update scene file.
    
    This command will update a scene for specific changes in data files.
    
    "-fix-map-palette-settings" will find all data files that have had a change
    in the number of maps since the scene scene was created. If the file has its
    "Apply to All Maps" property enabled, the palette setting in the first map
    is copied to all maps in the file. Note: This modifies the palette settings
    for the file in the scene (data file is NOT modified).
    
    "-copy-map-one-palette" will copy the palette settings from the first map to
    all other maps in a data file. This option is typically used when the number
    of maps in a data file changes. It changes the palette settings in the scene
    that are applied to the data file when the scene is loaded (the data file is
    not modified). The name of the data file specified on the command line is
    matched to the end of file names in the scene. This allows matching multiple
    files if their names end with the same characters. It also allows including
    a relative path when there is more than one file with the same name but in
    different paths and only one of the files to be updated.
    
    "-remove-missing-files" Any files that fail to load when the scene is read
    will be removed from the scene. Thus, if one deletes files prior to running
    with this option, the deleted files are removed from the scene.
    
    "-error" If this option is provided and there is an error while performing
    any of the scene operations, the command will immediately cease processing
    and the output scene file will not be created. Otherwise any errors will be
    listed after the command finishes.
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_scene_file: the input scene file.
        output_scene_file: the new scene file to create.
        scene_name_or_number: name or number (starting at one) of the scene in\
            the scene file.
        opt_fix_map_palette_settings: Fix palette settings for files with\
            change in number of maps.
        opt_remove_missing_files: Remove missing files from SpecFile.
        opt_error: Abort command if there is an error performing any of the\
            operations on the scene file.
        opt_verbose: Print names of files that have palettes updated.
        copy_map_one_palette: Copy palettes settings from first map to all maps\
            in a data file.
        data_file_add: Add a data file to scene's loaded files.
        data_file_remove: Remove a data file from scene's loaded files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SceneFileUpdateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCENE_FILE_UPDATE_METADATA)
    params = scene_file_update_params(input_scene_file=input_scene_file, output_scene_file=output_scene_file, scene_name_or_number=scene_name_or_number, opt_fix_map_palette_settings=opt_fix_map_palette_settings, opt_remove_missing_files=opt_remove_missing_files, opt_error=opt_error, opt_verbose=opt_verbose, copy_map_one_palette=copy_map_one_palette, data_file_add=data_file_add, data_file_remove=data_file_remove)
    return scene_file_update_execute(params, execution)


__all__ = [
    "SCENE_FILE_UPDATE_METADATA",
    "SceneFileUpdateCopyMapOnePaletteParameters",
    "SceneFileUpdateDataFileAddParameters",
    "SceneFileUpdateDataFileRemoveParameters",
    "SceneFileUpdateOutputs",
    "SceneFileUpdateParameters",
    "scene_file_update",
    "scene_file_update_copy_map_one_palette_params",
    "scene_file_update_data_file_add_params",
    "scene_file_update_data_file_remove_params",
    "scene_file_update_params",
]
