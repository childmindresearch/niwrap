# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_BSET_METADATA = Metadata(
    id="a5ba928b721f328bbae969650915bdc4c218018a.boutiques",
    name="dmri_bset",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriBsetParameters = typing.TypedDict('DmriBsetParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_bset"],
    "input_dwi": InputPathType,
    "output_dwi": str,
    "btol": typing.NotRequired[float | None],
    "bsort": bool,
    "bmax": typing.NotRequired[float | None],
    "input_b_table": typing.NotRequired[InputPathType | None],
    "input_g_table": typing.NotRequired[InputPathType | None],
    "output_b_table": typing.NotRequired[str | None],
    "output_g_table": typing.NotRequired[str | None],
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
        "dmri_bset": dmri_bset_cargs,
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
        "dmri_bset": dmri_bset_outputs,
    }.get(t)


class DmriBsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_bset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dwi_file: OutputPathType
    """Output DWI series"""
    output_b_table_file: OutputPathType | None
    """Output b-value table"""
    output_g_table_file: OutputPathType | None
    """Output gradient table"""


def dmri_bset_params(
    input_dwi: InputPathType,
    output_dwi: str,
    btol: float | None = 0.05,
    bsort: bool = False,
    bmax: float | None = None,
    input_b_table: InputPathType | None = None,
    input_g_table: InputPathType | None = None,
    output_b_table: str | None = None,
    output_g_table: str | None = None,
) -> DmriBsetParameters:
    """
    Build parameters.
    
    Args:
        input_dwi: Input DWI series.
        output_dwi: Output DWI series.
        btol: Tolerance around each single b-value (default: 0.05).
        bsort: Reorder output data by b-shell (default: maintain original\
            order).
        bmax: Extract all b-values less than or equal to a maximum.
        input_b_table: Input b-value table (default: input DWI base, .bvals\
            extension).
        input_g_table: Input gradient table (default: input DWI base, .bvecs\
            extension).
        output_b_table: Output b-value table (default: output DWI base, .bvals\
            extension).
        output_g_table: Output gradient table (default: output DWI base, .bvecs\
            extension).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_bset",
        "input_dwi": input_dwi,
        "output_dwi": output_dwi,
        "bsort": bsort,
    }
    if btol is not None:
        params["btol"] = btol
    if bmax is not None:
        params["bmax"] = bmax
    if input_b_table is not None:
        params["input_b_table"] = input_b_table
    if input_g_table is not None:
        params["input_g_table"] = input_g_table
    if output_b_table is not None:
        params["output_b_table"] = output_b_table
    if output_g_table is not None:
        params["output_g_table"] = output_g_table
    return params


def dmri_bset_cargs(
    params: DmriBsetParameters,
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
    cargs.append("dmri_bset")
    cargs.append(execution.input_file(params.get("input_dwi")))
    cargs.append(params.get("output_dwi"))
    cargs.append("[B_VALUES...]")
    if params.get("btol") is not None:
        cargs.extend([
            "--btol",
            str(params.get("btol"))
        ])
    if params.get("bsort"):
        cargs.append("--bsort")
    if params.get("bmax") is not None:
        cargs.extend([
            "--bmax",
            str(params.get("bmax"))
        ])
    if params.get("input_b_table") is not None:
        cargs.extend([
            "--inb",
            execution.input_file(params.get("input_b_table"))
        ])
    if params.get("input_g_table") is not None:
        cargs.extend([
            "--ing",
            execution.input_file(params.get("input_g_table"))
        ])
    if params.get("output_b_table") is not None:
        cargs.extend([
            "--outb",
            params.get("output_b_table")
        ])
    if params.get("output_g_table") is not None:
        cargs.extend([
            "--outg",
            params.get("output_g_table")
        ])
    return cargs


def dmri_bset_outputs(
    params: DmriBsetParameters,
    execution: Execution,
) -> DmriBsetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriBsetOutputs(
        root=execution.output_file("."),
        output_dwi_file=execution.output_file(params.get("output_dwi")),
        output_b_table_file=execution.output_file(params.get("output_b_table")) if (params.get("output_b_table") is not None) else None,
        output_g_table_file=execution.output_file(params.get("output_g_table")) if (params.get("output_g_table") is not None) else None,
    )
    return ret


def dmri_bset_execute(
    params: DmriBsetParameters,
    execution: Execution,
) -> DmriBsetOutputs:
    """
    This tool extracts a subset of volumes, b-values, and gradient directions from a
    diffusion MRI data set.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriBsetOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dmri_bset_cargs(params, execution)
    ret = dmri_bset_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_bset(
    input_dwi: InputPathType,
    output_dwi: str,
    btol: float | None = 0.05,
    bsort: bool = False,
    bmax: float | None = None,
    input_b_table: InputPathType | None = None,
    input_g_table: InputPathType | None = None,
    output_b_table: str | None = None,
    output_g_table: str | None = None,
    runner: Runner | None = None,
) -> DmriBsetOutputs:
    """
    This tool extracts a subset of volumes, b-values, and gradient directions from a
    diffusion MRI data set.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_dwi: Input DWI series.
        output_dwi: Output DWI series.
        btol: Tolerance around each single b-value (default: 0.05).
        bsort: Reorder output data by b-shell (default: maintain original\
            order).
        bmax: Extract all b-values less than or equal to a maximum.
        input_b_table: Input b-value table (default: input DWI base, .bvals\
            extension).
        input_g_table: Input gradient table (default: input DWI base, .bvecs\
            extension).
        output_b_table: Output b-value table (default: output DWI base, .bvals\
            extension).
        output_g_table: Output gradient table (default: output DWI base, .bvecs\
            extension).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriBsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_BSET_METADATA)
    params = dmri_bset_params(input_dwi=input_dwi, output_dwi=output_dwi, btol=btol, bsort=bsort, bmax=bmax, input_b_table=input_b_table, input_g_table=input_g_table, output_b_table=output_b_table, output_g_table=output_g_table)
    return dmri_bset_execute(params, execution)


__all__ = [
    "DMRI_BSET_METADATA",
    "DmriBsetOutputs",
    "DmriBsetParameters",
    "dmri_bset",
    "dmri_bset_params",
]
