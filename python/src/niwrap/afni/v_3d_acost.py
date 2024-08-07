# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ALLINEATE_METADATA = Metadata(
    id="7c35d8a9c0b16fa42accd6769557ff7f8ddf4d29",
    name="3dAllineate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dAllineateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_allineate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType
    """Output aligned dataset (HEAD file)"""
    output_brik: OutputPathType
    """Output aligned dataset (BRIK file)"""


def v_3d_allineate(
    infile: InputPathType,
    basefile: InputPathType,
    outfile: str,
    all_cost: bool = False,
    runner: Runner | None = None,
) -> V3dAllineateOutputs:
    """
    3dAllineate by AFNI Team.
    
    Allineate dataset to a base dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dAcost.html
    
    Args:
        infile: Input dataset for allineation.
        basefile: Base dataset for allineation.
        outfile: Prefix for the output dataset.
        all_cost: Prints all alignment cost metrics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAllineateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ALLINEATE_METADATA)
    cargs = []
    cargs.append("3dAllineate")
    cargs.append(execution.input_file(infile))
    cargs.append("-base")
    cargs.extend(["-base", execution.input_file(basefile)])
    cargs.append("-prefix")
    cargs.extend(["-prefix", outfile])
    cargs.append("[OTHER_OPTIONS]")
    ret = V3dAllineateOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(f"{outfile}+orig.HEAD"),
        output_brik=execution.output_file(f"{outfile}+orig.BRIK"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAllineateOutputs",
    "V_3D_ALLINEATE_METADATA",
    "v_3d_allineate",
]
