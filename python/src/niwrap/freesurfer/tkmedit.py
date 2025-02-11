# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TKMEDIT_METADATA = Metadata(
    id="215f4c63f4d1d614a5f6ddc04a121949f2f19d48.boutiques",
    name="tkmedit",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
TkmeditParameters = typing.TypedDict('TkmeditParameters', {
    "__STYX_TYPE__": typing.Literal["tkmedit"],
    "input_volume": InputPathType,
    "options": typing.NotRequired[str | None],
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
        "tkmedit": tkmedit_cargs,
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


class TkmeditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tkmedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tkmedit_params(
    input_volume: InputPathType,
    options: str | None = None,
) -> TkmeditParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume file (e.g., nu.mgz or brain.mgz).
        options: Options for running tkmedit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tkmedit",
        "input_volume": input_volume,
    }
    if options is not None:
        params["options"] = options
    return params


def tkmedit_cargs(
    params: TkmeditParameters,
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
    cargs.append("tkmedit")
    cargs.append(execution.input_file(params.get("input_volume")))
    if params.get("options") is not None:
        cargs.append(params.get("options"))
    return cargs


def tkmedit_outputs(
    params: TkmeditParameters,
    execution: Execution,
) -> TkmeditOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TkmeditOutputs(
        root=execution.output_file("."),
    )
    return ret


def tkmedit_execute(
    params: TkmeditParameters,
    execution: Execution,
) -> TkmeditOutputs:
    """
    tkmedit is a multi-functional imaging tool for viewing and editing surface
    models and volumes in FreeSurfer. It provides a GUI representation of volumetric
    data and facilitates modifications in the data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TkmeditOutputs`).
    """
    cargs = tkmedit_cargs(params, execution)
    ret = tkmedit_outputs(params, execution)
    execution.run(cargs)
    return ret


def tkmedit(
    input_volume: InputPathType,
    options: str | None = None,
    runner: Runner | None = None,
) -> TkmeditOutputs:
    """
    tkmedit is a multi-functional imaging tool for viewing and editing surface
    models and volumes in FreeSurfer. It provides a GUI representation of volumetric
    data and facilitates modifications in the data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file (e.g., nu.mgz or brain.mgz).
        options: Options for running tkmedit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TkmeditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKMEDIT_METADATA)
    params = tkmedit_params(input_volume=input_volume, options=options)
    return tkmedit_execute(params, execution)


__all__ = [
    "TKMEDIT_METADATA",
    "TkmeditOutputs",
    "TkmeditParameters",
    "tkmedit",
    "tkmedit_params",
]
