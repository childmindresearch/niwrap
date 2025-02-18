# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REG_RESAMPLE_METADATA = Metadata(
    id="2ccb8532ef070b252ef142cb969c94469f490a69.boutiques",
    name="reg_resample",
    package="niftyreg",
    container_image_tag="vnmd/niftyreg_1.4.0:20220819",
)
RegResampleParameters = typing.TypedDict('RegResampleParameters', {
    "__STYX_TYPE__": typing.Literal["reg_resample"],
    "reference_image": InputPathType,
    "floating_image": InputPathType,
    "affine_transform": typing.NotRequired[InputPathType | None],
    "flirt_affine_transform": typing.NotRequired[InputPathType | None],
    "control_point_grid": typing.NotRequired[InputPathType | None],
    "deformation_field": typing.NotRequired[InputPathType | None],
    "resampled_image": typing.NotRequired[str | None],
    "resampled_blank": typing.NotRequired[str | None],
    "nearest_neighbor": bool,
    "linear_interpolation": bool,
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
        "reg_resample": reg_resample_cargs,
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
        "reg_resample": reg_resample_outputs,
    }.get(t)


class RegResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_resampled_image: OutputPathType | None
    """File containing the resampled image"""
    output_resampled_blank: OutputPathType | None
    """File containing the resampled blank grid"""


def reg_resample_params(
    reference_image: InputPathType,
    floating_image: InputPathType,
    affine_transform: InputPathType | None = None,
    flirt_affine_transform: InputPathType | None = None,
    control_point_grid: InputPathType | None = None,
    deformation_field: InputPathType | None = None,
    resampled_image: str | None = None,
    resampled_blank: str | None = None,
    nearest_neighbor: bool = False,
    linear_interpolation: bool = False,
) -> RegResampleParameters:
    """
    Build parameters.
    
    Args:
        reference_image: Filename of the reference image.
        floating_image: Filename of the floating image.
        affine_transform: Filename which contains an affine transformation\
            (Affine*Reference=Floating).
        flirt_affine_transform: Filename which contains a radiological flirt\
            affine transformation.
        control_point_grid: Filename of the control point grid image (from\
            reg_f3d).
        deformation_field: Filename of the deformation field image (from\
            reg_transform).
        resampled_image: Filename of the resampled image.
        resampled_blank: Filename of the resampled blank grid.
        nearest_neighbor: Use a Nearest Neighbor interpolation for the source\
            resampling (cubic spline by default).
        linear_interpolation: Use a Linear interpolation for the source\
            resampling (cubic spline by default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reg_resample",
        "reference_image": reference_image,
        "floating_image": floating_image,
        "nearest_neighbor": nearest_neighbor,
        "linear_interpolation": linear_interpolation,
    }
    if affine_transform is not None:
        params["affine_transform"] = affine_transform
    if flirt_affine_transform is not None:
        params["flirt_affine_transform"] = flirt_affine_transform
    if control_point_grid is not None:
        params["control_point_grid"] = control_point_grid
    if deformation_field is not None:
        params["deformation_field"] = deformation_field
    if resampled_image is not None:
        params["resampled_image"] = resampled_image
    if resampled_blank is not None:
        params["resampled_blank"] = resampled_blank
    return params


def reg_resample_cargs(
    params: RegResampleParameters,
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
    cargs.append("reg_resample")
    cargs.extend([
        "-ref",
        execution.input_file(params.get("reference_image"))
    ])
    cargs.extend([
        "-flo",
        execution.input_file(params.get("floating_image"))
    ])
    if params.get("affine_transform") is not None:
        cargs.extend([
            "-aff",
            execution.input_file(params.get("affine_transform"))
        ])
    if params.get("flirt_affine_transform") is not None:
        cargs.extend([
            "-affFlirt",
            execution.input_file(params.get("flirt_affine_transform"))
        ])
    if params.get("control_point_grid") is not None:
        cargs.extend([
            "-cpp",
            execution.input_file(params.get("control_point_grid"))
        ])
    if params.get("deformation_field") is not None:
        cargs.extend([
            "-def",
            execution.input_file(params.get("deformation_field"))
        ])
    if params.get("resampled_image") is not None:
        cargs.extend([
            "-res",
            params.get("resampled_image")
        ])
    if params.get("resampled_blank") is not None:
        cargs.extend([
            "-blank",
            params.get("resampled_blank")
        ])
    if params.get("nearest_neighbor"):
        cargs.append("-NN")
    if params.get("linear_interpolation"):
        cargs.append("-LIN")
    return cargs


def reg_resample_outputs(
    params: RegResampleParameters,
    execution: Execution,
) -> RegResampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegResampleOutputs(
        root=execution.output_file("."),
        output_resampled_image=execution.output_file(params.get("resampled_image")) if (params.get("resampled_image") is not None) else None,
        output_resampled_blank=execution.output_file(params.get("resampled_blank")) if (params.get("resampled_blank") is not None) else None,
    )
    return ret


def reg_resample_execute(
    params: RegResampleParameters,
    execution: Execution,
) -> RegResampleOutputs:
    """
    Tool for resampling floating images to the reference image space using different
    transformations.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegResampleOutputs`).
    """
    params = execution.params(params)
    cargs = reg_resample_cargs(params, execution)
    ret = reg_resample_outputs(params, execution)
    execution.run(cargs)
    return ret


def reg_resample(
    reference_image: InputPathType,
    floating_image: InputPathType,
    affine_transform: InputPathType | None = None,
    flirt_affine_transform: InputPathType | None = None,
    control_point_grid: InputPathType | None = None,
    deformation_field: InputPathType | None = None,
    resampled_image: str | None = None,
    resampled_blank: str | None = None,
    nearest_neighbor: bool = False,
    linear_interpolation: bool = False,
    runner: Runner | None = None,
) -> RegResampleOutputs:
    """
    Tool for resampling floating images to the reference image space using different
    transformations.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference image.
        floating_image: Filename of the floating image.
        affine_transform: Filename which contains an affine transformation\
            (Affine*Reference=Floating).
        flirt_affine_transform: Filename which contains a radiological flirt\
            affine transformation.
        control_point_grid: Filename of the control point grid image (from\
            reg_f3d).
        deformation_field: Filename of the deformation field image (from\
            reg_transform).
        resampled_image: Filename of the resampled image.
        resampled_blank: Filename of the resampled blank grid.
        nearest_neighbor: Use a Nearest Neighbor interpolation for the source\
            resampling (cubic spline by default).
        linear_interpolation: Use a Linear interpolation for the source\
            resampling (cubic spline by default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_RESAMPLE_METADATA)
    params = reg_resample_params(reference_image=reference_image, floating_image=floating_image, affine_transform=affine_transform, flirt_affine_transform=flirt_affine_transform, control_point_grid=control_point_grid, deformation_field=deformation_field, resampled_image=resampled_image, resampled_blank=resampled_blank, nearest_neighbor=nearest_neighbor, linear_interpolation=linear_interpolation)
    return reg_resample_execute(params, execution)


__all__ = [
    "REG_RESAMPLE_METADATA",
    "RegResampleOutputs",
    "RegResampleParameters",
    "reg_resample",
    "reg_resample_params",
]
