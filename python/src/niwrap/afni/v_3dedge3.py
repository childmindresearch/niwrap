# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DEDGE3_METADATA = Metadata(
    id="313abf8e7b3a12af92fa8fc519ae8bca1a87eaf0.boutiques",
    name="3dedge3",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dedge3Parameters = typing.TypedDict('V3dedge3Parameters', {
    "__STYX_TYPE__": typing.Literal["3dedge3"],
    "input_file": InputPathType,
    "verbose": bool,
    "prefix": typing.NotRequired[str | None],
    "datum": typing.NotRequired[str | None],
    "fscale": bool,
    "gscale": bool,
    "nscale": bool,
    "scale_floats": typing.NotRequired[float | None],
    "automask": bool,
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
        "3dedge3": v_3dedge3_cargs,
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
        "3dedge3": v_3dedge3_outputs,
    }
    return vt.get(t)


class V3dedge3Outputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dedge3(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output dataset"""


def v_3dedge3_params(
    input_file: InputPathType,
    verbose: bool = False,
    prefix: str | None = None,
    datum: str | None = None,
    fscale: bool = False,
    gscale: bool = False,
    nscale: bool = False,
    scale_floats: float | None = None,
    automask: bool = False,
) -> V3dedge3Parameters:
    """
    Build parameters.
    
    Args:
        input_file: Input dataset.
        verbose: Print out some information along the way.
        prefix: Sets the prefix of the output dataset.
        datum: Sets the datum of the output dataset.
        fscale: Force scaling of the output to the maximum integer range.
        gscale: Same as '-fscale', but also forces each output sub-brick to get\
            the same scaling factor.
        nscale: Don't do any scaling on output to byte or short datasets.
        scale_floats: Multiply input by VAL, but only if the input datum is\
            float.
        automask: For automatic internal calculation of a mask in the usual\
            AFNI way.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dedge3",
        "input_file": input_file,
        "verbose": verbose,
        "fscale": fscale,
        "gscale": gscale,
        "nscale": nscale,
        "automask": automask,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if datum is not None:
        params["datum"] = datum
    if scale_floats is not None:
        params["scale_floats"] = scale_floats
    return params


def v_3dedge3_cargs(
    params: V3dedge3Parameters,
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
    cargs.append("3dedge3")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("verbose"):
        cargs.append("-verbose")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("datum") is not None:
        cargs.extend([
            "-datum",
            params.get("datum")
        ])
    if params.get("fscale"):
        cargs.append("-fscale")
    if params.get("gscale"):
        cargs.append("-gscale")
    if params.get("nscale"):
        cargs.append("-nscale")
    if params.get("scale_floats") is not None:
        cargs.extend([
            "-scale_floats",
            str(params.get("scale_floats"))
        ])
    if params.get("automask"):
        cargs.append("-automask")
    return cargs


def v_3dedge3_outputs(
    params: V3dedge3Parameters,
    execution: Execution,
) -> V3dedge3Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dedge3Outputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3dedge3_execute(
    params: V3dedge3Parameters,
    execution: Execution,
) -> V3dedge3Outputs:
    """
    Does 3D Edge detection using the library 3DEdge.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dedge3Outputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3dedge3_cargs(params, execution)
    ret = v_3dedge3_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dedge3(
    input_file: InputPathType,
    verbose: bool = False,
    prefix: str | None = None,
    datum: str | None = None,
    fscale: bool = False,
    gscale: bool = False,
    nscale: bool = False,
    scale_floats: float | None = None,
    automask: bool = False,
    runner: Runner | None = None,
) -> V3dedge3Outputs:
    """
    Does 3D Edge detection using the library 3DEdge.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input dataset.
        verbose: Print out some information along the way.
        prefix: Sets the prefix of the output dataset.
        datum: Sets the datum of the output dataset.
        fscale: Force scaling of the output to the maximum integer range.
        gscale: Same as '-fscale', but also forces each output sub-brick to get\
            the same scaling factor.
        nscale: Don't do any scaling on output to byte or short datasets.
        scale_floats: Multiply input by VAL, but only if the input datum is\
            float.
        automask: For automatic internal calculation of a mask in the usual\
            AFNI way.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dedge3Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DEDGE3_METADATA)
    params = v_3dedge3_params(input_file=input_file, verbose=verbose, prefix=prefix, datum=datum, fscale=fscale, gscale=gscale, nscale=nscale, scale_floats=scale_floats, automask=automask)
    return v_3dedge3_execute(params, execution)


__all__ = [
    "V3dedge3Outputs",
    "V3dedge3Parameters",
    "V_3DEDGE3_METADATA",
    "v_3dedge3",
    "v_3dedge3_params",
]
