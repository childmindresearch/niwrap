# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.708424

import typing

from ..styxdefs import *


SURFACE_AFFINE_REGRESSION_METADATA = Metadata(
    id="d84b2ea0b2dea9173c32a06a28b309e177370f67",
    name="surface-affine-regression",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceAffineRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_affine_regression(...)`.
    """


def surface_affine_regression(
    runner: Runner,
    source: InputPathType,
    target: InputPathType,
    affine_out: str,
) -> SurfaceAffineRegressionOutputs:
    """
    REGRESS THE AFFINE TRANSFORM BETWEEN SURFACES ON THE SAME MESH.
    
    Use linear regression to compute an affine that minimizes the sum of squares
    of the coordinate differences between the target surface and the warped
    source surface. Note that this has a bias to shrink the surface that is
    being warped. The output is written as a NIFTI 'world' matrix, see
    -convert-affine to convert it for use in other software.
    
    Args:
        runner: Command runner
        source: the surface to warp
        target: the surface to match the coordinates of
        affine_out: output - the output affine file
    Returns:
        NamedTuple of outputs (described in `SurfaceAffineRegressionOutputs`).
    """
    execution = runner.start_execution(SURFACE_AFFINE_REGRESSION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-affine-regression")
    cargs.append(execution.input_file(source))
    cargs.append(execution.input_file(target))
    cargs.append(affine_out)
    ret = SurfaceAffineRegressionOutputs(
    )
    execution.run(cargs)
    return ret
