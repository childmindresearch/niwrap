# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

INFLATE_SUBJECT_NEW_LH_METADATA = Metadata(
    id="08307c12a50c2ff8603980e07c1bcf6e9a16f2e1.boutiques",
    name="inflate_subject_new-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
InflateSubjectNewLhParameters = typing.TypedDict('InflateSubjectNewLhParameters', {
    "__STYX_TYPE__": typing.Literal["inflate_subject_new-lh"],
    "subject_dir": str,
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
        "inflate_subject_new-lh": inflate_subject_new_lh_cargs,
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
        "inflate_subject_new-lh": inflate_subject_new_lh_outputs,
    }.get(t)


class InflateSubjectNewLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject_new_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inflated_surface: OutputPathType
    """Inflated surface file for the left hemisphere"""


def inflate_subject_new_lh_params(
    subject_dir: str,
) -> InflateSubjectNewLhParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Directory of the subject's data in FreeSurfer.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "inflate_subject_new-lh",
        "subject_dir": subject_dir,
    }
    return params


def inflate_subject_new_lh_cargs(
    params: InflateSubjectNewLhParameters,
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
    cargs.extend([
        "-lh",
        "inflate_subject_new" + params.get("subject_dir")
    ])
    cargs.append("[OPTIONS]")
    return cargs


def inflate_subject_new_lh_outputs(
    params: InflateSubjectNewLhParameters,
    execution: Execution,
) -> InflateSubjectNewLhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InflateSubjectNewLhOutputs(
        root=execution.output_file("."),
        inflated_surface=execution.output_file(params.get("subject_dir") + "/surf/lh.inflated"),
    )
    return ret


def inflate_subject_new_lh_execute(
    params: InflateSubjectNewLhParameters,
    execution: Execution,
) -> InflateSubjectNewLhOutputs:
    """
    Tool for inflating the left hemisphere of a subject in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectNewLhOutputs`).
    """
    cargs = inflate_subject_new_lh_cargs(params, execution)
    ret = inflate_subject_new_lh_outputs(params, execution)
    execution.run(cargs)
    return ret


def inflate_subject_new_lh(
    subject_dir: str,
    runner: Runner | None = None,
) -> InflateSubjectNewLhOutputs:
    """
    Tool for inflating the left hemisphere of a subject in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Directory of the subject's data in FreeSurfer.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectNewLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT_NEW_LH_METADATA)
    params = inflate_subject_new_lh_params(subject_dir=subject_dir)
    return inflate_subject_new_lh_execute(params, execution)


__all__ = [
    "INFLATE_SUBJECT_NEW_LH_METADATA",
    "InflateSubjectNewLhOutputs",
    "InflateSubjectNewLhParameters",
    "inflate_subject_new_lh",
    "inflate_subject_new_lh_params",
]
