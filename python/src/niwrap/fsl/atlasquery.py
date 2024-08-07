# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ATLASQUERY_METADATA = Metadata(
    id="e39b479cf4eea1c2e6f84cc30cf81de9a4f36cdb",
    name="atlasquery",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class AtlasqueryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `atlasquery(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def atlasquery(
    dumpatlases_flag: bool = False,
    atlas: str | None = None,
    coord: str | None = None,
    mask: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> AtlasqueryOutputs:
    """
    atlasquery by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Structural lookup tool for FSL atlases.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlasquery
    
    Args:
        dumpatlases_flag: Dump a list of available atlases.
        atlas: Name of atlas to use.
        coord: Coordinate to query in the format X,Y,Z.
        mask: A mask image to use during structural lookups.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Show help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AtlasqueryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ATLASQUERY_METADATA)
    cargs = []
    cargs.append("atlasq")
    cargs.append("ohi")
    if dumpatlases_flag:
        cargs.append("--dumpatlases")
    if atlas is not None:
        cargs.extend(["-a", atlas])
    if coord is not None:
        cargs.extend(["-c", coord])
    if mask is not None:
        cargs.extend(["-m", execution.input_file(mask)])
    if verbose_flag:
        cargs.append("-V")
    if help_flag:
        cargs.append("-h")
    ret = AtlasqueryOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ATLASQUERY_METADATA",
    "AtlasqueryOutputs",
    "atlasquery",
]
