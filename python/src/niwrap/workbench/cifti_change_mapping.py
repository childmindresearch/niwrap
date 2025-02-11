# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_CHANGE_MAPPING_METADATA = Metadata(
    id="53f8c510829c70200ad060f067b228f1aa52da65.boutiques",
    name="cifti-change-mapping",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiChangeMappingSeriesParameters = typing.TypedDict('CiftiChangeMappingSeriesParameters', {
    "__STYX_TYPE__": typing.Literal["series"],
    "step": float,
    "start": float,
    "opt_unit_unit": typing.NotRequired[str | None],
})
CiftiChangeMappingScalarParameters = typing.TypedDict('CiftiChangeMappingScalarParameters', {
    "__STYX_TYPE__": typing.Literal["scalar"],
    "opt_name_file_file": typing.NotRequired[str | None],
})
CiftiChangeMappingFromCiftiParameters = typing.TypedDict('CiftiChangeMappingFromCiftiParameters', {
    "__STYX_TYPE__": typing.Literal["from_cifti"],
    "template_cifti": InputPathType,
    "direction": str,
})
CiftiChangeMappingParameters = typing.TypedDict('CiftiChangeMappingParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-change-mapping"],
    "data_cifti": InputPathType,
    "direction": str,
    "cifti_out": str,
    "series": typing.NotRequired[CiftiChangeMappingSeriesParameters | None],
    "scalar": typing.NotRequired[CiftiChangeMappingScalarParameters | None],
    "from_cifti": typing.NotRequired[CiftiChangeMappingFromCiftiParameters | None],
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
        "cifti-change-mapping": cifti_change_mapping_cargs,
        "series": cifti_change_mapping_series_cargs,
        "scalar": cifti_change_mapping_scalar_cargs,
        "from_cifti": cifti_change_mapping_from_cifti_cargs,
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
        "cifti-change-mapping": cifti_change_mapping_outputs,
    }.get(t)


def cifti_change_mapping_series_params(
    step: float,
    start: float,
    opt_unit_unit: str | None = None,
) -> CiftiChangeMappingSeriesParameters:
    """
    Build parameters.
    
    Args:
        step: increment between series points.
        start: start value of the series.
        opt_unit_unit: select unit for series (default SECOND): unit identifier.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "series",
        "step": step,
        "start": start,
    }
    if opt_unit_unit is not None:
        params["opt_unit_unit"] = opt_unit_unit
    return params


def cifti_change_mapping_series_cargs(
    params: CiftiChangeMappingSeriesParameters,
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
    cargs.append("-series")
    cargs.append(str(params.get("step")))
    cargs.append(str(params.get("start")))
    if params.get("opt_unit_unit") is not None:
        cargs.extend([
            "-unit",
            params.get("opt_unit_unit")
        ])
    return cargs


def cifti_change_mapping_scalar_params(
    opt_name_file_file: str | None = None,
) -> CiftiChangeMappingScalarParameters:
    """
    Build parameters.
    
    Args:
        opt_name_file_file: specify names for the maps: text file containing\
            map names, one per line.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "scalar",
    }
    if opt_name_file_file is not None:
        params["opt_name_file_file"] = opt_name_file_file
    return params


def cifti_change_mapping_scalar_cargs(
    params: CiftiChangeMappingScalarParameters,
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
    cargs.append("-scalar")
    if params.get("opt_name_file_file") is not None:
        cargs.extend([
            "-name-file",
            params.get("opt_name_file_file")
        ])
    return cargs


def cifti_change_mapping_from_cifti_params(
    template_cifti: InputPathType,
    direction: str,
) -> CiftiChangeMappingFromCiftiParameters:
    """
    Build parameters.
    
    Args:
        template_cifti: a cifti file containing the desired mapping.
        direction: which direction to copy the mapping from.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "from_cifti",
        "template_cifti": template_cifti,
        "direction": direction,
    }
    return params


def cifti_change_mapping_from_cifti_cargs(
    params: CiftiChangeMappingFromCiftiParameters,
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
    cargs.append("-from-cifti")
    cargs.append(execution.input_file(params.get("template_cifti")))
    cargs.append(params.get("direction"))
    return cargs


class CiftiChangeMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_change_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_change_mapping_params(
    data_cifti: InputPathType,
    direction: str,
    cifti_out: str,
    series: CiftiChangeMappingSeriesParameters | None = None,
    scalar: CiftiChangeMappingScalarParameters | None = None,
    from_cifti: CiftiChangeMappingFromCiftiParameters | None = None,
) -> CiftiChangeMappingParameters:
    """
    Build parameters.
    
    Args:
        data_cifti: the cifti file to use the data from.
        direction: which direction on <data-cifti> to replace the mapping.
        cifti_out: the output cifti file.
        series: set the mapping to series.
        scalar: set the mapping to scalar.
        from_cifti: copy mapping from another cifti file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-change-mapping",
        "data_cifti": data_cifti,
        "direction": direction,
        "cifti_out": cifti_out,
    }
    if series is not None:
        params["series"] = series
    if scalar is not None:
        params["scalar"] = scalar
    if from_cifti is not None:
        params["from_cifti"] = from_cifti
    return params


def cifti_change_mapping_cargs(
    params: CiftiChangeMappingParameters,
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
    cargs.append("-cifti-change-mapping")
    cargs.append(execution.input_file(params.get("data_cifti")))
    cargs.append(params.get("direction"))
    cargs.append(params.get("cifti_out"))
    if params.get("series") is not None:
        cargs.extend(dyn_cargs(params.get("series")["__STYXTYPE__"])(params.get("series"), execution))
    if params.get("scalar") is not None:
        cargs.extend(dyn_cargs(params.get("scalar")["__STYXTYPE__"])(params.get("scalar"), execution))
    if params.get("from_cifti") is not None:
        cargs.extend(dyn_cargs(params.get("from_cifti")["__STYXTYPE__"])(params.get("from_cifti"), execution))
    return cargs


def cifti_change_mapping_outputs(
    params: CiftiChangeMappingParameters,
    execution: Execution,
) -> CiftiChangeMappingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiChangeMappingOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_change_mapping_execute(
    params: CiftiChangeMappingParameters,
    execution: Execution,
) -> CiftiChangeMappingOutputs:
    """
    Convert to scalar, copy mapping, etc.
    
    Take an existing cifti file and change one of the mappings. Exactly one of
    -series, -scalar, or -from-cifti must be specified. The direction can be
    either an integer starting from 1, or the strings 'ROW' or 'COLUMN'.
    
    The argument to -unit must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiChangeMappingOutputs`).
    """
    cargs = cifti_change_mapping_cargs(params, execution)
    ret = cifti_change_mapping_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_change_mapping(
    data_cifti: InputPathType,
    direction: str,
    cifti_out: str,
    series: CiftiChangeMappingSeriesParameters | None = None,
    scalar: CiftiChangeMappingScalarParameters | None = None,
    from_cifti: CiftiChangeMappingFromCiftiParameters | None = None,
    runner: Runner | None = None,
) -> CiftiChangeMappingOutputs:
    """
    Convert to scalar, copy mapping, etc.
    
    Take an existing cifti file and change one of the mappings. Exactly one of
    -series, -scalar, or -from-cifti must be specified. The direction can be
    either an integer starting from 1, or the strings 'ROW' or 'COLUMN'.
    
    The argument to -unit must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        data_cifti: the cifti file to use the data from.
        direction: which direction on <data-cifti> to replace the mapping.
        cifti_out: the output cifti file.
        series: set the mapping to series.
        scalar: set the mapping to scalar.
        from_cifti: copy mapping from another cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiChangeMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CHANGE_MAPPING_METADATA)
    params = cifti_change_mapping_params(data_cifti=data_cifti, direction=direction, cifti_out=cifti_out, series=series, scalar=scalar, from_cifti=from_cifti)
    return cifti_change_mapping_execute(params, execution)


__all__ = [
    "CIFTI_CHANGE_MAPPING_METADATA",
    "CiftiChangeMappingFromCiftiParameters",
    "CiftiChangeMappingOutputs",
    "CiftiChangeMappingParameters",
    "CiftiChangeMappingScalarParameters",
    "CiftiChangeMappingSeriesParameters",
    "cifti_change_mapping",
    "cifti_change_mapping_from_cifti_params",
    "cifti_change_mapping_params",
    "cifti_change_mapping_scalar_params",
    "cifti_change_mapping_series_params",
]
