# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANATOMICAL_AVERAGE_METADATA = Metadata(
    id="247f0a40aa16f444290b87939a981d90386a5a1a.boutiques",
    name="AnatomicalAverage",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
AnatomicalAverageParameters = typing.TypedDict('AnatomicalAverageParameters', {
    "__STYX_TYPE__": typing.Literal["AnatomicalAverage"],
    "output_basename": str,
    "input_images": list[InputPathType],
    "standard_image": typing.NotRequired[InputPathType | None],
    "standard_brain_mask": typing.NotRequired[InputPathType | None],
    "no_crop_flag": bool,
    "work_dir": typing.NotRequired[str | None],
    "brainsize": typing.NotRequired[float | None],
    "noclean_flag": bool,
    "verbose_flag": bool,
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
        "AnatomicalAverage": anatomical_average_cargs,
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
        "AnatomicalAverage": anatomical_average_outputs,
    }.get(t)


class AnatomicalAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `anatomical_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    avg_output: OutputPathType
    """Averaged anatomical image"""


def anatomical_average_params(
    output_basename: str,
    input_images: list[InputPathType],
    standard_image: InputPathType | None = None,
    standard_brain_mask: InputPathType | None = None,
    no_crop_flag: bool = False,
    work_dir: str | None = None,
    brainsize: float | None = None,
    noclean_flag: bool = False,
    verbose_flag: bool = False,
) -> AnatomicalAverageParameters:
    """
    Build parameters.
    
    Args:
        output_basename: Output basename.
        input_images: List of input images.
        standard_image: Standard image (default is MNI152_T1_2mm).
        standard_brain_mask: Standard brain mask (default is\
            MNI152_T1_2mm_brain_mask_dil).
        no_crop_flag: Do not crop images.
        work_dir: Local, temporary working directory (to be cleaned up - i.e.\
            deleted).
        brainsize: Specify brainsize in mm for internal ROI (via robustfov).
        noclean_flag: Do not run the cleanup.
        verbose_flag: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "AnatomicalAverage",
        "output_basename": output_basename,
        "input_images": input_images,
        "no_crop_flag": no_crop_flag,
        "noclean_flag": noclean_flag,
        "verbose_flag": verbose_flag,
    }
    if standard_image is not None:
        params["standard_image"] = standard_image
    if standard_brain_mask is not None:
        params["standard_brain_mask"] = standard_brain_mask
    if work_dir is not None:
        params["work_dir"] = work_dir
    if brainsize is not None:
        params["brainsize"] = brainsize
    return params


def anatomical_average_cargs(
    params: AnatomicalAverageParameters,
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
    cargs.append("AnatomicalAverage")
    cargs.extend([
        "-o",
        params.get("output_basename")
    ])
    cargs.extend([execution.input_file(f) for f in params.get("input_images")])
    if params.get("standard_image") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("standard_image"))
        ])
    if params.get("standard_brain_mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("standard_brain_mask"))
        ])
    if params.get("no_crop_flag"):
        cargs.append("-n")
    if params.get("work_dir") is not None:
        cargs.extend([
            "-w",
            params.get("work_dir")
        ])
    if params.get("brainsize") is not None:
        cargs.extend([
            "-b",
            str(params.get("brainsize"))
        ])
    if params.get("noclean_flag"):
        cargs.append("--noclean")
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def anatomical_average_outputs(
    params: AnatomicalAverageParameters,
    execution: Execution,
) -> AnatomicalAverageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AnatomicalAverageOutputs(
        root=execution.output_file("."),
        avg_output=execution.output_file(params.get("output_basename") + "_avg.nii.gz"),
    )
    return ret


def anatomical_average_execute(
    params: AnatomicalAverageParameters,
    execution: Execution,
) -> AnatomicalAverageOutputs:
    """
    Tool to create an anatomical average of input brain images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AnatomicalAverageOutputs`).
    """
    params = execution.params(params)
    cargs = anatomical_average_cargs(params, execution)
    ret = anatomical_average_outputs(params, execution)
    execution.run(cargs)
    return ret


def anatomical_average(
    output_basename: str,
    input_images: list[InputPathType],
    standard_image: InputPathType | None = None,
    standard_brain_mask: InputPathType | None = None,
    no_crop_flag: bool = False,
    work_dir: str | None = None,
    brainsize: float | None = None,
    noclean_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> AnatomicalAverageOutputs:
    """
    Tool to create an anatomical average of input brain images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_basename: Output basename.
        input_images: List of input images.
        standard_image: Standard image (default is MNI152_T1_2mm).
        standard_brain_mask: Standard brain mask (default is\
            MNI152_T1_2mm_brain_mask_dil).
        no_crop_flag: Do not crop images.
        work_dir: Local, temporary working directory (to be cleaned up - i.e.\
            deleted).
        brainsize: Specify brainsize in mm for internal ROI (via robustfov).
        noclean_flag: Do not run the cleanup.
        verbose_flag: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AnatomicalAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANATOMICAL_AVERAGE_METADATA)
    params = anatomical_average_params(output_basename=output_basename, input_images=input_images, standard_image=standard_image, standard_brain_mask=standard_brain_mask, no_crop_flag=no_crop_flag, work_dir=work_dir, brainsize=brainsize, noclean_flag=noclean_flag, verbose_flag=verbose_flag)
    return anatomical_average_execute(params, execution)


__all__ = [
    "ANATOMICAL_AVERAGE_METADATA",
    "AnatomicalAverageOutputs",
    "AnatomicalAverageParameters",
    "anatomical_average",
    "anatomical_average_params",
]
