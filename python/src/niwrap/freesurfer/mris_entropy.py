# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ENTROPY_METADATA = Metadata(
    id="5707967e94407108591e9f09a18741e3c81c9aed.boutiques",
    name="mris_entropy",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisEntropyParameters = typing.TypedDict('MrisEntropyParameters', {
    "__STYX_TYPE__": typing.Literal["mris_entropy"],
    "subject": str,
    "hemi": str,
    "wfile": InputPathType,
    "curvfile": InputPathType,
    "average_iterations": typing.NotRequired[float | None],
    "normalize": bool,
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
        "mris_entropy": mris_entropy_cargs,
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
        "mris_entropy": mris_entropy_outputs,
    }.get(t)


class MrisEntropyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_entropy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file containing the computed entropy"""


def mris_entropy_params(
    subject: str,
    hemi: str,
    wfile: InputPathType,
    curvfile: InputPathType,
    average_iterations: float | None = 0,
    normalize: bool = False,
) -> MrisEntropyParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject ID.
        hemi: Hemisphere (e.g., lh or rh).
        wfile: Weight file for surface.
        curvfile: Curvature file for input.
        average_iterations: Specify number of curvature averaging iterations\
            (default=0).
        normalize: Normalize curvature before writing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_entropy",
        "subject": subject,
        "hemi": hemi,
        "wfile": wfile,
        "curvfile": curvfile,
        "normalize": normalize,
    }
    if average_iterations is not None:
        params["average_iterations"] = average_iterations
    return params


def mris_entropy_cargs(
    params: MrisEntropyParameters,
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
    cargs.append("mris_entropy")
    cargs.append(params.get("subject"))
    cargs.append(params.get("hemi"))
    cargs.append(execution.input_file(params.get("wfile")))
    cargs.append(execution.input_file(params.get("curvfile")))
    if params.get("average_iterations") is not None:
        cargs.extend([
            "-a",
            str(params.get("average_iterations"))
        ])
    if params.get("normalize"):
        cargs.append("-n")
    return cargs


def mris_entropy_outputs(
    params: MrisEntropyParameters,
    execution: Execution,
) -> MrisEntropyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisEntropyOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("subject") + "_" + params.get("hemi") + "_output.txt"),
    )
    return ret


def mris_entropy_execute(
    params: MrisEntropyParameters,
    execution: Execution,
) -> MrisEntropyOutputs:
    """
    Computes the entropy of a surface activation pattern for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisEntropyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_entropy_cargs(params, execution)
    ret = mris_entropy_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_entropy(
    subject: str,
    hemi: str,
    wfile: InputPathType,
    curvfile: InputPathType,
    average_iterations: float | None = 0,
    normalize: bool = False,
    runner: Runner | None = None,
) -> MrisEntropyOutputs:
    """
    Computes the entropy of a surface activation pattern for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject ID.
        hemi: Hemisphere (e.g., lh or rh).
        wfile: Weight file for surface.
        curvfile: Curvature file for input.
        average_iterations: Specify number of curvature averaging iterations\
            (default=0).
        normalize: Normalize curvature before writing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisEntropyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ENTROPY_METADATA)
    params = mris_entropy_params(subject=subject, hemi=hemi, wfile=wfile, curvfile=curvfile, average_iterations=average_iterations, normalize=normalize)
    return mris_entropy_execute(params, execution)


__all__ = [
    "MRIS_ENTROPY_METADATA",
    "MrisEntropyOutputs",
    "MrisEntropyParameters",
    "mris_entropy",
    "mris_entropy_params",
]
