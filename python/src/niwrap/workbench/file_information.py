# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FILE_INFORMATION_METADATA = Metadata(
    id="4f3efe631f7525173d2f9ead98a75886c062437a.boutiques",
    name="file-information",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class FileInformationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `file_information(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def file_information(
    data_file: str,
    opt_no_map_info: bool = False,
    opt_only_step_interval: bool = False,
    opt_only_number_of_maps: bool = False,
    opt_only_map_names: bool = False,
    opt_only_metadata: bool = False,
    opt_key_key: str | None = None,
    opt_only_cifti_xml: bool = False,
    opt_czi: bool = False,
    opt_czi_all_sub_blocks: bool = False,
    opt_czi_xml: bool = False,
    runner: Runner | None = None,
) -> FileInformationOutputs:
    """
    List information about a file's content.
    
    List information about the content of a data file. Only one -only option may
    be specified. The information listed when no -only option is present is
    dependent upon the type of data file.
    
    Library paths:
    /usr/lib/x86_64-linux-gnu/qt5/plugins
    
    /mnt/c/Users/floru/Projects/cmi/nopype/extraction/workbench/source/build/CommandLine
    
    
    File and extensions for reading and writing:
    Annotation: wb_annot
    Annotation Text Substitution: wb_annsub.csv
    Border: border, wb_border
    CIFTI - Dense: dconn.nii
    CIFTI - Dense Label: dlabel.nii
    CIFTI - Dense Parcel: dpconn.nii
    CIFTI - Dense Scalar: dscalar.nii
    CIFTI - Dense Data Series: dtseries.nii
    CIFTI - Fiber Orientations TEMPORARY: fiberTEMP.nii
    CIFTI - Fiber Trajectory TEMPORARY: trajTEMP.wbsparse
    CIFTI - Parcel: pconn.nii
    CIFTI - Parcel Dense: pdconn.nii
    CIFTI - Parcel Label: plabel.nii
    CIFTI - Parcel Scalar: pscalar.nii
    CIFTI - Parcel Series: ptseries.nii
    CIFTI - Scalar Data Series: sdseries.nii
    CZI Image: czi
    Foci: foci, wb_foci
    Histology Slices: metaczi, meta-image
    Image Read: bmp, gif, jpeg, jpg, png, ppm
    Write: bmp, jpeg, jpg, png, ppm
    Label: label.gii
    Metric: func.gii, shape.gii
    Palette: palette, wb_palette
    RGBA: rgba.gii
    Samples: wb_samples
    Scene: scene, wb_scene
    Specification: spec, wb_spec
    Surface: surf.gii
    Volume: nii, nii.gz
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        data_file: data file.
        opt_no_map_info: do not show map information for files that support\
            maps.
        opt_only_step_interval: suppress normal output, print the interval\
            between maps.
        opt_only_number_of_maps: suppress normal output, print the number of\
            maps.
        opt_only_map_names: suppress normal output, print the names of all maps.
        opt_only_metadata: suppress normal output, print file metadata.
        opt_key_key: only print the metadata for one key, with no formatting:\
            the metadata key.
        opt_only_cifti_xml: suppress normal output, print the cifti xml if the\
            file type has it.
        opt_czi: For a CZI file, show information from the libCZI Info Command\
            instead of the Workbench CZI File.
        opt_czi_all_sub_blocks: show all sub-blocks in CZI file (may produce\
            long output).
        opt_czi_xml: show XML from CZI file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FileInformationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILE_INFORMATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-file-information")
    cargs.append(data_file)
    if opt_no_map_info:
        cargs.append("-no-map-info")
    if opt_only_step_interval:
        cargs.append("-only-step-interval")
    if opt_only_number_of_maps:
        cargs.append("-only-number-of-maps")
    if opt_only_map_names:
        cargs.append("-only-map-names")
    if opt_only_metadata:
        cargs.append("-only-metadata")
    if opt_key_key is not None:
        cargs.extend([
            "-key",
            opt_key_key
        ])
    if opt_only_cifti_xml:
        cargs.append("-only-cifti-xml")
    if opt_czi:
        cargs.append("-czi")
    if opt_czi_all_sub_blocks:
        cargs.append("-czi-all-sub-blocks")
    if opt_czi_xml:
        cargs.append("-czi-xml")
    ret = FileInformationOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FILE_INFORMATION_METADATA",
    "FileInformationOutputs",
    "file_information",
]
