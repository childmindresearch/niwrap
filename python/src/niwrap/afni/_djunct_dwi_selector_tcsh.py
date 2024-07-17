# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_DJUNCT_DWI_SELECTOR_METADATA = Metadata(
    id="6e71309d6c1fc8b0197c4b8778444d59f2a5a61c",
    name="@djunct_dwi_selector",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class DjunctDwiSelectorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_djunct_dwi_selector(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """The main output file"""


def _djunct_dwi_selector(
    dwi: InputPathType,
    png: InputPathType,
    outfile: str,
    runner: Runner | None = None,
) -> DjunctDwiSelectorOutputs:
    """
    @djunct_dwi_selector by AFNI Team.
    
    Selects DWI data and creates a representative image.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@djunct_dwi_selector.tcsh.html
    
    Args:
        dwi: Input DWI file.
        png: Output PNG image.
        outfile: Path to the output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DjunctDwiSelectorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_DJUNCT_DWI_SELECTOR_METADATA)
    cargs = []
    cargs.append("/opt/afni/src/../install/@djunct_dwi_selector.tcsh")
    cargs.append(execution.input_file(dwi))
    cargs.append(execution.input_file(png))
    cargs.append(outfile)
    ret = DjunctDwiSelectorOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{outfile}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DjunctDwiSelectorOutputs",
    "_DJUNCT_DWI_SELECTOR_METADATA",
    "_djunct_dwi_selector",
]
