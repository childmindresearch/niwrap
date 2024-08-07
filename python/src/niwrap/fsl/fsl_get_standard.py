# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_GET_STANDARD_METADATA = Metadata(
    id="11477c85326fcd13c2ec9e9d80ff45d5231efc93",
    name="fsl_get_standard",
)


class FslGetStandardOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_get_standard(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_get_standard(
    image_type: typing.Literal["whole_head", "brain", "brain_mask"],
    resolution: float | int | None = None,
    verbose_flag: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> FslGetStandardOutputs:
    """
    fsl_get_standard.
    
    Generate paths to FSL standard space images.
    
    Args:
        image_type: Image type - one of 'whole_head' (the default), 'brain', or\
            'brain_mask'.
        resolution: Desired isotropic resolution in millimetres.
        verbose_flag: Output more information.
        version_flag: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslGetStandardOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_GET_STANDARD_METADATA)
    cargs = []
    cargs.append("fsl_get_standard")
    cargs.append(image_type)
    if resolution is not None:
        cargs.extend(["-r", str(resolution)])
    if verbose_flag:
        cargs.append("-v")
    if version_flag:
        cargs.append("-V")
    ret = FslGetStandardOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_GET_STANDARD_METADATA",
    "FslGetStandardOutputs",
    "fsl_get_standard",
]
