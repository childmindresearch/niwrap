# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VERTEXVOL_METADATA = Metadata(
    id="43f2f0ece18dc9707df38e81102c8d727e4682e9.boutiques",
    name="vertexvol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
VertexvolParameters = typing.TypedDict('VertexvolParameters', {
    "__STYX_TYPE__": typing.Literal["vertexvol"],
    "subject": str,
    "right_hemisphere": bool,
    "output_file": typing.NotRequired[str | None],
    "no_th3": bool,
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
        "vertexvol": vertexvol_cargs,
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
        "vertexvol": vertexvol_outputs,
    }.get(t)


class VertexvolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vertexvol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType | None
    """Output file containing vertex-wise volume"""


def vertexvol_params(
    subject: str,
    right_hemisphere: bool = False,
    output_file: str | None = "?h.volume",
    no_th3: bool = False,
) -> VertexvolParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        right_hemisphere: Select right hemisphere.
        output_file: Output file name, default is ?h.volume.
        no_th3: Don't use TH3 method for computation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "vertexvol",
        "subject": subject,
        "right_hemisphere": right_hemisphere,
        "no_th3": no_th3,
    }
    if output_file is not None:
        params["output_file"] = output_file
    return params


def vertexvol_cargs(
    params: VertexvolParameters,
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
    cargs.append("vertexvol")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("right_hemisphere"):
        cargs.append("--rh")
    if params.get("output_file") is not None:
        cargs.extend([
            "--o",
            params.get("output_file")
        ])
    if params.get("no_th3"):
        cargs.append("--no-th3")
    return cargs


def vertexvol_outputs(
    params: VertexvolParameters,
    execution: Execution,
) -> VertexvolOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VertexvolOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def vertexvol_execute(
    params: VertexvolParameters,
    execution: Execution,
) -> VertexvolOutputs:
    """
    Computes vertex-wise volume (and mid.area).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VertexvolOutputs`).
    """
    params = execution.params(params)
    cargs = vertexvol_cargs(params, execution)
    ret = vertexvol_outputs(params, execution)
    execution.run(cargs)
    return ret


def vertexvol(
    subject: str,
    right_hemisphere: bool = False,
    output_file: str | None = "?h.volume",
    no_th3: bool = False,
    runner: Runner | None = None,
) -> VertexvolOutputs:
    """
    Computes vertex-wise volume (and mid.area).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        right_hemisphere: Select right hemisphere.
        output_file: Output file name, default is ?h.volume.
        no_th3: Don't use TH3 method for computation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VertexvolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VERTEXVOL_METADATA)
    params = vertexvol_params(subject=subject, right_hemisphere=right_hemisphere, output_file=output_file, no_th3=no_th3)
    return vertexvol_execute(params, execution)


__all__ = [
    "VERTEXVOL_METADATA",
    "VertexvolOutputs",
    "VertexvolParameters",
    "vertexvol",
    "vertexvol_params",
]
