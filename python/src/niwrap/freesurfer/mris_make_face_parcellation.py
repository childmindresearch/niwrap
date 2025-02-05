# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_MAKE_FACE_PARCELLATION_METADATA = Metadata(
    id="47813723c3b8dcdc56ee88729e050b27cbb7ae13.boutiques",
    name="mris_make_face_parcellation",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisMakeFaceParcellationParameters = typing.TypedDict('MrisMakeFaceParcellationParameters', {
    "__STYX_TYPE__": typing.Literal["mris_make_face_parcellation"],
    "input_surface": InputPathType,
    "ico_file": InputPathType,
    "output_annot": str,
    "colortable": typing.NotRequired[InputPathType | None],
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
        "mris_make_face_parcellation": mris_make_face_parcellation_cargs,
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
    vt = {
        "mris_make_face_parcellation": mris_make_face_parcellation_outputs,
    }
    return vt.get(t)


class MrisMakeFaceParcellationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_make_face_parcellation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    annot_file: OutputPathType
    """Generated annotation file based on the icosahedral face mapping."""


def mris_make_face_parcellation_params(
    input_surface: InputPathType,
    ico_file: InputPathType,
    output_annot: str,
    colortable: InputPathType | None = None,
) -> MrisMakeFaceParcellationParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file (e.g. lh.sphere or lh.sphere.reg).
        ico_file: Icosahedron file (e.g. ic3.tri).
        output_annot: Output annotation file (e.g. lh.ic3.annot).
        colortable: Color table file (e.g. colortable.txt).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_make_face_parcellation",
        "input_surface": input_surface,
        "ico_file": ico_file,
        "output_annot": output_annot,
    }
    if colortable is not None:
        params["colortable"] = colortable
    return params


def mris_make_face_parcellation_cargs(
    params: MrisMakeFaceParcellationParameters,
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
    cargs.append("mris_make_face_parcellation")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("ico_file")))
    cargs.append(params.get("output_annot"))
    if params.get("colortable") is not None:
        cargs.extend([
            "-ctab",
            execution.input_file(params.get("colortable"))
        ])
    return cargs


def mris_make_face_parcellation_outputs(
    params: MrisMakeFaceParcellationParameters,
    execution: Execution,
) -> MrisMakeFaceParcellationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMakeFaceParcellationOutputs(
        root=execution.output_file("."),
        annot_file=execution.output_file(params.get("output_annot")),
    )
    return ret


def mris_make_face_parcellation_execute(
    params: MrisMakeFaceParcellationParameters,
    execution: Execution,
) -> MrisMakeFaceParcellationOutputs:
    """
    Generates a parcellation based on which icosahedral face each vertex maps to.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMakeFaceParcellationOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_make_face_parcellation_cargs(params, execution)
    ret = mris_make_face_parcellation_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_make_face_parcellation(
    input_surface: InputPathType,
    ico_file: InputPathType,
    output_annot: str,
    colortable: InputPathType | None = None,
    runner: Runner | None = None,
) -> MrisMakeFaceParcellationOutputs:
    """
    Generates a parcellation based on which icosahedral face each vertex maps to.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file (e.g. lh.sphere or lh.sphere.reg).
        ico_file: Icosahedron file (e.g. ic3.tri).
        output_annot: Output annotation file (e.g. lh.ic3.annot).
        colortable: Color table file (e.g. colortable.txt).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMakeFaceParcellationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MAKE_FACE_PARCELLATION_METADATA)
    params = mris_make_face_parcellation_params(input_surface=input_surface, ico_file=ico_file, output_annot=output_annot, colortable=colortable)
    return mris_make_face_parcellation_execute(params, execution)


__all__ = [
    "MRIS_MAKE_FACE_PARCELLATION_METADATA",
    "MrisMakeFaceParcellationOutputs",
    "MrisMakeFaceParcellationParameters",
    "mris_make_face_parcellation",
    "mris_make_face_parcellation_params",
]
