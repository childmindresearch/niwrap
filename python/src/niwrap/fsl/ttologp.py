# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TTOLOGP_METADATA = Metadata(
    id="df6a41338c6c2e7be7a1d202eda877049516093f.boutiques",
    name="ttologp",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class TtologpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ttologp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_logpvol: OutputPathType | None
    """Output volume for logp value"""


def ttologp(
    varsfile: InputPathType,
    cbsfile: InputPathType,
    dof: str,
    outputvol: str | None = "logps",
    help_flag: bool = False,
    runner: Runner | None = None,
) -> TtologpOutputs:
    """
    Tool for computing logp.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        varsfile: Path to the vars file.
        cbsfile: Path to the cbs file.
        dof: Degree of freedom.
        outputvol: Output volume for logp value (default is logps).
        help_flag: Display help information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TtologpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TTOLOGP_METADATA)
    cargs = []
    cargs.append("ttologp")
    cargs.append(execution.input_file(varsfile))
    cargs.append(execution.input_file(cbsfile))
    cargs.append(dof)
    if outputvol is not None:
        cargs.extend([
            "-logpout",
            outputvol
        ])
    if help_flag:
        cargs.append("-help")
    ret = TtologpOutputs(
        root=execution.output_file("."),
        output_logpvol=execution.output_file(outputvol + ".nii.gz") if (outputvol is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TTOLOGP_METADATA",
    "TtologpOutputs",
    "ttologp",
]
