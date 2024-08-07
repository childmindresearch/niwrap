# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

LESION_FILLING_METADATA = Metadata(
    id="c456a3cba760f1dc8235c3023931caf8ff50ef5d",
    name="lesion_filling",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class LesionFillingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `lesion_filling(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Lesion filled output image"""


def lesion_filling(
    infile: InputPathType,
    outfile: str,
    lesionmask: InputPathType,
    wmmask: InputPathType | None = None,
    verbose_flag: bool = False,
    components_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> LesionFillingOutputs:
    """
    lesion_filling by University of Oxford (Mark Jenkinson & Taylor Hanayik).
    
    Lesion filling tool as part of FSL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/LESION_FILLING
    
    Args:
        infile: Input image filename (e.g., T1w image).
        outfile: Output filename (lesion filled image).
        lesionmask: Filename of lesion mask image.
        wmmask: Filename of white matter mask image.
        verbose_flag: Switch on diagnostic messages.
        components_flag: Save all lesion components as volumes.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LesionFillingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LESION_FILLING_METADATA)
    cargs = []
    cargs.append("lesion_filling")
    cargs.extend(["-i", execution.input_file(infile)])
    cargs.extend(["-o", outfile])
    cargs.extend(["-l", execution.input_file(lesionmask)])
    if wmmask is not None:
        cargs.extend(["-w", execution.input_file(wmmask)])
    if verbose_flag:
        cargs.append("-v")
    if components_flag:
        cargs.append("-c")
    ret = LesionFillingOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{outfile}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LESION_FILLING_METADATA",
    "LesionFillingOutputs",
    "lesion_filling",
]
