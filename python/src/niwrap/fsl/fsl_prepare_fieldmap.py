# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_PREPARE_FIELDMAP_METADATA = Metadata(
    id="5c59e0c61ed0a1488f719131a2d741d2cf4930a5.boutiques",
    name="fsl_prepare_fieldmap",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslPrepareFieldmapParameters = typing.TypedDict('FslPrepareFieldmapParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_prepare_fieldmap"],
    "scanner": str,
    "phase_image": InputPathType,
    "magnitude_image": InputPathType,
    "out_image": str,
    "delta_te": float,
    "nocheck_flag": bool,
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
        "fsl_prepare_fieldmap": fsl_prepare_fieldmap_cargs,
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
        "fsl_prepare_fieldmap": fsl_prepare_fieldmap_outputs,
    }.get(t)


class FslPrepareFieldmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_prepare_fieldmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_fieldmap: OutputPathType
    """The output fieldmap in rad/s format"""


def fsl_prepare_fieldmap_params(
    scanner: str,
    phase_image: InputPathType,
    magnitude_image: InputPathType,
    out_image: str,
    delta_te: float,
    nocheck_flag: bool = False,
) -> FslPrepareFieldmapParameters:
    """
    Build parameters.
    
    Args:
        scanner: Scanner type (must be SIEMENS).
        phase_image: Phase image file.
        magnitude_image: Magnitude image file (should be Brain Extracted).
        out_image: Output fieldmap image file.
        delta_te: Echo time difference of the fieldmap sequence in milliseconds.
        nocheck_flag: Suppress automatic sanity checking of image\
            size/range/dimensions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_prepare_fieldmap",
        "scanner": scanner,
        "phase_image": phase_image,
        "magnitude_image": magnitude_image,
        "out_image": out_image,
        "delta_te": delta_te,
        "nocheck_flag": nocheck_flag,
    }
    return params


def fsl_prepare_fieldmap_cargs(
    params: FslPrepareFieldmapParameters,
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
    cargs.append("fsl_prepare_fieldmap")
    cargs.append(params.get("scanner"))
    cargs.append(execution.input_file(params.get("phase_image")))
    cargs.append(execution.input_file(params.get("magnitude_image")))
    cargs.append(params.get("out_image"))
    cargs.append(str(params.get("delta_te")))
    if params.get("nocheck_flag"):
        cargs.append("--nocheck")
    return cargs


def fsl_prepare_fieldmap_outputs(
    params: FslPrepareFieldmapParameters,
    execution: Execution,
) -> FslPrepareFieldmapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslPrepareFieldmapOutputs(
        root=execution.output_file("."),
        output_fieldmap=execution.output_file(params.get("out_image") + ".nii.gz"),
    )
    return ret


def fsl_prepare_fieldmap_execute(
    params: FslPrepareFieldmapParameters,
    execution: Execution,
) -> FslPrepareFieldmapOutputs:
    """
    Prepares a fieldmap suitable for FEAT from SIEMENS data and saves output in
    rad/s format.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslPrepareFieldmapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsl_prepare_fieldmap_cargs(params, execution)
    ret = fsl_prepare_fieldmap_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_prepare_fieldmap(
    scanner: str,
    phase_image: InputPathType,
    magnitude_image: InputPathType,
    out_image: str,
    delta_te: float,
    nocheck_flag: bool = False,
    runner: Runner | None = None,
) -> FslPrepareFieldmapOutputs:
    """
    Prepares a fieldmap suitable for FEAT from SIEMENS data and saves output in
    rad/s format.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        scanner: Scanner type (must be SIEMENS).
        phase_image: Phase image file.
        magnitude_image: Magnitude image file (should be Brain Extracted).
        out_image: Output fieldmap image file.
        delta_te: Echo time difference of the fieldmap sequence in milliseconds.
        nocheck_flag: Suppress automatic sanity checking of image\
            size/range/dimensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslPrepareFieldmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_PREPARE_FIELDMAP_METADATA)
    params = fsl_prepare_fieldmap_params(scanner=scanner, phase_image=phase_image, magnitude_image=magnitude_image, out_image=out_image, delta_te=delta_te, nocheck_flag=nocheck_flag)
    return fsl_prepare_fieldmap_execute(params, execution)


__all__ = [
    "FSL_PREPARE_FIELDMAP_METADATA",
    "FslPrepareFieldmapOutputs",
    "FslPrepareFieldmapParameters",
    "fsl_prepare_fieldmap",
    "fsl_prepare_fieldmap_params",
]
