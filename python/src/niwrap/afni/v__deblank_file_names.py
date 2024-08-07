# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__DEBLANK_FILE_NAMES_METADATA = Metadata(
    id="1c25b85649e46fcbee2f22c262e79ba2e1c3e105",
    name="@DeblankFileNames",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VDeblankFileNamesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__deblank_file_names(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__deblank_file_names(
    move: bool = False,
    nobrac: bool = False,
    demo_set: bool = False,
    echo: bool = False,
    help_: bool = False,
    files: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> VDeblankFileNamesOutputs:
    """
    @DeblankFileNames by AFNI Team.
    
    A script to remove blanks and other annoying characters ([], ()) from
    filenames.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@DeblankFileNames.html
    
    Args:
        move: Actually rename the files (opposite of -dry_run).
        nobrac: Do not replace () and [] in filenames, just spaces.
        demo_set: Create a toy directory with bad names for testing.
        echo: Turn on script echo.
        help_: Display help message.
        files: Specify files to fix as opposed to letting it fix all the names\
            in the current directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDeblankFileNamesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DEBLANK_FILE_NAMES_METADATA)
    cargs = []
    cargs.append("@DeblankFileNames")
    if move:
        cargs.append("-move")
    if nobrac:
        cargs.append("-nobrac")
    if demo_set:
        cargs.append("-demo_set")
    if echo:
        cargs.append("-echo")
    if help_:
        cargs.append("-help")
    cargs.append("[FILES...]")
    ret = VDeblankFileNamesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDeblankFileNamesOutputs",
    "V__DEBLANK_FILE_NAMES_METADATA",
    "v__deblank_file_names",
]
