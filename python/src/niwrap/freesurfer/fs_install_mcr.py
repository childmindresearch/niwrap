# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FS_INSTALL_MCR_METADATA = Metadata(
    id="3368d00255c0d7e5b75947a021056a82a28657ea.boutiques",
    name="fs_install_mcr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FsInstallMcrParameters = typing.TypedDict('FsInstallMcrParameters', {
    "__STYX_TYPE__": typing.Literal["fs_install_mcr"],
    "mcr_version": str,
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
        "fs_install_mcr": fs_install_mcr_cargs,
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


class FsInstallMcrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fs_install_mcr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fs_install_mcr_params(
    mcr_version: str,
) -> FsInstallMcrParameters:
    """
    Build parameters.
    
    Args:
        mcr_version: Specify the MATLAB Compiler Runtime (MCR) version to\
            install.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fs_install_mcr",
        "mcr_version": mcr_version,
    }
    return params


def fs_install_mcr_cargs(
    params: FsInstallMcrParameters,
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
    cargs.append("fs_install_mcr")
    cargs.append(params.get("mcr_version"))
    return cargs


def fs_install_mcr_outputs(
    params: FsInstallMcrParameters,
    execution: Execution,
) -> FsInstallMcrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsInstallMcrOutputs(
        root=execution.output_file("."),
    )
    return ret


def fs_install_mcr_execute(
    params: FsInstallMcrParameters,
    execution: Execution,
) -> FsInstallMcrOutputs:
    """
    MCR installation tool for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsInstallMcrOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fs_install_mcr_cargs(params, execution)
    ret = fs_install_mcr_outputs(params, execution)
    execution.run(cargs)
    return ret


def fs_install_mcr(
    mcr_version: str,
    runner: Runner | None = None,
) -> FsInstallMcrOutputs:
    """
    MCR installation tool for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mcr_version: Specify the MATLAB Compiler Runtime (MCR) version to\
            install.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsInstallMcrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_INSTALL_MCR_METADATA)
    params = fs_install_mcr_params(mcr_version=mcr_version)
    return fs_install_mcr_execute(params, execution)


__all__ = [
    "FS_INSTALL_MCR_METADATA",
    "FsInstallMcrOutputs",
    "fs_install_mcr",
    "fs_install_mcr_params",
]
