# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CP_DICOM_METADATA = Metadata(
    id="e87057efacb16ed69de0523e99719b16d1c3fb64.boutiques",
    name="cp-dicom",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
CpDicomParameters = typing.TypedDict('CpDicomParameters', {
    "__STYX_TYPE__": typing.Literal["cp-dicom"],
    "dicom_dir": str,
    "output_dir": str,
    "debug": bool,
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
        "cp-dicom": cp_dicom_cargs,
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


class CpDicomOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cp_dicom(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cp_dicom_params(
    dicom_dir: str,
    output_dir: str,
    debug: bool = False,
) -> CpDicomParameters:
    """
    Build parameters.
    
    Args:
        dicom_dir: Directory containing DICOM files.
        output_dir: Output directory where sorted DICOM files will be stored.
        debug: Print additional debug information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cp-dicom",
        "dicom_dir": dicom_dir,
        "output_dir": output_dir,
        "debug": debug,
    }
    return params


def cp_dicom_cargs(
    params: CpDicomParameters,
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
    cargs.append("cp-dicom")
    cargs.extend([
        "-d",
        params.get("dicom_dir")
    ])
    cargs.extend([
        "-o",
        params.get("output_dir")
    ])
    if params.get("debug"):
        cargs.append("-debug")
    return cargs


def cp_dicom_outputs(
    params: CpDicomParameters,
    execution: Execution,
) -> CpDicomOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CpDicomOutputs(
        root=execution.output_file("."),
    )
    return ret


def cp_dicom_execute(
    params: CpDicomParameters,
    execution: Execution,
) -> CpDicomOutputs:
    """
    Copies DICOM files into separate directories for each series based on DICOM
    headers.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CpDicomOutputs`).
    """
    params = execution.params(params)
    cargs = cp_dicom_cargs(params, execution)
    ret = cp_dicom_outputs(params, execution)
    execution.run(cargs)
    return ret


def cp_dicom(
    dicom_dir: str,
    output_dir: str,
    debug: bool = False,
    runner: Runner | None = None,
) -> CpDicomOutputs:
    """
    Copies DICOM files into separate directories for each series based on DICOM
    headers.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dicom_dir: Directory containing DICOM files.
        output_dir: Output directory where sorted DICOM files will be stored.
        debug: Print additional debug information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CpDicomOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CP_DICOM_METADATA)
    params = cp_dicom_params(dicom_dir=dicom_dir, output_dir=output_dir, debug=debug)
    return cp_dicom_execute(params, execution)


__all__ = [
    "CP_DICOM_METADATA",
    "CpDicomOutputs",
    "CpDicomParameters",
    "cp_dicom",
    "cp_dicom_params",
]
