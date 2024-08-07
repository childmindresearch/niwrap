# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ADJUNCT_APQC_TSNR_GENERAL_METADATA = Metadata(
    id="cc30f8074e086c96e5cfea20ed33ef80b0074b2f",
    name="adjunct_apqc_tsnr_general",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AdjunctApqcTsnrGeneralOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_apqc_tsnr_general(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_apqc_tsnr_general(
    montgap: str | None = None,
    montcolor: str | None = None,
    montx: str | None = None,
    monty: str | None = None,
    opacity: str | None = None,
    blowup: str | None = None,
    save_ftype: str | None = None,
    set_dicom_xyz: list[str] | None = None,
    set_ijk: list[str] | None = None,
    set_subbricks: list[str] | None = None,
    olay_alpha: str | None = None,
    olay_boxed: str | None = None,
    thr_olay: str | None = None,
    ulay_range_nz: list[str] | None = None,
    ulay_range: list[str] | None = None,
    delta_slices: list[str] | None = None,
    olay_disc_hot_range: list[str] | None = None,
    olay_cont_max: str | None = None,
    cbar_cont: str | None = None,
    no_cor: bool = False,
    no_sag: bool = False,
    no_axi: bool = False,
    echo: bool = False,
    runner: Runner | None = None,
) -> AdjunctApqcTsnrGeneralOutputs:
    """
    adjunct_apqc_tsnr_general by AFNI Team.
    
    An adjunct program for making TSNR plots for APQC.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_apqc_tsnr_general.html
    
    Args:
        montgap: Specify montage gap.
        montcolor: Specify montage color.
        montx: Specify montage x coordinate.
        monty: Specify montage y coordinate.
        opacity: Specify overlay opacity.
        blowup: Specify blowup factor.
        save_ftype: Specify save file type.
        set_dicom_xyz: Set DICOM x, y, z coordinates.
        set_ijk: Set IJK coordinates.
        set_subbricks: Set sub-bricks.
        olay_alpha: Specify overlay alpha.
        olay_boxed: Specify boxed overlay.
        thr_olay: Specify threshold for overlay.
        ulay_range_nz: Specify non-zero range for underlay.
        ulay_range: Specify range for underlay.
        delta_slices: Specify delta slices.
        olay_disc_hot_range: Specify discrete hot range for overlay.
        olay_cont_max: Specify continuous max for overlay.
        cbar_cont: Specify continuous color bar.
        no_cor: No coronal view.
        no_sag: No sagittal view.
        no_axi: No axial view.
        echo: Echo the command line arguments.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctApqcTsnrGeneralOutputs`).
    """
    runner = runner or get_global_runner()
    if set_dicom_xyz is not None and not (len(set_dicom_xyz) <= 3): 
        raise ValueError(f"Length of 'set_dicom_xyz' must be less than 3 but was {len(set_dicom_xyz)}")
    if set_ijk is not None and not (len(set_ijk) <= 3): 
        raise ValueError(f"Length of 'set_ijk' must be less than 3 but was {len(set_ijk)}")
    if set_subbricks is not None and not (len(set_subbricks) <= 3): 
        raise ValueError(f"Length of 'set_subbricks' must be less than 3 but was {len(set_subbricks)}")
    if ulay_range_nz is not None and not (len(ulay_range_nz) <= 2): 
        raise ValueError(f"Length of 'ulay_range_nz' must be less than 2 but was {len(ulay_range_nz)}")
    if ulay_range is not None and not (len(ulay_range) <= 2): 
        raise ValueError(f"Length of 'ulay_range' must be less than 2 but was {len(ulay_range)}")
    if delta_slices is not None and not (len(delta_slices) <= 3): 
        raise ValueError(f"Length of 'delta_slices' must be less than 3 but was {len(delta_slices)}")
    if olay_disc_hot_range is not None and not (len(olay_disc_hot_range) <= 2): 
        raise ValueError(f"Length of 'olay_disc_hot_range' must be less than 2 but was {len(olay_disc_hot_range)}")
    execution = runner.start_execution(ADJUNCT_APQC_TSNR_GENERAL_METADATA)
    cargs = []
    cargs.append("adjunct_apqc_tsnr_general")
    cargs.append("[OPTIONS]")
    ret = AdjunctApqcTsnrGeneralOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_APQC_TSNR_GENERAL_METADATA",
    "AdjunctApqcTsnrGeneralOutputs",
    "adjunct_apqc_tsnr_general",
]
