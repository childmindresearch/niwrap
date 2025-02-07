# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ENTROPY_METADATA = Metadata(
    id="65268d877950e23f9bd06dfb7ede10b57050e1e9.boutiques",
    name="3dEntropy",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dEntropyParameters = typing.TypedDict('V3dEntropyParameters', {
    "__STYX_TYPE__": typing.Literal["3dEntropy"],
    "zskip": bool,
    "input_dataset": InputPathType,
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
        "3dEntropy": v_3d_entropy_cargs,
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
        "3dEntropy": v_3d_entropy_outputs,
    }.get(t)


class V3dEntropyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_entropy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_entropy_params(
    input_dataset: InputPathType,
    zskip: bool = False,
) -> V3dEntropyParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset (stored as 16 bit shorts).
        zskip: Skip 0 values in the entropy computation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dEntropy",
        "zskip": zskip,
        "input_dataset": input_dataset,
    }
    return params


def v_3d_entropy_cargs(
    params: V3dEntropyParameters,
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
    cargs.append("3dEntropy")
    if params.get("zskip"):
        cargs.append("-zskip")
    cargs.append(execution.input_file(params.get("input_dataset")))
    return cargs


def v_3d_entropy_outputs(
    params: V3dEntropyParameters,
    execution: Execution,
) -> V3dEntropyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dEntropyOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_entropy_execute(
    params: V3dEntropyParameters,
    execution: Execution,
) -> V3dEntropyOutputs:
    """
    Computes entropy for a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dEntropyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_entropy_cargs(params, execution)
    ret = v_3d_entropy_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_entropy(
    input_dataset: InputPathType,
    zskip: bool = False,
    runner: Runner | None = None,
) -> V3dEntropyOutputs:
    """
    Computes entropy for a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (stored as 16 bit shorts).
        zskip: Skip 0 values in the entropy computation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEntropyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ENTROPY_METADATA)
    params = v_3d_entropy_params(zskip=zskip, input_dataset=input_dataset)
    return v_3d_entropy_execute(params, execution)


__all__ = [
    "V3dEntropyOutputs",
    "V3dEntropyParameters",
    "V_3D_ENTROPY_METADATA",
    "v_3d_entropy",
    "v_3d_entropy_params",
]
