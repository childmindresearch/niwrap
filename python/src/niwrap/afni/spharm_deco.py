# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SPHARM_DECO_METADATA = Metadata(
    id="6c5408eda75c3fcbee3c137d9a99cb7b538fb149.boutiques",
    name="SpharmDeco",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SpharmDecoParameters = typing.TypedDict('SpharmDecoParameters', {
    "__STYX_TYPE__": typing.Literal["SpharmDeco"],
    "i_type_s": InputPathType,
    "unit_sph_label": str,
    "order_l": float,
    "i_type_sd": typing.NotRequired[list[InputPathType] | None],
    "data_d": typing.NotRequired[InputPathType | None],
    "bases_prefix": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "o_type_sdr": typing.NotRequired[list[InputPathType] | None],
    "debug": typing.NotRequired[float | None],
    "sigma": typing.NotRequired[float | None],
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
        "SpharmDeco": spharm_deco_cargs,
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
        "SpharmDeco": spharm_deco_outputs,
    }
    return vt.get(t)


class SpharmDecoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spharm_deco(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    harmonics_file: OutputPathType
    """File for harmonics of each order l."""
    beta_coefficients: OutputPathType
    """Beta coefficients for each data column."""
    reconstructed_data: OutputPathType
    """Reconstructed data or surface files named based on PREFIX."""


def spharm_deco_params(
    i_type_s: InputPathType,
    unit_sph_label: str,
    order_l: float,
    i_type_sd: list[InputPathType] | None = None,
    data_d: InputPathType | None = None,
    bases_prefix: str | None = None,
    prefix: str | None = None,
    o_type_sdr: list[InputPathType] | None = None,
    debug: float | None = None,
    sigma: float | None = None,
) -> SpharmDecoParameters:
    """
    Build parameters.
    
    Args:
        i_type_s: Unit sphere, isotopic to the surface domain over which the\
            data to be decomposed is defined.
        unit_sph_label: Label of the unit sphere.
        order_l: Decomposition order.
        i_type_sd: A surface whose node coordinates provide data vectors (X, Y,\
            Z) to be decomposed or a dataset whose columns are to be individually\
            decomposed. You can specify multiple surfaces to be processed.
        data_d: Data vectors to be decomposed.
        bases_prefix: Save the basis functions under the prefix BASES_PREFIX.
        prefix: Write out the reconstructed data into dataset PREFIX and write\
            the beta coefficients for each processed data column.
        o_type_sdr: Write out a new surface with reconstructed coordinates.
        debug: Debug levels (1-3).
        sigma: Smoothing parameter (0 .. 0.001) which weighs down the\
            contribution of higher order harmonics.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SpharmDeco",
        "i_type_s": i_type_s,
        "unit_sph_label": unit_sph_label,
        "order_l": order_l,
    }
    if i_type_sd is not None:
        params["i_type_sd"] = i_type_sd
    if data_d is not None:
        params["data_d"] = data_d
    if bases_prefix is not None:
        params["bases_prefix"] = bases_prefix
    if prefix is not None:
        params["prefix"] = prefix
    if o_type_sdr is not None:
        params["o_type_sdr"] = o_type_sdr
    if debug is not None:
        params["debug"] = debug
    if sigma is not None:
        params["sigma"] = sigma
    return params


def spharm_deco_cargs(
    params: SpharmDecoParameters,
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
    cargs.append("SpharmDeco")
    cargs.append(execution.input_file(params.get("i_type_s")))
    cargs.append(params.get("unit_sph_label"))
    cargs.append(str(params.get("order_l")))
    if params.get("i_type_sd") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("i_type_sd")])
    if params.get("data_d") is not None:
        cargs.append(execution.input_file(params.get("data_d")))
    if params.get("bases_prefix") is not None:
        cargs.append(params.get("bases_prefix"))
    if params.get("prefix") is not None:
        cargs.append(params.get("prefix"))
    if params.get("o_type_sdr") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("o_type_sdr")])
    if params.get("debug") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug"))
        ])
    if params.get("sigma") is not None:
        cargs.extend([
            "-sigma",
            str(params.get("sigma"))
        ])
    return cargs


def spharm_deco_outputs(
    params: SpharmDecoParameters,
    execution: Execution,
) -> SpharmDecoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SpharmDecoOutputs(
        root=execution.output_file("."),
        harmonics_file=execution.output_file("BASES_PREFIX.sph*.1D"),
        beta_coefficients=execution.output_file("PREFIX.beta.col*.1D.dset"),
        reconstructed_data=execution.output_file("<PREFIX>_reconstructed"),
    )
    return ret


def spharm_deco_execute(
    params: SpharmDecoParameters,
    execution: Execution,
) -> SpharmDecoOutputs:
    """
    Spherical Harmonics Decomposition of a surface's coordinates or data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SpharmDecoOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = spharm_deco_cargs(params, execution)
    ret = spharm_deco_outputs(params, execution)
    execution.run(cargs)
    return ret


def spharm_deco(
    i_type_s: InputPathType,
    unit_sph_label: str,
    order_l: float,
    i_type_sd: list[InputPathType] | None = None,
    data_d: InputPathType | None = None,
    bases_prefix: str | None = None,
    prefix: str | None = None,
    o_type_sdr: list[InputPathType] | None = None,
    debug: float | None = None,
    sigma: float | None = None,
    runner: Runner | None = None,
) -> SpharmDecoOutputs:
    """
    Spherical Harmonics Decomposition of a surface's coordinates or data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        i_type_s: Unit sphere, isotopic to the surface domain over which the\
            data to be decomposed is defined.
        unit_sph_label: Label of the unit sphere.
        order_l: Decomposition order.
        i_type_sd: A surface whose node coordinates provide data vectors (X, Y,\
            Z) to be decomposed or a dataset whose columns are to be individually\
            decomposed. You can specify multiple surfaces to be processed.
        data_d: Data vectors to be decomposed.
        bases_prefix: Save the basis functions under the prefix BASES_PREFIX.
        prefix: Write out the reconstructed data into dataset PREFIX and write\
            the beta coefficients for each processed data column.
        o_type_sdr: Write out a new surface with reconstructed coordinates.
        debug: Debug levels (1-3).
        sigma: Smoothing parameter (0 .. 0.001) which weighs down the\
            contribution of higher order harmonics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SpharmDecoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPHARM_DECO_METADATA)
    params = spharm_deco_params(i_type_s=i_type_s, unit_sph_label=unit_sph_label, order_l=order_l, i_type_sd=i_type_sd, data_d=data_d, bases_prefix=bases_prefix, prefix=prefix, o_type_sdr=o_type_sdr, debug=debug, sigma=sigma)
    return spharm_deco_execute(params, execution)


__all__ = [
    "SPHARM_DECO_METADATA",
    "SpharmDecoOutputs",
    "SpharmDecoParameters",
    "spharm_deco",
    "spharm_deco_params",
]
