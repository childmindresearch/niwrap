# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_CORRELATION_GRADIENT_METADATA = Metadata(
    id="3124adcadf240909150fde348a24ac400b7e75c1.boutiques",
    name="cifti-correlation-gradient",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiCorrelationGradientLeftSurfaceParameters = typing.TypedDict('CiftiCorrelationGradientLeftSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["left_surface"],
    "surface": InputPathType,
    "opt_left_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiCorrelationGradientRightSurfaceParameters = typing.TypedDict('CiftiCorrelationGradientRightSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["right_surface"],
    "surface": InputPathType,
    "opt_right_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiCorrelationGradientCerebellumSurfaceParameters = typing.TypedDict('CiftiCorrelationGradientCerebellumSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["cerebellum_surface"],
    "surface": InputPathType,
    "opt_cerebellum_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
})
CiftiCorrelationGradientDoubleCorrelationParameters = typing.TypedDict('CiftiCorrelationGradientDoubleCorrelationParameters', {
    "__STYX_TYPE__": typing.Literal["double_correlation"],
    "opt_fisher_z_first": bool,
    "opt_no_demean_first": bool,
    "opt_covariance_first": bool,
})
CiftiCorrelationGradientParameters = typing.TypedDict('CiftiCorrelationGradientParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-correlation-gradient"],
    "cifti": InputPathType,
    "cifti_out": str,
    "left_surface": typing.NotRequired[CiftiCorrelationGradientLeftSurfaceParameters | None],
    "right_surface": typing.NotRequired[CiftiCorrelationGradientRightSurfaceParameters | None],
    "cerebellum_surface": typing.NotRequired[CiftiCorrelationGradientCerebellumSurfaceParameters | None],
    "opt_surface_presmooth_surface_kernel": typing.NotRequired[float | None],
    "opt_volume_presmooth_volume_kernel": typing.NotRequired[float | None],
    "opt_presmooth_fwhm": bool,
    "opt_undo_fisher_z": bool,
    "opt_fisher_z": bool,
    "opt_surface_exclude_distance": typing.NotRequired[float | None],
    "opt_volume_exclude_distance": typing.NotRequired[float | None],
    "opt_covariance": bool,
    "opt_mem_limit_limit_gb": typing.NotRequired[float | None],
    "double_correlation": typing.NotRequired[CiftiCorrelationGradientDoubleCorrelationParameters | None],
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
        "cifti-correlation-gradient": cifti_correlation_gradient_cargs,
        "left_surface": cifti_correlation_gradient_left_surface_cargs,
        "right_surface": cifti_correlation_gradient_right_surface_cargs,
        "cerebellum_surface": cifti_correlation_gradient_cerebellum_surface_cargs,
        "double_correlation": cifti_correlation_gradient_double_correlation_cargs,
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
        "cifti-correlation-gradient": cifti_correlation_gradient_outputs,
        "left_surface": cifti_correlation_gradient_left_surface_outputs,
        "right_surface": cifti_correlation_gradient_right_surface_outputs,
        "cerebellum_surface": cifti_correlation_gradient_cerebellum_surface_outputs,
        "double_correlation": cifti_correlation_gradient_double_correlation_outputs,
    }.get(t)


def cifti_correlation_gradient_left_surface_params(
    surface: InputPathType,
    opt_left_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiCorrelationGradientLeftSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the left surface file.
        opt_left_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the left surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "left_surface",
        "surface": surface,
    }
    if opt_left_corrected_areas_area_metric is not None:
        params["opt_left_corrected_areas_area_metric"] = opt_left_corrected_areas_area_metric
    return params


def cifti_correlation_gradient_left_surface_cargs(
    params: CiftiCorrelationGradientLeftSurfaceParameters,
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
    cargs.append("-left-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_left_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-left-corrected-areas",
            execution.input_file(params.get("opt_left_corrected_areas_area_metric"))
        ])
    return cargs


def cifti_correlation_gradient_right_surface_params(
    surface: InputPathType,
    opt_right_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiCorrelationGradientRightSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the right surface file.
        opt_right_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the right surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "right_surface",
        "surface": surface,
    }
    if opt_right_corrected_areas_area_metric is not None:
        params["opt_right_corrected_areas_area_metric"] = opt_right_corrected_areas_area_metric
    return params


def cifti_correlation_gradient_right_surface_cargs(
    params: CiftiCorrelationGradientRightSurfaceParameters,
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
    cargs.append("-right-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_right_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-right-corrected-areas",
            execution.input_file(params.get("opt_right_corrected_areas_area_metric"))
        ])
    return cargs


def cifti_correlation_gradient_cerebellum_surface_params(
    surface: InputPathType,
    opt_cerebellum_corrected_areas_area_metric: InputPathType | None = None,
) -> CiftiCorrelationGradientCerebellumSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface: the cerebellum surface file.
        opt_cerebellum_corrected_areas_area_metric: vertex areas to use instead\
            of computing them from the cerebellum surface: the corrected vertex\
            areas, as a metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cerebellum_surface",
        "surface": surface,
    }
    if opt_cerebellum_corrected_areas_area_metric is not None:
        params["opt_cerebellum_corrected_areas_area_metric"] = opt_cerebellum_corrected_areas_area_metric
    return params


def cifti_correlation_gradient_cerebellum_surface_cargs(
    params: CiftiCorrelationGradientCerebellumSurfaceParameters,
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
    cargs.append("-cerebellum-surface")
    cargs.append(execution.input_file(params.get("surface")))
    if params.get("opt_cerebellum_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-cerebellum-corrected-areas",
            execution.input_file(params.get("opt_cerebellum_corrected_areas_area_metric"))
        ])
    return cargs


def cifti_correlation_gradient_double_correlation_params(
    opt_fisher_z_first: bool = False,
    opt_no_demean_first: bool = False,
    opt_covariance_first: bool = False,
) -> CiftiCorrelationGradientDoubleCorrelationParameters:
    """
    Build parameters.
    
    Args:
        opt_fisher_z_first: after the FIRST correlation, apply fisher small z\
            transform (ie, artanh).
        opt_no_demean_first: instead of correlation for the FIRST operation, do\
            dot product of rows, then normalize by diagonal.
        opt_covariance_first: instead of correlation for the FIRST operation,\
            compute covariance.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "double_correlation",
        "opt_fisher_z_first": opt_fisher_z_first,
        "opt_no_demean_first": opt_no_demean_first,
        "opt_covariance_first": opt_covariance_first,
    }
    return params


def cifti_correlation_gradient_double_correlation_cargs(
    params: CiftiCorrelationGradientDoubleCorrelationParameters,
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
    cargs.append("-double-correlation")
    if params.get("opt_fisher_z_first"):
        cargs.append("-fisher-z-first")
    if params.get("opt_no_demean_first"):
        cargs.append("-no-demean-first")
    if params.get("opt_covariance_first"):
        cargs.append("-covariance-first")
    return cargs


class CiftiCorrelationGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_correlation_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_correlation_gradient_params(
    cifti: InputPathType,
    cifti_out: str,
    left_surface: CiftiCorrelationGradientLeftSurfaceParameters | None = None,
    right_surface: CiftiCorrelationGradientRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiCorrelationGradientCerebellumSurfaceParameters | None = None,
    opt_surface_presmooth_surface_kernel: float | None = None,
    opt_volume_presmooth_volume_kernel: float | None = None,
    opt_presmooth_fwhm: bool = False,
    opt_undo_fisher_z: bool = False,
    opt_fisher_z: bool = False,
    opt_surface_exclude_distance: float | None = None,
    opt_volume_exclude_distance: float | None = None,
    opt_covariance: bool = False,
    opt_mem_limit_limit_gb: float | None = None,
    double_correlation: CiftiCorrelationGradientDoubleCorrelationParameters | None = None,
) -> CiftiCorrelationGradientParameters:
    """
    Build parameters.
    
    Args:
        cifti: the input cifti.
        cifti_out: the output cifti.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_surface_presmooth_surface_kernel: smooth on the surface before\
            computing the gradient: the size of the gaussian surface smoothing\
            kernel in mm, as sigma by default.
        opt_volume_presmooth_volume_kernel: smooth the volume before computing\
            the gradient: the size of the gaussian volume smoothing kernel in mm,\
            as sigma by default.
        opt_presmooth_fwhm: smoothing kernel sizes are FWHM, not sigma.
        opt_undo_fisher_z: apply the inverse fisher small z transform to the\
            input.
        opt_fisher_z: apply the fisher small z transform to the correlations\
            before taking the gradient.
        opt_surface_exclude_distance: exclude vertices near each seed vertex\
            from computation: geodesic distance from seed vertex for the exclusion\
            zone, in mm.
        opt_volume_exclude_distance: exclude voxels near each seed voxel from\
            computation: distance from seed voxel for the exclusion zone, in mm.
        opt_covariance: compute covariance instead of correlation.
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in\
            gigabytes.
        double_correlation: do two correlations before taking the gradient.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-correlation-gradient",
        "cifti": cifti,
        "cifti_out": cifti_out,
        "opt_presmooth_fwhm": opt_presmooth_fwhm,
        "opt_undo_fisher_z": opt_undo_fisher_z,
        "opt_fisher_z": opt_fisher_z,
        "opt_covariance": opt_covariance,
    }
    if left_surface is not None:
        params["left_surface"] = left_surface
    if right_surface is not None:
        params["right_surface"] = right_surface
    if cerebellum_surface is not None:
        params["cerebellum_surface"] = cerebellum_surface
    if opt_surface_presmooth_surface_kernel is not None:
        params["opt_surface_presmooth_surface_kernel"] = opt_surface_presmooth_surface_kernel
    if opt_volume_presmooth_volume_kernel is not None:
        params["opt_volume_presmooth_volume_kernel"] = opt_volume_presmooth_volume_kernel
    if opt_surface_exclude_distance is not None:
        params["opt_surface_exclude_distance"] = opt_surface_exclude_distance
    if opt_volume_exclude_distance is not None:
        params["opt_volume_exclude_distance"] = opt_volume_exclude_distance
    if opt_mem_limit_limit_gb is not None:
        params["opt_mem_limit_limit_gb"] = opt_mem_limit_limit_gb
    if double_correlation is not None:
        params["double_correlation"] = double_correlation
    return params


def cifti_correlation_gradient_cargs(
    params: CiftiCorrelationGradientParameters,
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
    cargs.append("-cifti-correlation-gradient")
    cargs.append(execution.input_file(params.get("cifti")))
    cargs.append(params.get("cifti_out"))
    if params.get("left_surface") is not None:
        cargs.extend(dyn_cargs(params.get("left_surface")["__STYXTYPE__"])(params.get("left_surface"), execution))
    if params.get("right_surface") is not None:
        cargs.extend(dyn_cargs(params.get("right_surface")["__STYXTYPE__"])(params.get("right_surface"), execution))
    if params.get("cerebellum_surface") is not None:
        cargs.extend(dyn_cargs(params.get("cerebellum_surface")["__STYXTYPE__"])(params.get("cerebellum_surface"), execution))
    if params.get("opt_surface_presmooth_surface_kernel") is not None:
        cargs.extend([
            "-surface-presmooth",
            str(params.get("opt_surface_presmooth_surface_kernel"))
        ])
    if params.get("opt_volume_presmooth_volume_kernel") is not None:
        cargs.extend([
            "-volume-presmooth",
            str(params.get("opt_volume_presmooth_volume_kernel"))
        ])
    if params.get("opt_presmooth_fwhm"):
        cargs.append("-presmooth-fwhm")
    if params.get("opt_undo_fisher_z"):
        cargs.append("-undo-fisher-z")
    if params.get("opt_fisher_z"):
        cargs.append("-fisher-z")
    if params.get("opt_surface_exclude_distance") is not None:
        cargs.extend([
            "-surface-exclude",
            str(params.get("opt_surface_exclude_distance"))
        ])
    if params.get("opt_volume_exclude_distance") is not None:
        cargs.extend([
            "-volume-exclude",
            str(params.get("opt_volume_exclude_distance"))
        ])
    if params.get("opt_covariance"):
        cargs.append("-covariance")
    if params.get("opt_mem_limit_limit_gb") is not None:
        cargs.extend([
            "-mem-limit",
            str(params.get("opt_mem_limit_limit_gb"))
        ])
    if params.get("double_correlation") is not None:
        cargs.extend(dyn_cargs(params.get("double_correlation")["__STYXTYPE__"])(params.get("double_correlation"), execution))
    return cargs


def cifti_correlation_gradient_outputs(
    params: CiftiCorrelationGradientParameters,
    execution: Execution,
) -> CiftiCorrelationGradientOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiCorrelationGradientOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_correlation_gradient_execute(
    params: CiftiCorrelationGradientParameters,
    execution: Execution,
) -> CiftiCorrelationGradientOutputs:
    """
    Correlate cifti rows and take gradient.
    
    For each structure, compute the correlation of the rows in the structure,
    and take the gradients of the resulting rows, then average them. Memory
    limit does not need to be an integer, you may also specify 0 to use as
    little memory as possible (this may be very slow).
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiCorrelationGradientOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_correlation_gradient_cargs(params, execution)
    ret = cifti_correlation_gradient_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_correlation_gradient(
    cifti: InputPathType,
    cifti_out: str,
    left_surface: CiftiCorrelationGradientLeftSurfaceParameters | None = None,
    right_surface: CiftiCorrelationGradientRightSurfaceParameters | None = None,
    cerebellum_surface: CiftiCorrelationGradientCerebellumSurfaceParameters | None = None,
    opt_surface_presmooth_surface_kernel: float | None = None,
    opt_volume_presmooth_volume_kernel: float | None = None,
    opt_presmooth_fwhm: bool = False,
    opt_undo_fisher_z: bool = False,
    opt_fisher_z: bool = False,
    opt_surface_exclude_distance: float | None = None,
    opt_volume_exclude_distance: float | None = None,
    opt_covariance: bool = False,
    opt_mem_limit_limit_gb: float | None = None,
    double_correlation: CiftiCorrelationGradientDoubleCorrelationParameters | None = None,
    runner: Runner | None = None,
) -> CiftiCorrelationGradientOutputs:
    """
    Correlate cifti rows and take gradient.
    
    For each structure, compute the correlation of the rows in the structure,
    and take the gradients of the resulting rows, then average them. Memory
    limit does not need to be an integer, you may also specify 0 to use as
    little memory as possible (this may be very slow).
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti: the input cifti.
        cifti_out: the output cifti.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_surface_presmooth_surface_kernel: smooth on the surface before\
            computing the gradient: the size of the gaussian surface smoothing\
            kernel in mm, as sigma by default.
        opt_volume_presmooth_volume_kernel: smooth the volume before computing\
            the gradient: the size of the gaussian volume smoothing kernel in mm,\
            as sigma by default.
        opt_presmooth_fwhm: smoothing kernel sizes are FWHM, not sigma.
        opt_undo_fisher_z: apply the inverse fisher small z transform to the\
            input.
        opt_fisher_z: apply the fisher small z transform to the correlations\
            before taking the gradient.
        opt_surface_exclude_distance: exclude vertices near each seed vertex\
            from computation: geodesic distance from seed vertex for the exclusion\
            zone, in mm.
        opt_volume_exclude_distance: exclude voxels near each seed voxel from\
            computation: distance from seed voxel for the exclusion zone, in mm.
        opt_covariance: compute covariance instead of correlation.
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in\
            gigabytes.
        double_correlation: do two correlations before taking the gradient.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCorrelationGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CORRELATION_GRADIENT_METADATA)
    params = cifti_correlation_gradient_params(cifti=cifti, cifti_out=cifti_out, left_surface=left_surface, right_surface=right_surface, cerebellum_surface=cerebellum_surface, opt_surface_presmooth_surface_kernel=opt_surface_presmooth_surface_kernel, opt_volume_presmooth_volume_kernel=opt_volume_presmooth_volume_kernel, opt_presmooth_fwhm=opt_presmooth_fwhm, opt_undo_fisher_z=opt_undo_fisher_z, opt_fisher_z=opt_fisher_z, opt_surface_exclude_distance=opt_surface_exclude_distance, opt_volume_exclude_distance=opt_volume_exclude_distance, opt_covariance=opt_covariance, opt_mem_limit_limit_gb=opt_mem_limit_limit_gb, double_correlation=double_correlation)
    return cifti_correlation_gradient_execute(params, execution)


__all__ = [
    "CIFTI_CORRELATION_GRADIENT_METADATA",
    "CiftiCorrelationGradientCerebellumSurfaceParameters",
    "CiftiCorrelationGradientDoubleCorrelationParameters",
    "CiftiCorrelationGradientLeftSurfaceParameters",
    "CiftiCorrelationGradientOutputs",
    "CiftiCorrelationGradientParameters",
    "CiftiCorrelationGradientRightSurfaceParameters",
    "cifti_correlation_gradient",
    "cifti_correlation_gradient_cerebellum_surface_params",
    "cifti_correlation_gradient_double_correlation_params",
    "cifti_correlation_gradient_left_surface_params",
    "cifti_correlation_gradient_params",
    "cifti_correlation_gradient_right_surface_params",
]
