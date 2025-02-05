# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLMERGE_METADATA = Metadata(
    id="5d8ea7aca79fd0b196c00441d4f31c201a3f63e6.boutiques",
    name="fslmerge",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslmergeParameters = typing.TypedDict('FslmergeParameters', {
    "__STYX_TYPE__": typing.Literal["fslmerge"],
    "merge_time": bool,
    "merge_set_tr": bool,
    "output_file": str,
    "input_files": list[InputPathType],
    "tr_value": typing.NotRequired[float | None],
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
        "fslmerge": fslmerge_cargs,
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
    vt = {
        "fslmerge": fslmerge_outputs,
    }
    return vt.get(t)


class FslmergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmerge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output concatenated image file"""


def fslmerge_params(
    output_file: str,
    input_files: list[InputPathType],
    merge_time: bool = False,
    merge_set_tr: bool = False,
    tr_value: float | None = None,
) -> FslmergeParameters:
    """
    Build parameters.
    
    Args:
        output_file: Output concatenated image file.
        input_files: Input image files to concatenate.
        merge_time: Concatenate images in time (4th dimension).
        merge_set_tr: Concatenate images in time and set the output image tr to\
            the provided value.
        tr_value: TR value in seconds, used with the -tr flag.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslmerge",
        "merge_time": merge_time,
        "merge_set_tr": merge_set_tr,
        "output_file": output_file,
        "input_files": input_files,
    }
    if tr_value is not None:
        params["tr_value"] = tr_value
    return params


def fslmerge_cargs(
    params: FslmergeParameters,
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
    cargs.append("fslmerge")
    if params.get("merge_time"):
        cargs.append("-t")
    if params.get("merge_set_tr"):
        cargs.append("-tr")
    cargs.append(params.get("output_file"))
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    if params.get("tr_value") is not None:
        cargs.append(str(params.get("tr_value")))
    return cargs


def fslmerge_outputs(
    params: FslmergeParameters,
    execution: Execution,
) -> FslmergeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslmergeOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("output_file")),
    )
    return ret


def fslmerge_execute(
    params: FslmergeParameters,
    execution: Execution,
) -> FslmergeOutputs:
    """
    FSL tool to concatenate images in various dimensions.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslmergeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslmerge_cargs(params, execution)
    ret = fslmerge_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslmerge(
    output_file: str,
    input_files: list[InputPathType],
    merge_time: bool = False,
    merge_set_tr: bool = False,
    tr_value: float | None = None,
    runner: Runner | None = None,
) -> FslmergeOutputs:
    """
    FSL tool to concatenate images in various dimensions.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_file: Output concatenated image file.
        input_files: Input image files to concatenate.
        merge_time: Concatenate images in time (4th dimension).
        merge_set_tr: Concatenate images in time and set the output image tr to\
            the provided value.
        tr_value: TR value in seconds, used with the -tr flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLMERGE_METADATA)
    params = fslmerge_params(merge_time=merge_time, merge_set_tr=merge_set_tr, output_file=output_file, input_files=input_files, tr_value=tr_value)
    return fslmerge_execute(params, execution)


__all__ = [
    "FSLMERGE_METADATA",
    "FslmergeOutputs",
    "FslmergeParameters",
    "fslmerge",
    "fslmerge_params",
]
