# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.693207

import typing

from ..styxdefs import *


SURFACE_INFLATION_METADATA = Metadata(
    id="4396d52c247c1666b5966ccb5860c8a28e87cdee",
    name="surface-inflation",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceInflationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_inflation(...)`.
    """
    surface_out: OutputPathType
    """output surface file"""


def surface_inflation(
    runner: Runner,
    anatomical_surface_in: InputPathType,
    surface_in: InputPathType,
    number_of_smoothing_cycles: float | int,
    smoothing_strength: float | int,
    smoothing_iterations: float | int,
    inflation_factor: float | int,
    surface_out: InputPathType,
) -> SurfaceInflationOutputs:
    """
    SURFACE INFLATION.
    
    Inflate a surface by performing cycles that consist of smoothing followed by
    inflation (to correct shrinkage caused by smoothing).
    
    Args:
        runner: Command runner
        anatomical_surface_in: the anatomical surface
        surface_in: the surface file to inflate
        number_of_smoothing_cycles: number of smoothing cycles
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0])
        smoothing_iterations: smoothing iterations
        inflation_factor: inflation factor
        surface_out: output surface file
    Returns:
        NamedTuple of outputs (described in `SurfaceInflationOutputs`).
    """
    execution = runner.start_execution(SURFACE_INFLATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-inflation")
    cargs.append(execution.input_file(anatomical_surface_in))
    cargs.append(execution.input_file(surface_in))
    cargs.append(str(number_of_smoothing_cycles))
    cargs.append(str(smoothing_strength))
    cargs.append(str(smoothing_iterations))
    cargs.append(str(inflation_factor))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceInflationOutputs(
        surface_out=execution.output_file(f"{surface_out}"),
    )
    execution.run(cargs)
    return ret
