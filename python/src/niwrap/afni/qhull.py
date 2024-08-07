# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

QHULL_METADATA = Metadata(
    id="b132d50e05aa63af1c8988eaaa09fbfdccc9c0a1",
    name="qhull",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class QhullOutputs(typing.NamedTuple):
    """
    Output object returned when calling `qhull(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_results: OutputPathType | None
    """Output file with the specified results."""


def qhull(
    input_coords: str,
    delaunay: bool = False,
    furthest_delaunay: bool = False,
    voronoi: bool = False,
    furthest_voronoi: bool = False,
    halfspace_intersection: bool = False,
    triangulated_output: bool = False,
    joggled_input: bool = False,
    verify: bool = False,
    summary: bool = False,
    vertices_incident: bool = False,
    normals: bool = False,
    vertex_coordinates: bool = False,
    halfspace_intersections: bool = False,
    extreme_points: bool = False,
    total_area_volume: bool = False,
    off_format: bool = False,
    geomview_output: bool = False,
    mathematica_output: bool = False,
    print_facets: str | None = None,
    output_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> QhullOutputs:
    """
    qhull by AFNI Team.
    
    Tool to compute convex hulls and related structures.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/qhull.html
    
    Args:
        input_coords: Dimension, number of points, and point coordinates\
            provided via stdin.
        delaunay: Compute Delaunay triangulation by lifting points to a\
            paraboloid.
        furthest_delaunay: Compute furthest-site Delaunay triangulation (upper\
            convex hull).
        voronoi: Compute Voronoi diagram as the dual of the Delaunay\
            triangulation.
        furthest_voronoi: Compute furthest-site Voronoi diagram.
        halfspace_intersection: Compute halfspace intersection about\
            [1,1,0,...] via polar duality.
        triangulated_output: Triangulated output.
        joggled_input: Joggled input instead of merged facets.
        verify: Verify result: structure, convexity, and point inclusion.
        summary: Summary of results.
        vertices_incident: Vertices incident to each facet.
        normals: Normals with offsets.
        vertex_coordinates: Vertex coordinates (if 'Qc', includes coplanar\
            points). If 'v', Voronoi vertices.
        halfspace_intersections: Halfspace intersections.
        extreme_points: Extreme points (convex hull vertices).
        total_area_volume: Compute total area and volume.
        off_format: OFF format (if 'v', outputs Voronoi regions).
        geomview_output: Geomview output (2-d, 3-d and 4-d).
        mathematica_output: Mathematica output (2-d and 3-d).
        print_facets: Print facets that include point n, -n if not.
        output_file: Output results to file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QhullOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QHULL_METADATA)
    cargs = []
    cargs.append("qhull")
    cargs.append("[OPTIONS]")
    cargs.append("[OUTPUT_OPTIONS]")
    ret = QhullOutputs(
        root=execution.output_file("."),
        output_results=execution.output_file(f"{pathlib.Path(output_file).name}.txt") if output_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QHULL_METADATA",
    "QhullOutputs",
    "qhull",
]
