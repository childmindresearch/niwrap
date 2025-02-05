# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STANDARD_SPACE_ROI_METADATA = Metadata(
    id="cc061c48c2d12a1afe15a890d8f2cfe7638fd047.boutiques",
    name="standard_space_roi",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
StandardSpaceRoiParameters = typing.TypedDict('StandardSpaceRoiParameters', {
    "__STYX_TYPE__": typing.Literal["standard_space_roi"],
    "infile": InputPathType,
    "outfile": str,
    "mask_fov_flag": bool,
    "mask_mask": typing.NotRequired[InputPathType | None],
    "mask_none_flag": bool,
    "roi_fov_flag": bool,
    "roi_mask": typing.NotRequired[InputPathType | None],
    "roi_none_flag": bool,
    "ss_ref": typing.NotRequired[InputPathType | None],
    "alt_input": typing.NotRequired[InputPathType | None],
    "debug_flag": bool,
    "bet_premask_flag": bool,
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
        "standard_space_roi": standard_space_roi_cargs,
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
        "standard_space_roi": standard_space_roi_outputs,
    }
    return vt.get(t)


class StandardSpaceRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `standard_space_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_image: OutputPathType
    """Output image after masking and/or FOV reduction"""


def standard_space_roi_params(
    infile: InputPathType,
    outfile: str,
    mask_fov_flag: bool = False,
    mask_mask: InputPathType | None = None,
    mask_none_flag: bool = False,
    roi_fov_flag: bool = False,
    roi_mask: InputPathType | None = None,
    roi_none_flag: bool = False,
    ss_ref: InputPathType | None = None,
    alt_input: InputPathType | None = None,
    debug_flag: bool = False,
    bet_premask_flag: bool = False,
) -> StandardSpaceRoiParameters:
    """
    Build parameters.
    
    Args:
        infile: Input image.
        outfile: Output image.
        mask_fov_flag: Mask output using transformed standard space FOV.
        mask_mask: Mask output using transformed standard space mask.
        mask_none_flag: Do not mask output.
        roi_fov_flag: Cut down input FOV using bounding box of the transformed\
            standard space FOV.
        roi_mask: Cut down input FOV using nonbackground bounding box of the\
            transformed standard space mask.
        roi_none_flag: Do not cut down input FOV.
        ss_ref: Standard space reference image to use (default:\
            /usr/local/fsl/data/standard/MNI152_T1).
        alt_input: Alternative input image to apply the ROI to (instead of the\
            one used to register to the reference).
        debug_flag: Debug mode (don't delete intermediate files).
        bet_premask_flag: Equivalent to: -maskMASK\
            /usr/local/fsl/data/standard/MNI152_T1_2mm_brain_mask_dil -roiNONE.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "standard_space_roi",
        "infile": infile,
        "outfile": outfile,
        "mask_fov_flag": mask_fov_flag,
        "mask_none_flag": mask_none_flag,
        "roi_fov_flag": roi_fov_flag,
        "roi_none_flag": roi_none_flag,
        "debug_flag": debug_flag,
        "bet_premask_flag": bet_premask_flag,
    }
    if mask_mask is not None:
        params["mask_mask"] = mask_mask
    if roi_mask is not None:
        params["roi_mask"] = roi_mask
    if ss_ref is not None:
        params["ss_ref"] = ss_ref
    if alt_input is not None:
        params["alt_input"] = alt_input
    return params


def standard_space_roi_cargs(
    params: StandardSpaceRoiParameters,
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
    cargs.append("standard_space_roi")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(params.get("outfile"))
    if params.get("mask_fov_flag"):
        cargs.append("-maskFOV")
    if params.get("mask_mask") is not None:
        cargs.extend([
            "-maskMASK",
            execution.input_file(params.get("mask_mask"))
        ])
    if params.get("mask_none_flag"):
        cargs.append("-maskNONE")
    if params.get("roi_fov_flag"):
        cargs.append("-roiFOV")
    if params.get("roi_mask") is not None:
        cargs.extend([
            "-roiMASK",
            execution.input_file(params.get("roi_mask"))
        ])
    if params.get("roi_none_flag"):
        cargs.append("-roiNONE")
    if params.get("ss_ref") is not None:
        cargs.extend([
            "-ssref",
            execution.input_file(params.get("ss_ref"))
        ])
    if params.get("alt_input") is not None:
        cargs.extend([
            "-altinput",
            execution.input_file(params.get("alt_input"))
        ])
    if params.get("debug_flag"):
        cargs.append("-d")
    if params.get("bet_premask_flag"):
        cargs.append("-b")
    return cargs


def standard_space_roi_outputs(
    params: StandardSpaceRoiParameters,
    execution: Execution,
) -> StandardSpaceRoiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = StandardSpaceRoiOutputs(
        root=execution.output_file("."),
        out_image=execution.output_file(params.get("outfile")),
    )
    return ret


def standard_space_roi_execute(
    params: StandardSpaceRoiParameters,
    execution: Execution,
) -> StandardSpaceRoiOutputs:
    """
    Masks input and/or reduces its FOV based on a standard space image or mask,
    transformed into the space of the input image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `StandardSpaceRoiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = standard_space_roi_cargs(params, execution)
    ret = standard_space_roi_outputs(params, execution)
    execution.run(cargs)
    return ret


def standard_space_roi(
    infile: InputPathType,
    outfile: str,
    mask_fov_flag: bool = False,
    mask_mask: InputPathType | None = None,
    mask_none_flag: bool = False,
    roi_fov_flag: bool = False,
    roi_mask: InputPathType | None = None,
    roi_none_flag: bool = False,
    ss_ref: InputPathType | None = None,
    alt_input: InputPathType | None = None,
    debug_flag: bool = False,
    bet_premask_flag: bool = False,
    runner: Runner | None = None,
) -> StandardSpaceRoiOutputs:
    """
    Masks input and/or reduces its FOV based on a standard space image or mask,
    transformed into the space of the input image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input image.
        outfile: Output image.
        mask_fov_flag: Mask output using transformed standard space FOV.
        mask_mask: Mask output using transformed standard space mask.
        mask_none_flag: Do not mask output.
        roi_fov_flag: Cut down input FOV using bounding box of the transformed\
            standard space FOV.
        roi_mask: Cut down input FOV using nonbackground bounding box of the\
            transformed standard space mask.
        roi_none_flag: Do not cut down input FOV.
        ss_ref: Standard space reference image to use (default:\
            /usr/local/fsl/data/standard/MNI152_T1).
        alt_input: Alternative input image to apply the ROI to (instead of the\
            one used to register to the reference).
        debug_flag: Debug mode (don't delete intermediate files).
        bet_premask_flag: Equivalent to: -maskMASK\
            /usr/local/fsl/data/standard/MNI152_T1_2mm_brain_mask_dil -roiNONE.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StandardSpaceRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STANDARD_SPACE_ROI_METADATA)
    params = standard_space_roi_params(infile=infile, outfile=outfile, mask_fov_flag=mask_fov_flag, mask_mask=mask_mask, mask_none_flag=mask_none_flag, roi_fov_flag=roi_fov_flag, roi_mask=roi_mask, roi_none_flag=roi_none_flag, ss_ref=ss_ref, alt_input=alt_input, debug_flag=debug_flag, bet_premask_flag=bet_premask_flag)
    return standard_space_roi_execute(params, execution)


__all__ = [
    "STANDARD_SPACE_ROI_METADATA",
    "StandardSpaceRoiOutputs",
    "StandardSpaceRoiParameters",
    "standard_space_roi",
    "standard_space_roi_params",
]
