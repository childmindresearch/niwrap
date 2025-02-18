# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_LABEL2ANNOT_METADATA = Metadata(
    id="67f30d66c4a858ea344c43f9704f2d647b6aa35d.boutiques",
    name="mris_label2annot",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisLabel2annotParameters = typing.TypedDict('MrisLabel2annotParameters', {
    "__STYX_TYPE__": typing.Literal["mris_label2annot"],
    "subject": str,
    "hemi": str,
    "ctabfile": InputPathType,
    "annotname": str,
    "index_offset": typing.NotRequired[float | None],
    "label_files": typing.NotRequired[list[InputPathType] | None],
    "annot_path": typing.NotRequired[str | None],
    "labeldir": typing.NotRequired[str | None],
    "ldir_default": bool,
    "no_unknown": bool,
    "thresh": typing.NotRequired[float | None],
    "maxstatwinner": bool,
    "surf": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
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
        "mris_label2annot": mris_label2annot_cargs,
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
        "mris_label2annot": mris_label2annot_outputs,
    }.get(t)


class MrisLabel2annotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label2annot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    annot_file: OutputPathType
    """Generated annotation file"""


def mris_label2annot_params(
    subject: str,
    hemi: str,
    ctabfile: InputPathType,
    annotname: str,
    index_offset: float | None = None,
    label_files: list[InputPathType] | None = None,
    annot_path: str | None = None,
    labeldir: str | None = None,
    ldir_default: bool = False,
    no_unknown: bool = False,
    thresh: float | None = None,
    maxstatwinner: bool = False,
    surf: str | None = None,
    subjects_dir: str | None = None,
) -> MrisLabel2annotParameters:
    """
    Build parameters.
    
    Args:
        subject: FreeSurfer subject.
        hemi: Hemisphere (lh or rh).
        ctabfile: Colortable file (like FreeSurferColorLUT.txt).
        annotname: Output annotation name.
        index_offset: Add to label number to get CTAB index.
        label_files: Label file(s).
        annot_path: Full name/path of annotation file.
        labeldir: Directory with label files when not using --l.
        ldir_default: Use subject/labels as label directory.
        no_unknown: Do not map unhit labels to index 0.
        thresh: Threshold label by stats field.
        maxstatwinner: Keep label with highest 'stat' value.
        surf: Surface name, default is orig.
        subjects_dir: Subjects Directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_label2annot",
        "subject": subject,
        "hemi": hemi,
        "ctabfile": ctabfile,
        "annotname": annotname,
        "ldir_default": ldir_default,
        "no_unknown": no_unknown,
        "maxstatwinner": maxstatwinner,
    }
    if index_offset is not None:
        params["index_offset"] = index_offset
    if label_files is not None:
        params["label_files"] = label_files
    if annot_path is not None:
        params["annot_path"] = annot_path
    if labeldir is not None:
        params["labeldir"] = labeldir
    if thresh is not None:
        params["thresh"] = thresh
    if surf is not None:
        params["surf"] = surf
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    return params


def mris_label2annot_cargs(
    params: MrisLabel2annotParameters,
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
    cargs.append("mris_label2annot")
    cargs.extend([
        "-s",
        params.get("subject")
    ])
    cargs.extend([
        "-h",
        params.get("hemi")
    ])
    cargs.extend([
        "-ctab",
        execution.input_file(params.get("ctabfile"))
    ])
    cargs.extend([
        "-a",
        params.get("annotname")
    ])
    if params.get("index_offset") is not None:
        cargs.extend([
            "--offset",
            str(params.get("index_offset"))
        ])
    if params.get("label_files") is not None:
        cargs.extend([
            "--l",
            *[execution.input_file(f) for f in params.get("label_files")]
        ])
    if params.get("annot_path") is not None:
        cargs.extend([
            "--annot-path",
            params.get("annot_path")
        ])
    if params.get("labeldir") is not None:
        cargs.extend([
            "--ldir",
            params.get("labeldir")
        ])
    if params.get("ldir_default"):
        cargs.append("--ldir-default")
    if params.get("no_unknown"):
        cargs.append("--no-unknown")
    if params.get("thresh") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("thresh"))
        ])
    if params.get("maxstatwinner"):
        cargs.append("--maxstatwinner")
    if params.get("surf") is not None:
        cargs.extend([
            "--surf",
            params.get("surf")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    return cargs


def mris_label2annot_outputs(
    params: MrisLabel2annotParameters,
    execution: Execution,
) -> MrisLabel2annotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisLabel2annotOutputs(
        root=execution.output_file("."),
        annot_file=execution.output_file(params.get("hemi") + "." + params.get("annotname") + ".annot"),
    )
    return ret


def mris_label2annot_execute(
    params: MrisLabel2annotParameters,
    execution: Execution,
) -> MrisLabel2annotOutputs:
    """
    Converts a set of surface labels to an annotation file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisLabel2annotOutputs`).
    """
    params = execution.params(params)
    cargs = mris_label2annot_cargs(params, execution)
    ret = mris_label2annot_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_label2annot(
    subject: str,
    hemi: str,
    ctabfile: InputPathType,
    annotname: str,
    index_offset: float | None = None,
    label_files: list[InputPathType] | None = None,
    annot_path: str | None = None,
    labeldir: str | None = None,
    ldir_default: bool = False,
    no_unknown: bool = False,
    thresh: float | None = None,
    maxstatwinner: bool = False,
    surf: str | None = None,
    subjects_dir: str | None = None,
    runner: Runner | None = None,
) -> MrisLabel2annotOutputs:
    """
    Converts a set of surface labels to an annotation file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject.
        hemi: Hemisphere (lh or rh).
        ctabfile: Colortable file (like FreeSurferColorLUT.txt).
        annotname: Output annotation name.
        index_offset: Add to label number to get CTAB index.
        label_files: Label file(s).
        annot_path: Full name/path of annotation file.
        labeldir: Directory with label files when not using --l.
        ldir_default: Use subject/labels as label directory.
        no_unknown: Do not map unhit labels to index 0.
        thresh: Threshold label by stats field.
        maxstatwinner: Keep label with highest 'stat' value.
        surf: Surface name, default is orig.
        subjects_dir: Subjects Directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabel2annotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL2ANNOT_METADATA)
    params = mris_label2annot_params(subject=subject, hemi=hemi, ctabfile=ctabfile, annotname=annotname, index_offset=index_offset, label_files=label_files, annot_path=annot_path, labeldir=labeldir, ldir_default=ldir_default, no_unknown=no_unknown, thresh=thresh, maxstatwinner=maxstatwinner, surf=surf, subjects_dir=subjects_dir)
    return mris_label2annot_execute(params, execution)


__all__ = [
    "MRIS_LABEL2ANNOT_METADATA",
    "MrisLabel2annotOutputs",
    "MrisLabel2annotParameters",
    "mris_label2annot",
    "mris_label2annot_params",
]
