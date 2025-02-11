# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1D_BANDPASS_METADATA = Metadata(
    id="69b4e08ff33a85a01f56df929195839c7c7f9208.boutiques",
    name="1dBandpass",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dBandpassParameters = typing.TypedDict('V1dBandpassParameters', {
    "__STYX_TYPE__": typing.Literal["1dBandpass"],
    "fbot": float,
    "ftop": float,
    "infile": InputPathType,
    "timestep": typing.NotRequired[float | None],
    "ortfile": typing.NotRequired[InputPathType | None],
    "nodetrend": bool,
    "norm": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "1dBandpass": v_1d_bandpass_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class V1dBandpassOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_bandpass(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_bandpass_params(
    fbot: float,
    ftop: float,
    infile: InputPathType,
    timestep: float | None = None,
    ortfile: InputPathType | None = None,
    nodetrend: bool = False,
    norm: bool = False,
) -> V1dBandpassParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dBandpass",
        "fbot": fbot,
        "ftop": ftop,
        "infile": infile,
        "nodetrend": nodetrend,
        "norm": norm,
    }
    if timestep is not None:
        params["timestep"] = timestep
    if ortfile is not None:
        params["ortfile"] = ortfile
    return params


def v_1d_bandpass_cargs(
    params: V1dBandpassParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("1dBandpass")
    cargs.append(str(params.get("fbot")))
    cargs.append(str(params.get("ftop")))
    cargs.append(execution.input_file(params.get("infile")))
    if params.get("timestep") is not None:
        cargs.extend([
            "-dt",
            str(params.get("timestep"))
        ])
    if params.get("ortfile") is not None:
        cargs.extend([
            "-ort",
            execution.input_file(params.get("ortfile"))
        ])
    if params.get("nodetrend"):
        cargs.append("-nodetrend")
    if params.get("norm"):
        cargs.append("-norm")
    return cargs


def v_1d_bandpass_outputs(
    params: V1dBandpassParameters,
    execution: Execution,
) -> V1dBandpassOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dBandpassOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_1d_bandpass_execute(
    params: V1dBandpassParameters,
    execution: Execution,
) -> V1dBandpassOutputs:
    """
    Bandpass filtering of time series data in AFNI *.1D files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dBandpassOutputs`).
    """
    cargs = v_1d_bandpass_cargs(params, execution)
    ret = v_1d_bandpass_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_BANDPASS_METADATA)
    params = v_1d_bandpass_params(fbot=fbot, ftop=ftop, infile=infile, timestep=timestep, ortfile=ortfile, nodetrend=nodetrend, norm=norm)
    return v_1d_bandpass_execute(params, execution)


__all__ = [
    "V1dBandpassOutputs",
    "V1dBandpassParameters",
    "V_1D_BANDPASS_METADATA",
    "v_1d_bandpass",
    "v_1d_bandpass_params",
]
