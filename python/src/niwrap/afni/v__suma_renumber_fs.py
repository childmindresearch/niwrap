# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__SUMA_RENUMBER_FS_METADATA = Metadata(
    id="7fb6a766483fe0e3be051963f8852dae6a06b5d8",
    name="@SUMA_renumber_FS",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VSumaRenumberFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_renumber_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    ren_all: OutputPathType
    """Whole parcellation/segmentation file with renumbered ROIs."""
    ren_gm: OutputPathType
    """Gray matter tissue segmentation map."""
    ren_wmat: OutputPathType
    """White matter tissue segmentation map."""
    ren_csf: OutputPathType
    """Cerebrospinal fluid tissue segmentation map."""
    ren_vent: OutputPathType
    """Ventricles and choroid plexus tissue segmentation map."""
    ren_othr: OutputPathType
    """Other tissue segmentation map (optic chiasm, non-WM-hypointens, etc.)."""
    ren_unkn: OutputPathType
    """Unknown tissue segmentation map (FS-defined 'unknown', with voxel value >0)."""
    ren_gmrois: OutputPathType
    """Gray matter ROIs without '*-Cerebral-Cortex' dots."""
    fs_ap_wm: OutputPathType
    """White matter mask (excluding the dotted part from FS)."""
    fs_ap_latvent: OutputPathType
    """Lateral ventricles mask ('*-Lateral-Ventricle')."""
    ren_lbl_table: OutputPathType
    """Labeltable of the new ROI values."""


def v__suma_renumber_fs(
    sumadir: str,
    runner: Runner | None = None,
) -> VSumaRenumberFsOutputs:
    """
    @SUMA_renumber_FS by AFNI Team.
    
    This script processes FreeSurfer-generated parcellation files and produces
    various derived datasets and segmentation maps.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@SUMA_renumber_FS.html
    
    Args:
        sumadir: Path to the 'SUMA/' directory created by @SUMA_Make_Spec_FS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaRenumberFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_RENUMBER_FS_METADATA)
    cargs = []
    cargs.append("@SUMA_renumber_FS")
    cargs.append(sumadir)
    ret = VSumaRenumberFsOutputs(
        root=execution.output_file("."),
        ren_all=execution.output_file(f"*_REN_all.nii.gz", optional=True),
        ren_gm=execution.output_file(f"*_REN_gm.nii.gz", optional=True),
        ren_wmat=execution.output_file(f"*_REN_wmat.nii.gz", optional=True),
        ren_csf=execution.output_file(f"*_REN_csf.nii.gz", optional=True),
        ren_vent=execution.output_file(f"*_REN_vent.nii.gz", optional=True),
        ren_othr=execution.output_file(f"*_REN_othr.nii.gz", optional=True),
        ren_unkn=execution.output_file(f"*_REN_unkn.nii.gz", optional=True),
        ren_gmrois=execution.output_file(f"*_REN_gmrois.nii.gz", optional=True),
        fs_ap_wm=execution.output_file(f"fs_ap_wm.nii.gz", optional=True),
        fs_ap_latvent=execution.output_file(f"fs_ap_latvent.nii.gz", optional=True),
        ren_lbl_table=execution.output_file(f"*_REN_all.niml.lt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSumaRenumberFsOutputs",
    "V__SUMA_RENUMBER_FS_METADATA",
    "v__suma_renumber_fs",
]
