# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_LFCD_METADATA = Metadata(
    id="3672a0a73f110863db06bed2e4d2f42fdd86772c",
    name="3dLFCD",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dLfcdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lfcd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_lfcd(
    in_file: InputPathType,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    polort: int | None = None,
    thresh: float | int | None = None,
    runner: Runner | None = None,
) -> V3dLfcdOutputs:
    """
    3dLFCD by AFNI Team.
    
    Performs degree centrality on a dataset using a given maskfile via the
    3dLFCD command.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLFCD.html
    
    Args:
        in_file: Input file to 3dlfcd.
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Mask the dataset to target brain-only voxels.
        mask: Mask file to mask input data.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        polort: No description provided.
        thresh: Threshold to exclude connections where corr <= thresh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLfcdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LFCD_METADATA)
    cargs = []
    cargs.append("3dLFCD")
    cargs.append(execution.input_file(in_file))
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if polort is not None:
        cargs.extend(["-polort", str(polort)])
    if thresh is not None:
        cargs.extend(["-thresh", str(thresh)])
    ret = V3dLfcdOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).name}_afni", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLfcdOutputs",
    "V_3D_LFCD_METADATA",
    "v_3d_lfcd",
]
