# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FOCI_GET_PROJECTION_VERTEX_METADATA = Metadata(
    id="7a851fbc13b146fb391d13bedfc2eac4da52237a.boutiques",
    name="foci-get-projection-vertex",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
FociGetProjectionVertexParameters = typing.TypedDict('FociGetProjectionVertexParameters', {
    "__STYX_TYPE__": typing.Literal["foci-get-projection-vertex"],
    "foci": InputPathType,
    "surface": InputPathType,
    "metric_out": str,
    "opt_name_name": typing.NotRequired[str | None],
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
        "foci-get-projection-vertex": foci_get_projection_vertex_cargs,
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
        "foci-get-projection-vertex": foci_get_projection_vertex_outputs,
    }.get(t)


class FociGetProjectionVertexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_get_projection_vertex(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def foci_get_projection_vertex_params(
    foci: InputPathType,
    surface: InputPathType,
    metric_out: str,
    opt_name_name: str | None = None,
) -> FociGetProjectionVertexParameters:
    """
    Build parameters.
    
    Args:
        foci: the foci file.
        surface: the surface related to the foci file.
        metric_out: the output metric file.
        opt_name_name: select a focus by name: the name of the focus.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "foci-get-projection-vertex",
        "foci": foci,
        "surface": surface,
        "metric_out": metric_out,
    }
    if opt_name_name is not None:
        params["opt_name_name"] = opt_name_name
    return params


def foci_get_projection_vertex_cargs(
    params: FociGetProjectionVertexParameters,
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
    cargs.append("wb_command")
    cargs.append("-foci-get-projection-vertex")
    cargs.append(execution.input_file(params.get("foci")))
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_name_name") is not None:
        cargs.extend([
            "-name",
            params.get("opt_name_name")
        ])
    return cargs


def foci_get_projection_vertex_outputs(
    params: FociGetProjectionVertexParameters,
    execution: Execution,
) -> FociGetProjectionVertexOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FociGetProjectionVertexOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def foci_get_projection_vertex_execute(
    params: FociGetProjectionVertexParameters,
    execution: Execution,
) -> FociGetProjectionVertexOutputs:
    """
    Get projection vertex for foci.
    
    For each focus, a column is created in <metric-out>, and the vertex with the
    most influence on its projection is assigned a value of 1 in that column,
    with all other vertices 0. If -name is used, only one focus will be used.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FociGetProjectionVertexOutputs`).
    """
    cargs = foci_get_projection_vertex_cargs(params, execution)
    ret = foci_get_projection_vertex_outputs(params, execution)
    execution.run(cargs)
    return ret


def foci_get_projection_vertex(
    foci: InputPathType,
    surface: InputPathType,
    metric_out: str,
    opt_name_name: str | None = None,
    runner: Runner | None = None,
) -> FociGetProjectionVertexOutputs:
    """
    Get projection vertex for foci.
    
    For each focus, a column is created in <metric-out>, and the vertex with the
    most influence on its projection is assigned a value of 1 in that column,
    with all other vertices 0. If -name is used, only one focus will be used.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        foci: the foci file.
        surface: the surface related to the foci file.
        metric_out: the output metric file.
        opt_name_name: select a focus by name: the name of the focus.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociGetProjectionVertexOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_GET_PROJECTION_VERTEX_METADATA)
    params = foci_get_projection_vertex_params(foci=foci, surface=surface, metric_out=metric_out, opt_name_name=opt_name_name)
    return foci_get_projection_vertex_execute(params, execution)


__all__ = [
    "FOCI_GET_PROJECTION_VERTEX_METADATA",
    "FociGetProjectionVertexOutputs",
    "FociGetProjectionVertexParameters",
    "foci_get_projection_vertex",
    "foci_get_projection_vertex_params",
]
