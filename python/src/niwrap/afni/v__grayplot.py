# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__GRAYPLOT_METADATA = Metadata(
    id="2d8af8df845fbb60cb7c112562424a57ea883df7",
    name="@grayplot",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VGrayplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__grayplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    grayplot_img: OutputPathType
    """Output grayplot image"""


def v__grayplot(
    dirname: str,
    pvorder: bool = False,
    peelorder: bool = False,
    ijkorder: bool = False,
    allorder: bool = False,
    runner: Runner | None = None,
) -> VGrayplotOutputs:
    """
    @grayplot by AFNI Team.
    
    Script to read files from an afni_proc.py results directory and produce a
    grayplot from the errts dataset(s), combined with a motion magnitude
    indicator graph.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@grayplot.html
    
    Args:
        dirname: Directory containing afni_proc.py results.
        pvorder: Within each partition, voxels are ordered by a simple\
            similarity measure.
        peelorder: Within each partition, voxels are ordered by how many 'peel'\
            operations are needed to reach a given voxel.
        ijkorder: Within each partition, voxels are ordered by the 3D index in\
            which they appear in the dataset.
        allorder: Create grayplots for all ordering methods.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGrayplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GRAYPLOT_METADATA)
    cargs = []
    cargs.append("@grayplot")
    cargs.append(dirname)
    if allorder:
        cargs.append("-ALLorder")
    ret = VGrayplotOutputs(
        root=execution.output_file("."),
        grayplot_img=execution.output_file(f"Grayplot.errts.*.png", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VGrayplotOutputs",
    "V__GRAYPLOT_METADATA",
    "v__grayplot",
]
