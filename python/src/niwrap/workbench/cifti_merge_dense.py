# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_MERGE_DENSE_METADATA = Metadata(
    id="ac9c1e2eade1767ad34b460fb5c4532e9b7ecedc",
    name="cifti-merge-dense",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiMergeDenseCifti:
    """
    specify an input cifti file
    """
    cifti_in: InputPathType
    """a cifti file to merge"""
    
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
        cargs.append("-cifti")
        cargs.append(execution.input_file(self.cifti_in))
        return cargs


class CiftiMergeDenseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_merge_dense(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_merge_dense(
    direction: str,
    cifti_out: str,
    opt_label_collision_action: str | None = None,
    cifti: list[CiftiMergeDenseCifti] = None,
    runner: Runner = None,
) -> CiftiMergeDenseOutputs:
    """
    cifti-merge-dense by Washington University School of Medicin.
    
    Merge cifti files along dense dimension.
    
    The input cifti files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Args:
        direction: which dimension to merge along, ROW or COLUMN.
        cifti_out: the output cifti file.
        opt_label_collision_action: how to handle conflicts between label keys:\
            'ERROR', 'FIRST', or 'LEGACY', default 'ERROR', use 'LEGACY' to match\
            v1.4.2 and earlier.
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiMergeDenseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_MERGE_DENSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-merge-dense")
    cargs.append(direction)
    cargs.append(cifti_out)
    if opt_label_collision_action is not None:
        cargs.extend(["-label-collision", opt_label_collision_action])
    if cifti is not None:
        cargs.extend([a for c in [s.run(execution) for s in cifti] for a in c])
    ret = CiftiMergeDenseOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_MERGE_DENSE_METADATA",
    "CiftiMergeDenseCifti",
    "CiftiMergeDenseOutputs",
    "cifti_merge_dense",
]
