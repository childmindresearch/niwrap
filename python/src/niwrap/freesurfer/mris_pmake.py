# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_PMAKE_METADATA = Metadata(
    id="dd00ff607795956546fa917b74a471d7811886b3.boutiques",
    name="mris_pmake",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisPmakeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_pmake(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_pmake(
    subject: str,
    hemisphere: str,
    options_file: str | None = "options.txt",
    working_dir: str | None = ".",
    listen_mode: bool = False,
    listen_on_port: float | None = None,
    surface0: str | None = "inflated",
    surface1: str | None = "smoothwm",
    curve0: str | None = "smoothwm.H.crv",
    curve1: str | None = "sulc",
    use_abs_curvs: bool = False,
    mpm_prog: str | None = None,
    mpm_args: str | None = None,
    runner: Runner | None = None,
) -> MrisPmakeOutputs:
    """
    Calculates paths and related costs on FreeSurfer surfaces based on an edge cost
    and Dijkstra's algorithm.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Set the subject to <subj>.
        hemisphere: The hemisphere to process.
        options_file: The main configuration file specifying the startup\
            run-time behaviour.
        working_dir: The working directory.
        listen_mode: Start in LISTEN mode without calculating a path.
        listen_on_port: Create the server port on specified port and do nothing\
            else.
        surface0: The main mesh surface to read.
        surface1: The aux mesh surface to read.
        curve0: The main curvature function maps.
        curve1: The aux curvature function maps.
        use_abs_curvs: Use absolute values on each curvature map.
        mpm_prog: The mpmProg to run.
        mpm_args: Arguments for the specified mpmProg.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisPmakeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_PMAKE_METADATA)
    cargs = []
    cargs.append("mris_pmake")
    if options_file is not None:
        cargs.extend([
            "--optionsFile",
            options_file
        ])
    if working_dir is not None:
        cargs.extend([
            "--dir",
            working_dir
        ])
    if listen_mode:
        cargs.append("--listen")
    if listen_on_port is not None:
        cargs.extend([
            "--listenOnPort",
            str(listen_on_port)
        ])
    cargs.extend([
        "--subject",
        subject
    ])
    cargs.extend([
        "--hemi",
        hemisphere
    ])
    if surface0 is not None:
        cargs.extend([
            "--surface0",
            surface0
        ])
    if surface1 is not None:
        cargs.extend([
            "--surface1",
            surface1
        ])
    if curve0 is not None:
        cargs.extend([
            "--curve0",
            curve0
        ])
    if curve1 is not None:
        cargs.extend([
            "--curve1",
            curve1
        ])
    if use_abs_curvs:
        cargs.append("--useAbsCurvs")
    if mpm_prog is not None:
        cargs.extend([
            "--mpmProg",
            mpm_prog
        ])
    if mpm_args is not None:
        cargs.extend([
            "--mpmArgs",
            mpm_args
        ])
    ret = MrisPmakeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_PMAKE_METADATA",
    "MrisPmakeOutputs",
    "mris_pmake",
]
