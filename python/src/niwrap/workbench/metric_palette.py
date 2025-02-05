# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_PALETTE_METADATA = Metadata(
    id="6600f0fd7050affe6aeef2d792aa2f3d3a26d6e8.boutiques",
    name="metric-palette",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricPalettePosPercentParameters = typing.TypedDict('MetricPalettePosPercentParameters', {
    "__STYX_TYPE__": typing.Literal["pos_percent"],
    "pos_min__": float,
    "pos_max__": float,
})
MetricPaletteNegPercentParameters = typing.TypedDict('MetricPaletteNegPercentParameters', {
    "__STYX_TYPE__": typing.Literal["neg_percent"],
    "neg_min__": float,
    "neg_max__": float,
})
MetricPalettePosUserParameters = typing.TypedDict('MetricPalettePosUserParameters', {
    "__STYX_TYPE__": typing.Literal["pos_user"],
    "pos_min_user": float,
    "pos_max_user": float,
})
MetricPaletteNegUserParameters = typing.TypedDict('MetricPaletteNegUserParameters', {
    "__STYX_TYPE__": typing.Literal["neg_user"],
    "neg_min_user": float,
    "neg_max_user": float,
})
MetricPaletteThresholdingParameters = typing.TypedDict('MetricPaletteThresholdingParameters', {
    "__STYX_TYPE__": typing.Literal["thresholding"],
    "type": str,
    "test": str,
    "min": float,
    "max": float,
})
MetricPaletteParameters = typing.TypedDict('MetricPaletteParameters', {
    "__STYX_TYPE__": typing.Literal["metric-palette"],
    "metric": str,
    "mode": str,
    "opt_column_column": typing.NotRequired[str | None],
    "pos_percent": typing.NotRequired[MetricPalettePosPercentParameters | None],
    "neg_percent": typing.NotRequired[MetricPaletteNegPercentParameters | None],
    "pos_user": typing.NotRequired[MetricPalettePosUserParameters | None],
    "neg_user": typing.NotRequired[MetricPaletteNegUserParameters | None],
    "opt_interpolate_interpolate": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_disp_pos_display": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_disp_neg_display": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_disp_zero_display": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_palette_name_name": typing.NotRequired[str | None],
    "thresholding": typing.NotRequired[MetricPaletteThresholdingParameters | None],
    "opt_inversion_type": typing.NotRequired[str | None],
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
        "metric-palette": metric_palette_cargs,
        "pos_percent": metric_palette_pos_percent_cargs,
        "neg_percent": metric_palette_neg_percent_cargs,
        "pos_user": metric_palette_pos_user_cargs,
        "neg_user": metric_palette_neg_user_cargs,
        "thresholding": metric_palette_thresholding_cargs,
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


def metric_palette_pos_percent_params(
    pos_min__: float,
    pos_max__: float,
) -> MetricPalettePosPercentParameters:
    """
    Build parameters.
    
    Args:
        pos_min__: the percentile for the least positive data.
        pos_max__: the percentile for the most positive data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pos_percent",
        "pos_min__": pos_min__,
        "pos_max__": pos_max__,
    }
    return params


def metric_palette_pos_percent_cargs(
    params: MetricPalettePosPercentParameters,
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
    cargs.append("-pos-percent")
    cargs.append(str(params.get("pos_min__")))
    cargs.append(str(params.get("pos_max__")))
    return cargs


def metric_palette_neg_percent_params(
    neg_min__: float,
    neg_max__: float,
) -> MetricPaletteNegPercentParameters:
    """
    Build parameters.
    
    Args:
        neg_min__: the percentile for the least negative data.
        neg_max__: the percentile for the most negative data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "neg_percent",
        "neg_min__": neg_min__,
        "neg_max__": neg_max__,
    }
    return params


def metric_palette_neg_percent_cargs(
    params: MetricPaletteNegPercentParameters,
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
    cargs.append("-neg-percent")
    cargs.append(str(params.get("neg_min__")))
    cargs.append(str(params.get("neg_max__")))
    return cargs


def metric_palette_pos_user_params(
    pos_min_user: float,
    pos_max_user: float,
) -> MetricPalettePosUserParameters:
    """
    Build parameters.
    
    Args:
        pos_min_user: the value for the least positive data.
        pos_max_user: the value for the most positive data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pos_user",
        "pos_min_user": pos_min_user,
        "pos_max_user": pos_max_user,
    }
    return params


def metric_palette_pos_user_cargs(
    params: MetricPalettePosUserParameters,
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
    cargs.append("-pos-user")
    cargs.append(str(params.get("pos_min_user")))
    cargs.append(str(params.get("pos_max_user")))
    return cargs


def metric_palette_neg_user_params(
    neg_min_user: float,
    neg_max_user: float,
) -> MetricPaletteNegUserParameters:
    """
    Build parameters.
    
    Args:
        neg_min_user: the value for the least negative data.
        neg_max_user: the value for the most negative data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "neg_user",
        "neg_min_user": neg_min_user,
        "neg_max_user": neg_max_user,
    }
    return params


def metric_palette_neg_user_cargs(
    params: MetricPaletteNegUserParameters,
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
    cargs.append("-neg-user")
    cargs.append(str(params.get("neg_min_user")))
    cargs.append(str(params.get("neg_max_user")))
    return cargs


def metric_palette_thresholding_params(
    type_: str,
    test: str,
    min_: float,
    max_: float,
) -> MetricPaletteThresholdingParameters:
    """
    Build parameters.
    
    Args:
        type_: thresholding setting.
        test: show values inside or outside thresholds.
        min_: lower threshold.
        max_: upper threshold.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "thresholding",
        "type": type_,
        "test": test,
        "min": min_,
        "max": max_,
    }
    return params


def metric_palette_thresholding_cargs(
    params: MetricPaletteThresholdingParameters,
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
    cargs.append("-thresholding")
    cargs.append(params.get("type"))
    cargs.append(params.get("test"))
    cargs.append(str(params.get("min")))
    cargs.append(str(params.get("max")))
    return cargs


class MetricPaletteOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_palette(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metric_palette_params(
    metric: str,
    mode: str,
    opt_column_column: str | None = None,
    pos_percent: MetricPalettePosPercentParameters | None = None,
    neg_percent: MetricPaletteNegPercentParameters | None = None,
    pos_user: MetricPalettePosUserParameters | None = None,
    neg_user: MetricPaletteNegUserParameters | None = None,
    opt_interpolate_interpolate: typing.Literal["true", "false"] | None = None,
    opt_disp_pos_display: typing.Literal["true", "false"] | None = None,
    opt_disp_neg_display: typing.Literal["true", "false"] | None = None,
    opt_disp_zero_display: typing.Literal["true", "false"] | None = None,
    opt_palette_name_name: str | None = None,
    thresholding: MetricPaletteThresholdingParameters | None = None,
    opt_inversion_type: str | None = None,
) -> MetricPaletteParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric to modify.
        mode: the mapping mode.
        opt_column_column: select a single column: the column number or name.
        pos_percent: percentage min/max for positive data coloring.
        neg_percent: percentage min/max for negative data coloring.
        pos_user: user min/max values for positive data coloring.
        neg_user: user min/max values for negative data coloring.
        opt_interpolate_interpolate: interpolate colors: boolean, whether to\
            interpolate.
        opt_disp_pos_display: display positive data: boolean, whether to\
            display.
        opt_disp_neg_display: display positive data: boolean, whether to\
            display.
        opt_disp_zero_display: display data closer to zero than the min cutoff:\
            boolean, whether to display.
        opt_palette_name_name: set the palette used: the name of the palette.
        thresholding: set the thresholding.
        opt_inversion_type: specify palette inversion: the type of inversion.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-palette",
        "metric": metric,
        "mode": mode,
    }
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if pos_percent is not None:
        params["pos_percent"] = pos_percent
    if neg_percent is not None:
        params["neg_percent"] = neg_percent
    if pos_user is not None:
        params["pos_user"] = pos_user
    if neg_user is not None:
        params["neg_user"] = neg_user
    if opt_interpolate_interpolate is not None:
        params["opt_interpolate_interpolate"] = opt_interpolate_interpolate
    if opt_disp_pos_display is not None:
        params["opt_disp_pos_display"] = opt_disp_pos_display
    if opt_disp_neg_display is not None:
        params["opt_disp_neg_display"] = opt_disp_neg_display
    if opt_disp_zero_display is not None:
        params["opt_disp_zero_display"] = opt_disp_zero_display
    if opt_palette_name_name is not None:
        params["opt_palette_name_name"] = opt_palette_name_name
    if thresholding is not None:
        params["thresholding"] = thresholding
    if opt_inversion_type is not None:
        params["opt_inversion_type"] = opt_inversion_type
    return params


def metric_palette_cargs(
    params: MetricPaletteParameters,
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
    cargs.append("-metric-palette")
    cargs.append(params.get("metric"))
    cargs.append(params.get("mode"))
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("pos_percent") is not None:
        cargs.extend(dyn_cargs(params.get("pos_percent")["__STYXTYPE__"])(params.get("pos_percent"), execution))
    if params.get("neg_percent") is not None:
        cargs.extend(dyn_cargs(params.get("neg_percent")["__STYXTYPE__"])(params.get("neg_percent"), execution))
    if params.get("pos_user") is not None:
        cargs.extend(dyn_cargs(params.get("pos_user")["__STYXTYPE__"])(params.get("pos_user"), execution))
    if params.get("neg_user") is not None:
        cargs.extend(dyn_cargs(params.get("neg_user")["__STYXTYPE__"])(params.get("neg_user"), execution))
    if params.get("opt_interpolate_interpolate") is not None:
        cargs.extend([
            "-interpolate",
            params.get("opt_interpolate_interpolate")
        ])
    if params.get("opt_disp_pos_display") is not None:
        cargs.extend([
            "-disp-pos",
            params.get("opt_disp_pos_display")
        ])
    if params.get("opt_disp_neg_display") is not None:
        cargs.extend([
            "-disp-neg",
            params.get("opt_disp_neg_display")
        ])
    if params.get("opt_disp_zero_display") is not None:
        cargs.extend([
            "-disp-zero",
            params.get("opt_disp_zero_display")
        ])
    if params.get("opt_palette_name_name") is not None:
        cargs.extend([
            "-palette-name",
            params.get("opt_palette_name_name")
        ])
    if params.get("thresholding") is not None:
        cargs.extend(dyn_cargs(params.get("thresholding")["__STYXTYPE__"])(params.get("thresholding"), execution))
    if params.get("opt_inversion_type") is not None:
        cargs.extend([
            "-inversion",
            params.get("opt_inversion_type")
        ])
    return cargs


def metric_palette_outputs(
    params: MetricPaletteParameters,
    execution: Execution,
) -> MetricPaletteOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricPaletteOutputs(
        root=execution.output_file("."),
    )
    return ret


def metric_palette_execute(
    params: MetricPaletteParameters,
    execution: Execution,
) -> MetricPaletteOutputs:
    """
    Set the palette of a metric file.
    
    The original metric file is overwritten with the modified version. By
    default, all columns of the metric file are adjusted to the new settings,
    use the -column option to change only one column. Mapping settings not
    specified in options will be taken from the first column. The <mode>
    argument must be one of the following:
    
    MODE_AUTO_SCALE
    MODE_AUTO_SCALE_ABSOLUTE_PERCENTAGE
    MODE_AUTO_SCALE_PERCENTAGE
    MODE_USER_SCALE
    
    The <name> argument to -palette-name must be one of the following:
    
    ROY-BIG-BL
    videen_style
    Gray_Interp_Positive
    Gray_Interp
    PSYCH-FIXED
    RBGYR20
    RBGYR20P
    RYGBR4_positive
    RGRBR_mirror90_pos
    Orange-Yellow
    POS_NEG_ZERO
    red-yellow
    blue-lightblue
    FSL
    power_surf
    black-red
    black-green
    black-blue
    black-red-positive
    black-green-positive
    black-blue-positive
    blue-black-green
    blue-black-red
    red-black-green
    fsl_red
    fsl_green
    fsl_blue
    fsl_yellow
    RedWhiteBlue
    cool-warm
    spectral
    RY-BC-BL
    magma
    JET256
    PSYCH
    PSYCH-NO-NONE
    ROY-BIG
    clear_brain
    fidl
    raich4_clrmid
    raich6_clrmid
    HSB8_clrmid
    POS_NEG
    Special-RGB-Volume
    
    The <type> argument to -thresholding must be one of the following:
    
    THRESHOLD_TYPE_OFF
    THRESHOLD_TYPE_NORMAL
    THRESHOLD_TYPE_FILE
    
    The <test> argument to -thresholding must be one of the following:
    
    THRESHOLD_TEST_SHOW_OUTSIDE
    THRESHOLD_TEST_SHOW_INSIDE
    
    The <type> argument to -inversion must be one of the following:
    
    OFF
    POSITIVE_WITH_NEGATIVE
    POSITIVE_NEGATIVE_SEPARATE
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricPaletteOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = metric_palette_cargs(params, execution)
    ret = metric_palette_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_palette(
    metric: str,
    mode: str,
    opt_column_column: str | None = None,
    pos_percent: MetricPalettePosPercentParameters | None = None,
    neg_percent: MetricPaletteNegPercentParameters | None = None,
    pos_user: MetricPalettePosUserParameters | None = None,
    neg_user: MetricPaletteNegUserParameters | None = None,
    opt_interpolate_interpolate: typing.Literal["true", "false"] | None = None,
    opt_disp_pos_display: typing.Literal["true", "false"] | None = None,
    opt_disp_neg_display: typing.Literal["true", "false"] | None = None,
    opt_disp_zero_display: typing.Literal["true", "false"] | None = None,
    opt_palette_name_name: str | None = None,
    thresholding: MetricPaletteThresholdingParameters | None = None,
    opt_inversion_type: str | None = None,
    runner: Runner | None = None,
) -> MetricPaletteOutputs:
    """
    Set the palette of a metric file.
    
    The original metric file is overwritten with the modified version. By
    default, all columns of the metric file are adjusted to the new settings,
    use the -column option to change only one column. Mapping settings not
    specified in options will be taken from the first column. The <mode>
    argument must be one of the following:
    
    MODE_AUTO_SCALE
    MODE_AUTO_SCALE_ABSOLUTE_PERCENTAGE
    MODE_AUTO_SCALE_PERCENTAGE
    MODE_USER_SCALE
    
    The <name> argument to -palette-name must be one of the following:
    
    ROY-BIG-BL
    videen_style
    Gray_Interp_Positive
    Gray_Interp
    PSYCH-FIXED
    RBGYR20
    RBGYR20P
    RYGBR4_positive
    RGRBR_mirror90_pos
    Orange-Yellow
    POS_NEG_ZERO
    red-yellow
    blue-lightblue
    FSL
    power_surf
    black-red
    black-green
    black-blue
    black-red-positive
    black-green-positive
    black-blue-positive
    blue-black-green
    blue-black-red
    red-black-green
    fsl_red
    fsl_green
    fsl_blue
    fsl_yellow
    RedWhiteBlue
    cool-warm
    spectral
    RY-BC-BL
    magma
    JET256
    PSYCH
    PSYCH-NO-NONE
    ROY-BIG
    clear_brain
    fidl
    raich4_clrmid
    raich6_clrmid
    HSB8_clrmid
    POS_NEG
    Special-RGB-Volume
    
    The <type> argument to -thresholding must be one of the following:
    
    THRESHOLD_TYPE_OFF
    THRESHOLD_TYPE_NORMAL
    THRESHOLD_TYPE_FILE
    
    The <test> argument to -thresholding must be one of the following:
    
    THRESHOLD_TEST_SHOW_OUTSIDE
    THRESHOLD_TEST_SHOW_INSIDE
    
    The <type> argument to -inversion must be one of the following:
    
    OFF
    POSITIVE_WITH_NEGATIVE
    POSITIVE_NEGATIVE_SEPARATE
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        metric: the metric to modify.
        mode: the mapping mode.
        opt_column_column: select a single column: the column number or name.
        pos_percent: percentage min/max for positive data coloring.
        neg_percent: percentage min/max for negative data coloring.
        pos_user: user min/max values for positive data coloring.
        neg_user: user min/max values for negative data coloring.
        opt_interpolate_interpolate: interpolate colors: boolean, whether to\
            interpolate.
        opt_disp_pos_display: display positive data: boolean, whether to\
            display.
        opt_disp_neg_display: display positive data: boolean, whether to\
            display.
        opt_disp_zero_display: display data closer to zero than the min cutoff:\
            boolean, whether to display.
        opt_palette_name_name: set the palette used: the name of the palette.
        thresholding: set the thresholding.
        opt_inversion_type: specify palette inversion: the type of inversion.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricPaletteOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_PALETTE_METADATA)
    params = metric_palette_params(metric=metric, mode=mode, opt_column_column=opt_column_column, pos_percent=pos_percent, neg_percent=neg_percent, pos_user=pos_user, neg_user=neg_user, opt_interpolate_interpolate=opt_interpolate_interpolate, opt_disp_pos_display=opt_disp_pos_display, opt_disp_neg_display=opt_disp_neg_display, opt_disp_zero_display=opt_disp_zero_display, opt_palette_name_name=opt_palette_name_name, thresholding=thresholding, opt_inversion_type=opt_inversion_type)
    return metric_palette_execute(params, execution)


__all__ = [
    "METRIC_PALETTE_METADATA",
    "MetricPaletteNegPercentParameters",
    "MetricPaletteNegUserParameters",
    "MetricPaletteOutputs",
    "MetricPaletteParameters",
    "MetricPalettePosPercentParameters",
    "MetricPalettePosUserParameters",
    "MetricPaletteThresholdingParameters",
    "metric_palette",
    "metric_palette_neg_percent_params",
    "metric_palette_neg_user_params",
    "metric_palette_params",
    "metric_palette_pos_percent_params",
    "metric_palette_pos_user_params",
    "metric_palette_thresholding_params",
]
