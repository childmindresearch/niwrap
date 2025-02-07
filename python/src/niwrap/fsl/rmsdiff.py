# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RMSDIFF_METADATA = Metadata(
    id="721e867f6f94c898ce8453a6c1d46d329b31f94e.boutiques",
    name="rmsdiff",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
RmsdiffParameters = typing.TypedDict('RmsdiffParameters', {
    "__STYX_TYPE__": typing.Literal["rmsdiff"],
    "matrixfile1": InputPathType,
    "matrixfile2": InputPathType,
    "refvol": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
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
        "rmsdiff": rmsdiff_cargs,
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
        "rmsdiff": rmsdiff_outputs,
    }.get(t)


class RmsdiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rmsdiff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rmsdiff_params(
    matrixfile1: InputPathType,
    matrixfile2: InputPathType,
    refvol: InputPathType,
    mask: InputPathType | None = None,
) -> RmsdiffParameters:
    """
    Build parameters.
    
    Args:
        matrixfile1: First matrix file.
        matrixfile2: Second matrix file.
        refvol: Reference volume.
        mask: Optional mask.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rmsdiff",
        "matrixfile1": matrixfile1,
        "matrixfile2": matrixfile2,
        "refvol": refvol,
    }
    if mask is not None:
        params["mask"] = mask
    return params


def rmsdiff_cargs(
    params: RmsdiffParameters,
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
    cargs.append("rmsdiff")
    cargs.append(execution.input_file(params.get("matrixfile1")))
    cargs.append(execution.input_file(params.get("matrixfile2")))
    cargs.append(execution.input_file(params.get("refvol")))
    if params.get("mask") is not None:
        cargs.append(execution.input_file(params.get("mask")))
    return cargs


def rmsdiff_outputs(
    params: RmsdiffParameters,
    execution: Execution,
) -> RmsdiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RmsdiffOutputs(
        root=execution.output_file("."),
    )
    return ret


def rmsdiff_execute(
    params: RmsdiffParameters,
    execution: Execution,
) -> RmsdiffOutputs:
    """
    Outputs RMS deviation between matrices (in mm).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RmsdiffOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = rmsdiff_cargs(params, execution)
    ret = rmsdiff_outputs(params, execution)
    execution.run(cargs)
    return ret


def rmsdiff(
    matrixfile1: InputPathType,
    matrixfile2: InputPathType,
    refvol: InputPathType,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> RmsdiffOutputs:
    """
    Outputs RMS deviation between matrices (in mm).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        matrixfile1: First matrix file.
        matrixfile2: Second matrix file.
        refvol: Reference volume.
        mask: Optional mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RmsdiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RMSDIFF_METADATA)
    params = rmsdiff_params(matrixfile1=matrixfile1, matrixfile2=matrixfile2, refvol=refvol, mask=mask)
    return rmsdiff_execute(params, execution)


__all__ = [
    "RMSDIFF_METADATA",
    "RmsdiffOutputs",
    "RmsdiffParameters",
    "rmsdiff",
    "rmsdiff_params",
]
