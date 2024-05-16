# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.792806

import typing

from ..styxdefs import *


SURFACE_NORMALS_METADATA = Metadata(
    id="cd9ef7063094ee215a9944b8661fee6515043b6c",
    name="surface-normals",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceNormalsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_normals(...)`.
    """
    metric_out: OutputPathType
    """the normal vectors"""


def surface_normals(
    runner: Runner,
    surface: InputPathType,
    metric_out: InputPathType,
) -> SurfaceNormalsOutputs:
    """
    OUTPUT VERTEX NORMALS AS METRIC FILE.
    
    Computes the normal vectors of the surface file, and outputs them as a 3
    column metric file.
    
    Args:
        runner: Command runner
        surface: the surface to output the normals of
        metric_out: the normal vectors
    Returns:
        NamedTuple of outputs (described in `SurfaceNormalsOutputs`).
    """
    execution = runner.start_execution(SURFACE_NORMALS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-normals")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_out))
    ret = SurfaceNormalsOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret
