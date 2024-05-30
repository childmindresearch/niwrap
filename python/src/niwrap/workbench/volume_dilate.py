# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


VOLUME_DILATE_METADATA = Metadata(
    id="798e2a6e854094d1153b72bf12651be07004014e",
    name="volume-dilate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class PresmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Presmooth.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Presmooth:
    """
    apply presmoothing before computing gradient vectors, not recommended
    """
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
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> PresmoothOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `PresmoothOutputs`).
        """
        ret = PresmoothOutputs(
            root=execution.output_file("."),
        )
        return ret


class VolumeDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""
    presmooth: PresmoothOutputs
    """Subcommand outputs"""


def volume_dilate(
    volume: InputPathType,
    distance: float | int,
    method: str,
    volume_out: InputPathType,
    opt_exponent_exponent: float | int | None = None,
    opt_bad_voxel_roi_roi_volume: InputPathType | None = None,
    opt_data_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_legacy_cutoff: bool = False,
    opt_grad_extrapolate: bool = False,
    presmooth: Presmooth | None = None,
    runner: Runner = None,
) -> VolumeDilateOutputs:
    """
    volume-dilate by Washington University School of Medicin.
    
    Dilate a volume file.
    
    For all voxels that are designated as bad, if they neighbor a non-bad voxel
    with data or are within the specified distance of such a voxel, replace the
    value in the bad voxel with a value calculated from nearby non-bad voxels
    that have data, otherwise set the value to zero. No matter how small
    <distance> is, dilation will always use at least the face neighbor voxels.
    
    By default, voxels that have data with the value 0 are bad, specify
    -bad-voxel-roi to only count voxels as bad if they are selected by the roi.
    If -data-roi is not specified, all voxels are assumed to have data.
    
    To get the behavior of version 1.3.2 or earlier, use '-legacy-cutoff
    -exponent 2'.
    
    Valid values for <method> are:
    
    NEAREST - use the value from the nearest good voxel
    WEIGHTED - use a weighted average based on distance.
    
    Args:
        volume: the volume to dilate
        distance: distance in mm to dilate
        method: dilation method to use
        volume_out: the output volume
        opt_exponent_exponent: use a different exponent in the weighting
            function: exponent 'n' to use in (1 / (distance ^ n)) as the weighting
            function (default 7)
        opt_bad_voxel_roi_roi_volume: specify an roi of voxels to overwrite,
            rather than voxels with value zero: volume file, positive values denote
            voxels to have their values replaced
        opt_data_roi_roi_volume: specify an roi of where there is data: volume
            file, positive values denote voxels that have data
        opt_subvolume_subvol: select a single subvolume to dilate: the subvolume
            number or name
        opt_legacy_cutoff: use the v1.3.2 method of excluding voxels further
            than the dilation distance when calculating the dilated value
        opt_grad_extrapolate: additionally use the gradient to extrapolate,
            intended to be used with WEIGHTED
        presmooth: apply presmoothing before computing gradient vectors, not
            recommended
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_DILATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-dilate")
    cargs.append(execution.input_file(volume))
    cargs.append(str(distance))
    cargs.append(method)
    cargs.append(execution.input_file(volume_out))
    if opt_exponent_exponent is not None:
        cargs.extend(["-exponent", str(opt_exponent_exponent)])
    if opt_bad_voxel_roi_roi_volume is not None:
        cargs.extend(["-bad-voxel-roi", execution.input_file(opt_bad_voxel_roi_roi_volume)])
    if opt_data_roi_roi_volume is not None:
        cargs.extend(["-data-roi", execution.input_file(opt_data_roi_roi_volume)])
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    if opt_legacy_cutoff:
        cargs.append("-legacy-cutoff")
    if opt_grad_extrapolate:
        cargs.append("-grad-extrapolate")
    if presmooth is not None:
        cargs.extend(["-presmooth", *presmooth.run(execution)])
    ret = VolumeDilateOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
        presmooth=presmooth.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "Presmooth",
    "PresmoothOutputs",
    "VOLUME_DILATE_METADATA",
    "VolumeDilateOutputs",
    "volume_dilate",
]
