# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_GRAYPLOT_METADATA = Metadata(
    id="6d17ab08ae2c6bafb3bb5a4bc0dd707aa3956213.boutiques",
    name="3dGrayplot",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dGrayplotParameters = typing.TypedDict('V3dGrayplotParameters', {
    "__STYX_TYPE__": typing.Literal["3dGrayplot"],
    "input": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "dimensions": typing.NotRequired[list[float] | None],
    "resample_old": bool,
    "polort": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
    "pvorder": bool,
    "LJorder": bool,
    "peelorder": bool,
    "ijkorder": bool,
    "range": typing.NotRequired[float | None],
    "percent": bool,
    "raw_with_bounds": typing.NotRequired[list[float] | None],
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
        "3dGrayplot": v_3d_grayplot_cargs,
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
        "3dGrayplot": v_3d_grayplot_outputs,
    }.get(t)


class V3dGrayplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_grayplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    grayplot_img: OutputPathType | None
    """Grayplot image file"""


def v_3d_grayplot_params(
    input_: InputPathType,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    dimensions: list[float] | None = None,
    resample_old: bool = False,
    polort: float | None = None,
    fwhm: float | None = None,
    pvorder: bool = False,
    ljorder: bool = False,
    peelorder: bool = False,
    ijkorder: bool = False,
    range_: float | None = None,
    percent: bool = False,
    raw_with_bounds: list[float] | None = None,
) -> V3dGrayplotParameters:
    """
    Build parameters.
    
    Args:
        input_: Input dataset.
        mask: Name of mask dataset. Voxels that are 0 in the mask will not be\
            processed.
        prefix: Name for the output file. Default is Grayplot.png.
        dimensions: Output size of image in pixels: [width height]. Defaults\
            are width=1024 and height=512.
        resample_old: Original resampling method for processed dataset.
        polort: Order of polynomials for detrending. Default is 2. Use '-1' if\
            data is already detrended and de-meaned.
        fwhm: FWHM of blurring radius to use in the dataset before making the\
            image. Default is 0 mm.
        pvorder: Order the voxels by how well they match the two leading\
            principal components of their partition.
        ljorder: Order the voxels by their Ljung-Box statistics, a measure of\
            temporal correlation.
        peelorder: Order the voxels by how many 'peel' steps are needed to get\
            from the partition boundary to the voxel.
        ijkorder: Default intra-partition ordering by dataset 3D index ('ijk').
        range_: Set the range of the data to be plotted. Value of 0 is\
            middle-gray, +X is white, -X is black.
        percent: Scale values to percent differences from the mean of each\
            voxel timeseries. Suitable for raw time series datasets.
        raw_with_bounds: Map values <= A to black, values >= B to white, and\
            intermediate values to grays.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dGrayplot",
        "input": input_,
        "resample_old": resample_old,
        "pvorder": pvorder,
        "LJorder": ljorder,
        "peelorder": peelorder,
        "ijkorder": ijkorder,
        "percent": percent,
    }
    if mask is not None:
        params["mask"] = mask
    if prefix is not None:
        params["prefix"] = prefix
    if dimensions is not None:
        params["dimensions"] = dimensions
    if polort is not None:
        params["polort"] = polort
    if fwhm is not None:
        params["fwhm"] = fwhm
    if range_ is not None:
        params["range"] = range_
    if raw_with_bounds is not None:
        params["raw_with_bounds"] = raw_with_bounds
    return params


def v_3d_grayplot_cargs(
    params: V3dGrayplotParameters,
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
    cargs.append("3dGrayplot")
    cargs.append(execution.input_file(params.get("input")))
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("dimensions") is not None:
        cargs.extend([
            "-dimen",
            *map(str, params.get("dimensions"))
        ])
    if params.get("resample_old"):
        cargs.append("-oldresam")
    if params.get("polort") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "-fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("pvorder"):
        cargs.append("-pvorder")
    if params.get("LJorder"):
        cargs.append("-LJorder")
    if params.get("peelorder"):
        cargs.append("-peelorder")
    if params.get("ijkorder"):
        cargs.append("-ijkorder")
    if params.get("range") is not None:
        cargs.extend([
            "-range",
            str(params.get("range"))
        ])
    if params.get("percent"):
        cargs.append("-percent")
    if params.get("raw_with_bounds") is not None:
        cargs.extend([
            "-raw_with_bounds",
            *map(str, params.get("raw_with_bounds"))
        ])
    return cargs


def v_3d_grayplot_outputs(
    params: V3dGrayplotParameters,
    execution: Execution,
) -> V3dGrayplotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dGrayplotOutputs(
        root=execution.output_file("."),
        grayplot_img=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_grayplot_execute(
    params: V3dGrayplotParameters,
    execution: Execution,
) -> V3dGrayplotOutputs:
    """
    Make a grayplot from a 3D+time dataset, like a carpet plot. Result is saved to a
    PNG image.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dGrayplotOutputs`).
    """
    cargs = v_3d_grayplot_cargs(params, execution)
    ret = v_3d_grayplot_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_grayplot(
    input_: InputPathType,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    dimensions: list[float] | None = None,
    resample_old: bool = False,
    polort: float | None = None,
    fwhm: float | None = None,
    pvorder: bool = False,
    ljorder: bool = False,
    peelorder: bool = False,
    ijkorder: bool = False,
    range_: float | None = None,
    percent: bool = False,
    raw_with_bounds: list[float] | None = None,
    runner: Runner | None = None,
) -> V3dGrayplotOutputs:
    """
    Make a grayplot from a 3D+time dataset, like a carpet plot. Result is saved to a
    PNG image.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Input dataset.
        mask: Name of mask dataset. Voxels that are 0 in the mask will not be\
            processed.
        prefix: Name for the output file. Default is Grayplot.png.
        dimensions: Output size of image in pixels: [width height]. Defaults\
            are width=1024 and height=512.
        resample_old: Original resampling method for processed dataset.
        polort: Order of polynomials for detrending. Default is 2. Use '-1' if\
            data is already detrended and de-meaned.
        fwhm: FWHM of blurring radius to use in the dataset before making the\
            image. Default is 0 mm.
        pvorder: Order the voxels by how well they match the two leading\
            principal components of their partition.
        ljorder: Order the voxels by their Ljung-Box statistics, a measure of\
            temporal correlation.
        peelorder: Order the voxels by how many 'peel' steps are needed to get\
            from the partition boundary to the voxel.
        ijkorder: Default intra-partition ordering by dataset 3D index ('ijk').
        range_: Set the range of the data to be plotted. Value of 0 is\
            middle-gray, +X is white, -X is black.
        percent: Scale values to percent differences from the mean of each\
            voxel timeseries. Suitable for raw time series datasets.
        raw_with_bounds: Map values <= A to black, values >= B to white, and\
            intermediate values to grays.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dGrayplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_GRAYPLOT_METADATA)
    params = v_3d_grayplot_params(input_=input_, mask=mask, prefix=prefix, dimensions=dimensions, resample_old=resample_old, polort=polort, fwhm=fwhm, pvorder=pvorder, ljorder=ljorder, peelorder=peelorder, ijkorder=ijkorder, range_=range_, percent=percent, raw_with_bounds=raw_with_bounds)
    return v_3d_grayplot_execute(params, execution)


__all__ = [
    "V3dGrayplotOutputs",
    "V3dGrayplotParameters",
    "V_3D_GRAYPLOT_METADATA",
    "v_3d_grayplot",
    "v_3d_grayplot_params",
]
