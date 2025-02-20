# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_HISTOGRAM_METADATA = Metadata(
    id="29a34e1d8dffc172e2f3223aff804ebe9bea2f93.boutiques",
    name="fsl_histogram",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslHistogramParameters = typing.TypedDict('FslHistogramParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_histogram"],
    "input_file_duplicate": InputPathType,
    "output_file_duplicate": str,
    "mask_file_duplicate": typing.NotRequired[InputPathType | None],
    "gmmfit_file_duplicate": typing.NotRequired[InputPathType | None],
    "plot_title_duplicate": typing.NotRequired[str | None],
    "legend_file_duplicate": typing.NotRequired[InputPathType | None],
    "xlabel_duplicate": typing.NotRequired[str | None],
    "ylabel_duplicate": typing.NotRequired[str | None],
    "plot_height_duplicate": typing.NotRequired[float | None],
    "plot_width_duplicate": typing.NotRequired[float | None],
    "num_bins_duplicate": typing.NotRequired[float | None],
    "zoom_factor_duplicate": typing.NotRequired[float | None],
    "use_gmm_flag": bool,
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
        "fsl_histogram": fsl_histogram_cargs,
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
        "fsl_histogram": fsl_histogram_outputs,
    }.get(t)


class FslHistogramOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_histogram(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    png_file: OutputPathType
    """Generated PNG file"""


def fsl_histogram_params(
    input_file_duplicate: InputPathType,
    output_file_duplicate: str,
    mask_file_duplicate: InputPathType | None = None,
    gmmfit_file_duplicate: InputPathType | None = None,
    plot_title_duplicate: str | None = None,
    legend_file_duplicate: InputPathType | None = None,
    xlabel_duplicate: str | None = None,
    ylabel_duplicate: str | None = None,
    plot_height_duplicate: float | None = None,
    plot_width_duplicate: float | None = None,
    num_bins_duplicate: float | None = None,
    zoom_factor_duplicate: float | None = None,
    use_gmm_flag: bool = False,
) -> FslHistogramParameters:
    """
    Build parameters.
    
    Args:
        input_file_duplicate: Input file name.
        output_file_duplicate: Output filename for the PNG file.
        mask_file_duplicate: Mask file name.
        gmmfit_file_duplicate: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        plot_title_duplicate: Plot title.
        legend_file_duplicate: File name of ASCII text file, one row per legend\
            entry.
        xlabel_duplicate: X-axis label.
        ylabel_duplicate: Y-axis label.
        plot_height_duplicate: Plot height in pixels (default 400).
        plot_width_duplicate: Plot width in pixels (default 600).
        num_bins_duplicate: Number of histogram bins.
        zoom_factor_duplicate: Zoom factor for y-range (e.g. 2.0).
        use_gmm_flag: Use Gaussian mixture model instead of Gaussian/Gamma\
            mixture model.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_histogram",
        "input_file_duplicate": input_file_duplicate,
        "output_file_duplicate": output_file_duplicate,
        "use_gmm_flag": use_gmm_flag,
    }
    if mask_file_duplicate is not None:
        params["mask_file_duplicate"] = mask_file_duplicate
    if gmmfit_file_duplicate is not None:
        params["gmmfit_file_duplicate"] = gmmfit_file_duplicate
    if plot_title_duplicate is not None:
        params["plot_title_duplicate"] = plot_title_duplicate
    if legend_file_duplicate is not None:
        params["legend_file_duplicate"] = legend_file_duplicate
    if xlabel_duplicate is not None:
        params["xlabel_duplicate"] = xlabel_duplicate
    if ylabel_duplicate is not None:
        params["ylabel_duplicate"] = ylabel_duplicate
    if plot_height_duplicate is not None:
        params["plot_height_duplicate"] = plot_height_duplicate
    if plot_width_duplicate is not None:
        params["plot_width_duplicate"] = plot_width_duplicate
    if num_bins_duplicate is not None:
        params["num_bins_duplicate"] = num_bins_duplicate
    if zoom_factor_duplicate is not None:
        params["zoom_factor_duplicate"] = zoom_factor_duplicate
    return params


def fsl_histogram_cargs(
    params: FslHistogramParameters,
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
    cargs.append("fsl_histogram")
    cargs.extend([
        "--in",
        execution.input_file(params.get("input_file_duplicate"))
    ])
    cargs.extend([
        "--out",
        params.get("output_file_duplicate")
    ])
    if params.get("mask_file_duplicate") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_file_duplicate"))
        ])
    if params.get("gmmfit_file_duplicate") is not None:
        cargs.extend([
            "--gmmfit",
            execution.input_file(params.get("gmmfit_file_duplicate"))
        ])
    if params.get("plot_title_duplicate") is not None:
        cargs.extend([
            "--title",
            params.get("plot_title_duplicate")
        ])
    if params.get("legend_file_duplicate") is not None:
        cargs.extend([
            "--legend",
            execution.input_file(params.get("legend_file_duplicate"))
        ])
    if params.get("xlabel_duplicate") is not None:
        cargs.extend([
            "--xlabel",
            params.get("xlabel_duplicate")
        ])
    if params.get("ylabel_duplicate") is not None:
        cargs.extend([
            "--ylabel",
            params.get("ylabel_duplicate")
        ])
    if params.get("plot_height_duplicate") is not None:
        cargs.extend([
            "--height",
            str(params.get("plot_height_duplicate"))
        ])
    if params.get("plot_width_duplicate") is not None:
        cargs.extend([
            "--width",
            str(params.get("plot_width_duplicate"))
        ])
    if params.get("num_bins_duplicate") is not None:
        cargs.extend([
            "--bins",
            str(params.get("num_bins_duplicate"))
        ])
    if params.get("zoom_factor_duplicate") is not None:
        cargs.extend([
            "--detail",
            str(params.get("zoom_factor_duplicate"))
        ])
    if params.get("use_gmm_flag"):
        cargs.append("--gmm")
    return cargs


def fsl_histogram_outputs(
    params: FslHistogramParameters,
    execution: Execution,
) -> FslHistogramOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslHistogramOutputs(
        root=execution.output_file("."),
        png_file=execution.output_file(params.get("output_file_duplicate")),
    )
    return ret


def fsl_histogram_execute(
    params: FslHistogramParameters,
    execution: Execution,
) -> FslHistogramOutputs:
    """
    Histogram plotting tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslHistogramOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_histogram_cargs(params, execution)
    ret = fsl_histogram_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_histogram(
    input_file_duplicate: InputPathType,
    output_file_duplicate: str,
    mask_file_duplicate: InputPathType | None = None,
    gmmfit_file_duplicate: InputPathType | None = None,
    plot_title_duplicate: str | None = None,
    legend_file_duplicate: InputPathType | None = None,
    xlabel_duplicate: str | None = None,
    ylabel_duplicate: str | None = None,
    plot_height_duplicate: float | None = None,
    plot_width_duplicate: float | None = None,
    num_bins_duplicate: float | None = None,
    zoom_factor_duplicate: float | None = None,
    use_gmm_flag: bool = False,
    runner: Runner | None = None,
) -> FslHistogramOutputs:
    """
    Histogram plotting tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file_duplicate: Input file name.
        output_file_duplicate: Output filename for the PNG file.
        mask_file_duplicate: Mask file name.
        gmmfit_file_duplicate: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        plot_title_duplicate: Plot title.
        legend_file_duplicate: File name of ASCII text file, one row per legend\
            entry.
        xlabel_duplicate: X-axis label.
        ylabel_duplicate: Y-axis label.
        plot_height_duplicate: Plot height in pixels (default 400).
        plot_width_duplicate: Plot width in pixels (default 600).
        num_bins_duplicate: Number of histogram bins.
        zoom_factor_duplicate: Zoom factor for y-range (e.g. 2.0).
        use_gmm_flag: Use Gaussian mixture model instead of Gaussian/Gamma\
            mixture model.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslHistogramOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_HISTOGRAM_METADATA)
    params = fsl_histogram_params(
        input_file_duplicate=input_file_duplicate,
        output_file_duplicate=output_file_duplicate,
        mask_file_duplicate=mask_file_duplicate,
        gmmfit_file_duplicate=gmmfit_file_duplicate,
        plot_title_duplicate=plot_title_duplicate,
        legend_file_duplicate=legend_file_duplicate,
        xlabel_duplicate=xlabel_duplicate,
        ylabel_duplicate=ylabel_duplicate,
        plot_height_duplicate=plot_height_duplicate,
        plot_width_duplicate=plot_width_duplicate,
        num_bins_duplicate=num_bins_duplicate,
        zoom_factor_duplicate=zoom_factor_duplicate,
        use_gmm_flag=use_gmm_flag,
    )
    return fsl_histogram_execute(params, execution)


__all__ = [
    "FSL_HISTOGRAM_METADATA",
    "FslHistogramOutputs",
    "FslHistogramParameters",
    "fsl_histogram",
    "fsl_histogram_params",
]
