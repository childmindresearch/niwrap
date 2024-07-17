# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

NIFTI_TOOL_METADATA = Metadata(
    id="f3847f858b58b107014c2a6fce26ff2c52cc827d",
    name="nifti_tool",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class NiftiToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nifti_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """The nifti file generated as output."""


def nifti_tool(
    action: str,
    input_files: list[InputPathType] | None = None,
    field: str | None = None,
    mod_field: str | None = None,
    prefix: str | None = None,
    debug: float | int | None = None,
    overwrite: bool = False,
    convert2dtype: str | None = None,
    convert_fail_choice: str | None = None,
    convert_verify: bool = False,
    add_comment_ext: str | None = None,
    rm_ext: str | None = None,
    runner: Runner | None = None,
) -> NiftiToolOutputs:
    """
    nifti_tool by AFNI Team.
    
    Display, modify, or compare nifti headers.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/nifti_tool.html
    
    Args:
        action: Action type that defines what nifti_tool will do.
        input_files: One or more input nifti files.
        field: Field name to display, modify, or compare.
        mod_field: Field name and new value to modify.
        prefix: Prefix for the output file.
        debug: Debugging level (0-3).
        overwrite: Overwrite input files with modifications.
        convert2dtype: Convert data to a new datatype.
        convert_fail_choice: Action on conversion failure (ignore, warn, fail).
        convert_verify: Verify datatype conversion exactness.
        add_comment_ext: Add COMMENT-type extension to dataset.
        rm_ext: Remove extension by index or ALL.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NiftiToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NIFTI_TOOL_METADATA)
    cargs = []
    cargs.append("nifti_tool")
    cargs.extend(["", action])
    if input_files is not None:
        cargs.extend(["-infiles", *[execution.input_file(f) for f in input_files]])
    cargs.append("[OPTIONS]")
    ret = NiftiToolOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{prefix}.nii", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NIFTI_TOOL_METADATA",
    "NiftiToolOutputs",
    "nifti_tool",
]
