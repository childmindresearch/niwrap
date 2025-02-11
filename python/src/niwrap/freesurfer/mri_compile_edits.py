# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COMPILE_EDITS_METADATA = Metadata(
    id="2f294d33e927de222c7f1e4b43430f1f824c2840.boutiques",
    name="mri_compile_edits",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriCompileEditsParameters = typing.TypedDict('MriCompileEditsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_compile_edits"],
    "subject_name": str,
    "output_volume": str,
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
        "mri_compile_edits": mri_compile_edits_cargs,
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
        "mri_compile_edits": mri_compile_edits_outputs,
    }.get(t)


class MriCompileEditsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compile_edits(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    compiled_edit_volume: OutputPathType
    """Compiled volume showing all the edits"""


def mri_compile_edits_params(
    subject_name: str,
    output_volume: str,
) -> MriCompileEditsParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Subject name whose edits are to be compiled into a volume.
        output_volume: Output volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_compile_edits",
        "subject_name": subject_name,
        "output_volume": output_volume,
    }
    return params


def mri_compile_edits_cargs(
    params: MriCompileEditsParameters,
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
    cargs.append("mri_compile_edits")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_compile_edits_outputs(
    params: MriCompileEditsParameters,
    execution: Execution,
) -> MriCompileEditsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCompileEditsOutputs(
        root=execution.output_file("."),
        compiled_edit_volume=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_compile_edits_execute(
    params: MriCompileEditsParameters,
    execution: Execution,
) -> MriCompileEditsOutputs:
    """
    Program to create a single volume showing all the volumetric edits made to a
    subject.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCompileEditsOutputs`).
    """
    cargs = mri_compile_edits_cargs(params, execution)
    ret = mri_compile_edits_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_compile_edits(
    subject_name: str,
    output_volume: str,
    runner: Runner | None = None,
) -> MriCompileEditsOutputs:
    """
    Program to create a single volume showing all the volumetric edits made to a
    subject.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name whose edits are to be compiled into a volume.
        output_volume: Output volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCompileEditsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPILE_EDITS_METADATA)
    params = mri_compile_edits_params(subject_name=subject_name, output_volume=output_volume)
    return mri_compile_edits_execute(params, execution)


__all__ = [
    "MRI_COMPILE_EDITS_METADATA",
    "MriCompileEditsOutputs",
    "MriCompileEditsParameters",
    "mri_compile_edits",
    "mri_compile_edits_params",
]
