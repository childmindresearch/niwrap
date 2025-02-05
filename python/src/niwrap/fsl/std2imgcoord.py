# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STD2IMGCOORD_METADATA = Metadata(
    id="05322cde0f0612798367ff4b15825c44466bc700.boutiques",
    name="std2imgcoord",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Std2imgcoordParameters = typing.TypedDict('Std2imgcoordParameters', {
    "__STYX_TYPE__": typing.Literal["std2imgcoord"],
    "filename_coordinates": InputPathType,
    "standard_image": typing.NotRequired[InputPathType | None],
    "input_image": InputPathType,
    "affine_transform": typing.NotRequired[InputPathType | None],
    "warp_field": typing.NotRequired[InputPathType | None],
    "prewarp_affine_transform": typing.NotRequired[InputPathType | None],
    "output_mm": bool,
    "output_vox": bool,
    "verbose": bool,
    "more_verbose": bool,
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
        "std2imgcoord": std2imgcoord_cargs,
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


class Std2imgcoordOutputs(typing.NamedTuple):
    """
    Output object returned when calling `std2imgcoord(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def std2imgcoord_params(
    filename_coordinates: InputPathType,
    input_image: InputPathType,
    standard_image: InputPathType | None = None,
    affine_transform: InputPathType | None = None,
    warp_field: InputPathType | None = None,
    prewarp_affine_transform: InputPathType | None = None,
    output_mm: bool = False,
    output_vox: bool = False,
    verbose: bool = False,
    more_verbose: bool = False,
) -> Std2imgcoordParameters:
    """
    Build parameters.
    
    Args:
        filename_coordinates: Path to the filename containing coordinates or\
            '-' to read from standard input.
        input_image: Filename of input image.
        standard_image: Filename of standard image.
        affine_transform: Filename of affine transform (e.g.\
            example_func2standard.mat).
        warp_field: Filename of warpfield (e.g. highres2standard_warp.nii.gz).
        prewarp_affine_transform: Filename of pre-warp affine transform (e.g.\
            example_func2highres.mat). Defaults to identity matrix.
        output_mm: Outputs coordinates in mm (default).
        output_vox: Outputs coordinates in voxels.
        verbose: Verbose output.
        more_verbose: More verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "std2imgcoord",
        "filename_coordinates": filename_coordinates,
        "input_image": input_image,
        "output_mm": output_mm,
        "output_vox": output_vox,
        "verbose": verbose,
        "more_verbose": more_verbose,
    }
    if standard_image is not None:
        params["standard_image"] = standard_image
    if affine_transform is not None:
        params["affine_transform"] = affine_transform
    if warp_field is not None:
        params["warp_field"] = warp_field
    if prewarp_affine_transform is not None:
        params["prewarp_affine_transform"] = prewarp_affine_transform
    return params


def std2imgcoord_cargs(
    params: Std2imgcoordParameters,
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
    cargs.append("std2imgcoord")
    cargs.append(execution.input_file(params.get("filename_coordinates")))
    if params.get("standard_image") is not None:
        cargs.extend([
            "-std",
            execution.input_file(params.get("standard_image"))
        ])
    cargs.extend([
        "-img",
        execution.input_file(params.get("input_image"))
    ])
    if params.get("affine_transform") is not None:
        cargs.extend([
            "-xfm",
            execution.input_file(params.get("affine_transform"))
        ])
    if params.get("warp_field") is not None:
        cargs.extend([
            "-warp",
            execution.input_file(params.get("warp_field"))
        ])
    if params.get("prewarp_affine_transform") is not None:
        cargs.extend([
            "-premat",
            execution.input_file(params.get("prewarp_affine_transform"))
        ])
    if params.get("output_mm"):
        cargs.append("-mm")
    if params.get("output_vox"):
        cargs.append("-vox")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("more_verbose"):
        cargs.append("-verbose")
    return cargs


def std2imgcoord_outputs(
    params: Std2imgcoordParameters,
    execution: Execution,
) -> Std2imgcoordOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Std2imgcoordOutputs(
        root=execution.output_file("."),
    )
    return ret


def std2imgcoord_execute(
    params: Std2imgcoordParameters,
    execution: Execution,
) -> Std2imgcoordOutputs:
    """
    Convert standard space coordinates to image space coordinates.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Std2imgcoordOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = std2imgcoord_cargs(params, execution)
    ret = std2imgcoord_outputs(params, execution)
    execution.run(cargs)
    return ret


def std2imgcoord(
    filename_coordinates: InputPathType,
    input_image: InputPathType,
    standard_image: InputPathType | None = None,
    affine_transform: InputPathType | None = None,
    warp_field: InputPathType | None = None,
    prewarp_affine_transform: InputPathType | None = None,
    output_mm: bool = False,
    output_vox: bool = False,
    verbose: bool = False,
    more_verbose: bool = False,
    runner: Runner | None = None,
) -> Std2imgcoordOutputs:
    """
    Convert standard space coordinates to image space coordinates.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        filename_coordinates: Path to the filename containing coordinates or\
            '-' to read from standard input.
        input_image: Filename of input image.
        standard_image: Filename of standard image.
        affine_transform: Filename of affine transform (e.g.\
            example_func2standard.mat).
        warp_field: Filename of warpfield (e.g. highres2standard_warp.nii.gz).
        prewarp_affine_transform: Filename of pre-warp affine transform (e.g.\
            example_func2highres.mat). Defaults to identity matrix.
        output_mm: Outputs coordinates in mm (default).
        output_vox: Outputs coordinates in voxels.
        verbose: Verbose output.
        more_verbose: More verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Std2imgcoordOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STD2IMGCOORD_METADATA)
    params = std2imgcoord_params(filename_coordinates=filename_coordinates, standard_image=standard_image, input_image=input_image, affine_transform=affine_transform, warp_field=warp_field, prewarp_affine_transform=prewarp_affine_transform, output_mm=output_mm, output_vox=output_vox, verbose=verbose, more_verbose=more_verbose)
    return std2imgcoord_execute(params, execution)


__all__ = [
    "STD2IMGCOORD_METADATA",
    "Std2imgcoordOutputs",
    "Std2imgcoordParameters",
    "std2imgcoord",
    "std2imgcoord_params",
]
