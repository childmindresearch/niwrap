# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCMDJPEG_FS_METADATA = Metadata(
    id="72def5b0b090531bebd9d33b2cf8001287532af2.boutiques",
    name="dcmdjpeg.fs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DcmdjpegFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmdjpeg_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """DICOM output file"""


def dcmdjpeg_fs(
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
    conv_photometric: bool = False,
    conv_lossy: bool = False,
    conv_guess: bool = False,
    conv_guess_lossy: bool = False,
    conv_always: bool = False,
    conv_never: bool = False,
    planar_auto: bool = False,
    color_by_pixel: bool = False,
    color_by_plane: bool = False,
    uid_default: bool = False,
    uid_always: bool = False,
    workaround_pred6: bool = False,
    workaround_incpl: bool = False,
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
    padding_create: list[float] | None = None,
    runner: Runner | None = None,
) -> DcmdjpegFsOutputs:
    """
    A tool to decode JPEG-compressed DICOM files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: DICOM input filename to be converted.
        output_file: DICOM output filename.
        help_: Print this help text and exit.
        version: Print version information and exit.
        arguments: Print expanded command line arguments.
        quiet: Quiet mode, print no warnings and errors.
        verbose: Verbose mode, print processing details.
        debug: Debug mode, print debug information.
        log_level: Use level l for the logger (fatal, error, warn, info, debug,\
            trace).
        log_config: Use config file f for the logger.
        read_file: Read file format or data set (default).
        read_file_only: Read file format only.
        read_dataset: Read data set without file meta information.
        conv_photometric: Convert if YCbCr photometric interpretation (default).
        conv_lossy: Convert YCbCr to RGB if lossy JPEG.
        conv_guess: Convert to RGB if YCbCr is guessed by library.
        conv_guess_lossy: Convert to RGB if lossy JPEG and YCbCr is guessed.
        conv_always: Always convert YCbCr to RGB.
        conv_never: Never convert color space.
        planar_auto: Automatically determine planar configuration from SOP\
            class and color space (default).
        color_by_pixel: Always store color-by-pixel.
        color_by_plane: Always store color-by-plane.
        uid_default: Keep same SOP Instance UID (default).
        uid_always: Always assign new UID.
        workaround_pred6: Enable workaround for JPEG lossless images with\
            overflow in predictor 6.
        workaround_incpl: Enable workaround for incomplete JPEG data.
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
        padding_retain: Do not change padding (default if not --write-dataset).
        padding_off: No padding (implicit if --write-dataset).
        padding_create: Align file on multiple of f bytes and items on multiple\
            of i bytes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmdjpegFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMDJPEG_FS_METADATA)
    cargs = []
    cargs.append("dcmdjpeg")
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
    if conv_photometric:
        cargs.append("+cp")
    if conv_lossy:
        cargs.append("+cl")
    if conv_guess:
        cargs.append("+cg")
    if conv_guess_lossy:
        cargs.append("+cgl")
    if conv_always:
        cargs.append("+ca")
    if conv_never:
        cargs.append("+cn")
    if planar_auto:
        cargs.append("+pa")
    if color_by_pixel:
        cargs.append("+px")
    if color_by_plane:
        cargs.append("+pl")
    if uid_default:
        cargs.append("+ud")
    if uid_always:
        cargs.append("+ua")
    if workaround_pred6:
        cargs.append("+w6")
    if workaround_incpl:
        cargs.append("+wi")
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
            *map(str, padding_create)
        ])
    ret = DcmdjpegFsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DCMDJPEG_FS_METADATA",
    "DcmdjpegFsOutputs",
    "dcmdjpeg_fs",
]
