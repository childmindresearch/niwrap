# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMGLOB_METADATA = Metadata(
    id="29838e0b15373b5dabb2c3c1f512b877c72b74fd",
    name="imglob",
)


class ImglobOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imglob(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def imglob(
    input_list: list[str],
    single_extension: bool = False,
    multiple_extensions: bool = False,
    runner: Runner | None = None,
) -> ImglobOutputs:
    """
    imglob by Software Author.
    
    Tool for generating image lists with specific extensions.
    
    Args:
        input_list: List of image names or file paths.
        single_extension: Output one image with full extension.
        multiple_extensions: Output list of images with full extensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImglobOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        single_extension +
        multiple_extensions
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "single_extension,\n"
            "multiple_extensions"
        )
    execution = runner.start_execution(IMGLOB_METADATA)
    cargs = []
    cargs.append("imglob")
    if multiple_extensions:
        cargs.append("-extensions")
    cargs.extend(input_list)
    ret = ImglobOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMGLOB_METADATA",
    "ImglobOutputs",
    "imglob",
]
