# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_MERGE_PARCELLATIONS_METADATA = Metadata(
    id="59eb13227975afaa7a05e9947ae25c61de64b8ec.boutiques",
    name="mris_merge_parcellations",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisMergeParcellationsParameters = typing.TypedDict('MrisMergeParcellationsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_merge_parcellations"],
    "surface": InputPathType,
    "label1": InputPathType,
    "label2": InputPathType,
    "annot_name": typing.NotRequired[str | None],
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
        "mris_merge_parcellations": mris_merge_parcellations_cargs,
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
        "mris_merge_parcellations": mris_merge_parcellations_outputs,
    }.get(t)


class MrisMergeParcellationsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_merge_parcellations(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_merge_parcellations_params(
    surface: InputPathType,
    label1: InputPathType,
    label2: InputPathType,
    annot_name: str | None = None,
) -> MrisMergeParcellationsParameters:
    """
    Build parameters.
    
    Args:
        surface: Surface file to analyze.
        label1: First label file.
        label2: Second label file.
        annot_name: Compute pairwise Hausdorff distance between all annotations.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_merge_parcellations",
        "surface": surface,
        "label1": label1,
        "label2": label2,
    }
    if annot_name is not None:
        params["annot_name"] = annot_name
    return params


def mris_merge_parcellations_cargs(
    params: MrisMergeParcellationsParameters,
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
    cargs.append("mris_merge_parcellations")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("label1")))
    cargs.append(execution.input_file(params.get("label2")))
    if params.get("annot_name") is not None:
        cargs.extend([
            "-a",
            params.get("annot_name")
        ])
    return cargs


def mris_merge_parcellations_outputs(
    params: MrisMergeParcellationsParameters,
    execution: Execution,
) -> MrisMergeParcellationsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMergeParcellationsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_merge_parcellations_execute(
    params: MrisMergeParcellationsParameters,
    execution: Execution,
) -> MrisMergeParcellationsOutputs:
    """
    This program computes the Hausdorff distance between two labels on the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMergeParcellationsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_merge_parcellations_cargs(params, execution)
    ret = mris_merge_parcellations_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_merge_parcellations(
    surface: InputPathType,
    label1: InputPathType,
    label2: InputPathType,
    annot_name: str | None = None,
    runner: Runner | None = None,
) -> MrisMergeParcellationsOutputs:
    """
    This program computes the Hausdorff distance between two labels on the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Surface file to analyze.
        label1: First label file.
        label2: Second label file.
        annot_name: Compute pairwise Hausdorff distance between all annotations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMergeParcellationsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MERGE_PARCELLATIONS_METADATA)
    params = mris_merge_parcellations_params(surface=surface, label1=label1, label2=label2, annot_name=annot_name)
    return mris_merge_parcellations_execute(params, execution)


__all__ = [
    "MRIS_MERGE_PARCELLATIONS_METADATA",
    "MrisMergeParcellationsOutputs",
    "MrisMergeParcellationsParameters",
    "mris_merge_parcellations",
    "mris_merge_parcellations_params",
]
