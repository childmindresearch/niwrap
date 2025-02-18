# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_FUSE_SEGMENTATIONS_METADATA = Metadata(
    id="b42ea2ffd32b62f852b2f074e21005b3ac5e5519.boutiques",
    name="mri_fuse_segmentations",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriFuseSegmentationsParameters = typing.TypedDict('MriFuseSegmentationsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_fuse_segmentations"],
    "asegs": list[InputPathType],
    "nocc_asegs": list[InputPathType],
    "norm_volumes": list[InputPathType],
    "transforms": typing.NotRequired[list[InputPathType] | None],
    "sigma": typing.NotRequired[float | None],
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
        "mri_fuse_segmentations": mri_fuse_segmentations_cargs,
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
        "mri_fuse_segmentations": mri_fuse_segmentations_outputs,
    }.get(t)


class MriFuseSegmentationsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fuse_segmentations(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Resulting fused segmentation as aseg.fused.mgz file"""


def mri_fuse_segmentations_params(
    asegs: list[InputPathType],
    nocc_asegs: list[InputPathType],
    norm_volumes: list[InputPathType],
    input_file: InputPathType,
    transforms: list[InputPathType] | None = None,
    sigma: float | None = 3.0,
) -> MriFuseSegmentationsParameters:
    """
    Build parameters.
    
    Args:
        asegs: Path to aseg.mgz files, one per TP.
        nocc_asegs: Path to aseg.auto_noCCseg.mgz files without CC labels, one\
            per TP.
        norm_volumes: Path to norm.mgz files, one per TP.
        input_file: Input norm.mgz file.
        transforms: Transform files from each TP to the input norm.mgz, can be\
            LTA, M3Z or identity.nofile.
        sigma: Cross-time sigma (default 3.0).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_fuse_segmentations",
        "asegs": asegs,
        "nocc_asegs": nocc_asegs,
        "norm_volumes": norm_volumes,
        "input_file": input_file,
    }
    if transforms is not None:
        params["transforms"] = transforms
    if sigma is not None:
        params["sigma"] = sigma
    return params


def mri_fuse_segmentations_cargs(
    params: MriFuseSegmentationsParameters,
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
    cargs.append("mri_fuse_segmentations")
    cargs.extend([
        "-a",
        *[execution.input_file(f) for f in params.get("asegs")]
    ])
    cargs.extend([
        "-c",
        *[execution.input_file(f) for f in params.get("nocc_asegs")]
    ])
    cargs.extend([
        "-n",
        *[execution.input_file(f) for f in params.get("norm_volumes")]
    ])
    if params.get("transforms") is not None:
        cargs.extend([
            "-t",
            *[execution.input_file(f) for f in params.get("transforms")]
        ])
    if params.get("sigma") is not None:
        cargs.extend([
            "-s",
            str(params.get("sigma"))
        ])
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append("[OUTPUT]")
    return cargs


def mri_fuse_segmentations_outputs(
    params: MriFuseSegmentationsParameters,
    execution: Execution,
) -> MriFuseSegmentationsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFuseSegmentationsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[OUTPUT]"),
    )
    return ret


def mri_fuse_segmentations_execute(
    params: MriFuseSegmentationsParameters,
    execution: Execution,
) -> MriFuseSegmentationsOutputs:
    """
    Fuse a set of segmentations (asegs) into an initial estimate of a longitudinal
    one.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFuseSegmentationsOutputs`).
    """
    params = execution.params(params)
    cargs = mri_fuse_segmentations_cargs(params, execution)
    ret = mri_fuse_segmentations_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_fuse_segmentations(
    asegs: list[InputPathType],
    nocc_asegs: list[InputPathType],
    norm_volumes: list[InputPathType],
    input_file: InputPathType,
    transforms: list[InputPathType] | None = None,
    sigma: float | None = 3.0,
    runner: Runner | None = None,
) -> MriFuseSegmentationsOutputs:
    """
    Fuse a set of segmentations (asegs) into an initial estimate of a longitudinal
    one.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        asegs: Path to aseg.mgz files, one per TP.
        nocc_asegs: Path to aseg.auto_noCCseg.mgz files without CC labels, one\
            per TP.
        norm_volumes: Path to norm.mgz files, one per TP.
        input_file: Input norm.mgz file.
        transforms: Transform files from each TP to the input norm.mgz, can be\
            LTA, M3Z or identity.nofile.
        sigma: Cross-time sigma (default 3.0).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFuseSegmentationsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FUSE_SEGMENTATIONS_METADATA)
    params = mri_fuse_segmentations_params(asegs=asegs, nocc_asegs=nocc_asegs, norm_volumes=norm_volumes, transforms=transforms, sigma=sigma, input_file=input_file)
    return mri_fuse_segmentations_execute(params, execution)


__all__ = [
    "MRI_FUSE_SEGMENTATIONS_METADATA",
    "MriFuseSegmentationsOutputs",
    "MriFuseSegmentationsParameters",
    "mri_fuse_segmentations",
    "mri_fuse_segmentations_params",
]
