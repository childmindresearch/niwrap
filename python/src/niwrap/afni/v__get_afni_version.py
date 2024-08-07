# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__GET_AFNI_VERSION_METADATA = Metadata(
    id="d6294f0f263143ec10e4fd4fc8a6df1d4bb64bf6",
    name="@get.afni.version",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VGetAfniVersionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_version(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    src_dir: OutputPathType
    """Directory containing the downloaded AFNI source code for the specified version."""


def v__get_afni_version(
    version: str,
    runner: Runner | None = None,
) -> VGetAfniVersionOutputs:
    """
    @get.afni.version by AFNI Team.
    
    Downloads the source code for a specified AFNI version.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@get.afni.version.html
    
    Args:
        version: AFNI version number to get (e.g., 16.0.01).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniVersionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_VERSION_METADATA)
    cargs = []
    cargs.append("@get.afni.version")
    cargs.append(version)
    ret = VGetAfniVersionOutputs(
        root=execution.output_file("."),
        src_dir=execution.output_file(f"AFNI_{version}/AFNI/src", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VGetAfniVersionOutputs",
    "V__GET_AFNI_VERSION_METADATA",
    "v__get_afni_version",
]
