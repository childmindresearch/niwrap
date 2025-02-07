# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

STRBLAST_METADATA = Metadata(
    id="a2cee2c629b430408b17d4c3a5b48c6d60070e17.boutiques",
    name="strblast",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
StrblastParameters = typing.TypedDict('StrblastParameters', {
    "__STYX_TYPE__": typing.Literal["strblast"],
    "targetstring": str,
    "input_files": list[InputPathType],
    "new_char": typing.NotRequired[str | None],
    "new_string": typing.NotRequired[str | None],
    "unescape": bool,
    "quiet": bool,
    "help": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "strblast": strblast_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "strblast": strblast_outputs,
    }.get(t)


class StrblastOutputs(typing.NamedTuple):
    """
    Output object returned when calling `strblast(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def strblast_params(
    targetstring: str,
    input_files: list[InputPathType],
    new_char: str | None = None,
    new_string: str | None = None,
    unescape: bool = False,
    quiet: bool = False,
    help_: bool = False,
) -> StrblastParameters:
    """
    Build parameters.
    
    Args:
        targetstring: Target string to search for in the input files.
        input_files: Input files to search for the target string.
        new_char: Replace TARGETSTRING with CHAR (repeated).
        new_string: Replace TARGETSTRING with STRING.
        unescape: Parse TARGETSTRING for escaped characters (includes '\\t',\
            '\\n', '\\r').
        quiet: Do not report files with no strings found. Use -quiet -quiet to\
            avoid any reporting.
        help_: Show help message and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "strblast",
        "targetstring": targetstring,
        "input_files": input_files,
        "unescape": unescape,
        "quiet": quiet,
        "help": help_,
    }
    if new_char is not None:
        params["new_char"] = new_char
    if new_string is not None:
        params["new_string"] = new_string
    return params


def strblast_cargs(
    params: StrblastParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("strblast")
    cargs.append(params.get("targetstring"))
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    if params.get("new_char") is not None:
        cargs.extend([
            "-new_char",
            params.get("new_char")
        ])
    if params.get("new_string") is not None:
        cargs.extend([
            "-new_string",
            params.get("new_string")
        ])
    if params.get("unescape"):
        cargs.append("-unescape")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def strblast_outputs(
    params: StrblastParameters,
    execution: Execution,
) -> StrblastOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = StrblastOutputs(
        root=execution.output_file("."),
    )
    return ret


def strblast_execute(
    params: StrblastParameters,
    execution: Execution,
) -> StrblastOutputs:
    """
    Finds exact copies of the target string in each of the input files, and replaces
    all characters with some junk string.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `StrblastOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = strblast_cargs(params, execution)
    ret = strblast_outputs(params, execution)
    execution.run(cargs)
    return ret


def strblast(
    targetstring: str,
    input_files: list[InputPathType],
    new_char: str | None = None,
    new_string: str | None = None,
    unescape: bool = False,
    quiet: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> StrblastOutputs:
    """
    Finds exact copies of the target string in each of the input files, and replaces
    all characters with some junk string.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        targetstring: Target string to search for in the input files.
        input_files: Input files to search for the target string.
        new_char: Replace TARGETSTRING with CHAR (repeated).
        new_string: Replace TARGETSTRING with STRING.
        unescape: Parse TARGETSTRING for escaped characters (includes '\\t',\
            '\\n', '\\r').
        quiet: Do not report files with no strings found. Use -quiet -quiet to\
            avoid any reporting.
        help_: Show help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StrblastOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STRBLAST_METADATA)
    params = strblast_params(targetstring=targetstring, input_files=input_files, new_char=new_char, new_string=new_string, unescape=unescape, quiet=quiet, help_=help_)
    return strblast_execute(params, execution)


__all__ = [
    "STRBLAST_METADATA",
    "StrblastOutputs",
    "StrblastParameters",
    "strblast",
    "strblast_params",
]
