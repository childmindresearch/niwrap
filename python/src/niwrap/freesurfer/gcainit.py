# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GCAINIT_METADATA = Metadata(
    id="00dfdd96c6b86f2b1c5b47fc4b41253a5bcd0e9f.boutiques",
    name="gcainit",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
GcainitParameters = typing.TypedDict('GcainitParameters', {
    "__STYX_TYPE__": typing.Literal["gcainit"],
    "gcadir": str,
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
        "gcainit": gcainit_cargs,
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


class GcainitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gcainit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gcainit_params(
    gcadir: str,
) -> GcainitParameters:
    """
    Build parameters.
    
    Args:
        gcadir: Output directory of gcaprep.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gcainit",
        "gcadir": gcadir,
    }
    return params


def gcainit_cargs(
    params: GcainitParameters,
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
    cargs.append("gcainit")
    cargs.extend([
        "--g",
        params.get("gcadir")
    ])
    return cargs


def gcainit_outputs(
    params: GcainitParameters,
    execution: Execution,
) -> GcainitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GcainitOutputs(
        root=execution.output_file("."),
    )
    return ret


def gcainit_execute(
    params: GcainitParameters,
    execution: Execution,
) -> GcainitOutputs:
    """
    Initializes the GCA for brain processing tasks.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GcainitOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = gcainit_cargs(params, execution)
    ret = gcainit_outputs(params, execution)
    execution.run(cargs)
    return ret


def gcainit(
    gcadir: str,
    runner: Runner | None = None,
) -> GcainitOutputs:
    """
    Initializes the GCA for brain processing tasks.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gcadir: Output directory of gcaprep.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GcainitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GCAINIT_METADATA)
    params = gcainit_params(gcadir=gcadir)
    return gcainit_execute(params, execution)


__all__ = [
    "GCAINIT_METADATA",
    "GcainitOutputs",
    "GcainitParameters",
    "gcainit",
    "gcainit_params",
]
