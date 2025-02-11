# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_CM_METADATA = Metadata(
    id="b067b12b1032c8b1f441c220e6f5349f1cfe1370.boutiques",
    name="3dCM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dCmParameters = typing.TypedDict('V3dCmParameters', {
    "__STYX_TYPE__": typing.Literal["3dCM"],
    "dset": InputPathType,
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
        "3dCM": v_3d_cm_cargs,
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
        "3dCM": v_3d_cm_outputs,
    }.get(t)


class V3dCmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_cm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    center_of_mass: OutputPathType
    """Center of mass of the dataset."""


def v_3d_cm_params(
    dset: InputPathType,
) -> V3dCmParameters:
    """
    Build parameters.
    
    Args:
        dset: Input dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dCM",
        "dset": dset,
    }
    return params


def v_3d_cm_cargs(
    params: V3dCmParameters,
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
    cargs.append("3dCM")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(params.get("dset")))
    return cargs


def v_3d_cm_outputs(
    params: V3dCmParameters,
    execution: Execution,
) -> V3dCmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dCmOutputs(
        root=execution.output_file("."),
        center_of_mass=execution.output_file("<stdout>"),
    )
    return ret


def v_3d_cm_execute(
    params: V3dCmParameters,
    execution: Execution,
) -> V3dCmOutputs:
    """
    Tool for computing the center of mass of a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dCmOutputs`).
    """
    cargs = v_3d_cm_cargs(params, execution)
    ret = v_3d_cm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_cm(
    dset: InputPathType,
    runner: Runner | None = None,
) -> V3dCmOutputs:
    """
    Tool for computing the center of mass of a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Input dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dCmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_CM_METADATA)
    params = v_3d_cm_params(dset=dset)
    return v_3d_cm_execute(params, execution)


__all__ = [
    "V3dCmOutputs",
    "V3dCmParameters",
    "V_3D_CM_METADATA",
    "v_3d_cm",
    "v_3d_cm_params",
]
