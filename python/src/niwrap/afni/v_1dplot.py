# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1DPLOT_METADATA = Metadata(
    id="8a73ee3a42ebaf653aef47adb6f3fa781e513997.boutiques",
    name="1dplot",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dplotParameters = typing.TypedDict('V1dplotParameters', {
    "__STYX_TYPE__": typing.Literal["1dplot"],
    "tsfiles": list[InputPathType],
    "install": bool,
    "sep": bool,
    "one": bool,
    "sepscl": bool,
    "NOLINE": bool,
    "NOLINE_1": bool,
    "box": bool,
    "hist": bool,
    "norm2": bool,
    "normx": bool,
    "norm1": bool,
    "demean": bool,
    "x": typing.NotRequired[InputPathType | None],
    "xl10": typing.NotRequired[InputPathType | None],
    "dx": typing.NotRequired[float | None],
    "xzero": typing.NotRequired[float | None],
    "nopush": bool,
    "ignore": typing.NotRequired[float | None],
    "use": typing.NotRequired[float | None],
    "xlabel": typing.NotRequired[str | None],
    "ylabel": typing.NotRequired[str | None],
    "plabel": typing.NotRequired[str | None],
    "title": typing.NotRequired[str | None],
    "wintitle": typing.NotRequired[str | None],
    "naked": bool,
    "aspect": typing.NotRequired[float | None],
    "stdin": bool,
    "ps": bool,
    "jpg": typing.NotRequired[str | None],
    "jpeg": typing.NotRequired[str | None],
    "png": typing.NotRequired[str | None],
    "pnm": typing.NotRequired[str | None],
    "pngs": typing.NotRequired[str | None],
    "jpgs": typing.NotRequired[str | None],
    "jpegs": typing.NotRequired[str | None],
    "pnms": typing.NotRequired[str | None],
    "ytran": typing.NotRequired[str | None],
    "xtran": typing.NotRequired[str | None],
    "xaxis": typing.NotRequired[str | None],
    "yaxis": typing.NotRequired[str | None],
    "ynames": typing.NotRequired[list[str] | None],
    "volreg": bool,
    "THICK": bool,
    "THICK_1": bool,
    "dashed": typing.NotRequired[str | None],
    "setenv": typing.NotRequired[str | None],
    "censor_RGB": typing.NotRequired[str | None],
    "censor": typing.NotRequired[InputPathType | None],
    "CENSORTR": typing.NotRequired[list[str] | None],
    "concat": typing.NotRequired[InputPathType | None],
    "Rbox": typing.NotRequired[str | None],
    "Rbox_1": typing.NotRequired[str | None],
    "line": typing.NotRequired[str | None],
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
        "1dplot": v_1dplot_cargs,
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
    }.get(t)


class V1dplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1dplot_params(
    tsfiles: list[InputPathType],
    install: bool = False,
    sep: bool = False,
    one: bool = False,
    sepscl: bool = False,
    noline: bool = False,
    noline_1: bool = False,
    box: bool = False,
    hist: bool = False,
    norm2: bool = False,
    normx: bool = False,
    norm1: bool = False,
    demean: bool = False,
    x: InputPathType | None = None,
    xl10: InputPathType | None = None,
    dx: float | None = None,
    xzero: float | None = None,
    nopush: bool = False,
    ignore: float | None = None,
    use: float | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    plabel: str | None = None,
    title: str | None = None,
    wintitle: str | None = None,
    naked: bool = False,
    aspect: float | None = None,
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
    thick_1: bool = False,
    dashed: str | None = None,
    setenv: str | None = None,
    censor_rgb: str | None = None,
    censor: InputPathType | None = None,
    censortr: list[str] | None = None,
    concat: InputPathType | None = None,
    rbox: str | None = None,
    rbox_1: str | None = None,
    line: str | None = None,
) -> V1dplotParameters:
    """
    Build parameters.
    
    Args:
        tsfiles: Input time series files (*.1D) to be plotted.
        install: Install a new X11 colormap.
        sep: Plot each column in a separate sub-graph.
        one: Plot all columns together in one big graph.
        sepscl: Plot each column in a separate sub-graph and allow each\
            sub-graph to have a different y-scale. This option is meaningless with\
            -one!.
        noline: Same as -noline, but will not try to plot values outside the\
            rectangular box that contains the graph axes.
        noline_1: Same as -noline, but will not try to plot values outside the\
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
        thick: Twice the power of '-thick' at no extra cost!.
        thick_1: Twice the power of '-thick' at no extra cost!.
        dashed: Plot dashed lines between data points using specified\
            colon-separated list of dash values (1: solid, 2: longer dashes, 3:\
            shorter dashes).
        setenv: Set environment variable 'name' to 'val' for this run of the\
            program only.
        censor_rgb: Set the color used for marking to a specified color.
        censor: Specify the filename of the censor .1D time series.
        censortr: Specify time indexes to be marked in the graph(s).
        concat: Specify the filename for the list of concatenated runs.
        rbox: Draw a rectangular box with one extra horizontal line.
        rbox_1: Draw a rectangular box with one extra horizontal line.
        line: Draw one line segment.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dplot",
        "tsfiles": tsfiles,
        "install": install,
        "sep": sep,
        "one": one,
        "sepscl": sepscl,
        "NOLINE": noline,
        "NOLINE_1": noline_1,
        "box": box,
        "hist": hist,
        "norm2": norm2,
        "normx": normx,
        "norm1": norm1,
        "demean": demean,
        "nopush": nopush,
        "naked": naked,
        "stdin": stdin,
        "ps": ps,
        "volreg": volreg,
        "THICK": thick,
        "THICK_1": thick_1,
    }
    if x is not None:
        params["x"] = x
    if xl10 is not None:
        params["xl10"] = xl10
    if dx is not None:
        params["dx"] = dx
    if xzero is not None:
        params["xzero"] = xzero
    if ignore is not None:
        params["ignore"] = ignore
    if use is not None:
        params["use"] = use
    if xlabel is not None:
        params["xlabel"] = xlabel
    if ylabel is not None:
        params["ylabel"] = ylabel
    if plabel is not None:
        params["plabel"] = plabel
    if title is not None:
        params["title"] = title
    if wintitle is not None:
        params["wintitle"] = wintitle
    if aspect is not None:
        params["aspect"] = aspect
    if jpg is not None:
        params["jpg"] = jpg
    if jpeg is not None:
        params["jpeg"] = jpeg
    if png is not None:
        params["png"] = png
    if pnm is not None:
        params["pnm"] = pnm
    if pngs is not None:
        params["pngs"] = pngs
    if jpgs is not None:
        params["jpgs"] = jpgs
    if jpegs is not None:
        params["jpegs"] = jpegs
    if pnms is not None:
        params["pnms"] = pnms
    if ytran is not None:
        params["ytran"] = ytran
    if xtran is not None:
        params["xtran"] = xtran
    if xaxis is not None:
        params["xaxis"] = xaxis
    if yaxis is not None:
        params["yaxis"] = yaxis
    if ynames is not None:
        params["ynames"] = ynames
    if dashed is not None:
        params["dashed"] = dashed
    if setenv is not None:
        params["setenv"] = setenv
    if censor_rgb is not None:
        params["censor_RGB"] = censor_rgb
    if censor is not None:
        params["censor"] = censor
    if censortr is not None:
        params["CENSORTR"] = censortr
    if concat is not None:
        params["concat"] = concat
    if rbox is not None:
        params["Rbox"] = rbox
    if rbox_1 is not None:
        params["Rbox_1"] = rbox_1
    if line is not None:
        params["line"] = line
    return params


def v_1dplot_cargs(
    params: V1dplotParameters,
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
    cargs.append("1dplot")
    cargs.extend([execution.input_file(f) for f in params.get("tsfiles")])
    if params.get("install"):
        cargs.append("-install")
    if params.get("sep"):
        cargs.append("-sep")
    if params.get("one"):
        cargs.append("-one")
    if params.get("sepscl"):
        cargs.append("-sepscl")
    if params.get("NOLINE"):
        cargs.append("-NOLINE")
    if params.get("NOLINE_1"):
        cargs.append("-NOLINE")
    if params.get("box"):
        cargs.append("-box")
    if params.get("hist"):
        cargs.append("-hist")
    if params.get("norm2"):
        cargs.append("-norm2")
    if params.get("normx"):
        cargs.append("-normx")
    if params.get("norm1"):
        cargs.append("-norm1")
    if params.get("demean"):
        cargs.append("-demean")
    if params.get("x") is not None:
        cargs.extend([
            "-x",
            execution.input_file(params.get("x"))
        ])
    if params.get("xl10") is not None:
        cargs.extend([
            "-xl10",
            execution.input_file(params.get("xl10"))
        ])
    if params.get("dx") is not None:
        cargs.extend([
            "-dx",
            str(params.get("dx"))
        ])
    if params.get("xzero") is not None:
        cargs.extend([
            "-xzero",
            str(params.get("xzero"))
        ])
    if params.get("nopush"):
        cargs.append("-nopush")
    if params.get("ignore") is not None:
        cargs.extend([
            "-ignore",
            str(params.get("ignore"))
        ])
    if params.get("use") is not None:
        cargs.extend([
            "-use",
            str(params.get("use"))
        ])
    if params.get("xlabel") is not None:
        cargs.extend([
            "-xlabel",
            params.get("xlabel")
        ])
    if params.get("ylabel") is not None:
        cargs.extend([
            "-ylabel",
            params.get("ylabel")
        ])
    if params.get("plabel") is not None:
        cargs.extend([
            "-plabel",
            params.get("plabel")
        ])
    if params.get("title") is not None:
        cargs.extend([
            "-title",
            params.get("title")
        ])
    if params.get("wintitle") is not None:
        cargs.extend([
            "-wintitle",
            params.get("wintitle")
        ])
    if params.get("naked"):
        cargs.append("-naked")
    if params.get("aspect") is not None:
        cargs.extend([
            "-aspect",
            str(params.get("aspect"))
        ])
    if params.get("stdin"):
        cargs.append("-stdin")
    if params.get("ps"):
        cargs.append("-ps")
    if params.get("jpg") is not None:
        cargs.extend([
            "-jpg",
            params.get("jpg")
        ])
    if params.get("jpeg") is not None:
        cargs.extend([
            "-jpeg",
            params.get("jpeg")
        ])
    if params.get("png") is not None:
        cargs.extend([
            "-png",
            params.get("png")
        ])
    if params.get("pnm") is not None:
        cargs.extend([
            "-pnm",
            params.get("pnm")
        ])
    if params.get("pngs") is not None:
        cargs.extend([
            "-pngs",
            params.get("pngs")
        ])
    if params.get("jpgs") is not None:
        cargs.extend([
            "-jpgs",
            params.get("jpgs")
        ])
    if params.get("jpegs") is not None:
        cargs.extend([
            "-jpegs",
            params.get("jpegs")
        ])
    if params.get("pnms") is not None:
        cargs.extend([
            "-pnms",
            params.get("pnms")
        ])
    if params.get("ytran") is not None:
        cargs.extend([
            "-ytran",
            params.get("ytran")
        ])
    if params.get("xtran") is not None:
        cargs.extend([
            "-xtran",
            params.get("xtran")
        ])
    if params.get("xaxis") is not None:
        cargs.extend([
            "-xaxis",
            params.get("xaxis")
        ])
    if params.get("yaxis") is not None:
        cargs.extend([
            "-yaxis",
            params.get("yaxis")
        ])
    if params.get("ynames") is not None:
        cargs.extend([
            "-ynames",
            *params.get("ynames")
        ])
    if params.get("volreg"):
        cargs.append("-volreg")
    if params.get("THICK"):
        cargs.append("-THICK")
    if params.get("THICK_1"):
        cargs.append("-THICK")
    if params.get("dashed") is not None:
        cargs.extend([
            "-dashed",
            params.get("dashed")
        ])
    if params.get("setenv") is not None:
        cargs.extend([
            "-D",
            params.get("setenv")
        ])
    if params.get("censor_RGB") is not None:
        cargs.extend([
            "-censor_RGB",
            params.get("censor_RGB")
        ])
    if params.get("censor") is not None:
        cargs.extend([
            "-censor",
            execution.input_file(params.get("censor"))
        ])
    if params.get("CENSORTR") is not None:
        cargs.extend([
            "-CENSORTR",
            *params.get("CENSORTR")
        ])
    if params.get("concat") is not None:
        cargs.extend([
            "-concat",
            execution.input_file(params.get("concat"))
        ])
    if params.get("Rbox") is not None:
        cargs.extend([
            "-Rbox",
            params.get("Rbox")
        ])
    if params.get("Rbox_1") is not None:
        cargs.extend([
            "-Rbox",
            params.get("Rbox_1")
        ])
    if params.get("line") is not None:
        cargs.extend([
            "-line",
            params.get("line")
        ])
    return cargs


def v_1dplot_outputs(
    params: V1dplotParameters,
    execution: Execution,
) -> V1dplotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dplotOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_1dplot_execute(
    params: V1dplotParameters,
    execution: Execution,
) -> V1dplotOutputs:
    """
    Graphs the columns of a *.1D time series file to the X11 screen, or to an image
    file (.jpg or .png).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dplotOutputs`).
    """
    cargs = v_1dplot_cargs(params, execution)
    ret = v_1dplot_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1dplot(
    tsfiles: list[InputPathType],
    install: bool = False,
    sep: bool = False,
    one: bool = False,
    sepscl: bool = False,
    noline: bool = False,
    noline_1: bool = False,
    box: bool = False,
    hist: bool = False,
    norm2: bool = False,
    normx: bool = False,
    norm1: bool = False,
    demean: bool = False,
    x: InputPathType | None = None,
    xl10: InputPathType | None = None,
    dx: float | None = None,
    xzero: float | None = None,
    nopush: bool = False,
    ignore: float | None = None,
    use: float | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    plabel: str | None = None,
    title: str | None = None,
    wintitle: str | None = None,
    naked: bool = False,
    aspect: float | None = None,
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
    thick_1: bool = False,
    dashed: str | None = None,
    setenv: str | None = None,
    censor_rgb: str | None = None,
    censor: InputPathType | None = None,
    censortr: list[str] | None = None,
    concat: InputPathType | None = None,
    rbox: str | None = None,
    rbox_1: str | None = None,
    line: str | None = None,
    runner: Runner | None = None,
) -> V1dplotOutputs:
    """
    Graphs the columns of a *.1D time series file to the X11 screen, or to an image
    file (.jpg or .png).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        tsfiles: Input time series files (*.1D) to be plotted.
        install: Install a new X11 colormap.
        sep: Plot each column in a separate sub-graph.
        one: Plot all columns together in one big graph.
        sepscl: Plot each column in a separate sub-graph and allow each\
            sub-graph to have a different y-scale. This option is meaningless with\
            -one!.
        noline: Same as -noline, but will not try to plot values outside the\
            rectangular box that contains the graph axes.
        noline_1: Same as -noline, but will not try to plot values outside the\
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
        thick: Twice the power of '-thick' at no extra cost!.
        thick_1: Twice the power of '-thick' at no extra cost!.
        dashed: Plot dashed lines between data points using specified\
            colon-separated list of dash values (1: solid, 2: longer dashes, 3:\
            shorter dashes).
        setenv: Set environment variable 'name' to 'val' for this run of the\
            program only.
        censor_rgb: Set the color used for marking to a specified color.
        censor: Specify the filename of the censor .1D time series.
        censortr: Specify time indexes to be marked in the graph(s).
        concat: Specify the filename for the list of concatenated runs.
        rbox: Draw a rectangular box with one extra horizontal line.
        rbox_1: Draw a rectangular box with one extra horizontal line.
        line: Draw one line segment.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DPLOT_METADATA)
    params = v_1dplot_params(tsfiles=tsfiles, install=install, sep=sep, one=one, sepscl=sepscl, noline=noline, noline_1=noline_1, box=box, hist=hist, norm2=norm2, normx=normx, norm1=norm1, demean=demean, x=x, xl10=xl10, dx=dx, xzero=xzero, nopush=nopush, ignore=ignore, use=use, xlabel=xlabel, ylabel=ylabel, plabel=plabel, title=title, wintitle=wintitle, naked=naked, aspect=aspect, stdin=stdin, ps=ps, jpg=jpg, jpeg=jpeg, png=png, pnm=pnm, pngs=pngs, jpgs=jpgs, jpegs=jpegs, pnms=pnms, ytran=ytran, xtran=xtran, xaxis=xaxis, yaxis=yaxis, ynames=ynames, volreg=volreg, thick=thick, thick_1=thick_1, dashed=dashed, setenv=setenv, censor_rgb=censor_rgb, censor=censor, censortr=censortr, concat=concat, rbox=rbox, rbox_1=rbox_1, line=line)
    return v_1dplot_execute(params, execution)


__all__ = [
    "V1dplotOutputs",
    "V1dplotParameters",
    "V_1DPLOT_METADATA",
    "v_1dplot",
    "v_1dplot_params",
]
