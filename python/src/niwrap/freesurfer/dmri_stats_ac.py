# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_STATS_AC_METADATA = Metadata(
    id="38bce967cfc9907f2f4aad1d1246fa98b24d0792.boutiques",
    name="dmri_stats_ac",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriStatsAcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_stats_ac(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output of the dMRI statistical analysis"""


def dmri_stats_ac(
    anatomicuts_folder: str,
    num_clusters: int,
    correspondence_file: str,
    measures: list[str],
    output_file: str,
    runner: Runner | None = None,
) -> DmriStatsAcOutputs:
    """
    The tool 'dmri_stats_ac' performs statistical analysis on dMRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        anatomicuts_folder: Input folder containing anatomicuts data.
        num_clusters: Number of clusters for analysis.
        correspondence_file: File specifying correspondence details.
        measures: Number of measures followed by each measure name and file.
        output_file: Output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriStatsAcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_STATS_AC_METADATA)
    cargs = []
    cargs.append("dmri_stats_ac")
    cargs.extend([
        "-i",
        anatomicuts_folder
    ])
    cargs.extend([
        "-n",
        str(num_clusters)
    ])
    cargs.extend([
        "-c",
        correspondence_file
    ])
    cargs.append("-m")
    cargs.append("[NUM_MEASURES]")
    cargs.extend([
        "-m",
        *measures
    ])
    cargs.extend([
        "-o",
        output_file
    ])
    ret = DmriStatsAcOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_STATS_AC_METADATA",
    "DmriStatsAcOutputs",
    "dmri_stats_ac",
]
