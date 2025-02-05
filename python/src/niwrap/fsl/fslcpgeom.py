# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLCPGEOM_METADATA = Metadata(
    id="abfea41c33a7487bc5c6fba058aaad8f45e8d06a.boutiques",
    name="fslcpgeom",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslcpgeomParameters = typing.TypedDict('FslcpgeomParameters', {
    "__STYX_TYPE__": typing.Literal["fslcpgeom"],
    "source_file": InputPathType,
    "destination_file": InputPathType,
    "dimensions_flag": bool,
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
        "fslcpgeom": fslcpgeom_cargs,
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


class FslcpgeomOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcpgeom(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslcpgeom_params(
    source_file: InputPathType,
    destination_file: InputPathType,
    dimensions_flag: bool = False,
) -> FslcpgeomParameters:
    """
    Build parameters.
    
    Args:
        source_file: Source image file (e.g. img1.nii.gz).
        destination_file: Destination image file (e.g. img2.nii.gz).
        dimensions_flag: Don't copy image dimensions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslcpgeom",
        "source_file": source_file,
        "destination_file": destination_file,
        "dimensions_flag": dimensions_flag,
    }
    return params


def fslcpgeom_cargs(
    params: FslcpgeomParameters,
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
    cargs.append("fslcpgeom")
    cargs.append(execution.input_file(params.get("source_file")))
    cargs.append(execution.input_file(params.get("destination_file")))
    if params.get("dimensions_flag"):
        cargs.append("-d")
    return cargs


def fslcpgeom_outputs(
    params: FslcpgeomParameters,
    execution: Execution,
) -> FslcpgeomOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslcpgeomOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslcpgeom_execute(
    params: FslcpgeomParameters,
    execution: Execution,
) -> FslcpgeomOutputs:
    """
    FSL tool to copy image geometry from one file to another.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslcpgeomOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslcpgeom_cargs(params, execution)
    ret = fslcpgeom_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslcpgeom(
    source_file: InputPathType,
    destination_file: InputPathType,
    dimensions_flag: bool = False,
    runner: Runner | None = None,
) -> FslcpgeomOutputs:
    """
    FSL tool to copy image geometry from one file to another.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        source_file: Source image file (e.g. img1.nii.gz).
        destination_file: Destination image file (e.g. img2.nii.gz).
        dimensions_flag: Don't copy image dimensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslcpgeomOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCPGEOM_METADATA)
    params = fslcpgeom_params(source_file=source_file, destination_file=destination_file, dimensions_flag=dimensions_flag)
    return fslcpgeom_execute(params, execution)


__all__ = [
    "FSLCPGEOM_METADATA",
    "FslcpgeomOutputs",
    "FslcpgeomParameters",
    "fslcpgeom",
    "fslcpgeom_params",
]
