# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_ROIS_FROM_EXTREMA_METADATA = Metadata(
    id="d80d15a560fc4c793db12ebf8002bfc2ce611bb6.boutiques",
    name="cifti-rois-from-extrema",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiRoisFromExtremaGaussianParameters = typing.TypedDict('CiftiRoisFromExtremaGaussianParameters', {
    "__STYX_TYPE__": typing.Literal["gaussian"],
    "surf_sigma": float,
    "vol_sigma": float,
})
CiftiRoisFromExtremaParameters = typing.TypedDict('CiftiRoisFromExtremaParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-rois-from-extrema"],
    "cifti": InputPathType,
    "surf_limit": float,
    "vol_limit": float,
    "direction": str,
    "cifti_out": str,
    "opt_left_surface_surface": typing.NotRequired[InputPathType | None],
    "opt_right_surface_surface": typing.NotRequired[InputPathType | None],
    "opt_cerebellum_surface_surface": typing.NotRequired[InputPathType | None],
    "gaussian": typing.NotRequired[CiftiRoisFromExtremaGaussianParameters | None],
    "opt_overlap_logic_method": typing.NotRequired[str | None],
    "opt_merged_volume": bool,
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
        "cifti-rois-from-extrema": cifti_rois_from_extrema_cargs,
        "gaussian": cifti_rois_from_extrema_gaussian_cargs,
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
        "cifti-rois-from-extrema": cifti_rois_from_extrema_outputs,
    }.get(t)


def cifti_rois_from_extrema_gaussian_params(
    surf_sigma: float,
    vol_sigma: float,
) -> CiftiRoisFromExtremaGaussianParameters:
    """
    Build parameters.
    
    Args:
        surf_sigma: the sigma for the surface gaussian kernel, in mm.
        vol_sigma: the sigma for the volume gaussian kernel, in mm.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gaussian",
        "surf_sigma": surf_sigma,
        "vol_sigma": vol_sigma,
    }
    return params


def cifti_rois_from_extrema_gaussian_cargs(
    params: CiftiRoisFromExtremaGaussianParameters,
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
    cargs.append("-gaussian")
    cargs.append(str(params.get("surf_sigma")))
    cargs.append(str(params.get("vol_sigma")))
    return cargs


class CiftiRoisFromExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_rois_from_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_rois_from_extrema_params(
    cifti: InputPathType,
    surf_limit: float,
    vol_limit: float,
    direction: str,
    cifti_out: str,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    gaussian: CiftiRoisFromExtremaGaussianParameters | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_merged_volume: bool = False,
) -> CiftiRoisFromExtremaParameters:
    """
    Build parameters.
    
    Args:
        cifti: the input cifti.
        surf_limit: geodesic distance limit from vertex, in mm.
        vol_limit: euclidean distance limit from voxel center, in mm.
        direction: which dimension an extrema map is along, ROW or COLUMN.
        cifti_out: the output cifti.
        opt_left_surface_surface: specify the left surface to use: the left\
            surface file.
        opt_right_surface_surface: specify the right surface to use: the right\
            surface file.
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:\
            the cerebellum surface file.
        gaussian: generate gaussian kernels instead of flat ROIs.
        opt_overlap_logic_method: how to handle overlapping ROIs, default\
            ALLOW: the method of resolving overlaps.
        opt_merged_volume: treat volume components as if they were a single\
            component.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-rois-from-extrema",
        "cifti": cifti,
        "surf_limit": surf_limit,
        "vol_limit": vol_limit,
        "direction": direction,
        "cifti_out": cifti_out,
        "opt_merged_volume": opt_merged_volume,
    }
    if opt_left_surface_surface is not None:
        params["opt_left_surface_surface"] = opt_left_surface_surface
    if opt_right_surface_surface is not None:
        params["opt_right_surface_surface"] = opt_right_surface_surface
    if opt_cerebellum_surface_surface is not None:
        params["opt_cerebellum_surface_surface"] = opt_cerebellum_surface_surface
    if gaussian is not None:
        params["gaussian"] = gaussian
    if opt_overlap_logic_method is not None:
        params["opt_overlap_logic_method"] = opt_overlap_logic_method
    return params


def cifti_rois_from_extrema_cargs(
    params: CiftiRoisFromExtremaParameters,
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
    cargs.append("wb_command")
    cargs.append("-cifti-rois-from-extrema")
    cargs.append(execution.input_file(params.get("cifti")))
    cargs.append(str(params.get("surf_limit")))
    cargs.append(str(params.get("vol_limit")))
    cargs.append(params.get("direction"))
    cargs.append(params.get("cifti_out"))
    if params.get("opt_left_surface_surface") is not None:
        cargs.extend([
            "-left-surface",
            execution.input_file(params.get("opt_left_surface_surface"))
        ])
    if params.get("opt_right_surface_surface") is not None:
        cargs.extend([
            "-right-surface",
            execution.input_file(params.get("opt_right_surface_surface"))
        ])
    if params.get("opt_cerebellum_surface_surface") is not None:
        cargs.extend([
            "-cerebellum-surface",
            execution.input_file(params.get("opt_cerebellum_surface_surface"))
        ])
    if params.get("gaussian") is not None:
        cargs.extend(dyn_cargs(params.get("gaussian")["__STYXTYPE__"])(params.get("gaussian"), execution))
    if params.get("opt_overlap_logic_method") is not None:
        cargs.extend([
            "-overlap-logic",
            params.get("opt_overlap_logic_method")
        ])
    if params.get("opt_merged_volume"):
        cargs.append("-merged-volume")
    return cargs


def cifti_rois_from_extrema_outputs(
    params: CiftiRoisFromExtremaParameters,
    execution: Execution,
) -> CiftiRoisFromExtremaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiRoisFromExtremaOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_rois_from_extrema_execute(
    params: CiftiRoisFromExtremaParameters,
    execution: Execution,
) -> CiftiRoisFromExtremaOutputs:
    """
    Create cifti roi maps from extrema maps.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiRoisFromExtremaOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_rois_from_extrema_cargs(params, execution)
    ret = cifti_rois_from_extrema_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_rois_from_extrema(
    cifti: InputPathType,
    surf_limit: float,
    vol_limit: float,
    direction: str,
    cifti_out: str,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    gaussian: CiftiRoisFromExtremaGaussianParameters | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_merged_volume: bool = False,
    runner: Runner | None = None,
) -> CiftiRoisFromExtremaOutputs:
    """
    Create cifti roi maps from extrema maps.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti: the input cifti.
        surf_limit: geodesic distance limit from vertex, in mm.
        vol_limit: euclidean distance limit from voxel center, in mm.
        direction: which dimension an extrema map is along, ROW or COLUMN.
        cifti_out: the output cifti.
        opt_left_surface_surface: specify the left surface to use: the left\
            surface file.
        opt_right_surface_surface: specify the right surface to use: the right\
            surface file.
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:\
            the cerebellum surface file.
        gaussian: generate gaussian kernels instead of flat ROIs.
        opt_overlap_logic_method: how to handle overlapping ROIs, default\
            ALLOW: the method of resolving overlaps.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiRoisFromExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ROIS_FROM_EXTREMA_METADATA)
    params = cifti_rois_from_extrema_params(cifti=cifti, surf_limit=surf_limit, vol_limit=vol_limit, direction=direction, cifti_out=cifti_out, opt_left_surface_surface=opt_left_surface_surface, opt_right_surface_surface=opt_right_surface_surface, opt_cerebellum_surface_surface=opt_cerebellum_surface_surface, gaussian=gaussian, opt_overlap_logic_method=opt_overlap_logic_method, opt_merged_volume=opt_merged_volume)
    return cifti_rois_from_extrema_execute(params, execution)


__all__ = [
    "CIFTI_ROIS_FROM_EXTREMA_METADATA",
    "CiftiRoisFromExtremaGaussianParameters",
    "CiftiRoisFromExtremaOutputs",
    "CiftiRoisFromExtremaParameters",
    "cifti_rois_from_extrema",
    "cifti_rois_from_extrema_gaussian_params",
    "cifti_rois_from_extrema_params",
]
