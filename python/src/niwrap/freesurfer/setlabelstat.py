# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SETLABELSTAT_METADATA = Metadata(
    id="4886639a09879a1b6f761d93393746968357bada.boutiques",
    name="setlabelstat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SetlabelstatParameters = typing.TypedDict('SetlabelstatParameters', {
    "__STYX_TYPE__": typing.Literal["setlabelstat"],
    "inlabelfile": InputPathType,
    "outlabelfile": InputPathType,
    "statval": float,
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
        "setlabelstat": setlabelstat_cargs,
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
        "setlabelstat": setlabelstat_outputs,
    }.get(t)


class SetlabelstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `setlabelstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """The resulting label file with updated stat values."""


def setlabelstat_params(
    inlabelfile: InputPathType,
    outlabelfile: InputPathType,
    statval: float,
    help_: bool = False,
) -> SetlabelstatParameters:
    """
    Build parameters.
    
    Args:
        inlabelfile: Input label file.
        outlabelfile: Output label file.
        statval: Stat value to replace in the label file.
        help_: Displays help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "setlabelstat",
        "inlabelfile": inlabelfile,
        "outlabelfile": outlabelfile,
        "statval": statval,
        "help": help_,
    }
    return params


def setlabelstat_cargs(
    params: SetlabelstatParameters,
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
    cargs.append("setlabelstat")
    cargs.extend([
        "-i",
        execution.input_file(params.get("inlabelfile"))
    ])
    cargs.extend([
        "-o",
        execution.input_file(params.get("outlabelfile"))
    ])
    cargs.extend([
        "-s",
        str(params.get("statval"))
    ])
    if params.get("help"):
        cargs.append("-help")
    return cargs


def setlabelstat_outputs(
    params: SetlabelstatParameters,
    execution: Execution,
) -> SetlabelstatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SetlabelstatOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(pathlib.Path(params.get("outlabelfile")).name),
    )
    return ret


def setlabelstat_execute(
    params: SetlabelstatParameters,
    execution: Execution,
) -> SetlabelstatOutputs:
    """
    Replaces the stat values in a label file with the single stat value supplied on
    the command-line.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SetlabelstatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = setlabelstat_cargs(params, execution)
    ret = setlabelstat_outputs(params, execution)
    execution.run(cargs)
    return ret


def setlabelstat(
    inlabelfile: InputPathType,
    outlabelfile: InputPathType,
    statval: float,
    help_: bool = False,
    runner: Runner | None = None,
) -> SetlabelstatOutputs:
    """
    Replaces the stat values in a label file with the single stat value supplied on
    the command-line.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inlabelfile: Input label file.
        outlabelfile: Output label file.
        statval: Stat value to replace in the label file.
        help_: Displays help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SetlabelstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SETLABELSTAT_METADATA)
    params = setlabelstat_params(inlabelfile=inlabelfile, outlabelfile=outlabelfile, statval=statval, help_=help_)
    return setlabelstat_execute(params, execution)


__all__ = [
    "SETLABELSTAT_METADATA",
    "SetlabelstatOutputs",
    "SetlabelstatParameters",
    "setlabelstat",
    "setlabelstat_params",
]
