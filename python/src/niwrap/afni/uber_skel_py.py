# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

UBER_SKEL_METADATA = Metadata(
    id="41786034a9fa11a1fc1239958a2c4ce04eb1e6f4",
    name="uber_skel",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class UberSkelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `uber_skel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def uber_skel(
    qt_options: str | None = None,
    no_gui_flag: bool = False,
    print_script: bool = False,
    save_script: str | None = None,
    user_var: list[str] | None = None,
    help_howto_program: bool = False,
    help_: bool = False,
    help_gui: bool = False,
    history: bool = False,
    show_valid_opts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> UberSkelOutputs:
    """
    uber_skel by AFNI Team.
    
    Sample uber processing program for initializing user and control variables,
    with options for both GUI and non-GUI modes.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/uber_skel.py.html
    
    Args:
        qt_options: Pass PyQt4 options directly to the GUI.
        no_gui_flag: Run without the GUI.
        print_script: Print the script.
        save_script: Save the script.
        user_var: Initialize user variables. Usage: -uvar <name> <value>.
        help_howto_program: Show programming comments.
        help_: Show help.
        help_gui: Show help for the GUI.
        history: Show history.
        show_valid_opts: Show valid options.
        version: Show version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UberSkelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UBER_SKEL_METADATA)
    cargs = []
    cargs.append("uber_skel.py")
    cargs.append("[OPTIONS]")
    ret = UberSkelOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UBER_SKEL_METADATA",
    "UberSkelOutputs",
    "uber_skel",
]
