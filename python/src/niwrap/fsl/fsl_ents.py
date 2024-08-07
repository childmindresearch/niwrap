# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_ENTS_METADATA = Metadata(
    id="3261c38b1e1185ee13ce58e276e2f92600ff9fd6",
    name="fsl_ents",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslEntsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_ents(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_time_series: OutputPathType | None
    """File to save time series to"""


def fsl_ents(
    icadir: str,
    components: list[str],
    outfile: InputPathType | None = None,
    overwrite: bool = False,
    conffile: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> FslEntsOutputs:
    """
    fsl_ents.
    
    Extract component time series from a MELODIC .ica directory.
    
    Args:
        icadir: .ica directory to extract time series from.
        components: Component number or FIX/AROMA file specifying components to\
            extract.
        outfile: File to save time series to.
        overwrite: Overwrite output file if it exists.
        conffile: Extra files to append to output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslEntsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_ENTS_METADATA)
    cargs = []
    cargs.append("fsl_ents")
    cargs.append(icadir)
    cargs.extend(components)
    if outfile is not None:
        cargs.extend(["-o", execution.input_file(outfile)])
    if overwrite:
        cargs.append("-ow")
    if conffile is not None:
        cargs.extend(["-c", *[execution.input_file(f) for f in conffile]])
    cargs.append("[-h]")
    ret = FslEntsOutputs(
        root=execution.output_file("."),
        out_time_series=execution.output_file(f"{pathlib.Path(outfile).name}", optional=True) if outfile is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_ENTS_METADATA",
    "FslEntsOutputs",
    "fsl_ents",
]
