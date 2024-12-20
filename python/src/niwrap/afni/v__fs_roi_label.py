# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__FS_ROI_LABEL_METADATA = Metadata(
    id="1309e970f178ba30ffa735edd056d5c550b135f1.boutiques",
    name="@FS_roi_label",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VFsRoiLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fs_roi_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__fs_roi_label(
    label_int: float | None = None,
    lab_flag: float | None = None,
    rank_int: float | None = None,
    rankmap_file: InputPathType | None = None,
    name: str | None = None,
    labeltable_file: InputPathType | None = None,
    surf_annot_cmap: InputPathType | None = None,
    slab_int: float | None = None,
    sname_name: str | None = None,
    runner: Runner | None = None,
) -> VFsRoiLabelOutputs:
    """
    Tool to get labels associated with FreeSurfer's parcellation and annotation
    files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        label_int: Integer labeled area in FreeSurfer's parcellation.
        lab_flag: Return the name of an integer labeled area in FreeSurfer's\
            parcellation.
        rank_int: Return the name of ranked integer labeled area from the\
            output of 3dRank or 3dmerge -1rank.
        rankmap_file: Path to the rank map file.
        name: Return entries matching NAME (case insensitive, partial match)\
            from FreeSurfer's FreeSurferColorLUT.txt.
        labeltable_file: Path to the label table file.
        surf_annot_cmap: CMAP file output by FSread_annot's -roi_1D option.
        slab_int: Return the name of an integer labeled area in FreeSurfer's\
            surface-based annotation.
        sname_name: Return the entries matching NAME (case insensitive, partial\
            match) from the CMAP file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFsRoiLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FS_ROI_LABEL_METADATA)
    cargs = []
    cargs.append("@FS_roi_label")
    if label_int is not None:
        cargs.append(str(label_int))
    if lab_flag is not None:
        cargs.extend([
            "-lab",
            str(lab_flag)
        ])
    if rank_int is not None:
        cargs.extend([
            "-rank",
            str(rank_int)
        ])
    if rankmap_file is not None:
        cargs.extend([
            "-rankmap",
            execution.input_file(rankmap_file)
        ])
    if name is not None:
        cargs.extend([
            "-name",
            name
        ])
    if labeltable_file is not None:
        cargs.extend([
            "-labeltable",
            execution.input_file(labeltable_file)
        ])
    if surf_annot_cmap is not None:
        cargs.extend([
            "-surf_annot_cmap",
            execution.input_file(surf_annot_cmap)
        ])
    if slab_int is not None:
        cargs.extend([
            "-slab",
            str(slab_int)
        ])
    if sname_name is not None:
        cargs.extend([
            "-sname",
            sname_name
        ])
    ret = VFsRoiLabelOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VFsRoiLabelOutputs",
    "V__FS_ROI_LABEL_METADATA",
    "v__fs_roi_label",
]
