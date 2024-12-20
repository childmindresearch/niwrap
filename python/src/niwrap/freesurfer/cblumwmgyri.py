# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CBLUMWMGYRI_METADATA = Metadata(
    id="fe20341079c6df1e8a587d62997fab1a4bf8a4d8.boutiques",
    name="cblumwmgyri",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class CblumwmgyriOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cblumwmgyri(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_seg_file: OutputPathType | None
    """Output segmentation file after processing"""


def cblumwmgyri(
    subject: str,
    source_seg: InputPathType | None = None,
    n_erodes_dilates: float | None = 2,
    out_seg: str | None = "sourceseg+cblumwmgyri.mgz",
    no_segstats: bool = False,
    subjects_dir: str | None = None,
    runner: Runner | None = None,
) -> CblumwmgyriOutputs:
    """
    Segments cerebellar white matter into gyral and core components using
    geometrical constraints.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        source_seg: Source segmentation file (default: aparc+aseg.mgz).
        n_erodes_dilates: Number of erosions/dilations (default: 2).
        out_seg: Output segmentation file (default: sourceseg+cblumwmgyri.mgz).
        no_segstats: Do not compute segmentation statistics.
        subjects_dir: Subjects directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CblumwmgyriOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CBLUMWMGYRI_METADATA)
    cargs = []
    cargs.append("cblumwmgyri")
    cargs.extend([
        "--s",
        subject
    ])
    if source_seg is not None:
        cargs.extend([
            "--seg",
            execution.input_file(source_seg)
        ])
    if n_erodes_dilates is not None:
        cargs.extend([
            "--n",
            str(n_erodes_dilates)
        ])
    if out_seg is not None:
        cargs.extend([
            "--o",
            out_seg
        ])
    if no_segstats:
        cargs.append("--no-segstats")
    if subjects_dir is not None:
        cargs.extend([
            "--sd",
            subjects_dir
        ])
    ret = CblumwmgyriOutputs(
        root=execution.output_file("."),
        output_seg_file=execution.output_file(out_seg) if (out_seg is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CBLUMWMGYRI_METADATA",
    "CblumwmgyriOutputs",
    "cblumwmgyri",
]
