# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_CORTICAL_THICKNESS_SH_METADATA = Metadata(
    id="927ff3d34dcb64b2fcbc355449b1223268e7ab32.boutiques",
    name="antsCorticalThickness.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsCorticalThicknessShParameters = typing.TypedDict('AntsCorticalThicknessShParameters', {
    "__STYX_TYPE__": typing.Literal["antsCorticalThickness.sh"],
    "image_dimension": typing.Literal[2, 3],
    "anatomical_image": InputPathType,
    "brain_template": InputPathType,
    "brain_extraction_probability_mask": InputPathType,
    "brain_segmentation_priors": str,
    "output_prefix": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "antsCorticalThickness.sh": ants_cortical_thickness_sh_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "antsCorticalThickness.sh": ants_cortical_thickness_sh_outputs,
    }.get(t)


class AntsCorticalThicknessShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_cortical_thickness_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cortical_thickness: OutputPathType
    """The output cortical thickness map."""
    brain_extraction_mask: OutputPathType
    """The brain extraction mask."""
    brain_segmentation: OutputPathType
    """The brain segmentation image."""
    segmentation_posteriors: OutputPathType
    """The segmentation posteriors for different tissue classes."""


def ants_cortical_thickness_sh_params(
    image_dimension: typing.Literal[2, 3],
    anatomical_image: InputPathType,
    brain_template: InputPathType,
    brain_extraction_probability_mask: InputPathType,
    brain_segmentation_priors: str,
    output_prefix: str,
) -> AntsCorticalThicknessShParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: 2 or 3 for 2- or 3-dimensional image.
        anatomical_image: Structural intensity image, typically T1.
        brain_template: Anatomical intensity template. This template is not\
            skull-stripped.
        brain_extraction_probability_mask: Brain probability mask in the\
            segmentation template space. A binary mask is acceptable.
        brain_segmentation_priors: Tissue probability priors corresponding to\
            the template image specified with the -e option. At least four priors\
            must exist, corresponding to CSF, Cortical GM, WM, Subcortical GM.
        output_prefix: Output prefix for the generated filenames.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsCorticalThickness.sh",
        "image_dimension": image_dimension,
        "anatomical_image": anatomical_image,
        "brain_template": brain_template,
        "brain_extraction_probability_mask": brain_extraction_probability_mask,
        "brain_segmentation_priors": brain_segmentation_priors,
        "output_prefix": output_prefix,
    }
    return params


def ants_cortical_thickness_sh_cargs(
    params: AntsCorticalThicknessShParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("antsCorticalThickness.sh")
    cargs.extend([
        "-d",
        str(params.get("image_dimension"))
    ])
    cargs.extend([
        "-a",
        execution.input_file(params.get("anatomical_image"))
    ])
    cargs.extend([
        "-e",
        execution.input_file(params.get("brain_template"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("brain_extraction_probability_mask"))
    ])
    cargs.extend([
        "-p",
        params.get("brain_segmentation_priors")
    ])
    cargs.append("[ADDITIONAL_PARAMETERS]")
    cargs.extend([
        "-o",
        params.get("output_prefix")
    ])
    return cargs


def ants_cortical_thickness_sh_outputs(
    params: AntsCorticalThicknessShParameters,
    execution: Execution,
) -> AntsCorticalThicknessShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsCorticalThicknessShOutputs(
        root=execution.output_file("."),
        cortical_thickness=execution.output_file(params.get("output_prefix") + "CorticalThickness.nii.gz"),
        brain_extraction_mask=execution.output_file(params.get("output_prefix") + "BrainExtractionMask.nii.gz"),
        brain_segmentation=execution.output_file(params.get("output_prefix") + "BrainSegmentation.nii.gz"),
        segmentation_posteriors=execution.output_file(params.get("output_prefix") + "BrainSegmentationPosteriors*.nii.gz"),
    )
    return ret


def ants_cortical_thickness_sh_execute(
    params: AntsCorticalThicknessShParameters,
    execution: Execution,
) -> AntsCorticalThicknessShOutputs:
    """
    This script performs T1 anatomical brain processing including brain extraction,
    brain n-tissue segmentation, cortical thickness estimation, and optional
    registration to a template.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsCorticalThicknessShOutputs`).
    """
    cargs = ants_cortical_thickness_sh_cargs(params, execution)
    ret = ants_cortical_thickness_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_cortical_thickness_sh(
    image_dimension: typing.Literal[2, 3],
    anatomical_image: InputPathType,
    brain_template: InputPathType,
    brain_extraction_probability_mask: InputPathType,
    brain_segmentation_priors: str,
    output_prefix: str,
    runner: Runner | None = None,
) -> AntsCorticalThicknessShOutputs:
    """
    This script performs T1 anatomical brain processing including brain extraction,
    brain n-tissue segmentation, cortical thickness estimation, and optional
    registration to a template.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: 2 or 3 for 2- or 3-dimensional image.
        anatomical_image: Structural intensity image, typically T1.
        brain_template: Anatomical intensity template. This template is not\
            skull-stripped.
        brain_extraction_probability_mask: Brain probability mask in the\
            segmentation template space. A binary mask is acceptable.
        brain_segmentation_priors: Tissue probability priors corresponding to\
            the template image specified with the -e option. At least four priors\
            must exist, corresponding to CSF, Cortical GM, WM, Subcortical GM.
        output_prefix: Output prefix for the generated filenames.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsCorticalThicknessShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_CORTICAL_THICKNESS_SH_METADATA)
    params = ants_cortical_thickness_sh_params(image_dimension=image_dimension, anatomical_image=anatomical_image, brain_template=brain_template, brain_extraction_probability_mask=brain_extraction_probability_mask, brain_segmentation_priors=brain_segmentation_priors, output_prefix=output_prefix)
    return ants_cortical_thickness_sh_execute(params, execution)


__all__ = [
    "ANTS_CORTICAL_THICKNESS_SH_METADATA",
    "AntsCorticalThicknessShOutputs",
    "AntsCorticalThicknessShParameters",
    "ants_cortical_thickness_sh",
    "ants_cortical_thickness_sh_params",
]
