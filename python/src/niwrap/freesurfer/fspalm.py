# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSPALM_METADATA = Metadata(
    id="99a4d5403d2183af602919ad014d4db78cf3675b.boutiques",
    name="fspalm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FspalmParameters = typing.TypedDict('FspalmParameters', {
    "__STYX_TYPE__": typing.Literal["fspalm"],
    "glmdir": str,
    "cft": float,
    "cwp": float,
    "onetail": bool,
    "twotail": bool,
    "name": typing.NotRequired[str | None],
    "iters": typing.NotRequired[float | None],
    "monly": bool,
    "pponly": bool,
    "octave": bool,
    "centroid": bool,
    "2spaces": bool,
    "3spaces": bool,
    "pargs": typing.NotRequired[str | None],
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
        "fspalm": fspalm_cargs,
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
        "fspalm": fspalm_outputs,
    }.get(t)


class FspalmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fspalm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fspalm_params(
    glmdir: str,
    cft: float,
    cwp: float,
    onetail: bool = False,
    twotail: bool = False,
    name: str | None = None,
    iters: float | None = None,
    monly: bool = False,
    pponly: bool = False,
    octave: bool = False,
    centroid: bool = False,
    v_2spaces: bool = False,
    v_3spaces: bool = False,
    pargs: str | None = None,
) -> FspalmParameters:
    """
    Build parameters.
    
    Args:
        glmdir: The mri_glmfit directory to prepare.
        cft: Voxel-wise cluster forming threshold (CFT), -log10(p).
        cwp: Clusterwise p-value threshold.
        onetail: Perform a one-tailed test.
        twotail: Perform a two-tailed test. NOTE: changes CFT.
        name: Name of palm subdirectory (default="palm").
        iters: Number of iterations.
        monly: Only create matlab file, do not run.
        pponly: Only perform post-processing.
        octave: Run with octave, not matlab.
        centroid: Add --centroid flag to mri_surfcluster post-processing.
        v_2spaces: Bonferroni-correct for 2 spaces.
        v_3spaces: Bonferroni-correct for 3 spaces.
        pargs: Supply additional args to be passed to the palm function.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fspalm",
        "glmdir": glmdir,
        "cft": cft,
        "cwp": cwp,
        "onetail": onetail,
        "twotail": twotail,
        "monly": monly,
        "pponly": pponly,
        "octave": octave,
        "centroid": centroid,
        "2spaces": v_2spaces,
        "3spaces": v_3spaces,
    }
    if name is not None:
        params["name"] = name
    if iters is not None:
        params["iters"] = iters
    if pargs is not None:
        params["pargs"] = pargs
    return params


def fspalm_cargs(
    params: FspalmParameters,
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
    cargs.append("fspalm")
    cargs.extend([
        "--glmdir",
        params.get("glmdir")
    ])
    cargs.extend([
        "--cft",
        str(params.get("cft"))
    ])
    cargs.extend([
        "--cwp",
        str(params.get("cwp"))
    ])
    if params.get("onetail"):
        cargs.append("--onetail")
    if params.get("twotail"):
        cargs.append("--twotail")
    if params.get("name") is not None:
        cargs.extend([
            "--name",
            params.get("name")
        ])
    if params.get("iters") is not None:
        cargs.extend([
            "--iters",
            str(params.get("iters"))
        ])
    if params.get("monly"):
        cargs.append("--monly")
    if params.get("pponly"):
        cargs.append("--pponly")
    if params.get("octave"):
        cargs.append("--octave")
    if params.get("centroid"):
        cargs.append("--centroid")
    if params.get("2spaces"):
        cargs.append("--2spaces")
    if params.get("3spaces"):
        cargs.append("--3spaces")
    if params.get("pargs") is not None:
        cargs.extend([
            "--pargs",
            params.get("pargs")
        ])
    return cargs


def fspalm_outputs(
    params: FspalmParameters,
    execution: Execution,
) -> FspalmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FspalmOutputs(
        root=execution.output_file("."),
    )
    return ret


def fspalm_execute(
    params: FspalmParameters,
    execution: Execution,
) -> FspalmOutputs:
    """
    Prepares and analyzes the output of mri_glmfit for Permutation Analysis of
    Linear Models (PALM) to correct for multiple comparisons.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FspalmOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fspalm_cargs(params, execution)
    ret = fspalm_outputs(params, execution)
    execution.run(cargs)
    return ret


def fspalm(
    glmdir: str,
    cft: float,
    cwp: float,
    onetail: bool = False,
    twotail: bool = False,
    name: str | None = None,
    iters: float | None = None,
    monly: bool = False,
    pponly: bool = False,
    octave: bool = False,
    centroid: bool = False,
    v_2spaces: bool = False,
    v_3spaces: bool = False,
    pargs: str | None = None,
    runner: Runner | None = None,
) -> FspalmOutputs:
    """
    Prepares and analyzes the output of mri_glmfit for Permutation Analysis of
    Linear Models (PALM) to correct for multiple comparisons.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        glmdir: The mri_glmfit directory to prepare.
        cft: Voxel-wise cluster forming threshold (CFT), -log10(p).
        cwp: Clusterwise p-value threshold.
        onetail: Perform a one-tailed test.
        twotail: Perform a two-tailed test. NOTE: changes CFT.
        name: Name of palm subdirectory (default="palm").
        iters: Number of iterations.
        monly: Only create matlab file, do not run.
        pponly: Only perform post-processing.
        octave: Run with octave, not matlab.
        centroid: Add --centroid flag to mri_surfcluster post-processing.
        v_2spaces: Bonferroni-correct for 2 spaces.
        v_3spaces: Bonferroni-correct for 3 spaces.
        pargs: Supply additional args to be passed to the palm function.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FspalmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSPALM_METADATA)
    params = fspalm_params(glmdir=glmdir, cft=cft, cwp=cwp, onetail=onetail, twotail=twotail, name=name, iters=iters, monly=monly, pponly=pponly, octave=octave, centroid=centroid, v_2spaces=v_2spaces, v_3spaces=v_3spaces, pargs=pargs)
    return fspalm_execute(params, execution)


__all__ = [
    "FSPALM_METADATA",
    "FspalmOutputs",
    "FspalmParameters",
    "fspalm",
    "fspalm_params",
]
