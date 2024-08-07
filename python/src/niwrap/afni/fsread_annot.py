# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSREAD_ANNOT_METADATA = Metadata(
    id="dc3bb10415597395151891557a14b7903da0da01",
    name="FSread_annot",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FsreadAnnotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsread_annot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_col_1d: OutputPathType
    """Output 4-column 1D color file."""
    out_roi_1d: OutputPathType
    """Output 5-column 1D ROI file."""
    out_niml_dset: OutputPathType
    """Output niml formatted label dataset."""
    out_cmap_1d: OutputPathType
    """Output 4-column 1D color map file."""


def fsread_annot(
    infile: InputPathType,
    hemi: str | None = None,
    fscmap: InputPathType | None = None,
    fscmap_range: list[float | int] | None = None,
    fsversion: str | None = None,
    col_1d: str | None = None,
    roi_1d: str | None = None,
    dset: str | None = None,
    cmap_1d: str | None = None,
    show_fscmap: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> FsreadAnnotOutputs:
    """
    FSread_annot by AFNI Team.
    
    Reads a FreeSurfer annotation file and outputs an equivalent ROI file and/or
    a colormap file for use with SUMA.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/FSread_annot.html
    
    Args:
        infile: Binary formatted FreeSurfer annotation file.
        hemi: Specify hemisphere. HEMI is one of lh or rh. Program guesses by\
            default.
        fscmap: Get the colormap from the Freesurfer colormap file CMAPFILE.\
            Colormaps inside the ANNOTFILE would be ignored.
        fscmap_range: CMAPFILE contains multiple types of labels. The\
            annotation values in ANNOTFILE can map to multiple labels if you do not\
            restrict the range with iMin and iMax.
        fsversion: VER is the annotation file vintage. Choose from 2009 or\
            2005.
        col_1d: Write a 4-column 1D color file.
        roi_1d: Write a 5-column 1D roi file.
        dset: Write the annotation and colormap as a niml formatted Label Dset.
        cmap_1d: Write a 4-column 1D color map file.
        show_fscmap: Show the info of the colormap in the ANNOT file.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsreadAnnotOutputs`).
    """
    runner = runner or get_global_runner()
    if fscmap_range is not None and (len(fscmap_range) != 2): 
        raise ValueError(f"Length of 'fscmap_range' must be 2 but was {len(fscmap_range)}")
    execution = runner.start_execution(FSREAD_ANNOT_METADATA)
    cargs = []
    cargs.append("FSread_annot")
    cargs.append("--input")
    cargs.append(execution.input_file(infile))
    if hemi is not None:
        cargs.extend(["-hemi", hemi])
    if fscmap is not None:
        cargs.extend(["-FScmap", execution.input_file(fscmap)])
    if fscmap_range is not None:
        cargs.extend(["-FScmaprange", *map(str, fscmap_range)])
    if fsversion is not None:
        cargs.extend(["-FSversion", fsversion])
    if col_1d is not None:
        cargs.extend(["-col_1D", col_1d])
    if roi_1d is not None:
        cargs.extend(["-roi_1D", roi_1d])
    if cmap_1d is not None:
        cargs.extend(["-cmap_1D", cmap_1d])
    if show_fscmap:
        cargs.append("-show_FScmap")
    if dset is not None:
        cargs.extend(["-dset", dset])
    if help_:
        cargs.append("-help")
    ret = FsreadAnnotOutputs(
        root=execution.output_file("."),
        out_col_1d=execution.output_file(f"annot.1D.col", optional=True),
        out_roi_1d=execution.output_file(f"annot.1D.roi", optional=True),
        out_niml_dset=execution.output_file(f"annot.niml.dset", optional=True),
        out_cmap_1d=execution.output_file(f"annot.1D.cmap", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSREAD_ANNOT_METADATA",
    "FsreadAnnotOutputs",
    "fsread_annot",
]
