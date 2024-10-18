# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIMULATE_DISPLACEMENT_FIELD_METADATA = Metadata(
    id="15637f91784c5818fe388e20310bf89997f3216e.boutiques",
    name="SimulateDisplacementField",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


@dataclasses.dataclass
class SimulateDisplacementFieldBsplineOptions:
    number_of_fitting_levels: int | None = 4
    """Number of fitting levels for BSpline."""
    number_of_control_points: int | None = 4
    """Number of control points for BSpline."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        if self.number_of_fitting_levels is not None:
            cargs.append(str(self.number_of_fitting_levels))
        if self.number_of_control_points is not None:
            cargs.append(str(self.number_of_control_points))
        return cargs


@dataclasses.dataclass
class SimulateDisplacementFieldExponentialOptions:
    smoothing_standard_deviation: float | None = 4
    """Smoothing standard deviation for Exponential."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        if self.smoothing_standard_deviation is not None:
            cargs.append(str(self.smoothing_standard_deviation))
        return cargs


class SimulateDisplacementFieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `simulate_displacement_field(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_displacement_field: OutputPathType
    """The simulated displacement field."""


def simulate_displacement_field(
    image_dimension: int,
    displacement_field_type: typing.Literal["BSpline", "Exponential"],
    domain_image: InputPathType,
    output_field: InputPathType,
    number_of_random_points: int | None = 1000,
    standard_deviation_displacement_field: float | None = 10,
    enforce_stationary_boundary: int | None = 1,
    displacement_specific_options: typing.Union[SimulateDisplacementFieldBsplineOptions, SimulateDisplacementFieldExponentialOptions] | None = None,
    runner: Runner | None = None,
) -> SimulateDisplacementFieldOutputs:
    """
    Advanced Normalization Tools (ANTs) is a C++ library available through the
    command line that computes high-dimensional mappings to capture the statistics
    of brain structure and function. It allows one to organize, visualize and
    statistically explore large biomedical image sets. Additionally, it integrates
    imaging modalities in space + time and works across species or organ systems
    with minimal customization.
    
    The ANTs library is considered a state-of-the-art medical image registration
    and segmentation toolkit which depends on the Insight ToolKit, a widely used
    medical image processing library to which ANTs developers contribute.
    ANTs-related tools have also won several international, unbiased
    competitions such as MICCAI, BRATS, and STACOM.
    
    Author: ANTs developers
    
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
    cargs = []
    cargs.append("SimulateDisplacementField")
    cargs.append(str(image_dimension))
    cargs.append(displacement_field_type)
    cargs.append(execution.input_file(domain_image))
    cargs.append(execution.input_file(output_field))
    if number_of_random_points is not None:
        cargs.append(str(number_of_random_points))
    if standard_deviation_displacement_field is not None:
        cargs.append(str(standard_deviation_displacement_field))
    if enforce_stationary_boundary is not None:
        cargs.append(str(enforce_stationary_boundary))
    if displacement_specific_options is not None:
        cargs.extend(displacement_specific_options.run(execution))
    ret = SimulateDisplacementFieldOutputs(
        root=execution.output_file("."),
        output_displacement_field=execution.output_file(pathlib.Path(output_field).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIMULATE_DISPLACEMENT_FIELD_METADATA",
    "SimulateDisplacementFieldBsplineOptions",
    "SimulateDisplacementFieldExponentialOptions",
    "SimulateDisplacementFieldOutputs",
    "simulate_displacement_field",
]
