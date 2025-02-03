# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_VOLUME_METADATA = Metadata(
    id="90a9e134e9f1f52b94a8a65439a8368906985f96.boutiques",
    name="mris_volume",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisVolumeParameters = typing.TypedDict('MrisVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["mris_volume"],
    "surface_file": InputPathType,
    "verbose_flag": bool,
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
        "mris_volume": mris_volume_cargs,
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


class MrisVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_volume_params(
    surface_file: InputPathType,
    verbose_flag: bool = False,
) -> MrisVolumeParameters:
    """
    Build parameters.
    
    Args:
        surface_file: The closed surface file whose volume is to be computed.
        verbose_flag: Output more messages for verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_volume",
        "surface_file": surface_file,
        "verbose_flag": verbose_flag,
    }
    return params


def mris_volume_cargs(
    params: MrisVolumeParameters,
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
    cargs.append("mris_volume")
    cargs.append(execution.input_file(params.get("surface_file")))
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def mris_volume_outputs(
    params: MrisVolumeParameters,
    execution: Execution,
) -> MrisVolumeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisVolumeOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_volume_execute(
    params: MrisVolumeParameters,
    execution: Execution,
) -> MrisVolumeOutputs:
    """
    A tool for computing the volume of a closed surface using a divergence formula.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisVolumeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_volume_cargs(params, execution)
    ret = mris_volume_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_volume(
    surface_file: InputPathType,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> MrisVolumeOutputs:
    """
    A tool for computing the volume of a closed surface using a divergence formula.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface_file: The closed surface file whose volume is to be computed.
        verbose_flag: Output more messages for verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_VOLUME_METADATA)
    params = mris_volume_params(surface_file=surface_file, verbose_flag=verbose_flag)
    return mris_volume_execute(params, execution)


__all__ = [
    "MRIS_VOLUME_METADATA",
    "MrisVolumeOutputs",
    "mris_volume",
    "mris_volume_params",
]
