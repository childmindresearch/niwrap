# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DTIGEN_METADATA = Metadata(
    id="5ce6d772bcc00a637795fc2c6e97a565d0c46086.boutiques",
    name="dtigen",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class DtigenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dtigen(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_diffusion_data: OutputPathType
    """Output diffusion data"""
    output_kurtosis_map: OutputPathType | None
    """Mean kurtosis map"""


def dtigen(
    tensor: InputPathType,
    s0: InputPathType,
    output_data: str,
    bvecs: InputPathType,
    bvals: InputPathType,
    brainmask: InputPathType,
    kurtosis: InputPathType | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> DtigenOutputs:
    """
    Generate diffusion data using tensor model.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        tensor: Input tensor file.
        s0: Input S0 file.
        output_data: Output data file.
        bvecs: bvecs ASCII text file.
        bvals: bvals ASCII text file.
        brainmask: Brain mask file.
        kurtosis: Mean kurtosis map.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DtigenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DTIGEN_METADATA)
    cargs = []
    cargs.append("dtigen")
    cargs.extend([
        "-t",
        execution.input_file(tensor)
    ])
    cargs.extend([
        "--s0",
        execution.input_file(s0)
    ])
    cargs.extend([
        "-o",
        output_data
    ])
    cargs.extend([
        "-r",
        execution.input_file(bvecs)
    ])
    cargs.extend([
        "-b",
        execution.input_file(bvals)
    ])
    cargs.extend([
        "-m",
        execution.input_file(brainmask)
    ])
    if kurtosis is not None:
        cargs.extend([
            "--kurt",
            execution.input_file(kurtosis)
        ])
    if help_:
        cargs.append("-h")
    ret = DtigenOutputs(
        root=execution.output_file("."),
        output_diffusion_data=execution.output_file(output_data + ".nii.gz"),
        output_kurtosis_map=execution.output_file(pathlib.Path(kurtosis).name) if (kurtosis is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DTIGEN_METADATA",
    "DtigenOutputs",
    "dtigen",
]
