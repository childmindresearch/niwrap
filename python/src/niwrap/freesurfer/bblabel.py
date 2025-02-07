# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BBLABEL_METADATA = Metadata(
    id="8029e18ce532d6970cd367d113a7d2298a390304.boutiques",
    name="bblabel",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
BblabelParameters = typing.TypedDict('BblabelParameters', {
    "__STYX_TYPE__": typing.Literal["bblabel"],
    "labelfile": InputPathType,
    "xmin": typing.NotRequired[float | None],
    "xmax": typing.NotRequired[float | None],
    "ymin": typing.NotRequired[float | None],
    "ymax": typing.NotRequired[float | None],
    "zmin": typing.NotRequired[float | None],
    "zmax": typing.NotRequired[float | None],
    "outlabelfile": str,
    "debug": bool,
    "umask": typing.NotRequired[str | None],
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
        "bblabel": bblabel_cargs,
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
        "bblabel": bblabel_outputs,
    }.get(t)


class BblabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bblabel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file with the label points within the specified bounding box."""


def bblabel_params(
    labelfile: InputPathType,
    outlabelfile: str,
    xmin: float | None = None,
    xmax: float | None = None,
    ymin: float | None = None,
    ymax: float | None = None,
    zmin: float | None = None,
    zmax: float | None = None,
    debug: bool = False,
    umask: str | None = None,
) -> BblabelParameters:
    """
    Build parameters.
    
    Args:
        labelfile: Input label file.
        outlabelfile: Output label file.
        xmin: Minimum x-coordinate for bounding box.
        xmax: Maximum x-coordinate for bounding box.
        ymin: Minimum y-coordinate for bounding box.
        ymax: Maximum y-coordinate for bounding box.
        zmin: Minimum z-coordinate for bounding box.
        zmax: Maximum z-coordinate for bounding box.
        debug: Enable debug mode.
        umask: Set Unix file permission mask.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bblabel",
        "labelfile": labelfile,
        "outlabelfile": outlabelfile,
        "debug": debug,
    }
    if xmin is not None:
        params["xmin"] = xmin
    if xmax is not None:
        params["xmax"] = xmax
    if ymin is not None:
        params["ymin"] = ymin
    if ymax is not None:
        params["ymax"] = ymax
    if zmin is not None:
        params["zmin"] = zmin
    if zmax is not None:
        params["zmax"] = zmax
    if umask is not None:
        params["umask"] = umask
    return params


def bblabel_cargs(
    params: BblabelParameters,
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
    cargs.append("bblabel")
    cargs.extend([
        "--l",
        execution.input_file(params.get("labelfile"))
    ])
    if params.get("xmin") is not None:
        cargs.extend([
            "--xmin",
            str(params.get("xmin"))
        ])
    if params.get("xmax") is not None:
        cargs.extend([
            "--xmax",
            str(params.get("xmax"))
        ])
    if params.get("ymin") is not None:
        cargs.extend([
            "--ymin",
            str(params.get("ymin"))
        ])
    if params.get("ymax") is not None:
        cargs.extend([
            "--ymax",
            str(params.get("ymax"))
        ])
    if params.get("zmin") is not None:
        cargs.extend([
            "--zmin",
            str(params.get("zmin"))
        ])
    if params.get("zmax") is not None:
        cargs.extend([
            "--zmax",
            str(params.get("zmax"))
        ])
    cargs.extend([
        "--o",
        params.get("outlabelfile")
    ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("umask") is not None:
        cargs.extend([
            "--umask",
            params.get("umask")
        ])
    return cargs


def bblabel_outputs(
    params: BblabelParameters,
    execution: Execution,
) -> BblabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BblabelOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("outlabelfile")),
    )
    return ret


def bblabel_execute(
    params: BblabelParameters,
    execution: Execution,
) -> BblabelOutputs:
    """
    Applies a bounding box to a label, copying only the label points within the
    specified box to the output.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BblabelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = bblabel_cargs(params, execution)
    ret = bblabel_outputs(params, execution)
    execution.run(cargs)
    return ret


def bblabel(
    labelfile: InputPathType,
    outlabelfile: str,
    xmin: float | None = None,
    xmax: float | None = None,
    ymin: float | None = None,
    ymax: float | None = None,
    zmin: float | None = None,
    zmax: float | None = None,
    debug: bool = False,
    umask: str | None = None,
    runner: Runner | None = None,
) -> BblabelOutputs:
    """
    Applies a bounding box to a label, copying only the label points within the
    specified box to the output.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        labelfile: Input label file.
        outlabelfile: Output label file.
        xmin: Minimum x-coordinate for bounding box.
        xmax: Maximum x-coordinate for bounding box.
        ymin: Minimum y-coordinate for bounding box.
        ymax: Maximum y-coordinate for bounding box.
        zmin: Minimum z-coordinate for bounding box.
        zmax: Maximum z-coordinate for bounding box.
        debug: Enable debug mode.
        umask: Set Unix file permission mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BblabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BBLABEL_METADATA)
    params = bblabel_params(labelfile=labelfile, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, zmin=zmin, zmax=zmax, outlabelfile=outlabelfile, debug=debug, umask=umask)
    return bblabel_execute(params, execution)


__all__ = [
    "BBLABEL_METADATA",
    "BblabelOutputs",
    "BblabelParameters",
    "bblabel",
    "bblabel_params",
]
