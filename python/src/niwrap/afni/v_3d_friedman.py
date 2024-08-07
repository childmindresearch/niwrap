# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_FRIEDMAN_METADATA = Metadata(
    id="b85c7f2e9a9d31f06fb2e61a2f2545d5a4481dab",
    name="3dFriedman",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dFriedmanOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_friedman(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Friedman statistics output file"""


def v_3d_friedman(
    levels: int,
    datasets: list[InputPathType],
    output_prefix: str,
    workmem: int | None = None,
    voxel_num: int | None = None,
    runner: Runner | None = None,
) -> V3dFriedmanOutputs:
    """
    3dFriedman by AFNI Team.
    
    Performs nonparametric Friedman test for randomized complete block design
    experiments.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dFriedman.html
    
    Args:
        levels: Number of treatments.
        datasets: Data sets for each treatment.
        output_prefix: Prefix for the output files.
        workmem: Number of megabytes of RAM to use for statistical workspace.
        voxel_num: Screen output for a specific voxel number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dFriedmanOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_FRIEDMAN_METADATA)
    cargs = []
    cargs.append("3dFriedman")
    cargs.append(str(levels))
    cargs.extend(["-dset", *[execution.input_file(f) for f in datasets]])
    if workmem is not None:
        cargs.extend(["-workmem", str(workmem)])
    if voxel_num is not None:
        cargs.extend(["-voxel", str(voxel_num)])
    cargs.extend(["-out", output_prefix])
    ret = V3dFriedmanOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output_prefix}*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dFriedmanOutputs",
    "V_3D_FRIEDMAN_METADATA",
    "v_3d_friedman",
]
