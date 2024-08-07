# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BEDPOSTX_DATACHECK_METADATA = Metadata(
    id="12cf9cce8320ad501c84f283f2b2225a181160e9",
    name="bedpostx_datacheck",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class BedpostxDatacheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bedpostx_datacheck(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bedpostx_datacheck(
    data_dir: str,
    runner: Runner | None = None,
) -> BedpostxDatacheckOutputs:
    """
    bedpostx_datacheck by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Check the data directory for BEDPOSTX compatibility.
    
    Args:
        data_dir: Data directory to check for BEDPOSTX compatibility.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BedpostxDatacheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BEDPOSTX_DATACHECK_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/bedpostx_datacheck")
    cargs.append(data_dir)
    ret = BedpostxDatacheckOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BEDPOSTX_DATACHECK_METADATA",
    "BedpostxDatacheckOutputs",
    "bedpostx_datacheck",
]
