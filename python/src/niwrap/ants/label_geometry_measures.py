# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL_GEOMETRY_MEASURES_METADATA = Metadata(
    id="e7ce3202e62bc39e7b15a1562ae20a5cef322440.boutiques",
    name="LabelGeometryMeasures",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
LabelGeometryMeasuresParameters = typing.TypedDict('LabelGeometryMeasuresParameters', {
    "__STYX_TYPE__": typing.Literal["LabelGeometryMeasures"],
    "image_dimension": int,
    "label_image": InputPathType,
    "intensity_image": typing.NotRequired[str | None],
    "csv_file": typing.NotRequired[InputPathType | None],
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
        "LabelGeometryMeasures": label_geometry_measures_cargs,
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
    vt = {
        "LabelGeometryMeasures": label_geometry_measures_outputs,
    }
    return vt.get(t)


class LabelGeometryMeasuresOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_geometry_measures(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_csv: OutputPathType | None
    """The CSV file containing the geometry measures."""


def label_geometry_measures_params(
    image_dimension: int,
    label_image: InputPathType,
    intensity_image: str | None = None,
    csv_file: InputPathType | None = None,
) -> LabelGeometryMeasuresParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimensionality of the input images (e.g., 2 for\
            2D, 3 for 3D).
        label_image: The label image on which geometry measures are computed.
        intensity_image: An optional intensity image for computing\
            intensity-weighted measures. Use "none" or "na" if not provided.
        csv_file: The output file where the geometry measures are written in\
            CSV format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "LabelGeometryMeasures",
        "image_dimension": image_dimension,
        "label_image": label_image,
    }
    if intensity_image is not None:
        params["intensity_image"] = intensity_image
    if csv_file is not None:
        params["csv_file"] = csv_file
    return params


def label_geometry_measures_cargs(
    params: LabelGeometryMeasuresParameters,
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
    cargs.append("LabelGeometryMeasures")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("label_image")))
    if params.get("intensity_image") is not None:
        cargs.append(params.get("intensity_image"))
    if params.get("csv_file") is not None:
        cargs.append(execution.input_file(params.get("csv_file")))
    return cargs


def label_geometry_measures_outputs(
    params: LabelGeometryMeasuresParameters,
    execution: Execution,
) -> LabelGeometryMeasuresOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelGeometryMeasuresOutputs(
        root=execution.output_file("."),
        output_csv=execution.output_file(pathlib.Path(params.get("csv_file")).name) if (params.get("csv_file") is not None) else None,
    )
    return ret


def label_geometry_measures_execute(
    params: LabelGeometryMeasuresParameters,
    execution: Execution,
) -> LabelGeometryMeasuresOutputs:
    """
    This tool computes various geometry measures on a label image, optionally using
    an intensity image, and outputs the results to a CSV file.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelGeometryMeasuresOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = label_geometry_measures_cargs(params, execution)
    ret = label_geometry_measures_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_geometry_measures(
    image_dimension: int,
    label_image: InputPathType,
    intensity_image: str | None = None,
    csv_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> LabelGeometryMeasuresOutputs:
    """
    This tool computes various geometry measures on a label image, optionally using
    an intensity image, and outputs the results to a CSV file.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the input images (e.g., 2 for\
            2D, 3 for 3D).
        label_image: The label image on which geometry measures are computed.
        intensity_image: An optional intensity image for computing\
            intensity-weighted measures. Use "none" or "na" if not provided.
        csv_file: The output file where the geometry measures are written in\
            CSV format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelGeometryMeasuresOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_GEOMETRY_MEASURES_METADATA)
    params = label_geometry_measures_params(image_dimension=image_dimension, label_image=label_image, intensity_image=intensity_image, csv_file=csv_file)
    return label_geometry_measures_execute(params, execution)


__all__ = [
    "LABEL_GEOMETRY_MEASURES_METADATA",
    "LabelGeometryMeasuresOutputs",
    "LabelGeometryMeasuresParameters",
    "label_geometry_measures",
    "label_geometry_measures_params",
]
