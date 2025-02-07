# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_APARC2WMSEG_METADATA = Metadata(
    id="892ee2faaf430ffd543fbcdbbee1b1cfff8331fb.boutiques",
    name="mri_aparc2wmseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriAparc2wmsegParameters = typing.TypedDict('MriAparc2wmsegParameters', {
    "__STYX_TYPE__": typing.Literal["mri_aparc2wmseg"],
    "subject": str,
    "wmseg_file": str,
    "help": bool,
    "version": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_aparc2wmseg": mri_aparc2wmseg_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_aparc2wmseg": mri_aparc2wmseg_outputs,
    }.get(t)


class MriAparc2wmsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_aparc2wmseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_aparc2wmseg_params(
    subject: str,
    wmseg_file: str,
    help_: bool = False,
    version: bool = False,
) -> MriAparc2wmsegParameters:
    """
    Build parameters.
    
    Args:
        subject: The subject identifier used in FreeSurfer.
        wmseg_file: File to store the output white matter segmentation.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_aparc2wmseg",
        "subject": subject,
        "wmseg_file": wmseg_file,
        "help": help_,
        "version": version,
    }
    return params


def mri_aparc2wmseg_cargs(
    params: MriAparc2wmsegParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mri_aparc2wmseg")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    cargs.extend([
        "--wmseg",
        params.get("wmseg_file")
    ])
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mri_aparc2wmseg_outputs(
    params: MriAparc2wmsegParameters,
    execution: Execution,
) -> MriAparc2wmsegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriAparc2wmsegOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_aparc2wmseg_execute(
    params: MriAparc2wmsegParameters,
    execution: Execution,
) -> MriAparc2wmsegOutputs:
    """
    A tool to convert aparc+aseg.mgz annotations into a white matter segmentation
    file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriAparc2wmsegOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_aparc2wmseg_cargs(params, execution)
    ret = mri_aparc2wmseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_aparc2wmseg(
    subject: str,
    wmseg_file: str,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriAparc2wmsegOutputs:
    """
    A tool to convert aparc+aseg.mgz annotations into a white matter segmentation
    file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject identifier used in FreeSurfer.
        wmseg_file: File to store the output white matter segmentation.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAparc2wmsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_APARC2WMSEG_METADATA)
    params = mri_aparc2wmseg_params(subject=subject, wmseg_file=wmseg_file, help_=help_, version=version)
    return mri_aparc2wmseg_execute(params, execution)


__all__ = [
    "MRI_APARC2WMSEG_METADATA",
    "MriAparc2wmsegOutputs",
    "MriAparc2wmsegParameters",
    "mri_aparc2wmseg",
    "mri_aparc2wmseg_params",
]
