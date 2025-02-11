# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TWOTO_COMPLEX_METADATA = Metadata(
    id="bf9493b3c937b76d0584de14a9b270a71cce9ca0.boutiques",
    name="3dTwotoComplex",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dTwotoComplexParameters = typing.TypedDict('V3dTwotoComplexParameters', {
    "__STYX_TYPE__": typing.Literal["3dTwotoComplex"],
    "dataset1": InputPathType,
    "dataset2": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "ri": bool,
    "mp": bool,
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
        "3dTwotoComplex": v_3d_twoto_complex_cargs,
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
        "3dTwotoComplex": v_3d_twoto_complex_outputs,
    }.get(t)


class V3dTwotoComplexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_twoto_complex(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_brick: OutputPathType | None
    """Output complex-valued dataset with prefix"""
    out_head: OutputPathType | None
    """Header for the complex-valued dataset"""


def v_3d_twoto_complex_params(
    dataset1: InputPathType,
    dataset2: InputPathType | None = None,
    prefix: str | None = None,
    ri: bool = False,
    mp: bool = False,
    mask: InputPathType | None = None,
) -> V3dTwotoComplexParameters:
    """
    Build parameters.
    
    Args:
        dataset1: Input dataset (either as 1 dataset with 2 sub-bricks or 2\
            separate datasets).
        dataset2: Second input dataset (optional if 2 sub-bricks in the first\
            dataset).
        prefix: Prefix for the output dataset [default='cmplx'].
        ri: Specify that the 2 inputs are real and imaginary parts [this is the\
            default].
        mp: Specify that the 2 inputs are magnitude and phase [phase is in\
            radians].
        mask: Only output nonzero values where the mask dataset is nonzero.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTwotoComplex",
        "dataset1": dataset1,
        "ri": ri,
        "mp": mp,
    }
    if dataset2 is not None:
        params["dataset2"] = dataset2
    if prefix is not None:
        params["prefix"] = prefix
    if mask is not None:
        params["mask"] = mask
    return params


def v_3d_twoto_complex_cargs(
    params: V3dTwotoComplexParameters,
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
    cargs.append("3dTwotoComplex")
    cargs.append(execution.input_file(params.get("dataset1")))
    if params.get("dataset2") is not None:
        cargs.append(execution.input_file(params.get("dataset2")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("ri"):
        cargs.append("-RI")
    if params.get("mp"):
        cargs.append("-MP")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    return cargs


def v_3d_twoto_complex_outputs(
    params: V3dTwotoComplexParameters,
    execution: Execution,
) -> V3dTwotoComplexOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTwotoComplexOutputs(
        root=execution.output_file("."),
        out_brick=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
        out_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_twoto_complex_execute(
    params: V3dTwotoComplexParameters,
    execution: Execution,
) -> V3dTwotoComplexOutputs:
    """
    Converts 2 sub-bricks of input to a complex-valued dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTwotoComplexOutputs`).
    """
    cargs = v_3d_twoto_complex_cargs(params, execution)
    ret = v_3d_twoto_complex_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_twoto_complex(
    dataset1: InputPathType,
    dataset2: InputPathType | None = None,
    prefix: str | None = None,
    ri: bool = False,
    mp: bool = False,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dTwotoComplexOutputs:
    """
    Converts 2 sub-bricks of input to a complex-valued dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset1: Input dataset (either as 1 dataset with 2 sub-bricks or 2\
            separate datasets).
        dataset2: Second input dataset (optional if 2 sub-bricks in the first\
            dataset).
        prefix: Prefix for the output dataset [default='cmplx'].
        ri: Specify that the 2 inputs are real and imaginary parts [this is the\
            default].
        mp: Specify that the 2 inputs are magnitude and phase [phase is in\
            radians].
        mask: Only output nonzero values where the mask dataset is nonzero.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTwotoComplexOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TWOTO_COMPLEX_METADATA)
    params = v_3d_twoto_complex_params(dataset1=dataset1, dataset2=dataset2, prefix=prefix, ri=ri, mp=mp, mask=mask)
    return v_3d_twoto_complex_execute(params, execution)


__all__ = [
    "V3dTwotoComplexOutputs",
    "V3dTwotoComplexParameters",
    "V_3D_TWOTO_COMPLEX_METADATA",
    "v_3d_twoto_complex",
    "v_3d_twoto_complex_params",
]
