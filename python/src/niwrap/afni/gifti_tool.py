# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

GIFTI_TOOL_METADATA = Metadata(
    id="405f86dc69641589b7ee6c6633639b7a69774f42",
    name="gifti_tool",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class GiftiToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_gifti: OutputPathType
    """Output GIFTI file"""


def gifti_tool(
    infile: InputPathType,
    write_gifti: str,
    new_numda: float | int | None = None,
    new_dtype: str | None = None,
    new_intent: str | None = None,
    new_ndim: float | int | None = None,
    new_dims: list[float | int] | None = None,
    set_extern_filelist: list[str] | None = None,
    mod_add_data: bool = False,
    verb: float | int | None = None,
    show_gifti: bool = False,
    read_das: list[float | int] | None = None,
    mod_gim_atr: list[str] | None = None,
    mod_gim_meta: list[str] | None = None,
    mod_da_atr: list[str] | None = None,
    mod_da_meta: list[str] | None = None,
    mod_das: list[float | int] | None = None,
    new_dset: bool = False,
    compare_gifti: bool = False,
    compare_data: bool = False,
    compare_verb: float | int | None = None,
    approx_gifti: bool = False,
    runner: Runner | None = None,
) -> GiftiToolOutputs:
    """
    gifti_tool by AFNI Team.
    
    Tool for creating, displaying, modifying, or comparing GIFTI datasets.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/gifti_tool.html
    
    Args:
        infile: Specify one or more GIFTI datasets as input.
        write_gifti: Write out dataset as gifti image.
        new_numda: New dataset will have NUMDA DataArray elements.
        new_dtype: Set data type to TYPE.
        new_intent: DA elements will have intent INTENT.
        new_ndim: Set Dimensionality to NUMDIMS.
        new_dims: Set dims[] to these 6 values.
        set_extern_filelist: Store data in external files.
        mod_add_data: Add data to empty DataArray elements.
        verb: Set verbose level.
        show_gifti: Show final gifti image.
        read_das: Read DataArray list indices.
        mod_gim_atr: Set the GIFTI NAME=VALUE attribute pair at GIFTI level.
        mod_gim_meta: Add this pair to the GIFTI MetaData.
        mod_da_atr: Set the DataArray NAME=VALUE attribute pair.
        mod_da_meta: Set the DataArray NAME=VALUE pair in DA's MetaData.
        mod_das: Specify the set of DataArrays to modify.
        new_dset: Create a new GIFTI dataset.
        compare_gifti: Compare two GIFTI datasets.
        compare_data: Flag to request comparison of the data.
        compare_verb: Set the verbose level of comparisons.
        approx_gifti: Approximate comparison of GIFTI datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GiftiToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GIFTI_TOOL_METADATA)
    cargs = []
    cargs.append("gifti_tool")
    cargs.append("[ARGS]")
    ret = GiftiToolOutputs(
        root=execution.output_file("."),
        output_gifti=execution.output_file(f"{write_gifti}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GIFTI_TOOL_METADATA",
    "GiftiToolOutputs",
    "gifti_tool",
]
