# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCM2NIIX_METADATA = Metadata(
    id="15ccd57203c6c358b266b58ae05fde04fa3d5414.boutiques",
    name="dcm2niix",
    package="dcm2niix",
    container_image_tag="vnmd/dcm2niix_v1.0.20240202:20241125",
)
Dcm2niixParameters = typing.TypedDict('Dcm2niixParameters', {
    "__STYX_TYPE__": typing.Literal["dcm2niix"],
    "compression_level": typing.NotRequired[float | None],
    "adjacent": typing.NotRequired[typing.Literal["y", "n"] | None],
    "bids": typing.NotRequired[typing.Literal["y", "n", "o"] | None],
    "bids_anon": typing.NotRequired[typing.Literal["y", "n"] | None],
    "comment": typing.NotRequired[str | None],
    "depth": typing.NotRequired[float | None],
    "export_format": typing.NotRequired[typing.Literal["y", "n", "o", "j", "b"] | None],
    "filename": typing.NotRequired[str | None],
    "defaults": typing.NotRequired[typing.Literal["y", "n", "o", "i"] | None],
    "ignore_derived": typing.NotRequired[typing.Literal["y", "n"] | None],
    "scaling": typing.NotRequired[typing.Literal["y", "n", "o"] | None],
    "merge_2d": typing.NotRequired[typing.Literal["n", "y", "0", "1", "2"] | None],
    "series_number": typing.NotRequired[str | None],
    "output_dir": typing.NotRequired[str | None],
    "philips_scaling": typing.NotRequired[typing.Literal["y", "n"] | None],
    "search_mode": typing.NotRequired[typing.Literal["y", "l", "n"] | None],
    "rename": typing.NotRequired[typing.Literal["y", "n"] | None],
    "single_file": typing.NotRequired[typing.Literal["y", "n"] | None],
    "update_check": bool,
    "verbose": typing.NotRequired[typing.Literal["0", "1", "2"] | None],
    "conflict_behavior": typing.NotRequired[float | None],
    "crop_3d": typing.NotRequired[typing.Literal["y", "n", "i"] | None],
    "compression": typing.NotRequired[typing.Literal["y", "o", "i", "n", "3"] | None],
    "endian": typing.NotRequired[typing.Literal["y", "n", "o"] | None],
    "progress": typing.NotRequired[typing.Literal["y", "n"] | None],
    "ignore_trigger": bool,
    "terse": bool,
    "xml": bool,
    "input_dir": InputPathType,
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
        "dcm2niix": dcm2niix_cargs,
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


class Dcm2niixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcm2niix_(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dcm2niix_params(
    input_dir: InputPathType,
    compression_level: float | None = None,
    adjacent: typing.Literal["y", "n"] | None = None,
    bids: typing.Literal["y", "n", "o"] | None = None,
    bids_anon: typing.Literal["y", "n"] | None = None,
    comment: str | None = None,
    depth: float | None = None,
    export_format: typing.Literal["y", "n", "o", "j", "b"] | None = None,
    filename: str | None = None,
    defaults: typing.Literal["y", "n", "o", "i"] | None = None,
    ignore_derived: typing.Literal["y", "n"] | None = None,
    scaling: typing.Literal["y", "n", "o"] | None = None,
    merge_2d: typing.Literal["n", "y", "0", "1", "2"] | None = None,
    series_number: str | None = None,
    output_dir: str | None = ".",
    philips_scaling: typing.Literal["y", "n"] | None = None,
    search_mode: typing.Literal["y", "l", "n"] | None = None,
    rename: typing.Literal["y", "n"] | None = None,
    single_file: typing.Literal["y", "n"] | None = None,
    update_check: bool = False,
    verbose: typing.Literal["0", "1", "2"] | None = None,
    conflict_behavior: float | None = None,
    crop_3d: typing.Literal["y", "n", "i"] | None = None,
    compression: typing.Literal["y", "o", "i", "n", "3"] | None = None,
    endian: typing.Literal["y", "n", "o"] | None = None,
    progress: typing.Literal["y", "n"] | None = None,
    ignore_trigger: bool = False,
    terse: bool = False,
    xml_: bool = False,
) -> Dcm2niixParameters:
    """
    Build parameters.
    
    Args:
        input_dir: Input folder containing DICOM files. Will be searched\
            recursively based on depth parameter.
        compression_level: gz compression level (1=fastest..9=smallest).
        adjacent: Adjacent DICOMs (images from same series always in same\
            folder) for faster conversion.
        bids: Generate BIDS sidecar JSON files (o=only: no NIfTI).
        bids_anon: Anonymize BIDS sidecar files by removing personal\
            information.
        comment: Comment stored in NIfTI aux_file (up to 24 characters).
        depth: Directory search depth for DICOM files in sub-folders.
        export_format: Export format: NRRD (y), MGH (o), JSON/JNIfTI (j), or\
            BJNIfTI (b).
        filename: Output filename template (%a=antenna, %b=basename,\
            %c=comments, %d=description, %e=echo number, %f=folder name,\
            %g=accession number, %i=ID of patient, %j=seriesInstanceUID,\
            %k=studyInstanceUID, %m=manufacturer, %n=name of patient,\
            %o=mediaObjectInstanceUID, %p=protocol, %r=instance number, %s=series\
            number, %t=time, %u=acquisition number, %v=vendor, %x=study ID;\
            %z=sequence name).
        defaults: Generate defaults file (o=only: reset and write defaults;\
            i=ignore: reset defaults).
        ignore_derived: Ignore derived, localizer and 2D images.
        scaling: Losslessly scale 16-bit integers (y=scale, n=no but\
            uint16->int16, o=original).
        merge_2d: Merge 2D slices from same series regardless of echo,\
            exposure, etc. (0=no, 1=yes, 2=auto).
        series_number: Only convert specified series CRC number (can be used up\
            to 16 times).
        output_dir: Output directory (omit to save to input folder).
        philips_scaling: Use Philips precise float (not display) scaling.
        search_mode: Search mode (y=show number of DICOMs, l=list DICOMs, n=no).
        rename: Rename instead of convert DICOMs.
        single_file: Single file mode, do not convert other images in folder.
        update_check: Check for newer versions.
        verbose: Verbose output (0=no, 1=yes, 2=logorrheic).
        conflict_behavior: Write behavior for name conflicts (0=skip,\
            1=overwrite, 2=add suffix).
        crop_3d: Crop 3D acquisitions (i=ignore: neither crop nor rotate).
        compression: gz compress images (y=pigz, o=optimal pigz,\
            i=internal:zlib, n=no, 3=no,3D).
        endian: Byte order (y=big-end, n=little-end, o=optimal/native).
        progress: Slicer format progress information.
        ignore_trigger: Disregard values in 0018,1060 and 0020,9153.
        terse: Omit filename post-fixes (can cause overwrites).
        xml_: Output Slicer format features.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dcm2niix",
        "update_check": update_check,
        "ignore_trigger": ignore_trigger,
        "terse": terse,
        "xml": xml_,
        "input_dir": input_dir,
    }
    if compression_level is not None:
        params["compression_level"] = compression_level
    if adjacent is not None:
        params["adjacent"] = adjacent
    if bids is not None:
        params["bids"] = bids
    if bids_anon is not None:
        params["bids_anon"] = bids_anon
    if comment is not None:
        params["comment"] = comment
    if depth is not None:
        params["depth"] = depth
    if export_format is not None:
        params["export_format"] = export_format
    if filename is not None:
        params["filename"] = filename
    if defaults is not None:
        params["defaults"] = defaults
    if ignore_derived is not None:
        params["ignore_derived"] = ignore_derived
    if scaling is not None:
        params["scaling"] = scaling
    if merge_2d is not None:
        params["merge_2d"] = merge_2d
    if series_number is not None:
        params["series_number"] = series_number
    if output_dir is not None:
        params["output_dir"] = output_dir
    if philips_scaling is not None:
        params["philips_scaling"] = philips_scaling
    if search_mode is not None:
        params["search_mode"] = search_mode
    if rename is not None:
        params["rename"] = rename
    if single_file is not None:
        params["single_file"] = single_file
    if verbose is not None:
        params["verbose"] = verbose
    if conflict_behavior is not None:
        params["conflict_behavior"] = conflict_behavior
    if crop_3d is not None:
        params["crop_3d"] = crop_3d
    if compression is not None:
        params["compression"] = compression
    if endian is not None:
        params["endian"] = endian
    if progress is not None:
        params["progress"] = progress
    return params


def dcm2niix_cargs(
    params: Dcm2niixParameters,
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
    cargs.append("dcm2niix")
    if params.get("compression_level") is not None:
        cargs.append("-" + str(params.get("compression_level")))
    if params.get("adjacent") is not None:
        cargs.extend([
            "-a",
            params.get("adjacent")
        ])
    if params.get("bids") is not None:
        cargs.extend([
            "-b",
            params.get("bids")
        ])
    if params.get("bids_anon") is not None:
        cargs.extend([
            "-ba",
            params.get("bids_anon")
        ])
    if params.get("comment") is not None:
        cargs.extend([
            "-c",
            params.get("comment")
        ])
    if params.get("depth") is not None:
        cargs.extend([
            "-d",
            str(params.get("depth"))
        ])
    if params.get("export_format") is not None:
        cargs.extend([
            "-e",
            params.get("export_format")
        ])
    if params.get("filename") is not None:
        cargs.extend([
            "-f",
            params.get("filename")
        ])
    if params.get("defaults") is not None:
        cargs.extend([
            "-g",
            params.get("defaults")
        ])
    if params.get("ignore_derived") is not None:
        cargs.extend([
            "-i",
            params.get("ignore_derived")
        ])
    if params.get("scaling") is not None:
        cargs.extend([
            "-l",
            params.get("scaling")
        ])
    if params.get("merge_2d") is not None:
        cargs.extend([
            "-m",
            params.get("merge_2d")
        ])
    if params.get("series_number") is not None:
        cargs.extend([
            "-n",
            params.get("series_number")
        ])
    if params.get("output_dir") is not None:
        cargs.extend([
            "-o",
            params.get("output_dir")
        ])
    if params.get("philips_scaling") is not None:
        cargs.extend([
            "-p",
            params.get("philips_scaling")
        ])
    if params.get("search_mode") is not None:
        cargs.extend([
            "-q",
            params.get("search_mode")
        ])
    if params.get("rename") is not None:
        cargs.extend([
            "-r",
            params.get("rename")
        ])
    if params.get("single_file") is not None:
        cargs.extend([
            "-s",
            params.get("single_file")
        ])
    if params.get("update_check"):
        cargs.append("-u")
    if params.get("verbose") is not None:
        cargs.extend([
            "-v",
            params.get("verbose")
        ])
    if params.get("conflict_behavior") is not None:
        cargs.extend([
            "-w",
            str(params.get("conflict_behavior"))
        ])
    if params.get("crop_3d") is not None:
        cargs.extend([
            "-x",
            params.get("crop_3d")
        ])
    if params.get("compression") is not None:
        cargs.extend([
            "-z",
            params.get("compression")
        ])
    if params.get("endian") is not None:
        cargs.extend([
            "--big-endian",
            params.get("endian")
        ])
    if params.get("progress") is not None:
        cargs.extend([
            "--progress",
            params.get("progress")
        ])
    if params.get("ignore_trigger"):
        cargs.append("--ignore_trigger_times")
    if params.get("terse"):
        cargs.append("--terse")
    if params.get("xml"):
        cargs.append("--xml")
    cargs.append(execution.input_file(params.get("input_dir")))
    return cargs


def dcm2niix_outputs(
    params: Dcm2niixParameters,
    execution: Execution,
) -> Dcm2niixOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Dcm2niixOutputs(
        root=execution.output_file("."),
    )
    return ret


def dcm2niix_execute(
    params: Dcm2niixParameters,
    execution: Execution,
) -> Dcm2niixOutputs:
    """
    Chris Rorden's dcm2niiX - DICOM to NIfTI converter. Converts DICOM files to
    NIfTI format with optional BIDS sidecar generation.
    
    Author: Chris Rorden
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Dcm2niixOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dcm2niix_cargs(params, execution)
    ret = dcm2niix_outputs(params, execution)
    execution.run(cargs)
    return ret


def dcm2niix_(
    input_dir: InputPathType,
    compression_level: float | None = None,
    adjacent: typing.Literal["y", "n"] | None = None,
    bids: typing.Literal["y", "n", "o"] | None = None,
    bids_anon: typing.Literal["y", "n"] | None = None,
    comment: str | None = None,
    depth: float | None = None,
    export_format: typing.Literal["y", "n", "o", "j", "b"] | None = None,
    filename: str | None = None,
    defaults: typing.Literal["y", "n", "o", "i"] | None = None,
    ignore_derived: typing.Literal["y", "n"] | None = None,
    scaling: typing.Literal["y", "n", "o"] | None = None,
    merge_2d: typing.Literal["n", "y", "0", "1", "2"] | None = None,
    series_number: str | None = None,
    output_dir: str | None = ".",
    philips_scaling: typing.Literal["y", "n"] | None = None,
    search_mode: typing.Literal["y", "l", "n"] | None = None,
    rename: typing.Literal["y", "n"] | None = None,
    single_file: typing.Literal["y", "n"] | None = None,
    update_check: bool = False,
    verbose: typing.Literal["0", "1", "2"] | None = None,
    conflict_behavior: float | None = None,
    crop_3d: typing.Literal["y", "n", "i"] | None = None,
    compression: typing.Literal["y", "o", "i", "n", "3"] | None = None,
    endian: typing.Literal["y", "n", "o"] | None = None,
    progress: typing.Literal["y", "n"] | None = None,
    ignore_trigger: bool = False,
    terse: bool = False,
    xml_: bool = False,
    runner: Runner | None = None,
) -> Dcm2niixOutputs:
    """
    Chris Rorden's dcm2niiX - DICOM to NIfTI converter. Converts DICOM files to
    NIfTI format with optional BIDS sidecar generation.
    
    Author: Chris Rorden
    
    Args:
        input_dir: Input folder containing DICOM files. Will be searched\
            recursively based on depth parameter.
        compression_level: gz compression level (1=fastest..9=smallest).
        adjacent: Adjacent DICOMs (images from same series always in same\
            folder) for faster conversion.
        bids: Generate BIDS sidecar JSON files (o=only: no NIfTI).
        bids_anon: Anonymize BIDS sidecar files by removing personal\
            information.
        comment: Comment stored in NIfTI aux_file (up to 24 characters).
        depth: Directory search depth for DICOM files in sub-folders.
        export_format: Export format: NRRD (y), MGH (o), JSON/JNIfTI (j), or\
            BJNIfTI (b).
        filename: Output filename template (%a=antenna, %b=basename,\
            %c=comments, %d=description, %e=echo number, %f=folder name,\
            %g=accession number, %i=ID of patient, %j=seriesInstanceUID,\
            %k=studyInstanceUID, %m=manufacturer, %n=name of patient,\
            %o=mediaObjectInstanceUID, %p=protocol, %r=instance number, %s=series\
            number, %t=time, %u=acquisition number, %v=vendor, %x=study ID;\
            %z=sequence name).
        defaults: Generate defaults file (o=only: reset and write defaults;\
            i=ignore: reset defaults).
        ignore_derived: Ignore derived, localizer and 2D images.
        scaling: Losslessly scale 16-bit integers (y=scale, n=no but\
            uint16->int16, o=original).
        merge_2d: Merge 2D slices from same series regardless of echo,\
            exposure, etc. (0=no, 1=yes, 2=auto).
        series_number: Only convert specified series CRC number (can be used up\
            to 16 times).
        output_dir: Output directory (omit to save to input folder).
        philips_scaling: Use Philips precise float (not display) scaling.
        search_mode: Search mode (y=show number of DICOMs, l=list DICOMs, n=no).
        rename: Rename instead of convert DICOMs.
        single_file: Single file mode, do not convert other images in folder.
        update_check: Check for newer versions.
        verbose: Verbose output (0=no, 1=yes, 2=logorrheic).
        conflict_behavior: Write behavior for name conflicts (0=skip,\
            1=overwrite, 2=add suffix).
        crop_3d: Crop 3D acquisitions (i=ignore: neither crop nor rotate).
        compression: gz compress images (y=pigz, o=optimal pigz,\
            i=internal:zlib, n=no, 3=no,3D).
        endian: Byte order (y=big-end, n=little-end, o=optimal/native).
        progress: Slicer format progress information.
        ignore_trigger: Disregard values in 0018,1060 and 0020,9153.
        terse: Omit filename post-fixes (can cause overwrites).
        xml_: Output Slicer format features.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Dcm2niixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCM2NIIX_METADATA)
    params = dcm2niix_params(compression_level=compression_level, adjacent=adjacent, bids=bids, bids_anon=bids_anon, comment=comment, depth=depth, export_format=export_format, filename=filename, defaults=defaults, ignore_derived=ignore_derived, scaling=scaling, merge_2d=merge_2d, series_number=series_number, output_dir=output_dir, philips_scaling=philips_scaling, search_mode=search_mode, rename=rename, single_file=single_file, update_check=update_check, verbose=verbose, conflict_behavior=conflict_behavior, crop_3d=crop_3d, compression=compression, endian=endian, progress=progress, ignore_trigger=ignore_trigger, terse=terse, xml_=xml_, input_dir=input_dir)
    return dcm2niix_execute(params, execution)


__all__ = [
    "DCM2NIIX_METADATA",
    "Dcm2niixOutputs",
    "Dcm2niixParameters",
    "dcm2niix_",
    "dcm2niix_params",
]
