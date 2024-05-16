# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.990353

import typing

from ..styxdefs import *


SURFACE_CURVATURE_METADATA = Metadata(
    id="929a909815b992062c14ff5d6fd6f6b6a08113c8",
    name="surface-curvature",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceCurvatureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_curvature(...)`.
    """


def surface_curvature(
    runner: Runner,
    surface: InputPathType,
    opt_mean: bool = False,
    opt_gauss: bool = False,
) -> SurfaceCurvatureOutputs:
    """
    CALCULATE CURVATURE OF SURFACE.
    
    Compute the curvature of the surface, using the method from:
    Interactive Texture Mapping by J. Maillot, Yahia, and Verroust, 1993.
    ACM-0-98791-601-8/93/008
    
    Args:
        runner: Command runner
        surface: the surface to compute the curvature of
        opt_mean: output mean curvature
        opt_gauss: output gaussian curvature
    Returns:
        NamedTuple of outputs (described in `SurfaceCurvatureOutputs`).
    """
    execution = runner.start_execution(SURFACE_CURVATURE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-curvature")
    cargs.append(execution.input_file(surface))
    if opt_mean:
        cargs.append("-mean")
    if opt_gauss:
        cargs.append("-gauss")
    ret = SurfaceCurvatureOutputs(
    )
    execution.run(cargs)
    return ret
