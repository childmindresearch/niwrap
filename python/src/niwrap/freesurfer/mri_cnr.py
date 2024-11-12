# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CNR_METADATA = Metadata(
    id="e426f06fe9ac260492b56203731c6940db9a022d.boutiques",
    name="mri_cnr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriCnrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cnr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_cnr(
    surf_dir: str,
    volume_files: list[InputPathType],
    slope: list[str] | None = None,
    logfile: str | None = None,
    labels: list[str] | None = None,
    print_total_cnr: bool = False,
    version_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> MriCnrOutputs:
    """
    Compute the gray/white/csf contrast-to-noise ratio for volumes using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surf_dir: Directory containing surface data.
        volume_files: Volumes to process.
        slope: Compute slope and write to files labeled with slope_fname.\
            Requires four additional values: dist_in, dist_out, step_in, and\
            step_out.
        logfile: Log CNR to specified logfile. Will contain 8 values in a\
            specific order: gray_white_cnr, gray_csf_cnr, white_mean, gray_mean,\
            csf_mean, sqrt(white_var), sqrt(gray_var), sqrt(csf_var).
        labels: Read hemisphere labels from specified left and right hemisphere\
            files.
        print_total_cnr: Print only the total CNR to stdout.
        version_flag: Print software version information and quit.
        help_flag: Print usage information and quit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCnrOutputs`).
    """
    if slope is not None and (len(slope) != 5): 
        raise ValueError(f"Length of 'slope' must be 5 but was {len(slope)}")
    if labels is not None and (len(labels) != 2): 
        raise ValueError(f"Length of 'labels' must be 2 but was {len(labels)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CNR_METADATA)
    cargs = []
    cargs.append("mri_cnr")
    cargs.append(surf_dir)
    cargs.extend([execution.input_file(f) for f in volume_files])
    if slope is not None:
        cargs.extend([
            "-s",
            *slope
        ])
    if logfile is not None:
        cargs.extend([
            "-l",
            logfile
        ])
    if labels is not None:
        cargs.extend([
            "label",
            *labels
        ])
    if print_total_cnr:
        cargs.append("-t")
    if version_flag:
        cargs.append("-version")
    if help_flag:
        cargs.append("-help")
    ret = MriCnrOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_CNR_METADATA",
    "MriCnrOutputs",
    "mri_cnr",
]