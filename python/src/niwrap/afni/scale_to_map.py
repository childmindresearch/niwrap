# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SCALE_TO_MAP_METADATA = Metadata(
    id="2f7e7a834eba315bf3a7ddf886a5f54b169d9aeb.boutiques",
    name="ScaleToMap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ScaleToMapParameters = typing.TypedDict('ScaleToMapParameters', {
    "__STYX_TYPE__": typing.Literal["ScaleToMap"],
    "input_file": InputPathType,
    "icol": float,
    "vcol": float,
    "cmap": typing.NotRequired[str | None],
    "cmapfile": typing.NotRequired[InputPathType | None],
    "cmapdb": typing.NotRequired[InputPathType | None],
    "frf": bool,
    "clp": typing.NotRequired[list[float] | None],
    "perc_clp": typing.NotRequired[list[float] | None],
    "apr": typing.NotRequired[float | None],
    "anr": typing.NotRequired[float | None],
    "interp": bool,
    "nointerp": bool,
    "direct": bool,
    "msk_zero": bool,
    "msk": typing.NotRequired[list[float] | None],
    "msk_col": typing.NotRequired[list[float] | None],
    "nomsk_col": bool,
    "br": typing.NotRequired[float | None],
    "help": bool,
    "verbose": bool,
    "showmap": bool,
    "showdb": bool,
    "novolreg": bool,
    "noxform": bool,
    "setenv": typing.NotRequired[str | None],
    "TRACE": bool,
    "TRACE": bool,
    "nomall": bool,
    "yesmall": bool,
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
        "ScaleToMap": scale_to_map_cargs,
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
        "ScaleToMap": scale_to_map_outputs,
    }.get(t)


class ScaleToMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scale_to_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scale_to_map_params(
    input_file: InputPathType,
    icol: float,
    vcol: float,
    cmap: str | None = None,
    cmapfile: InputPathType | None = None,
    cmapdb: InputPathType | None = None,
    frf: bool = False,
    clp: list[float] | None = None,
    perc_clp: list[float] | None = None,
    apr: float | None = None,
    anr: float | None = None,
    interp: bool = False,
    nointerp: bool = False,
    direct: bool = False,
    msk_zero: bool = False,
    msk: list[float] | None = None,
    msk_col: list[float] | None = None,
    nomsk_col: bool = False,
    br: float | None = None,
    help_: bool = False,
    verbose: bool = False,
    showmap: bool = False,
    showdb: bool = False,
    novolreg: bool = False,
    noxform: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    trace_2: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
) -> ScaleToMapParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file in 1D formatted ascii containing node values.
        icol: Index of node index column (-1 if node index is implicit).
        vcol: Index of node value column.
        cmap: Choose one of the standard colormaps available with SUMA.
        cmapfile: Read color map from a Mapfile.
        cmapdb: Read color maps from an AFNI .pal file.
        frf: Indicate that the first row in the file is the first color.
        clp: Clip values in IntVect to specified range.
        perc_clp: Percentile clip values in IntVect to specified range.
        apr: Clip values in IntVect to [0 range].
        anr: Clip values in IntVect to [-range range].
        interp: Use color interpolation between colors in colormap (default).
        nointerp: Turn off color interpolation within the colormap.
        direct: Directly map values to index of color in colormap.
        msk_zero: Mask values that are 0.
        msk: Mask values in vcol between specified range.
        msk_col: Set color of masked voxels.
        nomsk_col: Do not output nodes that got masked.
        br: Apply a brightness factor to colormap and mask color.
        help_: Display help message.
        verbose: Verbose mode.
        showmap: Print colormap to screen and quit.
        showdb: Print colors and colormaps of AFNI along with any loaded from\
            Palfile.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        setenv: Set environment variable ENVname to ENVvalue. Quotes are\
            necessary.
        trace_: Turn on extreme tracing.
        trace_2: Turn on extreme tracing.
        nomall: Turn off memory tracing.
        yesmall: Turn on memory tracing (default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ScaleToMap",
        "input_file": input_file,
        "icol": icol,
        "vcol": vcol,
        "frf": frf,
        "interp": interp,
        "nointerp": nointerp,
        "direct": direct,
        "msk_zero": msk_zero,
        "nomsk_col": nomsk_col,
        "help": help_,
        "verbose": verbose,
        "showmap": showmap,
        "showdb": showdb,
        "novolreg": novolreg,
        "noxform": noxform,
        "TRACE": trace_,
        "TRACE": trace_2,
        "nomall": nomall,
        "yesmall": yesmall,
    }
    if cmap is not None:
        params["cmap"] = cmap
    if cmapfile is not None:
        params["cmapfile"] = cmapfile
    if cmapdb is not None:
        params["cmapdb"] = cmapdb
    if clp is not None:
        params["clp"] = clp
    if perc_clp is not None:
        params["perc_clp"] = perc_clp
    if apr is not None:
        params["apr"] = apr
    if anr is not None:
        params["anr"] = anr
    if msk is not None:
        params["msk"] = msk
    if msk_col is not None:
        params["msk_col"] = msk_col
    if br is not None:
        params["br"] = br
    if setenv is not None:
        params["setenv"] = setenv
    return params


def scale_to_map_cargs(
    params: ScaleToMapParameters,
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
    cargs.append("ScaleToMap")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(str(params.get("icol")))
    cargs.append(str(params.get("vcol")))
    if params.get("cmap") is not None:
        cargs.extend([
            "-cmap",
            params.get("cmap")
        ])
    if params.get("cmapfile") is not None:
        cargs.extend([
            "-cmapfile",
            execution.input_file(params.get("cmapfile"))
        ])
    if params.get("cmapdb") is not None:
        cargs.extend([
            "-cmapdb",
            execution.input_file(params.get("cmapdb"))
        ])
    if params.get("frf"):
        cargs.append("-frf")
    if params.get("clp") is not None:
        cargs.extend([
            "-clp",
            *map(str, params.get("clp"))
        ])
    if params.get("perc_clp") is not None:
        cargs.extend([
            "-perc_clp",
            *map(str, params.get("perc_clp"))
        ])
    if params.get("apr") is not None:
        cargs.extend([
            "-apr",
            str(params.get("apr"))
        ])
    if params.get("anr") is not None:
        cargs.extend([
            "-anr",
            str(params.get("anr"))
        ])
    if params.get("interp"):
        cargs.append("-interp")
    if params.get("nointerp"):
        cargs.append("-nointerp")
    if params.get("direct"):
        cargs.append("-direct")
    if params.get("msk_zero"):
        cargs.append("-msk_zero")
    if params.get("msk") is not None:
        cargs.extend([
            "-msk",
            *map(str, params.get("msk"))
        ])
    if params.get("msk_col") is not None:
        cargs.extend([
            "-msk_col",
            *map(str, params.get("msk_col"))
        ])
    if params.get("nomsk_col"):
        cargs.append("-nomsk_col")
    if params.get("br") is not None:
        cargs.extend([
            "-br",
            str(params.get("br"))
        ])
    if params.get("help"):
        cargs.append("-h")
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("showmap"):
        cargs.append("-showmap")
    if params.get("showdb"):
        cargs.append("-showdb")
    if params.get("novolreg"):
        cargs.append("-novolreg")
    if params.get("noxform"):
        cargs.append("-noxform")
    if params.get("setenv") is not None:
        cargs.extend([
            "-setenv",
            params.get("setenv")
        ])
    if params.get("TRACE"):
        cargs.append("-TRACE")
    if params.get("TRACE"):
        cargs.append("-TRACE")
    if params.get("nomall"):
        cargs.append("-nomall")
    if params.get("yesmall"):
        cargs.append("-yesmall")
    return cargs


def scale_to_map_outputs(
    params: ScaleToMapParameters,
    execution: Execution,
) -> ScaleToMapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ScaleToMapOutputs(
        root=execution.output_file("."),
    )
    return ret


def scale_to_map_execute(
    params: ScaleToMapParameters,
    execution: Execution,
) -> ScaleToMapOutputs:
    """
    Tool to scale values to a color map.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ScaleToMapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = scale_to_map_cargs(params, execution)
    ret = scale_to_map_outputs(params, execution)
    execution.run(cargs)
    return ret


def scale_to_map(
    input_file: InputPathType,
    icol: float,
    vcol: float,
    cmap: str | None = None,
    cmapfile: InputPathType | None = None,
    cmapdb: InputPathType | None = None,
    frf: bool = False,
    clp: list[float] | None = None,
    perc_clp: list[float] | None = None,
    apr: float | None = None,
    anr: float | None = None,
    interp: bool = False,
    nointerp: bool = False,
    direct: bool = False,
    msk_zero: bool = False,
    msk: list[float] | None = None,
    msk_col: list[float] | None = None,
    nomsk_col: bool = False,
    br: float | None = None,
    help_: bool = False,
    verbose: bool = False,
    showmap: bool = False,
    showdb: bool = False,
    novolreg: bool = False,
    noxform: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    trace_2: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
    runner: Runner | None = None,
) -> ScaleToMapOutputs:
    """
    Tool to scale values to a color map.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input file in 1D formatted ascii containing node values.
        icol: Index of node index column (-1 if node index is implicit).
        vcol: Index of node value column.
        cmap: Choose one of the standard colormaps available with SUMA.
        cmapfile: Read color map from a Mapfile.
        cmapdb: Read color maps from an AFNI .pal file.
        frf: Indicate that the first row in the file is the first color.
        clp: Clip values in IntVect to specified range.
        perc_clp: Percentile clip values in IntVect to specified range.
        apr: Clip values in IntVect to [0 range].
        anr: Clip values in IntVect to [-range range].
        interp: Use color interpolation between colors in colormap (default).
        nointerp: Turn off color interpolation within the colormap.
        direct: Directly map values to index of color in colormap.
        msk_zero: Mask values that are 0.
        msk: Mask values in vcol between specified range.
        msk_col: Set color of masked voxels.
        nomsk_col: Do not output nodes that got masked.
        br: Apply a brightness factor to colormap and mask color.
        help_: Display help message.
        verbose: Verbose mode.
        showmap: Print colormap to screen and quit.
        showdb: Print colors and colormaps of AFNI along with any loaded from\
            Palfile.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        setenv: Set environment variable ENVname to ENVvalue. Quotes are\
            necessary.
        trace_: Turn on extreme tracing.
        trace_2: Turn on extreme tracing.
        nomall: Turn off memory tracing.
        yesmall: Turn on memory tracing (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ScaleToMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCALE_TO_MAP_METADATA)
    params = scale_to_map_params(input_file=input_file, icol=icol, vcol=vcol, cmap=cmap, cmapfile=cmapfile, cmapdb=cmapdb, frf=frf, clp=clp, perc_clp=perc_clp, apr=apr, anr=anr, interp=interp, nointerp=nointerp, direct=direct, msk_zero=msk_zero, msk=msk, msk_col=msk_col, nomsk_col=nomsk_col, br=br, help_=help_, verbose=verbose, showmap=showmap, showdb=showdb, novolreg=novolreg, noxform=noxform, setenv=setenv, trace_=trace_, trace_2=trace_2, nomall=nomall, yesmall=yesmall)
    return scale_to_map_execute(params, execution)


__all__ = [
    "SCALE_TO_MAP_METADATA",
    "ScaleToMapOutputs",
    "ScaleToMapParameters",
    "scale_to_map",
    "scale_to_map_params",
]
