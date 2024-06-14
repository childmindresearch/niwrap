# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FOCI_RESAMPLE_METADATA = Metadata(
    id="5877e1dbf154fcb8f46f76576910a8919aff2038",
    name="foci-resample",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class FociResampleLeftSurfaces:
    """
    the left surfaces for resampling
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
class FociResampleRightSurfaces:
    """
    the right surfaces for resampling
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
class FociResampleCerebellumSurfaces:
    """
    the cerebellum surfaces for resampling
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


class FociResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    foci_out: OutputPathType
    """the output foci file"""


def foci_resample(
    foci_in: InputPathType,
    foci_out: InputPathType,
    left_surfaces: FociResampleLeftSurfaces | None = None,
    right_surfaces: FociResampleRightSurfaces | None = None,
    cerebellum_surfaces: FociResampleCerebellumSurfaces | None = None,
    opt_discard_distance_from_surface: bool = False,
    opt_restore_xyz: bool = False,
    runner: Runner = None,
) -> FociResampleOutputs:
    """
    foci-resample by Washington University School of Medicin.
    
    Project foci to a different surface.
    
    Unprojects foci from the <current-surf> for the structure, then projects
    them to <new-surf>. If the foci have meaningful distances above or below the
    surface, use anatomical surfaces. If the foci should be on the surface, use
    registered spheres and the options -discard-distance-from-surface and
    -restore-xyz.
    
    Args:
        foci_in: the input foci file.
        foci_out: the output foci file.
        left_surfaces: the left surfaces for resampling.
        right_surfaces: the right surfaces for resampling.
        cerebellum_surfaces: the cerebellum surfaces for resampling.
        opt_discard_distance_from_surface: ignore the distance the foci are\
            above or below the current surface.
        opt_restore_xyz: put the original xyz coordinates into the foci, rather\
            than the coordinates obtained from unprojection.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-foci-resample")
    cargs.append(execution.input_file(foci_in))
    cargs.append(execution.input_file(foci_out))
    if left_surfaces is not None:
        cargs.extend(["-left-surfaces", *left_surfaces.run(execution)])
    if right_surfaces is not None:
        cargs.extend(["-right-surfaces", *right_surfaces.run(execution)])
    if cerebellum_surfaces is not None:
        cargs.extend(["-cerebellum-surfaces", *cerebellum_surfaces.run(execution)])
    if opt_discard_distance_from_surface:
        cargs.append("-discard-distance-from-surface")
    if opt_restore_xyz:
        cargs.append("-restore-xyz")
    ret = FociResampleOutputs(
        root=execution.output_file("."),
        foci_out=execution.output_file(f"{pathlib.Path(foci_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FOCI_RESAMPLE_METADATA",
    "FociResampleCerebellumSurfaces",
    "FociResampleLeftSurfaces",
    "FociResampleOutputs",
    "FociResampleRightSurfaces",
    "foci_resample",
]