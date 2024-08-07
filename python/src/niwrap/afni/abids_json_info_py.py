# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ABIDS_JSON_INFO_METADATA = Metadata(
    id="a32b9d2fbcb6512f832038e4d9d8bf14b8f189e2",
    name="abids_json_info",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AbidsJsonInfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `abids_json_info(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def abids_json_info(
    json_files: list[InputPathType],
    tr_flag: bool = False,
    te_flag: bool = False,
    te_sec_flag: bool = False,
    match_nii_flag: bool = False,
    field_list: list[str] | None = None,
    list_fields_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> AbidsJsonInfoOutputs:
    """
    abids_json_info by AFNI Team.
    
    A tool to extract information from BIDS formatted json files.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/abids_json_info.py.html
    
    Args:
        json_files: Specify .json file(s).
        tr_flag: Print the TR from the json file in seconds, from the\
            'RepetitionTime' field.
        te_flag: Print out the 'EchoTime' field in milliseconds (the json file\
            stores it in seconds).
        te_sec_flag: Print the 'EchoTime' field in seconds.
        match_nii_flag: Check if there is a .nii or .nii.gz file that matches\
            the .json file (1 if the dataset is loadable).
        field_list: Print any field or list of fields from the json file.
        list_fields_flag: Print a list of the available fields from the .json\
            file. This must be the only argument specified.
        help_flag: Show this help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AbidsJsonInfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ABIDS_JSON_INFO_METADATA)
    cargs = []
    cargs.append("/opt/afni/src/../install/abids_json_info.py")
    cargs.extend([execution.input_file(f) for f in json_files])
    if tr_flag:
        cargs.append("-TR")
    if te_flag:
        cargs.append("-TE")
    if te_sec_flag:
        cargs.append("-TE_sec")
    if match_nii_flag:
        cargs.append("-match_nii")
    if field_list is not None:
        cargs.extend(["-field", *field_list])
    if list_fields_flag:
        cargs.append("-list_fields")
    if help_flag:
        cargs.append("-help")
    ret = AbidsJsonInfoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ABIDS_JSON_INFO_METADATA",
    "AbidsJsonInfoOutputs",
    "abids_json_info",
]
