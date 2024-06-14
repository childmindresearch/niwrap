# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

LABEL_DILATE_METADATA = Metadata(
    id="553c9cdc59042dcf72c087b7549d5551831e7256",
    name="label-dilate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class LabelDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""


def label_dilate(
    label: InputPathType,
    surface: InputPathType,
    dilate_dist: float | int,
    label_out: InputPathType,
    opt_bad_vertex_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner = None,
) -> LabelDilateOutputs:
    """
    label-dilate by Washington University School of Medicin.
    
    Dilate a label file.
    
    Fills in label information for all vertices designated as bad, up to the
    specified distance away from other labels. If -bad-vertex-roi is specified,
    all vertices, including those with the unlabeled key, are good, except for
    vertices with a positive value in the ROI. If it is not specified, only
    vertices with the unlabeled key are bad.
    
    Args:
        label: the input label.
        surface: the surface to dilate on.
        dilate_dist: distance in mm to dilate the labels.
        label_out: the output label file.
        opt_bad_vertex_roi_roi_metric: specify an roi of vertices to overwrite,\
            rather than vertices with the unlabeled key: metric file, positive\
            values denote vertices to have their values replaced.
        opt_column_column: select a single column to dilate: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_DILATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-dilate")
    cargs.append(execution.input_file(label))
    cargs.append(execution.input_file(surface))
    cargs.append(str(dilate_dist))
    cargs.append(execution.input_file(label_out))
    if opt_bad_vertex_roi_roi_metric is not None:
        cargs.extend(["-bad-vertex-roi", execution.input_file(opt_bad_vertex_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = LabelDilateOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(f"{pathlib.Path(label_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_DILATE_METADATA",
    "LabelDilateOutputs",
    "label_dilate",
]