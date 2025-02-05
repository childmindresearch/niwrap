# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_SMOOTH_METADATA = Metadata(
    id="d12bfab32f106014ff3d8c52a7b720c737313260.boutiques",
    name="SurfSmooth",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfSmoothParameters = typing.TypedDict('SurfSmoothParameters', {
    "__STYX_TYPE__": typing.Literal["SurfSmooth"],
    "surface": str,
    "method": str,
    "input_data": typing.NotRequired[InputPathType | None],
    "target_fwhm": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
    "number_iterations": typing.NotRequired[float | None],
    "output_file": typing.NotRequired[str | None],
    "band_pass_frequency": typing.NotRequired[float | None],
    "lambda_mu": typing.NotRequired[str | None],
    "interp_weights": typing.NotRequired[str | None],
    "node_mask": typing.NotRequired[InputPathType | None],
    "surface_output": typing.NotRequired[InputPathType | None],
    "dbg_node": typing.NotRequired[float | None],
    "use_neighbors_outside_mask": bool,
    "talk_suma": bool,
    "refresh_rate": typing.NotRequired[float | None],
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
        "SurfSmooth": surf_smooth_cargs,
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
        "SurfSmooth": surf_smooth_outputs,
    }
    return vt.get(t)


class SurfSmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_smooth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Name of the output file."""


def surf_smooth_params(
    surface: str,
    method: str,
    input_data: InputPathType | None = None,
    target_fwhm: float | None = None,
    fwhm: float | None = None,
    number_iterations: float | None = None,
    output_file: str | None = None,
    band_pass_frequency: float | None = None,
    lambda_mu: str | None = None,
    interp_weights: str | None = None,
    node_mask: InputPathType | None = None,
    surface_output: InputPathType | None = None,
    dbg_node: float | None = None,
    use_neighbors_outside_mask: bool = False,
    talk_suma: bool = False,
    refresh_rate: float | None = None,
) -> SurfSmoothParameters:
    """
    Build parameters.
    
    Args:
        surface: Option for specifying the surface to smooth or the domain over\
            which DSET is defined.
        method: Name of smoothing method to use. Choose from: HEAT_07, HEAT_05,\
            LM, NN_geom.
        input_data: File containing data (in 1D or NIML format). Required for\
            HEAT_05 and HEAT_07 methods.
        target_fwhm: Blur so that the final FWHM of the data is TF mm. Only for\
            HEAT_07 method.
        fwhm: Effective Full Width at Half Maximum for smoothing. Required for\
            HEAT_05 and optional for HEAT_07 methods.
        number_iterations: Number of smoothing iterations (default is 100 for\
            LM and NN_geom, -1 for HEAT methods).
        output_file: Name of output file. Default based on method being used.
        band_pass_frequency: Bandpass frequency for LM method (0 < k < 10).
        lambda_mu: Lambda and Mu parameters for LM method. Sample values are:\
            0.6307 and -0.6732.
        interp_weights: Set interpolation weights for LM method. Options:\
            Equal, Fujiwara, Desbrun.
        node_mask: Apply operations only to nodes listed in the given mask.
        surface_output: Writes the surface with smoothed coordinates to disk.\
            For LM and NN_geom methods.
        dbg_node: Output debug information for node 'node'.
        use_neighbors_outside_mask: Allow value from a node neighboring node n\
            to contribute to the value at n even if the neighbor is not in the\
            mask.
        talk_suma: Send progress with each iteration to SUMA for real-time\
            visualization.
        refresh_rate: Maximum number of updates to SUMA per second.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfSmooth",
        "surface": surface,
        "method": method,
        "use_neighbors_outside_mask": use_neighbors_outside_mask,
        "talk_suma": talk_suma,
    }
    if input_data is not None:
        params["input_data"] = input_data
    if target_fwhm is not None:
        params["target_fwhm"] = target_fwhm
    if fwhm is not None:
        params["fwhm"] = fwhm
    if number_iterations is not None:
        params["number_iterations"] = number_iterations
    if output_file is not None:
        params["output_file"] = output_file
    if band_pass_frequency is not None:
        params["band_pass_frequency"] = band_pass_frequency
    if lambda_mu is not None:
        params["lambda_mu"] = lambda_mu
    if interp_weights is not None:
        params["interp_weights"] = interp_weights
    if node_mask is not None:
        params["node_mask"] = node_mask
    if surface_output is not None:
        params["surface_output"] = surface_output
    if dbg_node is not None:
        params["dbg_node"] = dbg_node
    if refresh_rate is not None:
        params["refresh_rate"] = refresh_rate
    return params


def surf_smooth_cargs(
    params: SurfSmoothParameters,
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
    cargs.append("SurfSmooth")
    cargs.extend([
        "-SURF_1",
        params.get("surface")
    ])
    cargs.extend([
        "-met",
        params.get("method")
    ])
    if params.get("input_data") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("input_data"))
        ])
    if params.get("target_fwhm") is not None:
        cargs.extend([
            "-target_fwhm",
            str(params.get("target_fwhm"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "-fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("number_iterations") is not None:
        cargs.extend([
            "-Niter",
            str(params.get("number_iterations"))
        ])
    if params.get("output_file") is not None:
        cargs.extend([
            "-output",
            params.get("output_file")
        ])
    if params.get("band_pass_frequency") is not None:
        cargs.extend([
            "-kpb",
            str(params.get("band_pass_frequency"))
        ])
    if params.get("lambda_mu") is not None:
        cargs.extend([
            "-lm",
            params.get("lambda_mu")
        ])
    if params.get("interp_weights") is not None:
        cargs.extend([
            "-iw",
            params.get("interp_weights")
        ])
    if params.get("node_mask") is not None:
        cargs.extend([
            "-MASK",
            execution.input_file(params.get("node_mask"))
        ])
    if params.get("surface_output") is not None:
        cargs.extend([
            "-surf_out",
            execution.input_file(params.get("surface_output"))
        ])
    if params.get("dbg_node") is not None:
        cargs.extend([
            "-dbg_n",
            str(params.get("dbg_node"))
        ])
    if params.get("use_neighbors_outside_mask"):
        cargs.append("-use_neighbors_outside_mask")
    if params.get("talk_suma"):
        cargs.append("-talk_suma")
    if params.get("refresh_rate") is not None:
        cargs.extend([
            "-refresh_rate",
            str(params.get("refresh_rate"))
        ])
    return cargs


def surf_smooth_outputs(
    params: SurfSmoothParameters,
    execution: Execution,
) -> SurfSmoothOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfSmoothOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def surf_smooth_execute(
    params: SurfSmoothParameters,
    execution: Execution,
) -> SurfSmoothOutputs:
    """
    Tool for smoothing data on surfaces using various methods.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfSmoothOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surf_smooth_cargs(params, execution)
    ret = surf_smooth_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_smooth(
    surface: str,
    method: str,
    input_data: InputPathType | None = None,
    target_fwhm: float | None = None,
    fwhm: float | None = None,
    number_iterations: float | None = None,
    output_file: str | None = None,
    band_pass_frequency: float | None = None,
    lambda_mu: str | None = None,
    interp_weights: str | None = None,
    node_mask: InputPathType | None = None,
    surface_output: InputPathType | None = None,
    dbg_node: float | None = None,
    use_neighbors_outside_mask: bool = False,
    talk_suma: bool = False,
    refresh_rate: float | None = None,
    runner: Runner | None = None,
) -> SurfSmoothOutputs:
    """
    Tool for smoothing data on surfaces using various methods.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        surface: Option for specifying the surface to smooth or the domain over\
            which DSET is defined.
        method: Name of smoothing method to use. Choose from: HEAT_07, HEAT_05,\
            LM, NN_geom.
        input_data: File containing data (in 1D or NIML format). Required for\
            HEAT_05 and HEAT_07 methods.
        target_fwhm: Blur so that the final FWHM of the data is TF mm. Only for\
            HEAT_07 method.
        fwhm: Effective Full Width at Half Maximum for smoothing. Required for\
            HEAT_05 and optional for HEAT_07 methods.
        number_iterations: Number of smoothing iterations (default is 100 for\
            LM and NN_geom, -1 for HEAT methods).
        output_file: Name of output file. Default based on method being used.
        band_pass_frequency: Bandpass frequency for LM method (0 < k < 10).
        lambda_mu: Lambda and Mu parameters for LM method. Sample values are:\
            0.6307 and -0.6732.
        interp_weights: Set interpolation weights for LM method. Options:\
            Equal, Fujiwara, Desbrun.
        node_mask: Apply operations only to nodes listed in the given mask.
        surface_output: Writes the surface with smoothed coordinates to disk.\
            For LM and NN_geom methods.
        dbg_node: Output debug information for node 'node'.
        use_neighbors_outside_mask: Allow value from a node neighboring node n\
            to contribute to the value at n even if the neighbor is not in the\
            mask.
        talk_suma: Send progress with each iteration to SUMA for real-time\
            visualization.
        refresh_rate: Maximum number of updates to SUMA per second.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfSmoothOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_SMOOTH_METADATA)
    params = surf_smooth_params(surface=surface, method=method, input_data=input_data, target_fwhm=target_fwhm, fwhm=fwhm, number_iterations=number_iterations, output_file=output_file, band_pass_frequency=band_pass_frequency, lambda_mu=lambda_mu, interp_weights=interp_weights, node_mask=node_mask, surface_output=surface_output, dbg_node=dbg_node, use_neighbors_outside_mask=use_neighbors_outside_mask, talk_suma=talk_suma, refresh_rate=refresh_rate)
    return surf_smooth_execute(params, execution)


__all__ = [
    "SURF_SMOOTH_METADATA",
    "SurfSmoothOutputs",
    "SurfSmoothParameters",
    "surf_smooth",
    "surf_smooth_params",
]
