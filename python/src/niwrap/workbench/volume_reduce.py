# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_REDUCE_METADATA = Metadata(
    id="ec96e3deef3a049213ca2b903cb61ddb1545a3b6",
    name="volume-reduce",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeReduceExcludeOutliers:
    """
    exclude non-numeric values and outliers by standard deviation
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


class VolumeReduceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_reduce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_reduce(
    volume_in: InputPathType,
    operation: str,
    volume_out: InputPathType,
    exclude_outliers: VolumeReduceExcludeOutliers | None = None,
    opt_only_numeric: bool = False,
    runner: Runner = None,
) -> VolumeReduceOutputs:
    """
    volume-reduce by Washington University School of Medicin.
    
    Perform reduction operation across subvolumes.
    
    For each voxel, takes the data across subvolumes as a vector, and performs
    the specified reduction on it, putting the result into the single output
    volume at that voxel. The reduction operators are as follows:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    .
    
    Args:
        volume_in: the volume file to reduce.
        operation: the reduction operator to use.
        volume_out: the output volume.
        exclude_outliers: exclude non-numeric values and outliers by standard\
            deviation.
        opt_only_numeric: exclude non-numeric values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeReduceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_REDUCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-reduce")
    cargs.append(execution.input_file(volume_in))
    cargs.append(operation)
    cargs.append(execution.input_file(volume_out))
    if exclude_outliers is not None:
        cargs.extend(["-exclude-outliers", *exclude_outliers.run(execution)])
    if opt_only_numeric:
        cargs.append("-only-numeric")
    ret = VolumeReduceOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_REDUCE_METADATA",
    "VolumeReduceExcludeOutliers",
    "VolumeReduceOutputs",
    "volume_reduce",
]