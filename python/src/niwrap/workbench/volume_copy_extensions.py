# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_COPY_EXTENSIONS_METADATA = Metadata(
    id="862abf7914f0edcebc84a7fc1d70c95d8938e52d.boutiques",
    name="volume-copy-extensions",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeCopyExtensionsParameters = typing.TypedDict('VolumeCopyExtensionsParameters', {
    "__STYX_TYPE__": typing.Literal["volume-copy-extensions"],
    "data_volume": InputPathType,
    "extension_volume": InputPathType,
    "volume_out": str,
    "opt_drop_unknown": bool,
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
        "volume-copy-extensions": volume_copy_extensions_cargs,
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
        "volume-copy-extensions": volume_copy_extensions_outputs,
    }.get(t)


class VolumeCopyExtensionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_copy_extensions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_copy_extensions_params(
    data_volume: InputPathType,
    extension_volume: InputPathType,
    volume_out: str,
    opt_drop_unknown: bool = False,
) -> VolumeCopyExtensionsParameters:
    """
    Build parameters.
    
    Args:
        data_volume: the volume file containing the voxel data to use.
        extension_volume: the volume file containing the extensions to use.
        volume_out: the output volume.
        opt_drop_unknown: don't copy extensions that workbench doesn't\
            understand.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-copy-extensions",
        "data_volume": data_volume,
        "extension_volume": extension_volume,
        "volume_out": volume_out,
        "opt_drop_unknown": opt_drop_unknown,
    }
    return params


def volume_copy_extensions_cargs(
    params: VolumeCopyExtensionsParameters,
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
    cargs.append("-volume-copy-extensions")
    cargs.append(execution.input_file(params.get("data_volume")))
    cargs.append(execution.input_file(params.get("extension_volume")))
    cargs.append(params.get("volume_out"))
    if params.get("opt_drop_unknown"):
        cargs.append("-drop-unknown")
    return cargs


def volume_copy_extensions_outputs(
    params: VolumeCopyExtensionsParameters,
    execution: Execution,
) -> VolumeCopyExtensionsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeCopyExtensionsOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_copy_extensions_execute(
    params: VolumeCopyExtensionsParameters,
    execution: Execution,
) -> VolumeCopyExtensionsOutputs:
    """
    Copy extended data to another volume file.
    
    This command copies the information in a volume file that isn't a critical
    part of the standard header or data matrix, e.g. map names, palette
    settings, label tables. If -drop-unknown is not specified, it also copies
    similar kinds of information set by other software.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeCopyExtensionsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = volume_copy_extensions_cargs(params, execution)
    ret = volume_copy_extensions_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_copy_extensions(
    data_volume: InputPathType,
    extension_volume: InputPathType,
    volume_out: str,
    opt_drop_unknown: bool = False,
    runner: Runner | None = None,
) -> VolumeCopyExtensionsOutputs:
    """
    Copy extended data to another volume file.
    
    This command copies the information in a volume file that isn't a critical
    part of the standard header or data matrix, e.g. map names, palette
    settings, label tables. If -drop-unknown is not specified, it also copies
    similar kinds of information set by other software.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        data_volume: the volume file containing the voxel data to use.
        extension_volume: the volume file containing the extensions to use.
        volume_out: the output volume.
        opt_drop_unknown: don't copy extensions that workbench doesn't\
            understand.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeCopyExtensionsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_COPY_EXTENSIONS_METADATA)
    params = volume_copy_extensions_params(data_volume=data_volume, extension_volume=extension_volume, volume_out=volume_out, opt_drop_unknown=opt_drop_unknown)
    return volume_copy_extensions_execute(params, execution)


__all__ = [
    "VOLUME_COPY_EXTENSIONS_METADATA",
    "VolumeCopyExtensionsOutputs",
    "VolumeCopyExtensionsParameters",
    "volume_copy_extensions",
    "volume_copy_extensions_params",
]
