# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_AFNITO3_D_METADATA = Metadata(
    id="51230e7f67f1e0eb607573872e1507d7fe45f41a.boutiques",
    name="3dAFNIto3D",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAfnito3DParameters = typing.TypedDict('V3dAfnito3DParameters', {
    "__STYX_TYPE__": typing.Literal["3dAFNIto3D"],
    "dataset": InputPathType,
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
        "3dAFNIto3D": v_3d_afnito3_d_cargs,
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
        "3dAFNIto3D": v_3d_afnito3_d_outputs,
    }.get(t)


class V3dAfnito3DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_afnito3_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output 3D file, either in binary or text format"""


def v_3d_afnito3_d_params(
    dataset: InputPathType,
) -> V3dAfnito3DParameters:
    """
    Build parameters.
    
    Args:
        dataset: AFNI dataset to be converted.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dAFNIto3D",
        "dataset": dataset,
    }
    return params


def v_3d_afnito3_d_cargs(
    params: V3dAfnito3DParameters,
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
    cargs.append("3dAFNIto3D")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3d_afnito3_d_outputs(
    params: V3dAfnito3DParameters,
    execution: Execution,
) -> V3dAfnito3DOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAfnito3DOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("[PREFIX].3D"),
    )
    return ret


def v_3d_afnito3_d_execute(
    params: V3dAfnito3DParameters,
    execution: Execution,
) -> V3dAfnito3DOutputs:
    """
    Reads in an AFNI dataset, and writes it out as a 3D file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAfnito3DOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_afnito3_d_cargs(params, execution)
    ret = v_3d_afnito3_d_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_afnito3_d(
    dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dAfnito3DOutputs:
    """
    Reads in an AFNI dataset, and writes it out as a 3D file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: AFNI dataset to be converted.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAfnito3DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AFNITO3_D_METADATA)
    params = v_3d_afnito3_d_params(dataset=dataset)
    return v_3d_afnito3_d_execute(params, execution)


__all__ = [
    "V3dAfnito3DOutputs",
    "V3dAfnito3DParameters",
    "V_3D_AFNITO3_D_METADATA",
    "v_3d_afnito3_d",
    "v_3d_afnito3_d_params",
]
