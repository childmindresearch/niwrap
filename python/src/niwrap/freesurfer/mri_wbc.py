# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_WBC_METADATA = Metadata(
    id="92584218abde258bddf747b7925b1c16f3270082.boutiques",
    name="mri_wbc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriWbcParameters = typing.TypedDict('MriWbcParameters', {
    "__STYX_TYPE__": typing.Literal["mri_wbc"],
    "functional_volume": InputPathType,
    "volume_mask": typing.NotRequired[InputPathType | None],
    "lh_functional_surface": InputPathType,
    "lh_surface": InputPathType,
    "lh_inflated": typing.NotRequired[InputPathType | None],
    "lh_mask": typing.NotRequired[InputPathType | None],
    "lh_label": typing.NotRequired[InputPathType | None],
    "rh_functional_surface": InputPathType,
    "rh_surface": InputPathType,
    "rh_inflated": typing.NotRequired[InputPathType | None],
    "rh_mask": typing.NotRequired[InputPathType | None],
    "rh_label": typing.NotRequired[InputPathType | None],
    "rho_threshold": typing.NotRequired[float | None],
    "dist_threshold": typing.NotRequired[float | None],
    "threads": typing.NotRequired[float | None],
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
        "mri_wbc": mri_wbc_cargs,
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


class MriWbcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_wbc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_wbc_params(
    functional_volume: InputPathType,
    lh_functional_surface: InputPathType,
    lh_surface: InputPathType,
    rh_functional_surface: InputPathType,
    rh_surface: InputPathType,
    volume_mask: InputPathType | None = None,
    lh_inflated: InputPathType | None = None,
    lh_mask: InputPathType | None = None,
    lh_label: InputPathType | None = None,
    rh_inflated: InputPathType | None = None,
    rh_mask: InputPathType | None = None,
    rh_label: InputPathType | None = None,
    rho_threshold: float | None = None,
    dist_threshold: float | None = None,
    threads: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
) -> MriWbcParameters:
    """
    Build parameters.
    
    Args:
        functional_volume: Functional volume file.
        lh_functional_surface: Left hemisphere functional surface file.
        lh_surface: Left hemisphere surface file.
        rh_functional_surface: Right hemisphere functional surface file.
        rh_surface: Right hemisphere surface file.
        volume_mask: Mask for functional volume.
        lh_inflated: Optional left hemisphere inflated surface file.
        lh_mask: Mask for left hemisphere functional surface.
        lh_label: Label mask for left hemisphere functional surface.
        rh_inflated: Optional right hemisphere inflated surface file.
        rh_mask: Mask for right hemisphere functional surface.
        rh_label: Label mask for right hemisphere functional surface.
        rho_threshold: Rho threshold value.
        dist_threshold: Distance threshold value.
        threads: Number of threads to use.
        debug: Turn on debugging.
        checkopts: Check options and exit without running.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_wbc",
        "functional_volume": functional_volume,
        "lh_functional_surface": lh_functional_surface,
        "lh_surface": lh_surface,
        "rh_functional_surface": rh_functional_surface,
        "rh_surface": rh_surface,
        "debug": debug,
        "checkopts": checkopts,
    }
    if volume_mask is not None:
        params["volume_mask"] = volume_mask
    if lh_inflated is not None:
        params["lh_inflated"] = lh_inflated
    if lh_mask is not None:
        params["lh_mask"] = lh_mask
    if lh_label is not None:
        params["lh_label"] = lh_label
    if rh_inflated is not None:
        params["rh_inflated"] = rh_inflated
    if rh_mask is not None:
        params["rh_mask"] = rh_mask
    if rh_label is not None:
        params["rh_label"] = rh_label
    if rho_threshold is not None:
        params["rho_threshold"] = rho_threshold
    if dist_threshold is not None:
        params["dist_threshold"] = dist_threshold
    if threads is not None:
        params["threads"] = threads
    return params


def mri_wbc_cargs(
    params: MriWbcParameters,
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
    cargs.append("mri_wbc")
    cargs.extend([
        "--fvol",
        execution.input_file(params.get("functional_volume"))
    ])
    if params.get("volume_mask") is not None:
        cargs.extend([
            "--volmask",
            execution.input_file(params.get("volume_mask"))
        ])
    cargs.extend([
        "--lh",
        execution.input_file(params.get("lh_functional_surface"))
    ])
    cargs.extend([
        "--lh",
        execution.input_file(params.get("lh_surface"))
    ])
    if params.get("lh_inflated") is not None:
        cargs.extend([
            "--lh",
            execution.input_file(params.get("lh_inflated"))
        ])
    if params.get("lh_mask") is not None:
        cargs.extend([
            "--lhmask",
            execution.input_file(params.get("lh_mask"))
        ])
    if params.get("lh_label") is not None:
        cargs.extend([
            "--lhlabel",
            execution.input_file(params.get("lh_label"))
        ])
    cargs.extend([
        "--rh",
        execution.input_file(params.get("rh_functional_surface"))
    ])
    cargs.extend([
        "--rh",
        execution.input_file(params.get("rh_surface"))
    ])
    if params.get("rh_inflated") is not None:
        cargs.extend([
            "--rh",
            execution.input_file(params.get("rh_inflated"))
        ])
    if params.get("rh_mask") is not None:
        cargs.extend([
            "--rhmask",
            execution.input_file(params.get("rh_mask"))
        ])
    if params.get("rh_label") is not None:
        cargs.extend([
            "--rhlabel",
            execution.input_file(params.get("rh_label"))
        ])
    if params.get("rho_threshold") is not None:
        cargs.extend([
            "--rho",
            str(params.get("rho_threshold"))
        ])
    if params.get("dist_threshold") is not None:
        cargs.extend([
            "--dist",
            str(params.get("dist_threshold"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    return cargs


def mri_wbc_outputs(
    params: MriWbcParameters,
    execution: Execution,
) -> MriWbcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriWbcOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_wbc_execute(
    params: MriWbcParameters,
    execution: Execution,
) -> MriWbcOutputs:
    """
    A tool for working with functional brain imaging data on surfaces and volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriWbcOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_wbc_cargs(params, execution)
    ret = mri_wbc_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_wbc(
    functional_volume: InputPathType,
    lh_functional_surface: InputPathType,
    lh_surface: InputPathType,
    rh_functional_surface: InputPathType,
    rh_surface: InputPathType,
    volume_mask: InputPathType | None = None,
    lh_inflated: InputPathType | None = None,
    lh_mask: InputPathType | None = None,
    lh_label: InputPathType | None = None,
    rh_inflated: InputPathType | None = None,
    rh_mask: InputPathType | None = None,
    rh_label: InputPathType | None = None,
    rho_threshold: float | None = None,
    dist_threshold: float | None = None,
    threads: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MriWbcOutputs:
    """
    A tool for working with functional brain imaging data on surfaces and volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        functional_volume: Functional volume file.
        lh_functional_surface: Left hemisphere functional surface file.
        lh_surface: Left hemisphere surface file.
        rh_functional_surface: Right hemisphere functional surface file.
        rh_surface: Right hemisphere surface file.
        volume_mask: Mask for functional volume.
        lh_inflated: Optional left hemisphere inflated surface file.
        lh_mask: Mask for left hemisphere functional surface.
        lh_label: Label mask for left hemisphere functional surface.
        rh_inflated: Optional right hemisphere inflated surface file.
        rh_mask: Mask for right hemisphere functional surface.
        rh_label: Label mask for right hemisphere functional surface.
        rho_threshold: Rho threshold value.
        dist_threshold: Distance threshold value.
        threads: Number of threads to use.
        debug: Turn on debugging.
        checkopts: Check options and exit without running.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriWbcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_WBC_METADATA)
    params = mri_wbc_params(functional_volume=functional_volume, volume_mask=volume_mask, lh_functional_surface=lh_functional_surface, lh_surface=lh_surface, lh_inflated=lh_inflated, lh_mask=lh_mask, lh_label=lh_label, rh_functional_surface=rh_functional_surface, rh_surface=rh_surface, rh_inflated=rh_inflated, rh_mask=rh_mask, rh_label=rh_label, rho_threshold=rho_threshold, dist_threshold=dist_threshold, threads=threads, debug=debug, checkopts=checkopts)
    return mri_wbc_execute(params, execution)


__all__ = [
    "MRI_WBC_METADATA",
    "MriWbcOutputs",
    "MriWbcParameters",
    "mri_wbc",
    "mri_wbc_params",
]
