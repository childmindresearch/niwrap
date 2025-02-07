# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DNVALS_METADATA = Metadata(
    id="d7ef1cfaf0a24a61ba64fc6419199d6758fdcf7a.boutiques",
    name="3dnvals",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dnvalsParameters = typing.TypedDict('V3dnvalsParameters', {
    "__STYX_TYPE__": typing.Literal["3dnvals"],
    "datasets": list[InputPathType],
    "all_flag": bool,
    "verbose_flag": bool,
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
        "3dnvals": v_3dnvals_cargs,
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
        "3dnvals": v_3dnvals_outputs,
    }.get(t)


class V3dnvalsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dnvals(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3dnvals_params(
    datasets: list[InputPathType],
    all_flag: bool = False,
    verbose_flag: bool = False,
) -> V3dnvalsParameters:
    """
    Build parameters.
    
    Args:
        datasets: Input 3D dataset(s).
        all_flag: Print out all 4 dimensions: Nx, Ny, Nz, Nvals.
        verbose_flag: Print the header name of the dataset first.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dnvals",
        "datasets": datasets,
        "all_flag": all_flag,
        "verbose_flag": verbose_flag,
    }
    return params


def v_3dnvals_cargs(
    params: V3dnvalsParameters,
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
    cargs.append("3dnvals")
    cargs.extend([execution.input_file(f) for f in params.get("datasets")])
    if params.get("all_flag"):
        cargs.append("-all")
    if params.get("verbose_flag"):
        cargs.append("-verbose")
    return cargs


def v_3dnvals_outputs(
    params: V3dnvalsParameters,
    execution: Execution,
) -> V3dnvalsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dnvalsOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3dnvals_execute(
    params: V3dnvalsParameters,
    execution: Execution,
) -> V3dnvalsOutputs:
    """
    Tool to print the number of sub-bricks in a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dnvalsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3dnvals_cargs(params, execution)
    ret = v_3dnvals_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dnvals(
    datasets: list[InputPathType],
    all_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> V3dnvalsOutputs:
    """
    Tool to print the number of sub-bricks in a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: Input 3D dataset(s).
        all_flag: Print out all 4 dimensions: Nx, Ny, Nz, Nvals.
        verbose_flag: Print the header name of the dataset first.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dnvalsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DNVALS_METADATA)
    params = v_3dnvals_params(datasets=datasets, all_flag=all_flag, verbose_flag=verbose_flag)
    return v_3dnvals_execute(params, execution)


__all__ = [
    "V3dnvalsOutputs",
    "V3dnvalsParameters",
    "V_3DNVALS_METADATA",
    "v_3dnvals",
    "v_3dnvals_params",
]
