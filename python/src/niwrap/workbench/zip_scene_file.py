# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ZIP_SCENE_FILE_METADATA = Metadata(
    id="9da95fbe632d10dacb4c060224ca406ac914b355.boutiques",
    name="zip-scene-file",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
ZipSceneFileParameters = typing.TypedDict('ZipSceneFileParameters', {
    "__STYX_TYPE__": typing.Literal["zip-scene-file"],
    "scene_file": str,
    "extract_folder": str,
    "zip_file": str,
    "opt_base_dir_directory": typing.NotRequired[str | None],
    "opt_skip_missing": bool,
    "opt_write_scene_file": bool,
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
        "zip-scene-file": zip_scene_file_cargs,
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


class ZipSceneFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `zip_scene_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def zip_scene_file_params(
    scene_file: str,
    extract_folder: str,
    zip_file: str,
    opt_base_dir_directory: str | None = None,
    opt_skip_missing: bool = False,
    opt_write_scene_file: bool = False,
) -> ZipSceneFileParameters:
    """
    Build parameters.
    
    Args:
        scene_file: the scene file to make the zip file from.
        extract_folder: the name of the folder created when the zip file is\
            unzipped.
        zip_file: out - the zip file that will be created.
        opt_base_dir_directory: specify a directory that all data files are\
            somewhere within, this will become the root of the zipfile's directory\
            structure: the directory.
        opt_skip_missing: any missing files will generate only warnings, and\
            the zip file will be created anyway.
        opt_write_scene_file: rewrite the scene file before zipping, to store a\
            new base path or fix extra '..'s in paths that might break.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "zip-scene-file",
        "scene_file": scene_file,
        "extract_folder": extract_folder,
        "zip_file": zip_file,
        "opt_skip_missing": opt_skip_missing,
        "opt_write_scene_file": opt_write_scene_file,
    }
    if opt_base_dir_directory is not None:
        params["opt_base_dir_directory"] = opt_base_dir_directory
    return params


def zip_scene_file_cargs(
    params: ZipSceneFileParameters,
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
    cargs.append("-zip-scene-file")
    cargs.append(params.get("scene_file"))
    cargs.append(params.get("extract_folder"))
    cargs.append(params.get("zip_file"))
    if params.get("opt_base_dir_directory") is not None:
        cargs.extend([
            "-base-dir",
            params.get("opt_base_dir_directory")
        ])
    if params.get("opt_skip_missing"):
        cargs.append("-skip-missing")
    if params.get("opt_write_scene_file"):
        cargs.append("-write-scene-file")
    return cargs


def zip_scene_file_outputs(
    params: ZipSceneFileParameters,
    execution: Execution,
) -> ZipSceneFileOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ZipSceneFileOutputs(
        root=execution.output_file("."),
    )
    return ret


def zip_scene_file_execute(
    params: ZipSceneFileParameters,
    execution: Execution,
) -> ZipSceneFileOutputs:
    """
    Zip a scene file and its data files.
    
    If zip-file already exists, it will be overwritten. If -base-dir is not
    specified, the base directory will be automatically set to the lowest level
    directory containing all files. The scene file must contain only relative
    paths, and no data files may be outside the base directory.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ZipSceneFileOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = zip_scene_file_cargs(params, execution)
    ret = zip_scene_file_outputs(params, execution)
    execution.run(cargs)
    return ret


def zip_scene_file(
    scene_file: str,
    extract_folder: str,
    zip_file: str,
    opt_base_dir_directory: str | None = None,
    opt_skip_missing: bool = False,
    opt_write_scene_file: bool = False,
    runner: Runner | None = None,
) -> ZipSceneFileOutputs:
    """
    Zip a scene file and its data files.
    
    If zip-file already exists, it will be overwritten. If -base-dir is not
    specified, the base directory will be automatically set to the lowest level
    directory containing all files. The scene file must contain only relative
    paths, and no data files may be outside the base directory.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        scene_file: the scene file to make the zip file from.
        extract_folder: the name of the folder created when the zip file is\
            unzipped.
        zip_file: out - the zip file that will be created.
        opt_base_dir_directory: specify a directory that all data files are\
            somewhere within, this will become the root of the zipfile's directory\
            structure: the directory.
        opt_skip_missing: any missing files will generate only warnings, and\
            the zip file will be created anyway.
        opt_write_scene_file: rewrite the scene file before zipping, to store a\
            new base path or fix extra '..'s in paths that might break.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ZipSceneFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ZIP_SCENE_FILE_METADATA)
    params = zip_scene_file_params(scene_file=scene_file, extract_folder=extract_folder, zip_file=zip_file, opt_base_dir_directory=opt_base_dir_directory, opt_skip_missing=opt_skip_missing, opt_write_scene_file=opt_write_scene_file)
    return zip_scene_file_execute(params, execution)


__all__ = [
    "ZIP_SCENE_FILE_METADATA",
    "ZipSceneFileOutputs",
    "zip_scene_file",
    "zip_scene_file_params",
]
