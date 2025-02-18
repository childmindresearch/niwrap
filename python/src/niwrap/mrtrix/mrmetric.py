# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRMETRIC_METADATA = Metadata(
    id="68993bab707571cc9c043c8d06d2a16330445585.boutiques",
    name="mrmetric",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MrmetricConfigParameters = typing.TypedDict('MrmetricConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MrmetricParameters = typing.TypedDict('MrmetricParameters', {
    "__STYX_TYPE__": typing.Literal["mrmetric"],
    "space": typing.NotRequired[str | None],
    "interp": typing.NotRequired[str | None],
    "metric": typing.NotRequired[str | None],
    "mask1": typing.NotRequired[InputPathType | None],
    "mask2": typing.NotRequired[InputPathType | None],
    "nonormalisation": bool,
    "overlap": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrmetricConfigParameters] | None],
    "help": bool,
    "version": bool,
    "image1": InputPathType,
    "image2": InputPathType,
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
        "mrmetric": mrmetric_cargs,
        "config": mrmetric_config_cargs,
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
    }.get(t)


def mrmetric_config_params(
    key: str,
    value: str,
) -> MrmetricConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def mrmetric_config_cargs(
    params: MrmetricConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class MrmetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrmetric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mrmetric_params(
    image1: InputPathType,
    image2: InputPathType,
    space: str | None = None,
    interp: str | None = None,
    metric: str | None = None,
    mask1: InputPathType | None = None,
    mask2: InputPathType | None = None,
    nonormalisation: bool = False,
    overlap: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrmetricConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrmetricParameters:
    """
    Build parameters.
    
    Args:
        image1: the first input image.
        image2: the second input image.
        space: voxel (default): per voxel image1: scanner space of image 1\
            image2: scanner space of image 2 average: scanner space of the average\
            affine transformation of image 1 and 2.
        interp: set the interpolation method to use when reslicing (choices:\
            nearest, linear, cubic, sinc. Default: linear).
        metric: define the dissimilarity metric used to calculate the cost.\
            Choices: diff (squared differences), cc (non-normalised negative cross\
            correlation aka negative cross covariance). Default: diff). cc is only\
            implemented for -space average and -interp linear and cubic.
        mask1: mask for image 1.
        mask2: mask for image 2.
        nonormalisation: do not normalise the dissimilarity metric to the\
            number of voxels.
        overlap: output number of voxels that were used.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mrmetric",
        "nonormalisation": nonormalisation,
        "overlap": overlap,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "image1": image1,
        "image2": image2,
    }
    if space is not None:
        params["space"] = space
    if interp is not None:
        params["interp"] = interp
    if metric is not None:
        params["metric"] = metric
    if mask1 is not None:
        params["mask1"] = mask1
    if mask2 is not None:
        params["mask2"] = mask2
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrmetric_cargs(
    params: MrmetricParameters,
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
    cargs.append("mrmetric")
    if params.get("space") is not None:
        cargs.extend([
            "-space",
            params.get("space")
        ])
    if params.get("interp") is not None:
        cargs.extend([
            "-interp",
            params.get("interp")
        ])
    if params.get("metric") is not None:
        cargs.extend([
            "-metric",
            params.get("metric")
        ])
    if params.get("mask1") is not None:
        cargs.extend([
            "-mask1",
            execution.input_file(params.get("mask1"))
        ])
    if params.get("mask2") is not None:
        cargs.extend([
            "-mask2",
            execution.input_file(params.get("mask2"))
        ])
    if params.get("nonormalisation"):
        cargs.append("-nonormalisation")
    if params.get("overlap"):
        cargs.append("-overlap")
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("image1")))
    cargs.append(execution.input_file(params.get("image2")))
    return cargs


def mrmetric_outputs(
    params: MrmetricParameters,
    execution: Execution,
) -> MrmetricOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrmetricOutputs(
        root=execution.output_file("."),
    )
    return ret


def mrmetric_execute(
    params: MrmetricParameters,
    execution: Execution,
) -> MrmetricOutputs:
    """
    Computes a dissimilarity metric between two images.
    
    Currently only the mean squared difference is fully implemented.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrmetricOutputs`).
    """
    params = execution.params(params)
    cargs = mrmetric_cargs(params, execution)
    ret = mrmetric_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrmetric(
    image1: InputPathType,
    image2: InputPathType,
    space: str | None = None,
    interp: str | None = None,
    metric: str | None = None,
    mask1: InputPathType | None = None,
    mask2: InputPathType | None = None,
    nonormalisation: bool = False,
    overlap: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrmetricConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrmetricOutputs:
    """
    Computes a dissimilarity metric between two images.
    
    Currently only the mean squared difference is fully implemented.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        image1: the first input image.
        image2: the second input image.
        space: voxel (default): per voxel image1: scanner space of image 1\
            image2: scanner space of image 2 average: scanner space of the average\
            affine transformation of image 1 and 2.
        interp: set the interpolation method to use when reslicing (choices:\
            nearest, linear, cubic, sinc. Default: linear).
        metric: define the dissimilarity metric used to calculate the cost.\
            Choices: diff (squared differences), cc (non-normalised negative cross\
            correlation aka negative cross covariance). Default: diff). cc is only\
            implemented for -space average and -interp linear and cubic.
        mask1: mask for image 1.
        mask2: mask for image 2.
        nonormalisation: do not normalise the dissimilarity metric to the\
            number of voxels.
        overlap: output number of voxels that were used.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrmetricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRMETRIC_METADATA)
    params = mrmetric_params(space=space, interp=interp, metric=metric, mask1=mask1, mask2=mask2, nonormalisation=nonormalisation, overlap=overlap, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, image1=image1, image2=image2)
    return mrmetric_execute(params, execution)


__all__ = [
    "MRMETRIC_METADATA",
    "MrmetricConfigParameters",
    "MrmetricOutputs",
    "MrmetricParameters",
    "mrmetric",
    "mrmetric_config_params",
    "mrmetric_params",
]
