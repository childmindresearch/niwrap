# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLHD_METADATA = Metadata(
    id="d73c7c47c18423156696e1dd5e4756b9af7451a8.boutiques",
    name="fslhd",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslhdParameters = typing.TypedDict('FslhdParameters', {
    "__STYX_TYPE__": typing.Literal["fslhd"],
    "xml_flag": bool,
    "input_file": InputPathType,
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
        "fslhd": fslhd_cargs,
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
        "fslhd": fslhd_outputs,
    }.get(t)


class FslhdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslhd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslhd_params(
    input_file: InputPathType,
    xml_flag: bool = False,
) -> FslhdParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input NIFTI file.
        xml_flag: Print an XML-style NIFTI header.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslhd",
        "xml_flag": xml_flag,
        "input_file": input_file,
    }
    return params


def fslhd_cargs(
    params: FslhdParameters,
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
    cargs.append("fslhd")
    if params.get("xml_flag"):
        cargs.append("-x")
    cargs.append(execution.input_file(params.get("input_file")))
    return cargs


def fslhd_outputs(
    params: FslhdParameters,
    execution: Execution,
) -> FslhdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslhdOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslhd_execute(
    params: FslhdParameters,
    execution: Execution,
) -> FslhdOutputs:
    """
    Display header information from a NIFTI file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslhdOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslhd_cargs(params, execution)
    ret = fslhd_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslhd(
    input_file: InputPathType,
    xml_flag: bool = False,
    runner: Runner | None = None,
) -> FslhdOutputs:
    """
    Display header information from a NIFTI file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input NIFTI file.
        xml_flag: Print an XML-style NIFTI header.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslhdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLHD_METADATA)
    params = fslhd_params(xml_flag=xml_flag, input_file=input_file)
    return fslhd_execute(params, execution)


__all__ = [
    "FSLHD_METADATA",
    "FslhdOutputs",
    "FslhdParameters",
    "fslhd",
    "fslhd_params",
]
