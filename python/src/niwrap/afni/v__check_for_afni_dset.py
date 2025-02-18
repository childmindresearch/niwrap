# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__CHECK_FOR_AFNI_DSET_METADATA = Metadata(
    id="36d93d7fee0a8f5033359b79ea1fc2a9f56b9766.boutiques",
    name="@CheckForAfniDset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VCheckForAfniDsetParameters = typing.TypedDict('VCheckForAfniDsetParameters', {
    "__STYX_TYPE__": typing.Literal["@CheckForAfniDset"],
    "dataset_name": str,
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
        "@CheckForAfniDset": v__check_for_afni_dset_cargs,
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
        "@CheckForAfniDset": v__check_for_afni_dset_outputs,
    }.get(t)


class VCheckForAfniDsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__check_for_afni_dset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_status: OutputPathType
    """Text file containing the status code of the dataset"""


def v__check_for_afni_dset_params(
    dataset_name: str,
) -> VCheckForAfniDsetParameters:
    """
    Build parameters.
    
    Args:
        dataset_name: Path to the AFNI dataset (e.g.,\
            /Data/stuff/Hello+orig.HEAD).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@CheckForAfniDset",
        "dataset_name": dataset_name,
    }
    return params


def v__check_for_afni_dset_cargs(
    params: VCheckForAfniDsetParameters,
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
    cargs.append("@CheckForAfniDset")
    cargs.append(params.get("dataset_name"))
    return cargs


def v__check_for_afni_dset_outputs(
    params: VCheckForAfniDsetParameters,
    execution: Execution,
) -> VCheckForAfniDsetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VCheckForAfniDsetOutputs(
        root=execution.output_file("."),
        output_status=execution.output_file(params.get("dataset_name") + "_status.txt"),
    )
    return ret


def v__check_for_afni_dset_execute(
    params: VCheckForAfniDsetParameters,
    execution: Execution,
) -> VCheckForAfniDsetOutputs:
    """
    Check for the existence of AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VCheckForAfniDsetOutputs`).
    """
    params = execution.params(params)
    cargs = v__check_for_afni_dset_cargs(params, execution)
    ret = v__check_for_afni_dset_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__check_for_afni_dset(
    dataset_name: str,
    runner: Runner | None = None,
) -> VCheckForAfniDsetOutputs:
    """
    Check for the existence of AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset_name: Path to the AFNI dataset (e.g.,\
            /Data/stuff/Hello+orig.HEAD).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VCheckForAfniDsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CHECK_FOR_AFNI_DSET_METADATA)
    params = v__check_for_afni_dset_params(dataset_name=dataset_name)
    return v__check_for_afni_dset_execute(params, execution)


__all__ = [
    "VCheckForAfniDsetOutputs",
    "VCheckForAfniDsetParameters",
    "V__CHECK_FOR_AFNI_DSET_METADATA",
    "v__check_for_afni_dset",
    "v__check_for_afni_dset_params",
]
