# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__DJUNCT_MONTAGE_COORDINATOR_METADATA = Metadata(
    id="9c2cbb473d95421a680be52f18d9f90f2ec86dfb.boutiques",
    name="@djunct_montage_coordinator",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDjunctMontageCoordinatorParameters = typing.TypedDict('VDjunctMontageCoordinatorParameters', {
    "__STYX_TYPE__": typing.Literal["@djunct_montage_coordinator"],
    "input_file": InputPathType,
    "montx": float,
    "monty": float,
    "out_xyz": bool,
    "help": bool,
    "version": bool,
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
        "@djunct_montage_coordinator": v__djunct_montage_coordinator_cargs,
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
        "@djunct_montage_coordinator": v__djunct_montage_coordinator_outputs,
    }.get(t)


class VDjunctMontageCoordinatorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_montage_coordinator(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_coords: OutputPathType
    """Output coordinates (IJK or XYZ) for the montage setup."""


def v__djunct_montage_coordinator_params(
    input_file: InputPathType,
    montx: float,
    monty: float,
    out_xyz: bool = False,
    help_: bool = False,
    version: bool = False,
) -> VDjunctMontageCoordinatorParameters:
    """
    Build parameters.
    
    Args:
        input_file: Name of input dataset.
        montx: Montage dimension: number of panels along x-axis (i.e., number\
            of cols).
        monty: Montage dimension: number of panels along y-axis (i.e., number\
            of rows).
        out_xyz: Make program output 'X Y Z' values.
        help_: See helpfile.
        version: See version number.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@djunct_montage_coordinator",
        "input_file": input_file,
        "montx": montx,
        "monty": monty,
        "out_xyz": out_xyz,
        "help": help_,
        "version": version,
    }
    return params


def v__djunct_montage_coordinator_cargs(
    params: VDjunctMontageCoordinatorParameters,
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
    cargs.append("@djunct_montage_coordinator")
    cargs.extend([
        "-inset",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-montx",
        str(params.get("montx"))
    ])
    cargs.extend([
        "-monty",
        str(params.get("monty"))
    ])
    if params.get("out_xyz"):
        cargs.append("-out_xyz")
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-ver")
    return cargs


def v__djunct_montage_coordinator_outputs(
    params: VDjunctMontageCoordinatorParameters,
    execution: Execution,
) -> VDjunctMontageCoordinatorOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDjunctMontageCoordinatorOutputs(
        root=execution.output_file("."),
        output_coords=execution.output_file("output.txt"),
    )
    return ret


def v__djunct_montage_coordinator_execute(
    params: VDjunctMontageCoordinatorParameters,
    execution: Execution,
) -> VDjunctMontageCoordinatorOutputs:
    """
    Small program to calculate how to evenly space a certain number of slices within
    each view plane of a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDjunctMontageCoordinatorOutputs`).
    """
    params = execution.params(params)
    cargs = v__djunct_montage_coordinator_cargs(params, execution)
    ret = v__djunct_montage_coordinator_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__djunct_montage_coordinator(
    input_file: InputPathType,
    montx: float,
    monty: float,
    out_xyz: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> VDjunctMontageCoordinatorOutputs:
    """
    Small program to calculate how to evenly space a certain number of slices within
    each view plane of a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Name of input dataset.
        montx: Montage dimension: number of panels along x-axis (i.e., number\
            of cols).
        monty: Montage dimension: number of panels along y-axis (i.e., number\
            of rows).
        out_xyz: Make program output 'X Y Z' values.
        help_: See helpfile.
        version: See version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctMontageCoordinatorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_MONTAGE_COORDINATOR_METADATA)
    params = v__djunct_montage_coordinator_params(input_file=input_file, montx=montx, monty=monty, out_xyz=out_xyz, help_=help_, version=version)
    return v__djunct_montage_coordinator_execute(params, execution)


__all__ = [
    "VDjunctMontageCoordinatorOutputs",
    "VDjunctMontageCoordinatorParameters",
    "V__DJUNCT_MONTAGE_COORDINATOR_METADATA",
    "v__djunct_montage_coordinator",
    "v__djunct_montage_coordinator_params",
]
