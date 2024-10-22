# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_WARP_CONVERT_METADATA = Metadata(
    id="81a617f11d0feeee60da12d955fce5ebd395e531.boutiques",
    name="mri_warp_convert",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriWarpConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_warp_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outwarp: OutputPathType | None
    """Converted output warp file"""


def mri_warp_convert(
    invox: InputPathType | None = None,
    outvox: str | None = None,
    insrcgeom: InputPathType | None = None,
    downsample: bool = False,
    runner: Runner | None = None,
) -> MriWarpConvertOutputs:
    """
    This program converts non-linear deformation field warp file formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        invox: Input file with displacements in source-voxel space.
        outvox: Output file with displacements in source-voxel space.
        insrcgeom: Specify source image geometry (moving volume).
        downsample: Downsample output M3Z to spacing of 2.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriWarpConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_WARP_CONVERT_METADATA)
    cargs = []
    cargs.append("mri_warp_convert")
    if invox is not None:
        cargs.extend([
            "--invox",
            execution.input_file(invox)
        ])
    if outvox is not None:
        cargs.extend([
            "--outvox",
            outvox
        ])
    if insrcgeom is not None:
        cargs.extend([
            "--insrcgeom",
            execution.input_file(insrcgeom)
        ])
    if downsample:
        cargs.append("--downsample")
    ret = MriWarpConvertOutputs(
        root=execution.output_file("."),
        outwarp=execution.output_file(outvox) if (outvox is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_WARP_CONVERT_METADATA",
    "MriWarpConvertOutputs",
    "mri_warp_convert",
]