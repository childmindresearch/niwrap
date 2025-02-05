# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_AI_METADATA = Metadata(
    id="694c77fb3122e7ae7609dc66837caa7834538472.boutiques",
    name="antsAI",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsAiParameters = typing.TypedDict('AntsAiParameters', {
    "__STYX_TYPE__": typing.Literal["antsAI"],
    "dimensionality": typing.NotRequired[typing.Literal[2, 3] | None],
    "metric": typing.Literal["Mattes[fixedImage,movingImage]", "GC[fixedImage,movingImage]", "MI[fixedImage,movingImage]"],
    "transform": typing.Literal["Rigid[gradientStep]", "Affine[gradientStep]", "Similarity[gradientStep]", "AlignGeometricCenters", "AlignCentersOfMass"],
    "align_principal_axes": typing.NotRequired[typing.Literal[0, 1] | None],
    "align_blobs": typing.NotRequired[typing.Literal["numberOfBlobsToExtract", "[numberOfBlobsToExtract,numberOfBlobsToMatch]"] | None],
    "search_factor": typing.NotRequired[typing.Literal["searchFactor", "[searchFactor,arcFraction]"] | None],
    "translation_search_grid": typing.NotRequired[typing.Literal["[stepSize, AxBxC]"] | None],
    "convergence": typing.NotRequired[typing.Literal["numberOfIterations", "[numberOfIterations,convergenceThreshold,convergenceWindowSize]"] | None],
    "masks": typing.NotRequired[typing.Literal["fixedImageMask", "[fixedImageMask,movingImageMask]"] | None],
    "output": str,
    "random_seed": typing.NotRequired[int | None],
    "verbose": typing.NotRequired[typing.Literal[0, 1] | None],
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
        "antsAI": ants_ai_cargs,
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
        "antsAI": ants_ai_outputs,
    }
    return vt.get(t)


class AntsAiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_ai(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform: OutputPathType
    """The output transform (ITK .mat file)."""


def ants_ai_params(
    metric: typing.Literal["Mattes[fixedImage,movingImage]", "GC[fixedImage,movingImage]", "MI[fixedImage,movingImage]"],
    transform: typing.Literal["Rigid[gradientStep]", "Affine[gradientStep]", "Similarity[gradientStep]", "AlignGeometricCenters", "AlignCentersOfMass"],
    output: str,
    dimensionality: typing.Literal[2, 3] | None = None,
    align_principal_axes: typing.Literal[0, 1] | None = None,
    align_blobs: typing.Literal["numberOfBlobsToExtract", "[numberOfBlobsToExtract,numberOfBlobsToMatch]"] | None = None,
    search_factor: typing.Literal["searchFactor", "[searchFactor,arcFraction]"] | None = None,
    translation_search_grid: typing.Literal["[stepSize, AxBxC]"] | None = None,
    convergence: typing.Literal["numberOfIterations", "[numberOfIterations,convergenceThreshold,convergenceWindowSize]"] | None = None,
    masks: typing.Literal["fixedImageMask", "[fixedImageMask,movingImageMask]"] | None = None,
    random_seed: int | None = None,
    verbose: typing.Literal[0, 1] | None = None,
) -> AntsAiParameters:
    """
    Build parameters.
    
    Args:
        metric: These image metrics are available: Mattes: Mattes mutual\
            information (recommended), GC: global correlation, MI: joint histogram\
            mutual information.
        transform: Several transform options are available. For the rigid,\
            affine, and similarity transforms, the gradientStep characterizes the\
            gradient descent optimization. The other two transform types finds the\
            simple translation transform which aligns the specified image feature.
        output: Specify the output transform (output format an ITK .mat file).
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, we try to infer the\
            dimensionality from the input image.
        align_principal_axes: Boolean indicating alignment by principal axes.\
            Alternatively, one can align using blobs.
        align_blobs: Boolean indicating alignment by a set of blobs.
        search_factor: Incremental search factor (in degrees) which will sample\
            the arc fraction around the principal axis or default axis.
        translation_search_grid: Translation search grid in mm, which will\
            translate the moving image in each dimension in increments of the step\
            size.
        convergence: Number of iterations.
        masks: Image masks to limit voxels considered by the metric.
        random_seed: Use a fixed seed for random number generation.
        verbose: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsAI",
        "metric": metric,
        "transform": transform,
        "output": output,
    }
    if dimensionality is not None:
        params["dimensionality"] = dimensionality
    if align_principal_axes is not None:
        params["align_principal_axes"] = align_principal_axes
    if align_blobs is not None:
        params["align_blobs"] = align_blobs
    if search_factor is not None:
        params["search_factor"] = search_factor
    if translation_search_grid is not None:
        params["translation_search_grid"] = translation_search_grid
    if convergence is not None:
        params["convergence"] = convergence
    if masks is not None:
        params["masks"] = masks
    if random_seed is not None:
        params["random_seed"] = random_seed
    if verbose is not None:
        params["verbose"] = verbose
    return params


def ants_ai_cargs(
    params: AntsAiParameters,
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
    cargs.append("antsAI")
    if params.get("dimensionality") is not None:
        cargs.extend([
            "--dimensionality",
            str(params.get("dimensionality"))
        ])
    cargs.extend([
        "-m",
        params.get("metric")
    ])
    cargs.extend([
        "-t",
        params.get("transform")
    ])
    if params.get("align_principal_axes") is not None:
        cargs.extend([
            "-p",
            str(params.get("align_principal_axes"))
        ])
    if params.get("align_blobs") is not None:
        cargs.extend([
            "-b",
            params.get("align_blobs")
        ])
    if params.get("search_factor") is not None:
        cargs.extend([
            "-s",
            params.get("search_factor")
        ])
    if params.get("translation_search_grid") is not None:
        cargs.extend([
            "-g",
            params.get("translation_search_grid")
        ])
    if params.get("convergence") is not None:
        cargs.extend([
            "-c",
            params.get("convergence")
        ])
    if params.get("masks") is not None:
        cargs.extend([
            "-x",
            params.get("masks")
        ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    if params.get("random_seed") is not None:
        cargs.extend([
            "--random-seed",
            str(params.get("random_seed"))
        ])
    if params.get("verbose") is not None:
        cargs.extend([
            "-v",
            str(params.get("verbose"))
        ])
    return cargs


def ants_ai_outputs(
    params: AntsAiParameters,
    execution: Execution,
) -> AntsAiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsAiOutputs(
        root=execution.output_file("."),
        output_transform=execution.output_file(params.get("output") + ".mat"),
    )
    return ret


def ants_ai_execute(
    params: AntsAiParameters,
    execution: Execution,
) -> AntsAiOutputs:
    """
    Program to calculate the optimal linear transform parameters for aligning two
    images.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsAiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ants_ai_cargs(params, execution)
    ret = ants_ai_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_ai(
    metric: typing.Literal["Mattes[fixedImage,movingImage]", "GC[fixedImage,movingImage]", "MI[fixedImage,movingImage]"],
    transform: typing.Literal["Rigid[gradientStep]", "Affine[gradientStep]", "Similarity[gradientStep]", "AlignGeometricCenters", "AlignCentersOfMass"],
    output: str,
    dimensionality: typing.Literal[2, 3] | None = None,
    align_principal_axes: typing.Literal[0, 1] | None = None,
    align_blobs: typing.Literal["numberOfBlobsToExtract", "[numberOfBlobsToExtract,numberOfBlobsToMatch]"] | None = None,
    search_factor: typing.Literal["searchFactor", "[searchFactor,arcFraction]"] | None = None,
    translation_search_grid: typing.Literal["[stepSize, AxBxC]"] | None = None,
    convergence: typing.Literal["numberOfIterations", "[numberOfIterations,convergenceThreshold,convergenceWindowSize]"] | None = None,
    masks: typing.Literal["fixedImageMask", "[fixedImageMask,movingImageMask]"] | None = None,
    random_seed: int | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AntsAiOutputs:
    """
    Program to calculate the optimal linear transform parameters for aligning two
    images.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        metric: These image metrics are available: Mattes: Mattes mutual\
            information (recommended), GC: global correlation, MI: joint histogram\
            mutual information.
        transform: Several transform options are available. For the rigid,\
            affine, and similarity transforms, the gradientStep characterizes the\
            gradient descent optimization. The other two transform types finds the\
            simple translation transform which aligns the specified image feature.
        output: Specify the output transform (output format an ITK .mat file).
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, we try to infer the\
            dimensionality from the input image.
        align_principal_axes: Boolean indicating alignment by principal axes.\
            Alternatively, one can align using blobs.
        align_blobs: Boolean indicating alignment by a set of blobs.
        search_factor: Incremental search factor (in degrees) which will sample\
            the arc fraction around the principal axis or default axis.
        translation_search_grid: Translation search grid in mm, which will\
            translate the moving image in each dimension in increments of the step\
            size.
        convergence: Number of iterations.
        masks: Image masks to limit voxels considered by the metric.
        random_seed: Use a fixed seed for random number generation.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsAiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_AI_METADATA)
    params = ants_ai_params(dimensionality=dimensionality, metric=metric, transform=transform, align_principal_axes=align_principal_axes, align_blobs=align_blobs, search_factor=search_factor, translation_search_grid=translation_search_grid, convergence=convergence, masks=masks, output=output, random_seed=random_seed, verbose=verbose)
    return ants_ai_execute(params, execution)


__all__ = [
    "ANTS_AI_METADATA",
    "AntsAiOutputs",
    "AntsAiParameters",
    "ants_ai",
    "ants_ai_params",
]
