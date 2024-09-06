# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ZCUTUP_METADATA = Metadata(
    id="4acd4850d9032c0dbd63b04da2b00bc69664b6bd",
    name="3dZcutup",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dZcutupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zcutup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType | None
    """The output dataset HEAD file"""
    output_brik: OutputPathType | None
    """The output dataset BRIK file"""


def v_3d_zcutup(
    dataset: InputPathType,
    keep_slices: str,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dZcutupOutputs:
    """
    3dZcutup by AFNI Team.
    
    Cut slices off a dataset in its z-direction and write a new dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dZcutup.html
    
    Args:
        dataset: The input dataset (e.g., epi07+orig). You can use a sub-brick\
            selector on the input dataset.
        keep_slices: Keep slices numbered 'b' through 't', inclusive. This is a\
            mandatory option. Slice numbers start at 0.
        prefix: Write result into dataset with the given prefix [default =\
            'zcutup'].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZcutupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZCUTUP_METADATA)
    cargs = []
    cargs.append("3dZcutup")
    cargs.append("-keep")
    cargs.extend(["-keep", keep_slices])
    cargs.append("-prefix")
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    cargs.append(execution.input_file(dataset))
    ret = V3dZcutupOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(f"{prefix}+orig.HEAD") if prefix is not None else None,
        output_brik=execution.output_file(f"{prefix}+orig.BRIK") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dZcutupOutputs",
    "V_3D_ZCUTUP_METADATA",
    "v_3d_zcutup",
]