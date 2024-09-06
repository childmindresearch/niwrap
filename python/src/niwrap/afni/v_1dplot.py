# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1DPLOT_METADATA = Metadata(
    id="fc4163f683186d0408789fe9373492cf03ce9d68",
    name="1dplot",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1dplot(
    tsfiles: list[InputPathType],
    install: bool = False,
    sep: bool = False,
    one: bool = False,
    sepscl: bool = False,
    noline: bool = False,
    noline_: bool = False,
    box: bool = False,
    hist: bool = False,
    norm2: bool = False,
    normx: bool = False,
    norm1: bool = False,
    demean: bool = False,
    x: InputPathType | None = None,
    xl10: InputPathType | None = None,
    dx: float | int | None = None,
    xzero: float | int | None = None,
    nopush: bool = False,
    ignore: float | int | None = None,
    use: float | int | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    plabel: str | None = None,
    title: str | None = None,
    wintitle: str | None = None,
    naked: bool = False,
    aspect: float | int | None = None,
    stdin: bool = False,
    ps: bool = False,
    jpg: str | None = None,
    jpeg: str | None = None,
    png: str | None = None,
    pnm: str | None = None,
    pngs: str | None = None,
    jpgs: str | None = None,
    jpegs: str | None = None,
    pnms: str | None = None,
    ytran: str | None = None,
    xtran: str | None = None,
    xaxis: str | None = None,
    yaxis: str | None = None,
    ynames: list[str] | None = None,
    volreg: bool = False,
    thick: bool = False,
    thick_: bool = False,
    dashed: str | None = None,
    setenv: str | None = None,
    censor_rgb: str | None = None,
    censor: InputPathType | None = None,
    censortr: list[str] | None = None,
    concat: InputPathType | None = None,
    rbox: str | None = None,
    rbox_: str | None = None,
    line: str | None = None,
    runner: Runner | None = None,
) -> V1dplotOutputs:
    """
    1dplot by AFNI Team.
    
    Graphs the columns of a *.1D time series file to the X11 screen, or to an
    image file (.jpg or .png).
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dplot.html
    
    Args:
        tsfiles: Input time series files (*.1D) to be plotted.
        install: Install a new X11 colormap.
        sep: Plot each column in a separate sub-graph.
        one: Plot all columns together in one big graph.
        sepscl: Plot each column in a separate sub-graph and allow each\
            sub-graph to have a different y-scale. This option is meaningless with\
            -one!.
        noline: Don't plot the connecting lines.
        noline_: Same as -noline, but will not try to plot values outside the\
            rectangular box that contains the graph axes.
        box: Plot a small 'box' at each data point.
        hist: Plot graphs in histogram style (i.e., vertical boxes).
        norm2: Independently scale each time series plotted to have L_2 norm =\
            1 (sum of squares).
        normx: Independently scale each time series plotted to have max\
            absolute value = 1 (L_infinity norm).
        norm1: Independently scale each time series plotted to have max sum of\
            absolute values = 1 (L_1 norm).
        demean: Remove the mean from each time series before normalizing.
        x: Use for X axis the data in a specified .1D file.
        xl10: Use log10 of the specified .1D file as the X axis.
        dx: Spacing between points on the x-axis.
        xzero: Initial x coordinate.
        nopush: Don't 'push' axes ranges outwards.
        ignore: Skip first 'nn' rows in the input file.
        use: Plot 'mm' points.
        xlabel: Put string 'aa' below the x-axis.
        ylabel: Put string 'aa' to the left of the y-axis.
        plabel: Put string 'pp' atop the plot.
        title: Same as -plabel, but only works with -ps/-png/-jpg/-pnm options.
        wintitle: Set string 'pp' as the title of the frame containing the\
            plot.
        naked: Do NOT plot axes or labels, just the graph(s).
        aspect: Set the width-to-height ratio of the plot region to 'A'.
        stdin: Don't read from tsfile; instead, read from stdin and plot it.
        ps: Don't draw plot in a window; instead, write it to stdout in\
            PostScript format.
        jpg: Render plot to JPEG image and save to a file named 'fname'.
        jpeg: Render plot to JPEG image and save to a file named 'fname'.
        png: Render plot to PNG image and save to a file named 'fname'.
        pnm: Render plot to PNM image and save to a file named 'fname'.
        pngs: Render plot to PNG image of specified size and save to a file\
            named 'fname'.
        jpgs: Render plot to JPEG image of specified size and save to a file\
            named 'fname'.
        jpegs: Render plot to JPEG image of specified size and save to a file\
            named 'fname'.
        pnms: Render plot to PNM image of specified size and save to a file\
            named 'fname'.
        ytran: Transform the data along the y-axis by applying the expression\
            to each input value.
        xtran: Transform the data along the x-axis by applying the expression\
            to each input value.
        xaxis: Set the x-axis to run from value 'b' to value 't', with 'n'\
            major divisions and 'm' minor tic marks per major division.
        yaxis: Set the y-axis to run from value 'b' to value 't', with 'n'\
            major divisions and 'm' minor tic marks per major division.
        ynames: Use the strings as labels to the right of the graphs,\
            corresponding to each input column.
        volreg: Makes the 'ynames' be the same as the 6 labels used in\
            plug_volreg for Roll, Pitch, Yaw, I-S, R-L, and A-P movements.
        thick: Increase the line thickness used for plotting.
        thick_: Twice the power of '-thick' at no extra cost!.
        dashed: Plot dashed lines between data points using specified\
            colon-separated list of dash values (1: solid, 2: longer dashes, 3:\
            shorter dashes).
        setenv: Set environment variable 'name' to 'val' for this run of the\
            program only.
        censor_rgb: Set the color used for marking to a specified color.
        censor: Specify the filename of the censor .1D time series.
        censortr: Specify time indexes to be marked in the graph(s).
        concat: Specify the filename for the list of concatenated runs.
        rbox: Draw a rectangular box with specified corners and colors.
        rbox_: Draw a rectangular box with one extra horizontal line.
        line: Draw one line segment.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DPLOT_METADATA)
    cargs = []
    cargs.append("1dplot")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in tsfiles])
    ret = V1dplotOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dplotOutputs",
    "V_1DPLOT_METADATA",
    "v_1dplot",
]