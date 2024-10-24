# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DESIGN_TTEST2_METADATA = Metadata(
    id="4f98cff1704b6243d344d536faebad9ca961f2af.boutiques",
    name="design_ttest2",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class DesignTtest2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `design_ttest2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def design_ttest2(
    design_files_rootname: str,
    ngroupa: float,
    ngroupb: float,
    include_mean_contrasts: bool = False,
    runner: Runner | None = None,
) -> DesignTtest2Outputs:
    """
    Command for generating group mean contrasts for a two-sample t-test design.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        design_files_rootname: Root name for design files.
        ngroupa: Number of subjects in group A.
        ngroupb: Number of subjects in group B.
        include_mean_contrasts: Include individual group mean contrasts.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DesignTtest2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DESIGN_TTEST2_METADATA)
    cargs = []
    cargs.append("design_ttest2")
    cargs.append(design_files_rootname)
    cargs.append(str(ngroupa))
    cargs.append(str(ngroupb))
    if include_mean_contrasts:
        cargs.append("-m")
    ret = DesignTtest2Outputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DESIGN_TTEST2_METADATA",
    "DesignTtest2Outputs",
    "design_ttest2",
]
