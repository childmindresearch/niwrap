# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ABIDS_TOOL_METADATA = Metadata(
    id="8f305cf62984f76712f9473b7294b450a484313b",
    name="abids_tool",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AbidsToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `abids_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def abids_tool(
    input_files: list[InputPathType],
    tr_match: bool = False,
    add_tr: bool = False,
    add_slice_times: bool = False,
    copy_prefix: list[str] | None = None,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> AbidsToolOutputs:
    """
    abids_tool by AFNI Team.
    
    A tool to work with BIDS formatted datasets created with dcm2niix_afni or
    dcm2niix, mainly to pull information from the matching JSON file and refit
    the input dataset using 3drefit.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/abids_tool.py.html
    
    Args:
        input_files: At least one 3d+time dataset in NIFTI format.
        tr_match: Check if the TR in the json file matches the TR from input\
            dataset header. (Returns 1 if match).
        add_tr: Add the TR from the BIDS json file to the input dataset using\
            3drefit.
        add_slice_times: Add the slice times from the BIDS json file to the\
            input dataset using 3drefit.
        copy_prefix: Copy both the NIFTI dataset(s) and matching .json file(s)\
            to PREFIX. Must have the same number of prefixes as datasets.
        help_flag: Show help information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AbidsToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ABIDS_TOOL_METADATA)
    cargs = []
    cargs.append("abids_tool")
    cargs.extend([execution.input_file(f) for f in input_files])
    if copy_prefix is not None:
        cargs.extend(["-copy", *copy_prefix])
    ret = AbidsToolOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ABIDS_TOOL_METADATA",
    "AbidsToolOutputs",
    "abids_tool",
]
