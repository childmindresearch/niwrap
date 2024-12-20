# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA = Metadata(
    id="9bc6b682807328e6a1b0c7145d97a8a86f72e627.boutiques",
    name="volume-label-to-surface-mapping",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class VolumeLabelToSurfaceMappingRibbonConstrained:
    """
    use ribbon constrained mapping algorithm.
    """
    inner_surf: InputPathType
    """the inner surface of the ribbon"""
    outer_surf: InputPathType
    """the outer surface of the ribbon"""
    opt_volume_roi_roi_volume: InputPathType | None = None
    """use a volume roi: the volume file"""
    opt_voxel_subdiv_subdiv_num: int | None = None
    """voxel divisions while estimating voxel weights: number of subdivisions,
    default 3"""
    opt_thin_columns: bool = False
    """use non-overlapping polyhedra"""
    
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
        cargs.append("-ribbon-constrained")
        cargs.append(execution.input_file(self.inner_surf))
        cargs.append(execution.input_file(self.outer_surf))
        if self.opt_volume_roi_roi_volume is not None:
            cargs.extend([
                "-volume-roi",
                execution.input_file(self.opt_volume_roi_roi_volume)
            ])
        if self.opt_voxel_subdiv_subdiv_num is not None:
            cargs.extend([
                "-voxel-subdiv",
                str(self.opt_voxel_subdiv_subdiv_num)
            ])
        if self.opt_thin_columns:
            cargs.append("-thin-columns")
        return cargs


class VolumeLabelToSurfaceMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_to_surface_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output gifti label file"""


def volume_label_to_surface_mapping(
    volume: InputPathType,
    surface: InputPathType,
    label_out: str,
    ribbon_constrained: VolumeLabelToSurfaceMappingRibbonConstrained | None = None,
    opt_subvol_select_subvol: str | None = None,
    runner: Runner | None = None,
) -> VolumeLabelToSurfaceMappingOutputs:
    """
    Map a label volume to a surface label file.
    
    Map label volume data to a surface. If -ribbon-constrained is not specified,
    uses the enclosing voxel method. The ribbon mapping method constructs a
    polyhedron from the vertex's neighbors on each surface, and estimates the
    amount of this polyhedron's volume that falls inside any nearby voxels, to
    use as the weights for a popularity comparison. If -thin-columns is
    specified, the polyhedron uses the edge midpoints and triangle centroids, so
    that neighboring vertices do not have overlapping polyhedra. This may
    require increasing -voxel-subdiv to get enough samples in each voxel to
    reliably land inside these smaller polyhedra. The volume ROI is useful to
    exclude partial volume effects of voxels the surfaces pass through, and will
    cause the mapping to ignore voxels that don't have a positive value in the
    mask. The subdivision number specifies how it approximates the amount of the
    volume the polyhedron intersects, by splitting each voxel into NxNxN pieces,
    and checking whether the center of each piece is inside the polyhedron. If
    you have very large voxels, consider increasing this if you get unexpected
    unlabeled vertices in your output.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume: the volume to map data from.
        surface: the surface to map the data onto.
        label_out: the output gifti label file.
        ribbon_constrained: use ribbon constrained mapping algorithm.
        opt_subvol_select_subvol: select a single subvolume to map: the\
            subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelToSurfaceMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-label-to-surface-mapping")
    cargs.append(execution.input_file(volume))
    cargs.append(execution.input_file(surface))
    cargs.append(label_out)
    if ribbon_constrained is not None:
        cargs.extend(ribbon_constrained.run(execution))
    if opt_subvol_select_subvol is not None:
        cargs.extend([
            "-subvol-select",
            opt_subvol_select_subvol
        ])
    ret = VolumeLabelToSurfaceMappingOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(label_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA",
    "VolumeLabelToSurfaceMappingOutputs",
    "VolumeLabelToSurfaceMappingRibbonConstrained",
    "volume_label_to_surface_mapping",
]
