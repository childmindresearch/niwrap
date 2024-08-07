# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ALIGN_EPI_ANAT_METADATA = Metadata(
    id="7c5ebfafa9397922348831041c3f229a6d5dc5c9",
    name="align_epi_anat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AlignEpiAnatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `align_epi_anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    anat_aligned: OutputPathType
    """A version of the anatomy that is aligned to the EPI"""
    epi_aligned: OutputPathType
    """A version of the EPI dataset aligned to the Anatomy"""


def align_epi_anat(
    epi: InputPathType,
    anat: InputPathType,
    epi_base: str,
    anat2epi: bool = False,
    epi2anat: bool = False,
    suffix: str | None = None,
    add_edge: bool = False,
    big_move: bool = False,
    giant_move: bool = False,
    ginormous_move: bool = False,
    keep_rm_files: bool = False,
    prep_only: bool = False,
    ana_has_skull: typing.Literal["yes", "no"] | None = None,
    epi_strip: typing.Literal["3dSkullStrip", "3dAutomask", "None"] | None = None,
    volreg_method: typing.Literal["3dvolreg", "3dWarpDrive", "3dAllineate"] | None = None,
    ex_mode: typing.Literal["quiet", "echo", "dry_run", "script"] | None = None,
    overwrite: bool = False,
    runner: Runner | None = None,
) -> AlignEpiAnatOutputs:
    """
    align_epi_anat by AFNI Team.
    
    Align EPI to anatomical datasets or vice versa.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/align_epi_anat.py.html
    
    Args:
        epi: EPI dataset to align or to which to align.
        anat: Anatomical dataset to align or to which to align.
        epi_base: Base sub-brick to use for alignment\
            (0/mean/median/max/subbrick#).
        anat2epi: Align anatomical to EPI dataset (default).
        epi2anat: Align EPI to anatomical dataset.
        suffix: Append suffix to the original anat/epi dataset to use in the\
            resulting dataset names.
        add_edge: Run @AddEdge script to create composite edge images.
        big_move: Large displacement is needed to align the two volumes.
        giant_move: Even larger movement required, uses cmass, two passes and\
            very large angles and shifts.
        ginormous_move: Adds align_centers to giant_move.
        keep_rm_files: Don't delete any of the temporary files created.
        prep_only: Do preprocessing steps only without alignment.
        ana_has_skull: Do not skullstrip anat dataset.
        epi_strip: Method to remove skull for EPI data.
        volreg_method: Time series volume registration method.
        ex_mode: Command execution mode.
        overwrite: Overwrite existing files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AlignEpiAnatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ALIGN_EPI_ANAT_METADATA)
    cargs = []
    cargs.append("align_epi_anat.py")
    cargs.extend(["-epi", execution.input_file(epi)])
    cargs.extend(["-anat", execution.input_file(anat)])
    cargs.extend(["-epi_base", epi_base])
    cargs.append("[OUTPUT_OPTIONS]")
    cargs.append("[ALIGNMENT_OPTIONS]")
    cargs.append("[PREPROCESSING_OPTIONS]")
    ret = AlignEpiAnatOutputs(
        root=execution.output_file("."),
        anat_aligned=execution.output_file(f"[ANAT]+orig", optional=True),
        epi_aligned=execution.output_file(f"[EPI]+orig", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ALIGN_EPI_ANAT_METADATA",
    "AlignEpiAnatOutputs",
    "align_epi_anat",
]
