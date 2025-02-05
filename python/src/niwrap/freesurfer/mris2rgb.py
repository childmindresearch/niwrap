# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS2RGB_METADATA = Metadata(
    id="818f21a5949f0f382881eefc95f28854696728c3.boutiques",
    name="mris2rgb",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Mris2rgbParameters = typing.TypedDict('Mris2rgbParameters', {
    "__STYX_TYPE__": typing.Literal["mris2rgb"],
    "library_path": str,
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
        "mris2rgb": mris2rgb_cargs,
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
    vt = {}
    return vt.get(t)


class Mris2rgbOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris2rgb(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris2rgb_params(
    library_path: str,
) -> Mris2rgbParameters:
    """
    Build parameters.
    
    Args:
        library_path: Path to the directory containing the libGLU.so.1 library\
            required by mris2rgb.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris2rgb",
        "library_path": library_path,
    }
    return params


def mris2rgb_cargs(
    params: Mris2rgbParameters,
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
    cargs.append("mris2rgb")
    cargs.extend([
        "export LD_LIBRARY_PATH=",
        params.get("library_path")
    ])
    return cargs


def mris2rgb_outputs(
    params: Mris2rgbParameters,
    execution: Execution,
) -> Mris2rgbOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Mris2rgbOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris2rgb_execute(
    params: Mris2rgbParameters,
    execution: Execution,
) -> Mris2rgbOutputs:
    """
    A tool from FreeSurfer for converting MRI surface files to RGB images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Mris2rgbOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris2rgb_cargs(params, execution)
    ret = mris2rgb_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris2rgb(
    library_path: str,
    runner: Runner | None = None,
) -> Mris2rgbOutputs:
    """
    A tool from FreeSurfer for converting MRI surface files to RGB images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        library_path: Path to the directory containing the libGLU.so.1 library\
            required by mris2rgb.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Mris2rgbOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS2RGB_METADATA)
    params = mris2rgb_params(library_path=library_path)
    return mris2rgb_execute(params, execution)


__all__ = [
    "MRIS2RGB_METADATA",
    "Mris2rgbOutputs",
    "Mris2rgbParameters",
    "mris2rgb",
    "mris2rgb_params",
]
