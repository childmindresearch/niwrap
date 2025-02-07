# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_REFINE_SEG_METADATA = Metadata(
    id="cb7729fa49160d260ecc58552917a2760053175e.boutiques",
    name="mri_refine_seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriRefineSegParameters = typing.TypedDict('MriRefineSegParameters', {
    "__STYX_TYPE__": typing.Literal["mri_refine_seg"],
    "input_segmentation": InputPathType,
    "output_segmentation": str,
    "debug": bool,
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
        "mri_refine_seg": mri_refine_seg_cargs,
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
        "mri_refine_seg": mri_refine_seg_outputs,
    }.get(t)


class MriRefineSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_refine_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    refined_output: OutputPathType
    """Refined segmentation output file."""


def mri_refine_seg_params(
    input_segmentation: InputPathType,
    output_segmentation: str,
    debug: bool = False,
) -> MriRefineSegParameters:
    """
    Build parameters.
    
    Args:
        input_segmentation: Input segmentation file.
        output_segmentation: Refined segmentation output name.
        debug: Save the original segmentation, a mask of the refined voxels,\
            and a pointset of the refined clusters to the output directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_refine_seg",
        "input_segmentation": input_segmentation,
        "output_segmentation": output_segmentation,
        "debug": debug,
    }
    return params


def mri_refine_seg_cargs(
    params: MriRefineSegParameters,
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
    cargs.append("mri_refine_seg")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_segmentation"))
    ])
    cargs.extend([
        "-o",
        params.get("output_segmentation")
    ])
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def mri_refine_seg_outputs(
    params: MriRefineSegParameters,
    execution: Execution,
) -> MriRefineSegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriRefineSegOutputs(
        root=execution.output_file("."),
        refined_output=execution.output_file(params.get("output_segmentation")),
    )
    return ret


def mri_refine_seg_execute(
    params: MriRefineSegParameters,
    execution: Execution,
) -> MriRefineSegOutputs:
    """
    Refines a messy segmentation by recoding stray voxels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriRefineSegOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_refine_seg_cargs(params, execution)
    ret = mri_refine_seg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_refine_seg(
    input_segmentation: InputPathType,
    output_segmentation: str,
    debug: bool = False,
    runner: Runner | None = None,
) -> MriRefineSegOutputs:
    """
    Refines a messy segmentation by recoding stray voxels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_segmentation: Input segmentation file.
        output_segmentation: Refined segmentation output name.
        debug: Save the original segmentation, a mask of the refined voxels,\
            and a pointset of the refined clusters to the output directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRefineSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_REFINE_SEG_METADATA)
    params = mri_refine_seg_params(input_segmentation=input_segmentation, output_segmentation=output_segmentation, debug=debug)
    return mri_refine_seg_execute(params, execution)


__all__ = [
    "MRI_REFINE_SEG_METADATA",
    "MriRefineSegOutputs",
    "MriRefineSegParameters",
    "mri_refine_seg",
    "mri_refine_seg_params",
]
