# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TCKSIFT2_METADATA = Metadata(
    id="399c2a04022ba3cedcda7e35cf69c1dae578656c.boutiques",
    name="tcksift2",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Tcksift2ConfigParameters = typing.TypedDict('Tcksift2ConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Tcksift2Parameters = typing.TypedDict('Tcksift2Parameters', {
    "__STYX_TYPE__": typing.Literal["tcksift2"],
    "proc_mask": typing.NotRequired[InputPathType | None],
    "act": typing.NotRequired[InputPathType | None],
    "fd_scale_gm": bool,
    "no_dilate_lut": bool,
    "make_null_lobes": bool,
    "remove_untracked": bool,
    "fd_thresh": typing.NotRequired[float | None],
    "csv": typing.NotRequired[str | None],
    "out_mu": typing.NotRequired[str | None],
    "output_debug": bool,
    "out_coeffs": typing.NotRequired[str | None],
    "reg_tikhonov": typing.NotRequired[float | None],
    "reg_tv": typing.NotRequired[float | None],
    "min_td_frac": typing.NotRequired[float | None],
    "min_iters": typing.NotRequired[int | None],
    "max_iters": typing.NotRequired[int | None],
    "min_factor": typing.NotRequired[float | None],
    "min_coeff": typing.NotRequired[float | None],
    "max_factor": typing.NotRequired[float | None],
    "max_coeff": typing.NotRequired[float | None],
    "max_coeff_step": typing.NotRequired[float | None],
    "min_cf_decrease": typing.NotRequired[float | None],
    "linear": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Tcksift2ConfigParameters] | None],
    "help": bool,
    "version": bool,
    "in_tracks": InputPathType,
    "in_fod": InputPathType,
    "out_weights": str,
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
        "tcksift2": tcksift2_cargs,
        "config": tcksift2_config_cargs,
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
        "tcksift2": tcksift2_outputs,
    }.get(t)


def tcksift2_config_params(
    key: str,
    value: str,
) -> Tcksift2ConfigParameters:
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


def tcksift2_config_cargs(
    params: Tcksift2ConfigParameters,
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


class Tcksift2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `tcksift2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_weights: OutputPathType
    """output text file containing the weighting factor for each streamline"""
    csv_: OutputPathType | None
    """output statistics of execution per iteration to a .csv file """
    out_mu: OutputPathType | None
    """output the final value of SIFT proportionality coefficient mu to a text
    file """
    out_coeffs: OutputPathType | None
    """output text file containing the weighting coefficient for each streamline
    """


def tcksift2_params(
    in_tracks: InputPathType,
    in_fod: InputPathType,
    out_weights: str,
    proc_mask: InputPathType | None = None,
    act: InputPathType | None = None,
    fd_scale_gm: bool = False,
    no_dilate_lut: bool = False,
    make_null_lobes: bool = False,
    remove_untracked: bool = False,
    fd_thresh: float | None = None,
    csv_: str | None = None,
    out_mu: str | None = None,
    output_debug: bool = False,
    out_coeffs: str | None = None,
    reg_tikhonov: float | None = None,
    reg_tv: float | None = None,
    min_td_frac: float | None = None,
    min_iters: int | None = None,
    max_iters: int | None = None,
    min_factor: float | None = None,
    min_coeff: float | None = None,
    max_factor: float | None = None,
    max_coeff: float | None = None,
    max_coeff_step: float | None = None,
    min_cf_decrease: float | None = None,
    linear: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tcksift2ConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Tcksift2Parameters:
    """
    Build parameters.
    
    Args:
        in_tracks: the input track file.
        in_fod: input image containing the spherical harmonics of the fibre\
            orientation distributions.
        out_weights: output text file containing the weighting factor for each\
            streamline.
        proc_mask: provide an image containing the processing mask weights for\
            the model; image spatial dimensions must match the fixel image.
        act: use an ACT five-tissue-type segmented anatomical image to derive\
            the processing mask.
        fd_scale_gm: provide this option (in conjunction with -act) to\
            heuristically downsize the fibre density estimates based on the\
            presence of GM in the voxel. This can assist in reducing tissue\
            interface effects when using a single-tissue deconvolution algorithm.
        no_dilate_lut: do NOT dilate FOD lobe lookup tables; only map\
            streamlines to FOD lobes if the precise tangent lies within the angular\
            spread of that lobe.
        make_null_lobes: add an additional FOD lobe to each voxel, with zero\
            integral, that covers all directions with zero / negative FOD\
            amplitudes.
        remove_untracked: remove FOD lobes that do not have any streamline\
            density attributed to them; this improves filtering slightly, at the\
            expense of longer computation time (and you can no longer do\
            quantitative comparisons between reconstructions if this is enabled).
        fd_thresh: fibre density threshold; exclude an FOD lobe from filtering\
            processing if its integral is less than this amount (streamlines will\
            still be mapped to it, but it will not contribute to the cost function\
            or the filtering).
        csv_: output statistics of execution per iteration to a .csv file.
        out_mu: output the final value of SIFT proportionality coefficient mu\
            to a text file.
        output_debug: provide various output images for assessing & debugging\
            performance etc.
        out_coeffs: output text file containing the weighting coefficient for\
            each streamline.
        reg_tikhonov: provide coefficient for regularising streamline weighting\
            coefficients (Tikhonov regularisation) (default: 0).
        reg_tv: provide coefficient for regularising variance of streamline\
            weighting coefficient to fixels along its length (Total Variation\
            regularisation) (default: 0.1).
        min_td_frac: minimum fraction of the FOD integral reconstructed by\
            streamlines; if the reconstructed streamline density is below this\
            fraction, the fixel is excluded from optimisation (default: 0.1).
        min_iters: minimum number of iterations to run before testing for\
            convergence; this can prevent premature termination at early iterations\
            if the cost function increases slightly (default: 10).
        max_iters: maximum number of iterations to run before terminating\
            program.
        min_factor: minimum weighting factor for an individual streamline; if\
            the factor falls below this number the streamline will be rejected\
            entirely (factor set to zero) (default: 0).
        min_coeff: minimum weighting coefficient for an individual streamline;\
            similar to the '-min_factor' option, but using the exponential\
            coefficient basis of the SIFT2 model; these parameters are related as:\
            factor = e^(coeff). Note that the -min_factor and -min_coeff options\
            are mutually exclusive - you can only provide one. (default: -inf).
        max_factor: maximum weighting factor that can be assigned to any one\
            streamline (default: inf).
        max_coeff: maximum weighting coefficient for an individual streamline;\
            similar to the '-max_factor' option, but using the exponential\
            coefficient basis of the SIFT2 model; these parameters are related as:\
            factor = e^(coeff). Note that the -max_factor and -max_coeff options\
            are mutually exclusive - you can only provide one. (default: inf).
        max_coeff_step: maximum change to a streamline's weighting coefficient\
            in a single iteration (default: 1).
        min_cf_decrease: minimum decrease in the cost function (as a fraction\
            of the initial value) that must occur each iteration for the algorithm\
            to continue (default: 2.5e-05).
        linear: perform a linear estimation of streamline weights, rather than\
            the standard non-linear optimisation (typically does not provide as\
            accurate a model fit; but only requires a single pass).
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
        "__STYXTYPE__": "tcksift2",
        "fd_scale_gm": fd_scale_gm,
        "no_dilate_lut": no_dilate_lut,
        "make_null_lobes": make_null_lobes,
        "remove_untracked": remove_untracked,
        "output_debug": output_debug,
        "linear": linear,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "in_tracks": in_tracks,
        "in_fod": in_fod,
        "out_weights": out_weights,
    }
    if proc_mask is not None:
        params["proc_mask"] = proc_mask
    if act is not None:
        params["act"] = act
    if fd_thresh is not None:
        params["fd_thresh"] = fd_thresh
    if csv_ is not None:
        params["csv"] = csv_
    if out_mu is not None:
        params["out_mu"] = out_mu
    if out_coeffs is not None:
        params["out_coeffs"] = out_coeffs
    if reg_tikhonov is not None:
        params["reg_tikhonov"] = reg_tikhonov
    if reg_tv is not None:
        params["reg_tv"] = reg_tv
    if min_td_frac is not None:
        params["min_td_frac"] = min_td_frac
    if min_iters is not None:
        params["min_iters"] = min_iters
    if max_iters is not None:
        params["max_iters"] = max_iters
    if min_factor is not None:
        params["min_factor"] = min_factor
    if min_coeff is not None:
        params["min_coeff"] = min_coeff
    if max_factor is not None:
        params["max_factor"] = max_factor
    if max_coeff is not None:
        params["max_coeff"] = max_coeff
    if max_coeff_step is not None:
        params["max_coeff_step"] = max_coeff_step
    if min_cf_decrease is not None:
        params["min_cf_decrease"] = min_cf_decrease
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tcksift2_cargs(
    params: Tcksift2Parameters,
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
    cargs.append("tcksift2")
    if params.get("proc_mask") is not None:
        cargs.extend([
            "-proc_mask",
            execution.input_file(params.get("proc_mask"))
        ])
    if params.get("act") is not None:
        cargs.extend([
            "-act",
            execution.input_file(params.get("act"))
        ])
    if params.get("fd_scale_gm"):
        cargs.append("-fd_scale_gm")
    if params.get("no_dilate_lut"):
        cargs.append("-no_dilate_lut")
    if params.get("make_null_lobes"):
        cargs.append("-make_null_lobes")
    if params.get("remove_untracked"):
        cargs.append("-remove_untracked")
    if params.get("fd_thresh") is not None:
        cargs.extend([
            "-fd_thresh",
            str(params.get("fd_thresh"))
        ])
    if params.get("csv") is not None:
        cargs.extend([
            "-csv",
            params.get("csv")
        ])
    if params.get("out_mu") is not None:
        cargs.extend([
            "-out_mu",
            params.get("out_mu")
        ])
    if params.get("output_debug"):
        cargs.append("-output_debug")
    if params.get("out_coeffs") is not None:
        cargs.extend([
            "-out_coeffs",
            params.get("out_coeffs")
        ])
    if params.get("reg_tikhonov") is not None:
        cargs.extend([
            "-reg_tikhonov",
            str(params.get("reg_tikhonov"))
        ])
    if params.get("reg_tv") is not None:
        cargs.extend([
            "-reg_tv",
            str(params.get("reg_tv"))
        ])
    if params.get("min_td_frac") is not None:
        cargs.extend([
            "-min_td_frac",
            str(params.get("min_td_frac"))
        ])
    if params.get("min_iters") is not None:
        cargs.extend([
            "-min_iters",
            str(params.get("min_iters"))
        ])
    if params.get("max_iters") is not None:
        cargs.extend([
            "-max_iters",
            str(params.get("max_iters"))
        ])
    if params.get("min_factor") is not None:
        cargs.extend([
            "-min_factor",
            str(params.get("min_factor"))
        ])
    if params.get("min_coeff") is not None:
        cargs.extend([
            "-min_coeff",
            str(params.get("min_coeff"))
        ])
    if params.get("max_factor") is not None:
        cargs.extend([
            "-max_factor",
            str(params.get("max_factor"))
        ])
    if params.get("max_coeff") is not None:
        cargs.extend([
            "-max_coeff",
            str(params.get("max_coeff"))
        ])
    if params.get("max_coeff_step") is not None:
        cargs.extend([
            "-max_coeff_step",
            str(params.get("max_coeff_step"))
        ])
    if params.get("min_cf_decrease") is not None:
        cargs.extend([
            "-min_cf_decrease",
            str(params.get("min_cf_decrease"))
        ])
    if params.get("linear"):
        cargs.append("-linear")
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
    cargs.append(execution.input_file(params.get("in_tracks")))
    cargs.append(execution.input_file(params.get("in_fod")))
    cargs.append(params.get("out_weights"))
    return cargs


def tcksift2_outputs(
    params: Tcksift2Parameters,
    execution: Execution,
) -> Tcksift2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Tcksift2Outputs(
        root=execution.output_file("."),
        out_weights=execution.output_file(params.get("out_weights")),
        csv_=execution.output_file(params.get("csv")) if (params.get("csv") is not None) else None,
        out_mu=execution.output_file(params.get("out_mu")) if (params.get("out_mu") is not None) else None,
        out_coeffs=execution.output_file(params.get("out_coeffs")) if (params.get("out_coeffs") is not None) else None,
    )
    return ret


def tcksift2_execute(
    params: Tcksift2Parameters,
    execution: Execution,
) -> Tcksift2Outputs:
    """
    Optimise per-streamline cross-section multipliers to match a whole-brain
    tractogram to fixel-wise fibre densities.
    
    
    
    References:
    
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT2: Enabling
    dense quantitative assessment of brain white matter connectivity using
    streamlines tractography. NeuroImage, 2015, 119, 338-351
    
    * If using the -linear option:
    Smith, RE; Raffelt, D; Tournier, J-D; Connelly, A. Quantitative Streamlines
    Tractography: Methods and Inter-Subject Normalisation. Open Science
    Framework, https://doi.org/10.31219/osf.io/c67kn.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Tcksift2Outputs`).
    """
    cargs = tcksift2_cargs(params, execution)
    ret = tcksift2_outputs(params, execution)
    execution.run(cargs)
    return ret


def tcksift2(
    in_tracks: InputPathType,
    in_fod: InputPathType,
    out_weights: str,
    proc_mask: InputPathType | None = None,
    act: InputPathType | None = None,
    fd_scale_gm: bool = False,
    no_dilate_lut: bool = False,
    make_null_lobes: bool = False,
    remove_untracked: bool = False,
    fd_thresh: float | None = None,
    csv_: str | None = None,
    out_mu: str | None = None,
    output_debug: bool = False,
    out_coeffs: str | None = None,
    reg_tikhonov: float | None = None,
    reg_tv: float | None = None,
    min_td_frac: float | None = None,
    min_iters: int | None = None,
    max_iters: int | None = None,
    min_factor: float | None = None,
    min_coeff: float | None = None,
    max_factor: float | None = None,
    max_coeff: float | None = None,
    max_coeff_step: float | None = None,
    min_cf_decrease: float | None = None,
    linear: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tcksift2ConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Tcksift2Outputs:
    """
    Optimise per-streamline cross-section multipliers to match a whole-brain
    tractogram to fixel-wise fibre densities.
    
    
    
    References:
    
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT2: Enabling
    dense quantitative assessment of brain white matter connectivity using
    streamlines tractography. NeuroImage, 2015, 119, 338-351
    
    * If using the -linear option:
    Smith, RE; Raffelt, D; Tournier, J-D; Connelly, A. Quantitative Streamlines
    Tractography: Methods and Inter-Subject Normalisation. Open Science
    Framework, https://doi.org/10.31219/osf.io/c67kn.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        in_tracks: the input track file.
        in_fod: input image containing the spherical harmonics of the fibre\
            orientation distributions.
        out_weights: output text file containing the weighting factor for each\
            streamline.
        proc_mask: provide an image containing the processing mask weights for\
            the model; image spatial dimensions must match the fixel image.
        act: use an ACT five-tissue-type segmented anatomical image to derive\
            the processing mask.
        fd_scale_gm: provide this option (in conjunction with -act) to\
            heuristically downsize the fibre density estimates based on the\
            presence of GM in the voxel. This can assist in reducing tissue\
            interface effects when using a single-tissue deconvolution algorithm.
        no_dilate_lut: do NOT dilate FOD lobe lookup tables; only map\
            streamlines to FOD lobes if the precise tangent lies within the angular\
            spread of that lobe.
        make_null_lobes: add an additional FOD lobe to each voxel, with zero\
            integral, that covers all directions with zero / negative FOD\
            amplitudes.
        remove_untracked: remove FOD lobes that do not have any streamline\
            density attributed to them; this improves filtering slightly, at the\
            expense of longer computation time (and you can no longer do\
            quantitative comparisons between reconstructions if this is enabled).
        fd_thresh: fibre density threshold; exclude an FOD lobe from filtering\
            processing if its integral is less than this amount (streamlines will\
            still be mapped to it, but it will not contribute to the cost function\
            or the filtering).
        csv_: output statistics of execution per iteration to a .csv file.
        out_mu: output the final value of SIFT proportionality coefficient mu\
            to a text file.
        output_debug: provide various output images for assessing & debugging\
            performance etc.
        out_coeffs: output text file containing the weighting coefficient for\
            each streamline.
        reg_tikhonov: provide coefficient for regularising streamline weighting\
            coefficients (Tikhonov regularisation) (default: 0).
        reg_tv: provide coefficient for regularising variance of streamline\
            weighting coefficient to fixels along its length (Total Variation\
            regularisation) (default: 0.1).
        min_td_frac: minimum fraction of the FOD integral reconstructed by\
            streamlines; if the reconstructed streamline density is below this\
            fraction, the fixel is excluded from optimisation (default: 0.1).
        min_iters: minimum number of iterations to run before testing for\
            convergence; this can prevent premature termination at early iterations\
            if the cost function increases slightly (default: 10).
        max_iters: maximum number of iterations to run before terminating\
            program.
        min_factor: minimum weighting factor for an individual streamline; if\
            the factor falls below this number the streamline will be rejected\
            entirely (factor set to zero) (default: 0).
        min_coeff: minimum weighting coefficient for an individual streamline;\
            similar to the '-min_factor' option, but using the exponential\
            coefficient basis of the SIFT2 model; these parameters are related as:\
            factor = e^(coeff). Note that the -min_factor and -min_coeff options\
            are mutually exclusive - you can only provide one. (default: -inf).
        max_factor: maximum weighting factor that can be assigned to any one\
            streamline (default: inf).
        max_coeff: maximum weighting coefficient for an individual streamline;\
            similar to the '-max_factor' option, but using the exponential\
            coefficient basis of the SIFT2 model; these parameters are related as:\
            factor = e^(coeff). Note that the -max_factor and -max_coeff options\
            are mutually exclusive - you can only provide one. (default: inf).
        max_coeff_step: maximum change to a streamline's weighting coefficient\
            in a single iteration (default: 1).
        min_cf_decrease: minimum decrease in the cost function (as a fraction\
            of the initial value) that must occur each iteration for the algorithm\
            to continue (default: 2.5e-05).
        linear: perform a linear estimation of streamline weights, rather than\
            the standard non-linear optimisation (typically does not provide as\
            accurate a model fit; but only requires a single pass).
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
        NamedTuple of outputs (described in `Tcksift2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKSIFT2_METADATA)
    params = tcksift2_params(proc_mask=proc_mask, act=act, fd_scale_gm=fd_scale_gm, no_dilate_lut=no_dilate_lut, make_null_lobes=make_null_lobes, remove_untracked=remove_untracked, fd_thresh=fd_thresh, csv_=csv_, out_mu=out_mu, output_debug=output_debug, out_coeffs=out_coeffs, reg_tikhonov=reg_tikhonov, reg_tv=reg_tv, min_td_frac=min_td_frac, min_iters=min_iters, max_iters=max_iters, min_factor=min_factor, min_coeff=min_coeff, max_factor=max_factor, max_coeff=max_coeff, max_coeff_step=max_coeff_step, min_cf_decrease=min_cf_decrease, linear=linear, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, in_tracks=in_tracks, in_fod=in_fod, out_weights=out_weights)
    return tcksift2_execute(params, execution)


__all__ = [
    "TCKSIFT2_METADATA",
    "Tcksift2ConfigParameters",
    "Tcksift2Outputs",
    "Tcksift2Parameters",
    "tcksift2",
    "tcksift2_config_params",
    "tcksift2_params",
]
