# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MERGESEG_METADATA = Metadata(
    id="e04b3424de0fa2092fe3065091e43e9ee626b75c.boutiques",
    name="mergeseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MergesegParameters = typing.TypedDict('MergesegParameters', {
    "__STYX_TYPE__": typing.Literal["mergeseg"],
    "src_seg": InputPathType,
    "merge_seg": InputPathType,
    "out_seg": str,
    "segid": typing.NotRequired[float | None],
    "segid_only": typing.NotRequired[float | None],
    "segid_erode": typing.NotRequired[float | None],
    "ctab": typing.NotRequired[InputPathType | None],
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
        "mergeseg": mergeseg_cargs,
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
        "mergeseg": mergeseg_outputs,
    }.get(t)


class MergesegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mergeseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_seg: OutputPathType
    """Output merged segmentation result."""


def mergeseg_params(
    src_seg: InputPathType,
    merge_seg: InputPathType,
    out_seg: str,
    segid: float | None = None,
    segid_only: float | None = None,
    segid_erode: float | None = None,
    ctab: InputPathType | None = None,
) -> MergesegParameters:
    """
    Build parameters.
    
    Args:
        src_seg: Source segmentation image file.
        merge_seg: Merge segmentation volume file.
        out_seg: Output merged segmentation.
        segid: Segmentation index (optional). If specified, all the voxels in\
            the merge seg will be set to segindex.
        segid_only: Only take segindex from merge and use it for merging.
        segid_erode: Erode seg-only segindex before merge. Specify the number\
            of erosion iterations.
        ctab: Color table to embed in the output segmentation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mergeseg",
        "src_seg": src_seg,
        "merge_seg": merge_seg,
        "out_seg": out_seg,
    }
    if segid is not None:
        params["segid"] = segid
    if segid_only is not None:
        params["segid_only"] = segid_only
    if segid_erode is not None:
        params["segid_erode"] = segid_erode
    if ctab is not None:
        params["ctab"] = ctab
    return params


def mergeseg_cargs(
    params: MergesegParameters,
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
    cargs.append("mergeseg")
    cargs.append(execution.input_file(params.get("src_seg")))
    cargs.append(execution.input_file(params.get("merge_seg")))
    cargs.extend([
        "--o",
        params.get("out_seg")
    ])
    if params.get("segid") is not None:
        cargs.extend([
            "--segid",
            str(params.get("segid"))
        ])
    if params.get("segid_only") is not None:
        cargs.extend([
            "--segid-only",
            str(params.get("segid_only"))
        ])
    if params.get("segid_erode") is not None:
        cargs.extend([
            "--segid-erode",
            str(params.get("segid_erode"))
        ])
    if params.get("ctab") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("ctab"))
        ])
    return cargs


def mergeseg_outputs(
    params: MergesegParameters,
    execution: Execution,
) -> MergesegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MergesegOutputs(
        root=execution.output_file("."),
        output_seg=execution.output_file(params.get("out_seg")),
    )
    return ret


def mergeseg_execute(
    params: MergesegParameters,
    execution: Execution,
) -> MergesegOutputs:
    """
    Merges one segmentation into another, replacing the source voxels with those
    from the merge segmentation where non-zero.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MergesegOutputs`).
    """
    params = execution.params(params)
    cargs = mergeseg_cargs(params, execution)
    ret = mergeseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mergeseg(
    src_seg: InputPathType,
    merge_seg: InputPathType,
    out_seg: str,
    segid: float | None = None,
    segid_only: float | None = None,
    segid_erode: float | None = None,
    ctab: InputPathType | None = None,
    runner: Runner | None = None,
) -> MergesegOutputs:
    """
    Merges one segmentation into another, replacing the source voxels with those
    from the merge segmentation where non-zero.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_seg: Source segmentation image file.
        merge_seg: Merge segmentation volume file.
        out_seg: Output merged segmentation.
        segid: Segmentation index (optional). If specified, all the voxels in\
            the merge seg will be set to segindex.
        segid_only: Only take segindex from merge and use it for merging.
        segid_erode: Erode seg-only segindex before merge. Specify the number\
            of erosion iterations.
        ctab: Color table to embed in the output segmentation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MergesegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MERGESEG_METADATA)
    params = mergeseg_params(src_seg=src_seg, merge_seg=merge_seg, out_seg=out_seg, segid=segid, segid_only=segid_only, segid_erode=segid_erode, ctab=ctab)
    return mergeseg_execute(params, execution)


__all__ = [
    "MERGESEG_METADATA",
    "MergesegOutputs",
    "MergesegParameters",
    "mergeseg",
    "mergeseg_params",
]
