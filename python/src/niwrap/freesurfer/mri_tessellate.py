# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_TESSELLATE_METADATA = Metadata(
    id="9dcf92c1d5089255feba7b2627ab0237e0be1c67.boutiques",
    name="mri_tessellate",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriTessellateParameters = typing.TypedDict('MriTessellateParameters', {
    "__STYX_TYPE__": typing.Literal["mri_tessellate"],
    "input_volume": InputPathType,
    "label_value": int,
    "output_surf": str,
    "different_labels": bool,
    "max_vertices": typing.NotRequired[int | None],
    "real_ras": bool,
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
        "mri_tessellate": mri_tessellate_cargs,
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
        "mri_tessellate": mri_tessellate_outputs,
    }.get(t)


class MriTessellateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_tessellate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """Output file of the tessellation surface, typically ?h.orig."""


def mri_tessellate_params(
    input_volume: InputPathType,
    label_value: int,
    output_surf: str,
    different_labels: bool = False,
    max_vertices: int | None = None,
    real_ras: bool = False,
) -> MriTessellateParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume (e.g., a filled MRI image).
        label_value: Label value for the tessellation. Integer value, if input\
            is filled volume, 127 is rh, 255 is lh.
        output_surf: Binary surface of the tessellation, output file.
        different_labels: Tessellate the surface of all voxels with different\
            labels.
        max_vertices: Set the max number of vertices to nvertices, and the max\
            number of faces to (2 * nvertices).
        real_ras: Save surface with real RAS coordinates where c_(r,a,s) != 0.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_tessellate",
        "input_volume": input_volume,
        "label_value": label_value,
        "output_surf": output_surf,
        "different_labels": different_labels,
        "real_ras": real_ras,
    }
    if max_vertices is not None:
        params["max_vertices"] = max_vertices
    return params


def mri_tessellate_cargs(
    params: MriTessellateParameters,
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
    cargs.append("mri_tessellate")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(str(params.get("label_value")))
    cargs.append(params.get("output_surf"))
    if params.get("different_labels"):
        cargs.append("-a")
    if params.get("max_vertices") is not None:
        cargs.extend([
            "-maxv",
            str(params.get("max_vertices"))
        ])
    if params.get("real_ras"):
        cargs.append("-n")
    return cargs


def mri_tessellate_outputs(
    params: MriTessellateParameters,
    execution: Execution,
) -> MriTessellateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriTessellateOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(params.get("output_surf")),
    )
    return ret


def mri_tessellate_execute(
    params: MriTessellateParameters,
    execution: Execution,
) -> MriTessellateOutputs:
    """
    This program creates a surface by tessellating a given input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriTessellateOutputs`).
    """
    params = execution.params(params)
    cargs = mri_tessellate_cargs(params, execution)
    ret = mri_tessellate_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_tessellate(
    input_volume: InputPathType,
    label_value: int,
    output_surf: str,
    different_labels: bool = False,
    max_vertices: int | None = None,
    real_ras: bool = False,
    runner: Runner | None = None,
) -> MriTessellateOutputs:
    """
    This program creates a surface by tessellating a given input volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume (e.g., a filled MRI image).
        label_value: Label value for the tessellation. Integer value, if input\
            is filled volume, 127 is rh, 255 is lh.
        output_surf: Binary surface of the tessellation, output file.
        different_labels: Tessellate the surface of all voxels with different\
            labels.
        max_vertices: Set the max number of vertices to nvertices, and the max\
            number of faces to (2 * nvertices).
        real_ras: Save surface with real RAS coordinates where c_(r,a,s) != 0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriTessellateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_TESSELLATE_METADATA)
    params = mri_tessellate_params(input_volume=input_volume, label_value=label_value, output_surf=output_surf, different_labels=different_labels, max_vertices=max_vertices, real_ras=real_ras)
    return mri_tessellate_execute(params, execution)


__all__ = [
    "MRI_TESSELLATE_METADATA",
    "MriTessellateOutputs",
    "MriTessellateParameters",
    "mri_tessellate",
    "mri_tessellate_params",
]
