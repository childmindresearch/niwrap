# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_THICKNESS_COMPARISON_METADATA = Metadata(
    id="7af273460a46de42cbe519e79fb65ca38e3c1fff.boutiques",
    name="mris_thickness_comparison",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisThicknessComparisonParameters = typing.TypedDict('MrisThicknessComparisonParameters', {
    "__STYX_TYPE__": typing.Literal["mris_thickness_comparison"],
    "subject": str,
    "hemi": str,
    "thickness_file": InputPathType,
    "w_file": InputPathType,
    "labels": list[str],
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
        "mris_thickness_comparison": mris_thickness_comparison_cargs,
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


class MrisThicknessComparisonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_thickness_comparison(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_thickness_comparison_params(
    subject: str,
    hemi: str,
    thickness_file: InputPathType,
    w_file: InputPathType,
    labels: list[str],
) -> MrisThicknessComparisonParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g., lh or rh).
        thickness_file: File containing thickness measurements.
        w_file: W file for cortical thickness comparison.
        labels: List of labels to compare, separated by spaces.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_thickness_comparison",
        "subject": subject,
        "hemi": hemi,
        "thickness_file": thickness_file,
        "w_file": w_file,
        "labels": labels,
    }
    return params


def mris_thickness_comparison_cargs(
    params: MrisThicknessComparisonParameters,
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
    cargs.append("mris_thickness_comparison")
    cargs.append(params.get("subject"))
    cargs.append(params.get("hemi"))
    cargs.append(execution.input_file(params.get("thickness_file")))
    cargs.append(execution.input_file(params.get("w_file")))
    cargs.extend(params.get("labels"))
    return cargs


def mris_thickness_comparison_outputs(
    params: MrisThicknessComparisonParameters,
    execution: Execution,
) -> MrisThicknessComparisonOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisThicknessComparisonOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_thickness_comparison_execute(
    params: MrisThicknessComparisonParameters,
    execution: Execution,
) -> MrisThicknessComparisonOutputs:
    """
    Tool to compare cortical thickness measurements between two or more specified
    labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessComparisonOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_thickness_comparison_cargs(params, execution)
    ret = mris_thickness_comparison_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_thickness_comparison(
    subject: str,
    hemi: str,
    thickness_file: InputPathType,
    w_file: InputPathType,
    labels: list[str],
    runner: Runner | None = None,
) -> MrisThicknessComparisonOutputs:
    """
    Tool to compare cortical thickness measurements between two or more specified
    labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g., lh or rh).
        thickness_file: File containing thickness measurements.
        w_file: W file for cortical thickness comparison.
        labels: List of labels to compare, separated by spaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessComparisonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_THICKNESS_COMPARISON_METADATA)
    params = mris_thickness_comparison_params(subject=subject, hemi=hemi, thickness_file=thickness_file, w_file=w_file, labels=labels)
    return mris_thickness_comparison_execute(params, execution)


__all__ = [
    "MRIS_THICKNESS_COMPARISON_METADATA",
    "MrisThicknessComparisonOutputs",
    "mris_thickness_comparison",
    "mris_thickness_comparison_params",
]
