# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_MULTIMODAL_SURFACE_PLACEMENT_METADATA = Metadata(
    id="0cfb3e00bbd6f85769e241237d86c23951a65897.boutiques",
    name="mris_multimodal_surface_placement",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisMultimodalSurfacePlacementParameters = typing.TypedDict('MrisMultimodalSurfacePlacementParameters', {
    "__STYX_TYPE__": typing.Literal["mris_multimodal_surface_placement"],
    "input_surface": InputPathType,
    "output_surface": InputPathType,
    "sphere_surface": InputPathType,
    "normals": str,
    "values": str,
    "debug_vertex": typing.NotRequired[float | None],
    "step_size": float,
    "number_of_steps": float,
    "gradient_sigma": float,
    "aseg_aparc": InputPathType,
    "white_surface": InputPathType,
    "prob_of_csf": float,
    "t1_image": InputPathType,
    "t2_image": InputPathType,
    "flair_image": InputPathType,
    "min_max": bool,
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
        "mris_multimodal_surface_placement": mris_multimodal_surface_placement_cargs,
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


class MrisMultimodalSurfacePlacementOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_multimodal_surface_placement(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_multimodal_surface_placement_params(
    input_surface: InputPathType,
    output_surface: InputPathType,
    sphere_surface: InputPathType,
    normals: str,
    values_: str,
    step_size: float,
    number_of_steps: float,
    gradient_sigma: float,
    aseg_aparc: InputPathType,
    white_surface: InputPathType,
    prob_of_csf: float,
    t1_image: InputPathType,
    t2_image: InputPathType,
    flair_image: InputPathType,
    debug_vertex: float | None = None,
    min_max: bool = False,
) -> MrisMultimodalSurfacePlacementParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        output_surface: Output surface file.
        sphere_surface: Sphere surface file.
        normals: Normals file in VTK format.
        values_: Values file in VTK format.
        step_size: Step size.
        number_of_steps: Number of steps.
        gradient_sigma: Gradient sigma value.
        aseg_aparc: ASEG APARC image file.
        white_surface: White surface file.
        prob_of_csf: Probability of CSF.
        t1_image: T1-weighted image file.
        t2_image: T2-weighted image file.
        flair_image: FLAIR image file.
        debug_vertex: Debug vertex index.
        min_max: Toggle between min or max operation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_multimodal_surface_placement",
        "input_surface": input_surface,
        "output_surface": output_surface,
        "sphere_surface": sphere_surface,
        "normals": normals,
        "values": values_,
        "step_size": step_size,
        "number_of_steps": number_of_steps,
        "gradient_sigma": gradient_sigma,
        "aseg_aparc": aseg_aparc,
        "white_surface": white_surface,
        "prob_of_csf": prob_of_csf,
        "t1_image": t1_image,
        "t2_image": t2_image,
        "flair_image": flair_image,
        "min_max": min_max,
    }
    if debug_vertex is not None:
        params["debug_vertex"] = debug_vertex
    return params


def mris_multimodal_surface_placement_cargs(
    params: MrisMultimodalSurfacePlacementParameters,
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
    cargs.append("mris_multimodal_surface_placement")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_surface"))
    ])
    cargs.extend([
        "-o",
        execution.input_file(params.get("output_surface"))
    ])
    cargs.extend([
        "-b",
        execution.input_file(params.get("sphere_surface"))
    ])
    cargs.extend([
        "-n",
        params.get("normals")
    ])
    cargs.extend([
        "-v",
        params.get("values")
    ])
    if params.get("debug_vertex") is not None:
        cargs.extend([
            "-d",
            str(params.get("debug_vertex"))
        ])
    cargs.extend([
        "-s",
        str(params.get("step_size"))
    ])
    cargs.extend([
        "-k",
        str(params.get("number_of_steps"))
    ])
    cargs.extend([
        "-g",
        str(params.get("gradient_sigma"))
    ])
    cargs.extend([
        "-a",
        execution.input_file(params.get("aseg_aparc"))
    ])
    cargs.extend([
        "-w",
        execution.input_file(params.get("white_surface"))
    ])
    cargs.extend([
        "-p",
        str(params.get("prob_of_csf"))
    ])
    cargs.extend([
        "-t1",
        execution.input_file(params.get("t1_image"))
    ])
    cargs.extend([
        "-t2",
        execution.input_file(params.get("t2_image"))
    ])
    cargs.extend([
        "-flair",
        execution.input_file(params.get("flair_image"))
    ])
    if params.get("min_max"):
        cargs.append("-min/max")
    return cargs


def mris_multimodal_surface_placement_outputs(
    params: MrisMultimodalSurfacePlacementParameters,
    execution: Execution,
) -> MrisMultimodalSurfacePlacementOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMultimodalSurfacePlacementOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_multimodal_surface_placement_execute(
    params: MrisMultimodalSurfacePlacementParameters,
    execution: Execution,
) -> MrisMultimodalSurfacePlacementOutputs:
    """
    FreeSurfer command for multimodal surface placement.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMultimodalSurfacePlacementOutputs`).
    """
    cargs = mris_multimodal_surface_placement_cargs(params, execution)
    ret = mris_multimodal_surface_placement_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_multimodal_surface_placement(
    input_surface: InputPathType,
    output_surface: InputPathType,
    sphere_surface: InputPathType,
    normals: str,
    values_: str,
    step_size: float,
    number_of_steps: float,
    gradient_sigma: float,
    aseg_aparc: InputPathType,
    white_surface: InputPathType,
    prob_of_csf: float,
    t1_image: InputPathType,
    t2_image: InputPathType,
    flair_image: InputPathType,
    debug_vertex: float | None = None,
    min_max: bool = False,
    runner: Runner | None = None,
) -> MrisMultimodalSurfacePlacementOutputs:
    """
    FreeSurfer command for multimodal surface placement.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        output_surface: Output surface file.
        sphere_surface: Sphere surface file.
        normals: Normals file in VTK format.
        values_: Values file in VTK format.
        step_size: Step size.
        number_of_steps: Number of steps.
        gradient_sigma: Gradient sigma value.
        aseg_aparc: ASEG APARC image file.
        white_surface: White surface file.
        prob_of_csf: Probability of CSF.
        t1_image: T1-weighted image file.
        t2_image: T2-weighted image file.
        flair_image: FLAIR image file.
        debug_vertex: Debug vertex index.
        min_max: Toggle between min or max operation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMultimodalSurfacePlacementOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MULTIMODAL_SURFACE_PLACEMENT_METADATA)
    params = mris_multimodal_surface_placement_params(input_surface=input_surface, output_surface=output_surface, sphere_surface=sphere_surface, normals=normals, values_=values_, debug_vertex=debug_vertex, step_size=step_size, number_of_steps=number_of_steps, gradient_sigma=gradient_sigma, aseg_aparc=aseg_aparc, white_surface=white_surface, prob_of_csf=prob_of_csf, t1_image=t1_image, t2_image=t2_image, flair_image=flair_image, min_max=min_max)
    return mris_multimodal_surface_placement_execute(params, execution)


__all__ = [
    "MRIS_MULTIMODAL_SURFACE_PLACEMENT_METADATA",
    "MrisMultimodalSurfacePlacementOutputs",
    "MrisMultimodalSurfacePlacementParameters",
    "mris_multimodal_surface_placement",
    "mris_multimodal_surface_placement_params",
]
