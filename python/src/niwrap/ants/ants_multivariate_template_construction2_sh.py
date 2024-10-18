# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_MULTIVARIATE_TEMPLATE_CONSTRUCTION2_SH_METADATA = Metadata(
    id="88e30f1de82d7238ed91b6f4994e2eef0cad4d8a.boutiques",
    name="antsMultivariateTemplateConstruction2.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsMultivariateTemplateConstruction2ShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_multivariate_template_construction2_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    template: OutputPathType
    """The output multivariate template."""


def ants_multivariate_template_construction2_sh(
    input_: str,
    runner: Runner | None = None,
) -> AntsMultivariateTemplateConstruction2ShOutputs:
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
        input_: Options for setting up and running the multivariate template\
            construction process.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsMultivariateTemplateConstruction2ShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_MULTIVARIATE_TEMPLATE_CONSTRUCTION2_SH_METADATA)
    cargs = []
    cargs.append("antsMultivariateTemplateConstruction2.sh")
    cargs.append(input_)
    ret = AntsMultivariateTemplateConstruction2ShOutputs(
        root=execution.output_file("."),
        template=execution.output_file("<output-prefix>Template.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_MULTIVARIATE_TEMPLATE_CONSTRUCTION2_SH_METADATA",
    "AntsMultivariateTemplateConstruction2ShOutputs",
    "ants_multivariate_template_construction2_sh",
]
