# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURF_PROJ_METADATA = Metadata(
    id="5becd46d13227dddb6e12affa6700ba53c1941a8",
    name="surf_proj",
)


class SurfProjOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_proj(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    projected_output: OutputPathType
    """Output of the projection"""
    output_surface: OutputPathType | None
    """Output surface file"""


def surf_proj(
    data: InputPathType,
    surface: InputPathType,
    output_file: str,
    surface_reference: InputPathType | None = None,
    transform: InputPathType | None = None,
    meshspace: str | None = None,
    step_size: float | int | None = None,
    direction: float | int | None = None,
    operation: str | None = None,
    surface_output: InputPathType | None = None,
    runner: Runner | None = None,
) -> SurfProjOutputs:
    """
    surf_proj by FMRIB Analysis Group, Oxford Centre for Functional MRI of the Brain
    (FMRIB).
    
    Projects data onto a surface mesh using specified parameters.
    
    Args:
        data: Data to project onto surface.
        surface: Surface file.
        output_file: Output file.
        surface_reference: Surface volume reference (default=same as data).
        transform: Data to surface transform (default=Identity).
        meshspace: Mesh space (default='caret').
        step_size: Average over step (mm - default=1).
        direction: If >0 goes towards brain (default=0 i.e. both directions).
        operation: What to do with values: 'mean' (default), 'max', 'median',\
            'last'.
        surface_output: Output surface file, not ASCII matrix (valid only for\
            scalars).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfProjOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_PROJ_METADATA)
    cargs = []
    cargs.append("surf_proj")
    cargs.append("--data")
    cargs.append(execution.input_file(data))
    cargs.append("--surf")
    cargs.append(execution.input_file(surface))
    cargs.append("--out")
    cargs.append(output_file)
    if surface_reference is not None:
        cargs.extend(["--meshref", execution.input_file(surface_reference)])
    if transform is not None:
        cargs.extend(["--xfm", execution.input_file(transform)])
    if meshspace is not None:
        cargs.extend(["--meshspace", meshspace])
    if step_size is not None:
        cargs.extend(["--step", str(step_size)])
    if direction is not None:
        cargs.extend(["--direction", str(direction)])
    if operation is not None:
        cargs.extend(["--operation", operation])
    if surface_output is not None:
        cargs.extend(["--surfout", execution.input_file(surface_output)])
    ret = SurfProjOutputs(
        root=execution.output_file("."),
        projected_output=execution.output_file(f"{output_file}"),
        output_surface=execution.output_file(f"{pathlib.Path(surface_output).name}", optional=True) if surface_output is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_PROJ_METADATA",
    "SurfProjOutputs",
    "surf_proj",
]
