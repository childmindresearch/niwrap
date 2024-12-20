# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MP_DIFFPOW_METADATA = Metadata(
    id="5d6f81008119f2f4a31e758201b79a4cc2a55918.boutiques",
    name="mp_diffpow",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class MpDiffpowOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mp_diffpow(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """File containing squared motion parameters, temporal difference of motion
    parameters, and squared differenced values."""


def mp_diffpow(
    reg_file: InputPathType,
    diff_reg_file: str,
    runner: Runner | None = None,
) -> MpDiffpowOutputs:
    """
    Generates a file with specific motion parameter calculations useful for
    accounting for 'spin history' effects and other variations not accounted for by
    motion correction.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        reg_file: Input file containing registration parameters (e.g.,\
            regparam.dat).
        diff_reg_file: Output file with differenced registration parameters\
            (e.g., diffregparam.dat).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MpDiffpowOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MP_DIFFPOW_METADATA)
    cargs = []
    cargs.append("mp_diffpow.sh")
    cargs.append(execution.input_file(reg_file))
    cargs.append(diff_reg_file)
    ret = MpDiffpowOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(diff_reg_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MP_DIFFPOW_METADATA",
    "MpDiffpowOutputs",
    "mp_diffpow",
]
