# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLHD_METADATA = Metadata(
    id="fffbfda4d7cd52a4364b0d99935e55a5d49cd5e1",
    name="fslhd",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslhdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslhd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslhd(
    input_file: InputPathType,
    xml_flag: bool = False,
    runner: Runner | None = None,
) -> FslhdOutputs:
    """
    fslhd by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Display header information from a NIFTI file.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils#FSLHD
    
    Args:
        input_file: Input NIFTI file.
        xml_flag: Print an XML-style NIFTI header.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslhdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLHD_METADATA)
    cargs = []
    cargs.append("fslhd")
    if xml_flag:
        cargs.append("-x")
    cargs.append(execution.input_file(input_file))
    ret = FslhdOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLHD_METADATA",
    "FslhdOutputs",
    "fslhd",
]
