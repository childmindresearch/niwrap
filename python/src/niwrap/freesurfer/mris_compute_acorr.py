# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_COMPUTE_ACORR_METADATA = Metadata(
    id="c87ef9e1a360bff02be52c7cd358fb4259d79971.boutiques",
    name="mris_compute_acorr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisComputeAcorrParameters = typing.TypedDict('MrisComputeAcorrParameters', {
    "__STYX_TYPE__": typing.Literal["mris_compute_acorr"],
    "output_subject": str,
    "hemi": str,
    "surf": InputPathType,
    "curv": InputPathType,
    "c1_subjects": list[str],
    "c2_subjects": list[str],
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
        "mris_compute_acorr": mris_compute_acorr_cargs,
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
    vt = {}
    return vt.get(t)


class MrisComputeAcorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_acorr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_compute_acorr_params(
    output_subject: str,
    hemi: str,
    surf: InputPathType,
    curv: InputPathType,
    c1_subjects: list[str],
    c2_subjects: list[str],
) -> MrisComputeAcorrParameters:
    """
    Build parameters.
    
    Args:
        output_subject: The output subject file.
        hemi: Specify the hemisphere for processing.
        surf: The surface file which must be a spherical surface suitable for\
            computing geodesics.
        curv: The input curvature file.
        c1_subjects: List of subjects from one class.
        c2_subjects: List of subjects from another class.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_compute_acorr",
        "output_subject": output_subject,
        "hemi": hemi,
        "surf": surf,
        "curv": curv,
        "c1_subjects": c1_subjects,
        "c2_subjects": c2_subjects,
    }
    return params


def mris_compute_acorr_cargs(
    params: MrisComputeAcorrParameters,
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
    cargs.append("mris_compute_acorr")
    cargs.extend([
        "-o",
        params.get("output_subject")
    ])
    cargs.append(params.get("hemi"))
    cargs.append(execution.input_file(params.get("surf")))
    cargs.append(execution.input_file(params.get("curv")))
    cargs.extend(params.get("c1_subjects"))
    cargs.extend(params.get("c2_subjects"))
    return cargs


def mris_compute_acorr_outputs(
    params: MrisComputeAcorrParameters,
    execution: Execution,
) -> MrisComputeAcorrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisComputeAcorrOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_compute_acorr_execute(
    params: MrisComputeAcorrParameters,
    execution: Execution,
) -> MrisComputeAcorrOutputs:
    """
    Compute the autocorrelation function of a curvature file on a spherical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisComputeAcorrOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_compute_acorr_cargs(params, execution)
    ret = mris_compute_acorr_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_compute_acorr(
    output_subject: str,
    hemi: str,
    surf: InputPathType,
    curv: InputPathType,
    c1_subjects: list[str],
    c2_subjects: list[str],
    runner: Runner | None = None,
) -> MrisComputeAcorrOutputs:
    """
    Compute the autocorrelation function of a curvature file on a spherical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_subject: The output subject file.
        hemi: Specify the hemisphere for processing.
        surf: The surface file which must be a spherical surface suitable for\
            computing geodesics.
        curv: The input curvature file.
        c1_subjects: List of subjects from one class.
        c2_subjects: List of subjects from another class.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeAcorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_ACORR_METADATA)
    params = mris_compute_acorr_params(output_subject=output_subject, hemi=hemi, surf=surf, curv=curv, c1_subjects=c1_subjects, c2_subjects=c2_subjects)
    return mris_compute_acorr_execute(params, execution)


__all__ = [
    "MRIS_COMPUTE_ACORR_METADATA",
    "MrisComputeAcorrOutputs",
    "mris_compute_acorr",
    "mris_compute_acorr_params",
]
