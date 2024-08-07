# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FFTEST_METADATA = Metadata(
    id="ce6ba9bfe8fc105e767d57335a343e80526236dd",
    name="fftest",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FftestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fftest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fftest(
    length: float | int,
    num_tests: float | int,
    vector_size: float | int,
    quiet_mode: bool = False,
    runner: Runner | None = None,
) -> FftestOutputs:
    """
    fftest by AFNI Team.
    
    A command line tool for testing purposes.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/fftest.html
    
    Args:
        length: Length of the test.
        num_tests: Number of tests to run.
        vector_size: Vector size for the test.
        quiet_mode: Quiet mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FftestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FFTEST_METADATA)
    cargs = []
    cargs.append("fftest")
    cargs.append("[-q]")
    cargs.append(str(length))
    cargs.append(str(num_tests))
    cargs.append(str(vector_size))
    ret = FftestOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FFTEST_METADATA",
    "FftestOutputs",
    "fftest",
]
