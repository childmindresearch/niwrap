# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ENTROPY_METADATA = Metadata(
    id="65268d877950e23f9bd06dfb7ede10b57050e1e9.boutiques",
    name="3dEntropy",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dEntropyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_entropy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_entropy(
    input_dataset: InputPathType,
    zskip: bool = False,
    runner: Runner | None = None,
) -> V3dEntropyOutputs:
    """
    Computes entropy for a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (stored as 16 bit shorts).
        zskip: Skip 0 values in the entropy computation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEntropyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ENTROPY_METADATA)
    cargs = []
    cargs.append("3dEntropy")
    if zskip:
        cargs.append("-zskip")
    cargs.append(execution.input_file(input_dataset))
    ret = V3dEntropyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dEntropyOutputs",
    "V_3D_ENTROPY_METADATA",
    "v_3d_entropy",
]
