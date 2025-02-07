# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ADWARP_METADATA = Metadata(
    id="22410e65c1361d9cb6b13a0fd56cc72bae69129b.boutiques",
    name="adwarp",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AdwarpParameters = typing.TypedDict('AdwarpParameters', {
    "__STYX_TYPE__": typing.Literal["adwarp"],
    "apar": InputPathType,
    "dpar": str,
    "prefix": typing.NotRequired[str | None],
    "dxyz": typing.NotRequired[float | None],
    "verbose": bool,
    "force": bool,
    "resam": typing.NotRequired[str | None],
    "thr": typing.NotRequired[str | None],
    "func": typing.NotRequired[str | None],
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
        "adwarp": adwarp_cargs,
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
        "adwarp": adwarp_outputs,
    }.get(t)


class AdwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    header_output: OutputPathType | None
    """Output dataset header file"""
    brick_output: OutputPathType | None
    """Output dataset brick file"""


def adwarp_params(
    apar: InputPathType,
    dpar: str,
    prefix: str | None = None,
    dxyz: float | None = None,
    verbose: bool = False,
    force: bool = False,
    resam: str | None = None,
    thr: str | None = None,
    func: str | None = None,
) -> AdwarpParameters:
    """
    Build parameters.
    
    Args:
        apar: Set the anat parent dataset (nonoptional).
        dpar: Set the data parent dataset (nonoptional). dset may contain a\
            sub-brick selector, e.g., -dpar 'dset+orig[2,5,7]'.
        prefix: Set the prefix for the output dataset. Default is the prefix of\
            'dset'.
        dxyz: Set the grid spacing in the output dataset. Default is 1 mm.
        verbose: Print out progress reports.
        force: Write out result even if it means deleting an existing dataset.\
            Default is not to overwrite.
        resam: Set resampling mode for all sub-bricks. Modes: NN (Nearest\
            Neighbor), Li (Linear Interpolation), Cu (Cubic Interpolation), Bk\
            (Blocky Interpolation). Default is Li for all sub-bricks.
        thr: Set resampling mode for threshold sub-bricks. Modes: NN (Nearest\
            Neighbor), Li (Linear Interpolation), Cu (Cubic Interpolation), Bk\
            (Blocky Interpolation).
        func: Set resampling mode for functional sub-bricks. Modes: NN (Nearest\
            Neighbor), Li (Linear Interpolation), Cu (Cubic Interpolation), Bk\
            (Blocky Interpolation).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "adwarp",
        "apar": apar,
        "dpar": dpar,
        "verbose": verbose,
        "force": force,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if dxyz is not None:
        params["dxyz"] = dxyz
    if resam is not None:
        params["resam"] = resam
    if thr is not None:
        params["thr"] = thr
    if func is not None:
        params["func"] = func
    return params


def adwarp_cargs(
    params: AdwarpParameters,
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
    cargs.append("adwarp")
    cargs.extend([
        "-apar",
        execution.input_file(params.get("apar"))
    ])
    cargs.extend([
        "-dpar",
        params.get("dpar")
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("dxyz") is not None:
        cargs.extend([
            "-dxyz",
            str(params.get("dxyz"))
        ])
    if params.get("verbose"):
        cargs.append("-verbose")
    if params.get("force"):
        cargs.append("-force")
    if params.get("resam") is not None:
        cargs.extend([
            "-resam",
            params.get("resam")
        ])
    if params.get("thr") is not None:
        cargs.extend([
            "-thr",
            params.get("thr")
        ])
    if params.get("func") is not None:
        cargs.extend([
            "-func",
            params.get("func")
        ])
    return cargs


def adwarp_outputs(
    params: AdwarpParameters,
    execution: Execution,
) -> AdwarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AdwarpOutputs(
        root=execution.output_file("."),
        header_output=execution.output_file(params.get("prefix") + ".HEAD") if (params.get("prefix") is not None) else None,
        brick_output=execution.output_file(params.get("prefix") + ".BRIK") if (params.get("prefix") is not None) else None,
    )
    return ret


def adwarp_execute(
    params: AdwarpParameters,
    execution: Execution,
) -> AdwarpOutputs:
    """
    Resamples a 'data parent' dataset to the grid defined by an 'anat parent'
    dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AdwarpOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = adwarp_cargs(params, execution)
    ret = adwarp_outputs(params, execution)
    execution.run(cargs)
    return ret


def adwarp(
    apar: InputPathType,
    dpar: str,
    prefix: str | None = None,
    dxyz: float | None = None,
    verbose: bool = False,
    force: bool = False,
    resam: str | None = None,
    thr: str | None = None,
    func: str | None = None,
    runner: Runner | None = None,
) -> AdwarpOutputs:
    """
    Resamples a 'data parent' dataset to the grid defined by an 'anat parent'
    dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        apar: Set the anat parent dataset (nonoptional).
        dpar: Set the data parent dataset (nonoptional). dset may contain a\
            sub-brick selector, e.g., -dpar 'dset+orig[2,5,7]'.
        prefix: Set the prefix for the output dataset. Default is the prefix of\
            'dset'.
        dxyz: Set the grid spacing in the output dataset. Default is 1 mm.
        verbose: Print out progress reports.
        force: Write out result even if it means deleting an existing dataset.\
            Default is not to overwrite.
        resam: Set resampling mode for all sub-bricks. Modes: NN (Nearest\
            Neighbor), Li (Linear Interpolation), Cu (Cubic Interpolation), Bk\
            (Blocky Interpolation). Default is Li for all sub-bricks.
        thr: Set resampling mode for threshold sub-bricks. Modes: NN (Nearest\
            Neighbor), Li (Linear Interpolation), Cu (Cubic Interpolation), Bk\
            (Blocky Interpolation).
        func: Set resampling mode for functional sub-bricks. Modes: NN (Nearest\
            Neighbor), Li (Linear Interpolation), Cu (Cubic Interpolation), Bk\
            (Blocky Interpolation).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADWARP_METADATA)
    params = adwarp_params(apar=apar, dpar=dpar, prefix=prefix, dxyz=dxyz, verbose=verbose, force=force, resam=resam, thr=thr, func=func)
    return adwarp_execute(params, execution)


__all__ = [
    "ADWARP_METADATA",
    "AdwarpOutputs",
    "AdwarpParameters",
    "adwarp",
    "adwarp_params",
]
