# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_TSORT_METADATA = Metadata(
    id="731309e5236007bd69df120b6a0494a5de798eeb.boutiques",
    name="1dTsort",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dTsortParameters = typing.TypedDict('V1dTsortParameters', {
    "__STYX_TYPE__": typing.Literal["1dTsort"],
    "dec_order": bool,
    "transpose": bool,
    "column": typing.NotRequired[float | None],
    "imode": bool,
    "infile": InputPathType,
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
        "1dTsort": v_1d_tsort_cargs,
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


class V1dTsortOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_tsort(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_tsort_params(
    infile: InputPathType,
    dec_order: bool = False,
    transpose: bool = False,
    column: float | None = None,
    imode: bool = False,
) -> V1dTsortParameters:
    """
    Build parameters.
    
    Args:
        infile: Input 1D file to be sorted.
        dec_order: Sort into decreasing order.
        transpose: Transpose the file before output.
        column: Sort only on column #j (counting starts at 0), and carry the\
            rest of the columns with it.
        imode: Typecast all values to integers, return the mode in the input\
            then exit. No sorting results are returned.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dTsort",
        "dec_order": dec_order,
        "transpose": transpose,
        "imode": imode,
        "infile": infile,
    }
    if column is not None:
        params["column"] = column
    return params


def v_1d_tsort_cargs(
    params: V1dTsortParameters,
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
    cargs.append("1dTsort")
    if params.get("dec_order"):
        cargs.append("-dec")
    if params.get("transpose"):
        cargs.append("-flip")
    if params.get("column") is not None:
        cargs.extend([
            "-col",
            str(params.get("column"))
        ])
    if params.get("imode"):
        cargs.append("-imode")
    cargs.append(execution.input_file(params.get("infile")))
    return cargs


def v_1d_tsort_outputs(
    params: V1dTsortParameters,
    execution: Execution,
) -> V1dTsortOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dTsortOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_1d_tsort_execute(
    params: V1dTsortParameters,
    execution: Execution,
) -> V1dTsortOutputs:
    """
    Sorts each column of the input 1D file and writes result to stdout.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dTsortOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_1d_tsort_cargs(params, execution)
    ret = v_1d_tsort_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_tsort(
    infile: InputPathType,
    dec_order: bool = False,
    transpose: bool = False,
    column: float | None = None,
    imode: bool = False,
    runner: Runner | None = None,
) -> V1dTsortOutputs:
    """
    Sorts each column of the input 1D file and writes result to stdout.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input 1D file to be sorted.
        dec_order: Sort into decreasing order.
        transpose: Transpose the file before output.
        column: Sort only on column #j (counting starts at 0), and carry the\
            rest of the columns with it.
        imode: Typecast all values to integers, return the mode in the input\
            then exit. No sorting results are returned.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dTsortOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_TSORT_METADATA)
    params = v_1d_tsort_params(dec_order=dec_order, transpose=transpose, column=column, imode=imode, infile=infile)
    return v_1d_tsort_execute(params, execution)


__all__ = [
    "V1dTsortOutputs",
    "V1dTsortParameters",
    "V_1D_TSORT_METADATA",
    "v_1d_tsort",
    "v_1d_tsort_params",
]
