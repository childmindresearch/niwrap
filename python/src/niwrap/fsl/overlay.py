# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

OVERLAY_METADATA = Metadata(
    id="08c461a1c1364a71fb120c4215e9f751f4996e20",
    name="Overlay",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class OverlayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `overlay(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file_outfile: OutputPathType | None
    """Combined image volume."""


def overlay(
    background_image: InputPathType,
    bg_thresh: list[float | int],
    stat_image: InputPathType,
    stat_thresh: list[float | int],
    auto_thresh_bg: bool = False,
    full_bg_range: bool = False,
    out_file: InputPathType | None = None,
    out_type: typing.Literal["float", "int"] | None = "float",
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    stat_image2: InputPathType | None = None,
    stat_thresh2: list[float | int] | None = None,
    use_checkerboard: bool = False,
    runner: Runner | None = None,
) -> OverlayOutputs:
    """
    Overlay by Nipype (interface).
    
    Use FSL's overlay command to combine background and statistical images into
    one volume.
    
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
    if (len(bg_thresh) != 2): 
        raise ValueError(f"Length of 'bg_thresh' must be 2 but was {len(bg_thresh)}")
    if (len(stat_thresh) != 2): 
        raise ValueError(f"Length of 'stat_thresh' must be 2 but was {len(stat_thresh)}")
    if stat_thresh2 is not None and (len(stat_thresh2) != 2): 
        raise ValueError(f"Length of 'stat_thresh2' must be 2 but was {len(stat_thresh2)}")
    if (
        (bg_thresh is not None) +
        full_bg_range +
        auto_thresh_bg
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "bg_thresh,\n"
            "full_bg_range,\n"
            "auto_thresh_bg"
        )
    if (
        (stat_image2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "stat_image2"
        )
    execution = runner.start_execution(OVERLAY_METADATA)
    cargs = []
    cargs.append("Overlay")
    cargs.append("[TRANSPARENCY]")
    if out_type is not None:
        cargs.append(out_type)
    if use_checkerboard:
        cargs.append("-c")
    cargs.append(execution.input_file(background_image))
    if full_bg_range:
        cargs.append("-A")
    cargs.append(execution.input_file(stat_image))
    cargs.extend(map(str, stat_thresh))
    cargs.append("[SHOW_NEGATIVE_STATS]")
    if stat_image2 is not None:
        cargs.append(execution.input_file(stat_image2))
    if stat_thresh2 is not None:
        cargs.extend(map(str, stat_thresh2))
    if out_file is not None:
        cargs.append(execution.input_file(out_file))
    if output_type is not None:
        cargs.append(output_type)
    ret = OverlayOutputs(
        root=execution.output_file("."),
        out_file_outfile=execution.output_file(f"{pathlib.Path(out_file).name}", optional=True) if out_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "OVERLAY_METADATA",
    "OverlayOutputs",
    "overlay",
]
