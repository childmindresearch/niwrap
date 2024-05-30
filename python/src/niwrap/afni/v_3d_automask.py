# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


V_3D_AUTOMASK_METADATA = Metadata(
    id="5d88af61e27409727aa79d7a3803347975b4abb1",
    name="3dAutomask",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dAutomaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_automask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    brain_file: OutputPathType
    """Output file from 3dautomask."""
    out_file: OutputPathType
    """Output image file name."""
    brain_file_: OutputPathType
    """Brain file (skull stripped)."""
    out_file_: OutputPathType
    """Mask file."""


def v_3d_automask(
    in_file: InputPathType,
    clfrac: float | int | None = None,
    dilate: int | None = None,
    erode: int | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    runner: Runner = None,
) -> V3dAutomaskOutputs:
    """
    3dAutomask by Nipype (interface).
    
    Create a brain-only mask of the image using AFNI 3dAutomask command.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dAutomask.html
    
    Args:
        in_file: Input file to 3dautomask.
        clfrac: Sets the clip level fraction (must be 0.1-0.9). a small value
            will tend to make the mask larger [default = 0.5].
        dilate: Dilate the mask outwards.
        erode: Erode the mask inwards.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dAutomaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AUTOMASK_METADATA)
    cargs = []
    cargs.append("3dAutomask")
    cargs.append(execution.input_file(in_file))
    cargs.append("[BRAIN_FILE]")
    if clfrac is not None:
        cargs.extend(["-clfrac", str(clfrac)])
    if dilate is not None:
        cargs.extend(["-dilate", str(dilate)])
    if erode is not None:
        cargs.extend(["-erode", str(erode)])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dAutomaskOutputs(
        root=execution.output_file("."),
        brain_file=execution.output_file(f"{pathlib.Path(in_file).name}_masked", optional=True),
        out_file=execution.output_file(f"{pathlib.Path(in_file).name}_mask", optional=True),
        brain_file_=execution.output_file(f"brain_file", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAutomaskOutputs",
    "V_3D_AUTOMASK_METADATA",
    "v_3d_automask",
]
