# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_METRICS_METADATA = Metadata(
    id="9c7c68750ba7fdd75cdb0aab145fa2f084713b18",
    name="SurfaceMetrics",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceMetricsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_metrics(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_metrics(
    surf1: str,
    volume: bool = False,
    convexity: bool = False,
    closest_node: InputPathType | None = None,
    area: bool = False,
    tri_sines: bool = False,
    tri_cosines: bool = False,
    tri_co_sines: bool = False,
    tri_angles: bool = False,
    node_angles: bool = False,
    curvature: bool = False,
    edges: bool = False,
    node_normals: bool = False,
    face_normals: bool = False,
    normals_scale: float | int | None = None,
    coords: bool = False,
    sph_coords: bool = False,
    sph_coords_center: list[float | int] | None = None,
    boundary_nodes: bool = False,
    boundary_triangles: bool = False,
    internal_nodes: bool = False,
    tlrc: bool = False,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> SurfaceMetricsOutputs:
    """
    SurfaceMetrics by AFNI Team.
    
    Outputs information about a surface's mesh.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfaceMetrics.html
    
    Args:
        surf1: Specifies the input surface.
        volume: Calculates the volume of a surface.
        convexity: Output surface convexity at each node.
        closest_node: Find the closest node to each XYZ triplet in XYZ_LIST.1D.
        area: Output area of each triangle.
        tri_sines: Output sine of angles at nodes forming triangles.
        tri_cosines: Output cosine of angles at nodes forming triangles.
        tri_co_sines: Output both cosines and sines of angles at nodes forming\
            triangles.
        tri_angles: Unsigned angles in radians of triangles.
        node_angles: Unsigned angles in radians at nodes of surface.
        curvature: Output curvature at each node.
        edges: Outputs info on each edge.
        node_normals: Outputs segments along node normals.
        face_normals: Outputs segments along triangle normals.
        normals_scale: Scale the normals by a given factor.
        coords: Output coordinates of each node after any transformation.
        sph_coords: Output spherical coordinates of each node.
        sph_coords_center: Shift each node by x y z before calculating\
            spherical coordinates.
        boundary_nodes: Output nodes that form a boundary of a surface.
        boundary_triangles: Output triangles that form a boundary of a surface.
        internal_nodes: Output nodes that are not a boundary.
        tlrc: Apply Talairach transform to surface.
        prefix: Use prefix for output files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceMetricsOutputs`).
    """
    runner = runner or get_global_runner()
    if sph_coords_center is not None and not (len(sph_coords_center) <= 3): 
        raise ValueError(f"Length of 'sph_coords_center' must be less than 3 but was {len(sph_coords_center)}")
    execution = runner.start_execution(SURFACE_METRICS_METADATA)
    cargs = []
    cargs.append("SurfaceMetrics")
    cargs.append("<METRIC>")
    cargs.append("-SURF_1")
    cargs.append("[-tlrc]")
    cargs.append("[-prefix")
    cargs.append("PREFIX]")
    ret = SurfaceMetricsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_METRICS_METADATA",
    "SurfaceMetricsOutputs",
    "surface_metrics",
]
