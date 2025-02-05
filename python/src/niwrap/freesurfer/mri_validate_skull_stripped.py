# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VALIDATE_SKULL_STRIPPED_METADATA = Metadata(
    id="2bdfa9e2cc73998aa283c518ac64ca8fd5b27024.boutiques",
    name="mri_validate_skull_stripped",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriValidateSkullStrippedParameters = typing.TypedDict('MriValidateSkullStrippedParameters', {
    "__STYX_TYPE__": typing.Literal["mri_validate_skull_stripped"],
    "mri_reference": InputPathType,
    "mri_test": InputPathType,
    "weight": float,
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
        "mri_validate_skull_stripped": mri_validate_skull_stripped_cargs,
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


class MriValidateSkullStrippedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_validate_skull_stripped(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_validate_skull_stripped_params(
    mri_reference: InputPathType,
    mri_test: InputPathType,
    weight: float,
) -> MriValidateSkullStrippedParameters:
    """
    Build parameters.
    
    Args:
        mri_reference: Reference MRI image to compare against.
        mri_test: Test MRI image that has undergone skull stripping.
        weight: Weight parameter, should be greater than 1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_validate_skull_stripped",
        "mri_reference": mri_reference,
        "mri_test": mri_test,
        "weight": weight,
    }
    return params


def mri_validate_skull_stripped_cargs(
    params: MriValidateSkullStrippedParameters,
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
    cargs.append("tntester")
    cargs.append(execution.input_file(params.get("mri_reference")))
    cargs.append(execution.input_file(params.get("mri_test")))
    cargs.append(str(params.get("weight")))
    return cargs


def mri_validate_skull_stripped_outputs(
    params: MriValidateSkullStrippedParameters,
    execution: Execution,
) -> MriValidateSkullStrippedOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriValidateSkullStrippedOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_validate_skull_stripped_execute(
    params: MriValidateSkullStrippedParameters,
    execution: Execution,
) -> MriValidateSkullStrippedOutputs:
    """
    Tool to validate skull stripped MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriValidateSkullStrippedOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_validate_skull_stripped_cargs(params, execution)
    ret = mri_validate_skull_stripped_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_validate_skull_stripped(
    mri_reference: InputPathType,
    mri_test: InputPathType,
    weight: float,
    runner: Runner | None = None,
) -> MriValidateSkullStrippedOutputs:
    """
    Tool to validate skull stripped MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mri_reference: Reference MRI image to compare against.
        mri_test: Test MRI image that has undergone skull stripping.
        weight: Weight parameter, should be greater than 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriValidateSkullStrippedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VALIDATE_SKULL_STRIPPED_METADATA)
    params = mri_validate_skull_stripped_params(mri_reference=mri_reference, mri_test=mri_test, weight=weight)
    return mri_validate_skull_stripped_execute(params, execution)


__all__ = [
    "MRI_VALIDATE_SKULL_STRIPPED_METADATA",
    "MriValidateSkullStrippedOutputs",
    "MriValidateSkullStrippedParameters",
    "mri_validate_skull_stripped",
    "mri_validate_skull_stripped_params",
]
