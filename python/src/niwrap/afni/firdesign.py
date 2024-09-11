# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIRDESIGN_METADATA = Metadata(
    id="b59dbb417f2a88efcc58befa175dcdcc3b4527b9.boutiques",
    name="FIRdesign",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class FirdesignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `firdesign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def firdesign(
    fbot: float,
    ftop: float,
    ntap: float,
    runner: Runner | None = None,
) -> FirdesignOutputs:
    """
    Uses the Remez algorithm to calculate the FIR filter weights for a bandpass
    filter; results are written to stdout in an unadorned (no header) column of
    numbers.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/FIRdesign.html
    
    Args:
        fbot: Lowest frequency in the pass band.
        ftop: Highest frequency in the pass band, must be higher than fbot and\
            <= 0.5/TR.
        ntap: Number of filter weights (AKA 'taps') to use, must be in the\
            range 8..2000 (inclusive).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirdesignOutputs`).
    """
    if not (0 <= fbot): 
        raise ValueError(f"'fbot' must be greater than 0 <= x but was {fbot}")
    if not (0 <= ftop): 
        raise ValueError(f"'ftop' must be greater than 0 <= x but was {ftop}")
    if not (8 <= ntap <= 2000): 
        raise ValueError(f"'ntap' must be between 8 <= x <= 2000 but was {ntap}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRDESIGN_METADATA)
    cargs = []
    cargs.append("FIRdesign")
    cargs.append("[OPTIONS]")
    cargs.append(str(fbot))
    cargs.append(str(ftop))
    cargs.append(str(ntap))
    ret = FirdesignOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIRDESIGN_METADATA",
    "FirdesignOutputs",
    "firdesign",
]
