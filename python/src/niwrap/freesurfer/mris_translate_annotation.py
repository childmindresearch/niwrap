# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_TRANSLATE_ANNOTATION_METADATA = Metadata(
    id="d032fa992bc89b8d397cfa5c1c3735e9bf0447e6.boutiques",
    name="mris_translate_annotation",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisTranslateAnnotationParameters = typing.TypedDict('MrisTranslateAnnotationParameters', {
    "__STYX_TYPE__": typing.Literal["mris_translate_annotation"],
    "subject": str,
    "hemi": str,
    "in_annot": InputPathType,
    "translation_file": InputPathType,
    "out_annot": str,
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
        "mris_translate_annotation": mris_translate_annotation_cargs,
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
        "mris_translate_annotation": mris_translate_annotation_outputs,
    }.get(t)


class MrisTranslateAnnotationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_translate_annotation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_annotation: OutputPathType
    """The output file with the translated annotation."""


def mris_translate_annotation_params(
    subject: str,
    hemi: str,
    in_annot: InputPathType,
    translation_file: InputPathType,
    out_annot: str,
) -> MrisTranslateAnnotationParameters:
    """
    Build parameters.
    
    Args:
        subject: The subject identifier.
        hemi: Hemisphere identifier (e.g., lh or rh).
        in_annot: Input annotation file.
        translation_file: Translation table file.
        out_annot: Output annotation file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_translate_annotation",
        "subject": subject,
        "hemi": hemi,
        "in_annot": in_annot,
        "translation_file": translation_file,
        "out_annot": out_annot,
    }
    return params


def mris_translate_annotation_cargs(
    params: MrisTranslateAnnotationParameters,
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
    cargs.append("mris_translate_annotation")
    cargs.append(params.get("subject"))
    cargs.append(params.get("hemi"))
    cargs.append(execution.input_file(params.get("in_annot")))
    cargs.append(execution.input_file(params.get("translation_file")))
    cargs.append(params.get("out_annot"))
    return cargs


def mris_translate_annotation_outputs(
    params: MrisTranslateAnnotationParameters,
    execution: Execution,
) -> MrisTranslateAnnotationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisTranslateAnnotationOutputs(
        root=execution.output_file("."),
        output_annotation=execution.output_file(params.get("out_annot")),
    )
    return ret


def mris_translate_annotation_execute(
    params: MrisTranslateAnnotationParameters,
    execution: Execution,
) -> MrisTranslateAnnotationOutputs:
    """
    This program applies a translation table to an annotation file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisTranslateAnnotationOutputs`).
    """
    cargs = mris_translate_annotation_cargs(params, execution)
    ret = mris_translate_annotation_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_translate_annotation(
    subject: str,
    hemi: str,
    in_annot: InputPathType,
    translation_file: InputPathType,
    out_annot: str,
    runner: Runner | None = None,
) -> MrisTranslateAnnotationOutputs:
    """
    This program applies a translation table to an annotation file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject identifier.
        hemi: Hemisphere identifier (e.g., lh or rh).
        in_annot: Input annotation file.
        translation_file: Translation table file.
        out_annot: Output annotation file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisTranslateAnnotationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_TRANSLATE_ANNOTATION_METADATA)
    params = mris_translate_annotation_params(subject=subject, hemi=hemi, in_annot=in_annot, translation_file=translation_file, out_annot=out_annot)
    return mris_translate_annotation_execute(params, execution)


__all__ = [
    "MRIS_TRANSLATE_ANNOTATION_METADATA",
    "MrisTranslateAnnotationOutputs",
    "MrisTranslateAnnotationParameters",
    "mris_translate_annotation",
    "mris_translate_annotation_params",
]
