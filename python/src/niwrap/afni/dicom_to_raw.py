# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

DICOM_TO_RAW_METADATA = Metadata(
    id="396e9c2761351d014db7d547d4758c9e39ab070d",
    name="dicom_to_raw",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class DicomToRawOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dicom_to_raw(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_raw_file: OutputPathType
    """Output raw file(s)"""


def dicom_to_raw(
    input_dicom: InputPathType,
    runner: Runner | None = None,
) -> DicomToRawOutputs:
    """
    dicom_to_raw by AFNI Team.
    
    Reads images from DICOM file and writes them to raw file(s).
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/dicom_to_raw.html
    
    Args:
        input_dicom: Input DICOM file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DicomToRawOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DICOM_TO_RAW_METADATA)
    cargs = []
    cargs.append("dicom_to_raw")
    cargs.append(execution.input_file(input_dicom))
    ret = DicomToRawOutputs(
        root=execution.output_file("."),
        output_raw_file=execution.output_file(f"{pathlib.Path(input_dicom).name}.raw.0001"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DICOM_TO_RAW_METADATA",
    "DicomToRawOutputs",
    "dicom_to_raw",
]
