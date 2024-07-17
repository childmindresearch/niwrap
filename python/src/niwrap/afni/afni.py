# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

AFNI_METADATA = Metadata(
    id="2977c6bcc62d3f1d2d34d8ff25df04ef51a921ab",
    name="afni",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    session_output: OutputPathType
    """Output file for the session data"""


def afni(
    session_directories: str | None = None,
    bysub: list[str] | None = None,
    all_dsets: bool = False,
    purge: bool = False,
    posfunc: bool = False,
    recursive: bool = False,
    no1_d: bool = False,
    nocsv: bool = False,
    notsv: bool = False,
    unique: bool = False,
    orient: str | None = None,
    noplugins: bool = False,
    seehidden: bool = False,
    allow_all_plugins: bool = False,
    yesplugouts: bool = False,
    debug_plugouts: bool = False,
    noplugouts: bool = False,
    skip_afnirc: bool = False,
    layout: InputPathType | None = None,
    niml: bool = False,
    np: int | None = None,
    npq: int | None = None,
    npb: int | None = None,
    com: str | None = None,
    comsep: str | None = None,
    runner: Runner | None = None,
) -> AfniOutputs:
    """
    afni by AFNI Team.
    
    Tool for reading in sessions of 3D datasets and visualizing them.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni.html
    
    Args:
        session_directories: Input session directories containing the datasets.
        bysub: Gather all datasets corresponding to a single subject identifier.
        all_dsets: Read in all datasets from all listed folders together.
        purge: Conserve memory by purging unused datasets.
        posfunc: Start up the color 'pbar' to use only positive function values.
        recursive: Recursively search each session_directory for more session\
            subdirectories.
        no1_d: Tells AFNI not to read *.1D timeseries files.
        nocsv: Tells AFNI not to read *.csv files.
        notsv: Tells AFNI not to read *.tsv files.
        unique: Create a unique set of colors for each AFNI controller window.
        orient: Orientation code for displaying x-y-z coordinates.
        noplugins: Do not load plugins.
        seehidden: Show hidden plugins.
        allow_all_plugins: Do not hide plugins.
        yesplugouts: Listen for plugouts.
        debug_plugouts: Plugout code prints lots of messages (for debugging).
        noplugouts: Do not listen for plugouts.
        skip_afnirc: Do not read .afnirc file.
        layout: Read initial windows layout from a file.
        niml: Turn on listening for NIML-formatted data from SUMA.
        np: Provide a port offset for multiple instances.
        npq: Like -np but quieter in case of errors.
        npb: Provide a block of port numbers.
        com: Specify command strings to drive AFNI on startup.
        comsep: Character to use as a separator for commands.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_METADATA)
    cargs = []
    cargs.append("afni")
    cargs.append("[OPTIONS]")
    if session_directories is not None:
        cargs.append(session_directories)
    ret = AfniOutputs(
        root=execution.output_file("."),
        session_output=execution.output_file(f"output_session.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_METADATA",
    "AfniOutputs",
    "afni",
]
