# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DMERGE_METADATA = Metadata(
    id="7f1c2ca1745d4893ae0eaf6d19b9cf828f0a6f25.boutiques",
    name="3dmerge",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dmergeParameters = typing.TypedDict('V3dmergeParameters', {
    "__STYX_TYPE__": typing.Literal["3dmerge"],
    "input_files": list[InputPathType],
    "output_file": str,
    "blur_fwhm": typing.NotRequired[float | None],
    "threshold": typing.NotRequired[float | None],
    "clust": typing.NotRequired[list[float] | None],
    "dindex": typing.NotRequired[float | None],
    "tindex": typing.NotRequired[float | None],
    "absolute": bool,
    "dxyz": bool,
    "gmean": bool,
    "gmax": bool,
    "quiet": bool,
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
        "3dmerge": v_3dmerge_cargs,
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
        "3dmerge": v_3dmerge_outputs,
    }.get(t)


class V3dmergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmerge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset file"""


def v_3dmerge_params(
    input_files: list[InputPathType],
    output_file: str,
    blur_fwhm: float | None = None,
    threshold: float | None = None,
    clust: list[float] | None = None,
    dindex: float | None = None,
    tindex: float | None = None,
    absolute: bool = False,
    dxyz: bool = False,
    gmean: bool = False,
    gmax: bool = False,
    quiet: bool = False,
) -> V3dmergeParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input dataset files.
        output_file: Output dataset prefix.
        blur_fwhm: Gaussian blur with FWHM in mm.
        threshold: Threshold data to censor the intensities; only valid for\
            'fith', 'fico', or 'fitt' datasets.
        clust: Form clusters with connection distance and clip off data not in\
            clusters of a minimum volume.
        dindex: Specify sub-brick #j as the data source.
        tindex: Specify sub-brick #k as the threshold source.
        absolute: Take absolute values of intensities.
        dxyz: Force cluster editing to behave as if all voxel dimensions were\
            set to 1 mm.
        gmean: Combine datasets by averaging intensities (default).
        gmax: Combine datasets by taking max intensity.
        quiet: Reduce the number of messages shown.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dmerge",
        "input_files": input_files,
        "output_file": output_file,
        "absolute": absolute,
        "dxyz": dxyz,
        "gmean": gmean,
        "gmax": gmax,
        "quiet": quiet,
    }
    if blur_fwhm is not None:
        params["blur_fwhm"] = blur_fwhm
    if threshold is not None:
        params["threshold"] = threshold
    if clust is not None:
        params["clust"] = clust
    if dindex is not None:
        params["dindex"] = dindex
    if tindex is not None:
        params["tindex"] = tindex
    return params


def v_3dmerge_cargs(
    params: V3dmergeParameters,
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
    cargs.append("3dmerge")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    cargs.extend([
        "-prefix",
        params.get("output_file")
    ])
    if params.get("blur_fwhm") is not None:
        cargs.extend([
            "-1blur_fwhm",
            str(params.get("blur_fwhm"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "-1thresh",
            str(params.get("threshold"))
        ])
    if params.get("clust") is not None:
        cargs.extend([
            "-1clust",
            *map(str, params.get("clust"))
        ])
    if params.get("dindex") is not None:
        cargs.extend([
            "-1dindex",
            str(params.get("dindex"))
        ])
    if params.get("tindex") is not None:
        cargs.extend([
            "-1tindex",
            str(params.get("tindex"))
        ])
    if params.get("absolute"):
        cargs.append("-1abs")
    if params.get("dxyz"):
        cargs.append("-dxyz=1")
    if params.get("gmean"):
        cargs.append("-gmean")
    if params.get("gmax"):
        cargs.append("-gmax")
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v_3dmerge_outputs(
    params: V3dmergeParameters,
    execution: Execution,
) -> V3dmergeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dmergeOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("output_file")),
    )
    return ret


def v_3dmerge_execute(
    params: V3dmergeParameters,
    execution: Execution,
) -> V3dmergeOutputs:
    """
    3dmerge edits and merges 3D datasets by applying various operations like
    thresholding, blurring, clustering, and more.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dmergeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3dmerge_cargs(params, execution)
    ret = v_3dmerge_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dmerge(
    input_files: list[InputPathType],
    output_file: str,
    blur_fwhm: float | None = None,
    threshold: float | None = None,
    clust: list[float] | None = None,
    dindex: float | None = None,
    tindex: float | None = None,
    absolute: bool = False,
    dxyz: bool = False,
    gmean: bool = False,
    gmax: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dmergeOutputs:
    """
    3dmerge edits and merges 3D datasets by applying various operations like
    thresholding, blurring, clustering, and more.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input dataset files.
        output_file: Output dataset prefix.
        blur_fwhm: Gaussian blur with FWHM in mm.
        threshold: Threshold data to censor the intensities; only valid for\
            'fith', 'fico', or 'fitt' datasets.
        clust: Form clusters with connection distance and clip off data not in\
            clusters of a minimum volume.
        dindex: Specify sub-brick #j as the data source.
        tindex: Specify sub-brick #k as the threshold source.
        absolute: Take absolute values of intensities.
        dxyz: Force cluster editing to behave as if all voxel dimensions were\
            set to 1 mm.
        gmean: Combine datasets by averaging intensities (default).
        gmax: Combine datasets by taking max intensity.
        quiet: Reduce the number of messages shown.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMERGE_METADATA)
    params = v_3dmerge_params(input_files=input_files, output_file=output_file, blur_fwhm=blur_fwhm, threshold=threshold, clust=clust, dindex=dindex, tindex=tindex, absolute=absolute, dxyz=dxyz, gmean=gmean, gmax=gmax, quiet=quiet)
    return v_3dmerge_execute(params, execution)


__all__ = [
    "V3dmergeOutputs",
    "V3dmergeParameters",
    "V_3DMERGE_METADATA",
    "v_3dmerge",
    "v_3dmerge_params",
]
