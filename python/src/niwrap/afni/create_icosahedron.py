# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CREATE_ICOSAHEDRON_METADATA = Metadata(
    id="440fcdd002e5d641735eb6701121c23d5ac7b544",
    name="CreateIcosahedron",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CreateIcosahedronOutputs(typing.NamedTuple):
    """
    Output object returned when calling `create_icosahedron(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def create_icosahedron(
    rad: float | int | None = None,
    rec_depth: float | int | None = None,
    lin_depth: float | int | None = None,
    min_nodes: float | int | None = None,
    nums: bool = False,
    nums_quiet: bool = False,
    center_coordinates: list[float | int] | None = None,
    to_sphere: bool = False,
    output_prefix: str | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> CreateIcosahedronOutputs:
    """
    CreateIcosahedron by AFNI Team.
    
    Tool to create an icosahedron with optional tessellation.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/CreateIcosahedron.html
    
    Args:
        rad: Size of icosahedron.
        rec_depth: Recursive tessellation depth for icosahedron.
        lin_depth: Number of edge divides for linear icosahedron tessellation.
        min_nodes: Automatically select the -ld value which produces an\
            icosahedron of at least MIN_NODES nodes.
        nums: Output the number of nodes (vertices), triangles, edges, total\
            volume, and total area then quit.
        nums_quiet: Output numbers in a less verbose manner.
        center_coordinates: Coordinates of the center of the icosahedron.
        to_sphere: Project nodes to sphere.
        output_prefix: Prefix for output files.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CreateIcosahedronOutputs`).
    """
    runner = runner or get_global_runner()
    if center_coordinates is not None and (len(center_coordinates) != 3): 
        raise ValueError(f"Length of 'center_coordinates' must be 3 but was {len(center_coordinates)}")
    execution = runner.start_execution(CREATE_ICOSAHEDRON_METADATA)
    cargs = []
    cargs.append("CreateIcosahedron")
    cargs.append("[-rad")
    cargs.append("r]")
    cargs.append("[-rd")
    cargs.append("recDepth]")
    cargs.append("[-ld")
    cargs.append("linDepth]")
    cargs.append("[-ctr")
    cargs.append("ctr]")
    cargs.append("[-prefix")
    cargs.append("fout]")
    cargs.append("[-min_nodes")
    cargs.append("MIN_NODES]")
    cargs.append("[-nums]")
    cargs.append("[-nums_quiet]")
    cargs.append("[-tosphere]")
    cargs.append("[-help]")
    ret = CreateIcosahedronOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CREATE_ICOSAHEDRON_METADATA",
    "CreateIcosahedronOutputs",
    "create_icosahedron",
]
