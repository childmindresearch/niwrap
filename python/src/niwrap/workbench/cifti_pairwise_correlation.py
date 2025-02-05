# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_PAIRWISE_CORRELATION_METADATA = Metadata(
    id="b915f6d8b944ba1576e9632affc392ecdfd65dfe.boutiques",
    name="cifti-pairwise-correlation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiPairwiseCorrelationParameters = typing.TypedDict('CiftiPairwiseCorrelationParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-pairwise-correlation"],
    "cifti_a": InputPathType,
    "cifti_b": InputPathType,
    "cifti_out": str,
    "opt_fisher_z": bool,
    "opt_override_mapping_check": bool,
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
        "cifti-pairwise-correlation": cifti_pairwise_correlation_cargs,
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
        "cifti-pairwise-correlation": cifti_pairwise_correlation_outputs,
    }
    return vt.get(t)


class CiftiPairwiseCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_pairwise_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_pairwise_correlation_params(
    cifti_a: InputPathType,
    cifti_b: InputPathType,
    cifti_out: str,
    opt_fisher_z: bool = False,
    opt_override_mapping_check: bool = False,
) -> CiftiPairwiseCorrelationParameters:
    """
    Build parameters.
    
    Args:
        cifti_a: first input cifti file.
        cifti_b: second input cifti file.
        cifti_out: output cifti file.
        opt_fisher_z: apply fisher small z transform (ie, artanh) to\
            correlation.
        opt_override_mapping_check: don't check the mappings for compatibility,\
            only check length.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-pairwise-correlation",
        "cifti_a": cifti_a,
        "cifti_b": cifti_b,
        "cifti_out": cifti_out,
        "opt_fisher_z": opt_fisher_z,
        "opt_override_mapping_check": opt_override_mapping_check,
    }
    return params


def cifti_pairwise_correlation_cargs(
    params: CiftiPairwiseCorrelationParameters,
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
    cargs.append("-cifti-pairwise-correlation")
    cargs.append(execution.input_file(params.get("cifti_a")))
    cargs.append(execution.input_file(params.get("cifti_b")))
    cargs.append(params.get("cifti_out"))
    if params.get("opt_fisher_z"):
        cargs.append("-fisher-z")
    if params.get("opt_override_mapping_check"):
        cargs.append("-override-mapping-check")
    return cargs


def cifti_pairwise_correlation_outputs(
    params: CiftiPairwiseCorrelationParameters,
    execution: Execution,
) -> CiftiPairwiseCorrelationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiPairwiseCorrelationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_pairwise_correlation_execute(
    params: CiftiPairwiseCorrelationParameters,
    execution: Execution,
) -> CiftiPairwiseCorrelationOutputs:
    """
    Correlate paired rows between two cifti files.
    
    For each row in <cifti-a>, correlate it with the same row in <cifti-b>, and
    put the result in the same row of <cifti-out>, which has only one column.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiPairwiseCorrelationOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_pairwise_correlation_cargs(params, execution)
    ret = cifti_pairwise_correlation_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_pairwise_correlation(
    cifti_a: InputPathType,
    cifti_b: InputPathType,
    cifti_out: str,
    opt_fisher_z: bool = False,
    opt_override_mapping_check: bool = False,
    runner: Runner | None = None,
) -> CiftiPairwiseCorrelationOutputs:
    """
    Correlate paired rows between two cifti files.
    
    For each row in <cifti-a>, correlate it with the same row in <cifti-b>, and
    put the result in the same row of <cifti-out>, which has only one column.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_a: first input cifti file.
        cifti_b: second input cifti file.
        cifti_out: output cifti file.
        opt_fisher_z: apply fisher small z transform (ie, artanh) to\
            correlation.
        opt_override_mapping_check: don't check the mappings for compatibility,\
            only check length.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiPairwiseCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_PAIRWISE_CORRELATION_METADATA)
    params = cifti_pairwise_correlation_params(cifti_a=cifti_a, cifti_b=cifti_b, cifti_out=cifti_out, opt_fisher_z=opt_fisher_z, opt_override_mapping_check=opt_override_mapping_check)
    return cifti_pairwise_correlation_execute(params, execution)


__all__ = [
    "CIFTI_PAIRWISE_CORRELATION_METADATA",
    "CiftiPairwiseCorrelationOutputs",
    "CiftiPairwiseCorrelationParameters",
    "cifti_pairwise_correlation",
    "cifti_pairwise_correlation_params",
]
