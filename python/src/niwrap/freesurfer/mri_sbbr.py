# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SBBR_METADATA = Metadata(
    id="f4b950626104a4845f82588892a8047d0782b10a.boutiques",
    name="mri_sbbr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSbbrParameters = typing.TypedDict('MriSbbrParameters', {
    "__STYX_TYPE__": typing.Literal["mri_sbbr"],
    "template_volume": InputPathType,
    "surface_file": InputPathType,
    "init_reg_file": InputPathType,
    "t1": bool,
    "t2": bool,
    "optimization_type": typing.NotRequired[float | None],
    "distance_in": typing.NotRequired[float | None],
    "distance_out": typing.NotRequired[float | None],
    "slope": typing.NotRequired[float | None],
    "ftol": typing.NotRequired[float | None],
    "linmintol": typing.NotRequired[float | None],
    "niters_max": typing.NotRequired[float | None],
    "search": typing.NotRequired[str | None],
    "search1d": typing.NotRequired[str | None],
    "parameter_set": typing.NotRequired[str | None],
    "increment": typing.NotRequired[float | None],
    "slice_number": typing.NotRequired[float | None],
    "threads": typing.NotRequired[float | None],
    "output_registration": typing.NotRequired[str | None],
    "inverted_output_registration": typing.NotRequired[str | None],
    "output_surface": typing.NotRequired[str | None],
    "debug": bool,
    "diagnostic": bool,
    "check_options": bool,
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
        "mri_sbbr": mri_sbbr_cargs,
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
        "mri_sbbr": mri_sbbr_outputs,
    }.get(t)


class MriSbbrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_sbbr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_sbbr_params(
    template_volume: InputPathType,
    surface_file: InputPathType,
    init_reg_file: InputPathType,
    t1: bool = False,
    t2: bool = False,
    optimization_type: float | None = None,
    distance_in: float | None = None,
    distance_out: float | None = None,
    slope: float | None = None,
    ftol: float | None = None,
    linmintol: float | None = None,
    niters_max: float | None = None,
    search: str | None = None,
    search1d: str | None = None,
    parameter_set: str | None = None,
    increment: float | None = None,
    slice_number: float | None = None,
    threads: float | None = None,
    output_registration: str | None = None,
    inverted_output_registration: str | None = None,
    output_surface: str | None = None,
    debug: bool = False,
    diagnostic: bool = False,
    check_options: bool = False,
) -> MriSbbrParameters:
    """
    Build parameters.
    
    Args:
        template_volume: Template volume file.
        surface_file: Surface file.
        init_reg_file: Initial registration file.
        t1: Use T1-weighted image.
        t2: Use T2-weighted image.
        optimization_type: Optimization type; choose 1, 2, or 3 (default is 1,\
            6 dof).
        distance_in: Distance in mm into surface (default 1.0).
        distance_out: Distance in mm out of surface (default 2.0).
        slope: BBR slope (default 0.5).
        ftol: Tolerance for fitting (default 1.000000e-08).
        linmintol: Linear minimization tolerance (default 0.0).
        niters_max: Maximum number of iterations (default 10).
        search: Brute force search through parameter space.
        search1d: 1D search through parameter space.
        parameter_set: Set initial parameter.
        increment: Face number increment (default 1).
        slice_number: Slice number (defaults to 0).
        threads: Number of threads.
        output_registration: Output registration file.
        inverted_output_registration: Inverted output registration file.
        output_surface: Output surface in slice coordinates.
        debug: Turn on debugging.
        diagnostic: Turn on diagnostics.
        check_options: Don't run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_sbbr",
        "template_volume": template_volume,
        "surface_file": surface_file,
        "init_reg_file": init_reg_file,
        "t1": t1,
        "t2": t2,
        "debug": debug,
        "diagnostic": diagnostic,
        "check_options": check_options,
    }
    if optimization_type is not None:
        params["optimization_type"] = optimization_type
    if distance_in is not None:
        params["distance_in"] = distance_in
    if distance_out is not None:
        params["distance_out"] = distance_out
    if slope is not None:
        params["slope"] = slope
    if ftol is not None:
        params["ftol"] = ftol
    if linmintol is not None:
        params["linmintol"] = linmintol
    if niters_max is not None:
        params["niters_max"] = niters_max
    if search is not None:
        params["search"] = search
    if search1d is not None:
        params["search1d"] = search1d
    if parameter_set is not None:
        params["parameter_set"] = parameter_set
    if increment is not None:
        params["increment"] = increment
    if slice_number is not None:
        params["slice_number"] = slice_number
    if threads is not None:
        params["threads"] = threads
    if output_registration is not None:
        params["output_registration"] = output_registration
    if inverted_output_registration is not None:
        params["inverted_output_registration"] = inverted_output_registration
    if output_surface is not None:
        params["output_surface"] = output_surface
    return params


def mri_sbbr_cargs(
    params: MriSbbrParameters,
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
    cargs.append("mri_sbbr")
    cargs.extend([
        "--mov",
        execution.input_file(params.get("template_volume"))
    ])
    cargs.extend([
        "--surf",
        execution.input_file(params.get("surface_file"))
    ])
    cargs.extend([
        "--init-reg",
        execution.input_file(params.get("init_reg_file"))
    ])
    if params.get("t1"):
        cargs.append("--t1")
    if params.get("t2"):
        cargs.append("--t2")
    if params.get("optimization_type") is not None:
        cargs.extend([
            "--opt",
            str(params.get("optimization_type"))
        ])
    if params.get("distance_in") is not None:
        cargs.extend([
            "--din",
            str(params.get("distance_in"))
        ])
    if params.get("distance_out") is not None:
        cargs.extend([
            "--dout",
            str(params.get("distance_out"))
        ])
    if params.get("slope") is not None:
        cargs.extend([
            "--slope",
            str(params.get("slope"))
        ])
    if params.get("ftol") is not None:
        cargs.extend([
            "--ftol",
            str(params.get("ftol"))
        ])
    if params.get("linmintol") is not None:
        cargs.extend([
            "--linmintol",
            str(params.get("linmintol"))
        ])
    if params.get("niters_max") is not None:
        cargs.extend([
            "--niters-max",
            str(params.get("niters_max"))
        ])
    if params.get("search") is not None:
        cargs.extend([
            "--search",
            params.get("search")
        ])
    if params.get("search1d") is not None:
        cargs.extend([
            "--search1d",
            params.get("search1d")
        ])
    if params.get("parameter_set") is not None:
        cargs.extend([
            "--p",
            params.get("parameter_set")
        ])
    if params.get("increment") is not None:
        cargs.extend([
            "--inc",
            str(params.get("increment"))
        ])
    if params.get("slice_number") is not None:
        cargs.extend([
            "--slice",
            str(params.get("slice_number"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("output_registration") is not None:
        cargs.extend([
            "--reg",
            params.get("output_registration")
        ])
    if params.get("inverted_output_registration") is not None:
        cargs.extend([
            "--reg-inv",
            params.get("inverted_output_registration")
        ])
    if params.get("output_surface") is not None:
        cargs.extend([
            "--out-surf",
            params.get("output_surface")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("diagnostic"):
        cargs.append("--diag")
    if params.get("check_options"):
        cargs.append("--checkopts")
    return cargs


def mri_sbbr_outputs(
    params: MriSbbrParameters,
    execution: Execution,
) -> MriSbbrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSbbrOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_sbbr_execute(
    params: MriSbbrParameters,
    execution: Execution,
) -> MriSbbrOutputs:
    """
    Special implementation of boundary-based registration for a single slice.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSbbrOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_sbbr_cargs(params, execution)
    ret = mri_sbbr_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_sbbr(
    template_volume: InputPathType,
    surface_file: InputPathType,
    init_reg_file: InputPathType,
    t1: bool = False,
    t2: bool = False,
    optimization_type: float | None = None,
    distance_in: float | None = None,
    distance_out: float | None = None,
    slope: float | None = None,
    ftol: float | None = None,
    linmintol: float | None = None,
    niters_max: float | None = None,
    search: str | None = None,
    search1d: str | None = None,
    parameter_set: str | None = None,
    increment: float | None = None,
    slice_number: float | None = None,
    threads: float | None = None,
    output_registration: str | None = None,
    inverted_output_registration: str | None = None,
    output_surface: str | None = None,
    debug: bool = False,
    diagnostic: bool = False,
    check_options: bool = False,
    runner: Runner | None = None,
) -> MriSbbrOutputs:
    """
    Special implementation of boundary-based registration for a single slice.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        template_volume: Template volume file.
        surface_file: Surface file.
        init_reg_file: Initial registration file.
        t1: Use T1-weighted image.
        t2: Use T2-weighted image.
        optimization_type: Optimization type; choose 1, 2, or 3 (default is 1,\
            6 dof).
        distance_in: Distance in mm into surface (default 1.0).
        distance_out: Distance in mm out of surface (default 2.0).
        slope: BBR slope (default 0.5).
        ftol: Tolerance for fitting (default 1.000000e-08).
        linmintol: Linear minimization tolerance (default 0.0).
        niters_max: Maximum number of iterations (default 10).
        search: Brute force search through parameter space.
        search1d: 1D search through parameter space.
        parameter_set: Set initial parameter.
        increment: Face number increment (default 1).
        slice_number: Slice number (defaults to 0).
        threads: Number of threads.
        output_registration: Output registration file.
        inverted_output_registration: Inverted output registration file.
        output_surface: Output surface in slice coordinates.
        debug: Turn on debugging.
        diagnostic: Turn on diagnostics.
        check_options: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSbbrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SBBR_METADATA)
    params = mri_sbbr_params(template_volume=template_volume, surface_file=surface_file, init_reg_file=init_reg_file, t1=t1, t2=t2, optimization_type=optimization_type, distance_in=distance_in, distance_out=distance_out, slope=slope, ftol=ftol, linmintol=linmintol, niters_max=niters_max, search=search, search1d=search1d, parameter_set=parameter_set, increment=increment, slice_number=slice_number, threads=threads, output_registration=output_registration, inverted_output_registration=inverted_output_registration, output_surface=output_surface, debug=debug, diagnostic=diagnostic, check_options=check_options)
    return mri_sbbr_execute(params, execution)


__all__ = [
    "MRI_SBBR_METADATA",
    "MriSbbrOutputs",
    "MriSbbrParameters",
    "mri_sbbr",
    "mri_sbbr_params",
]
