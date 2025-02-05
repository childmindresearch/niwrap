# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLCOMPLEX_METADATA = Metadata(
    id="c9fb65ebb725f2a440c3750432b06e3255db8eb3.boutiques",
    name="fslcomplex",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslcomplexParameters = typing.TypedDict('FslcomplexParameters', {
    "__STYX_TYPE__": typing.Literal["fslcomplex"],
    "input_file": InputPathType,
    "output_file": str,
    "output_type": typing.Literal["-realabs", "-realphase", "-realpolar", "-realcartesian", "-complex", "-complexpolar", "-complexsplit", "-complexmerge", "-copyonly"],
    "start_vol": typing.NotRequired[int | None],
    "end_vol": typing.NotRequired[int | None],
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
        "fslcomplex": fslcomplex_cargs,
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
        "fslcomplex": fslcomplex_outputs,
    }
    return vt.get(t)


class FslcomplexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcomplex(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_output_file: OutputPathType
    """The resulting output file from the specified operation."""


def fslcomplex_params(
    input_file: InputPathType,
    output_file: str,
    output_type: typing.Literal["-realabs", "-realphase", "-realpolar", "-realcartesian", "-complex", "-complexpolar", "-complexsplit", "-complexmerge", "-copyonly"],
    start_vol: int | None = None,
    end_vol: int | None = None,
) -> FslcomplexParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input volume (e.g. complexvol.nii.gz).
        output_file: Output volume (e.g. absvol.nii.gz).
        output_type: Output type (determines the operation to perform).
        start_vol: Start volume (optional).
        end_vol: End volume (optional).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslcomplex",
        "input_file": input_file,
        "output_file": output_file,
        "output_type": output_type,
    }
    if start_vol is not None:
        params["start_vol"] = start_vol
    if end_vol is not None:
        params["end_vol"] = end_vol
    return params


def fslcomplex_cargs(
    params: FslcomplexParameters,
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
    cargs.append("fslcomplex")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    cargs.append(params.get("output_type"))
    if params.get("start_vol") is not None:
        cargs.append(str(params.get("start_vol")))
    if params.get("end_vol") is not None:
        cargs.append(str(params.get("end_vol")))
    return cargs


def fslcomplex_outputs(
    params: FslcomplexParameters,
    execution: Execution,
) -> FslcomplexOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslcomplexOutputs(
        root=execution.output_file("."),
        result_output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def fslcomplex_execute(
    params: FslcomplexParameters,
    execution: Execution,
) -> FslcomplexOutputs:
    """
    Tool for manipulating complex-valued MR data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslcomplexOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslcomplex_cargs(params, execution)
    ret = fslcomplex_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslcomplex(
    input_file: InputPathType,
    output_file: str,
    output_type: typing.Literal["-realabs", "-realphase", "-realpolar", "-realcartesian", "-complex", "-complexpolar", "-complexsplit", "-complexmerge", "-copyonly"],
    start_vol: int | None = None,
    end_vol: int | None = None,
    runner: Runner | None = None,
) -> FslcomplexOutputs:
    """
    Tool for manipulating complex-valued MR data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input volume (e.g. complexvol.nii.gz).
        output_file: Output volume (e.g. absvol.nii.gz).
        output_type: Output type (determines the operation to perform).
        start_vol: Start volume (optional).
        end_vol: End volume (optional).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslcomplexOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCOMPLEX_METADATA)
    params = fslcomplex_params(input_file=input_file, output_file=output_file, output_type=output_type, start_vol=start_vol, end_vol=end_vol)
    return fslcomplex_execute(params, execution)


__all__ = [
    "FSLCOMPLEX_METADATA",
    "FslcomplexOutputs",
    "FslcomplexParameters",
    "fslcomplex",
    "fslcomplex_params",
]
