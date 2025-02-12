# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRFILTER_METADATA = Metadata(
    id="3bb2ab8375a99185acaeac0f9e608829bff091ac.boutiques",
    name="mrfilter",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MrfilterVariousStringParameters = typing.TypedDict('MrfilterVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
MrfilterVariousFileParameters = typing.TypedDict('MrfilterVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
MrfilterConfigParameters = typing.TypedDict('MrfilterConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MrfilterParameters = typing.TypedDict('MrfilterParameters', {
    "__STYX_TYPE__": typing.Literal["mrfilter"],
    "axes": typing.NotRequired[list[int] | None],
    "inverse": bool,
    "magnitude": bool,
    "centre_zero": bool,
    "stdev": typing.NotRequired[list[float] | None],
    "magnitude_1": bool,
    "scanner": bool,
    "extent": typing.NotRequired[list[int] | None],
    "extent_1": typing.NotRequired[list[int] | None],
    "stdev_1": typing.NotRequired[list[float] | None],
    "fwhm": typing.NotRequired[list[float] | None],
    "extent_2": typing.NotRequired[list[int] | None],
    "zupper": typing.NotRequired[float | None],
    "zlower": typing.NotRequired[float | None],
    "bridge": typing.NotRequired[int | None],
    "maskin": typing.NotRequired[InputPathType | None],
    "maskout": typing.NotRequired[str | None],
    "strides": typing.NotRequired[typing.Union[MrfilterVariousStringParameters, MrfilterVariousFileParameters] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrfilterConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "filter": str,
    "output": str,
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
        "mrfilter": mrfilter_cargs,
        "VariousString": mrfilter_various_string_cargs,
        "VariousFile": mrfilter_various_file_cargs,
        "config": mrfilter_config_cargs,
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
        "mrfilter": mrfilter_outputs,
    }.get(t)


def mrfilter_various_string_params(
    obj: str,
) -> MrfilterVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def mrfilter_various_string_cargs(
    params: MrfilterVariousStringParameters,
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
    cargs.append(params.get("obj"))
    return cargs


def mrfilter_various_file_params(
    obj: InputPathType,
) -> MrfilterVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def mrfilter_various_file_cargs(
    params: MrfilterVariousFileParameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def mrfilter_config_params(
    key: str,
    value: str,
) -> MrfilterConfigParameters:
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


def mrfilter_config_cargs(
    params: MrfilterConfigParameters,
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


class MrfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""
    maskout: OutputPathType | None
    """Output a refined mask based on a spatially coherent region with normal
    intensity range. """


def mrfilter_params(
    input_: InputPathType,
    filter_: str,
    output: str,
    axes: list[int] | None = None,
    inverse: bool = False,
    magnitude: bool = False,
    centre_zero: bool = False,
    stdev: list[float] | None = None,
    magnitude_1: bool = False,
    scanner: bool = False,
    extent: list[int] | None = None,
    extent_1: list[int] | None = None,
    stdev_1: list[float] | None = None,
    fwhm: list[float] | None = None,
    extent_2: list[int] | None = None,
    zupper: float | None = None,
    zlower: float | None = None,
    bridge: int | None = None,
    maskin: InputPathType | None = None,
    maskout: str | None = None,
    strides: typing.Union[MrfilterVariousStringParameters, MrfilterVariousFileParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrfilterConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrfilterParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image.
        filter_: the type of filter to be applied.
        output: the output image.
        axes: the axes along which to apply the Fourier Transform. By default,\
            the transform is applied along the three spatial axes. Provide as a\
            comma-separate list of axis indices.
        inverse: apply the inverse FFT.
        magnitude: output a magnitude image rather than a complex-valued image.
        centre_zero: re-arrange the FFT results so that the zero-frequency\
            component appears in the centre of the image, rather than at the edges.
        stdev: the standard deviation of the Gaussian kernel used to smooth the\
            input image (in mm). The image is smoothed to reduced large spurious\
            gradients caused by noise. Use this option to override the default\
            stdev of 1 voxel. This can be specified either as a single value to be\
            used for all 3 axes, or as a comma-separated list of 3 values, one for\
            each axis.
        magnitude_1: output the gradient magnitude, rather than the default\
            x,y,z components.
        scanner: define the gradient with respect to the scanner coordinate\
            frame of reference.
        extent: specify extent of median filtering neighbourhood in voxels.\
            This can be specified either as a single value to be used for all 3\
            axes, or as a comma-separated list of 3 values, one for each axis\
            (default: 3x3x3).
        extent_1: specify extent of normalisation filtering neighbourhood in\
            voxels. This can be specified either as a single value to be used for\
            all 3 axes, or as a comma-separated list of 3 values, one for each axis\
            (default: 3x3x3).
        stdev_1: apply Gaussian smoothing with the specified standard\
            deviation. The standard deviation is defined in mm (Default 1 voxel).\
            This can be specified either as a single value to be used for all axes,\
            or as a comma-separated list of the stdev for each axis.
        fwhm: apply Gaussian smoothing with the specified full-width half\
            maximum. The FWHM is defined in mm (Default 1 voxel * 2.3548). This can\
            be specified either as a single value to be used for all axes, or as a\
            comma-separated list of the FWHM for each axis.
        extent_2: specify the extent (width) of kernel size in voxels. This can\
            be specified either as a single value to be used for all axes, or as a\
            comma-separated list of the extent for each axis. The default extent is\
            2 * ceil(2.5 * stdev / voxel_size) - 1.
        zupper: define high intensity outliers: default: 2.5.
        zlower: define low intensity outliers: default: 2.5.
        bridge: number of voxels to gap to fill holes in mask: default: 4.
        maskin: initial mask that defines the maximum spatial extent and the\
            region from which to smaple the intensity range.
        maskout: Output a refined mask based on a spatially coherent region\
            with normal intensity range.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
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
        "__STYXTYPE__": "mrfilter",
        "inverse": inverse,
        "magnitude": magnitude,
        "centre_zero": centre_zero,
        "magnitude_1": magnitude_1,
        "scanner": scanner,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "filter": filter_,
        "output": output,
    }
    if axes is not None:
        params["axes"] = axes
    if stdev is not None:
        params["stdev"] = stdev
    if extent is not None:
        params["extent"] = extent
    if extent_1 is not None:
        params["extent_1"] = extent_1
    if stdev_1 is not None:
        params["stdev_1"] = stdev_1
    if fwhm is not None:
        params["fwhm"] = fwhm
    if extent_2 is not None:
        params["extent_2"] = extent_2
    if zupper is not None:
        params["zupper"] = zupper
    if zlower is not None:
        params["zlower"] = zlower
    if bridge is not None:
        params["bridge"] = bridge
    if maskin is not None:
        params["maskin"] = maskin
    if maskout is not None:
        params["maskout"] = maskout
    if strides is not None:
        params["strides"] = strides
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrfilter_cargs(
    params: MrfilterParameters,
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
    cargs.append("mrfilter")
    if params.get("axes") is not None:
        cargs.extend([
            "-axes",
            *map(str, params.get("axes"))
        ])
    if params.get("inverse"):
        cargs.append("-inverse")
    if params.get("magnitude"):
        cargs.append("-magnitude")
    if params.get("centre_zero"):
        cargs.append("-centre_zero")
    if params.get("stdev") is not None:
        cargs.extend([
            "-stdev",
            ",".join(map(str, params.get("stdev")))
        ])
    if params.get("magnitude_1"):
        cargs.append("-magnitude")
    if params.get("scanner"):
        cargs.append("-scanner")
    if params.get("extent") is not None:
        cargs.extend([
            "-extent",
            ",".join(map(str, params.get("extent")))
        ])
    if params.get("extent_1") is not None:
        cargs.extend([
            "-extent",
            ",".join(map(str, params.get("extent_1")))
        ])
    if params.get("stdev_1") is not None:
        cargs.extend([
            "-stdev",
            ",".join(map(str, params.get("stdev_1")))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "-fwhm",
            ",".join(map(str, params.get("fwhm")))
        ])
    if params.get("extent_2") is not None:
        cargs.extend([
            "-extent",
            ",".join(map(str, params.get("extent_2")))
        ])
    if params.get("zupper") is not None:
        cargs.extend([
            "-zupper",
            str(params.get("zupper"))
        ])
    if params.get("zlower") is not None:
        cargs.extend([
            "-zlower",
            str(params.get("zlower"))
        ])
    if params.get("bridge") is not None:
        cargs.extend([
            "-bridge",
            str(params.get("bridge"))
        ])
    if params.get("maskin") is not None:
        cargs.extend([
            "-maskin",
            execution.input_file(params.get("maskin"))
        ])
    if params.get("maskout") is not None:
        cargs.extend([
            "-maskout",
            params.get("maskout")
        ])
    if params.get("strides") is not None:
        cargs.extend([
            "-strides",
            *dyn_cargs(params.get("strides")["__STYXTYPE__"])(params.get("strides"), execution)
        ])
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
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("filter"))
    cargs.append(params.get("output"))
    return cargs


def mrfilter_outputs(
    params: MrfilterParameters,
    execution: Execution,
) -> MrfilterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrfilterOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
        maskout=execution.output_file(params.get("maskout")) if (params.get("maskout") is not None) else None,
    )
    return ret


def mrfilter_execute(
    params: MrfilterParameters,
    execution: Execution,
) -> MrfilterOutputs:
    """
    Perform filtering operations on 3D / 4D MR images.
    
    The available filters are: fft, gradient, median, smooth, normalise, zclean.
    
    Each filter has its own unique set of optional parameters.
    
    For 4D images, each 3D volume is processed independently.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrfilterOutputs`).
    """
    cargs = mrfilter_cargs(params, execution)
    ret = mrfilter_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrfilter(
    input_: InputPathType,
    filter_: str,
    output: str,
    axes: list[int] | None = None,
    inverse: bool = False,
    magnitude: bool = False,
    centre_zero: bool = False,
    stdev: list[float] | None = None,
    magnitude_1: bool = False,
    scanner: bool = False,
    extent: list[int] | None = None,
    extent_1: list[int] | None = None,
    stdev_1: list[float] | None = None,
    fwhm: list[float] | None = None,
    extent_2: list[int] | None = None,
    zupper: float | None = None,
    zlower: float | None = None,
    bridge: int | None = None,
    maskin: InputPathType | None = None,
    maskout: str | None = None,
    strides: typing.Union[MrfilterVariousStringParameters, MrfilterVariousFileParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrfilterConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrfilterOutputs:
    """
    Perform filtering operations on 3D / 4D MR images.
    
    The available filters are: fft, gradient, median, smooth, normalise, zclean.
    
    Each filter has its own unique set of optional parameters.
    
    For 4D images, each 3D volume is processed independently.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image.
        filter_: the type of filter to be applied.
        output: the output image.
        axes: the axes along which to apply the Fourier Transform. By default,\
            the transform is applied along the three spatial axes. Provide as a\
            comma-separate list of axis indices.
        inverse: apply the inverse FFT.
        magnitude: output a magnitude image rather than a complex-valued image.
        centre_zero: re-arrange the FFT results so that the zero-frequency\
            component appears in the centre of the image, rather than at the edges.
        stdev: the standard deviation of the Gaussian kernel used to smooth the\
            input image (in mm). The image is smoothed to reduced large spurious\
            gradients caused by noise. Use this option to override the default\
            stdev of 1 voxel. This can be specified either as a single value to be\
            used for all 3 axes, or as a comma-separated list of 3 values, one for\
            each axis.
        magnitude_1: output the gradient magnitude, rather than the default\
            x,y,z components.
        scanner: define the gradient with respect to the scanner coordinate\
            frame of reference.
        extent: specify extent of median filtering neighbourhood in voxels.\
            This can be specified either as a single value to be used for all 3\
            axes, or as a comma-separated list of 3 values, one for each axis\
            (default: 3x3x3).
        extent_1: specify extent of normalisation filtering neighbourhood in\
            voxels. This can be specified either as a single value to be used for\
            all 3 axes, or as a comma-separated list of 3 values, one for each axis\
            (default: 3x3x3).
        stdev_1: apply Gaussian smoothing with the specified standard\
            deviation. The standard deviation is defined in mm (Default 1 voxel).\
            This can be specified either as a single value to be used for all axes,\
            or as a comma-separated list of the stdev for each axis.
        fwhm: apply Gaussian smoothing with the specified full-width half\
            maximum. The FWHM is defined in mm (Default 1 voxel * 2.3548). This can\
            be specified either as a single value to be used for all axes, or as a\
            comma-separated list of the FWHM for each axis.
        extent_2: specify the extent (width) of kernel size in voxels. This can\
            be specified either as a single value to be used for all axes, or as a\
            comma-separated list of the extent for each axis. The default extent is\
            2 * ceil(2.5 * stdev / voxel_size) - 1.
        zupper: define high intensity outliers: default: 2.5.
        zlower: define low intensity outliers: default: 2.5.
        bridge: number of voxels to gap to fill holes in mask: default: 4.
        maskin: initial mask that defines the maximum spatial extent and the\
            region from which to smaple the intensity range.
        maskout: Output a refined mask based on a spatially coherent region\
            with normal intensity range.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
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
        NamedTuple of outputs (described in `MrfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRFILTER_METADATA)
    params = mrfilter_params(axes=axes, inverse=inverse, magnitude=magnitude, centre_zero=centre_zero, stdev=stdev, magnitude_1=magnitude_1, scanner=scanner, extent=extent, extent_1=extent_1, stdev_1=stdev_1, fwhm=fwhm, extent_2=extent_2, zupper=zupper, zlower=zlower, bridge=bridge, maskin=maskin, maskout=maskout, strides=strides, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, filter_=filter_, output=output)
    return mrfilter_execute(params, execution)


__all__ = [
    "MRFILTER_METADATA",
    "MrfilterConfigParameters",
    "MrfilterOutputs",
    "MrfilterParameters",
    "MrfilterVariousFileParameters",
    "MrfilterVariousStringParameters",
    "mrfilter",
    "mrfilter_config_params",
    "mrfilter_params",
    "mrfilter_various_file_params",
    "mrfilter_various_string_params",
]
