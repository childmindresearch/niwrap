# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ZCUTUP_METADATA = Metadata(
    id="9f4c5ae0e2d25b35b3ce4085901c813b8cd03916.boutiques",
    name="3dZcutup",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dZcutupParameters = typing.TypedDict('V3dZcutupParameters', {
    "__STYX_TYPE__": typing.Literal["3dZcutup"],
    "keep_slices": str,
    "prefix": typing.NotRequired[str | None],
    "dataset": InputPathType,
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
        "3dZcutup": v_3d_zcutup_cargs,
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
        "3dZcutup": v_3d_zcutup_outputs,
    }.get(t)


class V3dZcutupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zcutup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType | None
    """The output dataset HEAD file"""
    output_brik: OutputPathType | None
    """The output dataset BRIK file"""


def v_3d_zcutup_params(
    keep_slices: str,
    dataset: InputPathType,
    prefix: str | None = None,
) -> V3dZcutupParameters:
    """
    Build parameters.
    
    Args:
        keep_slices: Keep slices numbered 'b' through 't', inclusive. This is a\
            mandatory option. Slice numbers start at 0.
        dataset: The input dataset (e.g., epi07+orig). You can use a sub-brick\
            selector on the input dataset.
        prefix: Write result into dataset with the given prefix [default =\
            'zcutup'].
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dZcutup",
        "keep_slices": keep_slices,
        "dataset": dataset,
    }
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_zcutup_cargs(
    params: V3dZcutupParameters,
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
    cargs.append("3dZcutup")
    cargs.extend([
        "-keep",
        params.get("keep_slices")
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3d_zcutup_outputs(
    params: V3dZcutupParameters,
    execution: Execution,
) -> V3dZcutupOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dZcutupOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
        output_brik=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_zcutup_execute(
    params: V3dZcutupParameters,
    execution: Execution,
) -> V3dZcutupOutputs:
    """
    Cut slices off a dataset in its z-direction and write a new dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dZcutupOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_zcutup_cargs(params, execution)
    ret = v_3d_zcutup_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_zcutup(
    keep_slices: str,
    dataset: InputPathType,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dZcutupOutputs:
    """
    Cut slices off a dataset in its z-direction and write a new dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        keep_slices: Keep slices numbered 'b' through 't', inclusive. This is a\
            mandatory option. Slice numbers start at 0.
        dataset: The input dataset (e.g., epi07+orig). You can use a sub-brick\
            selector on the input dataset.
        prefix: Write result into dataset with the given prefix [default =\
            'zcutup'].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZcutupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZCUTUP_METADATA)
    params = v_3d_zcutup_params(keep_slices=keep_slices, prefix=prefix, dataset=dataset)
    return v_3d_zcutup_execute(params, execution)


__all__ = [
    "V3dZcutupOutputs",
    "V3dZcutupParameters",
    "V_3D_ZCUTUP_METADATA",
    "v_3d_zcutup",
    "v_3d_zcutup_params",
]
