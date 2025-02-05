# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMSTAT_METADATA = Metadata(
    id="c59c01eb2a12e7d9a2066403a73878b709e55aa5.boutiques",
    name="imstat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ImstatParameters = typing.TypedDict('ImstatParameters', {
    "__STYX_TYPE__": typing.Literal["imstat"],
    "no_label": bool,
    "quiet": bool,
    "pixstat_prefix": typing.NotRequired[str | None],
    "image_files": list[InputPathType],
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
        "imstat": imstat_cargs,
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
        "imstat": imstat_outputs,
    }
    return vt.get(t)


class ImstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mean_output: OutputPathType | None
    """Mean of pixel-wise statistics for the collection of 2D images"""
    sdev_output: OutputPathType | None
    """Standard deviation of pixel-wise statistics for the collection of 2D
    images"""


def imstat_params(
    image_files: list[InputPathType],
    no_label: bool = False,
    quiet: bool = False,
    pixstat_prefix: str | None = None,
) -> ImstatParameters:
    """
    Build parameters.
    
    Args:
        image_files: Input image file(s).
        no_label: Don't write labels on each file's summary line.
        quiet: Don't print statistics for each file.
        pixstat_prefix: If more than one image file is given, then\
            'prefix.mean' and 'prefix.sdev' will be written as the pixel-wise\
            statistics images of the whole collection. These images will be in the\
            'flim' floating point format. [This option only works on 2D images!].
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imstat",
        "no_label": no_label,
        "quiet": quiet,
        "image_files": image_files,
    }
    if pixstat_prefix is not None:
        params["pixstat_prefix"] = pixstat_prefix
    return params


def imstat_cargs(
    params: ImstatParameters,
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
    cargs.append("imstat")
    if params.get("no_label"):
        cargs.append("-nolabel")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("pixstat_prefix") is not None:
        cargs.extend([
            "-pixstat",
            params.get("pixstat_prefix")
        ])
    cargs.extend([execution.input_file(f) for f in params.get("image_files")])
    return cargs


def imstat_outputs(
    params: ImstatParameters,
    execution: Execution,
) -> ImstatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImstatOutputs(
        root=execution.output_file("."),
        mean_output=execution.output_file(params.get("pixstat_prefix") + ".mean") if (params.get("pixstat_prefix") is not None) else None,
        sdev_output=execution.output_file(params.get("pixstat_prefix") + ".sdev") if (params.get("pixstat_prefix") is not None) else None,
    )
    return ret


def imstat_execute(
    params: ImstatParameters,
    execution: Execution,
) -> ImstatOutputs:
    """
    Calculation of statistics of one or more images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImstatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = imstat_cargs(params, execution)
    ret = imstat_outputs(params, execution)
    execution.run(cargs)
    return ret


def imstat(
    image_files: list[InputPathType],
    no_label: bool = False,
    quiet: bool = False,
    pixstat_prefix: str | None = None,
    runner: Runner | None = None,
) -> ImstatOutputs:
    """
    Calculation of statistics of one or more images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        image_files: Input image file(s).
        no_label: Don't write labels on each file's summary line.
        quiet: Don't print statistics for each file.
        pixstat_prefix: If more than one image file is given, then\
            'prefix.mean' and 'prefix.sdev' will be written as the pixel-wise\
            statistics images of the whole collection. These images will be in the\
            'flim' floating point format. [This option only works on 2D images!].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMSTAT_METADATA)
    params = imstat_params(no_label=no_label, quiet=quiet, pixstat_prefix=pixstat_prefix, image_files=image_files)
    return imstat_execute(params, execution)


__all__ = [
    "IMSTAT_METADATA",
    "ImstatOutputs",
    "ImstatParameters",
    "imstat",
    "imstat_params",
]
