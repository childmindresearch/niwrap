# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_VIOLIN_PLOTS_METADATA = Metadata(
    id="a193f3c5d1fcce153b59c31f2df32aafdf44cb45.boutiques",
    name="dmri_violinPlots",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriViolinPlotsParameters = typing.TypedDict('DmriViolinPlotsParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_violinPlots"],
    "input_directory": str,
    "labels": InputPathType,
    "structure": str,
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
        "dmri_violinPlots": dmri_violin_plots_cargs,
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
        "dmri_violinPlots": dmri_violin_plots_outputs,
    }.get(t)


class DmriViolinPlotsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_violin_plots(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmri_violin_plots_params(
    input_directory: str,
    labels: InputPathType,
    structure: str,
) -> DmriViolinPlotsParameters:
    """
    Build parameters.
    
    Args:
        input_directory: Directory with all subjects.
        labels: CSV file with group labels.
        structure: Name of the structure.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_violinPlots",
        "input_directory": input_directory,
        "labels": labels,
        "structure": structure,
    }
    return params


def dmri_violin_plots_cargs(
    params: DmriViolinPlotsParameters,
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
    cargs.append("dmri_violinPlots")
    cargs.extend([
        "-i",
        params.get("input_directory")
    ])
    cargs.extend([
        "-l",
        execution.input_file(params.get("labels"))
    ])
    cargs.extend([
        "-s",
        params.get("structure")
    ])
    return cargs


def dmri_violin_plots_outputs(
    params: DmriViolinPlotsParameters,
    execution: Execution,
) -> DmriViolinPlotsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriViolinPlotsOutputs(
        root=execution.output_file("."),
    )
    return ret


def dmri_violin_plots_execute(
    params: DmriViolinPlotsParameters,
    execution: Execution,
) -> DmriViolinPlotsOutputs:
    """
    Generate violin plots for dMRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriViolinPlotsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dmri_violin_plots_cargs(params, execution)
    ret = dmri_violin_plots_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_violin_plots(
    input_directory: str,
    labels: InputPathType,
    structure: str,
    runner: Runner | None = None,
) -> DmriViolinPlotsOutputs:
    """
    Generate violin plots for dMRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_directory: Directory with all subjects.
        labels: CSV file with group labels.
        structure: Name of the structure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriViolinPlotsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_VIOLIN_PLOTS_METADATA)
    params = dmri_violin_plots_params(input_directory=input_directory, labels=labels, structure=structure)
    return dmri_violin_plots_execute(params, execution)


__all__ = [
    "DMRI_VIOLIN_PLOTS_METADATA",
    "DmriViolinPlotsOutputs",
    "DmriViolinPlotsParameters",
    "dmri_violin_plots",
    "dmri_violin_plots_params",
]
