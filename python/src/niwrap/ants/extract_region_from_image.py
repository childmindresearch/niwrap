# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EXTRACT_REGION_FROM_IMAGE_METADATA = Metadata(
    id="ae946f4d1bb246c4c0e1a26e1d18d3d6f5ce930d.boutiques",
    name="ExtractRegionFromImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
ExtractRegionFromImageRegionMinMaxIndexParameters = typing.TypedDict('ExtractRegionFromImageRegionMinMaxIndexParameters', {
    "__STYX_TYPE__": typing.Literal["region_min_max_index"],
    "min_index": str,
    "max_index": str,
})
ExtractRegionFromImageRegionLabelParameters = typing.TypedDict('ExtractRegionFromImageRegionLabelParameters', {
    "__STYX_TYPE__": typing.Literal["region_label"],
    "label": str,
})
ExtractRegionFromImageRegionDomainImageParameters = typing.TypedDict('ExtractRegionFromImageRegionDomainImageParameters', {
    "__STYX_TYPE__": typing.Literal["region_domain_image"],
    "domain_image": InputPathType,
})
ExtractRegionFromImageRegionLabelWithImageParameters = typing.TypedDict('ExtractRegionFromImageRegionLabelWithImageParameters', {
    "__STYX_TYPE__": typing.Literal["region_label_with_image"],
    "label": str,
    "label_image": InputPathType,
})
ExtractRegionFromImageParameters = typing.TypedDict('ExtractRegionFromImageParameters', {
    "__STYX_TYPE__": typing.Literal["ExtractRegionFromImage"],
    "image_dimension": int,
    "input_image": InputPathType,
    "output_image": str,
    "region_specification": typing.Union[ExtractRegionFromImageRegionMinMaxIndexParameters, ExtractRegionFromImageRegionLabelParameters, ExtractRegionFromImageRegionDomainImageParameters, ExtractRegionFromImageRegionLabelWithImageParameters],
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
        "ExtractRegionFromImage": extract_region_from_image_cargs,
        "region_min_max_index": extract_region_from_image_region_min_max_index_cargs,
        "region_label": extract_region_from_image_region_label_cargs,
        "region_domain_image": extract_region_from_image_region_domain_image_cargs,
        "region_label_with_image": extract_region_from_image_region_label_with_image_cargs,
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
        "ExtractRegionFromImage": extract_region_from_image_outputs,
    }
    return vt.get(t)


def extract_region_from_image_region_min_max_index_params(
    min_index: str,
    max_index: str,
) -> ExtractRegionFromImageRegionMinMaxIndexParameters:
    """
    Build parameters.
    
    Args:
        min_index: Minimum index to define the starting point of the region.
        max_index: Maximum index to define the endpoint of the region.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "region_min_max_index",
        "min_index": min_index,
        "max_index": max_index,
    }
    return params


def extract_region_from_image_region_min_max_index_cargs(
    params: ExtractRegionFromImageRegionMinMaxIndexParameters,
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
    cargs.append(params.get("min_index"))
    cargs.append(params.get("max_index"))
    return cargs


def extract_region_from_image_region_label_params(
    label: str,
) -> ExtractRegionFromImageRegionLabelParameters:
    """
    Build parameters.
    
    Args:
        label: Label value to extract the region corresponding to the specified\
            label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "region_label",
        "label": label,
    }
    return params


def extract_region_from_image_region_label_cargs(
    params: ExtractRegionFromImageRegionLabelParameters,
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
    cargs.append(params.get("label"))
    return cargs


def extract_region_from_image_region_domain_image_params(
    domain_image: InputPathType,
) -> ExtractRegionFromImageRegionDomainImageParameters:
    """
    Build parameters.
    
    Args:
        domain_image: Image defining the domain from which to extract the\
            region.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "region_domain_image",
        "domain_image": domain_image,
    }
    return params


def extract_region_from_image_region_domain_image_cargs(
    params: ExtractRegionFromImageRegionDomainImageParameters,
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
    cargs.append(execution.input_file(params.get("domain_image")))
    return cargs


def extract_region_from_image_region_label_with_image_params(
    label: str,
    label_image: InputPathType,
) -> ExtractRegionFromImageRegionLabelWithImageParameters:
    """
    Build parameters.
    
    Args:
        label: Label value used for the region extraction.
        label_image: Image containing label information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "region_label_with_image",
        "label": label,
        "label_image": label_image,
    }
    return params


def extract_region_from_image_region_label_with_image_cargs(
    params: ExtractRegionFromImageRegionLabelWithImageParameters,
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
    cargs.append(params.get("label"))
    cargs.append(execution.input_file(params.get("label_image")))
    cargs.append("1")
    return cargs


class ExtractRegionFromImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `extract_region_from_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """File containing the extracted region."""


def extract_region_from_image_params(
    image_dimension: int,
    input_image: InputPathType,
    output_image: str,
    region_specification: typing.Union[ExtractRegionFromImageRegionMinMaxIndexParameters, ExtractRegionFromImageRegionLabelParameters, ExtractRegionFromImageRegionDomainImageParameters, ExtractRegionFromImageRegionLabelWithImageParameters],
) -> ExtractRegionFromImageParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimensionality of the image.
        input_image: Path to the input image from which the region will be\
            extracted.
        output_image: Path to the output image where the extracted region will\
            be saved.
        region_specification: Specify the region to extract using indices,\
            label, domain image, or label with label image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ExtractRegionFromImage",
        "image_dimension": image_dimension,
        "input_image": input_image,
        "output_image": output_image,
        "region_specification": region_specification,
    }
    return params


def extract_region_from_image_cargs(
    params: ExtractRegionFromImageParameters,
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
    cargs.append("ExtractRegionFromImage")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    cargs.extend(dyn_cargs(params.get("region_specification")["__STYXTYPE__"])(params.get("region_specification"), execution))
    return cargs


def extract_region_from_image_outputs(
    params: ExtractRegionFromImageParameters,
    execution: Execution,
) -> ExtractRegionFromImageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ExtractRegionFromImageOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")),
    )
    return ret


def extract_region_from_image_execute(
    params: ExtractRegionFromImageParameters,
    execution: Execution,
) -> ExtractRegionFromImageOutputs:
    """
    ExtractRegionFromImage can be used to extract a specific region from a given
    image. The region can be specified via indices, label, or another domain image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ExtractRegionFromImageOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = extract_region_from_image_cargs(params, execution)
    ret = extract_region_from_image_outputs(params, execution)
    execution.run(cargs)
    return ret


def extract_region_from_image(
    image_dimension: int,
    input_image: InputPathType,
    output_image: str,
    region_specification: typing.Union[ExtractRegionFromImageRegionMinMaxIndexParameters, ExtractRegionFromImageRegionLabelParameters, ExtractRegionFromImageRegionDomainImageParameters, ExtractRegionFromImageRegionLabelWithImageParameters],
    runner: Runner | None = None,
) -> ExtractRegionFromImageOutputs:
    """
    ExtractRegionFromImage can be used to extract a specific region from a given
    image. The region can be specified via indices, label, or another domain image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the image.
        input_image: Path to the input image from which the region will be\
            extracted.
        output_image: Path to the output image where the extracted region will\
            be saved.
        region_specification: Specify the region to extract using indices,\
            label, domain image, or label with label image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ExtractRegionFromImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EXTRACT_REGION_FROM_IMAGE_METADATA)
    params = extract_region_from_image_params(image_dimension=image_dimension, input_image=input_image, output_image=output_image, region_specification=region_specification)
    return extract_region_from_image_execute(params, execution)


__all__ = [
    "EXTRACT_REGION_FROM_IMAGE_METADATA",
    "ExtractRegionFromImageOutputs",
    "ExtractRegionFromImageParameters",
    "ExtractRegionFromImageRegionDomainImageParameters",
    "ExtractRegionFromImageRegionLabelParameters",
    "ExtractRegionFromImageRegionLabelWithImageParameters",
    "ExtractRegionFromImageRegionMinMaxIndexParameters",
    "extract_region_from_image",
    "extract_region_from_image_params",
    "extract_region_from_image_region_domain_image_params",
    "extract_region_from_image_region_label_params",
    "extract_region_from_image_region_label_with_image_params",
    "extract_region_from_image_region_min_max_index_params",
]
