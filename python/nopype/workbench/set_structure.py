# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.775864

import typing

from ..styxdefs import *


SET_STRUCTURE_METADATA = Metadata(
    id="6f18e3c2892fa9d2e7cb52fb7ce2c01193ef0494",
    name="set-structure",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SetStructureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `set_structure(...)`.
    """


def set_structure(
    runner: Runner,
    data_file: str,
    structure: str,
    opt_surface_type_type: str | None = None,
    opt_surface_secondary_type_secondary_type: str | None = None,
) -> SetStructureOutputs:
    """
    SET STRUCTURE OF A DATA FILE.
    
    The existing file is modified and rewritten to the same filename. Valid
    values for the structure name are:
    
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
    THALAMUS_RIGHT
    
    Valid names for the surface type are:
    
    UNKNOWN
    RECONSTRUCTION
    ANATOMICAL
    INFLATED
    VERY_INFLATED
    SPHERICAL
    SEMI_SPHERICAL
    ELLIPSOID
    FLAT
    HULL
    
    Valid names for the surface secondary type are:
    
    INVALID
    GRAY_WHITE
    MIDTHICKNESS
    PIAL
    
    Args:
        runner: Command runner
        data_file: the file to set the structure of
        structure: the structure to set the file to
        opt_surface_type_type: set the type of a surface (only used if file is a
            surface file): name of surface type
        opt_surface_secondary_type_secondary_type: set the secondary type of a
            surface (only used if file is a surface file): name of surface secondary
            type
    Returns:
        NamedTuple of outputs (described in `SetStructureOutputs`).
    """
    execution = runner.start_execution(SET_STRUCTURE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-set-structure")
    cargs.append(data_file)
    cargs.append(structure)
    if opt_surface_type_type is not None:
        cargs.extend(["-surface-type", opt_surface_type_type])
    if opt_surface_secondary_type_secondary_type is not None:
        cargs.extend(["-surface-secondary-type", opt_surface_secondary_type_secondary_type])
    ret = SetStructureOutputs(
    )
    execution.run(cargs)
    return ret
