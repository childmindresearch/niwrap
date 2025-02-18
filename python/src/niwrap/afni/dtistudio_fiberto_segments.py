# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DTISTUDIO_FIBERTO_SEGMENTS_METADATA = Metadata(
    id="3f18eb1cd61025f3b6f243c49c95ab75c9ad86a9.boutiques",
    name="DTIStudioFibertoSegments",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
DtistudioFibertoSegmentsParameters = typing.TypedDict('DtistudioFibertoSegmentsParameters', {
    "__STYX_TYPE__": typing.Literal["DTIStudioFibertoSegments"],
    "dataset": InputPathType,
    "output_file": typing.NotRequired[str | None],
    "swap_flag": bool,
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
        "DTIStudioFibertoSegments": dtistudio_fiberto_segments_cargs,
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
        "DTIStudioFibertoSegments": dtistudio_fiberto_segments_outputs,
    }.get(t)


class DtistudioFibertoSegmentsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dtistudio_fiberto_segments(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_segment_file: OutputPathType | None
    """Output SUMA segment file"""


def dtistudio_fiberto_segments_params(
    dataset: InputPathType,
    output_file: str | None = None,
    swap_flag: bool = False,
) -> DtistudioFibertoSegmentsParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset file.
        output_file: Name of the output file (default is rawxyzseg.dat).
        swap_flag: Swap bytes in data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "DTIStudioFibertoSegments",
        "dataset": dataset,
        "swap_flag": swap_flag,
    }
    if output_file is not None:
        params["output_file"] = output_file
    return params


def dtistudio_fiberto_segments_cargs(
    params: DtistudioFibertoSegmentsParameters,
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
    cargs.append("DTIStudioFibertoSegments")
    cargs.append(execution.input_file(params.get("dataset")))
    if params.get("output_file") is not None:
        cargs.extend([
            "-output",
            params.get("output_file")
        ])
    if params.get("swap_flag"):
        cargs.append("-swap")
    return cargs


def dtistudio_fiberto_segments_outputs(
    params: DtistudioFibertoSegmentsParameters,
    execution: Execution,
) -> DtistudioFibertoSegmentsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DtistudioFibertoSegmentsOutputs(
        root=execution.output_file("."),
        output_segment_file=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def dtistudio_fiberto_segments_execute(
    params: DtistudioFibertoSegmentsParameters,
    execution: Execution,
) -> DtistudioFibertoSegmentsOutputs:
    """
    Convert a DTIStudio Fiber file to a SUMA segment file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DtistudioFibertoSegmentsOutputs`).
    """
    params = execution.params(params)
    cargs = dtistudio_fiberto_segments_cargs(params, execution)
    ret = dtistudio_fiberto_segments_outputs(params, execution)
    execution.run(cargs)
    return ret


def dtistudio_fiberto_segments(
    dataset: InputPathType,
    output_file: str | None = None,
    swap_flag: bool = False,
    runner: Runner | None = None,
) -> DtistudioFibertoSegmentsOutputs:
    """
    Convert a DTIStudio Fiber file to a SUMA segment file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset file.
        output_file: Name of the output file (default is rawxyzseg.dat).
        swap_flag: Swap bytes in data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DtistudioFibertoSegmentsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DTISTUDIO_FIBERTO_SEGMENTS_METADATA)
    params = dtistudio_fiberto_segments_params(dataset=dataset, output_file=output_file, swap_flag=swap_flag)
    return dtistudio_fiberto_segments_execute(params, execution)


__all__ = [
    "DTISTUDIO_FIBERTO_SEGMENTS_METADATA",
    "DtistudioFibertoSegmentsOutputs",
    "DtistudioFibertoSegmentsParameters",
    "dtistudio_fiberto_segments",
    "dtistudio_fiberto_segments_params",
]
