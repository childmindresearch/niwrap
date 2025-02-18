# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ZCAT_METADATA = Metadata(
    id="a00d1d033ba00163e081549b0d7b74b2c667d65a.boutiques",
    name="3dZcat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dZcatParameters = typing.TypedDict('V3dZcatParameters', {
    "__STYX_TYPE__": typing.Literal["3dZcat"],
    "prefix": typing.NotRequired[str | None],
    "datum": typing.NotRequired[typing.Literal["byte", "short", "float"] | None],
    "fscale": bool,
    "nscale": bool,
    "verb": bool,
    "frugal": bool,
    "input_files": list[InputPathType],
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
        "3dZcat": v_3d_zcat_cargs,
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
        "3dZcat": v_3d_zcat_outputs,
    }.get(t)


class V3dZcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_head: OutputPathType | None
    """AFNI HEAD file of the output dataset"""
    out_brik: OutputPathType | None
    """AFNI BRIK file of the output dataset"""


def v_3d_zcat_params(
    input_files: list[InputPathType],
    prefix: str | None = None,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    fscale: bool = False,
    nscale: bool = False,
    verb: bool = False,
    frugal: bool = False,
) -> V3dZcatParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input datasets.
        prefix: Use 'pname' for the output dataset prefix name.\
            [default='zcat'].
        datum: Coerce the output data to be stored as the given type, which may\
            be byte, short, or float.
        fscale: Force scaling of the output to the maximum integer range. This\
            only has effect if the output datum is byte or short (either forced or\
            defaulted). This option is sometimes necessary to eliminate unpleasant\
            truncation artifacts.
        nscale: Don't do any scaling on output to byte or short datasets. This\
            may be especially useful when operating on mask datasets whose output\
            values are only 0's and 1's.
        verb: Print out some verbosity as the program proceeds.
        frugal: Be 'frugal' in the use of memory, at the cost of I/O time. Only\
            needed if the program runs out of memory. Note frugality cannot be\
            combined with NIFTI output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dZcat",
        "fscale": fscale,
        "nscale": nscale,
        "verb": verb,
        "frugal": frugal,
        "input_files": input_files,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if datum is not None:
        params["datum"] = datum
    return params


def v_3d_zcat_cargs(
    params: V3dZcatParameters,
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
    cargs.append("3dZcat")
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
    if params.get("nscale"):
        cargs.append("-nscale")
    if params.get("verb"):
        cargs.append("-verb")
    if params.get("frugal"):
        cargs.append("-frugal")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def v_3d_zcat_outputs(
    params: V3dZcatParameters,
    execution: Execution,
) -> V3dZcatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dZcatOutputs(
        root=execution.output_file("."),
        out_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
        out_brik=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_zcat_execute(
    params: V3dZcatParameters,
    execution: Execution,
) -> V3dZcatOutputs:
    """
    Concatenates datasets in the slice (z) direction.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dZcatOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_zcat_cargs(params, execution)
    ret = v_3d_zcat_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_zcat(
    input_files: list[InputPathType],
    prefix: str | None = None,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    fscale: bool = False,
    nscale: bool = False,
    verb: bool = False,
    frugal: bool = False,
    runner: Runner | None = None,
) -> V3dZcatOutputs:
    """
    Concatenates datasets in the slice (z) direction.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input datasets.
        prefix: Use 'pname' for the output dataset prefix name.\
            [default='zcat'].
        datum: Coerce the output data to be stored as the given type, which may\
            be byte, short, or float.
        fscale: Force scaling of the output to the maximum integer range. This\
            only has effect if the output datum is byte or short (either forced or\
            defaulted). This option is sometimes necessary to eliminate unpleasant\
            truncation artifacts.
        nscale: Don't do any scaling on output to byte or short datasets. This\
            may be especially useful when operating on mask datasets whose output\
            values are only 0's and 1's.
        verb: Print out some verbosity as the program proceeds.
        frugal: Be 'frugal' in the use of memory, at the cost of I/O time. Only\
            needed if the program runs out of memory. Note frugality cannot be\
            combined with NIFTI output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZCAT_METADATA)
    params = v_3d_zcat_params(prefix=prefix, datum=datum, fscale=fscale, nscale=nscale, verb=verb, frugal=frugal, input_files=input_files)
    return v_3d_zcat_execute(params, execution)


__all__ = [
    "V3dZcatOutputs",
    "V3dZcatParameters",
    "V_3D_ZCAT_METADATA",
    "v_3d_zcat",
    "v_3d_zcat_params",
]
