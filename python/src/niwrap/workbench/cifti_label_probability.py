# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_LABEL_PROBABILITY_METADATA = Metadata(
    id="fb93f8ce53e22b6efd862837588951005975ba93.boutiques",
    name="cifti-label-probability",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiLabelProbabilityParameters = typing.TypedDict('CiftiLabelProbabilityParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-label-probability"],
    "label_maps": InputPathType,
    "probability_dscalar_out": str,
    "opt_exclude_unlabeled": bool,
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
        "cifti-label-probability": cifti_label_probability_cargs,
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
        "cifti-label-probability": cifti_label_probability_outputs,
    }
    return vt.get(t)


class CiftiLabelProbabilityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_probability(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    probability_dscalar_out: OutputPathType
    """the relative frequencies of each label at each vertex/voxel"""


def cifti_label_probability_params(
    label_maps: InputPathType,
    probability_dscalar_out: str,
    opt_exclude_unlabeled: bool = False,
) -> CiftiLabelProbabilityParameters:
    """
    Build parameters.
    
    Args:
        label_maps: cifti dlabel file containing individual label maps from\
            many subjects.
        probability_dscalar_out: the relative frequencies of each label at each\
            vertex/voxel.
        opt_exclude_unlabeled: don't make a probability map of the unlabeled\
            key.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-label-probability",
        "label_maps": label_maps,
        "probability_dscalar_out": probability_dscalar_out,
        "opt_exclude_unlabeled": opt_exclude_unlabeled,
    }
    return params


def cifti_label_probability_cargs(
    params: CiftiLabelProbabilityParameters,
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
    cargs.append("wb_command")
    cargs.append("-cifti-label-probability")
    cargs.append(execution.input_file(params.get("label_maps")))
    cargs.append(params.get("probability_dscalar_out"))
    if params.get("opt_exclude_unlabeled"):
        cargs.append("-exclude-unlabeled")
    return cargs


def cifti_label_probability_outputs(
    params: CiftiLabelProbabilityParameters,
    execution: Execution,
) -> CiftiLabelProbabilityOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiLabelProbabilityOutputs(
        root=execution.output_file("."),
        probability_dscalar_out=execution.output_file(params.get("probability_dscalar_out")),
    )
    return ret


def cifti_label_probability_execute(
    params: CiftiLabelProbabilityParameters,
    execution: Execution,
) -> CiftiLabelProbabilityOutputs:
    """
    Find frequency of cifti labels.
    
    This command outputs a set of soft ROIs, one for each label in the input,
    where the value is how many of the input maps had that label at that
    vertex/voxel, divided by the number of input maps.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelProbabilityOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_label_probability_cargs(params, execution)
    ret = cifti_label_probability_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_label_probability(
    label_maps: InputPathType,
    probability_dscalar_out: str,
    opt_exclude_unlabeled: bool = False,
    runner: Runner | None = None,
) -> CiftiLabelProbabilityOutputs:
    """
    Find frequency of cifti labels.
    
    This command outputs a set of soft ROIs, one for each label in the input,
    where the value is how many of the input maps had that label at that
    vertex/voxel, divided by the number of input maps.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_maps: cifti dlabel file containing individual label maps from\
            many subjects.
        probability_dscalar_out: the relative frequencies of each label at each\
            vertex/voxel.
        opt_exclude_unlabeled: don't make a probability map of the unlabeled\
            key.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelProbabilityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_PROBABILITY_METADATA)
    params = cifti_label_probability_params(label_maps=label_maps, probability_dscalar_out=probability_dscalar_out, opt_exclude_unlabeled=opt_exclude_unlabeled)
    return cifti_label_probability_execute(params, execution)


__all__ = [
    "CIFTI_LABEL_PROBABILITY_METADATA",
    "CiftiLabelProbabilityOutputs",
    "CiftiLabelProbabilityParameters",
    "cifti_label_probability",
    "cifti_label_probability_params",
]
