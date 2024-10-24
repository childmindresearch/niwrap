# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_BANDPASS_METADATA = Metadata(
    id="69b4e08ff33a85a01f56df929195839c7c7f9208.boutiques",
    name="1dBandpass",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dBandpassOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_bandpass(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_bandpass(
    fbot: float,
    ftop: float,
    infile: InputPathType,
    timestep: float | None = None,
    ortfile: InputPathType | None = None,
    nodetrend: bool = False,
    norm: bool = False,
    runner: Runner | None = None,
) -> V1dBandpassOutputs:
    """
    Bandpass filtering of time series data in AFNI *.1D files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        fbot: Lowest frequency in the passband, in Hz (must be greater than or\
            equal to 0).
        ftop: Highest frequency in the passband, in Hz (must be greater than\
            FBOT).
        infile: Input AFNI *.1D file; each column is processed.
        timestep: Set time step to 'dd' sec (default is 1.0).
        ortfile: Also orthogonalize input to columns in specified *.1D file\
            (only one '-ort' option is allowed).
        nodetrend: Skip the quadratic detrending of the input.
        norm: Make output time series have L2 norm = 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dBandpassOutputs`).
    """
    if not (0 <= fbot): 
        raise ValueError(f"'fbot' must be greater than 0 <= x but was {fbot}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_BANDPASS_METADATA)
    cargs = []
    cargs.append("1dBandpass")
    cargs.append(str(fbot))
    cargs.append(str(ftop))
    cargs.append(execution.input_file(infile))
    if timestep is not None:
        cargs.extend([
            "-dt",
            str(timestep)
        ])
    if ortfile is not None:
        cargs.extend([
            "-ort",
            execution.input_file(ortfile)
        ])
    if nodetrend:
        cargs.append("-nodetrend")
    if norm:
        cargs.append("-norm")
    ret = V1dBandpassOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dBandpassOutputs",
    "V_1D_BANDPASS_METADATA",
    "v_1d_bandpass",
]
