# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_BRAIN_EXTRACTION_SH_METADATA = Metadata(
    id="1f8c451b98f93c105aed231bb6898634ea958829.boutiques",
    name="antsBrainExtraction.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsBrainExtractionShParameters = typing.TypedDict('AntsBrainExtractionShParameters', {
    "__STYX_TYPE__": typing.Literal["antsBrainExtraction.sh"],
    "image_dimension": int,
    "anatomical_image": InputPathType,
    "template": InputPathType,
    "probability_mask": InputPathType,
    "tissue_classification": typing.NotRequired[str | None],
    "brain_extraction_registration_mask": typing.NotRequired[InputPathType | None],
    "keep_temporary_files": bool,
    "single_floating_point_precision": bool,
    "initial_moving_transform": typing.NotRequired[InputPathType | None],
    "rotation_search_params": typing.NotRequired[str | None],
    "image_file_suffix": typing.NotRequired[str | None],
    "translation_search_params": typing.NotRequired[str | None],
    "random_seeding": bool,
    "debug_mode": bool,
    "output_prefix": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "antsBrainExtraction.sh": ants_brain_extraction_sh_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "antsBrainExtraction.sh": ants_brain_extraction_sh_outputs,
    }
    return vt.get(t)


class AntsBrainExtractionShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_brain_extraction_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    brain_extracted_image: OutputPathType | None
    """Brain extracted image"""
    brain_mask: OutputPathType | None
    """Brain mask"""
    brain_probability_mask: OutputPathType | None
    """Brain probability mask"""


def ants_brain_extraction_sh_params(
    anatomical_image: InputPathType,
    template: InputPathType,
    probability_mask: InputPathType,
    image_dimension: int = 3,
    tissue_classification: str | None = None,
    brain_extraction_registration_mask: InputPathType | None = None,
    keep_temporary_files: bool = False,
    single_floating_point_precision: bool = False,
    initial_moving_transform: InputPathType | None = None,
    rotation_search_params: str | None = None,
    image_file_suffix: str | None = None,
    translation_search_params: str | None = None,
    random_seeding: bool = False,
    debug_mode: bool = False,
    output_prefix: str | None = "output",
) -> AntsBrainExtractionShParameters:
    """
    Build parameters.
    
    Args:
        anatomical_image: Anatomical image (Structural image, typically T1).
        template: Brain extraction template (Anatomical template).
        probability_mask: Brain extraction probability mask.
        image_dimension: Image dimension (2 or 3).
        tissue_classification: Tissue classification.
        brain_extraction_registration_mask: Brain extraction registration mask.
        keep_temporary_files: Keep temporary files.
        single_floating_point_precision: Use single floating point precision.
        initial_moving_transform: Initial moving transform.
        rotation_search_params: Rotation search parameters.
        image_file_suffix: Image file suffix.
        translation_search_params: Translation search parameters.
        random_seeding: Use random seeding.
        debug_mode: Test / debug mode.
        output_prefix: Output prefix.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsBrainExtraction.sh",
        "image_dimension": image_dimension,
        "anatomical_image": anatomical_image,
        "template": template,
        "probability_mask": probability_mask,
        "keep_temporary_files": keep_temporary_files,
        "single_floating_point_precision": single_floating_point_precision,
        "random_seeding": random_seeding,
        "debug_mode": debug_mode,
    }
    if tissue_classification is not None:
        params["tissue_classification"] = tissue_classification
    if brain_extraction_registration_mask is not None:
        params["brain_extraction_registration_mask"] = brain_extraction_registration_mask
    if initial_moving_transform is not None:
        params["initial_moving_transform"] = initial_moving_transform
    if rotation_search_params is not None:
        params["rotation_search_params"] = rotation_search_params
    if image_file_suffix is not None:
        params["image_file_suffix"] = image_file_suffix
    if translation_search_params is not None:
        params["translation_search_params"] = translation_search_params
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    return params


def ants_brain_extraction_sh_cargs(
    params: AntsBrainExtractionShParameters,
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
    cargs.append("antsBrainExtraction.sh")
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
        execution.input_file(params.get("template"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("probability_mask"))
    ])
    if params.get("tissue_classification") is not None:
        cargs.extend([
            "-c",
            params.get("tissue_classification")
        ])
    if params.get("brain_extraction_registration_mask") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("brain_extraction_registration_mask"))
        ])
    if params.get("keep_temporary_files"):
        cargs.append("-k")
    if params.get("single_floating_point_precision"):
        cargs.append("-q")
    if params.get("initial_moving_transform") is not None:
        cargs.extend([
            "-r",
            execution.input_file(params.get("initial_moving_transform"))
        ])
    if params.get("rotation_search_params") is not None:
        cargs.extend([
            "-R",
            params.get("rotation_search_params")
        ])
    if params.get("image_file_suffix") is not None:
        cargs.extend([
            "-s",
            params.get("image_file_suffix")
        ])
    if params.get("translation_search_params") is not None:
        cargs.extend([
            "-T",
            params.get("translation_search_params")
        ])
    if params.get("random_seeding"):
        cargs.append("-u")
    if params.get("debug_mode"):
        cargs.append("-z")
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-o",
            params.get("output_prefix")
        ])
    return cargs


def ants_brain_extraction_sh_outputs(
    params: AntsBrainExtractionShParameters,
    execution: Execution,
) -> AntsBrainExtractionShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsBrainExtractionShOutputs(
        root=execution.output_file("."),
        brain_extracted_image=execution.output_file(params.get("output_prefix") + "_BrainExtractionBrain.nii.gz") if (params.get("output_prefix") is not None) else None,
        brain_mask=execution.output_file(params.get("output_prefix") + "_BrainExtractionMask.nii.gz") if (params.get("output_prefix") is not None) else None,
        brain_probability_mask=execution.output_file(params.get("output_prefix") + "_BrainExtractionPrior0GenericAffine.mat") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def ants_brain_extraction_sh_execute(
    params: AntsBrainExtractionShParameters,
    execution: Execution,
) -> AntsBrainExtractionShOutputs:
    """
    antsBrainExtraction.sh performs template-based brain extraction.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsBrainExtractionShOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ants_brain_extraction_sh_cargs(params, execution)
    ret = ants_brain_extraction_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_brain_extraction_sh(
    anatomical_image: InputPathType,
    template: InputPathType,
    probability_mask: InputPathType,
    image_dimension: int = 3,
    tissue_classification: str | None = None,
    brain_extraction_registration_mask: InputPathType | None = None,
    keep_temporary_files: bool = False,
    single_floating_point_precision: bool = False,
    initial_moving_transform: InputPathType | None = None,
    rotation_search_params: str | None = None,
    image_file_suffix: str | None = None,
    translation_search_params: str | None = None,
    random_seeding: bool = False,
    debug_mode: bool = False,
    output_prefix: str | None = "output",
    runner: Runner | None = None,
) -> AntsBrainExtractionShOutputs:
    """
    antsBrainExtraction.sh performs template-based brain extraction.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        anatomical_image: Anatomical image (Structural image, typically T1).
        template: Brain extraction template (Anatomical template).
        probability_mask: Brain extraction probability mask.
        image_dimension: Image dimension (2 or 3).
        tissue_classification: Tissue classification.
        brain_extraction_registration_mask: Brain extraction registration mask.
        keep_temporary_files: Keep temporary files.
        single_floating_point_precision: Use single floating point precision.
        initial_moving_transform: Initial moving transform.
        rotation_search_params: Rotation search parameters.
        image_file_suffix: Image file suffix.
        translation_search_params: Translation search parameters.
        random_seeding: Use random seeding.
        debug_mode: Test / debug mode.
        output_prefix: Output prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsBrainExtractionShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_BRAIN_EXTRACTION_SH_METADATA)
    params = ants_brain_extraction_sh_params(image_dimension=image_dimension, anatomical_image=anatomical_image, template=template, probability_mask=probability_mask, tissue_classification=tissue_classification, brain_extraction_registration_mask=brain_extraction_registration_mask, keep_temporary_files=keep_temporary_files, single_floating_point_precision=single_floating_point_precision, initial_moving_transform=initial_moving_transform, rotation_search_params=rotation_search_params, image_file_suffix=image_file_suffix, translation_search_params=translation_search_params, random_seeding=random_seeding, debug_mode=debug_mode, output_prefix=output_prefix)
    return ants_brain_extraction_sh_execute(params, execution)


__all__ = [
    "ANTS_BRAIN_EXTRACTION_SH_METADATA",
    "AntsBrainExtractionShOutputs",
    "AntsBrainExtractionShParameters",
    "ants_brain_extraction_sh",
    "ants_brain_extraction_sh_params",
]
