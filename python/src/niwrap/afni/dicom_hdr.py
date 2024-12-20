# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DICOM_HDR_METADATA = Metadata(
    id="f1dd7c5e97c664a21c6f4e09518ffc5513e4e54f.boutiques",
    name="dicom_hdr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class DicomHdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dicom_hdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dicom_hdr(
    files: list[InputPathType],
    hex_: bool = False,
    noname: bool = False,
    sexinfo: bool = False,
    mulfram: bool = False,
    v_dump: float | None = None,
    no_length: bool = False,
    slice_times: bool = False,
    slice_times_verb: bool = False,
    siemens_csa_data: bool = False,
    runner: Runner | None = None,
) -> DicomHdrOutputs:
    """
    A tool to print DICOM file information to stdout.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        files: DICOM file(s) to read.
        hex_: Include hexadecimal printout for integer values.
        noname: Don't include element names in the printout.
        sexinfo: Dump Siemens EXtra INFO text (0029 1020), if present (can be\
            VERY lengthy).
        mulfram: Dump multi-frame information, if present (1 line per frame,\
            plus an XML-style header/footer). This option also implies -noname.
        v_dump: Dump n words of binary data also.
        no_length: Skip lengths and offsets (helps diffs).
        slice_times: Show slice times from Siemens mosaic images.
        slice_times_verb: Show slice times from Siemens mosaic images\
            verbosely. (multiple uses increase verbosity, can dump CSA data).
        siemens_csa_data: Same as 3 -slice_times_verb opts.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DicomHdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DICOM_HDR_METADATA)
    cargs = []
    cargs.append("dicom_hdr")
    cargs.extend([execution.input_file(f) for f in files])
    if hex_:
        cargs.append("-hex")
    if noname:
        cargs.append("-noname")
    if sexinfo:
        cargs.append("-sexinfo")
    if mulfram:
        cargs.append("-mulfram")
    if v_dump is not None:
        cargs.extend([
            "-v",
            str(v_dump)
        ])
    if no_length:
        cargs.append("-no_length")
    if slice_times:
        cargs.append("-slice_times")
    if slice_times_verb:
        cargs.append("-slice_times_verb")
    if siemens_csa_data:
        cargs.append("-siemens_csa_data")
    ret = DicomHdrOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DICOM_HDR_METADATA",
    "DicomHdrOutputs",
    "dicom_hdr",
]
