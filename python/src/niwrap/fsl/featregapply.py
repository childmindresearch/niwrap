# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FEATREGAPPLY_METADATA = Metadata(
    id="30c4e6513395f39bf385f62de8b909c189f6d029.boutiques",
    name="featregapply",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FeatregapplyParameters = typing.TypedDict('FeatregapplyParameters', {
    "__STYX_TYPE__": typing.Literal["featregapply"],
    "feat_directory": str,
    "force_flag": bool,
    "cleanup_flag": bool,
    "upsample_trilinear": typing.NotRequired[InputPathType | None],
    "upsample_spline": typing.NotRequired[InputPathType | None],
    "standard_space_res": typing.NotRequired[float | None],
    "exclude_filtered_func_flag": bool,
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
        "featregapply": featregapply_cargs,
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
        "featregapply": featregapply_outputs,
    }.get(t)


class FeatregapplyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `featregapply(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_directory: OutputPathType
    """Directory where the output files will be stored"""


def featregapply_params(
    feat_directory: str,
    force_flag: bool = False,
    cleanup_flag: bool = False,
    upsample_trilinear: InputPathType | None = None,
    upsample_spline: InputPathType | None = None,
    standard_space_res: float | None = None,
    exclude_filtered_func_flag: bool = False,
) -> FeatregapplyParameters:
    """
    Build parameters.
    
    Args:
        feat_directory: FEAT directory from which registration will be taken.
        force_flag: Force featregapply to run even if it has already been run\
            on this FEAT directory.
        cleanup_flag: Cleanup, i.e. remove all featregapply output.
        upsample_trilinear: Upsample functional-space image to standard space\
            using trilinear interpolation.
        upsample_spline: Upsample functional-space image to standard space\
            using spline (like sinc) interpolation.
        standard_space_res: Specify the standard space resolution for melodic\
            (e.g. 3 for 3mm).
        exclude_filtered_func_flag: Exclude filtered func when processing\
            melodic directories (for FEAT directories filtered func is never\
            processed).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "featregapply",
        "feat_directory": feat_directory,
        "force_flag": force_flag,
        "cleanup_flag": cleanup_flag,
        "exclude_filtered_func_flag": exclude_filtered_func_flag,
    }
    if upsample_trilinear is not None:
        params["upsample_trilinear"] = upsample_trilinear
    if upsample_spline is not None:
        params["upsample_spline"] = upsample_spline
    if standard_space_res is not None:
        params["standard_space_res"] = standard_space_res
    return params


def featregapply_cargs(
    params: FeatregapplyParameters,
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
    cargs.append("featregapply")
    cargs.append(params.get("feat_directory"))
    if params.get("force_flag"):
        cargs.append("-f")
    if params.get("cleanup_flag"):
        cargs.append("-c")
    if params.get("upsample_trilinear") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("upsample_trilinear"))
        ])
    if params.get("upsample_spline") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("upsample_spline"))
        ])
    if params.get("standard_space_res") is not None:
        cargs.extend([
            "-r",
            str(params.get("standard_space_res"))
        ])
    if params.get("exclude_filtered_func_flag"):
        cargs.append("-e")
    return cargs


def featregapply_outputs(
    params: FeatregapplyParameters,
    execution: Execution,
) -> FeatregapplyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FeatregapplyOutputs(
        root=execution.output_file("."),
        output_directory=execution.output_file(params.get("feat_directory") + "/reg_standard"),
    )
    return ret


def featregapply_execute(
    params: FeatregapplyParameters,
    execution: Execution,
) -> FeatregapplyOutputs:
    """
    Apply registration from FEAT analysis to other images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FeatregapplyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = featregapply_cargs(params, execution)
    ret = featregapply_outputs(params, execution)
    execution.run(cargs)
    return ret


def featregapply(
    feat_directory: str,
    force_flag: bool = False,
    cleanup_flag: bool = False,
    upsample_trilinear: InputPathType | None = None,
    upsample_spline: InputPathType | None = None,
    standard_space_res: float | None = None,
    exclude_filtered_func_flag: bool = False,
    runner: Runner | None = None,
) -> FeatregapplyOutputs:
    """
    Apply registration from FEAT analysis to other images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        feat_directory: FEAT directory from which registration will be taken.
        force_flag: Force featregapply to run even if it has already been run\
            on this FEAT directory.
        cleanup_flag: Cleanup, i.e. remove all featregapply output.
        upsample_trilinear: Upsample functional-space image to standard space\
            using trilinear interpolation.
        upsample_spline: Upsample functional-space image to standard space\
            using spline (like sinc) interpolation.
        standard_space_res: Specify the standard space resolution for melodic\
            (e.g. 3 for 3mm).
        exclude_filtered_func_flag: Exclude filtered func when processing\
            melodic directories (for FEAT directories filtered func is never\
            processed).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FeatregapplyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEATREGAPPLY_METADATA)
    params = featregapply_params(feat_directory=feat_directory, force_flag=force_flag, cleanup_flag=cleanup_flag, upsample_trilinear=upsample_trilinear, upsample_spline=upsample_spline, standard_space_res=standard_space_res, exclude_filtered_func_flag=exclude_filtered_func_flag)
    return featregapply_execute(params, execution)


__all__ = [
    "FEATREGAPPLY_METADATA",
    "FeatregapplyOutputs",
    "FeatregapplyParameters",
    "featregapply",
    "featregapply_params",
]
