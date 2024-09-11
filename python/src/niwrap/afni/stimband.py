# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STIMBAND_METADATA = Metadata(
    id="315c2371380e4c86483c19d5c3e7490c0171d51b.boutiques",
    name="stimband",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class StimbandOutputs(typing.NamedTuple):
    """
    Output object returned when calling `stimband(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_band: OutputPathType
    """The frequency band covering at least 90% of the power of the stimulus
    columns."""


def stimband(
    verbose_flag: bool = False,
    min_freq: float | None = None,
    min_bwidth: float | None = None,
    min_pow: float | None = None,
    runner: Runner | None = None,
) -> StimbandOutputs:
    """
    Determines frequency band covering at least 90% of the 'power' (|FFT|^2) of
    stimulus columns from X.nocensor.xmat.1D files.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/stimband.html
    
    Args:
        verbose_flag: Print the power band for each individual stimulus column\
            from each matrix.
        min_freq: Set the minimum frequency output for the band. Default value\
            is 0.01.
        min_bwidth: Set the minimum bandwidth output (top frequency minus\
            bottom frequency). Default is 0.03.
        min_pow: Set the minimum power fraction (percentage) to 'ff' instead of\
            the default 90%. Value must be in the range 50..99.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StimbandOutputs`).
    """
    if min_pow is not None and not (50 <= min_pow <= 99): 
        raise ValueError(f"'min_pow' must be between 50 <= x <= 99 but was {min_pow}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(STIMBAND_METADATA)
    cargs = []
    cargs.append("stimband")
    if verbose_flag:
        cargs.append("-verb")
    cargs.append("[MATRIXFILES...]")
    cargs.append("[ADDITIONAL_MATRIXFILES...]")
    if min_freq is not None:
        cargs.extend([
            "-min_freq",
            str(min_freq)
        ])
    if min_bwidth is not None:
        cargs.extend([
            "-min_bwidth",
            str(min_bwidth)
        ])
    if min_pow is not None:
        cargs.extend([
            "-min_pow",
            str(min_pow)
        ])
    ret = StimbandOutputs(
        root=execution.output_file("."),
        output_band=execution.output_file("stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "STIMBAND_METADATA",
    "StimbandOutputs",
    "stimband",
]
