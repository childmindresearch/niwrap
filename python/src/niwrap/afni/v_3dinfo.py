# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DINFO_METADATA = Metadata(
    id="7079ec8db29fc5abd9efaff614f2daa00228ff5e.boutiques",
    name="3dinfo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3dinfo(
    runner: Runner | None = None,
) -> V3dinfoOutputs:
    """
    Prints out sort-of-useful information from a 3D dataset's header.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dinfo.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DINFO_METADATA)
    cargs = []
    cargs.append("3dinfo")
    cargs.append("[OPTIONS]")
    cargs.append("DATASET")
    cargs.append("[DATASET...]")
    ret = V3dinfoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dinfoOutputs",
    "V_3DINFO_METADATA",
    "v_3dinfo",
]