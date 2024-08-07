# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ROW_FILLIN_METADATA = Metadata(
    id="9b95a35c02918750c1ae17e8e318aa5995490681",
    name="3dRowFillin",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dRowFillinOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_row_fillin(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType | None
    """Output dataset in BRIK format"""
    output_head: OutputPathType | None
    """Output dataset in HEAD format"""


def v_3d_row_fillin(
    input_dataset: InputPathType,
    maxgap: float | int | None = None,
    dir_: str | None = None,
    binary: bool = False,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dRowFillinOutputs:
    """
    3dRowFillin by AFNI Team.
    
    Fills in blank regions in 1D rows extracted from a 3D dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dRowFillin.html
    
    Args:
        input_dataset: Input 3D dataset (e.g., dataset+orig).
        maxgap: Set the maximum length of a blank region that will be filled in.
        dir_: Set the direction of fill, e.g., A-P, P-A, I-S, S-I, L-R, R-L, x,\
            y, z, XYZ.OR, XYZ.AND.
        binary: Turn input dataset to binary (0 and 1) before filling in.\
            Output will also be binary.
        prefix: Set the prefix for the output dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRowFillinOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ROW_FILLIN_METADATA)
    cargs = []
    cargs.append("3dRowFillin")
    if maxgap is not None:
        cargs.extend(["-maxgap", str(maxgap)])
    if dir_ is not None:
        cargs.extend(["-dir", dir_])
    if binary:
        cargs.append("-binary")
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    cargs.append(execution.input_file(input_dataset))
    ret = V3dRowFillinOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(f"{prefix}+orig.BRIK") if prefix is not None else None,
        output_head=execution.output_file(f"{prefix}+orig.HEAD") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dRowFillinOutputs",
    "V_3D_ROW_FILLIN_METADATA",
    "v_3d_row_fillin",
]
