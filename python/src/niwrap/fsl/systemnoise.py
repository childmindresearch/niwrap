# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SYSTEMNOISE_METADATA = Metadata(
    id="491f1f9d1e77fe875414f044961ce13c20599887.boutiques",
    name="systemnoise",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SystemnoiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `systemnoise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_signal_file: OutputPathType
    """Output signal with added system noise"""


def systemnoise(
    input_signal: InputPathType,
    output_signal: InputPathType,
    noise_standard_deviation: float,
    seed: float | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> SystemnoiseOutputs:
    """
    Tool for adding system noise to a given signal using FSL's utilities.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_signal: Input signal (possum output matrix).
        output_signal: Output signal (possum matrix form).
        noise_standard_deviation: Set noise standard deviation (units of\
            intensity).
        seed: Input seed value for the sequence.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SystemnoiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SYSTEMNOISE_METADATA)
    cargs = []
    cargs.append("systemnoise")
    cargs.extend([
        "--in",
        execution.input_file(input_signal)
    ])
    cargs.extend([
        "--out",
        execution.input_file(output_signal)
    ])
    cargs.extend([
        "--sigma",
        str(noise_standard_deviation)
    ])
    if seed is not None:
        cargs.extend([
            "--seed",
            str(seed)
        ])
    if verbose_flag:
        cargs.append("--verbose")
    if help_flag:
        cargs.append("--help")
    ret = SystemnoiseOutputs(
        root=execution.output_file("."),
        output_signal_file=execution.output_file(pathlib.Path(output_signal).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SYSTEMNOISE_METADATA",
    "SystemnoiseOutputs",
    "systemnoise",
]
