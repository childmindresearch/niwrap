# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLFFT_METADATA = Metadata(
    id="ad11bfba23bb1392789a9fc677fd5e4e09fc9ac2",
    name="fslfft",
)


class FslfftOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslfft(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output volume result of the Fourier transform"""


def fslfft(
    input_volume: InputPathType,
    output_volume: InputPathType,
    inverse_flag: bool = False,
    runner: Runner = None,
) -> FslfftOutputs:
    """
    fslfft by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    A tool to compute the Fourier transform of an input volume and save the
    result in an output volume.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FT
    
    Args:
        input_volume: Input volume file (e.g. invol.nii.gz)
        output_volume: Output volume file (e.g. outvol.nii.gz)
        inverse_flag: Flag to perform the inverse Fourier transform
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslfftOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLFFT_METADATA)
    cargs = []
    cargs.append("fslfft")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(output_volume))
    if inverse_flag:
        cargs.append("-inv")
    ret = FslfftOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{pathlib.Path(output_volume).name}.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLFFT_METADATA",
    "FslfftOutputs",
    "fslfft",
]