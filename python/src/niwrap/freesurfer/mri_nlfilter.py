# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_NLFILTER_METADATA = Metadata(
    id="c44a60efcccca403f44c82f08afd31e3af464d00.boutiques",
    name="mri_nlfilter",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriNlfilterParameters = typing.TypedDict('MriNlfilterParameters', {
    "__STYX_TYPE__": typing.Literal["mri_nlfilter"],
    "input_image": InputPathType,
    "output_image": str,
    "blur_sigma": typing.NotRequired[float | None],
    "gaussian_sigma": typing.NotRequired[float | None],
    "mean_flag": bool,
    "window_size": typing.NotRequired[float | None],
    "cplov_flag": bool,
    "minmax_flag": bool,
    "no_offsets_flag": bool,
    "no_crop_flag": bool,
    "version_flag": bool,
    "help_flag": bool,
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
        "mri_nlfilter": mri_nlfilter_cargs,
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
        "mri_nlfilter": mri_nlfilter_outputs,
    }.get(t)


class MriNlfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_nlfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The processed image output file."""


def mri_nlfilter_params(
    input_image: InputPathType,
    output_image: str,
    blur_sigma: float | None = None,
    gaussian_sigma: float | None = None,
    mean_flag: bool = False,
    window_size: float | None = None,
    cplov_flag: bool = False,
    minmax_flag: bool = False,
    no_offsets_flag: bool = False,
    no_crop_flag: bool = False,
    version_flag: bool = False,
    help_flag: bool = False,
) -> MriNlfilterParameters:
    """
    Build parameters.
    
    Args:
        input_image: The input image file to be processed.
        output_image: The output image file where the processed image will be\
            saved.
        blur_sigma: Specify sigma of the blurring kernel. Default is 0.500.
        gaussian_sigma: Filter with Gaussian instead of median. Requires sigma\
            value.
        mean_flag: Filter with mean instead of median.
        window_size: Specify window size used for offset calculation. Default\
            is 3.
        cplov_flag: Filter with cplov.
        minmax_flag: Filter with minmax.
        no_offsets_flag: Don't use offsets, just apply standard filters.
        no_crop_flag: Don't crop to >0 region of image.
        version_flag: Display version number.
        help_flag: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_nlfilter",
        "input_image": input_image,
        "output_image": output_image,
        "mean_flag": mean_flag,
        "cplov_flag": cplov_flag,
        "minmax_flag": minmax_flag,
        "no_offsets_flag": no_offsets_flag,
        "no_crop_flag": no_crop_flag,
        "version_flag": version_flag,
        "help_flag": help_flag,
    }
    if blur_sigma is not None:
        params["blur_sigma"] = blur_sigma
    if gaussian_sigma is not None:
        params["gaussian_sigma"] = gaussian_sigma
    if window_size is not None:
        params["window_size"] = window_size
    return params


def mri_nlfilter_cargs(
    params: MriNlfilterParameters,
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
    cargs.append("mri_nlfilter")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    if params.get("blur_sigma") is not None:
        cargs.extend([
            "-blur",
            str(params.get("blur_sigma"))
        ])
    if params.get("gaussian_sigma") is not None:
        cargs.extend([
            "-gaussian",
            str(params.get("gaussian_sigma"))
        ])
    if params.get("mean_flag"):
        cargs.append("-mean")
    if params.get("window_size") is not None:
        cargs.extend([
            "-w",
            str(params.get("window_size"))
        ])
    if params.get("cplov_flag"):
        cargs.append("-cplov")
    if params.get("minmax_flag"):
        cargs.append("-minmax")
    if params.get("no_offsets_flag"):
        cargs.append("-n")
    if params.get("no_crop_flag"):
        cargs.append("-nc")
    if params.get("version_flag"):
        cargs.append("--version")
    if params.get("help_flag"):
        cargs.append("--help")
    return cargs


def mri_nlfilter_outputs(
    params: MriNlfilterParameters,
    execution: Execution,
) -> MriNlfilterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriNlfilterOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_image")),
    )
    return ret


def mri_nlfilter_execute(
    params: MriNlfilterParameters,
    execution: Execution,
) -> MriNlfilterOutputs:
    """
    This program processes an image using a nonlocal filter and writes the results
    to an output file. It supports different filtering methods such as median,
    Gaussian, and mean.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriNlfilterOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_nlfilter_cargs(params, execution)
    ret = mri_nlfilter_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_nlfilter(
    input_image: InputPathType,
    output_image: str,
    blur_sigma: float | None = None,
    gaussian_sigma: float | None = None,
    mean_flag: bool = False,
    window_size: float | None = None,
    cplov_flag: bool = False,
    minmax_flag: bool = False,
    no_offsets_flag: bool = False,
    no_crop_flag: bool = False,
    version_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> MriNlfilterOutputs:
    """
    This program processes an image using a nonlocal filter and writes the results
    to an output file. It supports different filtering methods such as median,
    Gaussian, and mean.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: The input image file to be processed.
        output_image: The output image file where the processed image will be\
            saved.
        blur_sigma: Specify sigma of the blurring kernel. Default is 0.500.
        gaussian_sigma: Filter with Gaussian instead of median. Requires sigma\
            value.
        mean_flag: Filter with mean instead of median.
        window_size: Specify window size used for offset calculation. Default\
            is 3.
        cplov_flag: Filter with cplov.
        minmax_flag: Filter with minmax.
        no_offsets_flag: Don't use offsets, just apply standard filters.
        no_crop_flag: Don't crop to >0 region of image.
        version_flag: Display version number.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriNlfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_NLFILTER_METADATA)
    params = mri_nlfilter_params(input_image=input_image, output_image=output_image, blur_sigma=blur_sigma, gaussian_sigma=gaussian_sigma, mean_flag=mean_flag, window_size=window_size, cplov_flag=cplov_flag, minmax_flag=minmax_flag, no_offsets_flag=no_offsets_flag, no_crop_flag=no_crop_flag, version_flag=version_flag, help_flag=help_flag)
    return mri_nlfilter_execute(params, execution)


__all__ = [
    "MRI_NLFILTER_METADATA",
    "MriNlfilterOutputs",
    "MriNlfilterParameters",
    "mri_nlfilter",
    "mri_nlfilter_params",
]
