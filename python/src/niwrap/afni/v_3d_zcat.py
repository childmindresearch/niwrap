# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ZCAT_METADATA = Metadata(
    id="efac51c86e82360905a0bb204fedd4b5b3ba897b",
    name="3dZcat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


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
    3dZcat by AFNI Team.
    
    Concatenates datasets in the slice (z) direction.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dZcat.html
    
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
    cargs = []
    cargs.append("3dZcat")
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if datum is not None:
        cargs.extend(["-datum", datum])
    if fscale:
        cargs.append("-fscale")
    if nscale:
        cargs.append("-nscale")
    if verb:
        cargs.append("-verb")
    if frugal:
        cargs.append("-frugal")
    cargs.append("[INPUT_FILES...]")
    ret = V3dZcatOutputs(
        root=execution.output_file("."),
        out_head=execution.output_file(f"{prefix}+orig.HEAD", optional=True) if prefix is not None else None,
        out_brik=execution.output_file(f"{prefix}+orig.BRIK", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dZcatOutputs",
    "V_3D_ZCAT_METADATA",
    "v_3d_zcat",
]
