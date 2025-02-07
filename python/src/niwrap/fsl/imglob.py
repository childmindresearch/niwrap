# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMGLOB_METADATA = Metadata(
    id="048af28afaecb36fea36a9848ee9d39cc57bafae.boutiques",
    name="imglob",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
ImglobParameters = typing.TypedDict('ImglobParameters', {
    "__STYX_TYPE__": typing.Literal["imglob"],
    "multiple_extensions": bool,
    "input_list": list[str],
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
        "imglob": imglob_cargs,
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
        "imglob": imglob_outputs,
    }.get(t)


class ImglobOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imglob(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def imglob_params(
    input_list: list[str],
    multiple_extensions: bool = False,
) -> ImglobParameters:
    """
    Build parameters.
    
    Args:
        input_list: List of image names or file paths.
        multiple_extensions: Output list of images with full extensions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imglob",
        "multiple_extensions": multiple_extensions,
        "input_list": input_list,
    }
    return params


def imglob_cargs(
    params: ImglobParameters,
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
    cargs.append("imglob")
    if params.get("multiple_extensions"):
        cargs.append("-extensions")
    cargs.extend(params.get("input_list"))
    return cargs


def imglob_outputs(
    params: ImglobParameters,
    execution: Execution,
) -> ImglobOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImglobOutputs(
        root=execution.output_file("."),
    )
    return ret


def imglob_execute(
    params: ImglobParameters,
    execution: Execution,
) -> ImglobOutputs:
    """
    Tool for generating image lists with specific extensions.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImglobOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = imglob_cargs(params, execution)
    ret = imglob_outputs(params, execution)
    execution.run(cargs)
    return ret


def imglob(
    input_list: list[str],
    multiple_extensions: bool = False,
    runner: Runner | None = None,
) -> ImglobOutputs:
    """
    Tool for generating image lists with specific extensions.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_list: List of image names or file paths.
        multiple_extensions: Output list of images with full extensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImglobOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMGLOB_METADATA)
    params = imglob_params(multiple_extensions=multiple_extensions, input_list=input_list)
    return imglob_execute(params, execution)


__all__ = [
    "IMGLOB_METADATA",
    "ImglobOutputs",
    "ImglobParameters",
    "imglob",
    "imglob_params",
]
