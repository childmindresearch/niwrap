# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TSORT_METADATA = Metadata(
    id="28c28b79e328ac59d8297a59e0298ad19fb48796.boutiques",
    name="3dTsort",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dTsortOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tsort(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType | None
    """Main default output of 3dTsort"""


def v_3d_tsort(
    input_file: InputPathType,
    prefix: str | None = None,
    dec: bool = False,
    rank: bool = False,
    ind: bool = False,
    val: bool = False,
    random_: bool = False,
    ranfft: bool = False,
    randft: bool = False,
    datum: str | None = None,
    runner: Runner | None = None,
) -> V3dTsortOutputs:
    """
    Sorts each voxel in a dataset and produces a new dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input dataset to be sorted.
        prefix: Prefix for the output dataset.
        dec: Sort into decreasing order.
        rank: Output rank instead of sorted values; ranks range from 1 to Nvals.
        ind: Output sorting index (0 to Nvals -1).
        val: Output sorted values (default).
        random_: Randomly shuffle (permute) the time points in each voxel.
        ranfft: Randomize each time series by scrambling the FFT phase.
        randft: Randomize each time series by scrambling the DFT phase.
        datum: Coerce the output data to be stored as the given type (byte,\
            short, or float).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTsortOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TSORT_METADATA)
    cargs = []
    cargs.append("3dTsort")
    cargs.append(execution.input_file(input_file))
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if dec:
        cargs.append("-dec")
    if rank:
        cargs.append("-rank")
    if ind:
        cargs.append("-ind")
    if val:
        cargs.append("-val")
    if random_:
        cargs.append("-random")
    if ranfft:
        cargs.append("-ranFFT")
    if randft:
        cargs.append("-ranDFT")
    if datum is not None:
        cargs.extend([
            "-datum",
            datum
        ])
    ret = V3dTsortOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(prefix + ".nii.gz") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTsortOutputs",
    "V_3D_TSORT_METADATA",
    "v_3d_tsort",
]
