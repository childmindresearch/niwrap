# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

JKGCATRAIN_METADATA = Metadata(
    id="9a38b64221a25b990a7d0af6bcb52cf21f4a0120.boutiques",
    name="jkgcatrain",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class JkgcatrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `jkgcatrain(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def jkgcatrain(
    gca_directory: str,
    iteration_number: float | None = 2,
    num_threads: float | None = None,
    no_submit: bool = False,
    mail_flag: bool = False,
    runner: Runner | None = None,
) -> JkgcatrainOutputs:
    """
    Jackknife training of GCA using existing output from gcatrain.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gca_directory: Output directory from gcatrain.
        iteration_number: Iteration number (usually 2).
        num_threads: Number of threads to use.
        no_submit: Run serially, do not use pbsubmit.
        mail_flag: Mail to user when jobs are pbsubmitted or finished.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `JkgcatrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(JKGCATRAIN_METADATA)
    cargs = []
    cargs.append("jkgcatrain")
    cargs.extend([
        "--g",
        gca_directory
    ])
    if iteration_number is not None:
        cargs.extend([
            "--iter",
            str(iteration_number)
        ])
    if num_threads is not None:
        cargs.extend([
            "--nthreads",
            str(num_threads)
        ])
    if no_submit:
        cargs.append("--no-submit")
    if mail_flag:
        cargs.append("--pb-m")
    ret = JkgcatrainOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "JKGCATRAIN_METADATA",
    "JkgcatrainOutputs",
    "jkgcatrain",
]
