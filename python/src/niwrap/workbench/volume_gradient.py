# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_GRADIENT_METADATA = Metadata(
    id="3aa54de009f773b6af3db24f165ff7c614a4bbfe",
    name="volume-gradient",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeGradientPresmooth:
    """
    smooth the volume before computing the gradient
    """
    kernel: float | int
    """the size of the gaussian smoothing kernel in mm, as sigma by default"""
    opt_fwhm: bool = False
    """kernel size is FWHM, not sigma"""
    
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
        cargs.append("-presmooth")
        cargs.append(str(self.kernel))
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs


class VolumeGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output gradient magnitude volume"""
    vector_volume_out: OutputPathType
    """the vectors as a volume file"""


def volume_gradient(
    volume_in: InputPathType,
    volume_out: str,
    vector_volume_out: str,
    presmooth: VolumeGradientPresmooth | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_vectors: bool = False,
    opt_subvolume_subvol: str | None = None,
    runner: Runner = None,
) -> VolumeGradientOutputs:
    """
    volume-gradient by Washington University School of Medicin.
    
    Gradient of a volume file.
    
    Computes the gradient of the volume by doing linear regressions for each
    voxel, considering only its face neighbors unless too few face neighbors
    exist. The gradient vector is constructed from the partial derivatives of
    the resulting linear function, and the magnitude of this vector is the
    output. If specified, the volume vector output is arranged with the x, y,
    and z components from a subvolume as consecutive subvolumes.
    
    Args:
        volume_in: the input volume.
        volume_out: the output gradient magnitude volume.
        vector_volume_out: the vectors as a volume file.
        presmooth: smooth the volume before computing the gradient.
        opt_roi_roi_volume: select a region of interest to take the gradient\
            of: the region to take the gradient within.
        opt_vectors: output vectors.
        opt_subvolume_subvol: select a single subvolume to take the gradient\
            of: the subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_GRADIENT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-gradient")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_out)
    if presmooth is not None:
        cargs.extend(presmooth.run(execution))
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if opt_vectors:
        cargs.append("-vectors")
    cargs.append(vector_volume_out)
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    ret = VolumeGradientOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{volume_out}"),
        vector_volume_out=execution.output_file(f"{vector_volume_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_GRADIENT_METADATA",
    "VolumeGradientOutputs",
    "VolumeGradientPresmooth",
    "volume_gradient",
]
