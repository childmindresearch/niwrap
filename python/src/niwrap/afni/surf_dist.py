# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURF_DIST_METADATA = Metadata(
    id="64734b24b6511134261a4f149b84d909cf13f56f",
    name="SurfDist",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
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
    euclidean: bool = False,
    euclidian: bool = False,
    graph: bool = False,
    from_node: str | None = None,
    to_nodes: InputPathType | None = None,
    runner: Runner | None = None,
) -> SurfDistOutputs:
    """
    SurfDist by AFNI Team.
    
    Calculate shortest distance between node pairs on a surface mesh.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfDist.html
    
    Args:
        surface: Surface on which distances are computed.
        nodepairs: Specify node pairs for distance computation.
        node_path_do: Output the shortest path between each node pair as a SUMA\
            Displayable object.
        euclidean: Calculate Euclidean distance, rather than graph distance.
        euclidian: Synonym for '-Euclidean'.
        graph: Calculate distance along the mesh (default).
        from_node: Specify one starting node for pair calculation.
        to_nodes: Specify nodes used for pair calculation when using\
            -from_node.
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
        cargs.extend(["-node_path_do", node_path_do])
    if graph:
        cargs.append("-graph")
    ret = SurfDistOutputs(
        root=execution.output_file("."),
        distances=execution.output_file(f"example.1D", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_DIST_METADATA",
    "SurfDistOutputs",
    "surf_dist",
]
