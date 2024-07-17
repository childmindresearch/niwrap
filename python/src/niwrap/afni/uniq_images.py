# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

UNIQ_IMAGES_METADATA = Metadata(
    id="a17e0745a1ac2f5b3c80cb86edb8b3948635aec1",
    name="uniq_images",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class UniqImagesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `uniq_images(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unique_files_list: OutputPathType
    """Generated list of filenames with unique images"""


def uniq_images(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> UniqImagesOutputs:
    """
    uniq_images by AFNI Team.
    
    Simple program to read in a list of image filenames, determine which files
    have unique images inside, and echo out only a list of the filenames with
    unique images.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/uniq_images.html
    
    Args:
        input_files: List of image filenames to be processed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UniqImagesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNIQ_IMAGES_METADATA)
    cargs = []
    cargs.append("uniq_images")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = UniqImagesOutputs(
        root=execution.output_file("."),
        unique_files_list=execution.output_file(f"unique_images_list.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UNIQ_IMAGES_METADATA",
    "UniqImagesOutputs",
    "uniq_images",
]
