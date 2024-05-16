# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.746568

import typing

from ..styxdefs import *


CIFTI_AVERAGE_METADATA = Metadata(
    id="4a98b75c208b5c8dbf2f37253c8ec90ae78f127b",
    name="cifti-average",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average(...)`.
    """
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_average(
    runner: Runner,
    cifti_out: InputPathType,
    opt_mem_limit_limit_gb: float | int | None = None,
    opt_cifti_cifti_in: InputPathType | None = None,
) -> CiftiAverageOutputs:
    """
    AVERAGE CIFTI FILES.
    
    Averages cifti files together. Files without -weight specified are given a
    weight of 1. If -exclude-outliers is specified, at each element, the data
    across all files is taken as a set, its unweighted mean and sample standard
    deviation are found, and values outside the specified number of standard
    deviations are excluded from the (potentially weighted) average at that
    element.
    
    Args:
        runner: Command runner
        cifti_out: output cifti file
        opt_mem_limit_limit_gb: restrict memory used for file reading
            efficiency: memory limit in gigabytes
        opt_cifti_cifti_in: specify an input file: the input cifti file
    Returns:
        NamedTuple of outputs (described in `CiftiAverageOutputs`).
    """
    execution = runner.start_execution(CIFTI_AVERAGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-average")
    cargs.append(execution.input_file(cifti_out))
    if opt_mem_limit_limit_gb is not None:
        cargs.extend(["-mem-limit", str(opt_mem_limit_limit_gb)])
    if opt_cifti_cifti_in is not None:
        cargs.extend(["-cifti", execution.input_file(opt_cifti_cifti_in)])
    ret = CiftiAverageOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret
