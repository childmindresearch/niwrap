# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MIDTRANS_METADATA = Metadata(
    id="199624ee421c21ddcb5318e1c0213bf85f4d3c9a.boutiques",
    name="midtrans",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MidtransParameters = typing.TypedDict('MidtransParameters', {
    "__STYX_TYPE__": typing.Literal["midtrans"],
    "transforms": list[InputPathType],
    "output_matrix": typing.NotRequired[str | None],
    "template_image": typing.NotRequired[InputPathType | None],
    "separate_basename": typing.NotRequired[str | None],
    "debug_flag": bool,
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
        "midtrans": midtrans_cargs,
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
    }.get(t)


class MidtransOutputs(typing.NamedTuple):
    """
    Output object returned when calling `midtrans(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def midtrans_params(
    transforms: list[InputPathType],
    output_matrix: str | None = None,
    template_image: InputPathType | None = None,
    separate_basename: str | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
) -> MidtransParameters:
    """
    Build parameters.
    
    Args:
        transforms: List of input transform files (e.g. transform1.mat\
            transform2.mat ... transformN.mat).
        output_matrix: Output filename for the resulting matrix.
        template_image: Input filename for template image (needed for fix\
            origin).
        separate_basename: Basename for the output of separate matrices (final\
            name includes a number; e.g. img2mid0001.mat).
        debug_flag: Switch on debugging output.
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "midtrans",
        "transforms": transforms,
        "debug_flag": debug_flag,
        "verbose_flag": verbose_flag,
    }
    if output_matrix is not None:
        params["output_matrix"] = output_matrix
    if template_image is not None:
        params["template_image"] = template_image
    if separate_basename is not None:
        params["separate_basename"] = separate_basename
    return params


def midtrans_cargs(
    params: MidtransParameters,
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
    cargs.append("midtrans")
    cargs.extend([execution.input_file(f) for f in params.get("transforms")])
    if params.get("output_matrix") is not None:
        cargs.extend([
            "-o",
            params.get("output_matrix")
        ])
    if params.get("template_image") is not None:
        cargs.extend([
            "--template",
            execution.input_file(params.get("template_image"))
        ])
    if params.get("separate_basename") is not None:
        cargs.extend([
            "--separate",
            params.get("separate_basename")
        ])
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("verbose_flag"):
        cargs.append("-v, --verbose")
    return cargs


def midtrans_outputs(
    params: MidtransParameters,
    execution: Execution,
) -> MidtransOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MidtransOutputs(
        root=execution.output_file("."),
    )
    return ret


def midtrans_execute(
    params: MidtransParameters,
    execution: Execution,
) -> MidtransOutputs:
    """
    Calculate the midpoint transform from a series of input transforms.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MidtransOutputs`).
    """
    params = execution.params(params)
    cargs = midtrans_cargs(params, execution)
    ret = midtrans_outputs(params, execution)
    execution.run(cargs)
    return ret


def midtrans(
    transforms: list[InputPathType],
    output_matrix: str | None = None,
    template_image: InputPathType | None = None,
    separate_basename: str | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> MidtransOutputs:
    """
    Calculate the midpoint transform from a series of input transforms.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        transforms: List of input transform files (e.g. transform1.mat\
            transform2.mat ... transformN.mat).
        output_matrix: Output filename for the resulting matrix.
        template_image: Input filename for template image (needed for fix\
            origin).
        separate_basename: Basename for the output of separate matrices (final\
            name includes a number; e.g. img2mid0001.mat).
        debug_flag: Switch on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MidtransOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MIDTRANS_METADATA)
    params = midtrans_params(transforms=transforms, output_matrix=output_matrix, template_image=template_image, separate_basename=separate_basename, debug_flag=debug_flag, verbose_flag=verbose_flag)
    return midtrans_execute(params, execution)


__all__ = [
    "MIDTRANS_METADATA",
    "MidtransOutputs",
    "MidtransParameters",
    "midtrans",
    "midtrans_params",
]
