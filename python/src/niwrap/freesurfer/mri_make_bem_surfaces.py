# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_MAKE_BEM_SURFACES_METADATA = Metadata(
    id="991d0fd0e24d64260bc9d9bb27cd91c24fb07fb0.boutiques",
    name="mri_make_bem_surfaces",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriMakeBemSurfacesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_make_bem_surfaces(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inner_skull_tri: OutputPathType
    """Generated inner skull surface triangle file."""
    inner_skull_tmp_tri: OutputPathType
    """Temporary file for best guess at inner skull surface."""


def mri_make_bem_surfaces(
    name: str,
    mfile: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriMakeBemSurfacesOutputs:
    """
    Tool to create Boundary Element Method (BEM) surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        name: The name of the subject or session to process.
        mfile: Optional mfile parameter to provide additional settings.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMakeBemSurfacesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MAKE_BEM_SURFACES_METADATA)
    cargs = []
    cargs.append("mri_make_bem_surfaces")
    cargs.append(name)
    if mfile is not None:
        cargs.append(execution.input_file(mfile))
    ret = MriMakeBemSurfacesOutputs(
        root=execution.output_file("."),
        inner_skull_tri=execution.output_file("inner_skull.tri"),
        inner_skull_tmp_tri=execution.output_file("inner_skull_tmp.tri"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_MAKE_BEM_SURFACES_METADATA",
    "MriMakeBemSurfacesOutputs",
    "mri_make_bem_surfaces",
]
