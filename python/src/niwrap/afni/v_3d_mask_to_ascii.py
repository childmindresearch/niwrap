# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_MASK_TO_ASCII_METADATA = Metadata(
    id="b850d6d473bbf3763cf436e175726b9f36196b22",
    name="3dMaskToASCII",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dMaskToAsciiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mask_to_ascii(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outputfile: OutputPathType
    """Output file where ASCII string mask or binary mask will be written."""


def v_3d_mask_to_ascii(
    dataset: InputPathType,
    tobin_flag: bool = False,
    runner: Runner | None = None,
) -> V3dMaskToAsciiOutputs:
    """
    3dMaskToASCII by AFNI Team.
    
    Converts a byte-valued 0/1 dataset into an ASCII string, or vice versa.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dMaskToASCII.html
    
    Args:
        dataset: Input dataset (e.g. mask.nii.gz).
        tobin_flag: Read ASCII mask, expand it to byte-valued dataset, and\
            write to stdout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMaskToAsciiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MASK_TO_ASCII_METADATA)
    cargs = []
    cargs.append("3dMaskToASCII")
    if tobin_flag:
        cargs.append("-tobin")
    cargs.append(execution.input_file(dataset))
    cargs.append(">")
    cargs.append("[OUTPUTFILE]")
    ret = V3dMaskToAsciiOutputs(
        root=execution.output_file("."),
        outputfile=execution.output_file(f"[OUTPUTFILE]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dMaskToAsciiOutputs",
    "V_3D_MASK_TO_ASCII_METADATA",
    "v_3d_mask_to_ascii",
]
