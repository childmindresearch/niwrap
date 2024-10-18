# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL_GEOMETRY_MEASURES_METADATA = Metadata(
    id="5440303fc5aad0a732d9de45cce4a4df0e716aa2.boutiques",
    name="LabelGeometryMeasures",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class LabelGeometryMeasuresOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_geometry_measures(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_csv: OutputPathType | None
    """The CSV file containing the geometry measures."""


def label_geometry_measures(
    image_dimension: int,
    label_image: InputPathType,
    intensity_image: str | None = None,
    csv_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> LabelGeometryMeasuresOutputs:
    """
    Advanced Normalization Tools (ANTs) is a C++ library available through the
    command line that computes high-dimensional mappings to capture the statistics
    of brain structure and function. It allows one to organize, visualize and
    statistically explore large biomedical image sets. Additionally, it integrates
    imaging modalities in space + time and works across species or organ systems
    with minimal customization.
    
    The ANTs library is considered a state-of-the-art medical image registration
    and segmentation toolkit which depends on the Insight ToolKit, a widely used
    medical image processing library to which ANTs developers contribute.
    ANTs-related tools have also won several international, unbiased
    competitions such as MICCAI, BRATS, and STACOM.
    
    Author: ANTs developers
    
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
    cargs = []
    cargs.append("LabelGeometryMeasures")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(label_image))
    if intensity_image is not None:
        cargs.append(intensity_image)
    if csv_file is not None:
        cargs.append(execution.input_file(csv_file))
    ret = LabelGeometryMeasuresOutputs(
        root=execution.output_file("."),
        output_csv=execution.output_file(pathlib.Path(csv_file).name) if (csv_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_GEOMETRY_MEASURES_METADATA",
    "LabelGeometryMeasuresOutputs",
    "label_geometry_measures",
]
