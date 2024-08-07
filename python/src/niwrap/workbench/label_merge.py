# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

LABEL_MERGE_METADATA = Metadata(
    id="d7b51321c357157a56e0a33d9221afc1e53ec1f1",
    name="label-merge",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class LabelMergeUpTo:
    """
    use an inclusive range of columns
    """
    last_column: str
    """the number or name of the last column to include"""
    opt_reverse: bool = False
    """use the range in reverse order"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-up-to")
        cargs.append(self.last_column)
        if self.opt_reverse:
            cargs.append("-reverse")
        return cargs


@dataclasses.dataclass
class LabelMergeColumn:
    """
    select a single column to use
    """
    column_: str
    """the column number or name"""
    up_to: LabelMergeUpTo | None = None
    """use an inclusive range of columns"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-column")
        cargs.append(self.column_)
        if self.up_to is not None:
            cargs.extend(self.up_to.run(execution))
        return cargs


@dataclasses.dataclass
class LabelMergeLabel:
    """
    specify an input label
    """
    label_in: InputPathType
    """a label file to use columns from"""
    column: list[LabelMergeColumn] | None = None
    """select a single column to use"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-label")
        cargs.append(execution.input_file(self.label_in))
        if self.column is not None:
            cargs.extend([a for c in [s.run(execution) for s in self.column] for a in c])
        return cargs


class LabelMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label"""


def label_merge(
    label_out: str,
    label: list[LabelMergeLabel] | None = None,
    runner: Runner | None = None,
) -> LabelMergeOutputs:
    """
    label-merge by Washington University School of Medicin.
    
    Merge label files into a new file.
    
    Takes one or more label files and constructs a new label file by
    concatenating columns from them. The input files must have the same number
    of vertices and the same structure.
    
    Example: wb_command -label-merge out.label.gii -label first.label.gii
    -column 1 -label second.label.gii
    
    This example would take the first column from first.label.gii and all
    subvolumes from second.label.gii, and write these to out.label.gii.
    
    Args:
        label_out: the output label.
        label: specify an input label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-merge")
    cargs.append(label_out)
    if label is not None:
        cargs.extend([a for c in [s.run(execution) for s in label] for a in c])
    ret = LabelMergeOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(f"{label_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_MERGE_METADATA",
    "LabelMergeColumn",
    "LabelMergeLabel",
    "LabelMergeOutputs",
    "LabelMergeUpTo",
    "label_merge",
]
