# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_HIRES_REGISTER_METADATA = Metadata(
    id="6971a2770a2fb8afa234ab525393bacd1cd86c4e.boutiques",
    name="mri_hires_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriHiresRegisterParameters = typing.TypedDict('MriHiresRegisterParameters', {
    "__STYX_TYPE__": typing.Literal["mri_hires_register"],
    "hires_labeling": InputPathType,
    "input_intensity": InputPathType,
    "input_aseg": InputPathType,
    "output_xform": str,
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
        "mri_hires_register": mri_hires_register_cargs,
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
        "mri_hires_register": mri_hires_register_outputs,
    }.get(t)


class MriHiresRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_hires_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output transform file resulting from high-resolution registration"""


def mri_hires_register_params(
    hires_labeling: InputPathType,
    input_intensity: InputPathType,
    input_aseg: InputPathType,
    output_xform: str,
) -> MriHiresRegisterParameters:
    """
    Build parameters.
    
    Args:
        hires_labeling: The high resolution labeling input file.
        input_intensity: The input intensity file.
        input_aseg: The input aseg file.
        output_xform: The output transform file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_hires_register",
        "hires_labeling": hires_labeling,
        "input_intensity": input_intensity,
        "input_aseg": input_aseg,
        "output_xform": output_xform,
    }
    return params


def mri_hires_register_cargs(
    params: MriHiresRegisterParameters,
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
    cargs.append("mri_hires_register")
    cargs.append(execution.input_file(params.get("hires_labeling")))
    cargs.append(execution.input_file(params.get("input_intensity")))
    cargs.append(execution.input_file(params.get("input_aseg")))
    cargs.append(params.get("output_xform"))
    return cargs


def mri_hires_register_outputs(
    params: MriHiresRegisterParameters,
    execution: Execution,
) -> MriHiresRegisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriHiresRegisterOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_xform")),
    )
    return ret


def mri_hires_register_execute(
    params: MriHiresRegisterParameters,
    execution: Execution,
) -> MriHiresRegisterOutputs:
    """
    A tool for high-resolution registration for Freesurfer images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriHiresRegisterOutputs`).
    """
    cargs = mri_hires_register_cargs(params, execution)
    ret = mri_hires_register_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_hires_register(
    hires_labeling: InputPathType,
    input_intensity: InputPathType,
    input_aseg: InputPathType,
    output_xform: str,
    runner: Runner | None = None,
) -> MriHiresRegisterOutputs:
    """
    A tool for high-resolution registration for Freesurfer images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hires_labeling: The high resolution labeling input file.
        input_intensity: The input intensity file.
        input_aseg: The input aseg file.
        output_xform: The output transform file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriHiresRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_HIRES_REGISTER_METADATA)
    params = mri_hires_register_params(hires_labeling=hires_labeling, input_intensity=input_intensity, input_aseg=input_aseg, output_xform=output_xform)
    return mri_hires_register_execute(params, execution)


__all__ = [
    "MRI_HIRES_REGISTER_METADATA",
    "MriHiresRegisterOutputs",
    "MriHiresRegisterParameters",
    "mri_hires_register",
    "mri_hires_register_params",
]
