# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSREAD_ANNOT_METADATA = Metadata(
    id="1aee44cf7efa00cb2630f7f3d7fb84af69eadb4f.boutiques",
    name="FSread_annot",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FsreadAnnotParameters = typing.TypedDict('FsreadAnnotParameters', {
    "__STYX_TYPE__": typing.Literal["FSread_annot"],
    "infile": InputPathType,
    "hemi": typing.NotRequired[str | None],
    "fscmap": typing.NotRequired[InputPathType | None],
    "fscmap_range": typing.NotRequired[list[float] | None],
    "fsversion": typing.NotRequired[str | None],
    "col_1d": typing.NotRequired[str | None],
    "roi_1d": typing.NotRequired[str | None],
    "cmap_1d": typing.NotRequired[str | None],
    "show_fscmap": bool,
    "dset": typing.NotRequired[str | None],
    "help": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "FSread_annot": fsread_annot_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "FSread_annot": fsread_annot_outputs,
    }.get(t)


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


def fsread_annot_params(
    infile: InputPathType,
    hemi: str | None = None,
    fscmap: InputPathType | None = None,
    fscmap_range: list[float] | None = None,
    fsversion: str | None = None,
    col_1d: str | None = None,
    roi_1d: str | None = None,
    cmap_1d: str | None = None,
    show_fscmap: bool = False,
    dset: str | None = None,
    help_: bool = False,
) -> FsreadAnnotParameters:
    """
    Build parameters.
    
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
        cmap_1d: Write a 4-column 1D color map file.
        show_fscmap: Show the info of the colormap in the ANNOT file.
        dset: Write the annotation and colormap as a niml formatted Label Dset.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "FSread_annot",
        "infile": infile,
        "show_fscmap": show_fscmap,
        "help": help_,
    }
    if hemi is not None:
        params["hemi"] = hemi
    if fscmap is not None:
        params["fscmap"] = fscmap
    if fscmap_range is not None:
        params["fscmap_range"] = fscmap_range
    if fsversion is not None:
        params["fsversion"] = fsversion
    if col_1d is not None:
        params["col_1d"] = col_1d
    if roi_1d is not None:
        params["roi_1d"] = roi_1d
    if cmap_1d is not None:
        params["cmap_1d"] = cmap_1d
    if dset is not None:
        params["dset"] = dset
    return params


def fsread_annot_cargs(
    params: FsreadAnnotParameters,
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
    cargs.append("FSread_annot")
    cargs.extend([
        "-input",
        "-" + execution.input_file(params.get("infile"))
    ])
    if params.get("hemi") is not None:
        cargs.extend([
            "-hemi",
            params.get("hemi")
        ])
    if params.get("fscmap") is not None:
        cargs.extend([
            "-FScmap",
            execution.input_file(params.get("fscmap"))
        ])
    if params.get("fscmap_range") is not None:
        cargs.extend([
            "-FScmaprange",
            *map(str, params.get("fscmap_range"))
        ])
    if params.get("fsversion") is not None:
        cargs.extend([
            "-FSversion",
            params.get("fsversion")
        ])
    if params.get("col_1d") is not None:
        cargs.extend([
            "-col_1D",
            params.get("col_1d")
        ])
    if params.get("roi_1d") is not None:
        cargs.extend([
            "-roi_1D",
            params.get("roi_1d")
        ])
    if params.get("cmap_1d") is not None:
        cargs.extend([
            "-cmap_1D",
            params.get("cmap_1d")
        ])
    if params.get("show_fscmap"):
        cargs.append("-show_FScmap")
    if params.get("dset") is not None:
        cargs.extend([
            "-dset",
            params.get("dset")
        ])
    if params.get("help"):
        cargs.append("-help")
    return cargs


def fsread_annot_outputs(
    params: FsreadAnnotParameters,
    execution: Execution,
) -> FsreadAnnotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsreadAnnotOutputs(
        root=execution.output_file("."),
        out_col_1d=execution.output_file("annot.1D.col"),
        out_roi_1d=execution.output_file("annot.1D.roi"),
        out_niml_dset=execution.output_file("annot.niml.dset"),
        out_cmap_1d=execution.output_file("annot.1D.cmap"),
    )
    return ret


def fsread_annot_execute(
    params: FsreadAnnotParameters,
    execution: Execution,
) -> FsreadAnnotOutputs:
    """
    Reads a FreeSurfer annotation file and outputs an equivalent ROI file and/or a
    colormap file for use with SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsreadAnnotOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsread_annot_cargs(params, execution)
    ret = fsread_annot_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsread_annot(
    infile: InputPathType,
    hemi: str | None = None,
    fscmap: InputPathType | None = None,
    fscmap_range: list[float] | None = None,
    fsversion: str | None = None,
    col_1d: str | None = None,
    roi_1d: str | None = None,
    cmap_1d: str | None = None,
    show_fscmap: bool = False,
    dset: str | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> FsreadAnnotOutputs:
    """
    Reads a FreeSurfer annotation file and outputs an equivalent ROI file and/or a
    colormap file for use with SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
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
        cmap_1d: Write a 4-column 1D color map file.
        show_fscmap: Show the info of the colormap in the ANNOT file.
        dset: Write the annotation and colormap as a niml formatted Label Dset.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsreadAnnotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSREAD_ANNOT_METADATA)
    params = fsread_annot_params(infile=infile, hemi=hemi, fscmap=fscmap, fscmap_range=fscmap_range, fsversion=fsversion, col_1d=col_1d, roi_1d=roi_1d, cmap_1d=cmap_1d, show_fscmap=show_fscmap, dset=dset, help_=help_)
    return fsread_annot_execute(params, execution)


__all__ = [
    "FSREAD_ANNOT_METADATA",
    "FsreadAnnotOutputs",
    "FsreadAnnotParameters",
    "fsread_annot",
    "fsread_annot_params",
]
