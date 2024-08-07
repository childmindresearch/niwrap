# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PARSE_NAME_METADATA = Metadata(
    id="f2fca43e72ebbbe55dd71701837afcbff9f18f9a",
    name="ParseName",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ParseNameOutputs(typing.NamedTuple):
    """
    Output object returned when calling `parse_name(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def parse_name(
    filename: str,
    cwd: str | None = None,
    pre: str | None = None,
    app: str | None = None,
    out_component: typing.Literal["FullName", "RelName", "AbsPath", "RelPath", "HeadName", "Prefix", "uPrefix", "pPrefix", "PPrefix", "*PrefixView", "OnDisk", "FName", "FNameNoAfniExt", "trim"] | None = None,
    out_separator: str | None = None,
    runner: Runner | None = None,
) -> ParseNameOutputs:
    """
    ParseName by AFNI Team.
    
    Parses filename into components useful for AFNI.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/ParseName.html
    
    Args:
        filename: File name to be parsed.
        cwd: Specify the working directory, from which the relative path is\
            constructed. Default is the program's CWD.
        pre: Change the name so that you prepend PRE to the prefix.
        app: Change the name so that you append APP to the prefix.
        out_component: Output specific component of the parsed file name.
        out_separator: When outputting multiple components, use SEP as a\
            separator between them. Default is ' '.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ParseNameOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PARSE_NAME_METADATA)
    cargs = []
    cargs.append("ParseName")
    cargs.append("[OPTIONAL_PARAMETERS]")
    cargs.append("<FName>")
    ret = ParseNameOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PARSE_NAME_METADATA",
    "ParseNameOutputs",
    "parse_name",
]
