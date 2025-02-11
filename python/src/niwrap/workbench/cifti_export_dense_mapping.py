# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_EXPORT_DENSE_MAPPING_METADATA = Metadata(
    id="fb57b1ad6ea2cecd7c20af72044952f21f5e3510.boutiques",
    name="cifti-export-dense-mapping",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiExportDenseMappingVolumeAllParameters = typing.TypedDict('CiftiExportDenseMappingVolumeAllParameters', {
    "__STYX_TYPE__": typing.Literal["volume_all"],
    "text_out": str,
    "opt_no_cifti_index": bool,
    "opt_structure": bool,
})
CiftiExportDenseMappingSurfaceParameters = typing.TypedDict('CiftiExportDenseMappingSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["surface"],
    "structure": str,
    "text_out": str,
    "opt_no_cifti_index": bool,
})
CiftiExportDenseMappingVolumeParameters = typing.TypedDict('CiftiExportDenseMappingVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["volume"],
    "structure": str,
    "text_out": str,
    "opt_no_cifti_index": bool,
})
CiftiExportDenseMappingParameters = typing.TypedDict('CiftiExportDenseMappingParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-export-dense-mapping"],
    "cifti": InputPathType,
    "direction": str,
    "volume_all": typing.NotRequired[CiftiExportDenseMappingVolumeAllParameters | None],
    "surface": typing.NotRequired[list[CiftiExportDenseMappingSurfaceParameters] | None],
    "volume": typing.NotRequired[list[CiftiExportDenseMappingVolumeParameters] | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "cifti-export-dense-mapping": cifti_export_dense_mapping_cargs,
        "volume_all": cifti_export_dense_mapping_volume_all_cargs,
        "surface": cifti_export_dense_mapping_surface_cargs,
        "volume": cifti_export_dense_mapping_volume_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


def cifti_export_dense_mapping_volume_all_params(
    text_out: str,
    opt_no_cifti_index: bool = False,
    opt_structure: bool = False,
) -> CiftiExportDenseMappingVolumeAllParameters:
    """
    Build parameters.
    
    Args:
        text_out: output - the output text file.
        opt_no_cifti_index: don't write the cifti index in the output file.
        opt_structure: write the structure each voxel belongs to in the output\
            file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume_all",
        "text_out": text_out,
        "opt_no_cifti_index": opt_no_cifti_index,
        "opt_structure": opt_structure,
    }
    return params


def cifti_export_dense_mapping_volume_all_cargs(
    params: CiftiExportDenseMappingVolumeAllParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-volume-all")
    cargs.append(params.get("text_out"))
    if params.get("opt_no_cifti_index"):
        cargs.append("-no-cifti-index")
    if params.get("opt_structure"):
        cargs.append("-structure")
    return cargs


def cifti_export_dense_mapping_surface_params(
    structure: str,
    text_out: str,
    opt_no_cifti_index: bool = False,
) -> CiftiExportDenseMappingSurfaceParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to output.
        text_out: output - the output text file.
        opt_no_cifti_index: don't write the cifti index in the output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface",
        "structure": structure,
        "text_out": text_out,
        "opt_no_cifti_index": opt_no_cifti_index,
    }
    return params


def cifti_export_dense_mapping_surface_cargs(
    params: CiftiExportDenseMappingSurfaceParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-surface")
    cargs.append(params.get("structure"))
    cargs.append(params.get("text_out"))
    if params.get("opt_no_cifti_index"):
        cargs.append("-no-cifti-index")
    return cargs


def cifti_export_dense_mapping_volume_params(
    structure: str,
    text_out: str,
    opt_no_cifti_index: bool = False,
) -> CiftiExportDenseMappingVolumeParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to output.
        text_out: output - the output text file.
        opt_no_cifti_index: don't write the cifti index in the output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume",
        "structure": structure,
        "text_out": text_out,
        "opt_no_cifti_index": opt_no_cifti_index,
    }
    return params


def cifti_export_dense_mapping_volume_cargs(
    params: CiftiExportDenseMappingVolumeParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-volume")
    cargs.append(params.get("structure"))
    cargs.append(params.get("text_out"))
    if params.get("opt_no_cifti_index"):
        cargs.append("-no-cifti-index")
    return cargs


class CiftiExportDenseMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_export_dense_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_export_dense_mapping_params(
    cifti: InputPathType,
    direction: str,
    volume_all: CiftiExportDenseMappingVolumeAllParameters | None = None,
    surface: list[CiftiExportDenseMappingSurfaceParameters] | None = None,
    volume: list[CiftiExportDenseMappingVolumeParameters] | None = None,
) -> CiftiExportDenseMappingParameters:
    """
    Build parameters.
    
    Args:
        cifti: the cifti file.
        direction: which direction to export the mapping from, ROW or COLUMN.
        volume_all: export the the mapping of all voxels.
        surface: export the the mapping of one surface structure.
        volume: export the the mapping of one volume structure.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-export-dense-mapping",
        "cifti": cifti,
        "direction": direction,
    }
    if volume_all is not None:
        params["volume_all"] = volume_all
    if surface is not None:
        params["surface"] = surface
    if volume is not None:
        params["volume"] = volume
    return params


def cifti_export_dense_mapping_cargs(
    params: CiftiExportDenseMappingParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-export-dense-mapping")
    cargs.append(execution.input_file(params.get("cifti")))
    cargs.append(params.get("direction"))
    if params.get("volume_all") is not None:
        cargs.extend(dyn_cargs(params.get("volume_all")["__STYXTYPE__"])(params.get("volume_all"), execution))
    if params.get("surface") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("surface")] for a in c])
    if params.get("volume") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("volume")] for a in c])
    return cargs


def cifti_export_dense_mapping_outputs(
    params: CiftiExportDenseMappingParameters,
    execution: Execution,
) -> CiftiExportDenseMappingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiExportDenseMappingOutputs(
        root=execution.output_file("."),
    )
    return ret


def cifti_export_dense_mapping_execute(
    params: CiftiExportDenseMappingParameters,
    execution: Execution,
) -> CiftiExportDenseMappingOutputs:
    """
    Write index to element mapping as text.
    
    This command produces text files that describe the mapping from cifti
    indices to surface vertices or voxels. All indices are zero-based. The
    default format for -surface is lines of the form:
    
    <cifti-index> <vertex>
    
    The default format for -volume and -volume-all is lines of the form:
    
    <cifti-index> <i> <j> <k>
    
    For each <structure> argument, use one of the following strings:
    
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
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiExportDenseMappingOutputs`).
    """
    cargs = cifti_export_dense_mapping_cargs(params, execution)
    ret = cifti_export_dense_mapping_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_export_dense_mapping(
    cifti: InputPathType,
    direction: str,
    volume_all: CiftiExportDenseMappingVolumeAllParameters | None = None,
    surface: list[CiftiExportDenseMappingSurfaceParameters] | None = None,
    volume: list[CiftiExportDenseMappingVolumeParameters] | None = None,
    runner: Runner | None = None,
) -> CiftiExportDenseMappingOutputs:
    """
    Write index to element mapping as text.
    
    This command produces text files that describe the mapping from cifti
    indices to surface vertices or voxels. All indices are zero-based. The
    default format for -surface is lines of the form:
    
    <cifti-index> <vertex>
    
    The default format for -volume and -volume-all is lines of the form:
    
    <cifti-index> <i> <j> <k>
    
    For each <structure> argument, use one of the following strings:
    
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
        cifti: the cifti file.
        direction: which direction to export the mapping from, ROW or COLUMN.
        volume_all: export the the mapping of all voxels.
        surface: export the the mapping of one surface structure.
        volume: export the the mapping of one volume structure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiExportDenseMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_EXPORT_DENSE_MAPPING_METADATA)
    params = cifti_export_dense_mapping_params(cifti=cifti, direction=direction, volume_all=volume_all, surface=surface, volume=volume)
    return cifti_export_dense_mapping_execute(params, execution)


__all__ = [
    "CIFTI_EXPORT_DENSE_MAPPING_METADATA",
    "CiftiExportDenseMappingOutputs",
    "CiftiExportDenseMappingParameters",
    "CiftiExportDenseMappingSurfaceParameters",
    "CiftiExportDenseMappingVolumeAllParameters",
    "CiftiExportDenseMappingVolumeParameters",
    "cifti_export_dense_mapping",
    "cifti_export_dense_mapping_params",
    "cifti_export_dense_mapping_surface_params",
    "cifti_export_dense_mapping_volume_all_params",
    "cifti_export_dense_mapping_volume_params",
]
