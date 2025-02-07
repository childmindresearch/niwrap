# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_NOTES_METADATA = Metadata(
    id="940bc1c01a30bd95a8de66900c6eff7191dde7e1.boutiques",
    name="3dNotes",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dNotesParameters = typing.TypedDict('V3dNotesParameters', {
    "__STYX_TYPE__": typing.Literal["3dNotes"],
    "add_note": typing.NotRequired[str | None],
    "append_history": typing.NotRequired[str | None],
    "replace_history": typing.NotRequired[str | None],
    "delete_note": typing.NotRequired[float | None],
    "print_notes": bool,
    "help": bool,
    "dataset": InputPathType,
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
        "3dNotes": v_3d_notes_cargs,
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
        "3dNotes": v_3d_notes_outputs,
    }.get(t)


class V3dNotesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_notes(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_notes_params(
    dataset: InputPathType,
    add_note: str | None = None,
    append_history: str | None = None,
    replace_history: str | None = None,
    delete_note: float | None = None,
    print_notes: bool = False,
    help_: bool = False,
) -> V3dNotesParameters:
    """
    Build parameters.
    
    Args:
        dataset: AFNI compatible dataset [required].
        add_note: Add the string 'str' to the list of notes.
        append_history: Append the string 'str' to the dataset's history. This\
            can only appear once on the command line.
        replace_history: Replace any existing history note with 'str'. This\
            option cannot be used with '-h'.
        delete_note: Deletes note number num.
        print_notes: Print to stdout the expanded notes.
        help_: Displays this help screen.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dNotes",
        "print_notes": print_notes,
        "help": help_,
        "dataset": dataset,
    }
    if add_note is not None:
        params["add_note"] = add_note
    if append_history is not None:
        params["append_history"] = append_history
    if replace_history is not None:
        params["replace_history"] = replace_history
    if delete_note is not None:
        params["delete_note"] = delete_note
    return params


def v_3d_notes_cargs(
    params: V3dNotesParameters,
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
    cargs.append("3dNotes")
    if params.get("add_note") is not None:
        cargs.extend([
            "-a",
            params.get("add_note")
        ])
    if params.get("append_history") is not None:
        cargs.extend([
            "-h",
            params.get("append_history")
        ])
    if params.get("replace_history") is not None:
        cargs.extend([
            "-HH",
            params.get("replace_history")
        ])
    if params.get("delete_note") is not None:
        cargs.extend([
            "-d",
            str(params.get("delete_note"))
        ])
    if params.get("print_notes"):
        cargs.append("-ses")
    if params.get("help"):
        cargs.append("-help")
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3d_notes_outputs(
    params: V3dNotesParameters,
    execution: Execution,
) -> V3dNotesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dNotesOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_notes_execute(
    params: V3dNotesParameters,
    execution: Execution,
) -> V3dNotesOutputs:
    """
    A program to add, delete and show notes for AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dNotesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_notes_cargs(params, execution)
    ret = v_3d_notes_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_notes(
    dataset: InputPathType,
    add_note: str | None = None,
    append_history: str | None = None,
    replace_history: str | None = None,
    delete_note: float | None = None,
    print_notes: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> V3dNotesOutputs:
    """
    A program to add, delete and show notes for AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: AFNI compatible dataset [required].
        add_note: Add the string 'str' to the list of notes.
        append_history: Append the string 'str' to the dataset's history. This\
            can only appear once on the command line.
        replace_history: Replace any existing history note with 'str'. This\
            option cannot be used with '-h'.
        delete_note: Deletes note number num.
        print_notes: Print to stdout the expanded notes.
        help_: Displays this help screen.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNotesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NOTES_METADATA)
    params = v_3d_notes_params(add_note=add_note, append_history=append_history, replace_history=replace_history, delete_note=delete_note, print_notes=print_notes, help_=help_, dataset=dataset)
    return v_3d_notes_execute(params, execution)


__all__ = [
    "V3dNotesOutputs",
    "V3dNotesParameters",
    "V_3D_NOTES_METADATA",
    "v_3d_notes",
    "v_3d_notes_params",
]
