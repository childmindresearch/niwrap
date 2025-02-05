# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_COMPUTE_VOLUME_FRACTIONS_METADATA = Metadata(
    id="02961ba1db8b265f07c25a08461891b1caa9c54c.boutiques",
    name="mris_compute_volume_fractions",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisComputeVolumeFractionsParameters = typing.TypedDict('MrisComputeVolumeFractionsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_compute_volume_fractions"],
    "volume_file": InputPathType,
    "surface_file": InputPathType,
    "accuracy": float,
    "output_file": str,
    "debug": bool,
    "checkopts": bool,
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
        "mris_compute_volume_fractions": mris_compute_volume_fractions_cargs,
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
        "mris_compute_volume_fractions": mris_compute_volume_fractions_outputs,
    }
    return vt.get(t)


class MrisComputeVolumeFractionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_volume_fractions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """The output volume file containing the computed fractions."""


def mris_compute_volume_fractions_params(
    volume_file: InputPathType,
    surface_file: InputPathType,
    accuracy: float,
    output_file: str,
    debug: bool = False,
    checkopts: bool = False,
) -> MrisComputeVolumeFractionsParameters:
    """
    Build parameters.
    
    Args:
        volume_file: Input volume file.
        surface_file: Input surface file.
        accuracy: Required accuracy.
        output_file: Output volume file for the fractions.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_compute_volume_fractions",
        "volume_file": volume_file,
        "surface_file": surface_file,
        "accuracy": accuracy,
        "output_file": output_file,
        "debug": debug,
        "checkopts": checkopts,
    }
    return params


def mris_compute_volume_fractions_cargs(
    params: MrisComputeVolumeFractionsParameters,
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
    cargs.append("mris_compute_volume_fractions")
    cargs.extend([
        "--vol",
        execution.input_file(params.get("volume_file"))
    ])
    cargs.extend([
        "--surf",
        execution.input_file(params.get("surface_file"))
    ])
    cargs.extend([
        "--acc",
        str(params.get("accuracy"))
    ])
    cargs.extend([
        "--out",
        params.get("output_file")
    ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    return cargs


def mris_compute_volume_fractions_outputs(
    params: MrisComputeVolumeFractionsParameters,
    execution: Execution,
) -> MrisComputeVolumeFractionsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisComputeVolumeFractionsOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_file")),
    )
    return ret


def mris_compute_volume_fractions_execute(
    params: MrisComputeVolumeFractionsParameters,
    execution: Execution,
) -> MrisComputeVolumeFractionsOutputs:
    """
    Computes volume fractions based on a given surface and volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisComputeVolumeFractionsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_compute_volume_fractions_cargs(params, execution)
    ret = mris_compute_volume_fractions_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_compute_volume_fractions(
    volume_file: InputPathType,
    surface_file: InputPathType,
    accuracy: float,
    output_file: str,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MrisComputeVolumeFractionsOutputs:
    """
    Computes volume fractions based on a given surface and volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volume_file: Input volume file.
        surface_file: Input surface file.
        accuracy: Required accuracy.
        output_file: Output volume file for the fractions.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeVolumeFractionsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_VOLUME_FRACTIONS_METADATA)
    params = mris_compute_volume_fractions_params(volume_file=volume_file, surface_file=surface_file, accuracy=accuracy, output_file=output_file, debug=debug, checkopts=checkopts)
    return mris_compute_volume_fractions_execute(params, execution)


__all__ = [
    "MRIS_COMPUTE_VOLUME_FRACTIONS_METADATA",
    "MrisComputeVolumeFractionsOutputs",
    "MrisComputeVolumeFractionsParameters",
    "mris_compute_volume_fractions",
    "mris_compute_volume_fractions_params",
]
