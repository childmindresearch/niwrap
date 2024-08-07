# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__CENTER_DISTANCE_METADATA = Metadata(
    id="b3113fa600a410855b411750fb0391ea1c4c8404",
    name="@Center_Distance",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VCenterDistanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__center_distance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    distance_output: OutputPathType
    """The calculated distance between the centers of DSET_1 and DSET_2"""


def v__center_distance(
    dset1: InputPathType,
    dset2: InputPathType,
    runner: Runner | None = None,
) -> VCenterDistanceOutputs:
    """
    @Center_Distance by AFNI Team.
    
    Tool to calculate the distance between the centers of two datasets.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Center_Distance.html
    
    Args:
        dset1: First dataset file (e.g. file1.nii.gz).
        dset2: Second dataset file (e.g. file2.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VCenterDistanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CENTER_DISTANCE_METADATA)
    cargs = []
    cargs.append("@Center_Distance")
    cargs.append("-dset")
    cargs.append(execution.input_file(dset1))
    cargs.append(execution.input_file(dset2))
    ret = VCenterDistanceOutputs(
        root=execution.output_file("."),
        distance_output=execution.output_file(f"distance.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VCenterDistanceOutputs",
    "V__CENTER_DISTANCE_METADATA",
    "v__center_distance",
]
