# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PROBTRACKX_DOT_CONVERT_METADATA = Metadata(
    id="a166bee9e05b7717d215d29b5221c732cd06e6fb.boutiques",
    name="probtrackx-dot-convert",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
ProbtrackxDotConvertRowVoxelsParameters = typing.TypedDict('ProbtrackxDotConvertRowVoxelsParameters', {
    "__STYX_TYPE__": typing.Literal["row_voxels"],
    "voxel_list_file": str,
    "label_vol": InputPathType,
})
ProbtrackxDotConvertRowCiftiParameters = typing.TypedDict('ProbtrackxDotConvertRowCiftiParameters', {
    "__STYX_TYPE__": typing.Literal["row_cifti"],
    "cifti": InputPathType,
    "direction": str,
})
ProbtrackxDotConvertColVoxelsParameters = typing.TypedDict('ProbtrackxDotConvertColVoxelsParameters', {
    "__STYX_TYPE__": typing.Literal["col_voxels"],
    "voxel_list_file": str,
    "label_vol": InputPathType,
})
ProbtrackxDotConvertColCiftiParameters = typing.TypedDict('ProbtrackxDotConvertColCiftiParameters', {
    "__STYX_TYPE__": typing.Literal["col_cifti"],
    "cifti": InputPathType,
    "direction": str,
})
ProbtrackxDotConvertParameters = typing.TypedDict('ProbtrackxDotConvertParameters', {
    "__STYX_TYPE__": typing.Literal["probtrackx-dot-convert"],
    "dot_file": str,
    "cifti_out": str,
    "row_voxels": typing.NotRequired[ProbtrackxDotConvertRowVoxelsParameters | None],
    "opt_row_surface_roi_metric": typing.NotRequired[InputPathType | None],
    "row_cifti": typing.NotRequired[ProbtrackxDotConvertRowCiftiParameters | None],
    "col_voxels": typing.NotRequired[ProbtrackxDotConvertColVoxelsParameters | None],
    "opt_col_surface_roi_metric": typing.NotRequired[InputPathType | None],
    "col_cifti": typing.NotRequired[ProbtrackxDotConvertColCiftiParameters | None],
    "opt_transpose": bool,
    "opt_make_symmetric": bool,
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
        "probtrackx-dot-convert": probtrackx_dot_convert_cargs,
        "row_voxels": probtrackx_dot_convert_row_voxels_cargs,
        "row_cifti": probtrackx_dot_convert_row_cifti_cargs,
        "col_voxels": probtrackx_dot_convert_col_voxels_cargs,
        "col_cifti": probtrackx_dot_convert_col_cifti_cargs,
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
        "probtrackx-dot-convert": probtrackx_dot_convert_outputs,
        "row_voxels": probtrackx_dot_convert_row_voxels_outputs,
        "row_cifti": probtrackx_dot_convert_row_cifti_outputs,
        "col_voxels": probtrackx_dot_convert_col_voxels_outputs,
        "col_cifti": probtrackx_dot_convert_col_cifti_outputs,
    }.get(t)


def probtrackx_dot_convert_row_voxels_params(
    voxel_list_file: str,
    label_vol: InputPathType,
) -> ProbtrackxDotConvertRowVoxelsParameters:
    """
    Build parameters.
    
    Args:
        voxel_list_file: a text file containing IJK indices for the voxels used.
        label_vol: a label volume with the dimensions and sform used, with\
            structure labels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "row_voxels",
        "voxel_list_file": voxel_list_file,
        "label_vol": label_vol,
    }
    return params


def probtrackx_dot_convert_row_voxels_cargs(
    params: ProbtrackxDotConvertRowVoxelsParameters,
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
    cargs.append("-row-voxels")
    cargs.append(params.get("voxel_list_file"))
    cargs.append(execution.input_file(params.get("label_vol")))
    return cargs


def probtrackx_dot_convert_row_cifti_params(
    cifti: InputPathType,
    direction: str,
) -> ProbtrackxDotConvertRowCiftiParameters:
    """
    Build parameters.
    
    Args:
        cifti: the cifti file to take the mapping from.
        direction: which dimension to take the mapping along, ROW or COLUMN.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "row_cifti",
        "cifti": cifti,
        "direction": direction,
    }
    return params


def probtrackx_dot_convert_row_cifti_cargs(
    params: ProbtrackxDotConvertRowCiftiParameters,
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
    cargs.append("-row-cifti")
    cargs.append(execution.input_file(params.get("cifti")))
    cargs.append(params.get("direction"))
    return cargs


def probtrackx_dot_convert_col_voxels_params(
    voxel_list_file: str,
    label_vol: InputPathType,
) -> ProbtrackxDotConvertColVoxelsParameters:
    """
    Build parameters.
    
    Args:
        voxel_list_file: a text file containing IJK indices for the voxels used.
        label_vol: a label volume with the dimensions and sform used, with\
            structure labels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "col_voxels",
        "voxel_list_file": voxel_list_file,
        "label_vol": label_vol,
    }
    return params


def probtrackx_dot_convert_col_voxels_cargs(
    params: ProbtrackxDotConvertColVoxelsParameters,
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
    cargs.append("-col-voxels")
    cargs.append(params.get("voxel_list_file"))
    cargs.append(execution.input_file(params.get("label_vol")))
    return cargs


def probtrackx_dot_convert_col_cifti_params(
    cifti: InputPathType,
    direction: str,
) -> ProbtrackxDotConvertColCiftiParameters:
    """
    Build parameters.
    
    Args:
        cifti: the cifti file to take the mapping from.
        direction: which dimension to take the mapping along, ROW or COLUMN.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "col_cifti",
        "cifti": cifti,
        "direction": direction,
    }
    return params


def probtrackx_dot_convert_col_cifti_cargs(
    params: ProbtrackxDotConvertColCiftiParameters,
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
    cargs.append("-col-cifti")
    cargs.append(execution.input_file(params.get("cifti")))
    cargs.append(params.get("direction"))
    return cargs


class ProbtrackxDotConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `probtrackx_dot_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def probtrackx_dot_convert_params(
    dot_file: str,
    cifti_out: str,
    row_voxels: ProbtrackxDotConvertRowVoxelsParameters | None = None,
    opt_row_surface_roi_metric: InputPathType | None = None,
    row_cifti: ProbtrackxDotConvertRowCiftiParameters | None = None,
    col_voxels: ProbtrackxDotConvertColVoxelsParameters | None = None,
    opt_col_surface_roi_metric: InputPathType | None = None,
    col_cifti: ProbtrackxDotConvertColCiftiParameters | None = None,
    opt_transpose: bool = False,
    opt_make_symmetric: bool = False,
) -> ProbtrackxDotConvertParameters:
    """
    Build parameters.
    
    Args:
        dot_file: input .dot file.
        cifti_out: output cifti file.
        row_voxels: the output mapping along a row will be voxels.
        opt_row_surface_roi_metric: the output mapping along a row will be\
            surface vertices: a metric file with positive values on all vertices\
            used.
        row_cifti: take the mapping along a row from a cifti file.
        col_voxels: the output mapping along a column will be voxels.
        opt_col_surface_roi_metric: the output mapping along a column will be\
            surface vertices: a metric file with positive values on all vertices\
            used.
        col_cifti: take the mapping along a column from a cifti file.
        opt_transpose: transpose the input matrix.
        opt_make_symmetric: transform half-square input into full matrix output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "probtrackx-dot-convert",
        "dot_file": dot_file,
        "cifti_out": cifti_out,
        "opt_transpose": opt_transpose,
        "opt_make_symmetric": opt_make_symmetric,
    }
    if row_voxels is not None:
        params["row_voxels"] = row_voxels
    if opt_row_surface_roi_metric is not None:
        params["opt_row_surface_roi_metric"] = opt_row_surface_roi_metric
    if row_cifti is not None:
        params["row_cifti"] = row_cifti
    if col_voxels is not None:
        params["col_voxels"] = col_voxels
    if opt_col_surface_roi_metric is not None:
        params["opt_col_surface_roi_metric"] = opt_col_surface_roi_metric
    if col_cifti is not None:
        params["col_cifti"] = col_cifti
    return params


def probtrackx_dot_convert_cargs(
    params: ProbtrackxDotConvertParameters,
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
    cargs.append("-probtrackx-dot-convert")
    cargs.append(params.get("dot_file"))
    cargs.append(params.get("cifti_out"))
    if params.get("row_voxels") is not None:
        cargs.extend(dyn_cargs(params.get("row_voxels")["__STYXTYPE__"])(params.get("row_voxels"), execution))
    if params.get("opt_row_surface_roi_metric") is not None:
        cargs.extend([
            "-row-surface",
            execution.input_file(params.get("opt_row_surface_roi_metric"))
        ])
    if params.get("row_cifti") is not None:
        cargs.extend(dyn_cargs(params.get("row_cifti")["__STYXTYPE__"])(params.get("row_cifti"), execution))
    if params.get("col_voxels") is not None:
        cargs.extend(dyn_cargs(params.get("col_voxels")["__STYXTYPE__"])(params.get("col_voxels"), execution))
    if params.get("opt_col_surface_roi_metric") is not None:
        cargs.extend([
            "-col-surface",
            execution.input_file(params.get("opt_col_surface_roi_metric"))
        ])
    if params.get("col_cifti") is not None:
        cargs.extend(dyn_cargs(params.get("col_cifti")["__STYXTYPE__"])(params.get("col_cifti"), execution))
    if params.get("opt_transpose"):
        cargs.append("-transpose")
    if params.get("opt_make_symmetric"):
        cargs.append("-make-symmetric")
    return cargs


def probtrackx_dot_convert_outputs(
    params: ProbtrackxDotConvertParameters,
    execution: Execution,
) -> ProbtrackxDotConvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ProbtrackxDotConvertOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def probtrackx_dot_convert_execute(
    params: ProbtrackxDotConvertParameters,
    execution: Execution,
) -> ProbtrackxDotConvertOutputs:
    """
    Convert a .dot file from probtrackx to cifti.
    
    NOTE: exactly one -row option and one -col option must be used.
    
    If the input file does not have its indexes sorted in the correct ordering,
    this command may take longer than expected. Specifying -transpose will
    transpose the input matrix before trying to put its values into the cifti
    file, which is currently needed for at least matrix2 in order to display it
    as intended. How the cifti file is displayed is based on which -row option
    is specified: if -row-voxels is specified, then it will display data on
    volume slices. The label names in the label volume(s) must have the
    following names, other names are ignored:
    
    
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
        NamedTuple of outputs (described in `ProbtrackxDotConvertOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = probtrackx_dot_convert_cargs(params, execution)
    ret = probtrackx_dot_convert_outputs(params, execution)
    execution.run(cargs)
    return ret


def probtrackx_dot_convert(
    dot_file: str,
    cifti_out: str,
    row_voxels: ProbtrackxDotConvertRowVoxelsParameters | None = None,
    opt_row_surface_roi_metric: InputPathType | None = None,
    row_cifti: ProbtrackxDotConvertRowCiftiParameters | None = None,
    col_voxels: ProbtrackxDotConvertColVoxelsParameters | None = None,
    opt_col_surface_roi_metric: InputPathType | None = None,
    col_cifti: ProbtrackxDotConvertColCiftiParameters | None = None,
    opt_transpose: bool = False,
    opt_make_symmetric: bool = False,
    runner: Runner | None = None,
) -> ProbtrackxDotConvertOutputs:
    """
    Convert a .dot file from probtrackx to cifti.
    
    NOTE: exactly one -row option and one -col option must be used.
    
    If the input file does not have its indexes sorted in the correct ordering,
    this command may take longer than expected. Specifying -transpose will
    transpose the input matrix before trying to put its values into the cifti
    file, which is currently needed for at least matrix2 in order to display it
    as intended. How the cifti file is displayed is based on which -row option
    is specified: if -row-voxels is specified, then it will display data on
    volume slices. The label names in the label volume(s) must have the
    following names, other names are ignored:
    
    
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
        dot_file: input .dot file.
        cifti_out: output cifti file.
        row_voxels: the output mapping along a row will be voxels.
        opt_row_surface_roi_metric: the output mapping along a row will be\
            surface vertices: a metric file with positive values on all vertices\
            used.
        row_cifti: take the mapping along a row from a cifti file.
        col_voxels: the output mapping along a column will be voxels.
        opt_col_surface_roi_metric: the output mapping along a column will be\
            surface vertices: a metric file with positive values on all vertices\
            used.
        col_cifti: take the mapping along a column from a cifti file.
        opt_transpose: transpose the input matrix.
        opt_make_symmetric: transform half-square input into full matrix output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ProbtrackxDotConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PROBTRACKX_DOT_CONVERT_METADATA)
    params = probtrackx_dot_convert_params(dot_file=dot_file, cifti_out=cifti_out, row_voxels=row_voxels, opt_row_surface_roi_metric=opt_row_surface_roi_metric, row_cifti=row_cifti, col_voxels=col_voxels, opt_col_surface_roi_metric=opt_col_surface_roi_metric, col_cifti=col_cifti, opt_transpose=opt_transpose, opt_make_symmetric=opt_make_symmetric)
    return probtrackx_dot_convert_execute(params, execution)


__all__ = [
    "PROBTRACKX_DOT_CONVERT_METADATA",
    "ProbtrackxDotConvertColCiftiParameters",
    "ProbtrackxDotConvertColVoxelsParameters",
    "ProbtrackxDotConvertOutputs",
    "ProbtrackxDotConvertParameters",
    "ProbtrackxDotConvertRowCiftiParameters",
    "ProbtrackxDotConvertRowVoxelsParameters",
    "probtrackx_dot_convert",
    "probtrackx_dot_convert_col_cifti_params",
    "probtrackx_dot_convert_col_voxels_params",
    "probtrackx_dot_convert_params",
    "probtrackx_dot_convert_row_cifti_params",
    "probtrackx_dot_convert_row_voxels_params",
]
