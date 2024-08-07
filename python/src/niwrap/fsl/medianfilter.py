# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MEDIANFILTER_METADATA = Metadata(
    id="eb3ef93f1100c3353ba46099d77c2e2452efa1e6",
    name="medianfilter",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="your-default-docker-image:latest",
)


class MedianfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `medianfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filtered_file: OutputPathType
    """Output file containing the median filtered image"""


def medianfilter(
    infile: InputPathType,
    outfile: InputPathType,
    runner: Runner | None = None,
) -> MedianfilterOutputs:
    """
    medianfilter by Unknown.
    
    A tool to perform 26 neighbourhood median filtering on an input image.
    
    Args:
        infile: Input image file to be filtered (e.g., img.nii.gz).
        outfile: Output file to store the filtered image (e.g.,\
            img_filtered.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MedianfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MEDIANFILTER_METADATA)
    cargs = []
    cargs.append("medianfilter")
    cargs.append(execution.input_file(infile))
    cargs.append(execution.input_file(outfile))
    ret = MedianfilterOutputs(
        root=execution.output_file("."),
        filtered_file=execution.output_file(f"{pathlib.Path(outfile).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MEDIANFILTER_METADATA",
    "MedianfilterOutputs",
    "medianfilter",
]
