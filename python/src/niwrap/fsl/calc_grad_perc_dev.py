# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CALC_GRAD_PERC_DEV_METADATA = Metadata(
    id="76e8d6c21efe0b0e70c7144ea3347d4476e917aa.boutiques",
    name="calc_grad_perc_dev",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
CalcGradPercDevParameters = typing.TypedDict('CalcGradPercDevParameters', {
    "__STYX_TYPE__": typing.Literal["calc_grad_perc_dev"],
    "fullwarp_image": InputPathType,
    "out_basename": str,
    "verbose_flag": bool,
    "help_flag": bool,
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
        "calc_grad_perc_dev": calc_grad_perc_dev_cargs,
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
        "calc_grad_perc_dev": calc_grad_perc_dev_outputs,
    }.get(t)


class CalcGradPercDevOutputs(typing.NamedTuple):
    """
    Output object returned when calling `calc_grad_perc_dev(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def calc_grad_perc_dev_params(
    fullwarp_image: InputPathType,
    out_basename: str,
    verbose_flag: bool = False,
    help_flag: bool = False,
) -> CalcGradPercDevParameters:
    """
    Build parameters.
    
    Args:
        fullwarp_image: Full warp image from gradient_unwarp.py.
        out_basename: Output basename.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display the help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "calc_grad_perc_dev",
        "fullwarp_image": fullwarp_image,
        "out_basename": out_basename,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    return params


def calc_grad_perc_dev_cargs(
    params: CalcGradPercDevParameters,
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
    cargs.append("calc_grad_perc_dev")
    cargs.extend([
        "--fullwarp",
        execution.input_file(params.get("fullwarp_image"))
    ])
    cargs.extend([
        "-o,--out",
        params.get("out_basename")
    ])
    if params.get("verbose_flag"):
        cargs.append("-v,--verbose")
    if params.get("help_flag"):
        cargs.append("-h,--help")
    return cargs


def calc_grad_perc_dev_outputs(
    params: CalcGradPercDevParameters,
    execution: Execution,
) -> CalcGradPercDevOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CalcGradPercDevOutputs(
        root=execution.output_file("."),
    )
    return ret


def calc_grad_perc_dev_execute(
    params: CalcGradPercDevParameters,
    execution: Execution,
) -> CalcGradPercDevOutputs:
    """
    Compute the gradient percent deviation based on a full warp image from
    gradient_unwarp.py.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CalcGradPercDevOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = calc_grad_perc_dev_cargs(params, execution)
    ret = calc_grad_perc_dev_outputs(params, execution)
    execution.run(cargs)
    return ret


def calc_grad_perc_dev(
    fullwarp_image: InputPathType,
    out_basename: str,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> CalcGradPercDevOutputs:
    """
    Compute the gradient percent deviation based on a full warp image from
    gradient_unwarp.py.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        fullwarp_image: Full warp image from gradient_unwarp.py.
        out_basename: Output basename.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display the help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CalcGradPercDevOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CALC_GRAD_PERC_DEV_METADATA)
    params = calc_grad_perc_dev_params(fullwarp_image=fullwarp_image, out_basename=out_basename, verbose_flag=verbose_flag, help_flag=help_flag)
    return calc_grad_perc_dev_execute(params, execution)


__all__ = [
    "CALC_GRAD_PERC_DEV_METADATA",
    "CalcGradPercDevOutputs",
    "CalcGradPercDevParameters",
    "calc_grad_perc_dev",
    "calc_grad_perc_dev_params",
]
