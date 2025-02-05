# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKEDIT_METADATA = Metadata(
    id="e2f6cba90c1172611cb544017f9c4f8e312c397d.boutiques",
    name="tckedit",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
TckeditVariousStringParameters = typing.TypedDict('TckeditVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
TckeditVariousFileParameters = typing.TypedDict('TckeditVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
TckeditIncludeParameters = typing.TypedDict('TckeditIncludeParameters', {
    "__STYX_TYPE__": typing.Literal["include"],
    "spec": typing.Union[TckeditVariousStringParameters, TckeditVariousFileParameters],
})
TckeditIncludeOrderedParameters = typing.TypedDict('TckeditIncludeOrderedParameters', {
    "__STYX_TYPE__": typing.Literal["include_ordered"],
    "image": str,
})
TckeditVariousStringParameters_ = typing.TypedDict('TckeditVariousStringParameters_', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
TckeditVariousFileParameters_ = typing.TypedDict('TckeditVariousFileParameters_', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
TckeditExcludeParameters = typing.TypedDict('TckeditExcludeParameters', {
    "__STYX_TYPE__": typing.Literal["exclude"],
    "spec": typing.Union[TckeditVariousStringParameters_, TckeditVariousFileParameters_],
})
TckeditVariousStringParameters_2 = typing.TypedDict('TckeditVariousStringParameters_2', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
TckeditVariousFileParameters_2 = typing.TypedDict('TckeditVariousFileParameters_2', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
TckeditMaskParameters = typing.TypedDict('TckeditMaskParameters', {
    "__STYX_TYPE__": typing.Literal["mask"],
    "spec": typing.Union[TckeditVariousStringParameters_2, TckeditVariousFileParameters_2],
})
TckeditConfigParameters = typing.TypedDict('TckeditConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
TckeditParameters = typing.TypedDict('TckeditParameters', {
    "__STYX_TYPE__": typing.Literal["tckedit"],
    "include": typing.NotRequired[list[TckeditIncludeParameters] | None],
    "include_ordered": typing.NotRequired[list[TckeditIncludeOrderedParameters] | None],
    "exclude": typing.NotRequired[list[TckeditExcludeParameters] | None],
    "mask": typing.NotRequired[list[TckeditMaskParameters] | None],
    "maxlength": typing.NotRequired[float | None],
    "minlength": typing.NotRequired[float | None],
    "number": typing.NotRequired[int | None],
    "skip": typing.NotRequired[int | None],
    "maxweight": typing.NotRequired[float | None],
    "minweight": typing.NotRequired[float | None],
    "inverse": bool,
    "ends_only": bool,
    "tck_weights_in": typing.NotRequired[InputPathType | None],
    "tck_weights_out": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TckeditConfigParameters] | None],
    "help": bool,
    "version": bool,
    "tracks_in": list[InputPathType],
    "tracks_out": str,
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
        "tckedit": tckedit_cargs,
        "include": tckedit_include_cargs,
        "VariousString": tckedit_various_string_cargs,
        "VariousFile": tckedit_various_file_cargs,
        "include_ordered": tckedit_include_ordered_cargs,
        "exclude": tckedit_exclude_cargs,
        "VariousString": tckedit_various_string_cargs_,
        "VariousFile": tckedit_various_file_cargs_,
        "mask": tckedit_mask_cargs,
        "VariousString": tckedit_various_string_cargs_2,
        "VariousFile": tckedit_various_file_cargs_2,
        "config": tckedit_config_cargs,
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
        "tckedit": tckedit_outputs,
    }
    return vt.get(t)


def tckedit_various_string_params(
    obj: str,
) -> TckeditVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def tckedit_various_string_cargs(
    params: TckeditVariousStringParameters,
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
    cargs.append(params.get("obj"))
    return cargs


def tckedit_various_file_params(
    obj: InputPathType,
) -> TckeditVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def tckedit_various_file_cargs(
    params: TckeditVariousFileParameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def tckedit_include_params(
    spec: typing.Union[TckeditVariousStringParameters, TckeditVariousFileParameters],
) -> TckeditIncludeParameters:
    """
    Build parameters.
    
    Args:
        spec: specify an inclusion region of interest, as either a binary mask\
            image, or as a sphere using 4 comma-separared values (x,y,z,radius).\
            Streamlines must traverse ALL inclusion regions to be accepted.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "include",
        "spec": spec,
    }
    return params


def tckedit_include_cargs(
    params: TckeditIncludeParameters,
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
    cargs.append("-include")
    cargs.extend(dyn_cargs(params.get("spec")["__STYXTYPE__"])(params.get("spec"), execution))
    return cargs


def tckedit_include_ordered_params(
    image: str,
) -> TckeditIncludeOrderedParameters:
    """
    Build parameters.
    
    Args:
        image: specify an inclusion region of interest, as either a binary mask\
            image, or as a sphere using 4 comma-separared values (x,y,z,radius).\
            Streamlines must traverse ALL inclusion_ordered regions in the order\
            they are specified in order to be accepted.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "include_ordered",
        "image": image,
    }
    return params


def tckedit_include_ordered_cargs(
    params: TckeditIncludeOrderedParameters,
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
    cargs.append("-include_ordered")
    cargs.append(params.get("image"))
    return cargs


def tckedit_various_string_params_(
    obj: str,
) -> TckeditVariousStringParameters_:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def tckedit_various_string_cargs_(
    params: TckeditVariousStringParameters_,
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
    cargs.append(params.get("obj"))
    return cargs


def tckedit_various_file_params_(
    obj: InputPathType,
) -> TckeditVariousFileParameters_:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def tckedit_various_file_cargs_(
    params: TckeditVariousFileParameters_,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def tckedit_exclude_params(
    spec: typing.Union[TckeditVariousStringParameters_, TckeditVariousFileParameters_],
) -> TckeditExcludeParameters:
    """
    Build parameters.
    
    Args:
        spec: specify an exclusion region of interest, as either a binary mask\
            image, or as a sphere using 4 comma-separared values (x,y,z,radius).\
            Streamlines that enter ANY exclude region will be discarded.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "exclude",
        "spec": spec,
    }
    return params


def tckedit_exclude_cargs(
    params: TckeditExcludeParameters,
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
    cargs.append("-exclude")
    cargs.extend(dyn_cargs(params.get("spec")["__STYXTYPE__"])(params.get("spec"), execution))
    return cargs


def tckedit_various_string_params_2(
    obj: str,
) -> TckeditVariousStringParameters_2:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def tckedit_various_string_cargs_2(
    params: TckeditVariousStringParameters_2,
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
    cargs.append(params.get("obj"))
    return cargs


def tckedit_various_file_params_2(
    obj: InputPathType,
) -> TckeditVariousFileParameters_2:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def tckedit_various_file_cargs_2(
    params: TckeditVariousFileParameters_2,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def tckedit_mask_params(
    spec: typing.Union[TckeditVariousStringParameters_2, TckeditVariousFileParameters_2],
) -> TckeditMaskParameters:
    """
    Build parameters.
    
    Args:
        spec: specify a masking region of interest, as either a binary mask\
            image, or as a sphere using 4 comma-separared values (x,y,z,radius). If\
            defined, streamlines exiting the mask will be truncated.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mask",
        "spec": spec,
    }
    return params


def tckedit_mask_cargs(
    params: TckeditMaskParameters,
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
    cargs.append("-mask")
    cargs.extend(dyn_cargs(params.get("spec")["__STYXTYPE__"])(params.get("spec"), execution))
    return cargs


def tckedit_config_params(
    key: str,
    value: str,
) -> TckeditConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def tckedit_config_cargs(
    params: TckeditConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class TckeditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tracks_out: OutputPathType
    """the output track file"""
    tck_weights_out: OutputPathType | None
    """specify the path for an output text scalar file containing streamline
    weights """


def tckedit_params(
    tracks_in: list[InputPathType],
    tracks_out: str,
    include: list[TckeditIncludeParameters] | None = None,
    include_ordered: list[TckeditIncludeOrderedParameters] | None = None,
    exclude: list[TckeditExcludeParameters] | None = None,
    mask: list[TckeditMaskParameters] | None = None,
    maxlength: float | None = None,
    minlength: float | None = None,
    number: int | None = None,
    skip: int | None = None,
    maxweight: float | None = None,
    minweight: float | None = None,
    inverse: bool = False,
    ends_only: bool = False,
    tck_weights_in: InputPathType | None = None,
    tck_weights_out: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckeditConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TckeditParameters:
    """
    Build parameters.
    
    Args:
        tracks_in: the input track file(s).
        tracks_out: the output track file.
        include: specify an inclusion region of interest, as either a binary\
            mask image, or as a sphere using 4 comma-separared values\
            (x,y,z,radius). Streamlines must traverse ALL inclusion regions to be\
            accepted.
        include_ordered: specify an inclusion region of interest, as either a\
            binary mask image, or as a sphere using 4 comma-separared values\
            (x,y,z,radius). Streamlines must traverse ALL inclusion_ordered regions\
            in the order they are specified in order to be accepted.
        exclude: specify an exclusion region of interest, as either a binary\
            mask image, or as a sphere using 4 comma-separared values\
            (x,y,z,radius). Streamlines that enter ANY exclude region will be\
            discarded.
        mask: specify a masking region of interest, as either a binary mask\
            image, or as a sphere using 4 comma-separared values (x,y,z,radius). If\
            defined, streamlines exiting the mask will be truncated.
        maxlength: set the maximum length of any streamline in mm.
        minlength: set the minimum length of any streamline in mm.
        number: set the desired number of selected streamlines to be propagated\
            to the output file.
        skip: omit this number of selected streamlines before commencing\
            writing to the output file.
        maxweight: set the maximum weight of any streamline.
        minweight: set the minimum weight of any streamline.
        inverse: output the inverse selection of streamlines based on the\
            criteria provided; i.e. only those streamlines that fail at least one\
            selection criterion, and/or vertices that are outside masks if\
            provided, will be written to file.
        ends_only: only test the ends of each streamline against the provided\
            include/exclude ROIs.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
        tck_weights_out: specify the path for an output text scalar file\
            containing streamline weights.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tckedit",
        "inverse": inverse,
        "ends_only": ends_only,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "tracks_in": tracks_in,
        "tracks_out": tracks_out,
    }
    if include is not None:
        params["include"] = include
    if include_ordered is not None:
        params["include_ordered"] = include_ordered
    if exclude is not None:
        params["exclude"] = exclude
    if mask is not None:
        params["mask"] = mask
    if maxlength is not None:
        params["maxlength"] = maxlength
    if minlength is not None:
        params["minlength"] = minlength
    if number is not None:
        params["number"] = number
    if skip is not None:
        params["skip"] = skip
    if maxweight is not None:
        params["maxweight"] = maxweight
    if minweight is not None:
        params["minweight"] = minweight
    if tck_weights_in is not None:
        params["tck_weights_in"] = tck_weights_in
    if tck_weights_out is not None:
        params["tck_weights_out"] = tck_weights_out
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tckedit_cargs(
    params: TckeditParameters,
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
    cargs.append("tckedit")
    if params.get("include") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("include")] for a in c])
    if params.get("include_ordered") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("include_ordered")] for a in c])
    if params.get("exclude") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("exclude")] for a in c])
    if params.get("mask") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("mask")] for a in c])
    if params.get("maxlength") is not None:
        cargs.extend([
            "-maxlength",
            str(params.get("maxlength"))
        ])
    if params.get("minlength") is not None:
        cargs.extend([
            "-minlength",
            str(params.get("minlength"))
        ])
    if params.get("number") is not None:
        cargs.extend([
            "-number",
            str(params.get("number"))
        ])
    if params.get("skip") is not None:
        cargs.extend([
            "-skip",
            str(params.get("skip"))
        ])
    if params.get("maxweight") is not None:
        cargs.extend([
            "-maxweight",
            str(params.get("maxweight"))
        ])
    if params.get("minweight") is not None:
        cargs.extend([
            "-minweight",
            str(params.get("minweight"))
        ])
    if params.get("inverse"):
        cargs.append("-inverse")
    if params.get("ends_only"):
        cargs.append("-ends_only")
    if params.get("tck_weights_in") is not None:
        cargs.extend([
            "-tck_weights_in",
            execution.input_file(params.get("tck_weights_in"))
        ])
    if params.get("tck_weights_out") is not None:
        cargs.extend([
            "-tck_weights_out",
            params.get("tck_weights_out")
        ])
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.extend([execution.input_file(f) for f in params.get("tracks_in")])
    cargs.append(params.get("tracks_out"))
    return cargs


def tckedit_outputs(
    params: TckeditParameters,
    execution: Execution,
) -> TckeditOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TckeditOutputs(
        root=execution.output_file("."),
        tracks_out=execution.output_file(params.get("tracks_out")),
        tck_weights_out=execution.output_file(params.get("tck_weights_out")) if (params.get("tck_weights_out") is not None) else None,
    )
    return ret


def tckedit_execute(
    params: TckeditParameters,
    execution: Execution,
) -> TckeditOutputs:
    """
    Perform various editing operations on track files.
    
    This command can be used to perform various types of manipulations on track
    data. A range of such manipulations are demonstrated in the examples
    provided below.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TckeditOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tckedit_cargs(params, execution)
    ret = tckedit_outputs(params, execution)
    execution.run(cargs)
    return ret


def tckedit(
    tracks_in: list[InputPathType],
    tracks_out: str,
    include: list[TckeditIncludeParameters] | None = None,
    include_ordered: list[TckeditIncludeOrderedParameters] | None = None,
    exclude: list[TckeditExcludeParameters] | None = None,
    mask: list[TckeditMaskParameters] | None = None,
    maxlength: float | None = None,
    minlength: float | None = None,
    number: int | None = None,
    skip: int | None = None,
    maxweight: float | None = None,
    minweight: float | None = None,
    inverse: bool = False,
    ends_only: bool = False,
    tck_weights_in: InputPathType | None = None,
    tck_weights_out: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckeditConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckeditOutputs:
    """
    Perform various editing operations on track files.
    
    This command can be used to perform various types of manipulations on track
    data. A range of such manipulations are demonstrated in the examples
    provided below.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks_in: the input track file(s).
        tracks_out: the output track file.
        include: specify an inclusion region of interest, as either a binary\
            mask image, or as a sphere using 4 comma-separared values\
            (x,y,z,radius). Streamlines must traverse ALL inclusion regions to be\
            accepted.
        include_ordered: specify an inclusion region of interest, as either a\
            binary mask image, or as a sphere using 4 comma-separared values\
            (x,y,z,radius). Streamlines must traverse ALL inclusion_ordered regions\
            in the order they are specified in order to be accepted.
        exclude: specify an exclusion region of interest, as either a binary\
            mask image, or as a sphere using 4 comma-separared values\
            (x,y,z,radius). Streamlines that enter ANY exclude region will be\
            discarded.
        mask: specify a masking region of interest, as either a binary mask\
            image, or as a sphere using 4 comma-separared values (x,y,z,radius). If\
            defined, streamlines exiting the mask will be truncated.
        maxlength: set the maximum length of any streamline in mm.
        minlength: set the minimum length of any streamline in mm.
        number: set the desired number of selected streamlines to be propagated\
            to the output file.
        skip: omit this number of selected streamlines before commencing\
            writing to the output file.
        maxweight: set the maximum weight of any streamline.
        minweight: set the minimum weight of any streamline.
        inverse: output the inverse selection of streamlines based on the\
            criteria provided; i.e. only those streamlines that fail at least one\
            selection criterion, and/or vertices that are outside masks if\
            provided, will be written to file.
        ends_only: only test the ends of each streamline against the provided\
            include/exclude ROIs.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
        tck_weights_out: specify the path for an output text scalar file\
            containing streamline weights.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TckeditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKEDIT_METADATA)
    params = tckedit_params(include=include, include_ordered=include_ordered, exclude=exclude, mask=mask, maxlength=maxlength, minlength=minlength, number=number, skip=skip, maxweight=maxweight, minweight=minweight, inverse=inverse, ends_only=ends_only, tck_weights_in=tck_weights_in, tck_weights_out=tck_weights_out, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, tracks_in=tracks_in, tracks_out=tracks_out)
    return tckedit_execute(params, execution)


__all__ = [
    "TCKEDIT_METADATA",
    "TckeditConfigParameters",
    "TckeditExcludeParameters",
    "TckeditIncludeOrderedParameters",
    "TckeditIncludeParameters",
    "TckeditMaskParameters",
    "TckeditOutputs",
    "TckeditParameters",
    "TckeditVariousFileParameters",
    "TckeditVariousFileParameters_",
    "TckeditVariousFileParameters_2",
    "TckeditVariousStringParameters",
    "TckeditVariousStringParameters_",
    "TckeditVariousStringParameters_2",
    "tckedit",
    "tckedit_config_params",
    "tckedit_exclude_params",
    "tckedit_include_ordered_params",
    "tckedit_include_params",
    "tckedit_mask_params",
    "tckedit_params",
    "tckedit_various_file_params",
    "tckedit_various_file_params_",
    "tckedit_various_file_params_2",
    "tckedit_various_string_params",
    "tckedit_various_string_params_",
    "tckedit_various_string_params_2",
]
