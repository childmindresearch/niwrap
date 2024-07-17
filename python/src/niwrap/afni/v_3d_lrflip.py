# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_LRFLIP_METADATA = Metadata(
    id="f40a6fcdc3a3daf5efa03fb37a609a7e32d731be",
    name="3dLRflip",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dLrflipOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lrflip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    flipped_output: OutputPathType | None
    """Output dataset after flipping"""


def v_3d_lrflip(
    datasets: list[InputPathType],
    output_prefix: str | None = None,
    flip_lr: bool = False,
    flip_ap: bool = False,
    flip_is: bool = False,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    runner: Runner | None = None,
) -> V3dLrflipOutputs:
    """
    3dLRflip by AFNI Team.
    
    Flips the rows of a dataset along one of the three axes to correct dataset
    direction labeling errors.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLRflip.html
    
    Args:
        datasets: Datasets to flip.
        output_prefix: Prefix to use for output. If multiple datasets are\
            input, the program will choose a prefix for each output.
        flip_lr: Flip about Left-Right axis.
        flip_ap: Flip about Anterior-Posterior axis.
        flip_is: Flip about Inferior-Superior axis.
        flip_x: Flip about the 1st direction.
        flip_y: Flip about the 2nd direction.
        flip_z: Flip about the 3rd direction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLrflipOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LRFLIP_METADATA)
    cargs = []
    cargs.append("3dLRflip")
    if flip_z:
        cargs.append("-Z")
    if output_prefix is not None:
        cargs.extend(["-prefix", output_prefix])
    cargs.extend([execution.input_file(f) for f in datasets])
    ret = V3dLrflipOutputs(
        root=execution.output_file("."),
        flipped_output=execution.output_file(f"{output_prefix}*", optional=True) if output_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLrflipOutputs",
    "V_3D_LRFLIP_METADATA",
    "v_3d_lrflip",
]
