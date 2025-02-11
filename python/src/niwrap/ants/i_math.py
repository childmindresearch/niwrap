# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

I_MATH_METADATA = Metadata(
    id="82da58a8a784459b76c3083f4eca6f26d139e8c9.boutiques",
    name="iMath",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
IMathParameters = typing.TypedDict('IMathParameters', {
    "__STYX_TYPE__": typing.Literal["iMath"],
    "image_dimension": typing.Literal[2, 3, 4],
    "output_image": str,
    "operations": str,
    "image1": InputPathType,
    "image2": typing.NotRequired[InputPathType | None],
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
        "iMath": i_math_cargs,
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
        "iMath": i_math_outputs,
    }.get(t)


class IMathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `i_math(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    resulting_image: OutputPathType
    """The output image resulting from the operation."""


def i_math_params(
    image_dimension: typing.Literal[2, 3, 4],
    output_image: str,
    operations: str,
    image1: InputPathType,
    image2: InputPathType | None = None,
) -> IMathParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Dimensionality of the image, either 2, 3, or 4.
        output_image: Path for the output image file.
        operations: Operations to be performed along with parameters, e.g.,\
            GetLargestComponent, MC for Closing, etc.
        image1: First input image file.
        image2: Second input image file, if required by operation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "iMath",
        "image_dimension": image_dimension,
        "output_image": output_image,
        "operations": operations,
        "image1": image1,
    }
    if image2 is not None:
        params["image2"] = image2
    return params


def i_math_cargs(
    params: IMathParameters,
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
    cargs.append("iMath")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(params.get("output_image"))
    cargs.append(params.get("operations"))
    cargs.append(execution.input_file(params.get("image1")))
    if params.get("image2") is not None:
        cargs.append(execution.input_file(params.get("image2")))
    return cargs


def i_math_outputs(
    params: IMathParameters,
    execution: Execution,
) -> IMathOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IMathOutputs(
        root=execution.output_file("."),
        resulting_image=execution.output_file(params.get("output_image")),
    )
    return ret


def i_math_execute(
    params: IMathParameters,
    execution: Execution,
) -> IMathOutputs:
    """
    iMath is a tool for performing various image mathematical operations on medical
    images, specifically supporting operations on 2D, 3D, and 4D data.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IMathOutputs`).
    """
    cargs = i_math_cargs(params, execution)
    ret = i_math_outputs(params, execution)
    execution.run(cargs)
    return ret


def i_math(
    image_dimension: typing.Literal[2, 3, 4],
    output_image: str,
    operations: str,
    image1: InputPathType,
    image2: InputPathType | None = None,
    runner: Runner | None = None,
) -> IMathOutputs:
    """
    iMath is a tool for performing various image mathematical operations on medical
    images, specifically supporting operations on 2D, 3D, and 4D data.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Dimensionality of the image, either 2, 3, or 4.
        output_image: Path for the output image file.
        operations: Operations to be performed along with parameters, e.g.,\
            GetLargestComponent, MC for Closing, etc.
        image1: First input image file.
        image2: Second input image file, if required by operation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IMathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(I_MATH_METADATA)
    params = i_math_params(image_dimension=image_dimension, output_image=output_image, operations=operations, image1=image1, image2=image2)
    return i_math_execute(params, execution)


__all__ = [
    "IMathOutputs",
    "IMathParameters",
    "I_MATH_METADATA",
    "i_math",
    "i_math_params",
]
