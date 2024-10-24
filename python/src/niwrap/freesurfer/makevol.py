# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKEVOL_METADATA = Metadata(
    id="b095c7a5e6e89f542d67def46cd9241f840756fe.boutiques",
    name="makevol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MakevolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `makevol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """The created volume file."""


def makevol(
    filename: str | None = "new_volume.mgz",
    width: int | None = 256,
    height: int | None = 256,
    depth: int | None = 256,
    sizex: float | None = 1.0,
    sizey: float | None = 1.0,
    sizez: float | None = 1.0,
    set_method: str | None = "xyz",
    runner: Runner | None = None,
) -> MakevolOutputs:
    """
    A tool to create a volume with given parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        filename: Write volume to the given file name, implying type.
        width: Use integer WIDTH as the x dimension.
        height: Use integer HEIGHT as the y dimension.
        depth: Use integer DEPTH as the z dimension.
        sizex: Use float SIZEX as the x resolution.
        sizey: Use float SIZEY as the y resolution.
        sizez: Use float SIZEZ as the z resolution.
        set_method: Use METHOD to fill the values. Methods: xyz, random,\
            constant.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakevolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKEVOL_METADATA)
    cargs = []
    cargs.append("makevol")
    if filename is not None:
        cargs.extend([
            "-f",
            filename
        ])
    if width is not None:
        cargs.extend([
            "-x",
            str(width)
        ])
    if height is not None:
        cargs.extend([
            "-y",
            str(height)
        ])
    if depth is not None:
        cargs.extend([
            "-z",
            str(depth)
        ])
    if sizex is not None:
        cargs.extend([
            "--sizex",
            str(sizex)
        ])
    if sizey is not None:
        cargs.extend([
            "--sizey",
            str(sizey)
        ])
    if sizez is not None:
        cargs.extend([
            "--sizez",
            str(sizez)
        ])
    if set_method is not None:
        cargs.extend([
            "--set-method",
            set_method
        ])
    ret = MakevolOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(filename) if (filename is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKEVOL_METADATA",
    "MakevolOutputs",
    "makevol",
]
