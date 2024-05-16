# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.915522

import typing

from ..styxdefs import *


CONVERT_WARPFIELD_METADATA = Metadata(
    id="c52b74c68834b7085df657b39a11e01443141aef",
    name="convert-warpfield",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class ConvertWarpfieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_warpfield(...)`.
    """


def convert_warpfield(
    runner: Runner,
    opt_from_world_input: str | None = None,
    opt_from_itk_input: str | None = None,
    opt_to_world_output: str | None = None,
    opt_to_itk_output: str | None = None,
) -> ConvertWarpfieldOutputs:
    """
    CONVERT A WARPFIELD BETWEEN CONVENTIONS.
    
    NIFTI world warpfields can be used directly on mm coordinates via sampling
    the three subvolumes at the coordinate and adding the sampled values to the
    coordinate vector. They use the NIFTI coordinate system, that is, X is left
    to right, Y is posterior to anterior, and Z is inferior to superior.
    
    NOTE: this command does not invert the warpfield, and to warp a surface, you
    must use the inverse of the warpfield that warps the corresponding volume.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-fnirt may be specified more than once.
    
    Args:
        runner: Command runner
        opt_from_world_input: input is a NIFTI 'world' warpfield: the input
            warpfield
        opt_from_itk_input: input is an ITK warpfield: the input warpfield
        opt_to_world_output: write output as a NIFTI 'world' warpfield: output -
            the output warpfield
        opt_to_itk_output: write output as an ITK warpfield: output - the output
            warpfield
    Returns:
        NamedTuple of outputs (described in `ConvertWarpfieldOutputs`).
    """
    execution = runner.start_execution(CONVERT_WARPFIELD_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-warpfield")
    if opt_from_world_input is not None:
        cargs.extend(["-from-world", opt_from_world_input])
    if opt_from_itk_input is not None:
        cargs.extend(["-from-itk", opt_from_itk_input])
    if opt_to_world_output is not None:
        cargs.extend(["-to-world", opt_to_world_output])
    if opt_to_itk_output is not None:
        cargs.extend(["-to-itk", opt_to_itk_output])
    ret = ConvertWarpfieldOutputs(
    )
    execution.run(cargs)
    return ret
