# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_TSORT_METADATA = Metadata(
    id="310e5cf7cdd899aa9f25717a2f61e86e6223b21c.boutiques",
    name="1dTsort",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dTsortOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_tsort(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


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
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dTsort.html
    
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
    cargs = []
    cargs.append("1dTsort")
    if dec_order:
        cargs.append("-dec")
    if transpose:
        cargs.append("-flip")
    if column is not None:
        cargs.extend([
            "-col",
            str(column)
        ])
    if imode:
        cargs.append("-imode")
    cargs.append(execution.input_file(infile))
    ret = V1dTsortOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dTsortOutputs",
    "V_1D_TSORT_METADATA",
    "v_1d_tsort",
]