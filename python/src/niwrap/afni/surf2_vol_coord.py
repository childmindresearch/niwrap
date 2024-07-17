# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURF2_VOL_COORD_METADATA = Metadata(
    id="eee7b43a9da1ac2397d3f30fe1545a13e174d6d8",
    name="Surf2VolCoord",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class Surf2VolCoordOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf2_vol_coord(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    results_file: OutputPathType
    """Output results file."""


def surf2_vol_coord(
    surface: str,
    grid_vol: InputPathType,
    closest_nodes: InputPathType,
    prefix: str,
    grid_subbrick: float | int | None = None,
    sv: InputPathType | None = None,
    one_node: str | None = None,
    qual: str | None = None,
    lpi: bool = False,
    rai: bool = False,
    verb_level: float | int | None = None,
    runner: Runner | None = None,
) -> Surf2VolCoordOutputs:
    """
    Surf2VolCoord by AFNI Team.
    
    Relates node indices to coordinates given x y z coordinates and returns the
    nodes closest to them.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/Surf2VolCoord.html
    
    Args:
        surface: Specify input surface.
        grid_vol: Specifies the grid for the output volume.
        closest_nodes: A coordinate file specifying coordinates for which the\
            closest nodes will be found.
        prefix: Output results to file PREFIX (will overwrite). Default is\
            stdout.
        grid_subbrick: Sub-brick from which data are taken.
        sv: Surface Volume file aligning with the surface.
        one_node: Specify a single node's coordinates.
        qual: A string of characters that qualify the surface in which the\
            closest node was found.
        lpi: Coordinate axis direction for values in XYZ.1D are in LPI.
        rai: Coordinate axis direction for values in XYZ.1D are in RAI\
            (default).
        verb_level: Verbosity level, default is 0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Surf2VolCoordOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF2_VOL_COORD_METADATA)
    cargs = []
    cargs.append("Surf2VolCoord")
    cargs.append("-i_TYPE")
    cargs.extend(["-i_TYPE", surface])
    cargs.append("-grid_parent")
    cargs.extend(["-grid_parent", execution.input_file(grid_vol)])
    if grid_subbrick is not None:
        cargs.extend(["-grid_subbrick", str(grid_subbrick)])
    if sv is not None:
        cargs.extend(["-sv", execution.input_file(sv)])
    if one_node is not None:
        cargs.extend(["-one_node", one_node])
    cargs.extend(["-closest_nodes", execution.input_file(closest_nodes)])
    if qual is not None:
        cargs.extend(["-qual", qual])
    if lpi:
        cargs.append("-LPI")
    if rai:
        cargs.append("-RAI")
    if verb_level is not None:
        cargs.extend(["-verb", str(verb_level)])
    cargs.extend(["-prefix", prefix])
    ret = Surf2VolCoordOutputs(
        root=execution.output_file("."),
        results_file=execution.output_file(f"{prefix}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF2_VOL_COORD_METADATA",
    "Surf2VolCoordOutputs",
    "surf2_vol_coord",
]
