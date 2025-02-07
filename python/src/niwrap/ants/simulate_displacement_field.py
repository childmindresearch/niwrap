# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SIMULATE_DISPLACEMENT_FIELD_METADATA = Metadata(
    id="ca776aa44d13ed564a1e49ff2d3269669eb9067c.boutiques",
    name="SimulateDisplacementField",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
SimulateDisplacementFieldBsplineOptionsParameters = typing.TypedDict('SimulateDisplacementFieldBsplineOptionsParameters', {
    "__STYX_TYPE__": typing.Literal["bspline_options"],
    "number_of_fitting_levels": typing.NotRequired[int | None],
    "number_of_control_points": typing.NotRequired[int | None],
})
SimulateDisplacementFieldExponentialOptionsParameters = typing.TypedDict('SimulateDisplacementFieldExponentialOptionsParameters', {
    "__STYX_TYPE__": typing.Literal["exponential_options"],
    "smoothing_standard_deviation": typing.NotRequired[float | None],
})
SimulateDisplacementFieldParameters = typing.TypedDict('SimulateDisplacementFieldParameters', {
    "__STYX_TYPE__": typing.Literal["SimulateDisplacementField"],
    "image_dimension": int,
    "displacement_field_type": typing.Literal["BSpline", "Exponential"],
    "domain_image": InputPathType,
    "output_field": str,
    "number_of_random_points": typing.NotRequired[int | None],
    "standard_deviation_displacement_field": typing.NotRequired[float | None],
    "enforce_stationary_boundary": typing.NotRequired[int | None],
    "displacement_specific_options": typing.NotRequired[typing.Union[SimulateDisplacementFieldBsplineOptionsParameters, SimulateDisplacementFieldExponentialOptionsParameters] | None],
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
        "SimulateDisplacementField": simulate_displacement_field_cargs,
        "bspline_options": simulate_displacement_field_bspline_options_cargs,
        "exponential_options": simulate_displacement_field_exponential_options_cargs,
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
        "SimulateDisplacementField": simulate_displacement_field_outputs,
        "bspline_options": simulate_displacement_field_bspline_options_outputs,
        "exponential_options": simulate_displacement_field_exponential_options_outputs,
    }.get(t)


def simulate_displacement_field_bspline_options_params(
    number_of_fitting_levels: int | None = 4,
    number_of_control_points: int | None = 4,
) -> SimulateDisplacementFieldBsplineOptionsParameters:
    """
    Build parameters.
    
    Args:
        number_of_fitting_levels: Number of fitting levels for BSpline.
        number_of_control_points: Number of control points for BSpline.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bspline_options",
    }
    if number_of_fitting_levels is not None:
        params["number_of_fitting_levels"] = number_of_fitting_levels
    if number_of_control_points is not None:
        params["number_of_control_points"] = number_of_control_points
    return params


def simulate_displacement_field_bspline_options_cargs(
    params: SimulateDisplacementFieldBsplineOptionsParameters,
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
    if params.get("number_of_fitting_levels") is not None:
        cargs.append(str(params.get("number_of_fitting_levels")))
    if params.get("number_of_control_points") is not None:
        cargs.append(str(params.get("number_of_control_points")))
    return cargs


def simulate_displacement_field_exponential_options_params(
    smoothing_standard_deviation: float | None = 4,
) -> SimulateDisplacementFieldExponentialOptionsParameters:
    """
    Build parameters.
    
    Args:
        smoothing_standard_deviation: Smoothing standard deviation for\
            Exponential.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "exponential_options",
    }
    if smoothing_standard_deviation is not None:
        params["smoothing_standard_deviation"] = smoothing_standard_deviation
    return params


def simulate_displacement_field_exponential_options_cargs(
    params: SimulateDisplacementFieldExponentialOptionsParameters,
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
    if params.get("smoothing_standard_deviation") is not None:
        cargs.append(str(params.get("smoothing_standard_deviation")))
    return cargs


class SimulateDisplacementFieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `simulate_displacement_field(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_displacement_field: OutputPathType
    """The simulated displacement field."""


def simulate_displacement_field_params(
    image_dimension: int,
    displacement_field_type: typing.Literal["BSpline", "Exponential"],
    domain_image: InputPathType,
    output_field: str,
    number_of_random_points: int | None = 1000,
    standard_deviation_displacement_field: float | None = 10,
    enforce_stationary_boundary: int | None = 1,
    displacement_specific_options: typing.Union[SimulateDisplacementFieldBsplineOptionsParameters, SimulateDisplacementFieldExponentialOptionsParameters] | None = None,
) -> SimulateDisplacementFieldParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Dimensionality of the image.
        displacement_field_type: Type of displacement field to simulate.
        domain_image: Image defining the domain for the displacement field.
        output_field: Path to save the output displacement field.
        number_of_random_points: Number of random points to use in the\
            simulation.
        standard_deviation_displacement_field: Standard deviation for the\
            displacement field.
        enforce_stationary_boundary: Boolean flag indicating whether to enforce\
            stationary boundary.
        displacement_specific_options: Options specific to the type of\
            displacement field simulation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SimulateDisplacementField",
        "image_dimension": image_dimension,
        "displacement_field_type": displacement_field_type,
        "domain_image": domain_image,
        "output_field": output_field,
    }
    if number_of_random_points is not None:
        params["number_of_random_points"] = number_of_random_points
    if standard_deviation_displacement_field is not None:
        params["standard_deviation_displacement_field"] = standard_deviation_displacement_field
    if enforce_stationary_boundary is not None:
        params["enforce_stationary_boundary"] = enforce_stationary_boundary
    if displacement_specific_options is not None:
        params["displacement_specific_options"] = displacement_specific_options
    return params


def simulate_displacement_field_cargs(
    params: SimulateDisplacementFieldParameters,
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
    cargs.append("SimulateDisplacementField")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(params.get("displacement_field_type"))
    cargs.append(execution.input_file(params.get("domain_image")))
    cargs.append(params.get("output_field"))
    if params.get("number_of_random_points") is not None:
        cargs.append(str(params.get("number_of_random_points")))
    if params.get("standard_deviation_displacement_field") is not None:
        cargs.append(str(params.get("standard_deviation_displacement_field")))
    if params.get("enforce_stationary_boundary") is not None:
        cargs.append(str(params.get("enforce_stationary_boundary")))
    if params.get("displacement_specific_options") is not None:
        cargs.extend(dyn_cargs(params.get("displacement_specific_options")["__STYXTYPE__"])(params.get("displacement_specific_options"), execution))
    return cargs


def simulate_displacement_field_outputs(
    params: SimulateDisplacementFieldParameters,
    execution: Execution,
) -> SimulateDisplacementFieldOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SimulateDisplacementFieldOutputs(
        root=execution.output_file("."),
        output_displacement_field=execution.output_file(params.get("output_field")),
    )
    return ret


def simulate_displacement_field_execute(
    params: SimulateDisplacementFieldParameters,
    execution: Execution,
) -> SimulateDisplacementFieldOutputs:
    """
    Simulate displacement fields using various methods such as BSpline or
    Exponential.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SimulateDisplacementFieldOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = simulate_displacement_field_cargs(params, execution)
    ret = simulate_displacement_field_outputs(params, execution)
    execution.run(cargs)
    return ret


def simulate_displacement_field(
    image_dimension: int,
    displacement_field_type: typing.Literal["BSpline", "Exponential"],
    domain_image: InputPathType,
    output_field: str,
    number_of_random_points: int | None = 1000,
    standard_deviation_displacement_field: float | None = 10,
    enforce_stationary_boundary: int | None = 1,
    displacement_specific_options: typing.Union[SimulateDisplacementFieldBsplineOptionsParameters, SimulateDisplacementFieldExponentialOptionsParameters] | None = None,
    runner: Runner | None = None,
) -> SimulateDisplacementFieldOutputs:
    """
    Simulate displacement fields using various methods such as BSpline or
    Exponential.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Dimensionality of the image.
        displacement_field_type: Type of displacement field to simulate.
        domain_image: Image defining the domain for the displacement field.
        output_field: Path to save the output displacement field.
        number_of_random_points: Number of random points to use in the\
            simulation.
        standard_deviation_displacement_field: Standard deviation for the\
            displacement field.
        enforce_stationary_boundary: Boolean flag indicating whether to enforce\
            stationary boundary.
        displacement_specific_options: Options specific to the type of\
            displacement field simulation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SimulateDisplacementFieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIMULATE_DISPLACEMENT_FIELD_METADATA)
    params = simulate_displacement_field_params(image_dimension=image_dimension, displacement_field_type=displacement_field_type, domain_image=domain_image, output_field=output_field, number_of_random_points=number_of_random_points, standard_deviation_displacement_field=standard_deviation_displacement_field, enforce_stationary_boundary=enforce_stationary_boundary, displacement_specific_options=displacement_specific_options)
    return simulate_displacement_field_execute(params, execution)


__all__ = [
    "SIMULATE_DISPLACEMENT_FIELD_METADATA",
    "SimulateDisplacementFieldBsplineOptionsParameters",
    "SimulateDisplacementFieldExponentialOptionsParameters",
    "SimulateDisplacementFieldOutputs",
    "SimulateDisplacementFieldParameters",
    "simulate_displacement_field",
    "simulate_displacement_field_bspline_options_params",
    "simulate_displacement_field_exponential_options_params",
    "simulate_displacement_field_params",
]
