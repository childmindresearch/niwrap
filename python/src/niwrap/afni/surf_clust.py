# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_CLUST_METADATA = Metadata(
    id="2346425eb197f04f33322dea847636dd74a3b8a3.boutiques",
    name="SurfClust",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfClustParameters = typing.TypedDict('SurfClustParameters', {
    "__STYX_TYPE__": typing.Literal["SurfClust"],
    "specfile": typing.NotRequired[InputPathType | None],
    "input_surface": typing.NotRequired[str | None],
    "input_surf_name": typing.NotRequired[InputPathType | None],
    "input_dataset": list[InputPathType],
    "rmm": float,
    "amm2": typing.NotRequired[float | None],
    "min_nodes": typing.NotRequired[float | None],
    "prefix": typing.NotRequired[str | None],
    "out_clusterdset": bool,
    "out_roidset": bool,
    "out_fulllist": bool,
    "sort_none": bool,
    "sort_n_nodes": bool,
    "sort_area": bool,
    "thresh_col": typing.NotRequired[float | None],
    "thresh": typing.NotRequired[float | None],
    "athresh": typing.NotRequired[float | None],
    "ir_range": typing.NotRequired[list[float] | None],
    "ex_range": typing.NotRequired[list[float] | None],
    "prepend_node_index": bool,
    "update": typing.NotRequired[float | None],
    "no_cent": bool,
    "cent": bool,
    "novolreg": bool,
    "noxform": bool,
    "set_env": typing.NotRequired[str | None],
    "trace": bool,
    "trace_extreme": bool,
    "no_memory_trace": bool,
    "yes_memory_trace": bool,
    "mini_help": bool,
    "help": bool,
    "extreme_help": bool,
    "view_help": bool,
    "web_help": bool,
    "find_help": typing.NotRequired[str | None],
    "raw_help": bool,
    "spx_help": bool,
    "aspx_help": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "SurfClust": surf_clust_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "SurfClust": surf_clust_outputs,
    }
    return vt.get(t)


class SurfClustOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_clust(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cluster_table: OutputPathType | None
    """Cluster table output"""
    clustered_dataset: OutputPathType | None
    """Clustered version of input dataset"""
    roi_dataset: OutputPathType | None
    """ROI dataset with rank of clusters"""


def surf_clust_params(
    input_dataset: list[InputPathType],
    rmm: float,
    specfile: InputPathType | None = None,
    input_surface: str | None = None,
    input_surf_name: InputPathType | None = None,
    amm2: float | None = None,
    min_nodes: float | None = None,
    prefix: str | None = None,
    out_clusterdset: bool = False,
    out_roidset: bool = False,
    out_fulllist: bool = False,
    sort_none: bool = False,
    sort_n_nodes: bool = False,
    sort_area: bool = False,
    thresh_col: float | None = None,
    thresh: float | None = None,
    athresh: float | None = None,
    ir_range: list[float] | None = None,
    ex_range: list[float] | None = None,
    prepend_node_index: bool = False,
    update_: float | None = None,
    no_cent: bool = False,
    cent: bool = False,
    novolreg: bool = False,
    noxform: bool = False,
    set_env: str | None = None,
    trace_: bool = False,
    trace_extreme: bool = False,
    no_memory_trace: bool = False,
    yes_memory_trace: bool = False,
    mini_help: bool = False,
    help_: bool = False,
    extreme_help: bool = False,
    view_help: bool = False,
    web_help: bool = False,
    find_help: str | None = None,
    raw_help: bool = False,
    spx_help: bool = False,
    aspx_help: bool = False,
) -> SurfClustParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: The input dataset and the index of the datacolumn to use\
            (index 0 for 1st column). Values of 0 indicate inactive nodes.
        rmm: Maximum distance between an activated node and the cluster to\
            which it belongs.
        specfile: The surface spec file.
        input_surface: The input surface name.
        input_surf_name: Full name of the input surface.
        amm2: Minimum area for clusters.
        min_nodes: Minimum nodes for clusters.
        prefix: Prefix for output. Default is the prefix of the input dataset.
        out_clusterdset: Output a clustered version of input dataset.
        out_roidset: Output an ROI dataset with the rank of its cluster.
        out_fulllist: Output a value for all nodes of input surface.
        sort_none: No sorting of ROI clusters.
        sort_n_nodes: Sorting based on number of nodes in cluster.
        sort_area: Sorting based on area of clusters (default).
        thresh_col: Index of thresholding column. Default is column 0.
        thresh: Apply thresholding prior to clustering.
        athresh: Apply absolute thresholding prior to clustering.
        ir_range: Apply thresholding in range. A node n is considered if\
            thresh_col[n] >= R0 && thresh_col[n] <= R1.
        ex_range: Apply thresholding outside of range. A node n is considered\
            if thresh_col[n] < R0 || thresh_col[n] > R1.
        prepend_node_index: Force the output dataset to have node indices in\
            column 0 of output.
        update_: Pacify me when perc of the data have been processed. perc is\
            between 1% and 50%. Default is no update.
        no_cent: Do not find the central nodes.
        cent: Do find the central nodes (default).
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        set_env: Set environment variable ENVname to be ENVvalue. Quotes are\
            necessary.
        trace_: Turns on In/Out debug and Memory tracing.
        trace_extreme: Turns on extreme tracing.
        no_memory_trace: Turn off memory tracing.
        yes_memory_trace: Turn on memory tracing (default).
        mini_help: Mini help, same as -help in many cases.
        help_: The entire help output.
        extreme_help: Extreme help, same as -help in majority of cases.
        view_help: Open help in text editor. AFNI will try to find a GUI editor\
            on your machine. You can control which it should use by setting\
            environment variable AFNI_GUI_EDITOR.
        web_help: Open help in web browser. AFNI will try to find a browser.\
            You can control which it should use by setting environment variable\
            AFNI_GUI_EDITOR.
        find_help: Look for lines in this program's -help output that match\
            (approximately) the given word.
        raw_help: Help string unedited.
        spx_help: Help string in sphinx format, but do not try to autoformat.
        aspx_help: Help string in sphinx format with autoformatting of options.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfClust",
        "input_dataset": input_dataset,
        "rmm": rmm,
        "out_clusterdset": out_clusterdset,
        "out_roidset": out_roidset,
        "out_fulllist": out_fulllist,
        "sort_none": sort_none,
        "sort_n_nodes": sort_n_nodes,
        "sort_area": sort_area,
        "prepend_node_index": prepend_node_index,
        "no_cent": no_cent,
        "cent": cent,
        "novolreg": novolreg,
        "noxform": noxform,
        "trace": trace_,
        "trace_extreme": trace_extreme,
        "no_memory_trace": no_memory_trace,
        "yes_memory_trace": yes_memory_trace,
        "mini_help": mini_help,
        "help": help_,
        "extreme_help": extreme_help,
        "view_help": view_help,
        "web_help": web_help,
        "raw_help": raw_help,
        "spx_help": spx_help,
        "aspx_help": aspx_help,
    }
    if specfile is not None:
        params["specfile"] = specfile
    if input_surface is not None:
        params["input_surface"] = input_surface
    if input_surf_name is not None:
        params["input_surf_name"] = input_surf_name
    if amm2 is not None:
        params["amm2"] = amm2
    if min_nodes is not None:
        params["min_nodes"] = min_nodes
    if prefix is not None:
        params["prefix"] = prefix
    if thresh_col is not None:
        params["thresh_col"] = thresh_col
    if thresh is not None:
        params["thresh"] = thresh
    if athresh is not None:
        params["athresh"] = athresh
    if ir_range is not None:
        params["ir_range"] = ir_range
    if ex_range is not None:
        params["ex_range"] = ex_range
    if update_ is not None:
        params["update"] = update_
    if set_env is not None:
        params["set_env"] = set_env
    if find_help is not None:
        params["find_help"] = find_help
    return params


def surf_clust_cargs(
    params: SurfClustParameters,
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
    cargs.append("SurfClust")
    if params.get("specfile") is not None:
        cargs.extend([
            "-spec",
            execution.input_file(params.get("specfile"))
        ])
    if params.get("input_surface") is not None:
        cargs.extend([
            "-surf_A",
            params.get("input_surface")
        ])
    if params.get("input_surf_name") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("input_surf_name"))
        ])
    cargs.extend([
        "-input",
        *[execution.input_file(f) for f in params.get("input_dataset")]
    ])
    cargs.extend([
        "-rmm",
        str(params.get("rmm"))
    ])
    if params.get("amm2") is not None:
        cargs.extend([
            "-amm2",
            str(params.get("amm2"))
        ])
    if params.get("min_nodes") is not None:
        cargs.extend([
            "-n",
            str(params.get("min_nodes"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("out_clusterdset"):
        cargs.append("-out_clusterdset")
    if params.get("out_roidset"):
        cargs.append("-out_roidset")
    if params.get("out_fulllist"):
        cargs.append("-out_fulllist")
    if params.get("sort_none"):
        cargs.append("-sort_none")
    if params.get("sort_n_nodes"):
        cargs.append("-sort_n_nodes")
    if params.get("sort_area"):
        cargs.append("-sort_area")
    if params.get("thresh_col") is not None:
        cargs.extend([
            "-thresh_col",
            str(params.get("thresh_col"))
        ])
    if params.get("thresh") is not None:
        cargs.extend([
            "-thresh",
            str(params.get("thresh"))
        ])
    if params.get("athresh") is not None:
        cargs.extend([
            "-athresh",
            str(params.get("athresh"))
        ])
    if params.get("ir_range") is not None:
        cargs.extend([
            "-ir_range",
            *map(str, params.get("ir_range"))
        ])
    if params.get("ex_range") is not None:
        cargs.extend([
            "-ex_range",
            *map(str, params.get("ex_range"))
        ])
    if params.get("prepend_node_index"):
        cargs.append("-prepend_node_index")
    if params.get("update") is not None:
        cargs.extend([
            "-update",
            str(params.get("update"))
        ])
    if params.get("no_cent"):
        cargs.append("-no_cent")
    if params.get("cent"):
        cargs.append("-cent")
    if params.get("novolreg"):
        cargs.append("-novolreg")
    if params.get("noxform"):
        cargs.append("-noxform")
    if params.get("set_env") is not None:
        cargs.extend([
            "-setenv",
            params.get("set_env")
        ])
    if params.get("trace"):
        cargs.append("-trace")
    if params.get("trace_extreme"):
        cargs.append("-TRACE")
    if params.get("no_memory_trace"):
        cargs.append("-nomall")
    if params.get("yes_memory_trace"):
        cargs.append("-yesmall")
    if params.get("mini_help"):
        cargs.append("-h")
    if params.get("help"):
        cargs.append("-help")
    if params.get("extreme_help"):
        cargs.append("-HELP")
    if params.get("view_help"):
        cargs.append("-h_view")
    if params.get("web_help"):
        cargs.append("-h_web")
    if params.get("find_help") is not None:
        cargs.extend([
            "-h_find",
            params.get("find_help")
        ])
    if params.get("raw_help"):
        cargs.append("-h_raw")
    if params.get("spx_help"):
        cargs.append("-h_spx")
    if params.get("aspx_help"):
        cargs.append("-h_aspx")
    return cargs


def surf_clust_outputs(
    params: SurfClustParameters,
    execution: Execution,
) -> SurfClustOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfClustOutputs(
        root=execution.output_file("."),
        cluster_table=execution.output_file(params.get("prefix") + "_ClstTable_rXX_aXX.1D") if (params.get("prefix") is not None) else None,
        clustered_dataset=execution.output_file(params.get("prefix") + "_Clustered_rXX_aXX.dset") if (params.get("prefix") is not None) else None,
        roi_dataset=execution.output_file(params.get("prefix") + "_ClstMsk_rXX_aXX.dset") if (params.get("prefix") is not None) else None,
    )
    return ret


def surf_clust_execute(
    params: SurfClustParameters,
    execution: Execution,
) -> SurfClustOutputs:
    """
    A program to perform clustering analysis surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfClustOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surf_clust_cargs(params, execution)
    ret = surf_clust_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_clust(
    input_dataset: list[InputPathType],
    rmm: float,
    specfile: InputPathType | None = None,
    input_surface: str | None = None,
    input_surf_name: InputPathType | None = None,
    amm2: float | None = None,
    min_nodes: float | None = None,
    prefix: str | None = None,
    out_clusterdset: bool = False,
    out_roidset: bool = False,
    out_fulllist: bool = False,
    sort_none: bool = False,
    sort_n_nodes: bool = False,
    sort_area: bool = False,
    thresh_col: float | None = None,
    thresh: float | None = None,
    athresh: float | None = None,
    ir_range: list[float] | None = None,
    ex_range: list[float] | None = None,
    prepend_node_index: bool = False,
    update_: float | None = None,
    no_cent: bool = False,
    cent: bool = False,
    novolreg: bool = False,
    noxform: bool = False,
    set_env: str | None = None,
    trace_: bool = False,
    trace_extreme: bool = False,
    no_memory_trace: bool = False,
    yes_memory_trace: bool = False,
    mini_help: bool = False,
    help_: bool = False,
    extreme_help: bool = False,
    view_help: bool = False,
    web_help: bool = False,
    find_help: str | None = None,
    raw_help: bool = False,
    spx_help: bool = False,
    aspx_help: bool = False,
    runner: Runner | None = None,
) -> SurfClustOutputs:
    """
    A program to perform clustering analysis surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: The input dataset and the index of the datacolumn to use\
            (index 0 for 1st column). Values of 0 indicate inactive nodes.
        rmm: Maximum distance between an activated node and the cluster to\
            which it belongs.
        specfile: The surface spec file.
        input_surface: The input surface name.
        input_surf_name: Full name of the input surface.
        amm2: Minimum area for clusters.
        min_nodes: Minimum nodes for clusters.
        prefix: Prefix for output. Default is the prefix of the input dataset.
        out_clusterdset: Output a clustered version of input dataset.
        out_roidset: Output an ROI dataset with the rank of its cluster.
        out_fulllist: Output a value for all nodes of input surface.
        sort_none: No sorting of ROI clusters.
        sort_n_nodes: Sorting based on number of nodes in cluster.
        sort_area: Sorting based on area of clusters (default).
        thresh_col: Index of thresholding column. Default is column 0.
        thresh: Apply thresholding prior to clustering.
        athresh: Apply absolute thresholding prior to clustering.
        ir_range: Apply thresholding in range. A node n is considered if\
            thresh_col[n] >= R0 && thresh_col[n] <= R1.
        ex_range: Apply thresholding outside of range. A node n is considered\
            if thresh_col[n] < R0 || thresh_col[n] > R1.
        prepend_node_index: Force the output dataset to have node indices in\
            column 0 of output.
        update_: Pacify me when perc of the data have been processed. perc is\
            between 1% and 50%. Default is no update.
        no_cent: Do not find the central nodes.
        cent: Do find the central nodes (default).
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        set_env: Set environment variable ENVname to be ENVvalue. Quotes are\
            necessary.
        trace_: Turns on In/Out debug and Memory tracing.
        trace_extreme: Turns on extreme tracing.
        no_memory_trace: Turn off memory tracing.
        yes_memory_trace: Turn on memory tracing (default).
        mini_help: Mini help, same as -help in many cases.
        help_: The entire help output.
        extreme_help: Extreme help, same as -help in majority of cases.
        view_help: Open help in text editor. AFNI will try to find a GUI editor\
            on your machine. You can control which it should use by setting\
            environment variable AFNI_GUI_EDITOR.
        web_help: Open help in web browser. AFNI will try to find a browser.\
            You can control which it should use by setting environment variable\
            AFNI_GUI_EDITOR.
        find_help: Look for lines in this program's -help output that match\
            (approximately) the given word.
        raw_help: Help string unedited.
        spx_help: Help string in sphinx format, but do not try to autoformat.
        aspx_help: Help string in sphinx format with autoformatting of options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfClustOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_CLUST_METADATA)
    params = surf_clust_params(specfile=specfile, input_surface=input_surface, input_surf_name=input_surf_name, input_dataset=input_dataset, rmm=rmm, amm2=amm2, min_nodes=min_nodes, prefix=prefix, out_clusterdset=out_clusterdset, out_roidset=out_roidset, out_fulllist=out_fulllist, sort_none=sort_none, sort_n_nodes=sort_n_nodes, sort_area=sort_area, thresh_col=thresh_col, thresh=thresh, athresh=athresh, ir_range=ir_range, ex_range=ex_range, prepend_node_index=prepend_node_index, update_=update_, no_cent=no_cent, cent=cent, novolreg=novolreg, noxform=noxform, set_env=set_env, trace_=trace_, trace_extreme=trace_extreme, no_memory_trace=no_memory_trace, yes_memory_trace=yes_memory_trace, mini_help=mini_help, help_=help_, extreme_help=extreme_help, view_help=view_help, web_help=web_help, find_help=find_help, raw_help=raw_help, spx_help=spx_help, aspx_help=aspx_help)
    return surf_clust_execute(params, execution)


__all__ = [
    "SURF_CLUST_METADATA",
    "SurfClustOutputs",
    "SurfClustParameters",
    "surf_clust",
    "surf_clust_params",
]
