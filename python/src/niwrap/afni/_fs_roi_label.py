# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_FS_ROI_LABEL_METADATA = Metadata(
    id="33ed9677c3f16b954d259c156fd5c1c4bc788aa8",
    name="@FS_roi_label",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FsRoiLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_fs_roi_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _fs_roi_label(
    label_int: float | int | None = None,
    lab_flag: float | int | None = None,
    rank_int: float | int | None = None,
    rankmap_file: InputPathType | None = None,
    name: str | None = None,
    labeltable_file: InputPathType | None = None,
    surf_annot_cmap: InputPathType | None = None,
    slab_int: float | int | None = None,
    sname_name: str | None = None,
    runner: Runner | None = None,
) -> FsRoiLabelOutputs:
    """
    @FS_roi_label by AFNI Team.
    
    Tool to get labels associated with FreeSurfer's parcellation and annotation
    files.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@FS_roi_label.html
    
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
        NamedTuple of outputs (described in `FsRoiLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_FS_ROI_LABEL_METADATA)
    cargs = []
    cargs.append("@FS_roi_label")
    if label_int is not None:
        cargs.append(str(label_int))
    if lab_flag is not None:
        cargs.extend(["-lab", str(lab_flag)])
    if rank_int is not None:
        cargs.extend(["-rank", str(rank_int)])
    if rankmap_file is not None:
        cargs.extend(["-rankmap", execution.input_file(rankmap_file)])
    if name is not None:
        cargs.extend(["-name", name])
    if labeltable_file is not None:
        cargs.extend(["-labeltable", execution.input_file(labeltable_file)])
    if surf_annot_cmap is not None:
        cargs.extend(["-surf_annot_cmap", execution.input_file(surf_annot_cmap)])
    if slab_int is not None:
        cargs.extend(["-slab", str(slab_int)])
    if sname_name is not None:
        cargs.extend(["-sname", sname_name])
    ret = FsRoiLabelOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FsRoiLabelOutputs",
    "_FS_ROI_LABEL_METADATA",
    "_fs_roi_label",
]
