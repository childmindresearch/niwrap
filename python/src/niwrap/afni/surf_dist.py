# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_DIST_METADATA = Metadata(
    id="ba51dd4f5e28dff9f90eeed0a06742c5cbdeb475.boutiques",
    name="SurfDist",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SurfDistOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_dist(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    distances: OutputPathType
    """File containing the distances between nodes"""


def surf_dist(
    surface: InputPathType,
    nodepairs: InputPathType,
    node_path_do: str | None = None,
    graph: bool = False,
    runner: Runner | None = None,
) -> SurfDistOutputs:
    """
    Calculate shortest distance between node pairs on a surface mesh.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfDist.html
    
    Args:
        surface: Surface on which distances are computed.
        nodepairs: Specify node pairs for distance computation.
        node_path_do: Output the shortest path between each node pair as a SUMA\
            Displayable object.
        graph: Calculate distance along the mesh (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfDistOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_DIST_METADATA)
    cargs = []
    cargs.append("SurfDist")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(nodepairs))
    if node_path_do is not None:
        cargs.extend([
            "-node_path_do",
            node_path_do
        ])
    if graph:
        cargs.append("-graph")
    ret = SurfDistOutputs(
        root=execution.output_file("."),
        distances=execution.output_file("example.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_DIST_METADATA",
    "SurfDistOutputs",
    "surf_dist",
]