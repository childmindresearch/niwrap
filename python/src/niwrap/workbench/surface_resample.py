# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_RESAMPLE_METADATA = Metadata(
    id="d969759c0a9b6cf50715a3f792dc5b6638eb9982.boutiques",
    name="surface-resample",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceResampleAreaSurfsParameters = typing.TypedDict('SurfaceResampleAreaSurfsParameters', {
    "__STYX_TYPE__": typing.Literal["area_surfs"],
    "current_area": InputPathType,
    "new_area": InputPathType,
})
SurfaceResampleAreaMetricsParameters = typing.TypedDict('SurfaceResampleAreaMetricsParameters', {
    "__STYX_TYPE__": typing.Literal["area_metrics"],
    "current_area": InputPathType,
    "new_area": InputPathType,
})
SurfaceResampleParameters = typing.TypedDict('SurfaceResampleParameters', {
    "__STYX_TYPE__": typing.Literal["surface-resample"],
    "surface_in": InputPathType,
    "current_sphere": InputPathType,
    "new_sphere": InputPathType,
    "method": str,
    "surface_out": str,
    "area_surfs": typing.NotRequired[SurfaceResampleAreaSurfsParameters | None],
    "area_metrics": typing.NotRequired[SurfaceResampleAreaMetricsParameters | None],
    "opt_bypass_sphere_check": bool,
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
        "surface-resample": surface_resample_cargs,
        "area_surfs": surface_resample_area_surfs_cargs,
        "area_metrics": surface_resample_area_metrics_cargs,
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
        "surface-resample": surface_resample_outputs,
    }.get(t)


def surface_resample_area_surfs_params(
    current_area: InputPathType,
    new_area: InputPathType,
) -> SurfaceResampleAreaSurfsParameters:
    """
    Build parameters.
    
    Args:
        current_area: a relevant surface with <current-sphere> mesh.
        new_area: a relevant surface with <new-sphere> mesh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "area_surfs",
        "current_area": current_area,
        "new_area": new_area,
    }
    return params


def surface_resample_area_surfs_cargs(
    params: SurfaceResampleAreaSurfsParameters,
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
    cargs.append("-area-surfs")
    cargs.append(execution.input_file(params.get("current_area")))
    cargs.append(execution.input_file(params.get("new_area")))
    return cargs


def surface_resample_area_metrics_params(
    current_area: InputPathType,
    new_area: InputPathType,
) -> SurfaceResampleAreaMetricsParameters:
    """
    Build parameters.
    
    Args:
        current_area: a metric file with vertex areas for <current-sphere> mesh.
        new_area: a metric file with vertex areas for <new-sphere> mesh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "area_metrics",
        "current_area": current_area,
        "new_area": new_area,
    }
    return params


def surface_resample_area_metrics_cargs(
    params: SurfaceResampleAreaMetricsParameters,
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
    cargs.append("-area-metrics")
    cargs.append(execution.input_file(params.get("current_area")))
    cargs.append(execution.input_file(params.get("new_area")))
    return cargs


class SurfaceResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output surface file"""


def surface_resample_params(
    surface_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    method: str,
    surface_out: str,
    area_surfs: SurfaceResampleAreaSurfsParameters | None = None,
    area_metrics: SurfaceResampleAreaMetricsParameters | None = None,
    opt_bypass_sphere_check: bool = False,
) -> SurfaceResampleParameters:
    """
    Build parameters.
    
    Args:
        surface_in: the surface file to resample.
        current_sphere: a sphere surface with the mesh that the input surface\
            is currently on.
        new_sphere: a sphere surface that is in register with <current-sphere>\
            and has the desired output mesh.
        method: the method name.
        surface_out: the output surface file.
        area_surfs: specify surfaces to do vertex area correction based on.
        area_metrics: specify vertex area metrics to do area correction based\
            on.
        opt_bypass_sphere_check: ADVANCED: allow the current and new 'spheres'\
            to have arbitrary shape as long as they follow the same contour.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-resample",
        "surface_in": surface_in,
        "current_sphere": current_sphere,
        "new_sphere": new_sphere,
        "method": method,
        "surface_out": surface_out,
        "opt_bypass_sphere_check": opt_bypass_sphere_check,
    }
    if area_surfs is not None:
        params["area_surfs"] = area_surfs
    if area_metrics is not None:
        params["area_metrics"] = area_metrics
    return params


def surface_resample_cargs(
    params: SurfaceResampleParameters,
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
    cargs.append("-surface-resample")
    cargs.append(execution.input_file(params.get("surface_in")))
    cargs.append(execution.input_file(params.get("current_sphere")))
    cargs.append(execution.input_file(params.get("new_sphere")))
    cargs.append(params.get("method"))
    cargs.append(params.get("surface_out"))
    if params.get("area_surfs") is not None:
        cargs.extend(dyn_cargs(params.get("area_surfs")["__STYXTYPE__"])(params.get("area_surfs"), execution))
    if params.get("area_metrics") is not None:
        cargs.extend(dyn_cargs(params.get("area_metrics")["__STYXTYPE__"])(params.get("area_metrics"), execution))
    if params.get("opt_bypass_sphere_check"):
        cargs.append("-bypass-sphere-check")
    return cargs


def surface_resample_outputs(
    params: SurfaceResampleParameters,
    execution: Execution,
) -> SurfaceResampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceResampleOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(params.get("surface_out")),
    )
    return ret


def surface_resample_execute(
    params: SurfaceResampleParameters,
    execution: Execution,
) -> SurfaceResampleOutputs:
    """
    Resample a surface to a different mesh.
    
    Resamples a surface file, given two spherical surfaces that are in register.
    If ADAP_BARY_AREA is used, exactly one of -area-surfs or -area-metrics must
    be specified. This method is not generally recommended for surface
    resampling, but is provided for completeness.
    
    The BARYCENTRIC method is generally recommended for anatomical surfaces, in
    order to minimize smoothing.
    
    For cut surfaces (including flatmaps), use -surface-cut-resample.
    
    Instead of resampling a spherical surface, the
    -surface-sphere-project-unproject command is recommended.
    
    The <method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceResampleOutputs`).
    """
    cargs = surface_resample_cargs(params, execution)
    ret = surface_resample_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_resample(
    surface_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    method: str,
    surface_out: str,
    area_surfs: SurfaceResampleAreaSurfsParameters | None = None,
    area_metrics: SurfaceResampleAreaMetricsParameters | None = None,
    opt_bypass_sphere_check: bool = False,
    runner: Runner | None = None,
) -> SurfaceResampleOutputs:
    """
    Resample a surface to a different mesh.
    
    Resamples a surface file, given two spherical surfaces that are in register.
    If ADAP_BARY_AREA is used, exactly one of -area-surfs or -area-metrics must
    be specified. This method is not generally recommended for surface
    resampling, but is provided for completeness.
    
    The BARYCENTRIC method is generally recommended for anatomical surfaces, in
    order to minimize smoothing.
    
    For cut surfaces (including flatmaps), use -surface-cut-resample.
    
    Instead of resampling a spherical surface, the
    -surface-sphere-project-unproject command is recommended.
    
    The <method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_in: the surface file to resample.
        current_sphere: a sphere surface with the mesh that the input surface\
            is currently on.
        new_sphere: a sphere surface that is in register with <current-sphere>\
            and has the desired output mesh.
        method: the method name.
        surface_out: the output surface file.
        area_surfs: specify surfaces to do vertex area correction based on.
        area_metrics: specify vertex area metrics to do area correction based\
            on.
        opt_bypass_sphere_check: ADVANCED: allow the current and new 'spheres'\
            to have arbitrary shape as long as they follow the same contour.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_RESAMPLE_METADATA)
    params = surface_resample_params(surface_in=surface_in, current_sphere=current_sphere, new_sphere=new_sphere, method=method, surface_out=surface_out, area_surfs=area_surfs, area_metrics=area_metrics, opt_bypass_sphere_check=opt_bypass_sphere_check)
    return surface_resample_execute(params, execution)


__all__ = [
    "SURFACE_RESAMPLE_METADATA",
    "SurfaceResampleAreaMetricsParameters",
    "SurfaceResampleAreaSurfsParameters",
    "SurfaceResampleOutputs",
    "SurfaceResampleParameters",
    "surface_resample",
    "surface_resample_area_metrics_params",
    "surface_resample_area_surfs_params",
    "surface_resample_params",
]
