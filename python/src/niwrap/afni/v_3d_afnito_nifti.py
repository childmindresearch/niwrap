# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_AFNITO_NIFTI_METADATA = Metadata(
    id="c2219650fbe1d83f01eda91dff81cc7a82f46430.boutiques",
    name="3dAFNItoNIFTI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAfnitoNiftiParameters = typing.TypedDict('V3dAfnitoNiftiParameters', {
    "__STYX_TYPE__": typing.Literal["3dAFNItoNIFTI"],
    "input_dataset": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "verbose": bool,
    "force_float": bool,
    "pure": bool,
    "denote": bool,
    "oldid": bool,
    "newid": bool,
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
        "3dAFNItoNIFTI": v_3d_afnito_nifti_cargs,
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
        "3dAFNItoNIFTI": v_3d_afnito_nifti_outputs,
    }.get(t)


class V3dAfnitoNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_afnito_nifti(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_nifti: OutputPathType | None
    """Output NIfTI file."""


def v_3d_afnito_nifti_params(
    input_dataset: InputPathType,
    prefix: str | None = None,
    verbose: bool = False,
    force_float: bool = False,
    pure: bool = False,
    denote: bool = False,
    oldid: bool = False,
    newid: bool = False,
) -> V3dAfnitoNiftiParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input AFNI dataset.
        prefix: Output NIfTI file prefix.
        verbose: Print progress messages (increases verbosity if repeated).
        force_float: Force the output dataset to be 32-bit floats.
        pure: Do not write an AFNI extension field into the output file.
        denote: Remove text notes from AFNI extension field that might contain\
            identifying information.
        oldid: Retain the input dataset's AFNI ID code.
        newid: Assign a new AFNI ID code to the dataset (default action).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dAFNItoNIFTI",
        "input_dataset": input_dataset,
        "verbose": verbose,
        "force_float": force_float,
        "pure": pure,
        "denote": denote,
        "oldid": oldid,
        "newid": newid,
    }
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_afnito_nifti_cargs(
    params: V3dAfnitoNiftiParameters,
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
    cargs.append("3dAFNItoNIFTI")
    cargs.append(execution.input_file(params.get("input_dataset")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("force_float"):
        cargs.append("-float")
    if params.get("pure"):
        cargs.append("-pure")
    if params.get("denote"):
        cargs.append("-denote")
    if params.get("oldid"):
        cargs.append("-oldid")
    if params.get("newid"):
        cargs.append("-newid")
    return cargs


def v_3d_afnito_nifti_outputs(
    params: V3dAfnitoNiftiParameters,
    execution: Execution,
) -> V3dAfnitoNiftiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAfnitoNiftiOutputs(
        root=execution.output_file("."),
        output_nifti=execution.output_file(params.get("prefix") + ".nii") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_afnito_nifti_execute(
    params: V3dAfnitoNiftiParameters,
    execution: Execution,
) -> V3dAfnitoNiftiOutputs:
    """
    Converts an AFNI dataset to a NIfTI-1.1 file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoNiftiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_afnito_nifti_cargs(params, execution)
    ret = v_3d_afnito_nifti_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_afnito_nifti(
    input_dataset: InputPathType,
    prefix: str | None = None,
    verbose: bool = False,
    force_float: bool = False,
    pure: bool = False,
    denote: bool = False,
    oldid: bool = False,
    newid: bool = False,
    runner: Runner | None = None,
) -> V3dAfnitoNiftiOutputs:
    """
    Converts an AFNI dataset to a NIfTI-1.1 file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input AFNI dataset.
        prefix: Output NIfTI file prefix.
        verbose: Print progress messages (increases verbosity if repeated).
        force_float: Force the output dataset to be 32-bit floats.
        pure: Do not write an AFNI extension field into the output file.
        denote: Remove text notes from AFNI extension field that might contain\
            identifying information.
        oldid: Retain the input dataset's AFNI ID code.
        newid: Assign a new AFNI ID code to the dataset (default action).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoNiftiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AFNITO_NIFTI_METADATA)
    params = v_3d_afnito_nifti_params(input_dataset=input_dataset, prefix=prefix, verbose=verbose, force_float=force_float, pure=pure, denote=denote, oldid=oldid, newid=newid)
    return v_3d_afnito_nifti_execute(params, execution)


__all__ = [
    "V3dAfnitoNiftiOutputs",
    "V3dAfnitoNiftiParameters",
    "V_3D_AFNITO_NIFTI_METADATA",
    "v_3d_afnito_nifti",
    "v_3d_afnito_nifti_params",
]
