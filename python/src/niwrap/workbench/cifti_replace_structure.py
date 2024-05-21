# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_REPLACE_STRUCTURE_METADATA = Metadata(
    id="98efad4168990f6c1d3bd457ba507cba0f097330",
    name="cifti-replace-structure",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiReplaceStructureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_replace_structure(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_replace_structure(
    cifti: str,
    direction: str,
    opt_volume_all_volume: InputPathType | None = None,
    opt_discard_unused_labels: bool = False,
    opt_label_collision_action: str | None = None,
    runner: Runner = None,
) -> CiftiReplaceStructureOutputs:
    """
    cifti-replace-structure by Washington University School of Medicin.
    
    REPLACE DATA IN A STRUCTURE IN A CIFTI FILE.
    
    This is a fairly low-level command, you probably want to use
    -cifti-create-dense-from-template instead.
    
    You must specify at least one of -metric, -label, -volume, or -volume-all
    for this command to do anything. Input volumes must line up with the output
    of -cifti-separate. For dtseries/dscalar, use COLUMN, and if your dconn
    matrix will be fully symmetric, COLUMN is more efficient. The -volume-all
    option must not be specified when using a -volume option. A -metric option
    must not be specified when using a -label option, and is not recommended on
    a label-type cifti file. For each <structure> argument, use one of the
    following strings:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Args:
        cifti: the cifti to modify
        direction: which dimension to interpret as a single map, ROW or COLUMN
        opt_volume_all_volume: replace the data in all volume components: the
            input volume
        opt_discard_unused_labels: when operating on a dlabel file, drop any
            unused label keys from the label table
        opt_label_collision_action: how to handle conflicts between label keys:
            'ERROR', 'LEFT_SURFACE_FIRST', or 'LEGACY', default 'ERROR', use
            'LEGACY' to match v1.4.2 and earlier
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiReplaceStructureOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_REPLACE_STRUCTURE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-replace-structure")
    cargs.append(cifti)
    cargs.append(direction)
    if opt_volume_all_volume is not None:
        cargs.extend(["-volume-all", execution.input_file(opt_volume_all_volume)])
    if opt_discard_unused_labels:
        cargs.append("-discard-unused-labels")
    if opt_label_collision_action is not None:
        cargs.extend(["-label-collision", opt_label_collision_action])
    ret = CiftiReplaceStructureOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
