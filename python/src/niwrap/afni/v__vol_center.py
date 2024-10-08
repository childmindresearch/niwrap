# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__VOL_CENTER_METADATA = Metadata(
    id="9937026b44a9f1b535cc79485b75a3fad96b7a74.boutiques",
    name="@VolCenter",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VVolCenterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__vol_center(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__vol_center(
    dset: InputPathType,
    orient: str | None = None,
    runner: Runner | None = None,
) -> VVolCenterOutputs:
    """
    Tool to return the center of volume for a given dataset.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@VolCenter.html
    
    Args:
        dset: Input volume dataset.
        orient: Output coordinate system orientation (e.g., RAI).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VVolCenterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__VOL_CENTER_METADATA)
    cargs = []
    cargs.append("@VolCenter")
    cargs.extend([
        "-dset",
        execution.input_file(dset)
    ])
    if orient is not None:
        cargs.extend([
            "-or",
            orient
        ])
    ret = VVolCenterOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VVolCenterOutputs",
    "V__VOL_CENTER_METADATA",
    "v__vol_center",
]
