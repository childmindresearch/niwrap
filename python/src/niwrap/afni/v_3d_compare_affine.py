# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_COMPARE_AFFINE_METADATA = Metadata(
    id="05a5d8e8f58b82dd3d94b8878f12307d386f682c.boutiques",
    name="3dCompareAffine",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dCompareAffineParameters = typing.TypedDict('V3dCompareAffineParameters', {
    "__STYX_TYPE__": typing.Literal["3dCompareAffine"],
    "mask": typing.NotRequired[str | None],
    "dset": typing.NotRequired[InputPathType | None],
    "affine": typing.NotRequired[list[str] | None],
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
        "3dCompareAffine": v_3d_compare_affine_cargs,
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
        "3dCompareAffine": v_3d_compare_affine_outputs,
    }.get(t)


class V3dCompareAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_compare_affine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing comparison results of affine transformations"""


def v_3d_compare_affine_params(
    mask: str | None = None,
    dset: InputPathType | None = None,
    affine: list[str] | None = None,
) -> V3dCompareAffineParameters:
    """
    Build parameters.
    
    Args:
        mask: Dataset containing non-zero voxels used as the region over which\
            to compare the affine transformations.
        dset: Dataset to compute an automask from it and use that mask as the\
            spatial region for comparison.
        affine: Input an affine transformation (file or 'MATRIX'). Multiple\
            '-affine' options can be used to input multiple files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dCompareAffine",
    }
    if mask is not None:
        params["mask"] = mask
    if dset is not None:
        params["dset"] = dset
    if affine is not None:
        params["affine"] = affine
    return params


def v_3d_compare_affine_cargs(
    params: V3dCompareAffineParameters,
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
    cargs.append("3dCompareAffine")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            params.get("mask")
        ])
    if params.get("dset") is not None:
        cargs.extend([
            "-dset",
            execution.input_file(params.get("dset"))
        ])
    if params.get("affine") is not None:
        cargs.extend([
            "-affine",
            *params.get("affine")
        ])
    return cargs


def v_3d_compare_affine_outputs(
    params: V3dCompareAffineParameters,
    execution: Execution,
) -> V3dCompareAffineOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dCompareAffineOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("[OUTPUT_PREFIX]_comparison.txt"),
    )
    return ret


def v_3d_compare_affine_execute(
    params: V3dCompareAffineParameters,
    execution: Execution,
) -> V3dCompareAffineOutputs:
    """
    Compares two (or more) affine spatial transformations on a dataset and outputs
    measurements of their differences in spatial displacements.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dCompareAffineOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_compare_affine_cargs(params, execution)
    ret = v_3d_compare_affine_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_compare_affine(
    mask: str | None = None,
    dset: InputPathType | None = None,
    affine: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dCompareAffineOutputs:
    """
    Compares two (or more) affine spatial transformations on a dataset and outputs
    measurements of their differences in spatial displacements.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        mask: Dataset containing non-zero voxels used as the region over which\
            to compare the affine transformations.
        dset: Dataset to compute an automask from it and use that mask as the\
            spatial region for comparison.
        affine: Input an affine transformation (file or 'MATRIX'). Multiple\
            '-affine' options can be used to input multiple files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dCompareAffineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_COMPARE_AFFINE_METADATA)
    params = v_3d_compare_affine_params(mask=mask, dset=dset, affine=affine)
    return v_3d_compare_affine_execute(params, execution)


__all__ = [
    "V3dCompareAffineOutputs",
    "V3dCompareAffineParameters",
    "V_3D_COMPARE_AFFINE_METADATA",
    "v_3d_compare_affine",
    "v_3d_compare_affine_params",
]
