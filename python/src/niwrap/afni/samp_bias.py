# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SAMP_BIAS_METADATA = Metadata(
    id="6e470934bf7282b84b4830d0577fb44d56bf39e3.boutiques",
    name="SampBias",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SampBiasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `samp_bias(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_1_d: OutputPathType
    """Output results in .1D format"""
    out_prefix: OutputPathType | None
    """Output results in a proper surface-based dataset."""


def samp_bias(
    specfile: InputPathType,
    surfname: str,
    outfile: str,
    plimit: float | None = None,
    dlimit: float | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> SampBiasOutputs:
    """
    SampBias is a tool for sampling bias resultant segments between paired nodes on
    anatomical surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        specfile: Spec file containing input surfaces.
        surfname: Name of input surface.
        outfile: Output results in .1D format.
        plimit: Maximum length of path along surface in mm. Default is 50 mm.
        dlimit: Maximum length of euclidean distance in mm. Default is 1000 mm.
        prefix: Output results into a proper surface-based dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SampBiasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SAMP_BIAS_METADATA)
    cargs = []
    cargs.append("SampBias")
    cargs.extend([
        "-spec",
        execution.input_file(specfile)
    ])
    cargs.extend([
        "-surf",
        surfname
    ])
    if plimit is not None:
        cargs.extend([
            "-plimit",
            str(plimit)
        ])
    if dlimit is not None:
        cargs.extend([
            "-dlimit",
            str(dlimit)
        ])
    cargs.extend([
        "-out",
        outfile
    ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    ret = SampBiasOutputs(
        root=execution.output_file("."),
        out_1_d=execution.output_file(outfile + ".1D"),
        out_prefix=execution.output_file(prefix) if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SAMP_BIAS_METADATA",
    "SampBiasOutputs",
    "samp_bias",
]
