# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_LOCAL_HISTOG_METADATA = Metadata(
    id="b660a7fce0314f96af48dc779a9f19beae27f400",
    name="3dLocalHistog",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dLocalHistogOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_histog(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_head: OutputPathType
    """The output dataset with the specified prefix"""
    output_dataset_brik: OutputPathType
    """The output dataset with the specified prefix"""
    histogram_file: OutputPathType | None
    """The overall histogram saved into the specified file"""


def v_3d_local_histog(
    input_datasets: list[InputPathType],
    prefix: str,
    nbhd_option: str | None = None,
    hsave: str | None = None,
    lab_file: InputPathType | None = None,
    exclude: list[str] | None = None,
    exc_nonlab: bool = False,
    mincount: float | int | None = None,
    probability: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dLocalHistogOutputs:
    """
    3dLocalHistog by AFNI Team.
    
    This program computes a local histogram at each voxel in the input datasets.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLocalHistog.html
    
    Args:
        input_datasets: Input dataset(s) for the 3dLocalHistog tool.
        prefix: Use string 'ppp' as the prefix for the output dataset.
        nbhd_option: Defines the region around each voxel to be used for the\
            statistics calculation. Available formats: 'SPHERE(r)', 'RECT(a,b,c)',\
            'RHDD(a)', 'TOHD(a)'.
        hsave: Save the overall histogram into file 'sss'. This file will have\
            2 columns: value and count.
        lab_file: Use file 'LL' as a label file.
        exclude: Exclude values from 'a' to 'b' from the counting. This option\
            can be used more than once.
        exc_nonlab: If '-lab_file' is used, then exclude all values that are\
            NOT in the label file (except for 0).
        mincount: Exclude values which appear in the overall histogram fewer\
            than 'mm' times.
        probability: Convert each count to a probability by dividing by the\
            total number of counts at each voxel.
        quiet: Stop the highly informative progress reports.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalHistogOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_HISTOG_METADATA)
    cargs = []
    cargs.append("3dLocalHistog")
    if nbhd_option is not None:
        cargs.extend(["-nbhd", nbhd_option])
    cargs.append("-prefix")
    cargs.extend(["-prefix", prefix])
    if hsave is not None:
        cargs.extend(["-hsave", hsave])
    if lab_file is not None:
        cargs.extend(["-lab_file", execution.input_file(lab_file)])
    if exclude is not None:
        cargs.extend(["-exclude", *exclude])
    if mincount is not None:
        cargs.extend(["-mincount", str(mincount)])
    cargs.extend([execution.input_file(f) for f in input_datasets])
    ret = V3dLocalHistogOutputs(
        root=execution.output_file("."),
        output_dataset_head=execution.output_file(f"{prefix}+orig.HEAD"),
        output_dataset_brik=execution.output_file(f"{prefix}+orig.BRIK"),
        histogram_file=execution.output_file(f"{hsave}", optional=True) if hsave is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLocalHistogOutputs",
    "V_3D_LOCAL_HISTOG_METADATA",
    "v_3d_local_histog",
]
