# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TEST_TUTORIALS_SH_METADATA = Metadata(
    id="12b91716710dd5b63abd67223200ca5920aafcec.boutiques",
    name="test_tutorials.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TestTutorialsShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `test_tutorials_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def test_tutorials_sh(
    all_tutorials: bool = False,
    quick_test: bool = False,
    auto_quit_freeview: bool = False,
    skip_all_guis: bool = False,
    skip_tk_guis: bool = False,
    skip_qdec_guis: bool = False,
    individual_subject: bool = False,
    troubleshooting: bool = False,
    group_analysis: bool = False,
    qdec: bool = False,
    longitudinal: bool = False,
    roi_analysis: bool = False,
    diffusion: bool = False,
    tracula: bool = False,
    fsfast: bool = False,
    multimodal: bool = False,
    runner: Runner | None = None,
) -> TestTutorialsShOutputs:
    """
    A script to run various tutorial commands, with options for skipping GUI
    components and focusing on specific tutorials.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        all_tutorials: Run all tutorials.
        quick_test: Perform a quick subset of commands.
        auto_quit_freeview: Automatically closes freeview after opening.
        skip_all_guis: Skips all commands that open a GUI.
        skip_tk_guis: Skips commands that open a tk GUI (tkmedit, tksurfer,\
            etc).
        skip_qdec_guis: Skips commands that open qdec.
        individual_subject: Do Interaction with Individual Subject Data\
            tutorial.
        troubleshooting: Do Troubleshooting tutorial.
        group_analysis: Do Group Analysis tutorial.
        qdec: Do QDEC tutorial.
        longitudinal: Do Longitudinal tutorial.
        roi_analysis: Do ROI Analysis tutorial.
        diffusion: Do Diffusion tutorial.
        tracula: Do TRACULA tutorial.
        fsfast: Do FSFASt tutorial.
        multimodal: Do Mulimodal tutorial.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TestTutorialsShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEST_TUTORIALS_SH_METADATA)
    cargs = []
    cargs.append("test_tutorials.sh")
    if all_tutorials:
        cargs.append("-all")
    if quick_test:
        cargs.append("-quick")
    if auto_quit_freeview:
        cargs.append("-auto_quit_freeview")
    if skip_all_guis:
        cargs.append("-skip_all_guis")
    if skip_tk_guis:
        cargs.append("-skip_tk_guis")
    if skip_qdec_guis:
        cargs.append("-skip_qdec_guis")
    if individual_subject:
        cargs.append("-individual_subject")
    if troubleshooting:
        cargs.append("-troubleshooting")
    if group_analysis:
        cargs.append("-group_analysis")
    if qdec:
        cargs.append("-qdec")
    if longitudinal:
        cargs.append("-longitudinal")
    if roi_analysis:
        cargs.append("-roi_analysis")
    if diffusion:
        cargs.append("-diffusion")
    if tracula:
        cargs.append("-tracula")
    if fsfast:
        cargs.append("-fsfast")
    if multimodal:
        cargs.append("-multimodal")
    ret = TestTutorialsShOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TEST_TUTORIALS_SH_METADATA",
    "TestTutorialsShOutputs",
    "test_tutorials_sh",
]
