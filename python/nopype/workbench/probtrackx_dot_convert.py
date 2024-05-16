# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.984775

import typing

from ..styxdefs import *


PROBTRACKX_DOT_CONVERT_METADATA = Metadata(
    id="d634f136f33a3af96d313b9224313d52b4ed351e",
    name="probtrackx-dot-convert",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class ProbtrackxDotConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `probtrackx_dot_convert(...)`.
    """
    cifti_out: OutputPathType
    """output cifti file"""


def probtrackx_dot_convert(
    runner: Runner,
    dot_file: str,
    cifti_out: InputPathType,
    opt_row_surface_roi_metric: InputPathType | None = None,
    opt_col_surface_roi_metric: InputPathType | None = None,
    opt_transpose: bool = False,
    opt_make_symmetric: bool = False,
) -> ProbtrackxDotConvertOutputs:
    """
    CONVERT A .DOT FILE FROM PROBTRACKX TO CIFTI.
    
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
    THALAMUS_RIGHT
    
    Args:
        runner: Command runner
        dot_file: input .dot file
        cifti_out: output cifti file
        opt_row_surface_roi_metric: the output mapping along a row will be
            surface vertices: a metric file with positive values on all vertices
            used
        opt_col_surface_roi_metric: the output mapping along a column will be
            surface vertices: a metric file with positive values on all vertices
            used
        opt_transpose: transpose the input matrix
        opt_make_symmetric: transform half-square input into full matrix output
    Returns:
        NamedTuple of outputs (described in `ProbtrackxDotConvertOutputs`).
    """
    execution = runner.start_execution(PROBTRACKX_DOT_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-probtrackx-dot-convert")
    cargs.append(dot_file)
    cargs.append(execution.input_file(cifti_out))
    if opt_row_surface_roi_metric is not None:
        cargs.extend(["-row-surface", execution.input_file(opt_row_surface_roi_metric)])
    if opt_col_surface_roi_metric is not None:
        cargs.extend(["-col-surface", execution.input_file(opt_col_surface_roi_metric)])
    if opt_transpose:
        cargs.append("-transpose")
    if opt_make_symmetric:
        cargs.append("-make-symmetric")
    ret = ProbtrackxDotConvertOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret
