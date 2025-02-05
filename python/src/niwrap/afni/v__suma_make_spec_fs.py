# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SUMA_MAKE_SPEC_FS_METADATA = Metadata(
    id="35abec1cbcc0a7c9a8b395b5a4855788850c3f95.boutiques",
    name="@SUMA_Make_Spec_FS",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VSumaMakeSpecFsParameters = typing.TypedDict('VSumaMakeSpecFsParameters', {
    "__STYX_TYPE__": typing.Literal["@SUMA_Make_Spec_FS"],
    "subject_id": str,
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
        "@SUMA_Make_Spec_FS": v__suma_make_spec_fs_cargs,
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
        "@SUMA_Make_Spec_FS": v__suma_make_spec_fs_outputs,
    }
    return vt.get(t)


class VSumaMakeSpecFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_make_spec_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    suma_output: OutputPathType
    """All created files are stored in a new SUMA directory"""


def v__suma_make_spec_fs_params(
    subject_id: str,
) -> VSumaMakeSpecFsParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Required subject ID for file naming.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@SUMA_Make_Spec_FS",
        "subject_id": subject_id,
    }
    return params


def v__suma_make_spec_fs_cargs(
    params: VSumaMakeSpecFsParameters,
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
    cargs.append("@SUMA_Make_Spec_FS")
    cargs.append("[OPTIONS]")
    cargs.extend([
        "-sid",
        params.get("subject_id")
    ])
    return cargs


def v__suma_make_spec_fs_outputs(
    params: VSumaMakeSpecFsParameters,
    execution: Execution,
) -> VSumaMakeSpecFsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSumaMakeSpecFsOutputs(
        root=execution.output_file("."),
        suma_output=execution.output_file("SUMA/*"),
    )
    return ret


def v__suma_make_spec_fs_execute(
    params: VSumaMakeSpecFsParameters,
    execution: Execution,
) -> VSumaMakeSpecFsOutputs:
    """
    Prepare for surface viewing in SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSumaMakeSpecFsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__suma_make_spec_fs_cargs(params, execution)
    ret = v__suma_make_spec_fs_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__suma_make_spec_fs(
    subject_id: str,
    runner: Runner | None = None,
) -> VSumaMakeSpecFsOutputs:
    """
    Prepare for surface viewing in SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        subject_id: Required subject ID for file naming.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaMakeSpecFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_MAKE_SPEC_FS_METADATA)
    params = v__suma_make_spec_fs_params(subject_id=subject_id)
    return v__suma_make_spec_fs_execute(params, execution)


__all__ = [
    "VSumaMakeSpecFsOutputs",
    "VSumaMakeSpecFsParameters",
    "V__SUMA_MAKE_SPEC_FS_METADATA",
    "v__suma_make_spec_fs",
    "v__suma_make_spec_fs_params",
]
