# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

COMPUTE_INTERRATER_VARIABILITY_CSH_METADATA = Metadata(
    id="d85f89519ecdd6db050cf20b230dd279bab615ca.boutiques",
    name="compute_interrater_variability.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ComputeInterraterVariabilityCshParameters = typing.TypedDict('ComputeInterraterVariabilityCshParameters', {
    "__STYX_TYPE__": typing.Literal["compute_interrater_variability.csh"],
    "label_vol1": InputPathType,
    "label_vol2": InputPathType,
    "output_prefix": str,
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
        "compute_interrater_variability.csh": compute_interrater_variability_csh_cargs,
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
        "compute_interrater_variability.csh": compute_interrater_variability_csh_outputs,
    }.get(t)


class ComputeInterraterVariabilityCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `compute_interrater_variability_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file_1: OutputPathType
    """Output file containing mean Hausdorff distance."""
    output_file_2: OutputPathType
    """Output file containing max Hausdorff distance."""
    output_file_3: OutputPathType
    """Output file containing label volume difference, Dice, and Jaccard overlap
    measures."""


def compute_interrater_variability_csh_params(
    label_vol1: InputPathType,
    label_vol2: InputPathType,
    output_prefix: str,
) -> ComputeInterraterVariabilityCshParameters:
    """
    Build parameters.
    
    Args:
        label_vol1: Label volume from rater 1.
        label_vol2: Label volume from rater 2.
        output_prefix: Prefix for the output text files containing results. A\
            total of three files will be produced.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "compute_interrater_variability.csh",
        "label_vol1": label_vol1,
        "label_vol2": label_vol2,
        "output_prefix": output_prefix,
    }
    return params


def compute_interrater_variability_csh_cargs(
    params: ComputeInterraterVariabilityCshParameters,
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
    cargs.append("compute_interrater_variability")
    cargs.extend([
        "--vol1",
        execution.input_file(params.get("label_vol1"))
    ])
    cargs.extend([
        "--vol2",
        execution.input_file(params.get("label_vol2"))
    ])
    cargs.extend([
        "--out",
        params.get("output_prefix")
    ])
    return cargs


def compute_interrater_variability_csh_outputs(
    params: ComputeInterraterVariabilityCshParameters,
    execution: Execution,
) -> ComputeInterraterVariabilityCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ComputeInterraterVariabilityCshOutputs(
        root=execution.output_file("."),
        output_file_1=execution.output_file(params.get("output_prefix") + "_file1.txt"),
        output_file_2=execution.output_file(params.get("output_prefix") + "_file2.txt"),
        output_file_3=execution.output_file(params.get("output_prefix") + "_file3.txt"),
    )
    return ret


def compute_interrater_variability_csh_execute(
    params: ComputeInterraterVariabilityCshParameters,
    execution: Execution,
) -> ComputeInterraterVariabilityCshOutputs:
    """
    Computes the interrater variability between label volumes from different raters
    or time points using several metrics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ComputeInterraterVariabilityCshOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = compute_interrater_variability_csh_cargs(params, execution)
    ret = compute_interrater_variability_csh_outputs(params, execution)
    execution.run(cargs)
    return ret


def compute_interrater_variability_csh(
    label_vol1: InputPathType,
    label_vol2: InputPathType,
    output_prefix: str,
    runner: Runner | None = None,
) -> ComputeInterraterVariabilityCshOutputs:
    """
    Computes the interrater variability between label volumes from different raters
    or time points using several metrics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label_vol1: Label volume from rater 1.
        label_vol2: Label volume from rater 2.
        output_prefix: Prefix for the output text files containing results. A\
            total of three files will be produced.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ComputeInterraterVariabilityCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(COMPUTE_INTERRATER_VARIABILITY_CSH_METADATA)
    params = compute_interrater_variability_csh_params(label_vol1=label_vol1, label_vol2=label_vol2, output_prefix=output_prefix)
    return compute_interrater_variability_csh_execute(params, execution)


__all__ = [
    "COMPUTE_INTERRATER_VARIABILITY_CSH_METADATA",
    "ComputeInterraterVariabilityCshOutputs",
    "ComputeInterraterVariabilityCshParameters",
    "compute_interrater_variability_csh",
    "compute_interrater_variability_csh_params",
]
