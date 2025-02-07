# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_LOG_LIKELIHOOD_METADATA = Metadata(
    id="f22fe6123ce8f0f860ffe7eecd35b5f18caff0af.boutiques",
    name="mri_log_likelihood",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriLogLikelihoodParameters = typing.TypedDict('MriLogLikelihoodParameters', {
    "__STYX_TYPE__": typing.Literal["mri_log_likelihood"],
    "input_brain_images": list[InputPathType],
    "atlas_file": InputPathType,
    "transform_file": InputPathType,
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
        "mri_log_likelihood": mri_log_likelihood_cargs,
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
        "mri_log_likelihood": mri_log_likelihood_outputs,
    }.get(t)


class MriLogLikelihoodOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_log_likelihood(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_log_likelihood_params(
    input_brain_images: list[InputPathType],
    atlas_file: InputPathType,
    transform_file: InputPathType,
) -> MriLogLikelihoodParameters:
    """
    Build parameters.
    
    Args:
        input_brain_images: List of input brain images.
        atlas_file: Atlas image file.
        transform_file: Transform file for registration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_log_likelihood",
        "input_brain_images": input_brain_images,
        "atlas_file": atlas_file,
        "transform_file": transform_file,
    }
    return params


def mri_log_likelihood_cargs(
    params: MriLogLikelihoodParameters,
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
    cargs.append("mri_log_likelihood")
    cargs.extend([execution.input_file(f) for f in params.get("input_brain_images")])
    cargs.append(execution.input_file(params.get("atlas_file")))
    cargs.append(execution.input_file(params.get("transform_file")))
    return cargs


def mri_log_likelihood_outputs(
    params: MriLogLikelihoodParameters,
    execution: Execution,
) -> MriLogLikelihoodOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriLogLikelihoodOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_log_likelihood_execute(
    params: MriLogLikelihoodParameters,
    execution: Execution,
) -> MriLogLikelihoodOutputs:
    """
    MRI log likelihood calculation tool for brain images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriLogLikelihoodOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_log_likelihood_cargs(params, execution)
    ret = mri_log_likelihood_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_log_likelihood(
    input_brain_images: list[InputPathType],
    atlas_file: InputPathType,
    transform_file: InputPathType,
    runner: Runner | None = None,
) -> MriLogLikelihoodOutputs:
    """
    MRI log likelihood calculation tool for brain images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_brain_images: List of input brain images.
        atlas_file: Atlas image file.
        transform_file: Transform file for registration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriLogLikelihoodOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_LOG_LIKELIHOOD_METADATA)
    params = mri_log_likelihood_params(input_brain_images=input_brain_images, atlas_file=atlas_file, transform_file=transform_file)
    return mri_log_likelihood_execute(params, execution)


__all__ = [
    "MRI_LOG_LIKELIHOOD_METADATA",
    "MriLogLikelihoodOutputs",
    "MriLogLikelihoodParameters",
    "mri_log_likelihood",
    "mri_log_likelihood_params",
]
