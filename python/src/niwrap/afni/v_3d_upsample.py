# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_UPSAMPLE_METADATA = Metadata(
    id="e4750d1cff9a9b319ed4f1652bde0087af37e6dc.boutiques",
    name="3dUpsample",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dUpsampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_upsample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType | None
    """Upsampled dataset in BRIK format."""
    output_head: OutputPathType | None
    """Header information for the upsampled dataset."""


def v_3d_upsample(
    upsample_factor: int,
    input_dataset: str,
    linear_interpolation: bool = False,
    output_prefix: str | None = None,
    verbose_flag: bool = False,
    datatype: str | None = None,
    runner: Runner | None = None,
) -> V3dUpsampleOutputs:
    """
    Upsamples a 3D+time dataset in the time direction by a specified factor.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        upsample_factor: Upsampling factor; must be between 2 and 320\
            (inclusive).
        input_dataset: Input dataset.
        linear_interpolation: Use linear interpolation instead of 7th order\
            polynomial interpolation.
        output_prefix: Define the prefix name of the output dataset; default is\
            'Upsam'.
        verbose_flag: Print verbose output.
        datatype: Specify the datatype for the output dataset (float, short,\
            byte); default is float.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dUpsampleOutputs`).
    """
    if not (2 <= upsample_factor <= 320): 
        raise ValueError(f"'upsample_factor' must be between 2 <= x <= 320 but was {upsample_factor}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_UPSAMPLE_METADATA)
    cargs = []
    cargs.append("3dUpsample")
    cargs.extend([
        "-n",
        str(upsample_factor)
    ])
    cargs.extend([
        "-input",
        input_dataset
    ])
    if linear_interpolation:
        cargs.append("-1")
    if output_prefix is not None:
        cargs.extend([
            "-prefix",
            output_prefix
        ])
    if verbose_flag:
        cargs.append("-verb")
    if datatype is not None:
        cargs.extend([
            "-datum",
            datatype
        ])
    ret = V3dUpsampleOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(output_prefix + "+orig.BRIK") if (output_prefix is not None) else None,
        output_head=execution.output_file(output_prefix + "+orig.HEAD") if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dUpsampleOutputs",
    "V_3D_UPSAMPLE_METADATA",
    "v_3d_upsample",
]
