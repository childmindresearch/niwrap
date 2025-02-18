# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_DYADIC_VECTORS_METADATA = Metadata(
    id="0ee2428d543d257f22c959327d85ce191f76e480.boutiques",
    name="make_dyadic_vectors",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MakeDyadicVectorsParameters = typing.TypedDict('MakeDyadicVectorsParameters', {
    "__STYX_TYPE__": typing.Literal["make_dyadic_vectors"],
    "theta_vol": InputPathType,
    "phi_vol": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "output": str,
    "perc": typing.NotRequired[float | None],
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
        "make_dyadic_vectors": make_dyadic_vectors_cargs,
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
        "make_dyadic_vectors": make_dyadic_vectors_outputs,
    }.get(t)


class MakeDyadicVectorsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_dyadic_vectors(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file containing the generated dyadic vectors"""


def make_dyadic_vectors_params(
    theta_vol: InputPathType,
    phi_vol: InputPathType,
    output: str,
    mask: InputPathType | None = None,
    perc: float | None = None,
) -> MakeDyadicVectorsParameters:
    """
    Build parameters.
    
    Args:
        theta_vol: Theta volume input file.
        phi_vol: Phi volume input file.
        output: Output file.
        mask: Mask input file (optional).
        perc: Percentage angle of the output cone of uncertainty (output will\
            be in degrees).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make_dyadic_vectors",
        "theta_vol": theta_vol,
        "phi_vol": phi_vol,
        "output": output,
    }
    if mask is not None:
        params["mask"] = mask
    if perc is not None:
        params["perc"] = perc
    return params


def make_dyadic_vectors_cargs(
    params: MakeDyadicVectorsParameters,
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
    cargs.append("make_dyadic_vectors")
    cargs.append(execution.input_file(params.get("theta_vol")))
    cargs.append(execution.input_file(params.get("phi_vol")))
    if params.get("mask") is not None:
        cargs.append(execution.input_file(params.get("mask")))
    cargs.append(params.get("output"))
    if params.get("perc") is not None:
        cargs.append(str(params.get("perc")))
    return cargs


def make_dyadic_vectors_outputs(
    params: MakeDyadicVectorsParameters,
    execution: Execution,
) -> MakeDyadicVectorsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeDyadicVectorsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output")),
    )
    return ret


def make_dyadic_vectors_execute(
    params: MakeDyadicVectorsParameters,
    execution: Execution,
) -> MakeDyadicVectorsOutputs:
    """
    Generate dyadic vectors from theta and phi volumes.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeDyadicVectorsOutputs`).
    """
    params = execution.params(params)
    cargs = make_dyadic_vectors_cargs(params, execution)
    ret = make_dyadic_vectors_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_dyadic_vectors(
    theta_vol: InputPathType,
    phi_vol: InputPathType,
    output: str,
    mask: InputPathType | None = None,
    perc: float | None = None,
    runner: Runner | None = None,
) -> MakeDyadicVectorsOutputs:
    """
    Generate dyadic vectors from theta and phi volumes.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        theta_vol: Theta volume input file.
        phi_vol: Phi volume input file.
        output: Output file.
        mask: Mask input file (optional).
        perc: Percentage angle of the output cone of uncertainty (output will\
            be in degrees).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeDyadicVectorsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_DYADIC_VECTORS_METADATA)
    params = make_dyadic_vectors_params(theta_vol=theta_vol, phi_vol=phi_vol, mask=mask, output=output, perc=perc)
    return make_dyadic_vectors_execute(params, execution)


__all__ = [
    "MAKE_DYADIC_VECTORS_METADATA",
    "MakeDyadicVectorsOutputs",
    "MakeDyadicVectorsParameters",
    "make_dyadic_vectors",
    "make_dyadic_vectors_params",
]
