# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

NSIZE_METADATA = Metadata(
    id="d61eb0714ab51aec00c025a2f54aab55318f6b55.boutiques",
    name="nsize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
NsizeParameters = typing.TypedDict('NsizeParameters', {
    "__STYX_TYPE__": typing.Literal["nsize"],
    "image_in": InputPathType,
    "image_out": str,
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
        "nsize": nsize_cargs,
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
        "nsize": nsize_outputs,
    }
    return vt.get(t)


class NsizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nsize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    image_out_file: OutputPathType
    """Zero padded output image file"""


def nsize_params(
    image_in: InputPathType,
    image_out: str,
) -> NsizeParameters:
    """
    Build parameters.
    
    Args:
        image_in: Input image file.
        image_out: Output padded image file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "nsize",
        "image_in": image_in,
        "image_out": image_out,
    }
    return params


def nsize_cargs(
    params: NsizeParameters,
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
    cargs.append("nsize")
    cargs.append(execution.input_file(params.get("image_in")))
    cargs.append(params.get("image_out"))
    return cargs


def nsize_outputs(
    params: NsizeParameters,
    execution: Execution,
) -> NsizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = NsizeOutputs(
        root=execution.output_file("."),
        image_out_file=execution.output_file(params.get("image_out")),
    )
    return ret


def nsize_execute(
    params: NsizeParameters,
    execution: Execution,
) -> NsizeOutputs:
    """
    Zero pads an input image to the nearest larger NxN dimensions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `NsizeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = nsize_cargs(params, execution)
    ret = nsize_outputs(params, execution)
    execution.run(cargs)
    return ret


def nsize(
    image_in: InputPathType,
    image_out: str,
    runner: Runner | None = None,
) -> NsizeOutputs:
    """
    Zero pads an input image to the nearest larger NxN dimensions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        image_in: Input image file.
        image_out: Output padded image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NsizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NSIZE_METADATA)
    params = nsize_params(image_in=image_in, image_out=image_out)
    return nsize_execute(params, execution)


__all__ = [
    "NSIZE_METADATA",
    "NsizeOutputs",
    "NsizeParameters",
    "nsize",
    "nsize_params",
]
