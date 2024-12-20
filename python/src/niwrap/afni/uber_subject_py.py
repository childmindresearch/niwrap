# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

UBER_SUBJECT_PY_METADATA = Metadata(
    id="d4f27b8c1311827036baefee6a5e5f22311c1cf3.boutiques",
    name="uber_subject.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class UberSubjectPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `uber_subject_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def uber_subject_py(
    qt_opts: str | None = None,
    svar: str | None = None,
    cvar: str | None = None,
    no_gui: bool = False,
    print_ap_command: bool = False,
    save_ap_command: str | None = None,
    exec_ap_command: bool = False,
    exec_proc_script: bool = False,
    align_cost: str | None = None,
    align_giant_move: str | None = None,
    align_opts_aea: str | None = None,
    anal_domain: str | None = None,
    anal_type: str | None = None,
    anat: InputPathType | None = None,
    anat_has_skull: str | None = None,
    blocks: str | None = None,
    blur_size: float | None = None,
    epi: str | None = None,
    epi_wildcard: str | None = None,
    gid: str | None = None,
    gltsym: str | None = None,
    gltsym_label: str | None = None,
    motion_limit: float | None = None,
    outlier_limit: float | None = None,
    regress_goforit: float | None = None,
    regress_bandpass: str | None = None,
    regress_jobs: float | None = None,
    regress_mot_deriv: str | None = None,
    regress_opts_3d_d: str | None = None,
    reml_exec: str | None = None,
    run_clustsim: str | None = None,
    sid: str | None = None,
    stim: InputPathType | None = None,
    stim_basis: str | None = None,
    stim_label: str | None = None,
    stim_type: str | None = None,
    stim_wildcard: str | None = None,
    tcat_nfirst: float | None = None,
    tlrc_base: str | None = None,
    tlrc_ok_maxite: str | None = None,
    tlrc_opts_at: str | None = None,
    volreg_base: str | None = None,
    verb: str | None = None,
    runner: Runner | None = None,
) -> UberSubjectPyOutputs:
    """
    Graphical interface to afni_proc.py.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        qt_opts: Pass options to PyQt4.
        svar: Set subject variable to value.
        cvar: Set control variable to value.
        no_gui: Do not open graphical interface.
        print_ap_command: Show afni_proc.py script.
        save_ap_command: Save afni_proc.py script.
        exec_ap_command: Run afni_proc.py command.
        exec_proc_script: Run proc script.
        align_cost: Specify cost function for anat/EPI alignment.
        align_giant_move: Use -giant_move in AEA.py.
        align_opts_aea: Specify extra options for align_epi_anat.py.
        anal_domain: Set data domain (volume/rest).
        anal_type: Set analysis type (task/rest).
        anat: Set anatomical dataset name.
        anat_has_skull: Whether anat has skull (yes/no).
        blocks: Set list of processing blocks to apply.
        blur_size: Set blur size in mm.
        epi: Set list of EPI datasets.
        epi_wildcard: Use wildcard for EPI datasets (yes/no).
        gid: Set group ID.
        gltsym: Specify list of symbolic GLTs.
        gltsym_label: Set corresponding GLT labels.
        motion_limit: Set per-TR motion limit in mm.
        outlier_limit: Specify outlier limit for censoring.
        regress_goforit: Set GOFORIT level in 3dDeconvolve.
        regress_bandpass: Specify bandpass limits to remain after regress.
        regress_jobs: Number of jobs to use in 3dDeconvolve.
        regress_mot_deriv: Regress motion derivatives (yes/no).
        regress_opts_3d_d: Specify extra options for 3dDeconvolve.
        reml_exec: Run 3dREMLfit (yes/no).
        run_clustsim: Run 3dClustSim (yes/no).
        sid: Set subject ID.
        stim: Set list of stim timing files.
        stim_basis: Set basis functions for stim classes.
        stim_label: Set stim file labels.
        stim_type: Set stim types for stim classes.
        stim_wildcard: Use wildcard for stim files (yes/no).
        tcat_nfirst: Set number of TRs to remove per run.
        tlrc_base: Specify anat for standard space alignment.
        tlrc_ok_maxite: Pass -OK_maxite to @auto_tlrc (yes/no).
        tlrc_opts_at: Specify extra options for @auto_tlrc.
        volreg_base: Set volreg base string (first/third/last).
        verb: Set verbose level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UberSubjectPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UBER_SUBJECT_PY_METADATA)
    cargs = []
    cargs.append("uber_subject.py")
    if qt_opts is not None:
        cargs.extend([
            "-qt_opts",
            qt_opts
        ])
    if svar is not None:
        cargs.extend([
            "-svar",
            svar
        ])
    if cvar is not None:
        cargs.extend([
            "-cvar",
            cvar
        ])
    if no_gui:
        cargs.append("-no_gui")
    if print_ap_command:
        cargs.append("-print_ap_command")
    if save_ap_command is not None:
        cargs.extend([
            "-save_ap_command",
            save_ap_command
        ])
    if exec_ap_command:
        cargs.append("-exec_ap_command")
    if exec_proc_script:
        cargs.append("-exec_proc_script")
    if align_cost is not None:
        cargs.extend([
            "-align_cost",
            align_cost
        ])
    if align_giant_move is not None:
        cargs.extend([
            "-align_giant_move",
            align_giant_move
        ])
    if align_opts_aea is not None:
        cargs.extend([
            "-align_opts_aea",
            align_opts_aea
        ])
    if anal_domain is not None:
        cargs.extend([
            "-anal_domain",
            anal_domain
        ])
    if anal_type is not None:
        cargs.extend([
            "-anal_type",
            anal_type
        ])
    if anat is not None:
        cargs.extend([
            "-anat",
            execution.input_file(anat)
        ])
    if anat_has_skull is not None:
        cargs.extend([
            "-anat_has_skull",
            anat_has_skull
        ])
    if blocks is not None:
        cargs.extend([
            "-blocks",
            blocks
        ])
    if blur_size is not None:
        cargs.extend([
            "-blur_size",
            str(blur_size)
        ])
    if epi is not None:
        cargs.extend([
            "-epi",
            epi
        ])
    if epi_wildcard is not None:
        cargs.extend([
            "-epi_wildcard",
            epi_wildcard
        ])
    if gid is not None:
        cargs.extend([
            "-gid",
            gid
        ])
    if gltsym is not None:
        cargs.extend([
            "-gltsym",
            gltsym
        ])
    if gltsym_label is not None:
        cargs.extend([
            "-gltsym_label",
            gltsym_label
        ])
    if motion_limit is not None:
        cargs.extend([
            "-motion_limit",
            str(motion_limit)
        ])
    if outlier_limit is not None:
        cargs.extend([
            "-outlier_limit",
            str(outlier_limit)
        ])
    if regress_goforit is not None:
        cargs.extend([
            "-regress_GOFORIT",
            str(regress_goforit)
        ])
    if regress_bandpass is not None:
        cargs.extend([
            "-regress_bandpass",
            regress_bandpass
        ])
    if regress_jobs is not None:
        cargs.extend([
            "-regress_jobs",
            str(regress_jobs)
        ])
    if regress_mot_deriv is not None:
        cargs.extend([
            "-regress_mot_deriv",
            regress_mot_deriv
        ])
    if regress_opts_3d_d is not None:
        cargs.extend([
            "-regress_opts_3dD",
            regress_opts_3d_d
        ])
    if reml_exec is not None:
        cargs.extend([
            "-reml_exec",
            reml_exec
        ])
    if run_clustsim is not None:
        cargs.extend([
            "-run_clustsim",
            run_clustsim
        ])
    if sid is not None:
        cargs.extend([
            "-sid",
            sid
        ])
    if stim is not None:
        cargs.extend([
            "-stim",
            execution.input_file(stim)
        ])
    if stim_basis is not None:
        cargs.extend([
            "-stim_basis",
            stim_basis
        ])
    if stim_label is not None:
        cargs.extend([
            "-stim_label",
            stim_label
        ])
    if stim_type is not None:
        cargs.extend([
            "-stim_type",
            stim_type
        ])
    if stim_wildcard is not None:
        cargs.extend([
            "-stim_wildcard",
            stim_wildcard
        ])
    if tcat_nfirst is not None:
        cargs.extend([
            "-tcat_nfirst",
            str(tcat_nfirst)
        ])
    if tlrc_base is not None:
        cargs.extend([
            "-tlrc_base",
            tlrc_base
        ])
    if tlrc_ok_maxite is not None:
        cargs.extend([
            "-tlrc_ok_maxite",
            tlrc_ok_maxite
        ])
    if tlrc_opts_at is not None:
        cargs.extend([
            "-tlrc_opts_at",
            tlrc_opts_at
        ])
    if volreg_base is not None:
        cargs.extend([
            "-volreg_base",
            volreg_base
        ])
    if verb is not None:
        cargs.extend([
            "-verb",
            verb
        ])
    ret = UberSubjectPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UBER_SUBJECT_PY_METADATA",
    "UberSubjectPyOutputs",
    "uber_subject_py",
]
