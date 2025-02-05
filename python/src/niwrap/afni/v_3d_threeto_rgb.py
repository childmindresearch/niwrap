# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_THREETO_RGB_METADATA = Metadata(
    id="0e50efb1e4d4adac2b47669f62f58516c895a1cf.boutiques",
    name="3dThreetoRGB",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dThreetoRgbParameters = typing.TypedDict('V3dThreetoRgbParameters', {
    "__STYX_TYPE__": typing.Literal["3dThreetoRGB"],
    "output_prefix": typing.NotRequired[str | None],
    "scale_factor": typing.NotRequired[float | None],
    "mask_dataset": typing.NotRequired[InputPathType | None],
    "fim": bool,
    "anat": bool,
    "input_dataset": InputPathType,
    "input_dataset2": typing.NotRequired[InputPathType | None],
    "input_dataset3": typing.NotRequired[InputPathType | None],
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
        "3dThreetoRGB": v_3d_threeto_rgb_cargs,
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
        "3dThreetoRGB": v_3d_threeto_rgb_outputs,
    }
    return vt.get(t)


class V3dThreetoRgbOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_threeto_rgb(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_head: OutputPathType | None
    """RGB-valued dataset output"""
    output_dataset_brik: OutputPathType | None
    """RGB-valued dataset output"""


def v_3d_threeto_rgb_params(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    scale_factor: float | None = None,
    mask_dataset: InputPathType | None = None,
    fim: bool = False,
    anat: bool = False,
    input_dataset2: InputPathType | None = None,
    input_dataset3: InputPathType | None = None,
) -> V3dThreetoRgbParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset or first dataset if three datasets are\
            provided.
        output_prefix: Write output into dataset with specified prefix.
        scale_factor: Multiply input values by this factor before using as RGB.
        mask_dataset: Only output nonzero values where the mask dataset is\
            nonzero.
        fim: Write result as a 'fim' type dataset (default behavior).
        anat: Write result as a anatomical type dataset.
        input_dataset2: Second dataset, required only if three datasets are\
            provided.
        input_dataset3: Third dataset, required only if three datasets are\
            provided.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dThreetoRGB",
        "fim": fim,
        "anat": anat,
        "input_dataset": input_dataset,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if scale_factor is not None:
        params["scale_factor"] = scale_factor
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    if input_dataset2 is not None:
        params["input_dataset2"] = input_dataset2
    if input_dataset3 is not None:
        params["input_dataset3"] = input_dataset3
    return params


def v_3d_threeto_rgb_cargs(
    params: V3dThreetoRgbParameters,
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
    cargs.append("3dThreetoRGB")
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("scale_factor") is not None:
        cargs.extend([
            "-scale",
            str(params.get("scale_factor"))
        ])
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dataset"))
        ])
    if params.get("fim"):
        cargs.append("-fim")
    if params.get("anat"):
        cargs.append("-anat")
    cargs.append(execution.input_file(params.get("input_dataset")))
    cargs.append("[DATASET1]")
    if params.get("input_dataset2") is not None:
        cargs.append(execution.input_file(params.get("input_dataset2")))
    if params.get("input_dataset3") is not None:
        cargs.append(execution.input_file(params.get("input_dataset3")))
    return cargs


def v_3d_threeto_rgb_outputs(
    params: V3dThreetoRgbParameters,
    execution: Execution,
) -> V3dThreetoRgbOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dThreetoRgbOutputs(
        root=execution.output_file("."),
        output_dataset_head=execution.output_file(params.get("output_prefix") + "+rgb.HEAD") if (params.get("output_prefix") is not None) else None,
        output_dataset_brik=execution.output_file(params.get("output_prefix") + "+rgb.BRIK") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_threeto_rgb_execute(
    params: V3dThreetoRgbParameters,
    execution: Execution,
) -> V3dThreetoRgbOutputs:
    """
    Converts 3 sub-bricks of input to an RGB-valued dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dThreetoRgbOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_threeto_rgb_cargs(params, execution)
    ret = v_3d_threeto_rgb_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_threeto_rgb(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    scale_factor: float | None = None,
    mask_dataset: InputPathType | None = None,
    fim: bool = False,
    anat: bool = False,
    input_dataset2: InputPathType | None = None,
    input_dataset3: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dThreetoRgbOutputs:
    """
    Converts 3 sub-bricks of input to an RGB-valued dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset or first dataset if three datasets are\
            provided.
        output_prefix: Write output into dataset with specified prefix.
        scale_factor: Multiply input values by this factor before using as RGB.
        mask_dataset: Only output nonzero values where the mask dataset is\
            nonzero.
        fim: Write result as a 'fim' type dataset (default behavior).
        anat: Write result as a anatomical type dataset.
        input_dataset2: Second dataset, required only if three datasets are\
            provided.
        input_dataset3: Third dataset, required only if three datasets are\
            provided.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dThreetoRgbOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_THREETO_RGB_METADATA)
    params = v_3d_threeto_rgb_params(output_prefix=output_prefix, scale_factor=scale_factor, mask_dataset=mask_dataset, fim=fim, anat=anat, input_dataset=input_dataset, input_dataset2=input_dataset2, input_dataset3=input_dataset3)
    return v_3d_threeto_rgb_execute(params, execution)


__all__ = [
    "V3dThreetoRgbOutputs",
    "V3dThreetoRgbParameters",
    "V_3D_THREETO_RGB_METADATA",
    "v_3d_threeto_rgb",
    "v_3d_threeto_rgb_params",
]
