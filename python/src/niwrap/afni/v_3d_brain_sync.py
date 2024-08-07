# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_BRAIN_SYNC_METADATA = Metadata(
    id="b8f6cbc63b7602b8c65d39241740822392ca4db4",
    name="3dBrainSync",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dBrainSyncOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_brain_sync(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    qprefix_output: OutputPathType | None
    """Output dataset after orthogonal matrix transformation"""
    pprefix_output: OutputPathType | None
    """Output dataset after permutation transformation"""
    qprefix_sval: OutputPathType | None
    """Singular values from the BC' decomposition"""
    qprefix_qmat: OutputPathType | None
    """Q matrix"""
    pprefix_perm: OutputPathType | None
    """Permutation indexes p(i)"""


def v_3d_brain_sync(
    inset1: InputPathType,
    inset2: InputPathType,
    qprefix: str | None = None,
    pprefix: str | None = None,
    normalize: bool = False,
    mask: InputPathType | None = None,
    verb: bool = False,
    runner: Runner | None = None,
) -> V3dBrainSyncOutputs:
    """
    3dBrainSync by AFNI Team.
    
    'Synchronizes' the -inset2 dataset to match the -inset1 dataset, using
    orthogonal or permutation transformation.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dBrainSync.html
    
    Args:
        inset1: Reference dataset.
        inset2: Dataset to be matched to the reference dataset.
        qprefix: Specifies the output dataset to be used for the orthogonal\
            matrix transformation.
        pprefix: Specifies the output dataset to be used for the permutation\
            transformation.
        normalize: Normalize the output dataset(s) so that each time series has\
            sum-of-squares = 1.
        mask: Only operate on nonzero voxels in the mask dataset.
        verb: Print some progress reports and auxiliary information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBrainSyncOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BRAIN_SYNC_METADATA)
    cargs = []
    cargs.append("3dBrainSync")
    cargs.append("[OPTIONS]")
    ret = V3dBrainSyncOutputs(
        root=execution.output_file("."),
        qprefix_output=execution.output_file(f"{qprefix}.nii", optional=True) if qprefix is not None else None,
        pprefix_output=execution.output_file(f"{pprefix}.nii", optional=True) if pprefix is not None else None,
        qprefix_sval=execution.output_file(f"{qprefix}.sval.1D", optional=True) if qprefix is not None else None,
        qprefix_qmat=execution.output_file(f"{qprefix}.qmat.1D", optional=True) if qprefix is not None else None,
        pprefix_perm=execution.output_file(f"{pprefix}.perm.1D", optional=True) if pprefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dBrainSyncOutputs",
    "V_3D_BRAIN_SYNC_METADATA",
    "v_3d_brain_sync",
]
