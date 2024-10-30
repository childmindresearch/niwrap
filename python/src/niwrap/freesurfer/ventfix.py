# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VENTFIX_METADATA = Metadata(
    id="6078f8fdef3285ea1af571bc8b74f69d88c2c638.boutiques",
    name="ventfix",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class VentfixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ventfix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fixed_ventricles: OutputPathType
    """Output image with fixed ventricles"""


def ventfix(
    subject_dir: str,
    option1: str | None = None,
    runner: Runner | None = None,
) -> VentfixOutputs:
    """
    Tool for fixing ventricles in MRI scans.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Path to the subject's directory containing MRI scans.
        option1: Description of option 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VentfixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VENTFIX_METADATA)
    cargs = []
    cargs.append("ventfix")
    cargs.append(subject_dir)
    if option1 is not None:
        cargs.extend([
            "--option1",
            option1
        ])
    ret = VentfixOutputs(
        root=execution.output_file("."),
        fixed_ventricles=execution.output_file(subject_dir + "/fixed_ventricles.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VENTFIX_METADATA",
    "VentfixOutputs",
    "ventfix",
]