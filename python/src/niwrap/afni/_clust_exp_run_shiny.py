# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_CLUST_EXP_RUN_SHINY_METADATA = Metadata(
    id="05a3aa0a07b923ccc33d0cb46548c6a1dfe6bcb9",
    name="@ClustExp_run_shiny",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ClustExpRunShinyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_clust_exp_run_shiny(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _clust_exp_run_shiny(
    directory: str,
    help_: bool = False,
    runner: Runner | None = None,
) -> ClustExpRunShinyOutputs:
    """
    @ClustExp_run_shiny by AFNI Team.
    
    Launch a shiny app that was created by ClustExp_StatParse.py.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ClustExp_run_shiny.html
    
    Args:
        directory: Folder created by ClustExp_StatParse.py.
        help_: Show help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ClustExpRunShinyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_CLUST_EXP_RUN_SHINY_METADATA)
    cargs = []
    cargs.append("@ClustExp_run_shiny")
    cargs.append(directory)
    if help_:
        cargs.append("-help")
    ret = ClustExpRunShinyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ClustExpRunShinyOutputs",
    "_CLUST_EXP_RUN_SHINY_METADATA",
    "_clust_exp_run_shiny",
]
