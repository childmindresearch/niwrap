# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__CHAUFFEUR_AFNI_METADATA = Metadata(
    id="e7900e8be3172fb7f5f31466dce984b2d6c5262a",
    name="@chauffeur_afni",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VChauffeurAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__chauffeur_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Generated montage image"""
    cluster_report: OutputPathType
    """Clusterization report"""
    whereami_report: OutputPathType
    """Whereami report for clusterized data"""


def v__chauffeur_afni(
    ulay: InputPathType,
    prefix: str,
    olay: InputPathType | None = None,
    mode_4_d: bool = False,
    func_range: float | int | None = None,
    opacity: float | int | None = None,
    set_subbricks: str | None = None,
    montx: float | int | None = None,
    monty: float | int | None = None,
    montgap: float | int | None = None,
    label_mode: float | int | None = None,
    label_size: float | int | None = None,
    label_color: str | None = None,
    label_setback: float | int | None = None,
    no_clean: bool = False,
    do_clean: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> VChauffeurAfniOutputs:
    """
    @chauffeur_afni by AFNI Team.
    
    Automated QC snapshots generator in AFNI.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@chauffeur_afni.html
    
    Args:
        ulay: Name of underlay dataset (required); can be 3D or 4D set.
        prefix: Prefix for output files (required).
        olay: Name of overlay dataset (optional).
        mode_4_d: For each viewing plane, one slice is selected across all\
            volumes in a 4D dataset.
        func_range: Specify upper value of the overlay dataset to be matched to\
            top of colorbar (default: 98%ile non-zero value of dataset).
        opacity: Enter an opacity factor for the overlay (0-9, with 9 being\
            opaque).
        set_subbricks: Specify subbricks for 3D image viewing.
        montx: Number of image panels in a row (default: 3).
        monty: Number of image panels in a column (default: 3).
        montgap: Number of pixels as gap between image panels (default: 0).
        label_mode: Control labels, ON/OFF and location (default: 1).
        label_size: Control labels, size (default: 3).
        label_color: Control labels, color (default: white).
        label_setback: Control labels, offset from edge (default: 0.01).
        no_clean: Do not remove the temporary directory of copied/intermediate\
            files.
        do_clean: Remove the temporary directory of copied/intermediate files.
        help_: Display help information.
        version: Display version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VChauffeurAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CHAUFFEUR_AFNI_METADATA)
    cargs = []
    cargs.append("@chauffeur_afni")
    cargs.append(execution.input_file(ulay))
    if olay is not None:
        cargs.append(execution.input_file(olay))
    cargs.append("-prefix")
    cargs.extend(["-prefix", prefix])
    cargs.append("[options]")
    ret = VChauffeurAfniOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(f"{prefix}.png"),
        cluster_report=execution.output_file(f"{prefix}_clust_rep.txt", optional=True),
        whereami_report=execution.output_file(f"{prefix}_clust_whereami.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VChauffeurAfniOutputs",
    "V__CHAUFFEUR_AFNI_METADATA",
    "v__chauffeur_afni",
]
