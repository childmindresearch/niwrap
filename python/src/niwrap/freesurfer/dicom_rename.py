# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DICOM_RENAME_METADATA = Metadata(
    id="2eb87845c3a6be71bcd6bb57089f0cd879da57d4.boutiques",
    name="dicom-rename",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DicomRenameParameters = typing.TypedDict('DicomRenameParameters', {
    "__STYX_TYPE__": typing.Literal["dicom-rename"],
    "input_files": list[InputPathType],
    "output_base": str,
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
        "dicom-rename": dicom_rename_cargs,
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
    vt = {
        "dicom-rename": dicom_rename_outputs,
    }
    return vt.get(t)


class DicomRenameOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dicom_rename(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    renamed_dicom: OutputPathType
    """Renamed output DICOM file with series and image numbers."""


def dicom_rename_params(
    input_files: list[InputPathType],
    output_base: str,
) -> DicomRenameParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input DICOM files to be renamed.
        output_base: Base name for output files that includes series and image\
            numbers.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dicom-rename",
        "input_files": input_files,
        "output_base": output_base,
    }
    return params


def dicom_rename_cargs(
    params: DicomRenameParameters,
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
    cargs.extend([
        "-rename",
        "dicom" + "".join([execution.input_file(f) for f in params.get("input_files")])
    ])
    cargs.extend([
        "--o",
        params.get("output_base")
    ])
    return cargs


def dicom_rename_outputs(
    params: DicomRenameParameters,
    execution: Execution,
) -> DicomRenameOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DicomRenameOutputs(
        root=execution.output_file("."),
        renamed_dicom=execution.output_file(params.get("output_base") + "-SSS-IIIII.dcm"),
    )
    return ret


def dicom_rename_execute(
    params: DicomRenameParameters,
    execution: Execution,
) -> DicomRenameOutputs:
    """
    Copies dicom file(s) to new path with more meaningful names.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DicomRenameOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dicom_rename_cargs(params, execution)
    ret = dicom_rename_outputs(params, execution)
    execution.run(cargs)
    return ret


def dicom_rename(
    input_files: list[InputPathType],
    output_base: str,
    runner: Runner | None = None,
) -> DicomRenameOutputs:
    """
    Copies dicom file(s) to new path with more meaningful names.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input DICOM files to be renamed.
        output_base: Base name for output files that includes series and image\
            numbers.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DicomRenameOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DICOM_RENAME_METADATA)
    params = dicom_rename_params(input_files=input_files, output_base=output_base)
    return dicom_rename_execute(params, execution)


__all__ = [
    "DICOM_RENAME_METADATA",
    "DicomRenameOutputs",
    "DicomRenameParameters",
    "dicom_rename",
    "dicom_rename_params",
]
