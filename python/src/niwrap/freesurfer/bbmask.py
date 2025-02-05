# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BBMASK_METADATA = Metadata(
    id="064153f645343fa44a6da922e9a35232f8ea8522.boutiques",
    name="bbmask",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
BbmaskParameters = typing.TypedDict('BbmaskParameters', {
    "__STYX_TYPE__": typing.Literal["bbmask"],
    "mask": list[InputPathType],
    "src_volumes": typing.NotRequired[list[InputPathType] | None],
    "npad": typing.NotRequired[float | None],
    "registration": typing.NotRequired[list[InputPathType] | None],
    "regheader": typing.NotRequired[InputPathType | None],
    "sub2src": typing.NotRequired[InputPathType | None],
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
        "bbmask": bbmask_cargs,
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
        "bbmask": bbmask_outputs,
    }
    return vt.get(t)


class BbmaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bbmask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mask_output_file: OutputPathType
    """Output mask volume"""
    src_output_file: OutputPathType
    """Output reduced volume(s)"""
    registration_output_file: OutputPathType
    """Output registration file"""
    regheader_output_file: OutputPathType
    """Output registration file from regheader"""
    sub2src_output_file: OutputPathType
    """Output file for sub2src registration"""


def bbmask_params(
    mask: list[InputPathType],
    src_volumes: list[InputPathType] | None = None,
    npad: float | None = None,
    registration: list[InputPathType] | None = None,
    regheader: InputPathType | None = None,
    sub2src: InputPathType | None = None,
) -> BbmaskParameters:
    """
    Build parameters.
    
    Args:
        mask: Input and output for the mask volume.
        src_volumes: Input and output volumes to be reduced to the bounding\
            box.
        npad: Number of voxels to expand the bounding box.
        registration: Input and output registration files.
        regheader: Output registration file from header.
        sub2src: Output file for sub-source registration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bbmask",
        "mask": mask,
    }
    if src_volumes is not None:
        params["src_volumes"] = src_volumes
    if npad is not None:
        params["npad"] = npad
    if registration is not None:
        params["registration"] = registration
    if regheader is not None:
        params["regheader"] = regheader
    if sub2src is not None:
        params["sub2src"] = sub2src
    return params


def bbmask_cargs(
    params: BbmaskParameters,
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
    cargs.append("bbmask")
    cargs.extend([
        "--mask",
        *[execution.input_file(f) for f in params.get("mask")]
    ])
    if params.get("src_volumes") is not None:
        cargs.extend([
            "--src",
            *[execution.input_file(f) for f in params.get("src_volumes")]
        ])
    if params.get("npad") is not None:
        cargs.extend([
            "--npad",
            str(params.get("npad"))
        ])
    if params.get("registration") is not None:
        cargs.extend([
            "--reg",
            *[execution.input_file(f) for f in params.get("registration")]
        ])
    if params.get("regheader") is not None:
        cargs.extend([
            "--regheader",
            execution.input_file(params.get("regheader"))
        ])
    if params.get("sub2src") is not None:
        cargs.extend([
            "--sub2src",
            execution.input_file(params.get("sub2src"))
        ])
    return cargs


def bbmask_outputs(
    params: BbmaskParameters,
    execution: Execution,
) -> BbmaskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BbmaskOutputs(
        root=execution.output_file("."),
        mask_output_file=execution.output_file("[MASK_OUTPUT]"),
        src_output_file=execution.output_file("[SRC_OUTPUT]"),
        registration_output_file=execution.output_file("[REG_OUTPUT]"),
        regheader_output_file=execution.output_file("[REG_HEADER_OUTPUT]"),
        sub2src_output_file=execution.output_file("[SUB2SRC_OUTPUT]"),
    )
    return ret


def bbmask_execute(
    params: BbmaskParameters,
    execution: Execution,
) -> BbmaskOutputs:
    """
    Tool to create a volume with a smaller field of view by creating a bounding box
    that encompasses a mask.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BbmaskOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = bbmask_cargs(params, execution)
    ret = bbmask_outputs(params, execution)
    execution.run(cargs)
    return ret


def bbmask(
    mask: list[InputPathType],
    src_volumes: list[InputPathType] | None = None,
    npad: float | None = None,
    registration: list[InputPathType] | None = None,
    regheader: InputPathType | None = None,
    sub2src: InputPathType | None = None,
    runner: Runner | None = None,
) -> BbmaskOutputs:
    """
    Tool to create a volume with a smaller field of view by creating a bounding box
    that encompasses a mask.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mask: Input and output for the mask volume.
        src_volumes: Input and output volumes to be reduced to the bounding\
            box.
        npad: Number of voxels to expand the bounding box.
        registration: Input and output registration files.
        regheader: Output registration file from header.
        sub2src: Output file for sub-source registration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BbmaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BBMASK_METADATA)
    params = bbmask_params(mask=mask, src_volumes=src_volumes, npad=npad, registration=registration, regheader=regheader, sub2src=sub2src)
    return bbmask_execute(params, execution)


__all__ = [
    "BBMASK_METADATA",
    "BbmaskOutputs",
    "BbmaskParameters",
    "bbmask",
    "bbmask_params",
]
