# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_HEMI_MASK_METADATA = Metadata(
    id="55920b5b609569d7bec1e1ab50384958b7621427.boutiques",
    name="make_hemi_mask",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MakeHemiMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_hemi_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Hemisphere masked MRI volume output"""


def make_hemi_mask(
    hemi: str,
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> MakeHemiMaskOutputs:
    """
    Generates a hemisphere mask by registering input to the left/right reversed
    version using mri_robust_register, then keeps only the selected hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemi: Hemisphere to keep ('lh' for left hemisphere, 'rh' for right\
            hemisphere).
        input_file: Input MRI volume file (e.g. input.mgz).
        output_file: Output masked MRI volume file (e.g. output.mgz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeHemiMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_HEMI_MASK_METADATA)
    cargs = []
    cargs.append("make_hemi_mask")
    cargs.append(hemi)
    cargs.append(execution.input_file(input_file))
    cargs.append(output_file)
    ret = MakeHemiMaskOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_HEMI_MASK_METADATA",
    "MakeHemiMaskOutputs",
    "make_hemi_mask",
]
