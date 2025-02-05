# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ASEGSTATSDIFF_METADATA = Metadata(
    id="10487227e273c61c9beadcb9b38d15804d6724e3.boutiques",
    name="asegstatsdiff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
AsegstatsdiffParameters = typing.TypedDict('AsegstatsdiffParameters', {
    "__STYX_TYPE__": typing.Literal["asegstatsdiff"],
    "subject1": str,
    "subject2": str,
    "outdir": typing.NotRequired[str | None],
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
        "asegstatsdiff": asegstatsdiff_cargs,
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
        "asegstatsdiff": asegstatsdiff_outputs,
    }
    return vt.get(t)


class AsegstatsdiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `asegstatsdiff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    asegstats_output: OutputPathType | None
    """Output table with percent differences added."""


def asegstatsdiff_params(
    subject1: str,
    subject2: str,
    outdir: str | None = None,
) -> AsegstatsdiffParameters:
    """
    Build parameters.
    
    Args:
        subject1: The first subject to be compared.
        subject2: The second subject to be compared.
        outdir: Optionally specify a directory to write the output\
            asegstats.txt.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "asegstatsdiff",
        "subject1": subject1,
        "subject2": subject2,
    }
    if outdir is not None:
        params["outdir"] = outdir
    return params


def asegstatsdiff_cargs(
    params: AsegstatsdiffParameters,
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
    cargs.append("asegstatsdiff")
    cargs.append(params.get("subject1"))
    if params.get("outdir") is not None:
        cargs.append(params.get("subject2") + params.get("outdir"))
    return cargs


def asegstatsdiff_outputs(
    params: AsegstatsdiffParameters,
    execution: Execution,
) -> AsegstatsdiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AsegstatsdiffOutputs(
        root=execution.output_file("."),
        asegstats_output=execution.output_file(params.get("outdir") + "/asegstats.txt") if (params.get("outdir") is not None) else None,
    )
    return ret


def asegstatsdiff_execute(
    params: AsegstatsdiffParameters,
    execution: Execution,
) -> AsegstatsdiffOutputs:
    """
    Compute and report percentage differences in aseg morphometry data between two
    subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AsegstatsdiffOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = asegstatsdiff_cargs(params, execution)
    ret = asegstatsdiff_outputs(params, execution)
    execution.run(cargs)
    return ret


def asegstatsdiff(
    subject1: str,
    subject2: str,
    outdir: str | None = None,
    runner: Runner | None = None,
) -> AsegstatsdiffOutputs:
    """
    Compute and report percentage differences in aseg morphometry data between two
    subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject1: The first subject to be compared.
        subject2: The second subject to be compared.
        outdir: Optionally specify a directory to write the output\
            asegstats.txt.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AsegstatsdiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ASEGSTATSDIFF_METADATA)
    params = asegstatsdiff_params(subject1=subject1, subject2=subject2, outdir=outdir)
    return asegstatsdiff_execute(params, execution)


__all__ = [
    "ASEGSTATSDIFF_METADATA",
    "AsegstatsdiffOutputs",
    "AsegstatsdiffParameters",
    "asegstatsdiff",
    "asegstatsdiff_params",
]
