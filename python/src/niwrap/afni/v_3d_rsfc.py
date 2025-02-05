# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_RSFC_METADATA = Metadata(
    id="b5c2a121f1ca24f0166e661caec651b36aec44bd.boutiques",
    name="3dRSFC",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dRsfcParameters = typing.TypedDict('V3dRsfcParameters', {
    "__STYX_TYPE__": typing.Literal["3dRSFC"],
    "fbot": float,
    "ftop": float,
    "input_dataset": InputPathType,
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
        "3dRSFC": v_3d_rsfc_cargs,
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
        "3dRSFC": v_3d_rsfc_outputs,
    }
    return vt.get(t)


class V3dRsfcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_rsfc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filtered_time_series: OutputPathType
    """Filtered time series output"""
    un_bandpassed_series: OutputPathType
    """Un-bandpassed series output"""


def v_3d_rsfc_params(
    fbot: float,
    ftop: float,
    input_dataset: InputPathType,
) -> V3dRsfcParameters:
    """
    Build parameters.
    
    Args:
        fbot: Lowest frequency in the passband, in Hz.
        ftop: Highest frequency in the passband (must be > fbot).
        input_dataset: Input dataset (3D+time sequence of volumes).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dRSFC",
        "fbot": fbot,
        "ftop": ftop,
        "input_dataset": input_dataset,
    }
    return params


def v_3d_rsfc_cargs(
    params: V3dRsfcParameters,
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
    cargs.append("3dRSFC")
    cargs.append("[OPTIONS]")
    cargs.append(str(params.get("fbot")))
    cargs.append(str(params.get("ftop")))
    cargs.append(execution.input_file(params.get("input_dataset")))
    return cargs


def v_3d_rsfc_outputs(
    params: V3dRsfcParameters,
    execution: Execution,
) -> V3dRsfcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dRsfcOutputs(
        root=execution.output_file("."),
        filtered_time_series=execution.output_file("[PREFIX]_LFF+orig.*"),
        un_bandpassed_series=execution.output_file("[PREFIX]_unBP+orig.*"),
    )
    return ret


def v_3d_rsfc_execute(
    params: V3dRsfcParameters,
    execution: Execution,
) -> V3dRsfcOutputs:
    """
    Program to calculate common resting state functional connectivity (RSFC)
    parameters.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dRsfcOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_rsfc_cargs(params, execution)
    ret = v_3d_rsfc_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_rsfc(
    fbot: float,
    ftop: float,
    input_dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dRsfcOutputs:
    """
    Program to calculate common resting state functional connectivity (RSFC)
    parameters.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        fbot: Lowest frequency in the passband, in Hz.
        ftop: Highest frequency in the passband (must be > fbot).
        input_dataset: Input dataset (3D+time sequence of volumes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRsfcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_RSFC_METADATA)
    params = v_3d_rsfc_params(fbot=fbot, ftop=ftop, input_dataset=input_dataset)
    return v_3d_rsfc_execute(params, execution)


__all__ = [
    "V3dRsfcOutputs",
    "V3dRsfcParameters",
    "V_3D_RSFC_METADATA",
    "v_3d_rsfc",
    "v_3d_rsfc_params",
]
