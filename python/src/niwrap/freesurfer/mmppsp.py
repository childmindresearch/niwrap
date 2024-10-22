# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MMPPSP_METADATA = Metadata(
    id="daa297d5819cc2a0b9822e3d8dba8f2c0cf6ddec.boutiques",
    name="mmppsp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MmppspOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mmppsp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType
    """Output surface files"""


def mmppsp(
    samseg_dir: str,
    outdir: str,
    lh_flag: bool = False,
    rh_flag: bool = False,
    likelihood_flag: bool = False,
    posterior_flag: bool = False,
    force_update_flag: bool = False,
    threads: float | None = None,
    no_initsphreg_flag: bool = False,
    stop_after: str | None = None,
    wexpanddist: float | None = None,
    runner: Runner | None = None,
) -> MmppspOutputs:
    """
    MultiModal Posterior Probability Surface Placement.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        samseg_dir: Directory containing Samseg output.
        outdir: Output directory for the results.
        lh_flag: Process left hemisphere.
        rh_flag: Process right hemisphere.
        likelihood_flag: Use likelihood for surface placement.
        posterior_flag: Use posteriors instead of likelihood for surface\
            placement.
        force_update_flag: Force update the surface placement.
        threads: Number of threads to use.
        no_initsphreg_flag: Do not use talairach.lta to initialize rotation.
        stop_after: Stop the processing after a specified step.
        wexpanddist: Distance to expand white surface to initialize pial (in\
            mm).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MmppspOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MMPPSP_METADATA)
    cargs = []
    cargs.append("mmppsp")
    cargs.extend([
        "--samseg",
        samseg_dir
    ])
    cargs.extend([
        "--o",
        outdir
    ])
    if lh_flag:
        cargs.append("--lh")
    if rh_flag:
        cargs.append("--rh")
    if likelihood_flag:
        cargs.append("--likelihood")
    if posterior_flag:
        cargs.append("--posterior")
    if force_update_flag:
        cargs.append("--force-update")
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if no_initsphreg_flag:
        cargs.append("--no-initsphreg")
    if stop_after is not None:
        cargs.extend([
            "--stop-after",
            stop_after
        ])
    if wexpanddist is not None:
        cargs.extend([
            "--wexpanddist",
            str(wexpanddist)
        ])
    ret = MmppspOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file(outdir + "/surf"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MMPPSP_METADATA",
    "MmppspOutputs",
    "mmppsp",
]