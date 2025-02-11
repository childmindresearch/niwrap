# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SURF2VTK_METADATA = Metadata(
    id="bfca7ed52c97191303bf209f7690859dfe93b483.boutiques",
    name="mris_surf2vtk",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSurf2vtkParameters = typing.TypedDict('MrisSurf2vtkParameters', {
    "__STYX_TYPE__": typing.Literal["mris_surf2vtk"],
    "input_surface": InputPathType,
    "output_surface": str,
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
        "mris_surf2vtk": mris_surf2vtk_cargs,
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
        "mris_surf2vtk": mris_surf2vtk_outputs,
    }.get(t)


class MrisSurf2vtkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_surf2vtk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    vtk_surface: OutputPathType
    """Output surface file converted to VTK format"""


def mris_surf2vtk_params(
    input_surface: InputPathType,
    output_surface: str,
) -> MrisSurf2vtkParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        output_surface: Output surface file in VTK format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_surf2vtk",
        "input_surface": input_surface,
        "output_surface": output_surface,
    }
    return params


def mris_surf2vtk_cargs(
    params: MrisSurf2vtkParameters,
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
    cargs.append("mris_surf2vtk")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_surface"))
    ])
    cargs.extend([
        "-o",
        params.get("output_surface")
    ])
    return cargs


def mris_surf2vtk_outputs(
    params: MrisSurf2vtkParameters,
    execution: Execution,
) -> MrisSurf2vtkOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSurf2vtkOutputs(
        root=execution.output_file("."),
        vtk_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_surf2vtk_execute(
    params: MrisSurf2vtkParameters,
    execution: Execution,
) -> MrisSurf2vtkOutputs:
    """
    Conversion tool to convert surface files to VTK format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSurf2vtkOutputs`).
    """
    cargs = mris_surf2vtk_cargs(params, execution)
    ret = mris_surf2vtk_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_surf2vtk(
    input_surface: InputPathType,
    output_surface: str,
    runner: Runner | None = None,
) -> MrisSurf2vtkOutputs:
    """
    Conversion tool to convert surface files to VTK format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        output_surface: Output surface file in VTK format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSurf2vtkOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SURF2VTK_METADATA)
    params = mris_surf2vtk_params(input_surface=input_surface, output_surface=output_surface)
    return mris_surf2vtk_execute(params, execution)


__all__ = [
    "MRIS_SURF2VTK_METADATA",
    "MrisSurf2vtkOutputs",
    "MrisSurf2vtkParameters",
    "mris_surf2vtk",
    "mris_surf2vtk_params",
]
