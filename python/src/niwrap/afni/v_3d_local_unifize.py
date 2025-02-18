# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_LOCAL_UNIFIZE_METADATA = Metadata(
    id="15f1fc4af844d2f3848e6e3527f1534179ded986.boutiques",
    name="3dLocalUnifize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dLocalUnifizeParameters = typing.TypedDict('V3dLocalUnifizeParameters', {
    "__STYX_TYPE__": typing.Literal["3dLocalUnifize"],
    "input": InputPathType,
    "output": str,
    "working_dir": typing.NotRequired[str | None],
    "echo": bool,
    "no_clean": bool,
    "local_rad": typing.NotRequired[float | None],
    "local_perc": typing.NotRequired[float | None],
    "local_mask": typing.NotRequired[str | None],
    "filter_thr": typing.NotRequired[float | None],
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
        "3dLocalUnifize": v_3d_local_unifize_cargs,
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
        "3dLocalUnifize": v_3d_local_unifize_outputs,
    }.get(t)


class V3dLocalUnifizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_unifize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset file"""


def v_3d_local_unifize_params(
    input_: InputPathType,
    output: str,
    working_dir: str | None = None,
    echo: bool = False,
    no_clean: bool = False,
    local_rad: float | None = None,
    local_perc: float | None = None,
    local_mask: str | None = None,
    filter_thr: float | None = None,
) -> V3dLocalUnifizeParameters:
    """
    Build parameters.
    
    Args:
        input_: Input dataset.
        output: Output dataset name, including path.
        working_dir: Name of temporary working directory (def:\
            __wdir_LocalUni_, plus a random alphanumeric str).
        echo: Run this program very verbosely (default: false).
        no_clean: Do not remove the working directory (default: remove it).
        local_rad: The spherical neighborhood's radius for the 3dLocalStat step\
            (default: -3).
        local_perc: The percentile used in the 3dLocalStat step, generating the\
            scaling volume (default: 50).
        local_mask: Provide the masking option for the 3dLocalStat step; to\
            remove any masking, put 'None' as the option value (default:\
            "-automask").
        filter_thr: Ceiling on values in the final, scaled dataset; values <=0\
            turn off this final filtering (default: 1.5).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dLocalUnifize",
        "input": input_,
        "output": output,
        "echo": echo,
        "no_clean": no_clean,
    }
    if working_dir is not None:
        params["working_dir"] = working_dir
    if local_rad is not None:
        params["local_rad"] = local_rad
    if local_perc is not None:
        params["local_perc"] = local_perc
    if local_mask is not None:
        params["local_mask"] = local_mask
    if filter_thr is not None:
        params["filter_thr"] = filter_thr
    return params


def v_3d_local_unifize_cargs(
    params: V3dLocalUnifizeParameters,
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
    cargs.append("3dLocalUnifize")
    cargs.append(execution.input_file(params.get("input")))
    cargs.extend([
        "-prefix",
        params.get("output")
    ])
    if params.get("working_dir") is not None:
        cargs.extend([
            "-wdir_name",
            params.get("working_dir")
        ])
    if params.get("echo"):
        cargs.append("-echo")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("local_rad") is not None:
        cargs.extend([
            "-local_rad",
            str(params.get("local_rad"))
        ])
    if params.get("local_perc") is not None:
        cargs.extend([
            "-local_perc",
            str(params.get("local_perc"))
        ])
    if params.get("local_mask") is not None:
        cargs.extend([
            "-local_mask",
            params.get("local_mask")
        ])
    if params.get("filter_thr") is not None:
        cargs.extend([
            "-filter_thr",
            str(params.get("filter_thr"))
        ])
    return cargs


def v_3d_local_unifize_outputs(
    params: V3dLocalUnifizeParameters,
    execution: Execution,
) -> V3dLocalUnifizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dLocalUnifizeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output")),
    )
    return ret


def v_3d_local_unifize_execute(
    params: V3dLocalUnifizeParameters,
    execution: Execution,
) -> V3dLocalUnifizeOutputs:
    """
    This program generates a 'unifized' output volume by estimating the median in
    the local neighborhood of each voxel and using that to scale each voxel's
    brightness.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dLocalUnifizeOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_local_unifize_cargs(params, execution)
    ret = v_3d_local_unifize_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_local_unifize(
    input_: InputPathType,
    output: str,
    working_dir: str | None = None,
    echo: bool = False,
    no_clean: bool = False,
    local_rad: float | None = None,
    local_perc: float | None = None,
    local_mask: str | None = None,
    filter_thr: float | None = None,
    runner: Runner | None = None,
) -> V3dLocalUnifizeOutputs:
    """
    This program generates a 'unifized' output volume by estimating the median in
    the local neighborhood of each voxel and using that to scale each voxel's
    brightness.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Input dataset.
        output: Output dataset name, including path.
        working_dir: Name of temporary working directory (def:\
            __wdir_LocalUni_, plus a random alphanumeric str).
        echo: Run this program very verbosely (default: false).
        no_clean: Do not remove the working directory (default: remove it).
        local_rad: The spherical neighborhood's radius for the 3dLocalStat step\
            (default: -3).
        local_perc: The percentile used in the 3dLocalStat step, generating the\
            scaling volume (default: 50).
        local_mask: Provide the masking option for the 3dLocalStat step; to\
            remove any masking, put 'None' as the option value (default:\
            "-automask").
        filter_thr: Ceiling on values in the final, scaled dataset; values <=0\
            turn off this final filtering (default: 1.5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalUnifizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_UNIFIZE_METADATA)
    params = v_3d_local_unifize_params(input_=input_, output=output, working_dir=working_dir, echo=echo, no_clean=no_clean, local_rad=local_rad, local_perc=local_perc, local_mask=local_mask, filter_thr=filter_thr)
    return v_3d_local_unifize_execute(params, execution)


__all__ = [
    "V3dLocalUnifizeOutputs",
    "V3dLocalUnifizeParameters",
    "V_3D_LOCAL_UNIFIZE_METADATA",
    "v_3d_local_unifize",
    "v_3d_local_unifize_params",
]
