# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_LINEAR_ALIGN_METADATA = Metadata(
    id="e21ce25c91e684ff7b180749c2270d4bd42ef69b.boutiques",
    name="mri_linear_align",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriLinearAlignParameters = typing.TypedDict('MriLinearAlignParameters', {
    "__STYX_TYPE__": typing.Literal["mri_linear_align"],
    "source": InputPathType,
    "target": InputPathType,
    "output_xform": str,
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
        "mri_linear_align": mri_linear_align_cargs,
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
        "mri_linear_align": mri_linear_align_outputs,
    }.get(t)


class MriLinearAlignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_linear_align(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_linear_align_params(
    source: InputPathType,
    target: InputPathType,
    output_xform: str,
) -> MriLinearAlignParameters:
    """
    Build parameters.
    
    Args:
        source: Source image file for alignment.
        target: Target image file for alignment.
        output_xform: Output transformation file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_linear_align",
        "source": source,
        "target": target,
        "output_xform": output_xform,
    }
    return params


def mri_linear_align_cargs(
    params: MriLinearAlignParameters,
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
    cargs.append("mri_linear_align")
    cargs.append(execution.input_file(params.get("source")))
    cargs.append(execution.input_file(params.get("target")))
    cargs.append(params.get("output_xform"))
    return cargs


def mri_linear_align_outputs(
    params: MriLinearAlignParameters,
    execution: Execution,
) -> MriLinearAlignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriLinearAlignOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_linear_align_execute(
    params: MriLinearAlignParameters,
    execution: Execution,
) -> MriLinearAlignOutputs:
    """
    MRI Linear Alignment Tool for Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriLinearAlignOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_linear_align_cargs(params, execution)
    ret = mri_linear_align_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_linear_align(
    source: InputPathType,
    target: InputPathType,
    output_xform: str,
    runner: Runner | None = None,
) -> MriLinearAlignOutputs:
    """
    MRI Linear Alignment Tool for Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source: Source image file for alignment.
        target: Target image file for alignment.
        output_xform: Output transformation file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriLinearAlignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_LINEAR_ALIGN_METADATA)
    params = mri_linear_align_params(source=source, target=target, output_xform=output_xform)
    return mri_linear_align_execute(params, execution)


__all__ = [
    "MRI_LINEAR_ALIGN_METADATA",
    "MriLinearAlignOutputs",
    "MriLinearAlignParameters",
    "mri_linear_align",
    "mri_linear_align_params",
]
