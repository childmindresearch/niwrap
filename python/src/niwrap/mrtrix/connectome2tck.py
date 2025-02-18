# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONNECTOME2TCK_METADATA = Metadata(
    id="68591f4f9a13309e07f97bb4a65436101f61042f.boutiques",
    name="connectome2tck",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Connectome2tckConfigParameters = typing.TypedDict('Connectome2tckConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Connectome2tckParameters = typing.TypedDict('Connectome2tckParameters', {
    "__STYX_TYPE__": typing.Literal["connectome2tck"],
    "nodes": typing.NotRequired[list[int] | None],
    "exclusive": bool,
    "files": typing.NotRequired[str | None],
    "exemplars": typing.NotRequired[InputPathType | None],
    "keep_unassigned": bool,
    "keep_self": bool,
    "tck_weights_in": typing.NotRequired[InputPathType | None],
    "prefix_tck_weights_out": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Connectome2tckConfigParameters] | None],
    "help": bool,
    "version": bool,
    "tracks_in": InputPathType,
    "assignments_in": InputPathType,
    "prefix_out": str,
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
        "connectome2tck": connectome2tck_cargs,
        "config": connectome2tck_config_cargs,
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


def connectome2tck_config_params(
    key: str,
    value: str,
) -> Connectome2tckConfigParameters:
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


def connectome2tck_config_cargs(
    params: Connectome2tckConfigParameters,
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


class Connectome2tckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `connectome2tck(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def connectome2tck_params(
    tracks_in: InputPathType,
    assignments_in: InputPathType,
    prefix_out: str,
    nodes: list[int] | None = None,
    exclusive: bool = False,
    files: str | None = None,
    exemplars: InputPathType | None = None,
    keep_unassigned: bool = False,
    keep_self: bool = False,
    tck_weights_in: InputPathType | None = None,
    prefix_tck_weights_out: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Connectome2tckConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Connectome2tckParameters:
    """
    Build parameters.
    
    Args:
        tracks_in: the input track file.
        assignments_in: input text file containing the node assignments for\
            each streamline.
        prefix_out: the output file / prefix.
        nodes: only select tracks that involve a set of nodes of interest\
            (provide as a comma-separated list of integers).
        exclusive: only select tracks that exclusively connect nodes from\
            within the list of nodes of interest.
        files: select how the resulting streamlines will be grouped in output\
            files. Options are: per_edge, per_node, single (default: per_edge).
        exemplars: generate a mean connection exemplar per edge, rather than\
            keeping all streamlines (the parcellation node image must be provided\
            in order to constrain the exemplar endpoints).
        keep_unassigned: by default, the program discards those streamlines\
            that are not successfully assigned to a node. Set this option to\
            generate corresponding outputs containing these streamlines (labelled\
            as node index 0).
        keep_self: by default, the program will not output streamlines that\
            connect to the same node at both ends. Set this option to instead keep\
            these self-connections.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
        prefix_tck_weights_out: provide a prefix for outputting a text file\
            corresponding to each output file, each containing only the streamline\
            weights relevant for that track file.
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
        "__STYXTYPE__": "connectome2tck",
        "exclusive": exclusive,
        "keep_unassigned": keep_unassigned,
        "keep_self": keep_self,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "tracks_in": tracks_in,
        "assignments_in": assignments_in,
        "prefix_out": prefix_out,
    }
    if nodes is not None:
        params["nodes"] = nodes
    if files is not None:
        params["files"] = files
    if exemplars is not None:
        params["exemplars"] = exemplars
    if tck_weights_in is not None:
        params["tck_weights_in"] = tck_weights_in
    if prefix_tck_weights_out is not None:
        params["prefix_tck_weights_out"] = prefix_tck_weights_out
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def connectome2tck_cargs(
    params: Connectome2tckParameters,
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
    cargs.append("connectome2tck")
    if params.get("nodes") is not None:
        cargs.extend([
            "-nodes",
            ",".join(map(str, params.get("nodes")))
        ])
    if params.get("exclusive"):
        cargs.append("-exclusive")
    if params.get("files") is not None:
        cargs.extend([
            "-files",
            params.get("files")
        ])
    if params.get("exemplars") is not None:
        cargs.extend([
            "-exemplars",
            execution.input_file(params.get("exemplars"))
        ])
    if params.get("keep_unassigned"):
        cargs.append("-keep_unassigned")
    if params.get("keep_self"):
        cargs.append("-keep_self")
    if params.get("tck_weights_in") is not None:
        cargs.extend([
            "-tck_weights_in",
            execution.input_file(params.get("tck_weights_in"))
        ])
    if params.get("prefix_tck_weights_out") is not None:
        cargs.extend([
            "-prefix_tck_weights_out",
            params.get("prefix_tck_weights_out")
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
    cargs.append(execution.input_file(params.get("tracks_in")))
    cargs.append(execution.input_file(params.get("assignments_in")))
    cargs.append(params.get("prefix_out"))
    return cargs


def connectome2tck_outputs(
    params: Connectome2tckParameters,
    execution: Execution,
) -> Connectome2tckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Connectome2tckOutputs(
        root=execution.output_file("."),
    )
    return ret


def connectome2tck_execute(
    params: Connectome2tckParameters,
    execution: Execution,
) -> Connectome2tckOutputs:
    """
    Extract streamlines from a tractogram based on their assignment to parcellated
    nodes.
    
    The compulsory input file "assignments_in" should contain a text file where
    there is one row for each streamline, and each row contains a list of
    numbers corresponding to the parcels to which that streamline was assigned
    (most typically there will be two entries per streamline, one for each
    endpoint; but this is not strictly a requirement). This file will most
    typically be generated using the tck2connectome command with the
    -out_assignments option.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Connectome2tckOutputs`).
    """
    params = execution.params(params)
    cargs = connectome2tck_cargs(params, execution)
    ret = connectome2tck_outputs(params, execution)
    execution.run(cargs)
    return ret


def connectome2tck(
    tracks_in: InputPathType,
    assignments_in: InputPathType,
    prefix_out: str,
    nodes: list[int] | None = None,
    exclusive: bool = False,
    files: str | None = None,
    exemplars: InputPathType | None = None,
    keep_unassigned: bool = False,
    keep_self: bool = False,
    tck_weights_in: InputPathType | None = None,
    prefix_tck_weights_out: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Connectome2tckConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Connectome2tckOutputs:
    """
    Extract streamlines from a tractogram based on their assignment to parcellated
    nodes.
    
    The compulsory input file "assignments_in" should contain a text file where
    there is one row for each streamline, and each row contains a list of
    numbers corresponding to the parcels to which that streamline was assigned
    (most typically there will be two entries per streamline, one for each
    endpoint; but this is not strictly a requirement). This file will most
    typically be generated using the tck2connectome command with the
    -out_assignments option.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks_in: the input track file.
        assignments_in: input text file containing the node assignments for\
            each streamline.
        prefix_out: the output file / prefix.
        nodes: only select tracks that involve a set of nodes of interest\
            (provide as a comma-separated list of integers).
        exclusive: only select tracks that exclusively connect nodes from\
            within the list of nodes of interest.
        files: select how the resulting streamlines will be grouped in output\
            files. Options are: per_edge, per_node, single (default: per_edge).
        exemplars: generate a mean connection exemplar per edge, rather than\
            keeping all streamlines (the parcellation node image must be provided\
            in order to constrain the exemplar endpoints).
        keep_unassigned: by default, the program discards those streamlines\
            that are not successfully assigned to a node. Set this option to\
            generate corresponding outputs containing these streamlines (labelled\
            as node index 0).
        keep_self: by default, the program will not output streamlines that\
            connect to the same node at both ends. Set this option to instead keep\
            these self-connections.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
        prefix_tck_weights_out: provide a prefix for outputting a text file\
            corresponding to each output file, each containing only the streamline\
            weights relevant for that track file.
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
        NamedTuple of outputs (described in `Connectome2tckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONNECTOME2TCK_METADATA)
    params = connectome2tck_params(nodes=nodes, exclusive=exclusive, files=files, exemplars=exemplars, keep_unassigned=keep_unassigned, keep_self=keep_self, tck_weights_in=tck_weights_in, prefix_tck_weights_out=prefix_tck_weights_out, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, tracks_in=tracks_in, assignments_in=assignments_in, prefix_out=prefix_out)
    return connectome2tck_execute(params, execution)


__all__ = [
    "CONNECTOME2TCK_METADATA",
    "Connectome2tckConfigParameters",
    "Connectome2tckOutputs",
    "Connectome2tckParameters",
    "connectome2tck",
    "connectome2tck_config_params",
    "connectome2tck_params",
]
