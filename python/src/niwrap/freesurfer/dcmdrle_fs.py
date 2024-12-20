# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCMDRLE_FS_METADATA = Metadata(
    id="1c6fdec3b4ee16a344e1e0d5d4e1bcbc79b17f47.boutiques",
    name="dcmdrle.fs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DcmdrleFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmdrle_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output DICOM file."""


def dcmdrle_fs(
    input_file: InputPathType,
    output_file: str,
    help_: bool = False,
    version: bool = False,
    arguments: bool = False,
    quiet: bool = False,
    verbose: bool = False,
    debug: bool = False,
    log_level: str | None = None,
    log_config: InputPathType | None = None,
    read_file: bool = False,
    read_file_only: bool = False,
    read_dataset: bool = False,
    uid_default: bool = False,
    uid_always: bool = False,
    byte_order_default: bool = False,
    byte_order_reverse: bool = False,
    write_file: bool = False,
    write_dataset: bool = False,
    write_xfer_little: bool = False,
    write_xfer_big: bool = False,
    write_xfer_implicit: bool = False,
    enable_new_vr: bool = False,
    disable_new_vr: bool = False,
    group_length_recalc: bool = False,
    group_length_create: bool = False,
    group_length_remove: bool = False,
    length_explicit: bool = False,
    length_undefined: bool = False,
    padding_retain: bool = False,
    padding_off: bool = False,
    padding_create: str | None = None,
    runner: Runner | None = None,
) -> DcmdrleFsOutputs:
    """
    Decodes RLE-compressed DICOM files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: DICOM input filename to be converted.
        output_file: DICOM output filename.
        help_: Print help text and exit.
        version: Print version information and exit.
        arguments: Print expanded command line arguments.
        quiet: Quiet mode, print no warnings and errors.
        verbose: Verbose mode, print processing details.
        debug: Debug mode, print debug information.
        log_level: Set logger level.
        log_config: Use config file for the logger.
        read_file: Read file format or data set (default).
        read_file_only: Read file format only.
        read_dataset: Read data set without file meta information.
        uid_default: Keep same SOP Instance UID (default).
        uid_always: Always assign new UID.
        byte_order_default: Most significant byte first (default).
        byte_order_reverse: Least significant byte first.
        write_file: Write file format (default).
        write_dataset: Write data set without file meta information.
        write_xfer_little: Write with explicit VR little endian (default).
        write_xfer_big: Write with explicit VR big endian TS.
        write_xfer_implicit: Write with implicit VR little endian TS.
        enable_new_vr: Enable support for new VRs (UN/UT) (default).
        disable_new_vr: Disable support for new VRs, convert to OB.
        group_length_recalc: Recalculate group lengths if present (default).
        group_length_create: Always write with group length elements.
        group_length_remove: Always write without group length elements.
        length_explicit: Write with explicit lengths (default).
        length_undefined: Write with undefined lengths.
        padding_retain: Do not change padding.
        padding_off: No padding (implicit if --write-dataset).
        padding_create: Align file on multiple of file-pad bytes and items on\
            multiple of item-pad bytes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmdrleFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMDRLE_FS_METADATA)
    cargs = []
    cargs.append("dcmdrle")
    cargs.append(execution.input_file(input_file))
    cargs.append(output_file)
    if help_:
        cargs.append("-h")
    if version:
        cargs.append("--version")
    if arguments:
        cargs.append("--arguments")
    if quiet:
        cargs.append("-q")
    if verbose:
        cargs.append("-v")
    if debug:
        cargs.append("-d")
    if log_level is not None:
        cargs.extend([
            "-ll",
            log_level
        ])
    if log_config is not None:
        cargs.extend([
            "-lc",
            execution.input_file(log_config)
        ])
    if read_file:
        cargs.append("+f")
    if read_file_only:
        cargs.append("+fo")
    if read_dataset:
        cargs.append("-f")
    if uid_default:
        cargs.append("+ud")
    if uid_always:
        cargs.append("+ua")
    if byte_order_default:
        cargs.append("+bd")
    if byte_order_reverse:
        cargs.append("+br")
    if write_file:
        cargs.append("+F")
    if write_dataset:
        cargs.append("-F")
    if write_xfer_little:
        cargs.append("+te")
    if write_xfer_big:
        cargs.append("+tb")
    if write_xfer_implicit:
        cargs.append("+ti")
    if enable_new_vr:
        cargs.append("+u")
    if disable_new_vr:
        cargs.append("-u")
    if group_length_recalc:
        cargs.append("+g=")
    if group_length_create:
        cargs.append("+g")
    if group_length_remove:
        cargs.append("-g")
    if length_explicit:
        cargs.append("+e")
    if length_undefined:
        cargs.append("-e")
    if padding_retain:
        cargs.append("-p=")
    if padding_off:
        cargs.append("-p")
    if padding_create is not None:
        cargs.extend([
            "+p",
            padding_create
        ])
    ret = DcmdrleFsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DCMDRLE_FS_METADATA",
    "DcmdrleFsOutputs",
    "dcmdrle_fs",
]
