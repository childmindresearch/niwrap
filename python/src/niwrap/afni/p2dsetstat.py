# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

P2DSETSTAT_METADATA = Metadata(
    id="b6b0a2e0f001073b8c2fe20c07c32193d6633cad",
    name="p2dsetstat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class P2dsetstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `p2dsetstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stat_value: OutputPathType
    """The converted statistic value."""


def p2dsetstat(
    dataset: str,
    pvalue: float | int,
    bisided: bool = False,
    twosided: bool = False,
    onesided: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> P2dsetstatOutputs:
    """
    p2dsetstat by AFNI Team.
    
    Convert a p-value to a statistic of choice with reference to a specific
    dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/p2dsetstat.html
    
    Args:
        dataset: Specify a dataset DDD and, if it has multiple sub-bricks, the\
            [i]th subbrick with the statistic of interest MUST be selected\
            explicitly; note the use of quotation marks around the brick selector\
            (because of the square-brackets). 'i' can be either a number or a\
            string label selector.
        pvalue: Input p-value P, which MUST be in the interval [0,1].
        bisided: Two-sided test.
        twosided: Two-sided test.
        onesided: One-sided test.
        quiet: Output only the final statistic value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `P2dsetstatOutputs`).
    """
    runner = runner or get_global_runner()
    if not (0 <= pvalue <= 1): 
        raise ValueError(f"'pvalue' must be between 0 <= x <= 1 but was {pvalue}")
    execution = runner.start_execution(P2DSETSTAT_METADATA)
    cargs = []
    cargs.append("p2dsetstat")
    cargs.append("-inset")
    cargs.extend(["-inset", dataset])
    cargs.append("-pval")
    cargs.extend(["-pval", str(pvalue)])
    if onesided:
        cargs.append("-1sided")
    if quiet:
        cargs.append("-quiet")
    ret = P2dsetstatOutputs(
        root=execution.output_file("."),
        stat_value=execution.output_file(f"stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "P2DSETSTAT_METADATA",
    "P2dsetstatOutputs",
    "p2dsetstat",
]
