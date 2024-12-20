# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_REPLACE_STRUCTURE_METADATA = Metadata(
    id="9c3e18b84a0136395940d5ee50cb45c790ea3cbb.boutiques",
    name="cifti-replace-structure",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiReplaceStructureVolumeAll:
    """
    replace the data in all volume components.
    """
    volume: InputPathType
    """the input volume"""
    opt_from_cropped: bool = False
    """the input is cropped to the size of the data"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-volume-all")
        cargs.append(execution.input_file(self.volume))
        if self.opt_from_cropped:
            cargs.append("-from-cropped")
        return cargs


@dataclasses.dataclass
class CiftiReplaceStructureLabel:
    """
    replace the data in a surface label component.
    """
    structure: str
    """the structure to replace the data of"""
    label: InputPathType
    """the input label file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-label")
        cargs.append(self.structure)
        cargs.append(execution.input_file(self.label))
        return cargs


@dataclasses.dataclass
class CiftiReplaceStructureMetric:
    """
    replace the data in a surface component.
    """
    structure: str
    """the structure to replace the data of"""
    metric: InputPathType
    """the input metric"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-metric")
        cargs.append(self.structure)
        cargs.append(execution.input_file(self.metric))
        return cargs


@dataclasses.dataclass
class CiftiReplaceStructureVolume:
    """
    replace the data in a volume component.
    """
    structure: str
    """the structure to replace the data of"""
    volume: InputPathType
    """the input volume"""
    opt_from_cropped: bool = False
    """the input is cropped to the size of the component"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-volume")
        cargs.append(self.structure)
        cargs.append(execution.input_file(self.volume))
        if self.opt_from_cropped:
            cargs.append("-from-cropped")
        return cargs


class CiftiReplaceStructureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_replace_structure(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_replace_structure(
    cifti: str,
    direction: str,
    volume_all: CiftiReplaceStructureVolumeAll | None = None,
    opt_discard_unused_labels: bool = False,
    opt_label_collision_action: str | None = None,
    label: list[CiftiReplaceStructureLabel] | None = None,
    metric: list[CiftiReplaceStructureMetric] | None = None,
    volume: list[CiftiReplaceStructureVolume] | None = None,
    runner: Runner | None = None,
) -> CiftiReplaceStructureOutputs:
    """
    Replace data in a structure in a cifti file.
    
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
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti: the cifti to modify.
        direction: which dimension to interpret as a single map, ROW or COLUMN.
        volume_all: replace the data in all volume components.
        opt_discard_unused_labels: when operating on a dlabel file, drop any\
            unused label keys from the label table.
        opt_label_collision_action: how to handle conflicts between label keys:\
            'ERROR', 'LEFT_SURFACE_FIRST', or 'LEGACY', default 'ERROR', use\
            'LEGACY' to match v1.4.2 and earlier.
        label: replace the data in a surface label component.
        metric: replace the data in a surface component.
        volume: replace the data in a volume component.
        runner: Command runner.
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
    if volume_all is not None:
        cargs.extend(volume_all.run(execution))
    if opt_discard_unused_labels:
        cargs.append("-discard-unused-labels")
    if opt_label_collision_action is not None:
        cargs.extend([
            "-label-collision",
            opt_label_collision_action
        ])
    if label is not None:
        cargs.extend([a for c in [s.run(execution) for s in label] for a in c])
    if metric is not None:
        cargs.extend([a for c in [s.run(execution) for s in metric] for a in c])
    if volume is not None:
        cargs.extend([a for c in [s.run(execution) for s in volume] for a in c])
    ret = CiftiReplaceStructureOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_REPLACE_STRUCTURE_METADATA",
    "CiftiReplaceStructureLabel",
    "CiftiReplaceStructureMetric",
    "CiftiReplaceStructureOutputs",
    "CiftiReplaceStructureVolume",
    "CiftiReplaceStructureVolumeAll",
    "cifti_replace_structure",
]
