# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1DPLOT_PY_METADATA = Metadata(
    id="af0d5999d24bbc6f3961a4d20bd4b38860891d74",
    name="1dplot.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dplotPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dplot_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Output image file, default to .jpg"""


def v_1dplot_py(
    infiles: list[InputPathType],
    prefix: str,
    help_: bool = False,
    boxplot_on: bool = False,
    bplot_view: str | None = None,
    margin_off: bool = False,
    scale: list[str] | None = None,
    xfile: InputPathType | None = None,
    xvals: list[float | int] | None = None,
    yaxis: list[str] | None = None,
    ylabels: list[str] | None = None,
    ylabels_maxlen: float | int | None = None,
    legend_on: bool = False,
    legend_labels: list[str] | None = None,
    legend_locs: list[str] | None = None,
    xlabel: str | None = None,
    title: str | None = None,
    reverse_order: bool = False,
    sepscl: bool = False,
    one_graph: bool = False,
    dpi: float | int | None = None,
    figsize: list[float | int] | None = None,
    fontsize: float | int | None = None,
    fontfamily: str | None = None,
    fontstyles: str | None = None,
    colors: list[str] | None = None,
    patches: list[str] | None = None,
    censor_trs: list[str] | None = None,
    censor_files: list[InputPathType] | None = None,
    censor_hline: list[str] | None = None,
    censor_rgb: str | None = None,
    bkgd_color: str | None = None,
    runner: Runner | None = None,
) -> V1dplotPyOutputs:
    """
    1dplot.py by AFNI Team.
    
    This program is for making images to visualize columns of numbers from 1D
    text files. It uses Python, particularly matplotlib, to create plots.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dplot.py.html
    
    Args:
        infiles: One or more file names of text files. Each column in this file\
            will be treated as a separate time series for plotting.
        prefix: Output filename or prefix. Default output image type is .jpg.
        help_: See helpfile.
        boxplot_on: A fun feature to show an additional boxplot adjacent to\
            each time series.
        bplot_view: Adjust view for boxplots when using censoring.
        margin_off: Fill the plot frame completely, thus no labels, frame, or\
            titles will be visible.
        scale: Provide a list of scales to apply to the y-values.
        xfile: One way to input x-values explicitly: as a "1D" file containing\
            a single file of numbers.
        xvals: Provide exactly 3 numbers for x-values: start, stop, and\
            stepsize.
        yaxis: Optional range for each 'infile' y-axis.
        ylabels: Optional text labels for each 'infile' column.
        ylabels_maxlen: allows y-axis labels to wrap into multiple rows, each\
            of length <= which the user can decide.
        legend_on: Turn on the plotting of a legend in the plot(s).
        legend_labels: Optional legend labels, if using '-legend_on'.
        legend_locs: Optional legend locations, if using '-legend_on'.
        xlabel: Optional text labels for the abscissa/x-axis.
        title: Optional title for the set of plots.
        reverse_order: Reverses the order of plotted time series.
        sepscl: Make each graph have its own y-range.
        one_graph: Plot multiple infiles in a single subplot.
        dpi: Choose the output image's DPI. Default value is 150.
        figsize: Choose the output image's dimensions (units are inches).
        fontsize: Change image fontsize; default is 10.
        fontfamily: Change font-family used; default is monospace.
        fontstyles: Add a specific font name; should match with chosen\
            font-family.
        colors: Decide what color(s) to cycle through in plots (one or more).
        patches: Specify run lengths for background patches to distinguish runs.
        censor_trs: Specify time points where censoring has occurred using AFNI\
            index notation.
        censor_files: Specify time points where censoring has occurred using\
            one or more 1D files.
        censor_hline: Add a dotted horizontal line to the plot, representing\
            the censor threshold.
        censor_rgb: Choose the color of the censoring background; default is:\
            [1, 0.7, 0.7].
        bkgd_color: Change the background color outside of the plot windows.\
            Default is 0.9.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dplotPyOutputs`).
    """
    runner = runner or get_global_runner()
    if xvals is not None and (len(xvals) != 3): 
        raise ValueError(f"Length of 'xvals' must be 3 but was {len(xvals)}")
    if figsize is not None and (len(figsize) != 2): 
        raise ValueError(f"Length of 'figsize' must be 2 but was {len(figsize)}")
    execution = runner.start_execution(V_1DPLOT_PY_METADATA)
    cargs = []
    cargs.append("1dplot.py")
    cargs.extend(["-infiles", *[execution.input_file(f) for f in infiles]])
    cargs.extend(["-prefix", prefix])
    cargs.append("[OTHER_OPTIONS]")
    ret = V1dplotPyOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(f"{prefix}.jpg", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dplotPyOutputs",
    "V_1DPLOT_PY_METADATA",
    "v_1dplot_py",
]
