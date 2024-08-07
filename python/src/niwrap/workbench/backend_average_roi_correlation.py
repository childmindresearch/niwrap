# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BACKEND_AVERAGE_ROI_CORRELATION_METADATA = Metadata(
    id="2baddc4c3d355a41fdd825bd07430cef65c542e0",
    name="backend-average-roi-correlation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class BackendAverageRoiCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `backend_average_roi_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def backend_average_roi_correlation(
    index_list: str,
    out_file: str,
    runner: Runner | None = None,
) -> BackendAverageRoiCorrelationOutputs:
    """
    backend-average-roi-correlation by Washington University School of Medicin.
    
    Connectome db backend command for cifti average roi correlation.
    
    This command is probably not the one you are looking for, try
    -cifti-average-roi-correlation. It takes the list of cifti files to average
    from standard input, and writes its output as little endian, 32-bit integer
    of row size followed by the row as 32-bit floats.
    
    Args:
        index_list: comma separated list of cifti indexes to average and then\
            correlate.
        out_file: file to write the average row to.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BackendAverageRoiCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BACKEND_AVERAGE_ROI_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-backend-average-roi-correlation")
    cargs.append(index_list)
    cargs.append(out_file)
    ret = BackendAverageRoiCorrelationOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BACKEND_AVERAGE_ROI_CORRELATION_METADATA",
    "BackendAverageRoiCorrelationOutputs",
    "backend_average_roi_correlation",
]
