# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PREWHITEN_METADATA = Metadata(
    id="bca64e92a06eb35cfe2ed8a5e6ae21de657a53a5.boutiques",
    name="prewhiten",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class PrewhitenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `prewhiten(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """Output files generated in the specified output directory"""


def prewhiten(
    feat_directory: str,
    output_directory: str | None = None,
    runner: Runner | None = None,
) -> PrewhitenOutputs:
    """
    Prewhitening tool for FEAT directories.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        feat_directory: Input FEAT directory.
        output_directory: Change output directory from default of input FEAT\
            directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PrewhitenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PREWHITEN_METADATA)
    cargs = []
    cargs.append("prewhiten")
    cargs.append(feat_directory)
    if output_directory is not None:
        cargs.extend([
            "-o",
            output_directory
        ])
    ret = PrewhitenOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(output_directory + "/*") if (output_directory is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PREWHITEN_METADATA",
    "PrewhitenOutputs",
    "prewhiten",
]
