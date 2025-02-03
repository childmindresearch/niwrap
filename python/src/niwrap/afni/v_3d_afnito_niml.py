# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_AFNITO_NIML_METADATA = Metadata(
    id="98f63f2e946d67b9373a37700e5abbc719dca8ea.boutiques",
    name="3dAFNItoNIML",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAfnitoNimlParameters = typing.TypedDict('V3dAfnitoNimlParameters', {
    "__STYX_TYPE__": typing.Literal["3dAFNItoNIML"],
    "dset": InputPathType,
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
        "3dAFNItoNIML": v_3d_afnito_niml_cargs,
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


class V3dAfnitoNimlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_afnito_niml(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_afnito_niml_params(
    dset: InputPathType,
) -> V3dAfnitoNimlParameters:
    """
    Build parameters.
    
    Args:
        dset: AFNI dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dAFNItoNIML",
        "dset": dset,
    }
    return params


def v_3d_afnito_niml_cargs(
    params: V3dAfnitoNimlParameters,
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
    cargs.append("3dAFNItoNIML")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(params.get("dset")))
    return cargs


def v_3d_afnito_niml_outputs(
    params: V3dAfnitoNimlParameters,
    execution: Execution,
) -> V3dAfnitoNimlOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAfnitoNimlOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_afnito_niml_execute(
    params: V3dAfnitoNimlParameters,
    execution: Execution,
) -> V3dAfnitoNimlOutputs:
    """
    Dumps AFNI dataset header information to stdout in NIML format. Mostly for
    debugging and testing purposes!.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoNimlOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_afnito_niml_cargs(params, execution)
    ret = v_3d_afnito_niml_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_afnito_niml(
    dset: InputPathType,
    runner: Runner | None = None,
) -> V3dAfnitoNimlOutputs:
    """
    Dumps AFNI dataset header information to stdout in NIML format. Mostly for
    debugging and testing purposes!.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: AFNI dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoNimlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AFNITO_NIML_METADATA)
    params = v_3d_afnito_niml_params(dset=dset)
    return v_3d_afnito_niml_execute(params, execution)


__all__ = [
    "V3dAfnitoNimlOutputs",
    "V_3D_AFNITO_NIML_METADATA",
    "v_3d_afnito_niml",
    "v_3d_afnito_niml_params",
]
