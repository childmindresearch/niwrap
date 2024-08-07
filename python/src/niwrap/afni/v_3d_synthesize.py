# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_SYNTHESIZE_METADATA = Metadata(
    id="2114f9664df6acaf070036b6be59b37008a2b9aa",
    name="3dSynthesize",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dSynthesizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_synthesize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_synthesize(
    c_bucket: InputPathType,
    matrix: InputPathType,
    prefix: str,
    select_: str,
    dry_flag: bool = False,
    tr: float | int | None = None,
    cenfill: typing.Literal["zero", "nbhr", "none"] | None = None,
    runner: Runner | None = None,
) -> V3dSynthesizeOutputs:
    """
    3dSynthesize by AFNI Team.
    
    Reads a '-cbucket' dataset and a '.xmat.1D' matrix from 3dDeconvolve, and
    synthesizes a fit dataset using selected sub-bricks and matrix columns.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSynthesize.html
    
    Args:
        c_bucket: Input dataset from 3dDeconvolve via the '-cbucket' option.
        matrix: Matrix file from 3dDeconvolve via the '-x1D' option.
        prefix: Output result into dataset with the specified name.
        select_: Select columns from the matrix and corresponding sub-bricks\
            from the cbucket. Can use forms like 'baseline', 'polort', 'allfunc',\
            'allstim', 'all', 'something', or numbers/ranges.
        dry_flag: Don't compute the output, just check the inputs.
        tr: Set TR in the output to the specified value.
        cenfill: How censored time points from 3dDeconvolve will be filled\
            (options: 'zero', 'nbhr', 'none').
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSynthesizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SYNTHESIZE_METADATA)
    cargs = []
    cargs.append("3dSynthesize")
    cargs.append("-cbucket")
    cargs.append(execution.input_file(c_bucket))
    cargs.append("-matrix")
    cargs.append(execution.input_file(matrix))
    cargs.append("-select")
    cargs.append(select_)
    cargs.append("-prefix")
    cargs.append(prefix)
    if dry_flag:
        cargs.append("-dry")
    if tr is not None:
        cargs.extend(["-TR", str(tr)])
    if cenfill is not None:
        cargs.extend(["-cenfill", cenfill])
    ret = V3dSynthesizeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSynthesizeOutputs",
    "V_3D_SYNTHESIZE_METADATA",
    "v_3d_synthesize",
]
