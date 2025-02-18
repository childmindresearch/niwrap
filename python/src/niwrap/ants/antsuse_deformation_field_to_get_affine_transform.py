# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTSUSE_DEFORMATION_FIELD_TO_GET_AFFINE_TRANSFORM_METADATA = Metadata(
    id="a114d5c9bfbab1242b558e6ff3e44480841f6e38.boutiques",
    name="ANTSUseDeformationFieldToGetAffineTransform",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsuseDeformationFieldToGetAffineTransformParameters = typing.TypedDict('AntsuseDeformationFieldToGetAffineTransformParameters', {
    "__STYX_TYPE__": typing.Literal["ANTSUseDeformationFieldToGetAffineTransform"],
    "deformation_field": InputPathType,
    "load_ratio": float,
    "transform_type": typing.Literal["rigid", "affine"],
    "output_affine": str,
    "mask": typing.NotRequired[InputPathType | None],
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
        "ANTSUseDeformationFieldToGetAffineTransform": antsuse_deformation_field_to_get_affine_transform_cargs,
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
        "ANTSUseDeformationFieldToGetAffineTransform": antsuse_deformation_field_to_get_affine_transform_outputs,
    }.get(t)


class AntsuseDeformationFieldToGetAffineTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `antsuse_deformation_field_to_get_affine_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_affine_txt: OutputPathType
    """The output is the affine transformation matrix file."""


def antsuse_deformation_field_to_get_affine_transform_params(
    deformation_field: InputPathType,
    load_ratio: float,
    transform_type: typing.Literal["rigid", "affine"],
    output_affine: str,
    mask: InputPathType | None = None,
) -> AntsuseDeformationFieldToGetAffineTransformParameters:
    """
    Build parameters.
    
    Args:
        deformation_field: The input deformation field in NIfTI format (e.g.,\
            zzzWarp.nii.gz).
        load_ratio: Ratio of points to be loaded from deformation field to save\
            memory (ex: 0.01).
        transform_type: Type of transform to be extracted. Can be 'rigid' or\
            'affine'.
        output_affine: The output file where the affine transform will be saved\
            (e.g., OutAffine.txt).
        mask: Optional mask file defining the region from which points will be\
            selected.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ANTSUseDeformationFieldToGetAffineTransform",
        "deformation_field": deformation_field,
        "load_ratio": load_ratio,
        "transform_type": transform_type,
        "output_affine": output_affine,
    }
    if mask is not None:
        params["mask"] = mask
    return params


def antsuse_deformation_field_to_get_affine_transform_cargs(
    params: AntsuseDeformationFieldToGetAffineTransformParameters,
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
    cargs.append("ANTSUseDeformationFieldToGetAffineTransform")
    cargs.append(execution.input_file(params.get("deformation_field")))
    cargs.append(str(params.get("load_ratio")))
    cargs.append(params.get("transform_type"))
    cargs.append(params.get("output_affine"))
    if params.get("mask") is not None:
        cargs.append(execution.input_file(params.get("mask")))
    return cargs


def antsuse_deformation_field_to_get_affine_transform_outputs(
    params: AntsuseDeformationFieldToGetAffineTransformParameters,
    execution: Execution,
) -> AntsuseDeformationFieldToGetAffineTransformOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsuseDeformationFieldToGetAffineTransformOutputs(
        root=execution.output_file("."),
        out_affine_txt=execution.output_file(params.get("output_affine")),
    )
    return ret


def antsuse_deformation_field_to_get_affine_transform_execute(
    params: AntsuseDeformationFieldToGetAffineTransformParameters,
    execution: Execution,
) -> AntsuseDeformationFieldToGetAffineTransformOutputs:
    """
    Extracts an affine transform from a deformation field. The input deformation
    field is expected to be in the same physical space as the images you want to
    transform.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsuseDeformationFieldToGetAffineTransformOutputs`).
    """
    params = execution.params(params)
    cargs = antsuse_deformation_field_to_get_affine_transform_cargs(params, execution)
    ret = antsuse_deformation_field_to_get_affine_transform_outputs(params, execution)
    execution.run(cargs)
    return ret


def antsuse_deformation_field_to_get_affine_transform(
    deformation_field: InputPathType,
    load_ratio: float,
    transform_type: typing.Literal["rigid", "affine"],
    output_affine: str,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> AntsuseDeformationFieldToGetAffineTransformOutputs:
    """
    Extracts an affine transform from a deformation field. The input deformation
    field is expected to be in the same physical space as the images you want to
    transform.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        deformation_field: The input deformation field in NIfTI format (e.g.,\
            zzzWarp.nii.gz).
        load_ratio: Ratio of points to be loaded from deformation field to save\
            memory (ex: 0.01).
        transform_type: Type of transform to be extracted. Can be 'rigid' or\
            'affine'.
        output_affine: The output file where the affine transform will be saved\
            (e.g., OutAffine.txt).
        mask: Optional mask file defining the region from which points will be\
            selected.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsuseDeformationFieldToGetAffineTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTSUSE_DEFORMATION_FIELD_TO_GET_AFFINE_TRANSFORM_METADATA)
    params = antsuse_deformation_field_to_get_affine_transform_params(deformation_field=deformation_field, load_ratio=load_ratio, transform_type=transform_type, output_affine=output_affine, mask=mask)
    return antsuse_deformation_field_to_get_affine_transform_execute(params, execution)


__all__ = [
    "ANTSUSE_DEFORMATION_FIELD_TO_GET_AFFINE_TRANSFORM_METADATA",
    "AntsuseDeformationFieldToGetAffineTransformOutputs",
    "AntsuseDeformationFieldToGetAffineTransformParameters",
    "antsuse_deformation_field_to_get_affine_transform",
    "antsuse_deformation_field_to_get_affine_transform_params",
]
