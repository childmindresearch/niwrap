# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DFRACTIONIZE_METADATA = Metadata(
    id="37f58eec13c830ca996027ca9751f46805708e60",
    name="3dfractionize",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dfractionizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dfractionize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType | None
    """Output dataset with the specified prefix."""


def v_3dfractionize(
    template: InputPathType,
    input_: InputPathType,
    prefix: str | None = None,
    clip: float | int | None = None,
    warp: InputPathType | None = None,
    preserve: bool = False,
    vote: bool = False,
    runner: Runner | None = None,
) -> V3dfractionizeOutputs:
    """
    3dfractionize by AFNI Team.
    
    For each voxel in the output dataset, computes the fraction of it that is
    occupied by nonzero voxels from the input.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dfractionize.html
    
    Args:
        template: Use dataset as a template for the output. The output dataset\
            will be on the same grid as this dataset.
        input_: Use dataset for the input. Only the sub-brick #0 of the input\
            is used.
        prefix: Prefix for the output dataset.
        clip: Clip off voxels that are less than the specified occupancy\
            fraction.
        warp: Dataset that provides a transformation (warp) from +orig\
            coordinates to the coordinates of the input dataset.
        preserve: Preserve the nonzero values of input voxels in the output\
            dataset rather than creating a fractional mask.
        vote: Vote for which input value to preserve when using the preserve\
            flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dfractionizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DFRACTIONIZE_METADATA)
    cargs = []
    cargs.append("3dfractionize")
    cargs.extend(["-template", execution.input_file(template)])
    cargs.extend(["-input", execution.input_file(input_)])
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if clip is not None:
        cargs.extend(["-clip", str(clip)])
    if warp is not None:
        cargs.extend(["-warp", execution.input_file(warp)])
    if preserve:
        cargs.append("-preserve")
    if vote:
        cargs.append("-vote")
    ret = V3dfractionizeOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{prefix}") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dfractionizeOutputs",
    "V_3DFRACTIONIZE_METADATA",
    "v_3dfractionize",
]
