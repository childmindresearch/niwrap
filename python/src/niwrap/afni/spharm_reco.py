# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SPHARM_RECO_METADATA = Metadata(
    id="33f63f74ec6a7870069eec599fbb3c35bec65ba8.boutiques",
    name="SpharmReco",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SpharmRecoParameters = typing.TypedDict('SpharmRecoParameters', {
    "__STYX_TYPE__": typing.Literal["SpharmReco"],
    "input_surface": str,
    "decomposition_order": float,
    "bases_prefix": str,
    "coefficients": list[InputPathType],
    "output_prefix": typing.NotRequired[str | None],
    "output_surface": typing.NotRequired[list[str] | None],
    "debug": typing.NotRequired[float | None],
    "smoothing": typing.NotRequired[float | None],
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
        "SpharmReco": spharm_reco_cargs,
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
    vt = {}
    return vt.get(t)


class SpharmRecoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spharm_reco(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def spharm_reco_params(
    input_surface: str,
    decomposition_order: float,
    bases_prefix: str,
    coefficients: list[InputPathType],
    output_prefix: str | None = None,
    output_surface: list[str] | None = None,
    debug: float | None = None,
    smoothing: float | None = None,
) -> SpharmRecoParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Surface that provides the topology of the mesh (nodes'\
            connections). TYPE specifies the input surface type.
        decomposition_order: Decomposition order.
        bases_prefix: Prefix of files containing the bases functions (spherical\
            harmonics). These files are generated with SpharmDeco.
        coefficients: Coefficients files used to recompose data columns.\
            Multiple coefficient files can be specified by repeating the option.
        output_prefix: Write out the reconstructed data into dataset PREFIX.\
            The output contains N columns; one for each COEF file.
        output_surface: Write out a new surface with reconstructed coordinates.\
            Requires N to be a multiple of 3.
        debug: Debug levels (1-3).
        smoothing: Smoothing parameter (0 .. 0.001) weighing the contribution\
            of higher order harmonics.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SpharmReco",
        "input_surface": input_surface,
        "decomposition_order": decomposition_order,
        "bases_prefix": bases_prefix,
        "coefficients": coefficients,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if output_surface is not None:
        params["output_surface"] = output_surface
    if debug is not None:
        params["debug"] = debug
    if smoothing is not None:
        params["smoothing"] = smoothing
    return params


def spharm_reco_cargs(
    params: SpharmRecoParameters,
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
    cargs.append("SpharmReco")
    cargs.extend([
        "-i_TYPE",
        params.get("input_surface")
    ])
    cargs.extend([
        "-l",
        str(params.get("decomposition_order"))
    ])
    cargs.extend([
        "-bases_prefix",
        params.get("bases_prefix")
    ])
    cargs.extend([
        "-coef",
        *[execution.input_file(f) for f in params.get("coefficients")]
    ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("output_surface") is not None:
        cargs.extend([
            "-o_TYPE",
            *params.get("output_surface")
        ])
    if params.get("debug") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug"))
        ])
    if params.get("smoothing") is not None:
        cargs.extend([
            "-sigma",
            str(params.get("smoothing"))
        ])
    return cargs


def spharm_reco_outputs(
    params: SpharmRecoParameters,
    execution: Execution,
) -> SpharmRecoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SpharmRecoOutputs(
        root=execution.output_file("."),
    )
    return ret


def spharm_reco_execute(
    params: SpharmRecoParameters,
    execution: Execution,
) -> SpharmRecoOutputs:
    """
    Spherical Harmonics Reconstruction from a set of harmonics and their
    corresponding coefficients.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SpharmRecoOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = spharm_reco_cargs(params, execution)
    ret = spharm_reco_outputs(params, execution)
    execution.run(cargs)
    return ret


def spharm_reco(
    input_surface: str,
    decomposition_order: float,
    bases_prefix: str,
    coefficients: list[InputPathType],
    output_prefix: str | None = None,
    output_surface: list[str] | None = None,
    debug: float | None = None,
    smoothing: float | None = None,
    runner: Runner | None = None,
) -> SpharmRecoOutputs:
    """
    Spherical Harmonics Reconstruction from a set of harmonics and their
    corresponding coefficients.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_surface: Surface that provides the topology of the mesh (nodes'\
            connections). TYPE specifies the input surface type.
        decomposition_order: Decomposition order.
        bases_prefix: Prefix of files containing the bases functions (spherical\
            harmonics). These files are generated with SpharmDeco.
        coefficients: Coefficients files used to recompose data columns.\
            Multiple coefficient files can be specified by repeating the option.
        output_prefix: Write out the reconstructed data into dataset PREFIX.\
            The output contains N columns; one for each COEF file.
        output_surface: Write out a new surface with reconstructed coordinates.\
            Requires N to be a multiple of 3.
        debug: Debug levels (1-3).
        smoothing: Smoothing parameter (0 .. 0.001) weighing the contribution\
            of higher order harmonics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SpharmRecoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPHARM_RECO_METADATA)
    params = spharm_reco_params(input_surface=input_surface, decomposition_order=decomposition_order, bases_prefix=bases_prefix, coefficients=coefficients, output_prefix=output_prefix, output_surface=output_surface, debug=debug, smoothing=smoothing)
    return spharm_reco_execute(params, execution)


__all__ = [
    "SPHARM_RECO_METADATA",
    "SpharmRecoOutputs",
    "spharm_reco",
    "spharm_reco_params",
]
