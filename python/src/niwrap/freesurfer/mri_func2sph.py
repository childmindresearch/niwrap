# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_FUNC2SPH_METADATA = Metadata(
    id="07527586a882465863cf7ef1f979d3d044731e6d.boutiques",
    name="mri-func2sph",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriFunc2sphOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_func2sph(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_func2sph(
    instem: str,
    outstem: str,
    hemisphere: typing.Literal["lh", "rh"],
    fvitdir: str,
    hole_filling_iters: float | None = 100,
    icosahedron_size: float | None = 10242,
    input_type: str | None = None,
    umask: str | None = None,
    runner: Runner | None = None,
) -> MriFunc2sphOutputs:
    """
    Maps functional data from volume space to spherical surface space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        instem: Input file stem.
        outstem: Output file stem.
        hemisphere: Hemisphere to process, can be 'lh' or 'rh'.
        fvitdir: Functional vertex information directory.
        hole_filling_iters: Number of hole-filling iterations.
        icosahedron_size: Size of the icosahedron.
        input_type: Type of input data, will be auto-detected if not specified.
        umask: New umask value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFunc2sphOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FUNC2SPH_METADATA)
    cargs = []
    cargs.append("mri-func2sph")
    cargs.extend([
        "-i",
        instem
    ])
    cargs.extend([
        "-o",
        outstem
    ])
    cargs.extend([
        "-hemi",
        hemisphere
    ])
    cargs.extend([
        "-fvitdir",
        fvitdir
    ])
    if hole_filling_iters is not None:
        cargs.extend([
            "-niters",
            str(hole_filling_iters)
        ])
    if icosahedron_size is not None:
        cargs.extend([
            "-icosize",
            str(icosahedron_size)
        ])
    if input_type is not None:
        cargs.extend([
            "-intype",
            input_type
        ])
    if umask is not None:
        cargs.extend([
            "-umask",
            umask
        ])
    ret = MriFunc2sphOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_FUNC2SPH_METADATA",
    "MriFunc2sphOutputs",
    "mri_func2sph",
]
