# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMSTAT_METADATA = Metadata(
    id="b9be114b2b3c5fb54ece698b7c389a7115f3d9fc",
    name="imstat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ImstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mean_output: OutputPathType | None
    """Mean of pixel-wise statistics for the collection of 2D images"""
    sdev_output: OutputPathType | None
    """Standard deviation of pixel-wise statistics for the collection of 2D images"""


def imstat(
    image_files: list[InputPathType],
    no_label: bool = False,
    quiet: bool = False,
    pixstat_prefix: str | None = None,
    runner: Runner | None = None,
) -> ImstatOutputs:
    """
    imstat by AFNI Team.
    
    Calculation of statistics of one or more images.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/imstat.html
    
    Args:
        image_files: Input image file(s).
        no_label: Don't write labels on each file's summary line.
        quiet: Don't print statistics for each file.
        pixstat_prefix: If more than one image file is given, then\
            'prefix.mean' and 'prefix.sdev' will be written as the pixel-wise\
            statistics images of the whole collection. These images will be in the\
            'flim' floating point format. [This option only works on 2D images!].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMSTAT_METADATA)
    cargs = []
    cargs.append("imstat")
    if no_label:
        cargs.append("-nolabel")
    if quiet:
        cargs.append("-quiet")
    if pixstat_prefix is not None:
        cargs.extend(["-pixstat", pixstat_prefix])
    cargs.extend([execution.input_file(f) for f in image_files])
    ret = ImstatOutputs(
        root=execution.output_file("."),
        mean_output=execution.output_file(f"{pixstat_prefix}.mean", optional=True) if pixstat_prefix is not None else None,
        sdev_output=execution.output_file(f"{pixstat_prefix}.sdev", optional=True) if pixstat_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMSTAT_METADATA",
    "ImstatOutputs",
    "imstat",
]
