# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_SET_SPACE_METADATA = Metadata(
    id="d2c5c3138f090c0357158891fa98a52186eace23",
    name="volume-set-space",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeSetSpacePlumb:
    """
    set via axis order and spacing/offset
    """
    
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
        return cargs


@dataclasses.dataclass
class VolumeSetSpaceSform:
    """
    set via a nifti sform
    """
    
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
        return cargs


@dataclasses.dataclass
class VolumeSetSpaceFile:
    """
    copy spacing info from volume file with matching dimensions
    """
    opt_ignore_dims: bool = False
    """copy the spacing info even if the dimensions don't match"""
    
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
        if self.opt_ignore_dims:
            cargs.append("-ignore-dims")
        return cargs


class VolumeSetSpaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_set_space(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_set_space(
    volume_in: InputPathType,
    volume_out: str,
    plumb: VolumeSetSpacePlumb | None = None,
    sform: VolumeSetSpaceSform | None = None,
    file: VolumeSetSpaceFile | None = None,
    runner: Runner = None,
) -> VolumeSetSpaceOutputs:
    """
    volume-set-space by Washington University School of Medicin.
    
    Change volume space information.
    
    Writes a copy of the volume file, with the spacing information changed as
    specified. No reordering of the voxel data occurs, see -volume-reorient to
    change the volume indexing order and reorder the voxels to match. Exactly
    one of -plumb, -sform, or -file must be specified.
    
    Args:
        volume_in: the input volume.
        volume_out: output - the output volume.
        plumb: set via axis order and spacing/offset.
        sform: set via a nifti sform.
        file: copy spacing info from volume file with matching dimensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeSetSpaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_SET_SPACE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-set-space")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_out)
    if plumb is not None:
        cargs.extend(["-plumb", *plumb.run(execution)])
    if sform is not None:
        cargs.extend(["-sform", *sform.run(execution)])
    if file is not None:
        cargs.extend(["-file", *file.run(execution)])
    ret = VolumeSetSpaceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_SET_SPACE_METADATA",
    "VolumeSetSpaceFile",
    "VolumeSetSpaceOutputs",
    "VolumeSetSpacePlumb",
    "VolumeSetSpaceSform",
    "volume_set_space",
]