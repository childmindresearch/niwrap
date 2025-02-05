# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_ANATOMI_CUTS_METADATA = Metadata(
    id="b3ae6660625cd9a73409943ca03518bf3c1e8760.boutiques",
    name="dmri_AnatomiCuts",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriAnatomiCutsParameters = typing.TypedDict('DmriAnatomiCutsParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_AnatomiCuts"],
    "segmentation_file": InputPathType,
    "fiber_file": InputPathType,
    "clusters": float,
    "points": float,
    "fibers_eigen": float,
    "output_folder": str,
    "direction_flag": typing.Literal["s", "d", "a", "o"],
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
        "dmri_AnatomiCuts": dmri_anatomi_cuts_cargs,
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
        "dmri_AnatomiCuts": dmri_anatomi_cuts_outputs,
    }
    return vt.get(t)


class DmriAnatomiCutsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_anatomi_cuts(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vtk: OutputPathType
    """Output VTK file of the segmentation"""


def dmri_anatomi_cuts_params(
    segmentation_file: InputPathType,
    fiber_file: InputPathType,
    clusters: float,
    points: float,
    fibers_eigen: float,
    output_folder: str,
    direction_flag: typing.Literal["s", "d", "a", "o"],
) -> DmriAnatomiCutsParameters:
    """
    Build parameters.
    
    Args:
        segmentation_file: Segmentation file.
        fiber_file: VTK fiber file.
        clusters: Number of clusters.
        points: Number of points.
        fibers_eigen: Number of fibers for eigen decomposition.
        output_folder: Output folder.
        direction_flag: Direction flag: 's' for straight, 'd' for diagonal, 'a'\
            for all, 'o' for none.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_AnatomiCuts",
        "segmentation_file": segmentation_file,
        "fiber_file": fiber_file,
        "clusters": clusters,
        "points": points,
        "fibers_eigen": fibers_eigen,
        "output_folder": output_folder,
        "direction_flag": direction_flag,
    }
    return params


def dmri_anatomi_cuts_cargs(
    params: DmriAnatomiCutsParameters,
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
    cargs.append("dmri_AnatomiCuts")
    cargs.extend([
        "-s",
        execution.input_file(params.get("segmentation_file"))
    ])
    cargs.extend([
        "-f",
        execution.input_file(params.get("fiber_file"))
    ])
    cargs.extend([
        "-c",
        str(params.get("clusters"))
    ])
    cargs.extend([
        "-n",
        str(params.get("points"))
    ])
    cargs.extend([
        "-e",
        str(params.get("fibers_eigen"))
    ])
    cargs.extend([
        "-o",
        params.get("output_folder")
    ])
    cargs.extend([
        "-d",
        params.get("direction_flag")
    ])
    return cargs


def dmri_anatomi_cuts_outputs(
    params: DmriAnatomiCutsParameters,
    execution: Execution,
) -> DmriAnatomiCutsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriAnatomiCutsOutputs(
        root=execution.output_file("."),
        output_vtk=execution.output_file(params.get("output_folder") + "/output.vtk"),
    )
    return ret


def dmri_anatomi_cuts_execute(
    params: DmriAnatomiCutsParameters,
    execution: Execution,
) -> DmriAnatomiCutsOutputs:
    """
    AnatomiCuts tool for DTI fibers segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriAnatomiCutsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dmri_anatomi_cuts_cargs(params, execution)
    ret = dmri_anatomi_cuts_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_anatomi_cuts(
    segmentation_file: InputPathType,
    fiber_file: InputPathType,
    clusters: float,
    points: float,
    fibers_eigen: float,
    output_folder: str,
    direction_flag: typing.Literal["s", "d", "a", "o"],
    runner: Runner | None = None,
) -> DmriAnatomiCutsOutputs:
    """
    AnatomiCuts tool for DTI fibers segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        segmentation_file: Segmentation file.
        fiber_file: VTK fiber file.
        clusters: Number of clusters.
        points: Number of points.
        fibers_eigen: Number of fibers for eigen decomposition.
        output_folder: Output folder.
        direction_flag: Direction flag: 's' for straight, 'd' for diagonal, 'a'\
            for all, 'o' for none.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriAnatomiCutsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_ANATOMI_CUTS_METADATA)
    params = dmri_anatomi_cuts_params(segmentation_file=segmentation_file, fiber_file=fiber_file, clusters=clusters, points=points, fibers_eigen=fibers_eigen, output_folder=output_folder, direction_flag=direction_flag)
    return dmri_anatomi_cuts_execute(params, execution)


__all__ = [
    "DMRI_ANATOMI_CUTS_METADATA",
    "DmriAnatomiCutsOutputs",
    "DmriAnatomiCutsParameters",
    "dmri_anatomi_cuts",
    "dmri_anatomi_cuts_params",
]
