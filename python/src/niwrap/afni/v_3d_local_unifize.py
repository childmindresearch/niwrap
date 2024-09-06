# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_LOCAL_UNIFIZE_METADATA = Metadata(
    id="174d5353a164f29ddb062909ba372afebd8f20ce",
    name="3dLocalUnifize",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dLocalUnifizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_unifize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset file"""


def v_3d_local_unifize(
    input_: InputPathType,
    output: str,
    working_dir: str | None = None,
    echo: bool = False,
    no_clean: bool = False,
    local_rad: float | int | None = None,
    local_perc: float | int | None = None,
    local_mask: str | None = None,
    filter_thr: float | int | None = None,
    runner: Runner | None = None,
) -> V3dLocalUnifizeOutputs:
    """
    3dLocalUnifize by AFNI Team.
    
    This program generates a 'unifized' output volume by estimating the median
    in the local neighborhood of each voxel and using that to scale each voxel's
    brightness.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLocalUnifize.html
    
    Args:
        input_: Input dataset.
        output: Output dataset name, including path.
        working_dir: Name of temporary working directory (def:\
            __wdir_LocalUni_, plus a random alphanumeric str).
        echo: Run this program very verbosely (default: false).
        no_clean: Do not remove the working directory (default: remove it).
        local_rad: The spherical neighborhood's radius for the 3dLocalStat step\
            (default: -3).
        local_perc: The percentile used in the 3dLocalStat step, generating the\
            scaling volume (default: 50).
        local_mask: Provide the masking option for the 3dLocalStat step; to\
            remove any masking, put 'None' as the option value (default:\
            "-automask").
        filter_thr: Ceiling on values in the final, scaled dataset; values <=0\
            turn off this final filtering (default: 1.5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalUnifizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_UNIFIZE_METADATA)
    cargs = []
    cargs.append("3dLocalUnifize")
    cargs.append(execution.input_file(input_))
    cargs.extend(["-prefix", output])
    if working_dir is not None:
        cargs.extend(["-wdir_name", working_dir])
    if echo:
        cargs.append("-echo")
    if no_clean:
        cargs.append("-no_clean")
    if local_rad is not None:
        cargs.extend(["-local_rad", str(local_rad)])
    if local_perc is not None:
        cargs.extend(["-local_perc", str(local_perc)])
    if local_mask is not None:
        cargs.extend(["-local_mask", local_mask])
    if filter_thr is not None:
        cargs.extend(["-filter_thr", str(filter_thr)])
    ret = V3dLocalUnifizeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLocalUnifizeOutputs",
    "V_3D_LOCAL_UNIFIZE_METADATA",
    "v_3d_local_unifize",
]