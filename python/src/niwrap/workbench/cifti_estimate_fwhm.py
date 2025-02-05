# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_ESTIMATE_FWHM_METADATA = Metadata(
    id="5a208f16e948f98d42112e2bc0a3ea2e8dd7f5ff.boutiques",
    name="cifti-estimate-fwhm",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiEstimateFwhmWholeFileParameters = typing.TypedDict('CiftiEstimateFwhmWholeFileParameters', {
    "__STYX_TYPE__": typing.Literal["whole_file"],
    "opt_demean": bool,
})
CiftiEstimateFwhmSurfaceParameters = typing.TypedDict('CiftiEstimateFwhmSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["surface"],
    "structure": str,
    "surface": InputPathType,
})
CiftiEstimateFwhmParameters = typing.TypedDict('CiftiEstimateFwhmParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-estimate-fwhm"],
    "cifti": InputPathType,
    "opt_merged_volume": bool,
    "opt_column_column": typing.NotRequired[int | None],
    "whole_file": typing.NotRequired[CiftiEstimateFwhmWholeFileParameters | None],
    "surface": typing.NotRequired[list[CiftiEstimateFwhmSurfaceParameters] | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "cifti-estimate-fwhm": cifti_estimate_fwhm_cargs,
        "whole_file": cifti_estimate_fwhm_whole_file_cargs,
        "surface": cifti_estimate_fwhm_surface_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {}
    return vt.get(t)


def cifti_estimate_fwhm_whole_file_params(
    opt_demean: bool = False,
) -> CiftiEstimateFwhmWholeFileParameters:
    """
    Build parameters.
    
    Args:
        opt_demean: subtract the mean image before estimating smoothness.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "whole_file",
        "opt_demean": opt_demean,
    }
    return params


def cifti_estimate_fwhm_whole_file_cargs(
    params: CiftiEstimateFwhmWholeFileParameters,
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
    cargs.append("-whole-file")
    if params.get("opt_demean"):
        cargs.append("-demean")
    return cargs


def cifti_estimate_fwhm_surface_params(
    structure: str,
    surface: InputPathType,
) -> CiftiEstimateFwhmSurfaceParameters:
    """
    Build parameters.
    
    Args:
        structure: what structure to use this surface for.
        surface: the surface file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface",
        "structure": structure,
        "surface": surface,
    }
    return params


def cifti_estimate_fwhm_surface_cargs(
    params: CiftiEstimateFwhmSurfaceParameters,
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
    cargs.append(execution.input_file(params.get("surface")))
    return cargs


class CiftiEstimateFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_estimate_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_estimate_fwhm_params(
    cifti: InputPathType,
    opt_merged_volume: bool = False,
    opt_column_column: int | None = None,
    whole_file: CiftiEstimateFwhmWholeFileParameters | None = None,
    surface: list[CiftiEstimateFwhmSurfaceParameters] | None = None,
) -> CiftiEstimateFwhmParameters:
    """
    Build parameters.
    
    Args:
        cifti: the input cifti file.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        opt_column_column: only output estimates for one column: the column\
            number.
        whole_file: estimate for the whole file at once, not each column\
            separately.
        surface: specify an input surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-estimate-fwhm",
        "cifti": cifti,
        "opt_merged_volume": opt_merged_volume,
    }
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if whole_file is not None:
        params["whole_file"] = whole_file
    if surface is not None:
        params["surface"] = surface
    return params


def cifti_estimate_fwhm_cargs(
    params: CiftiEstimateFwhmParameters,
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
    cargs.append("-cifti-estimate-fwhm")
    cargs.append(execution.input_file(params.get("cifti")))
    if params.get("opt_merged_volume"):
        cargs.append("-merged-volume")
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            str(params.get("opt_column_column"))
        ])
    if params.get("whole_file") is not None:
        cargs.extend(dyn_cargs(params.get("whole_file")["__STYXTYPE__"])(params.get("whole_file"), execution))
    if params.get("surface") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("surface")] for a in c])
    return cargs


def cifti_estimate_fwhm_outputs(
    params: CiftiEstimateFwhmParameters,
    execution: Execution,
) -> CiftiEstimateFwhmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiEstimateFwhmOutputs(
        root=execution.output_file("."),
    )
    return ret


def cifti_estimate_fwhm_execute(
    params: CiftiEstimateFwhmParameters,
    execution: Execution,
) -> CiftiEstimateFwhmOutputs:
    """
    Estimate fwhm smoothness of a cifti file.
    
    Estimate the smoothness of the components of the cifti file, printing the
    estimates to standard output. If -merged-volume is used, all voxels are used
    as a single component, rather than separated by structure.
    
    <structure> must be one of the following:
    
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
        NamedTuple of outputs (described in `CiftiEstimateFwhmOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_estimate_fwhm_cargs(params, execution)
    ret = cifti_estimate_fwhm_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_estimate_fwhm(
    cifti: InputPathType,
    opt_merged_volume: bool = False,
    opt_column_column: int | None = None,
    whole_file: CiftiEstimateFwhmWholeFileParameters | None = None,
    surface: list[CiftiEstimateFwhmSurfaceParameters] | None = None,
    runner: Runner | None = None,
) -> CiftiEstimateFwhmOutputs:
    """
    Estimate fwhm smoothness of a cifti file.
    
    Estimate the smoothness of the components of the cifti file, printing the
    estimates to standard output. If -merged-volume is used, all voxels are used
    as a single component, rather than separated by structure.
    
    <structure> must be one of the following:
    
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
        cifti: the input cifti file.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        opt_column_column: only output estimates for one column: the column\
            number.
        whole_file: estimate for the whole file at once, not each column\
            separately.
        surface: specify an input surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiEstimateFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ESTIMATE_FWHM_METADATA)
    params = cifti_estimate_fwhm_params(cifti=cifti, opt_merged_volume=opt_merged_volume, opt_column_column=opt_column_column, whole_file=whole_file, surface=surface)
    return cifti_estimate_fwhm_execute(params, execution)


__all__ = [
    "CIFTI_ESTIMATE_FWHM_METADATA",
    "CiftiEstimateFwhmOutputs",
    "CiftiEstimateFwhmParameters",
    "CiftiEstimateFwhmSurfaceParameters",
    "CiftiEstimateFwhmWholeFileParameters",
    "cifti_estimate_fwhm",
    "cifti_estimate_fwhm_params",
    "cifti_estimate_fwhm_surface_params",
    "cifti_estimate_fwhm_whole_file_params",
]
