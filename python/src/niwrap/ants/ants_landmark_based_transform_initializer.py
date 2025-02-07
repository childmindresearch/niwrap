# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_LANDMARK_BASED_TRANSFORM_INITIALIZER_METADATA = Metadata(
    id="0a1f0f529ca0b132289382b0bfa307fd1e5cda95.boutiques",
    name="antsLandmarkBasedTransformInitializer",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsLandmarkBasedTransformInitializerParameters = typing.TypedDict('AntsLandmarkBasedTransformInitializerParameters', {
    "__STYX_TYPE__": typing.Literal["antsLandmarkBasedTransformInitializer"],
    "dimension": int,
    "fixed_image": InputPathType,
    "moving_image": InputPathType,
    "transform_type": typing.Literal["rigid", "affine", "bspline"],
    "output_transform": str,
    "mesh_size": typing.NotRequired[str | None],
    "number_of_levels": typing.NotRequired[int | None],
    "order": typing.NotRequired[int | None],
    "enforce_stationary_boundaries": typing.NotRequired[typing.Literal[0, 1] | None],
    "landmark_weights": typing.NotRequired[InputPathType | None],
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
        "antsLandmarkBasedTransformInitializer": ants_landmark_based_transform_initializer_cargs,
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
        "antsLandmarkBasedTransformInitializer": ants_landmark_based_transform_initializer_outputs,
    }.get(t)


class AntsLandmarkBasedTransformInitializerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_landmark_based_transform_initializer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform: OutputPathType
    """The output file containing the initialized transform."""


def ants_landmark_based_transform_initializer_params(
    dimension: int,
    fixed_image: InputPathType,
    moving_image: InputPathType,
    transform_type: typing.Literal["rigid", "affine", "bspline"],
    output_transform: str,
    mesh_size: str | None = None,
    number_of_levels: int | None = None,
    order: int | None = None,
    enforce_stationary_boundaries: typing.Literal[0, 1] | None = None,
    landmark_weights: InputPathType | None = None,
) -> AntsLandmarkBasedTransformInitializerParameters:
    """
    Build parameters.
    
    Args:
        dimension: The dimensionality of the registration problem (e.g., 2 for\
            2D, 3 for 3D).
        fixed_image: The fixed image in the registration process.
        moving_image: The moving image in the registration process.
        transform_type: The type of transform to initialize. Options are\
            'rigid', 'affine', or 'bspline'.
        output_transform: The output transform file that will be created.
        mesh_size: The mesh size for the B-spline transform, specified as\
            'meshSize[0]xmeshSize[1]x...'. Default is '1x1x1'.
        number_of_levels: Number of levels for multi-resolution fitting.\
            Default is 4.
        order: The polynomial order of the B-spline transform. Default is 3.
        enforce_stationary_boundaries: Enforces stationary boundaries for the\
            B-spline transform. Default is 1 (true).
        landmark_weights: File containing landmark weights. Each row is either\
            'label,labelWeight' or 'labelWeight'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsLandmarkBasedTransformInitializer",
        "dimension": dimension,
        "fixed_image": fixed_image,
        "moving_image": moving_image,
        "transform_type": transform_type,
        "output_transform": output_transform,
    }
    if mesh_size is not None:
        params["mesh_size"] = mesh_size
    if number_of_levels is not None:
        params["number_of_levels"] = number_of_levels
    if order is not None:
        params["order"] = order
    if enforce_stationary_boundaries is not None:
        params["enforce_stationary_boundaries"] = enforce_stationary_boundaries
    if landmark_weights is not None:
        params["landmark_weights"] = landmark_weights
    return params


def ants_landmark_based_transform_initializer_cargs(
    params: AntsLandmarkBasedTransformInitializerParameters,
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
    cargs.append("antsLandmarkBasedTransformInitializer")
    cargs.append(str(params.get("dimension")))
    cargs.append(execution.input_file(params.get("fixed_image")))
    cargs.append(execution.input_file(params.get("moving_image")))
    cargs.append(params.get("transform_type"))
    cargs.append(params.get("output_transform"))
    if params.get("mesh_size") is not None:
        cargs.append(params.get("mesh_size"))
    if params.get("number_of_levels") is not None:
        cargs.append(str(params.get("number_of_levels")))
    if params.get("order") is not None:
        cargs.append(str(params.get("order")))
    if params.get("enforce_stationary_boundaries") is not None:
        cargs.append(str(params.get("enforce_stationary_boundaries")))
    if params.get("landmark_weights") is not None:
        cargs.append(execution.input_file(params.get("landmark_weights")))
    return cargs


def ants_landmark_based_transform_initializer_outputs(
    params: AntsLandmarkBasedTransformInitializerParameters,
    execution: Execution,
) -> AntsLandmarkBasedTransformInitializerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsLandmarkBasedTransformInitializerOutputs(
        root=execution.output_file("."),
        output_transform=execution.output_file(params.get("output_transform")),
    )
    return ret


def ants_landmark_based_transform_initializer_execute(
    params: AntsLandmarkBasedTransformInitializerParameters,
    execution: Execution,
) -> AntsLandmarkBasedTransformInitializerOutputs:
    """
    This tool initializes a transform between two images based on corresponding
    landmarks.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsLandmarkBasedTransformInitializerOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ants_landmark_based_transform_initializer_cargs(params, execution)
    ret = ants_landmark_based_transform_initializer_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_landmark_based_transform_initializer(
    dimension: int,
    fixed_image: InputPathType,
    moving_image: InputPathType,
    transform_type: typing.Literal["rigid", "affine", "bspline"],
    output_transform: str,
    mesh_size: str | None = None,
    number_of_levels: int | None = None,
    order: int | None = None,
    enforce_stationary_boundaries: typing.Literal[0, 1] | None = None,
    landmark_weights: InputPathType | None = None,
    runner: Runner | None = None,
) -> AntsLandmarkBasedTransformInitializerOutputs:
    """
    This tool initializes a transform between two images based on corresponding
    landmarks.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimension: The dimensionality of the registration problem (e.g., 2 for\
            2D, 3 for 3D).
        fixed_image: The fixed image in the registration process.
        moving_image: The moving image in the registration process.
        transform_type: The type of transform to initialize. Options are\
            'rigid', 'affine', or 'bspline'.
        output_transform: The output transform file that will be created.
        mesh_size: The mesh size for the B-spline transform, specified as\
            'meshSize[0]xmeshSize[1]x...'. Default is '1x1x1'.
        number_of_levels: Number of levels for multi-resolution fitting.\
            Default is 4.
        order: The polynomial order of the B-spline transform. Default is 3.
        enforce_stationary_boundaries: Enforces stationary boundaries for the\
            B-spline transform. Default is 1 (true).
        landmark_weights: File containing landmark weights. Each row is either\
            'label,labelWeight' or 'labelWeight'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsLandmarkBasedTransformInitializerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_LANDMARK_BASED_TRANSFORM_INITIALIZER_METADATA)
    params = ants_landmark_based_transform_initializer_params(dimension=dimension, fixed_image=fixed_image, moving_image=moving_image, transform_type=transform_type, output_transform=output_transform, mesh_size=mesh_size, number_of_levels=number_of_levels, order=order, enforce_stationary_boundaries=enforce_stationary_boundaries, landmark_weights=landmark_weights)
    return ants_landmark_based_transform_initializer_execute(params, execution)


__all__ = [
    "ANTS_LANDMARK_BASED_TRANSFORM_INITIALIZER_METADATA",
    "AntsLandmarkBasedTransformInitializerOutputs",
    "AntsLandmarkBasedTransformInitializerParameters",
    "ants_landmark_based_transform_initializer",
    "ants_landmark_based_transform_initializer_params",
]
