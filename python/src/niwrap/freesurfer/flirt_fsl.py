# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FLIRT_FSL_METADATA = Metadata(
    id="398eadb6f9dd1993cfd24de7b26c3a35c5d0f1cd.boutiques",
    name="flirt.fsl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FlirtFslParameters = typing.TypedDict('FlirtFslParameters', {
    "__STYX_TYPE__": typing.Literal["flirt.fsl"],
    "input_volume": InputPathType,
    "reference_volume": InputPathType,
    "output_volume": typing.NotRequired[str | None],
    "output_matrix": typing.NotRequired[str | None],
    "initial_matrix": typing.NotRequired[InputPathType | None],
    "data_type": typing.NotRequired[typing.Literal["char", "short", "int", "float", "double"] | None],
    "cost_function": typing.NotRequired[typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None],
    "search_cost_function": typing.NotRequired[typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None],
    "use_sform_qform": bool,
    "display_initial_matrix": bool,
    "angle_representation": typing.NotRequired[typing.Literal["quaternion", "euler"] | None],
    "interpolation_method": typing.NotRequired[typing.Literal["trilinear", "nearestneighbour", "sinc"] | None],
    "sinc_width": typing.NotRequired[float | None],
    "sinc_window": typing.NotRequired[typing.Literal["rectangular", "hanning", "blackman"] | None],
    "histogram_bins": typing.NotRequired[float | None],
    "degrees_of_freedom": typing.NotRequired[float | None],
    "no_resample": bool,
    "force_scaling": bool,
    "min_voxel_dimension": typing.NotRequired[float | None],
    "apply_transform": bool,
    "apply_isotropic_transform": typing.NotRequired[float | None],
    "padding_size": typing.NotRequired[float | None],
    "search_range_x": typing.NotRequired[list[float] | None],
    "search_range_y": typing.NotRequired[list[float] | None],
    "search_range_z": typing.NotRequired[list[float] | None],
    "no_search": bool,
    "coarse_search_angle": typing.NotRequired[float | None],
    "fine_search_angle": typing.NotRequired[float | None],
    "schedule_file": typing.NotRequired[InputPathType | None],
    "reference_weight": typing.NotRequired[InputPathType | None],
    "input_weight": typing.NotRequired[InputPathType | None],
    "no_clamp": bool,
    "no_resample_blur": bool,
    "rigid_body_mode": bool,
    "verbose": bool,
    "verbose_level": typing.NotRequired[float | None],
    "pause_stages": bool,
    "version_flag": bool,
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
        "flirt.fsl": flirt_fsl_cargs,
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
        "flirt.fsl": flirt_fsl_outputs,
    }.get(t)


class FlirtFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flirt_fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_volume: OutputPathType | None
    """Resulting registered volume"""
    transformation_matrix: OutputPathType | None
    """Resulting transformation matrix in ASCII format"""


def flirt_fsl_params(
    input_volume: InputPathType,
    reference_volume: InputPathType,
    output_volume: str | None = None,
    output_matrix: str | None = None,
    initial_matrix: InputPathType | None = None,
    data_type: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    cost_function: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None = "corratio",
    search_cost_function: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None = "corratio",
    use_sform_qform: bool = False,
    display_initial_matrix: bool = False,
    angle_representation: typing.Literal["quaternion", "euler"] | None = "euler",
    interpolation_method: typing.Literal["trilinear", "nearestneighbour", "sinc"] | None = "trilinear",
    sinc_width: float | None = 7,
    sinc_window: typing.Literal["rectangular", "hanning", "blackman"] | None = None,
    histogram_bins: float | None = 256,
    degrees_of_freedom: float | None = 12,
    no_resample: bool = False,
    force_scaling: bool = False,
    min_voxel_dimension: float | None = None,
    apply_transform: bool = False,
    apply_isotropic_transform: float | None = None,
    padding_size: float | None = None,
    search_range_x: list[float] | None = [-90, 90],
    search_range_y: list[float] | None = [-90, 90],
    search_range_z: list[float] | None = [-90, 90],
    no_search: bool = False,
    coarse_search_angle: float | None = 60,
    fine_search_angle: float | None = 18,
    schedule_file: InputPathType | None = None,
    reference_weight: InputPathType | None = None,
    input_weight: InputPathType | None = None,
    no_clamp: bool = False,
    no_resample_blur: bool = False,
    rigid_body_mode: bool = False,
    verbose: bool = False,
    verbose_level: float | None = 0,
    pause_stages: bool = False,
    version_flag: bool = False,
) -> FlirtFslParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume.
        reference_volume: Reference volume.
        output_volume: Output volume.
        output_matrix: Output matrix filename (4x4 ASCII format).
        initial_matrix: Input 4x4 affine matrix filename.
        data_type: Force output data type.
        cost_function: Cost function for registration.
        search_cost_function: Cost function for search.
        use_sform_qform: Initialize using appropriate sform or qform.
        display_initial_matrix: Display initial matrix.
        angle_representation: Set angle representation.
        interpolation_method: Interpolation method.
        sinc_width: Sinc interpolation width.
        sinc_window: Sinc interpolation window.
        histogram_bins: Number of histogram bins.
        degrees_of_freedom: Degrees of freedom.
        no_resample: Do not change input sampling.
        force_scaling: Force rescaling even for low-res images.
        min_voxel_dimension: Minimum voxel dimension for sampling (in mm).
        apply_transform: Apply transform (no optimisation), requires -init.
        apply_isotropic_transform: Apply transform with isotropic resampling.
        padding_size: Padding size for interpolation outside image.
        search_range_x: Search range for rotation around x-axis.
        search_range_y: Search range for rotation around y-axis.
        search_range_z: Search range for rotation around z-axis.
        no_search: Set all angular search ranges to 0.
        coarse_search_angle: Coarse search angle in degrees.
        fine_search_angle: Fine search angle in degrees.
        schedule_file: Custom schedule filename.
        reference_weight: Weights for reference volume.
        input_weight: Weights for input volume.
        no_clamp: Do not use intensity clamping.
        no_resample_blur: Do not use blurring on downsampling.
        rigid_body_mode: Use 2D rigid body mode (ignores dof).
        verbose: Equivalent to -verbose 1.
        verbose_level: Level of verbosity.
        pause_stages: Pause at each stage.
        version_flag: Print version number.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "flirt.fsl",
        "input_volume": input_volume,
        "reference_volume": reference_volume,
        "use_sform_qform": use_sform_qform,
        "display_initial_matrix": display_initial_matrix,
        "no_resample": no_resample,
        "force_scaling": force_scaling,
        "apply_transform": apply_transform,
        "no_search": no_search,
        "no_clamp": no_clamp,
        "no_resample_blur": no_resample_blur,
        "rigid_body_mode": rigid_body_mode,
        "verbose": verbose,
        "pause_stages": pause_stages,
        "version_flag": version_flag,
    }
    if output_volume is not None:
        params["output_volume"] = output_volume
    if output_matrix is not None:
        params["output_matrix"] = output_matrix
    if initial_matrix is not None:
        params["initial_matrix"] = initial_matrix
    if data_type is not None:
        params["data_type"] = data_type
    if cost_function is not None:
        params["cost_function"] = cost_function
    if search_cost_function is not None:
        params["search_cost_function"] = search_cost_function
    if angle_representation is not None:
        params["angle_representation"] = angle_representation
    if interpolation_method is not None:
        params["interpolation_method"] = interpolation_method
    if sinc_width is not None:
        params["sinc_width"] = sinc_width
    if sinc_window is not None:
        params["sinc_window"] = sinc_window
    if histogram_bins is not None:
        params["histogram_bins"] = histogram_bins
    if degrees_of_freedom is not None:
        params["degrees_of_freedom"] = degrees_of_freedom
    if min_voxel_dimension is not None:
        params["min_voxel_dimension"] = min_voxel_dimension
    if apply_isotropic_transform is not None:
        params["apply_isotropic_transform"] = apply_isotropic_transform
    if padding_size is not None:
        params["padding_size"] = padding_size
    if search_range_x is not None:
        params["search_range_x"] = search_range_x
    if search_range_y is not None:
        params["search_range_y"] = search_range_y
    if search_range_z is not None:
        params["search_range_z"] = search_range_z
    if coarse_search_angle is not None:
        params["coarse_search_angle"] = coarse_search_angle
    if fine_search_angle is not None:
        params["fine_search_angle"] = fine_search_angle
    if schedule_file is not None:
        params["schedule_file"] = schedule_file
    if reference_weight is not None:
        params["reference_weight"] = reference_weight
    if input_weight is not None:
        params["input_weight"] = input_weight
    if verbose_level is not None:
        params["verbose_level"] = verbose_level
    return params


def flirt_fsl_cargs(
    params: FlirtFslParameters,
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
    cargs.append("flirt")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("reference_volume")))
    if params.get("output_volume") is not None:
        cargs.append(params.get("output_volume"))
    if params.get("output_matrix") is not None:
        cargs.extend([
            "-omat",
            params.get("output_matrix")
        ])
    if params.get("initial_matrix") is not None:
        cargs.extend([
            "-init",
            execution.input_file(params.get("initial_matrix"))
        ])
    if params.get("data_type") is not None:
        cargs.extend([
            "-datatype",
            params.get("data_type")
        ])
    if params.get("cost_function") is not None:
        cargs.extend([
            "-cost",
            params.get("cost_function")
        ])
    if params.get("search_cost_function") is not None:
        cargs.extend([
            "-searchcost",
            params.get("search_cost_function")
        ])
    if params.get("use_sform_qform"):
        cargs.append("-usesqform")
    if params.get("display_initial_matrix"):
        cargs.append("-displayinit")
    if params.get("angle_representation") is not None:
        cargs.extend([
            "-anglerep",
            params.get("angle_representation")
        ])
    if params.get("interpolation_method") is not None:
        cargs.extend([
            "-interp",
            params.get("interpolation_method")
        ])
    if params.get("sinc_width") is not None:
        cargs.extend([
            "-sincwidth",
            str(params.get("sinc_width"))
        ])
    if params.get("sinc_window") is not None:
        cargs.extend([
            "-sincwindow",
            params.get("sinc_window")
        ])
    if params.get("histogram_bins") is not None:
        cargs.extend([
            "-bins",
            str(params.get("histogram_bins"))
        ])
    if params.get("degrees_of_freedom") is not None:
        cargs.extend([
            "-dof",
            str(params.get("degrees_of_freedom"))
        ])
    if params.get("no_resample"):
        cargs.append("-noresample")
    if params.get("force_scaling"):
        cargs.append("-forcescaling")
    if params.get("min_voxel_dimension") is not None:
        cargs.extend([
            "-minsampling",
            str(params.get("min_voxel_dimension"))
        ])
    if params.get("apply_transform"):
        cargs.append("-applyxfm")
    if params.get("apply_isotropic_transform") is not None:
        cargs.extend([
            "-applyisoxfm",
            str(params.get("apply_isotropic_transform"))
        ])
    if params.get("padding_size") is not None:
        cargs.extend([
            "-paddingsize",
            str(params.get("padding_size"))
        ])
    if params.get("search_range_x") is not None:
        cargs.extend([
            "-searchrx",
            *map(str, params.get("search_range_x"))
        ])
    if params.get("search_range_y") is not None:
        cargs.extend([
            "-searchry",
            *map(str, params.get("search_range_y"))
        ])
    if params.get("search_range_z") is not None:
        cargs.extend([
            "-searchrz",
            *map(str, params.get("search_range_z"))
        ])
    if params.get("no_search"):
        cargs.append("-nosearch")
    if params.get("coarse_search_angle") is not None:
        cargs.extend([
            "-coarsesearch",
            str(params.get("coarse_search_angle"))
        ])
    if params.get("fine_search_angle") is not None:
        cargs.extend([
            "-finesearch",
            str(params.get("fine_search_angle"))
        ])
    if params.get("schedule_file") is not None:
        cargs.extend([
            "-schedule",
            execution.input_file(params.get("schedule_file"))
        ])
    if params.get("reference_weight") is not None:
        cargs.extend([
            "-refweight",
            execution.input_file(params.get("reference_weight"))
        ])
    if params.get("input_weight") is not None:
        cargs.extend([
            "-inweight",
            execution.input_file(params.get("input_weight"))
        ])
    if params.get("no_clamp"):
        cargs.append("-noclamp")
    if params.get("no_resample_blur"):
        cargs.append("-noresampblur")
    if params.get("rigid_body_mode"):
        cargs.append("-2D")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("verbose_level") is not None:
        cargs.extend([
            "-verbose",
            str(params.get("verbose_level"))
        ])
    if params.get("pause_stages"):
        cargs.append("-i")
    if params.get("version_flag"):
        cargs.append("-version")
    return cargs


def flirt_fsl_outputs(
    params: FlirtFslParameters,
    execution: Execution,
) -> FlirtFslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FlirtFslOutputs(
        root=execution.output_file("."),
        registered_volume=execution.output_file(params.get("output_volume") + ".nii") if (params.get("output_volume") is not None) else None,
        transformation_matrix=execution.output_file(params.get("output_matrix")) if (params.get("output_matrix") is not None) else None,
    )
    return ret


def flirt_fsl_execute(
    params: FlirtFslParameters,
    execution: Execution,
) -> FlirtFslOutputs:
    """
    FMRIB's Linear Image Registration Tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FlirtFslOutputs`).
    """
    cargs = flirt_fsl_cargs(params, execution)
    ret = flirt_fsl_outputs(params, execution)
    execution.run(cargs)
    return ret


def flirt_fsl(
    input_volume: InputPathType,
    reference_volume: InputPathType,
    output_volume: str | None = None,
    output_matrix: str | None = None,
    initial_matrix: InputPathType | None = None,
    data_type: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    cost_function: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None = "corratio",
    search_cost_function: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None = "corratio",
    use_sform_qform: bool = False,
    display_initial_matrix: bool = False,
    angle_representation: typing.Literal["quaternion", "euler"] | None = "euler",
    interpolation_method: typing.Literal["trilinear", "nearestneighbour", "sinc"] | None = "trilinear",
    sinc_width: float | None = 7,
    sinc_window: typing.Literal["rectangular", "hanning", "blackman"] | None = None,
    histogram_bins: float | None = 256,
    degrees_of_freedom: float | None = 12,
    no_resample: bool = False,
    force_scaling: bool = False,
    min_voxel_dimension: float | None = None,
    apply_transform: bool = False,
    apply_isotropic_transform: float | None = None,
    padding_size: float | None = None,
    search_range_x: list[float] | None = [-90, 90],
    search_range_y: list[float] | None = [-90, 90],
    search_range_z: list[float] | None = [-90, 90],
    no_search: bool = False,
    coarse_search_angle: float | None = 60,
    fine_search_angle: float | None = 18,
    schedule_file: InputPathType | None = None,
    reference_weight: InputPathType | None = None,
    input_weight: InputPathType | None = None,
    no_clamp: bool = False,
    no_resample_blur: bool = False,
    rigid_body_mode: bool = False,
    verbose: bool = False,
    verbose_level: float | None = 0,
    pause_stages: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> FlirtFslOutputs:
    """
    FMRIB's Linear Image Registration Tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume.
        reference_volume: Reference volume.
        output_volume: Output volume.
        output_matrix: Output matrix filename (4x4 ASCII format).
        initial_matrix: Input 4x4 affine matrix filename.
        data_type: Force output data type.
        cost_function: Cost function for registration.
        search_cost_function: Cost function for search.
        use_sform_qform: Initialize using appropriate sform or qform.
        display_initial_matrix: Display initial matrix.
        angle_representation: Set angle representation.
        interpolation_method: Interpolation method.
        sinc_width: Sinc interpolation width.
        sinc_window: Sinc interpolation window.
        histogram_bins: Number of histogram bins.
        degrees_of_freedom: Degrees of freedom.
        no_resample: Do not change input sampling.
        force_scaling: Force rescaling even for low-res images.
        min_voxel_dimension: Minimum voxel dimension for sampling (in mm).
        apply_transform: Apply transform (no optimisation), requires -init.
        apply_isotropic_transform: Apply transform with isotropic resampling.
        padding_size: Padding size for interpolation outside image.
        search_range_x: Search range for rotation around x-axis.
        search_range_y: Search range for rotation around y-axis.
        search_range_z: Search range for rotation around z-axis.
        no_search: Set all angular search ranges to 0.
        coarse_search_angle: Coarse search angle in degrees.
        fine_search_angle: Fine search angle in degrees.
        schedule_file: Custom schedule filename.
        reference_weight: Weights for reference volume.
        input_weight: Weights for input volume.
        no_clamp: Do not use intensity clamping.
        no_resample_blur: Do not use blurring on downsampling.
        rigid_body_mode: Use 2D rigid body mode (ignores dof).
        verbose: Equivalent to -verbose 1.
        verbose_level: Level of verbosity.
        pause_stages: Pause at each stage.
        version_flag: Print version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FlirtFslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FLIRT_FSL_METADATA)
    params = flirt_fsl_params(input_volume=input_volume, reference_volume=reference_volume, output_volume=output_volume, output_matrix=output_matrix, initial_matrix=initial_matrix, data_type=data_type, cost_function=cost_function, search_cost_function=search_cost_function, use_sform_qform=use_sform_qform, display_initial_matrix=display_initial_matrix, angle_representation=angle_representation, interpolation_method=interpolation_method, sinc_width=sinc_width, sinc_window=sinc_window, histogram_bins=histogram_bins, degrees_of_freedom=degrees_of_freedom, no_resample=no_resample, force_scaling=force_scaling, min_voxel_dimension=min_voxel_dimension, apply_transform=apply_transform, apply_isotropic_transform=apply_isotropic_transform, padding_size=padding_size, search_range_x=search_range_x, search_range_y=search_range_y, search_range_z=search_range_z, no_search=no_search, coarse_search_angle=coarse_search_angle, fine_search_angle=fine_search_angle, schedule_file=schedule_file, reference_weight=reference_weight, input_weight=input_weight, no_clamp=no_clamp, no_resample_blur=no_resample_blur, rigid_body_mode=rigid_body_mode, verbose=verbose, verbose_level=verbose_level, pause_stages=pause_stages, version_flag=version_flag)
    return flirt_fsl_execute(params, execution)


__all__ = [
    "FLIRT_FSL_METADATA",
    "FlirtFslOutputs",
    "FlirtFslParameters",
    "flirt_fsl",
    "flirt_fsl_params",
]
