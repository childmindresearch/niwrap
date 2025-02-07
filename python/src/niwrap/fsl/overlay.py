# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

OVERLAY_METADATA = Metadata(
    id="c0718fc41040837c6b901bbd7591f11f61d7d2dd.boutiques",
    name="overlay",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
OverlayParameters = typing.TypedDict('OverlayParameters', {
    "__STYX_TYPE__": typing.Literal["overlay"],
    "auto_thresh_bg": bool,
    "background_image": InputPathType,
    "bg_thresh": list[float],
    "full_bg_range": bool,
    "out_file": typing.NotRequired[str | None],
    "out_type": typing.NotRequired[typing.Literal["float", "int"] | None],
    "output_type": typing.NotRequired[typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None],
    "stat_image": InputPathType,
    "stat_image2": typing.NotRequired[InputPathType | None],
    "stat_thresh": list[float],
    "stat_thresh2": typing.NotRequired[list[float] | None],
    "use_checkerboard": bool,
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
        "overlay": overlay_cargs,
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
        "overlay": overlay_outputs,
    }.get(t)


class OverlayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `overlay(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file_outfile: OutputPathType | None
    """Combined image volume."""


def overlay_params(
    background_image: InputPathType,
    bg_thresh: list[float],
    stat_image: InputPathType,
    stat_thresh: list[float],
    auto_thresh_bg: bool = False,
    full_bg_range: bool = False,
    out_file: str | None = None,
    out_type: typing.Literal["float", "int"] | None = "float",
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    stat_image2: InputPathType | None = None,
    stat_thresh2: list[float] | None = None,
    use_checkerboard: bool = False,
) -> OverlayParameters:
    """
    Build parameters.
    
    Args:
        background_image: Image to use as background.
        bg_thresh: (a float, a float). Min and max values for background\
            intensity.
        stat_image: Statistical image to overlay in color.
        stat_thresh: (a float, a float). Min and max values for the statistical\
            overlay.
        auto_thresh_bg: Automatically threshold the background image.
        full_bg_range: Use full range of background image.
        out_file: Combined image volume.
        out_type: 'float' or 'int'. Write output with float or int.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        stat_image2: Second statistical image to overlay in color.
        stat_thresh2: (a float, a float). Min and max values for second\
            statistical overlay.
        use_checkerboard: Use checkerboard mask for overlay.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "overlay",
        "auto_thresh_bg": auto_thresh_bg,
        "background_image": background_image,
        "bg_thresh": bg_thresh,
        "full_bg_range": full_bg_range,
        "stat_image": stat_image,
        "stat_thresh": stat_thresh,
        "use_checkerboard": use_checkerboard,
    }
    if out_file is not None:
        params["out_file"] = out_file
    if out_type is not None:
        params["out_type"] = out_type
    if output_type is not None:
        params["output_type"] = output_type
    if stat_image2 is not None:
        params["stat_image2"] = stat_image2
    if stat_thresh2 is not None:
        params["stat_thresh2"] = stat_thresh2
    return params


def overlay_cargs(
    params: OverlayParameters,
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
    cargs.append("overlay")
    if params.get("auto_thresh_bg"):
        cargs.append("-a")
    cargs.append(execution.input_file(params.get("background_image")))
    cargs.extend(map(str, params.get("bg_thresh")))
    if params.get("full_bg_range"):
        cargs.append("-A")
    if params.get("out_file") is not None:
        cargs.append(params.get("out_file"))
    if params.get("out_type") is not None:
        cargs.append(params.get("out_type"))
    if params.get("output_type") is not None:
        cargs.append(params.get("output_type"))
    cargs.append(execution.input_file(params.get("stat_image")))
    if params.get("stat_image2") is not None:
        cargs.append(execution.input_file(params.get("stat_image2")))
    cargs.extend(map(str, params.get("stat_thresh")))
    if params.get("stat_thresh2") is not None:
        cargs.extend(map(str, params.get("stat_thresh2")))
    if params.get("use_checkerboard"):
        cargs.append("-c")
    return cargs


def overlay_outputs(
    params: OverlayParameters,
    execution: Execution,
) -> OverlayOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = OverlayOutputs(
        root=execution.output_file("."),
        out_file_outfile=execution.output_file(params.get("out_file")) if (params.get("out_file") is not None) else None,
    )
    return ret


def overlay_execute(
    params: OverlayParameters,
    execution: Execution,
) -> OverlayOutputs:
    """
    Use FSL's overlay command to combine background and statistical images into one
    volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `OverlayOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = overlay_cargs(params, execution)
    ret = overlay_outputs(params, execution)
    execution.run(cargs)
    return ret


def overlay(
    background_image: InputPathType,
    bg_thresh: list[float],
    stat_image: InputPathType,
    stat_thresh: list[float],
    auto_thresh_bg: bool = False,
    full_bg_range: bool = False,
    out_file: str | None = None,
    out_type: typing.Literal["float", "int"] | None = "float",
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    stat_image2: InputPathType | None = None,
    stat_thresh2: list[float] | None = None,
    use_checkerboard: bool = False,
    runner: Runner | None = None,
) -> OverlayOutputs:
    """
    Use FSL's overlay command to combine background and statistical images into one
    volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        background_image: Image to use as background.
        bg_thresh: (a float, a float). Min and max values for background\
            intensity.
        stat_image: Statistical image to overlay in color.
        stat_thresh: (a float, a float). Min and max values for the statistical\
            overlay.
        auto_thresh_bg: Automatically threshold the background image.
        full_bg_range: Use full range of background image.
        out_file: Combined image volume.
        out_type: 'float' or 'int'. Write output with float or int.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        stat_image2: Second statistical image to overlay in color.
        stat_thresh2: (a float, a float). Min and max values for second\
            statistical overlay.
        use_checkerboard: Use checkerboard mask for overlay.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `OverlayOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(OVERLAY_METADATA)
    params = overlay_params(auto_thresh_bg=auto_thresh_bg, background_image=background_image, bg_thresh=bg_thresh, full_bg_range=full_bg_range, out_file=out_file, out_type=out_type, output_type=output_type, stat_image=stat_image, stat_image2=stat_image2, stat_thresh=stat_thresh, stat_thresh2=stat_thresh2, use_checkerboard=use_checkerboard)
    return overlay_execute(params, execution)


__all__ = [
    "OVERLAY_METADATA",
    "OverlayOutputs",
    "OverlayParameters",
    "overlay",
    "overlay_params",
]
