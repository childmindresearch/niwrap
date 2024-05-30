# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


N4_BIAS_FIELD_CORRECTION_METADATA = Metadata(
    id="a973cb16a85a643a60a114d99f426720945ad6c8",
    name="N4BiasFieldCorrection",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class N4BiasFieldCorrectionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `n4_bias_field_correction(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_image: OutputPathType
    """The bias corrected version of the input image."""
    bias_field: OutputPathType
    """Estimated bias field image."""


def n4_bias_field_correction(
    input_image: InputPathType,
    corrected_image_path: str,
    bias_field_path: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    shrink_factor: typing.Literal[1, 2, 3, 4] | None = None,
    mask_image: InputPathType | None = None,
    rescale_intensities: typing.Literal[0, 1] | None = None,
    weight_image: InputPathType | None = None,
    convergence: str | None = None,
    bspline_fitting: str | None = None,
    histogram_sharpening: str | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner = None,
) -> N4BiasFieldCorrectionOutputs:
    """
    N4BiasFieldCorrection by ANTs authors.
    
    N4 is a variant of the popular N3 (nonparameteric nonuniform normalization)
    retrospective bias correction algorithm. Based on the assumption that the
    corruption of the low frequency bias field can be modeled as a convolution
    of the intensity histogram by a Gaussian, the basic algorithmic protocol is
    to iterate between deconvolving the intensity histogram by a Gaussian,
    remapping the intensities, and then spatially smoothing this result by a
    B-spline modeling of the bias field itself. The modifications from and
    improvements obtained over the original N3 algorithm are described in the
    following paper: N. Tustison et al., N4ITK: Improved N3 Bias Correction,
    IEEE Transactions on Medical Imaging, 29(6):1310-1320, June 2010.
    
    More information: https://github.com/ANTsX/ANTs/wiki/N4BiasFieldCorrection
    
    Args:
        input_image: -i, --input-image inputImageFilename. A scalar image is
            expected as input for bias correction. Since N4 log transforms the
            intensities, negative values or values close to zero should be processed
            prior to correction.
        corrected_image_path: The bias corrected version of the input image.
        bias_field_path: Estimated bias field image.
        image_dimensionality: -d, --image-dimensionality 2/3/4. This option
            forces the image to be treated as a specified-dimensional image. If not
            specified, N4 tries to infer the dimensionality from the input image.
        shrink_factor: -s, --shrink-factor 1/2/3/(4)/... Running N4 on large
            images can be time consuming. To lessen computation time, the input
            image can be resampled. The shrink factor, specified as a single
            integer, describes this resampling. Shrink factors <= 4 are commonly
            used. Note that the shrink factor is only applied to the first two or
            three dimensions which we assume are spatial.
        mask_image: -x, --mask-image maskImageFilename. If a mask image is
            specified, the final bias correction is only performed in the mask
            region. If a weight image is not specified, only intensity values inside
            the masked region are used during the execution of the algorithm. If a
            weight image is specified, only the non-zero weights are used in the
            execution of the algorithm although the mask region defines where bias
            correction is performed in the final output. Otherwise bias correction
            occurs over the entire image domain. See also the option description for
            the weight image. If a mask image is *not* specified then the entire
            image region will be used as the mask region. Note that this is
            different than the N3 implementation which uses the results of Otsu
            thresholding to define a mask. However, this leads to unknown anatomical
            regions being included and excluded during the bias correction.
        rescale_intensities: -r, --rescale-intensities 0/(1). At each iteration,
            a new intensity mapping is calculated and applied but there is nothing
            which constrains the new intensity range to be within certain values.
            The result is that the range can "drift" from the original at each
            iteration. This option rescales to the [min,max] range of the original
            image intensities within the user-specified mask. A mask is required to
            perform rescaling.
        weight_image: -w, --weight-image weightImageFilename. The weight image
            allows the user to perform a relative weighting of specific voxels
            during the B-spline fitting. For example, some studies have shown that
            N3 performed on white matter segmentations improves performance. If one
            has a spatial probability map of the white matter, one can use this map
            to weight the b-spline fitting towards those voxels which are more
            probabilistically classified as white matter. See also the option
            description for the mask image.
        convergence: -c, --convergence
            [<numberOfIterations=50x50x50x50>,<convergenceThreshold=0.0>].
            Convergence is determined by calculating the coefficient of variation
            between subsequent iterations. When this value is less than the
            specified threshold from the previous iteration or the maximum number of
            iterations is exceeded the program terminates. Multiple resolutions can
            be specified by using 'x' between the number of iterations at each
            resolution, e.g. 100x50x50.
        bspline_fitting: -b, --bspline-fitting [splineDistance,<splineOrder=3>].
            These options describe the b-spline fitting parameters. The initial
            b-spline mesh at the coarsest resolution is specified either as the
            number of elements in each dimension, e.g. 2x2x3 for 3-D images, or it
            can be specified as a single scalar parameter which describes the
            isotropic sizing of the mesh elements. The latter option is typically
            preferred. For each subsequent level, the spline distance decreases in
            half, or equivalently, the number of mesh elements doubles Cubic splines
            (order = 3) are typically used. The default setting is to employ a
            single mesh element over the entire domain, i.e., -b [1x1x1,3].
        histogram_sharpening: -t, --histogram-sharpening
            [<FWHM=0.15>,<wienerNoise=0.01>,<numberOfHistogramBins=200>]. These
            options describe the histogram sharpening parameters, i.e. the
            deconvolution step parameters described in the original N3 algorithm.
            The default values have been shown to work fairly well.
        verbose: Verbose output.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `N4BiasFieldCorrectionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(N4_BIAS_FIELD_CORRECTION_METADATA)
    cargs = []
    cargs.append("N4BiasFieldCorrection")
    if image_dimensionality is not None:
        cargs.extend(["--image-dimensionality", str(image_dimensionality)])
    if shrink_factor is not None:
        cargs.extend(["--shrink-factor", str(shrink_factor)])
    if mask_image is not None:
        cargs.extend(["--mask-image", execution.input_file(mask_image)])
    if rescale_intensities is not None:
        cargs.extend(["--rescale-intensities", str(rescale_intensities)])
    if weight_image is not None:
        cargs.extend(["--weight-image", execution.input_file(weight_image)])
    if convergence is not None:
        cargs.extend(["--convergence", convergence])
    if bspline_fitting is not None:
        cargs.extend(["--bspline-fitting", bspline_fitting])
    if histogram_sharpening is not None:
        cargs.extend(["--histogram-sharpening", histogram_sharpening])
    if verbose is not None:
        cargs.extend(["--verbose", str(verbose)])
    cargs.extend(["--input-image", execution.input_file(input_image)])
    cargs.append("--output")
    cargs.append(
        "[" +
        corrected_image_path +
        "," +
        bias_field_path +
        "]"
    )
    ret = N4BiasFieldCorrectionOutputs(
        root=execution.output_file("."),
        corrected_image=execution.output_file(f"{corrected_image_path}"),
        bias_field=execution.output_file(f"{bias_field_path}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "N4BiasFieldCorrectionOutputs",
    "N4_BIAS_FIELD_CORRECTION_METADATA",
    "n4_bias_field_correction",
]
