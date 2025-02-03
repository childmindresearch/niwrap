# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

NICAT_METADATA = Metadata(
    id="150f64c79ef2ef5b2c3f9c0b00bdeb1447c981cd.boutiques",
    name="nicat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
NicatParameters = typing.TypedDict('NicatParameters', {
    "__STYX_TYPE__": typing.Literal["nicat"],
    "stream_spec": str,
    "reopen": typing.NotRequired[str | None],
    "copy_stream": bool,
    "read_only": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "nicat": nicat_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {}
    return vt.get(t)


class NicatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nicat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def nicat_params(
    stream_spec: str,
    reopen: str | None = None,
    copy_stream: bool = False,
    read_only: bool = False,
) -> NicatParameters:
    """
    Build parameters.
    
    Args:
        stream_spec: Stream specification (e.g., tcp:localhost:4444).
        reopen: Reopen the stream after connection to the stream specified by\
            the given value.
        copy_stream: Copy the stream to stdout instead; the 'streamspec' will\
            be opened for reading.
        read_only: Read the stream but don't copy to stdout.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "nicat",
        "stream_spec": stream_spec,
        "copy_stream": copy_stream,
        "read_only": read_only,
    }
    if reopen is not None:
        params["reopen"] = reopen
    return params


def nicat_cargs(
    params: NicatParameters,
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
    cargs.append("nicat")
    cargs.append(params.get("stream_spec"))
    if params.get("reopen") is not None:
        cargs.extend([
            "-reopen",
            params.get("reopen")
        ])
    if params.get("copy_stream"):
        cargs.append("-r")
    if params.get("read_only"):
        cargs.append("-R")
    return cargs


def nicat_outputs(
    params: NicatParameters,
    execution: Execution,
) -> NicatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = NicatOutputs(
        root=execution.output_file("."),
    )
    return ret


def nicat_execute(
    params: NicatParameters,
    execution: Execution,
) -> NicatOutputs:
    """
    Copies stdin to the NIML stream, which will be opened for writing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `NicatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = nicat_cargs(params, execution)
    ret = nicat_outputs(params, execution)
    execution.run(cargs)
    return ret


def nicat(
    stream_spec: str,
    reopen: str | None = None,
    copy_stream: bool = False,
    read_only: bool = False,
    runner: Runner | None = None,
) -> NicatOutputs:
    """
    Copies stdin to the NIML stream, which will be opened for writing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        stream_spec: Stream specification (e.g., tcp:localhost:4444).
        reopen: Reopen the stream after connection to the stream specified by\
            the given value.
        copy_stream: Copy the stream to stdout instead; the 'streamspec' will\
            be opened for reading.
        read_only: Read the stream but don't copy to stdout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NicatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NICAT_METADATA)
    params = nicat_params(stream_spec=stream_spec, reopen=reopen, copy_stream=copy_stream, read_only=read_only)
    return nicat_execute(params, execution)


__all__ = [
    "NICAT_METADATA",
    "NicatOutputs",
    "nicat",
    "nicat_params",
]
