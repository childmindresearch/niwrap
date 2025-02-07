# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FILM_GLS_METADATA = Metadata(
    id="f39dd7c8e81740062ca1452d21d0bb5ced20f4aa.boutiques",
    name="film_gls",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FilmGlsParameters = typing.TypedDict('FilmGlsParameters', {
    "__STYX_TYPE__": typing.Literal["film_gls"],
    "infile": InputPathType,
    "ac_flag": bool,
    "threshold": typing.NotRequired[float | None],
    "ar_flag": bool,
    "noest_flag": bool,
    "outputPW_flag": bool,
    "pava_flag": bool,
    "sa_flag": bool,
    "verbose_flag": bool,
    "results_dir": typing.NotRequired[str | None],
    "mode": typing.NotRequired[str | None],
    "input_surface": typing.NotRequired[InputPathType | None],
    "mean_func_file": typing.NotRequired[InputPathType | None],
    "min_timepoint_file": typing.NotRequired[InputPathType | None],
    "paradigm_file": typing.NotRequired[InputPathType | None],
    "t_contrasts_file": typing.NotRequired[InputPathType | None],
    "f_contrasts_file": typing.NotRequired[InputPathType | None],
    "epith": typing.NotRequired[float | None],
    "ms": typing.NotRequired[float | None],
    "tukey": typing.NotRequired[float | None],
    "mt": typing.NotRequired[float | None],
    "ven": typing.NotRequired[list[str] | None],
    "vef": typing.NotRequired[list[InputPathType] | None],
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
        "film_gls": film_gls_cargs,
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
        "film_gls": film_gls_outputs,
    }.get(t)


class FilmGlsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `film_gls(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    prewhitened_data: OutputPathType
    """Prewhitened data output"""
    average_design_matrix: OutputPathType
    """Average design matrix output"""
    results_data: OutputPathType
    """Results output"""


def film_gls_params(
    infile: InputPathType,
    ac_flag: bool = False,
    threshold: float | None = None,
    ar_flag: bool = False,
    noest_flag: bool = False,
    output_pw_flag: bool = False,
    pava_flag: bool = False,
    sa_flag: bool = False,
    verbose_flag: bool = False,
    results_dir: str | None = None,
    mode: str | None = None,
    input_surface: InputPathType | None = None,
    mean_func_file: InputPathType | None = None,
    min_timepoint_file: InputPathType | None = None,
    paradigm_file: InputPathType | None = None,
    t_contrasts_file: InputPathType | None = None,
    f_contrasts_file: InputPathType | None = None,
    epith: float | None = None,
    ms: float | None = None,
    tukey: float | None = None,
    mt: float | None = None,
    ven: list[str] | None = None,
    vef: list[InputPathType] | None = None,
) -> FilmGlsParameters:
    """
    Build parameters.
    
    Args:
        infile: Input data file (NIFTI for volumetric, GIFTI for surface).
        ac_flag: Perform autocorrelation estimation only.
        threshold: Initial threshold to apply to input data.
        ar_flag: Fits autoregressive model - default is to use tukey with\
            M=sqrt(numvols).
        noest_flag: Do not estimate autocorrelations.
        output_pw_flag: Output prewhitened data and average design matrix.
        pava_flag: Estimates autocorrelation using PAVA - default is to use\
            tukey with M=sqrt(numvols).
        sa_flag: Smooths autocorrelation estimates.
        verbose_flag: Outputs full data.
        results_dir: Directory name to store results in, default is results.
        mode: Analysis mode, options are volumetric (default) or surface.\
            Caution: surface-based functionality is still BETA.
        input_surface: Input surface for autocorrelation smoothing in\
            surface-based analyses.
        mean_func_file: Re-estimate mean_func baseline - for use with perfusion\
            subtraction.
        min_timepoint_file: Minimum timepoint file.
        paradigm_file: Paradigm file.
        t_contrasts_file: T-contrasts file.
        f_contrasts_file: F-contrasts file.
        epith: SUSAN brightness threshold for volumetric analysis/smoothing\
            sigma for surface analysis.
        ms: SUSAN mask size for volumetric analysis/smoothing extent for\
            surface analysis.
        tukey: Uses tukey window to estimate autocorrelation with window size\
            num - default is to use tukey with M=sqrt(numvols).
        mt: Uses multitapering with slepian tapers and num is the\
            time-bandwidth product - default is to use tukey with M=sqrt(numvols).
        ven: List of numbers indicating voxelwise EVs position in the design\
            matrix (list order corresponds to files in vxf option). Caution BETA\
            option, only use with volumetric analysis.
        vef: List of 4D images containing voxelwise EVs (list order corresponds\
            to numbers in vxl option). Caution BETA option, only use with\
            volumetric analysis.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "film_gls",
        "infile": infile,
        "ac_flag": ac_flag,
        "ar_flag": ar_flag,
        "noest_flag": noest_flag,
        "outputPW_flag": output_pw_flag,
        "pava_flag": pava_flag,
        "sa_flag": sa_flag,
        "verbose_flag": verbose_flag,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if results_dir is not None:
        params["results_dir"] = results_dir
    if mode is not None:
        params["mode"] = mode
    if input_surface is not None:
        params["input_surface"] = input_surface
    if mean_func_file is not None:
        params["mean_func_file"] = mean_func_file
    if min_timepoint_file is not None:
        params["min_timepoint_file"] = min_timepoint_file
    if paradigm_file is not None:
        params["paradigm_file"] = paradigm_file
    if t_contrasts_file is not None:
        params["t_contrasts_file"] = t_contrasts_file
    if f_contrasts_file is not None:
        params["f_contrasts_file"] = f_contrasts_file
    if epith is not None:
        params["epith"] = epith
    if ms is not None:
        params["ms"] = ms
    if tukey is not None:
        params["tukey"] = tukey
    if mt is not None:
        params["mt"] = mt
    if ven is not None:
        params["ven"] = ven
    if vef is not None:
        params["vef"] = vef
    return params


def film_gls_cargs(
    params: FilmGlsParameters,
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
    cargs.append("film_gls")
    cargs.append(execution.input_file(params.get("infile")))
    if params.get("ac_flag"):
        cargs.append("--ac")
    if params.get("threshold") is not None:
        cargs.extend([
            "--thr",
            str(params.get("threshold"))
        ])
    if params.get("ar_flag"):
        cargs.append("--ar")
    if params.get("noest_flag"):
        cargs.append("--noest")
    if params.get("outputPW_flag"):
        cargs.append("--outputPWdata")
    if params.get("pava_flag"):
        cargs.append("--pava")
    if params.get("sa_flag"):
        cargs.append("--sa")
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("results_dir") is not None:
        cargs.extend([
            "--rn",
            params.get("results_dir")
        ])
    if params.get("mode") is not None:
        cargs.extend([
            "--mode",
            params.get("mode")
        ])
    if params.get("input_surface") is not None:
        cargs.extend([
            "--in2",
            execution.input_file(params.get("input_surface"))
        ])
    if params.get("mean_func_file") is not None:
        cargs.extend([
            "--mf",
            execution.input_file(params.get("mean_func_file"))
        ])
    if params.get("min_timepoint_file") is not None:
        cargs.extend([
            "--mft",
            execution.input_file(params.get("min_timepoint_file"))
        ])
    if params.get("paradigm_file") is not None:
        cargs.extend([
            "--pd",
            execution.input_file(params.get("paradigm_file"))
        ])
    if params.get("t_contrasts_file") is not None:
        cargs.extend([
            "--con",
            execution.input_file(params.get("t_contrasts_file"))
        ])
    if params.get("f_contrasts_file") is not None:
        cargs.extend([
            "--fcon",
            execution.input_file(params.get("f_contrasts_file"))
        ])
    if params.get("epith") is not None:
        cargs.extend([
            "--epith",
            str(params.get("epith"))
        ])
    if params.get("ms") is not None:
        cargs.extend([
            "--ms",
            str(params.get("ms"))
        ])
    if params.get("tukey") is not None:
        cargs.extend([
            "--tukey",
            str(params.get("tukey"))
        ])
    if params.get("mt") is not None:
        cargs.extend([
            "--mt",
            str(params.get("mt"))
        ])
    if params.get("ven") is not None:
        cargs.extend([
            "--ven",
            *params.get("ven")
        ])
    if params.get("vef") is not None:
        cargs.extend([
            "--vef",
            *[execution.input_file(f) for f in params.get("vef")]
        ])
    return cargs


def film_gls_outputs(
    params: FilmGlsParameters,
    execution: Execution,
) -> FilmGlsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FilmGlsOutputs(
        root=execution.output_file("."),
        prewhitened_data=execution.output_file("[rn]/prewhitened_data.nii.gz"),
        average_design_matrix=execution.output_file("[rn]/average_design_matrix.txt"),
        results_data=execution.output_file("[rn]/results.txt"),
    )
    return ret


def film_gls_execute(
    params: FilmGlsParameters,
    execution: Execution,
) -> FilmGlsOutputs:
    """
    General Linear Model fitting with autocorrelation in FMRI.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FilmGlsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = film_gls_cargs(params, execution)
    ret = film_gls_outputs(params, execution)
    execution.run(cargs)
    return ret


def film_gls(
    infile: InputPathType,
    ac_flag: bool = False,
    threshold: float | None = None,
    ar_flag: bool = False,
    noest_flag: bool = False,
    output_pw_flag: bool = False,
    pava_flag: bool = False,
    sa_flag: bool = False,
    verbose_flag: bool = False,
    results_dir: str | None = None,
    mode: str | None = None,
    input_surface: InputPathType | None = None,
    mean_func_file: InputPathType | None = None,
    min_timepoint_file: InputPathType | None = None,
    paradigm_file: InputPathType | None = None,
    t_contrasts_file: InputPathType | None = None,
    f_contrasts_file: InputPathType | None = None,
    epith: float | None = None,
    ms: float | None = None,
    tukey: float | None = None,
    mt: float | None = None,
    ven: list[str] | None = None,
    vef: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> FilmGlsOutputs:
    """
    General Linear Model fitting with autocorrelation in FMRI.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input data file (NIFTI for volumetric, GIFTI for surface).
        ac_flag: Perform autocorrelation estimation only.
        threshold: Initial threshold to apply to input data.
        ar_flag: Fits autoregressive model - default is to use tukey with\
            M=sqrt(numvols).
        noest_flag: Do not estimate autocorrelations.
        output_pw_flag: Output prewhitened data and average design matrix.
        pava_flag: Estimates autocorrelation using PAVA - default is to use\
            tukey with M=sqrt(numvols).
        sa_flag: Smooths autocorrelation estimates.
        verbose_flag: Outputs full data.
        results_dir: Directory name to store results in, default is results.
        mode: Analysis mode, options are volumetric (default) or surface.\
            Caution: surface-based functionality is still BETA.
        input_surface: Input surface for autocorrelation smoothing in\
            surface-based analyses.
        mean_func_file: Re-estimate mean_func baseline - for use with perfusion\
            subtraction.
        min_timepoint_file: Minimum timepoint file.
        paradigm_file: Paradigm file.
        t_contrasts_file: T-contrasts file.
        f_contrasts_file: F-contrasts file.
        epith: SUSAN brightness threshold for volumetric analysis/smoothing\
            sigma for surface analysis.
        ms: SUSAN mask size for volumetric analysis/smoothing extent for\
            surface analysis.
        tukey: Uses tukey window to estimate autocorrelation with window size\
            num - default is to use tukey with M=sqrt(numvols).
        mt: Uses multitapering with slepian tapers and num is the\
            time-bandwidth product - default is to use tukey with M=sqrt(numvols).
        ven: List of numbers indicating voxelwise EVs position in the design\
            matrix (list order corresponds to files in vxf option). Caution BETA\
            option, only use with volumetric analysis.
        vef: List of 4D images containing voxelwise EVs (list order corresponds\
            to numbers in vxl option). Caution BETA option, only use with\
            volumetric analysis.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FilmGlsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILM_GLS_METADATA)
    params = film_gls_params(infile=infile, ac_flag=ac_flag, threshold=threshold, ar_flag=ar_flag, noest_flag=noest_flag, output_pw_flag=output_pw_flag, pava_flag=pava_flag, sa_flag=sa_flag, verbose_flag=verbose_flag, results_dir=results_dir, mode=mode, input_surface=input_surface, mean_func_file=mean_func_file, min_timepoint_file=min_timepoint_file, paradigm_file=paradigm_file, t_contrasts_file=t_contrasts_file, f_contrasts_file=f_contrasts_file, epith=epith, ms=ms, tukey=tukey, mt=mt, ven=ven, vef=vef)
    return film_gls_execute(params, execution)


__all__ = [
    "FILM_GLS_METADATA",
    "FilmGlsOutputs",
    "FilmGlsParameters",
    "film_gls",
    "film_gls_params",
]
