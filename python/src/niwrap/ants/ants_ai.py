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


class AntsAiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_ai(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform: OutputPathType
    """The output transform (ITK .mat file)."""


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
    if random_seed is not None and not (0 <= random_seed): 
        raise ValueError(f"'random_seed' must be greater than 0 <= x but was {random_seed}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_AI_METADATA)
    cargs = []
    cargs.append("antsAI")
    if dimensionality is not None:
        cargs.extend([
            "--dimensionality",
            str(dimensionality)
        ])
    cargs.extend([
        "-m",
        metric
    ])
    cargs.extend([
        "-t",
        transform
    ])
    if align_principal_axes is not None:
        cargs.extend([
            "-p",
            str(align_principal_axes)
        ])
    if align_blobs is not None:
        cargs.extend([
            "-b",
            align_blobs
        ])
    if search_factor is not None:
        cargs.extend([
            "-s",
            search_factor
        ])
    if translation_search_grid is not None:
        cargs.extend([
            "-g",
            translation_search_grid
        ])
    if convergence is not None:
        cargs.extend([
            "-c",
            convergence
        ])
    if masks is not None:
        cargs.extend([
            "-x",
            masks
        ])
    cargs.extend([
        "-o",
        output
    ])
    if random_seed is not None:
        cargs.extend([
            "--random-seed",
            str(random_seed)
        ])
    if verbose is not None:
        cargs.extend([
            "-v",
            str(verbose)
        ])
    ret = AntsAiOutputs(
        root=execution.output_file("."),
        output_transform=execution.output_file(output + ".mat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_AI_METADATA",
    "AntsAiOutputs",
    "ants_ai",
]
