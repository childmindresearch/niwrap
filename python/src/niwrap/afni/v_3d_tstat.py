# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_TSTAT_METADATA = Metadata(
    id="9de91f7f4abdac70f81125d00379ae3754addf88",
    name="3dTstat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_tstat(
    in_file: InputPathType,
    mask: InputPathType | None = None,
    num_threads: int | None = None,
    options: str | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    runner: Runner | None = None,
) -> V3dTstatOutputs:
    """
    3dTstat by AFNI Team.
    
    Compute voxel-wise statistics using AFNI 3dTstat command.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTstat.html
    
    Args:
        in_file: Input file to 3dtstat.
        mask: Mask file.
        num_threads: Set number of threads.
        options: Selected statistical output.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TSTAT_METADATA)
    cargs = []
    cargs.append("3dTstat")
    cargs.append(execution.input_file(in_file))
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if options is not None:
        cargs.append(options)
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dTstatOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).name}_tstat", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTstatOutputs",
    "V_3D_TSTAT_METADATA",
    "v_3d_tstat",
]
