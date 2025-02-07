# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

AMP2RESPONSE_METADATA = Metadata(
    id="45d8955b40d231d0262470246ab11182cd79fcb5.boutiques",
    name="amp2response",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Amp2responseConfigParameters = typing.TypedDict('Amp2responseConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Amp2responseParameters = typing.TypedDict('Amp2responseParameters', {
    "__STYX_TYPE__": typing.Literal["amp2response"],
    "isotropic": bool,
    "noconstraint": bool,
    "directions": typing.NotRequired[InputPathType | None],
    "shells": typing.NotRequired[list[float] | None],
    "lmax": typing.NotRequired[list[int] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Amp2responseConfigParameters] | None],
    "help": bool,
    "version": bool,
    "amps": InputPathType,
    "mask": InputPathType,
    "directions": InputPathType,
    "response": str,
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
        "amp2response": amp2response_cargs,
        "config": amp2response_config_cargs,
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
        "amp2response": amp2response_outputs,
        "config": amp2response_config_outputs,
    }.get(t)


def amp2response_config_params(
    key: str,
    value: str,
) -> Amp2responseConfigParameters:
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


def amp2response_config_cargs(
    params: Amp2responseConfigParameters,
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


class Amp2responseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `amp2response(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    response: OutputPathType
    """the output zonal spherical harmonic coefficients"""


def amp2response_params(
    amps: InputPathType,
    mask: InputPathType,
    directions_: InputPathType,
    response: str,
    isotropic: bool = False,
    noconstraint: bool = False,
    directions: InputPathType | None = None,
    shells: list[float] | None = None,
    lmax: list[int] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Amp2responseConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Amp2responseParameters:
    """
    Build parameters.
    
    Args:
        amps: the amplitudes image.
        mask: the mask containing the voxels from which to estimate the\
            response function.
        directions_: a 4D image containing the estimated fibre directions.
        response: the output zonal spherical harmonic coefficients.
        isotropic: estimate an isotropic response function (lmax=0 for all\
            shells).
        noconstraint: disable the non-negativity and monotonicity constraints.
        directions: provide an external text file containing the directions\
            along which the amplitudes are sampled.
        shells: specify one or more b-values to use during processing, as a\
            comma-separated list of the desired approximate b-values (b-values are\
            clustered to allow for small deviations). Note that some commands are\
            incompatible with multiple b-values, and will report an error if more\
            than one b-value is provided.\
            WARNING: note that, even though the b=0 volumes are never referred\
            to as shells in the literature, they still have to be explicitly\
            included in the list of b-values as provided to the -shell option!\
            Several algorithms which include the b=0 volumes in their\
            computations may otherwise return an undesired result.
        lmax: specify the maximum harmonic degree of the response function to\
            estimate (can be a comma-separated list for multi-shell data).
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
        "__STYXTYPE__": "amp2response",
        "isotropic": isotropic,
        "noconstraint": noconstraint,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "amps": amps,
        "mask": mask,
        "directions": directions_,
        "response": response,
    }
    if directions is not None:
        params["directions"] = directions
    if shells is not None:
        params["shells"] = shells
    if lmax is not None:
        params["lmax"] = lmax
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def amp2response_cargs(
    params: Amp2responseParameters,
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
    cargs.append("amp2response")
    if params.get("isotropic"):
        cargs.append("-isotropic")
    if params.get("noconstraint"):
        cargs.append("-noconstraint")
    if params.get("directions") is not None:
        cargs.extend([
            "-directions",
            execution.input_file(params.get("directions"))
        ])
    if params.get("shells") is not None:
        cargs.extend([
            "-shells",
            ",".join(map(str, params.get("shells")))
        ])
    if params.get("lmax") is not None:
        cargs.extend([
            "-lmax",
            ",".join(map(str, params.get("lmax")))
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
    cargs.append(execution.input_file(params.get("amps")))
    cargs.append(execution.input_file(params.get("mask")))
    cargs.append(execution.input_file(params.get("directions")))
    cargs.append(params.get("response"))
    return cargs


def amp2response_outputs(
    params: Amp2responseParameters,
    execution: Execution,
) -> Amp2responseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Amp2responseOutputs(
        root=execution.output_file("."),
        response=execution.output_file(params.get("response")),
    )
    return ret


def amp2response_execute(
    params: Amp2responseParameters,
    execution: Execution,
) -> Amp2responseOutputs:
    """
    Estimate response function coefficients based on the DWI signal in single-fibre
    voxels.
    
    This command uses the image data from all selected single-fibre voxels
    concurrently, rather than simply averaging their individual spherical
    harmonic coefficients. It also ensures that the response function is
    non-negative, and monotonic (i.e. its amplitude must increase from the fibre
    direction out to the orthogonal plane).
    
    If multi-shell data are provided, and one or more b-value shells are not
    explicitly requested, the command will generate a response function for
    every b-value shell (including b=0 if present).
    
    References:
    
    Smith, R. E.; Dhollander, T. & Connelly, A. Constrained linear least squares
    estimation of anisotropic response function for spherical deconvolution.
    ISMRM Workshop on Breaking the Barriers of Diffusion MRI, 23.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Amp2responseOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = amp2response_cargs(params, execution)
    ret = amp2response_outputs(params, execution)
    execution.run(cargs)
    return ret


def amp2response(
    amps: InputPathType,
    mask: InputPathType,
    directions_: InputPathType,
    response: str,
    isotropic: bool = False,
    noconstraint: bool = False,
    directions: InputPathType | None = None,
    shells: list[float] | None = None,
    lmax: list[int] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Amp2responseConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Amp2responseOutputs:
    """
    Estimate response function coefficients based on the DWI signal in single-fibre
    voxels.
    
    This command uses the image data from all selected single-fibre voxels
    concurrently, rather than simply averaging their individual spherical
    harmonic coefficients. It also ensures that the response function is
    non-negative, and monotonic (i.e. its amplitude must increase from the fibre
    direction out to the orthogonal plane).
    
    If multi-shell data are provided, and one or more b-value shells are not
    explicitly requested, the command will generate a response function for
    every b-value shell (including b=0 if present).
    
    References:
    
    Smith, R. E.; Dhollander, T. & Connelly, A. Constrained linear least squares
    estimation of anisotropic response function for spherical deconvolution.
    ISMRM Workshop on Breaking the Barriers of Diffusion MRI, 23.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        amps: the amplitudes image.
        mask: the mask containing the voxels from which to estimate the\
            response function.
        directions_: a 4D image containing the estimated fibre directions.
        response: the output zonal spherical harmonic coefficients.
        isotropic: estimate an isotropic response function (lmax=0 for all\
            shells).
        noconstraint: disable the non-negativity and monotonicity constraints.
        directions: provide an external text file containing the directions\
            along which the amplitudes are sampled.
        shells: specify one or more b-values to use during processing, as a\
            comma-separated list of the desired approximate b-values (b-values are\
            clustered to allow for small deviations). Note that some commands are\
            incompatible with multiple b-values, and will report an error if more\
            than one b-value is provided.\
            WARNING: note that, even though the b=0 volumes are never referred\
            to as shells in the literature, they still have to be explicitly\
            included in the list of b-values as provided to the -shell option!\
            Several algorithms which include the b=0 volumes in their\
            computations may otherwise return an undesired result.
        lmax: specify the maximum harmonic degree of the response function to\
            estimate (can be a comma-separated list for multi-shell data).
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
        NamedTuple of outputs (described in `Amp2responseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AMP2RESPONSE_METADATA)
    params = amp2response_params(isotropic=isotropic, noconstraint=noconstraint, directions=directions, shells=shells, lmax=lmax, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, amps=amps, mask=mask, directions_=directions_, response=response)
    return amp2response_execute(params, execution)


__all__ = [
    "AMP2RESPONSE_METADATA",
    "Amp2responseConfigParameters",
    "Amp2responseOutputs",
    "Amp2responseParameters",
    "amp2response",
    "amp2response_config_params",
    "amp2response_params",
]
