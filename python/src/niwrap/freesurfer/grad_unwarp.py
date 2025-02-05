# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GRAD_UNWARP_METADATA = Metadata(
    id="3f8f59f71178da3b91ee74fc055a9520bba22b05.boutiques",
    name="grad_unwarp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
GradUnwarpParameters = typing.TypedDict('GradUnwarpParameters', {
    "__STYX_TYPE__": typing.Literal["grad_unwarp"],
    "infile": InputPathType,
    "seriesno": typing.NotRequired[str | None],
    "unwarp_type": typing.NotRequired[str | None],
    "nojac": bool,
    "corfov": bool,
    "cor": bool,
    "interp": typing.NotRequired[str | None],
    "outfile": str,
    "matlab_binary": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "grad_unwarp": grad_unwarp_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "grad_unwarp": grad_unwarp_outputs,
    }
    return vt.get(t)


class GradUnwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `grad_unwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mgh_output: OutputPathType
    """Output file in MGH format"""
    cor_output: OutputPathType
    """Output directory in COR format"""


def grad_unwarp_params(
    infile: InputPathType,
    outfile: str,
    seriesno: str | None = None,
    unwarp_type: str | None = None,
    nojac: bool = False,
    corfov: bool = False,
    cor: bool = False,
    interp: str | None = None,
    matlab_binary: str | None = "/space/lyon/6/pubsw/common/matlab/6.5/bin/matlab",
) -> GradUnwarpParameters:
    """
    Build parameters.
    
    Args:
        infile: Input file or directory (dcmfile, dcmdir, or mghfile).
        outfile: Output file in MGH format.
        seriesno: DICOM series number, required if input is a directory.
        unwarp_type: Gradient unwarping displacement type or map file (required\
            for MGH file).
        nojac: Do not perform jacobian correction when unwarping.
        corfov: Resample to Coronal FOV.
        cor: Output in COR format instead of MGH.
        interp: Interpolation method (cubic, linear, nearest, spline).
        matlab_binary: Path to the Matlab binary, version 6.5 or higher\
            required.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "grad_unwarp",
        "infile": infile,
        "nojac": nojac,
        "corfov": corfov,
        "cor": cor,
        "outfile": outfile,
    }
    if seriesno is not None:
        params["seriesno"] = seriesno
    if unwarp_type is not None:
        params["unwarp_type"] = unwarp_type
    if interp is not None:
        params["interp"] = interp
    if matlab_binary is not None:
        params["matlab_binary"] = matlab_binary
    return params


def grad_unwarp_cargs(
    params: GradUnwarpParameters,
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
    cargs.append("grad_unwarp")
    cargs.append(execution.input_file(params.get("infile")))
    if params.get("seriesno") is not None:
        cargs.extend([
            "-s",
            params.get("seriesno")
        ])
    if params.get("unwarp_type") is not None:
        cargs.extend([
            "-unwarp",
            params.get("unwarp_type")
        ])
    if params.get("nojac"):
        cargs.append("-nojac")
    if params.get("corfov"):
        cargs.append("-corfov")
    if params.get("cor"):
        cargs.append("-cor")
    if params.get("interp") is not None:
        cargs.extend([
            "-interp",
            params.get("interp")
        ])
    cargs.extend([
        "-o",
        params.get("outfile")
    ])
    if params.get("matlab_binary") is not None:
        cargs.extend([
            "-matlab",
            params.get("matlab_binary")
        ])
    return cargs


def grad_unwarp_outputs(
    params: GradUnwarpParameters,
    execution: Execution,
) -> GradUnwarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GradUnwarpOutputs(
        root=execution.output_file("."),
        mgh_output=execution.output_file(params.get("outfile")),
        cor_output=execution.output_file(params.get("outfile") + "/"),
    )
    return ret


def grad_unwarp_execute(
    params: GradUnwarpParameters,
    execution: Execution,
) -> GradUnwarpOutputs:
    """
    Convert, dewarp, and resample DICOM files to MGH files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GradUnwarpOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = grad_unwarp_cargs(params, execution)
    ret = grad_unwarp_outputs(params, execution)
    execution.run(cargs)
    return ret


def grad_unwarp(
    infile: InputPathType,
    outfile: str,
    seriesno: str | None = None,
    unwarp_type: str | None = None,
    nojac: bool = False,
    corfov: bool = False,
    cor: bool = False,
    interp: str | None = None,
    matlab_binary: str | None = "/space/lyon/6/pubsw/common/matlab/6.5/bin/matlab",
    runner: Runner | None = None,
) -> GradUnwarpOutputs:
    """
    Convert, dewarp, and resample DICOM files to MGH files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input file or directory (dcmfile, dcmdir, or mghfile).
        outfile: Output file in MGH format.
        seriesno: DICOM series number, required if input is a directory.
        unwarp_type: Gradient unwarping displacement type or map file (required\
            for MGH file).
        nojac: Do not perform jacobian correction when unwarping.
        corfov: Resample to Coronal FOV.
        cor: Output in COR format instead of MGH.
        interp: Interpolation method (cubic, linear, nearest, spline).
        matlab_binary: Path to the Matlab binary, version 6.5 or higher\
            required.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GradUnwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GRAD_UNWARP_METADATA)
    params = grad_unwarp_params(infile=infile, seriesno=seriesno, unwarp_type=unwarp_type, nojac=nojac, corfov=corfov, cor=cor, interp=interp, outfile=outfile, matlab_binary=matlab_binary)
    return grad_unwarp_execute(params, execution)


__all__ = [
    "GRAD_UNWARP_METADATA",
    "GradUnwarpOutputs",
    "GradUnwarpParameters",
    "grad_unwarp",
    "grad_unwarp_params",
]
