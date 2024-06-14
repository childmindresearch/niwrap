# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CONVERT_XFM_METADATA = Metadata(
    id="48d9ebaa0f317be0039ff6ce316c83701317a1be",
    name="convert_xfm",
    container_image_type="docker",
    container_image_tag="fcp-indi/c-pac:nightly",
)


class ConvertXfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_xfm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_trasnformation: OutputPathType | None
    """Output transformation matrix."""


def convert_xfm(
    in_file: InputPathType,
    concat_xfm: InputPathType | None = None,
    fix_scale_skew: InputPathType | None = None,
    invert_xfm: bool = False,
    out_file: InputPathType | None = None,
    runner: Runner = None,
) -> ConvertXfmOutputs:
    """
    convert_xfm by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    convert_xfm is a utility that is used to convert between different
    transformation file formats. It can read and write ascii 4x4 matrices. In
    addition, it can be used to concatenate two transforms (using -concat with
    the second transform) or to find the inverse transformation (using
    -inverse).
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT/UserGuide#convert_xfm
    
    Args:
        in_file: Input transformation matrix.
        concat_xfm: A File. Write joint transformation of two input matrices.
        fix_scale_skew: A File. Use secondary matrix to fix scale and skew.
        invert_xfm: Invert input transformation.
        out_file: Final transformation matrix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertXfmOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        invert_xfm +
        (fix_scale_skew is not None) +
        (concat_xfm is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "invert_xfm,\n"
            "fix_scale_skew,\n"
            "concat_xfm"
        )
    execution = runner.start_execution(CONVERT_XFM_METADATA)
    cargs = []
    cargs.append("convert_xfm")
    cargs.append(execution.input_file(in_file))
    if invert_xfm:
        cargs.append("-inverse")
    if concat_xfm is not None:
        cargs.extend(["-concat", execution.input_file(concat_xfm)])
    if fix_scale_skew is not None:
        cargs.extend(["-fixscaleskew", execution.input_file(fix_scale_skew)])
    if out_file is not None:
        cargs.extend(["-omat", execution.input_file(out_file)])
    ret = ConvertXfmOutputs(
        root=execution.output_file("."),
        output_trasnformation=execution.output_file(f"{pathlib.Path(out_file).name}") if out_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_XFM_METADATA",
    "ConvertXfmOutputs",
    "convert_xfm",
]