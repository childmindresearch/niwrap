# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SPEC_FILE_RELOCATE_METADATA = Metadata(
    id="2d2973acdec95aaa23b607a3339fa38ce965c8dd.boutiques",
    name="spec-file-relocate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SpecFileRelocateParameters = typing.TypedDict('SpecFileRelocateParameters', {
    "__STYX_TYPE__": typing.Literal["spec-file-relocate"],
    "input_spec": str,
    "output_spec": str,
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
        "spec-file-relocate": spec_file_relocate_cargs,
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
    }.get(t)


class SpecFileRelocateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spec_file_relocate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def spec_file_relocate_params(
    input_spec: str,
    output_spec: str,
) -> SpecFileRelocateParameters:
    """
    Build parameters.
    
    Args:
        input_spec: the spec file to use.
        output_spec: output - the new spec file to create.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "spec-file-relocate",
        "input_spec": input_spec,
        "output_spec": output_spec,
    }
    return params


def spec_file_relocate_cargs(
    params: SpecFileRelocateParameters,
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
    cargs.append("wb_command")
    cargs.append("-spec-file-relocate")
    cargs.append(params.get("input_spec"))
    cargs.append(params.get("output_spec"))
    return cargs


def spec_file_relocate_outputs(
    params: SpecFileRelocateParameters,
    execution: Execution,
) -> SpecFileRelocateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SpecFileRelocateOutputs(
        root=execution.output_file("."),
    )
    return ret


def spec_file_relocate_execute(
    params: SpecFileRelocateParameters,
    execution: Execution,
) -> SpecFileRelocateOutputs:
    """
    Recreate spec file in new location.
    
    Spec files contain internal relative paths, such that moving or copying a
    spec file will cause it to lose track of the files it refers to. This
    command makes a modified copy of the spec file, changing the relative paths
    to refer to the new relative locations of the files.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SpecFileRelocateOutputs`).
    """
    cargs = spec_file_relocate_cargs(params, execution)
    ret = spec_file_relocate_outputs(params, execution)
    execution.run(cargs)
    return ret


def spec_file_relocate(
    input_spec: str,
    output_spec: str,
    runner: Runner | None = None,
) -> SpecFileRelocateOutputs:
    """
    Recreate spec file in new location.
    
    Spec files contain internal relative paths, such that moving or copying a
    spec file will cause it to lose track of the files it refers to. This
    command makes a modified copy of the spec file, changing the relative paths
    to refer to the new relative locations of the files.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_spec: the spec file to use.
        output_spec: output - the new spec file to create.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SpecFileRelocateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPEC_FILE_RELOCATE_METADATA)
    params = spec_file_relocate_params(input_spec=input_spec, output_spec=output_spec)
    return spec_file_relocate_execute(params, execution)


__all__ = [
    "SPEC_FILE_RELOCATE_METADATA",
    "SpecFileRelocateOutputs",
    "SpecFileRelocateParameters",
    "spec_file_relocate",
    "spec_file_relocate_params",
]
