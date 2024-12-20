# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_COMPARE_AFFINE_METADATA = Metadata(
    id="05a5d8e8f58b82dd3d94b8878f12307d386f682c.boutiques",
    name="3dCompareAffine",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dCompareAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_compare_affine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing comparison results of affine transformations"""


def v_3d_compare_affine(
    mask: str | None = None,
    dset: InputPathType | None = None,
    affine: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dCompareAffineOutputs:
    """
    Compares two (or more) affine spatial transformations on a dataset and outputs
    measurements of their differences in spatial displacements.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        mask: Dataset containing non-zero voxels used as the region over which\
            to compare the affine transformations.
        dset: Dataset to compute an automask from it and use that mask as the\
            spatial region for comparison.
        affine: Input an affine transformation (file or 'MATRIX'). Multiple\
            '-affine' options can be used to input multiple files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dCompareAffineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_COMPARE_AFFINE_METADATA)
    cargs = []
    cargs.append("3dCompareAffine")
    if mask is not None:
        cargs.extend([
            "-mask",
            mask
        ])
    if dset is not None:
        cargs.extend([
            "-dset",
            execution.input_file(dset)
        ])
    if affine is not None:
        cargs.extend([
            "-affine",
            *affine
        ])
    ret = V3dCompareAffineOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("[OUTPUT_PREFIX]_comparison.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dCompareAffineOutputs",
    "V_3D_COMPARE_AFFINE_METADATA",
    "v_3d_compare_affine",
]
