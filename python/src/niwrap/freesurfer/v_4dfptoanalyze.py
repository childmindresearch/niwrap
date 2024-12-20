# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_4DFPTOANALYZE_METADATA = Metadata(
    id="65cd83dce834e4e472f7fa7af8e2201dfe71e3b3.boutiques",
    name="4dfptoanalyze",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class V4dfptoanalyzeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_4dfptoanalyze(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    analyze_hdr: OutputPathType
    """Header file of Analyze format output"""
    analyze_img: OutputPathType
    """Image file of Analyze format output"""


def v_4dfptoanalyze(
    input_file: InputPathType,
    scale_factor: float | None = None,
    output_8bit: bool = False,
    spm99: bool = False,
    endianness: str | None = None,
    runner: Runner | None = None,
) -> V4dfptoanalyzeOutputs:
    """
    Converts 4dfp formatted files to Analyze format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input 4dfp filename.
        scale_factor: Scale output values by specified factor.
        output_8bit: Output 8 bit unsigned char.
        spm99: Include origin and scale in hdr.
        endianness: Output big or little endian (default CPU endian).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V4dfptoanalyzeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_4DFPTOANALYZE_METADATA)
    cargs = []
    cargs.append("4dfptoanalyze")
    cargs.append(execution.input_file(input_file))
    if scale_factor is not None:
        cargs.extend([
            "-c",
            str(scale_factor)
        ])
    if output_8bit:
        cargs.append("-8")
    if spm99:
        cargs.append("-SPM99")
    if endianness is not None:
        cargs.extend([
            "-@",
            endianness
        ])
    ret = V4dfptoanalyzeOutputs(
        root=execution.output_file("."),
        analyze_hdr=execution.output_file(pathlib.Path(input_file).name + "_analyze.hdr"),
        analyze_img=execution.output_file(pathlib.Path(input_file).name + "_analyze.img"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V4dfptoanalyzeOutputs",
    "V_4DFPTOANALYZE_METADATA",
    "v_4dfptoanalyze",
]
