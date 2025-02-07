# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

N4_BIAS_FIELD_CORRECTION_METADATA = Metadata(
    id="430c0cf662702b145c28eac54a52db1b1f1ee70a.boutiques",
    name="N4BiasFieldCorrection",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
N4BiasFieldCorrectionConvergenceParameters = typing.TypedDict('N4BiasFieldCorrectionConvergenceParameters', {
    "__STYX_TYPE__": typing.Literal["convergence"],
    "convergence": list[int],
    "convergence_threshold": typing.NotRequired[float | None],
})
N4BiasFieldCorrectionBsplineFittingParameters = typing.TypedDict('N4BiasFieldCorrectionBsplineFittingParameters', {
    "__STYX_TYPE__": typing.Literal["bspline_fitting"],
    "spline_distance": list[float],
    "spline_order": typing.NotRequired[int | None],
})
N4BiasFieldCorrectionHistogramSharpeningParameters = typing.TypedDict('N4BiasFieldCorrectionHistogramSharpeningParameters', {
    "__STYX_TYPE__": typing.Literal["histogram_sharpening"],
    "fwhm": typing.NotRequired[float | None],
    "wiener_noise": typing.NotRequired[float | None],
    "number_of_histogram_bins": typing.NotRequired[int | None],
})
N4BiasFieldCorrectionParameters = typing.TypedDict('N4BiasFieldCorrectionParameters', {
    "__STYX_TYPE__": typing.Literal["N4BiasFieldCorrection"],
    "image_dimensionality": typing.NotRequired[typing.Literal[2, 3, 4] | None],
    "shrink_factor": typing.NotRequired[int | None],
    "mask_image": typing.NotRequired[InputPathType | None],
    "rescale_intensities": typing.NotRequired[typing.Literal[0, 1] | None],
    "weight_image": typing.NotRequired[InputPathType | None],
    "convergence": typing.NotRequired[N4BiasFieldCorrectionConvergenceParameters | None],
    "bspline_fitting": typing.NotRequired[N4BiasFieldCorrectionBsplineFittingParameters | None],
    "histogram_sharpening": typing.NotRequired[N4BiasFieldCorrectionHistogramSharpeningParameters | None],
    "verbose": typing.NotRequired[typing.Literal[0, 1] | None],
    "input_image": InputPathType,
    "corrected_image_path": str,
    "bias_field_path": typing.NotRequired[str | None],
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
        "N4BiasFieldCorrection": n4_bias_field_correction_cargs,
        "convergence": n4_bias_field_correction_convergence_cargs,
        "bspline_fitting": n4_bias_field_correction_bspline_fitting_cargs,
        "histogram_sharpening": n4_bias_field_correction_histogram_sharpening_cargs,
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
        "N4BiasFieldCorrection": n4_bias_field_correction_outputs,
        "convergence": n4_bias_field_correction_convergence_outputs,
        "bspline_fitting": n4_bias_field_correction_bspline_fitting_outputs,
        "histogram_sharpening": n4_bias_field_correction_histogram_sharpening_outputs,
    }.get(t)


def n4_bias_field_correction_convergence_params(
    convergence: list[int],
    convergence_threshold: float | None = None,
) -> N4BiasFieldCorrectionConvergenceParameters:
    """
    Build parameters.
    
    Args:
        convergence:.
        convergence_threshold:.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "convergence",
        "convergence": convergence,
    }
    if convergence_threshold is not None:
        params["convergence_threshold"] = convergence_threshold
    return params


def n4_bias_field_correction_convergence_cargs(
    params: N4BiasFieldCorrectionConvergenceParameters,
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
    if params.get("convergence_threshold") is not None:
        cargs.append("[" + "x".join(map(str, params.get("convergence"))) + "," + str(params.get("convergence_threshold")) + "]")
    return cargs


def n4_bias_field_correction_bspline_fitting_params(
    spline_distance: list[float],
    spline_order: int | None = None,
) -> N4BiasFieldCorrectionBsplineFittingParameters:
    """
    Build parameters.
    
    Args:
        spline_distance:.
        spline_order:.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bspline_fitting",
        "spline_distance": spline_distance,
    }
    if spline_order is not None:
        params["spline_order"] = spline_order
    return params


def n4_bias_field_correction_bspline_fitting_cargs(
    params: N4BiasFieldCorrectionBsplineFittingParameters,
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
    if params.get("spline_order") is not None:
        cargs.append("[" + "x".join(map(str, params.get("spline_distance"))) + "," + str(params.get("spline_order")) + "]")
    return cargs


def n4_bias_field_correction_histogram_sharpening_params(
    fwhm: float | None = None,
    wiener_noise: float | None = None,
    number_of_histogram_bins: int | None = None,
) -> N4BiasFieldCorrectionHistogramSharpeningParameters:
    """
    Build parameters.
    
    Args:
        fwhm:.
        wiener_noise:.
        number_of_histogram_bins:.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "histogram_sharpening",
    }
    if fwhm is not None:
        params["fwhm"] = fwhm
    if wiener_noise is not None:
        params["wiener_noise"] = wiener_noise
    if number_of_histogram_bins is not None:
        params["number_of_histogram_bins"] = number_of_histogram_bins
    return params


def n4_bias_field_correction_histogram_sharpening_cargs(
    params: N4BiasFieldCorrectionHistogramSharpeningParameters,
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
    if params.get("fwhm") is not None or params.get("wiener_noise") is not None or params.get("number_of_histogram_bins") is not None:
        cargs.append("[" + (str(params.get("fwhm")) if (params.get("fwhm") is not None) else "") + "," + (str(params.get("wiener_noise")) if (params.get("wiener_noise") is not None) else "") + "," + (str(params.get("number_of_histogram_bins")) if (params.get("number_of_histogram_bins") is not None) else "") + "]")
    return cargs


class N4BiasFieldCorrectionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `n4_bias_field_correction(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_image: OutputPathType
    """The bias corrected version of the input image."""
    bias_field: OutputPathType | None
    """Estimated bias field image."""


def n4_bias_field_correction_params(
    input_image: InputPathType,
    corrected_image_path: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    shrink_factor: int | None = None,
    mask_image: InputPathType | None = None,
    rescale_intensities: typing.Literal[0, 1] | None = None,
    weight_image: InputPathType | None = None,
    convergence: N4BiasFieldCorrectionConvergenceParameters | None = None,
    bspline_fitting: N4BiasFieldCorrectionBsplineFittingParameters | None = None,
    histogram_sharpening: N4BiasFieldCorrectionHistogramSharpeningParameters | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    bias_field_path: str | None = None,
) -> N4BiasFieldCorrectionParameters:
    """
    Build parameters.
    
    Args:
        input_image: -i, --input-image inputImageFilename. A scalar image is\
            expected as input for bias correction. Since N4 log transforms the\
            intensities, negative values or values close to zero should be\
            processed prior to correction.
        corrected_image_path: The bias corrected version of the input image.
        image_dimensionality: -d, --image-dimensionality 2/3/4. This option\
            forces the image to be treated as a specified-dimensional image. If not\
            specified, N4 tries to infer the dimensionality from the input image.
        shrink_factor: -s, --shrink-factor 1/2/3/(4)/... Running N4 on large\
            images can be time consuming. To lessen computation time, the input\
            image can be resampled. The shrink factor, specified as a single\
            integer, describes this resampling. Shrink factors <= 4 are commonly\
            used. Note that the shrink factor is only applied to the first two or\
            three dimensions which we assume are spatial.
        mask_image: -x, --mask-image maskImageFilename. If a mask image is\
            specified, the final bias correction is only performed in the mask\
            region. If a weight image is not specified, only intensity values\
            inside the masked region are used during the execution of the\
            algorithm. If a weight image is specified, only the non-zero weights\
            are used in the execution of the algorithm although the mask region\
            defines where bias correction is performed in the final output.\
            Otherwise bias correction occurs over the entire image domain. See also\
            the option description for the weight image. If a mask image is *not*\
            specified then the entire image region will be used as the mask region.\
            Note that this is different than the N3 implementation which uses the\
            results of Otsu thresholding to define a mask. However, this leads to\
            unknown anatomical regions being included and excluded during the bias\
            correction.
        rescale_intensities: -r, --rescale-intensities 0/(1). At each\
            iteration, a new intensity mapping is calculated and applied but there\
            is nothing which constrains the new intensity range to be within\
            certain values. The result is that the range can "drift" from the\
            original at each iteration. This option rescales to the [min,max] range\
            of the original image intensities within the user-specified mask. A\
            mask is required to perform rescaling.
        weight_image: -w, --weight-image weightImageFilename. The weight image\
            allows the user to perform a relative weighting of specific voxels\
            during the B-spline fitting. For example, some studies have shown that\
            N3 performed on white matter segmentations improves performance. If one\
            has a spatial probability map of the white matter, one can use this map\
            to weight the b-spline fitting towards those voxels which are more\
            probabilistically classified as white matter. See also the option\
            description for the mask image.
        convergence: -c, --convergence\
            [<numberOfIterations=50x50x50x50>,<convergenceThreshold=0.0>].\
            Convergence is determined by calculating the coefficient of variation\
            between subsequent iterations. When this value is less than the\
            specified threshold from the previous iteration or the maximum number\
            of iterations is exceeded the program terminates. Multiple resolutions\
            can be specified by using 'x' between the number of iterations at each\
            resolution, e.g. 100x50x50.
        bspline_fitting: -b, --bspline-fitting\
            [splineDistance,<splineOrder=3>]. These options describe the b-spline\
            fitting parameters. The initial b-spline mesh at the coarsest\
            resolution is specified either as the number of elements in each\
            dimension, e.g. 2x2x3 for 3-D images, or it can be specified as a\
            single scalar parameter which describes the isotropic sizing of the\
            mesh elements. The latter option is typically preferred. For each\
            subsequent level, the spline distance decreases in half, or\
            equivalently, the number of mesh elements doubles Cubic splines (order\
            = 3) are typically used. The default setting is to employ a single mesh\
            element over the entire domain, i.e., -b [1x1x1,3].
        histogram_sharpening: -t, --histogram-sharpening\
            [<FWHM=0.15>,<wienerNoise=0.01>,<numberOfHistogramBins=200>]. These\
            options describe the histogram sharpening parameters, i.e. the\
            deconvolution step parameters described in the original N3 algorithm.\
            The default values have been shown to work fairly well.
        verbose: Verbose output.
        bias_field_path: Estimated bias field image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "N4BiasFieldCorrection",
        "input_image": input_image,
        "corrected_image_path": corrected_image_path,
    }
    if image_dimensionality is not None:
        params["image_dimensionality"] = image_dimensionality
    if shrink_factor is not None:
        params["shrink_factor"] = shrink_factor
    if mask_image is not None:
        params["mask_image"] = mask_image
    if rescale_intensities is not None:
        params["rescale_intensities"] = rescale_intensities
    if weight_image is not None:
        params["weight_image"] = weight_image
    if convergence is not None:
        params["convergence"] = convergence
    if bspline_fitting is not None:
        params["bspline_fitting"] = bspline_fitting
    if histogram_sharpening is not None:
        params["histogram_sharpening"] = histogram_sharpening
    if verbose is not None:
        params["verbose"] = verbose
    if bias_field_path is not None:
        params["bias_field_path"] = bias_field_path
    return params


def n4_bias_field_correction_cargs(
    params: N4BiasFieldCorrectionParameters,
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
    cargs.append("N4BiasFieldCorrection")
    if params.get("image_dimensionality") is not None:
        cargs.extend([
            "--image-dimensionality",
            str(params.get("image_dimensionality"))
        ])
    if params.get("shrink_factor") is not None:
        cargs.extend([
            "--shrink-factor",
            str(params.get("shrink_factor"))
        ])
    if params.get("mask_image") is not None:
        cargs.extend([
            "--mask-image",
            execution.input_file(params.get("mask_image"))
        ])
    if params.get("rescale_intensities") is not None:
        cargs.extend([
            "--rescale-intensities",
            str(params.get("rescale_intensities"))
        ])
    if params.get("weight_image") is not None:
        cargs.extend([
            "--weight-image",
            execution.input_file(params.get("weight_image"))
        ])
    if params.get("convergence") is not None:
        cargs.extend([
            "--convergence",
            *dyn_cargs(params.get("convergence")["__STYXTYPE__"])(params.get("convergence"), execution)
        ])
    if params.get("bspline_fitting") is not None:
        cargs.extend([
            "--bspline-fitting",
            *dyn_cargs(params.get("bspline_fitting")["__STYXTYPE__"])(params.get("bspline_fitting"), execution)
        ])
    if params.get("histogram_sharpening") is not None:
        cargs.extend([
            "--histogram-sharpening",
            *dyn_cargs(params.get("histogram_sharpening")["__STYXTYPE__"])(params.get("histogram_sharpening"), execution)
        ])
    if params.get("verbose") is not None:
        cargs.extend([
            "--verbose",
            str(params.get("verbose"))
        ])
    cargs.extend([
        "--input-image",
        execution.input_file(params.get("input_image"))
    ])
    cargs.append("--output")
    if params.get("bias_field_path") is not None:
        cargs.append("[" + params.get("corrected_image_path") + "," + params.get("bias_field_path") + "]")
    return cargs


def n4_bias_field_correction_outputs(
    params: N4BiasFieldCorrectionParameters,
    execution: Execution,
) -> N4BiasFieldCorrectionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = N4BiasFieldCorrectionOutputs(
        root=execution.output_file("."),
        corrected_image=execution.output_file(params.get("corrected_image_path")),
        bias_field=execution.output_file(params.get("bias_field_path")) if (params.get("bias_field_path") is not None) else None,
    )
    return ret


def n4_bias_field_correction_execute(
    params: N4BiasFieldCorrectionParameters,
    execution: Execution,
) -> N4BiasFieldCorrectionOutputs:
    """
    N4 is a variant of the popular N3 (nonparameteric nonuniform normalization)
    retrospective bias correction algorithm. Based on the assumption that the
    corruption of the low frequency bias field can be modeled as a convolution of
    the intensity histogram by a Gaussian, the basic algorithmic protocol is to
    iterate between deconvolving the intensity histogram by a Gaussian, remapping
    the intensities, and then spatially smoothing this result by a B-spline modeling
    of the bias field itself.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `N4BiasFieldCorrectionOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = n4_bias_field_correction_cargs(params, execution)
    ret = n4_bias_field_correction_outputs(params, execution)
    execution.run(cargs)
    return ret


def n4_bias_field_correction(
    input_image: InputPathType,
    corrected_image_path: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    shrink_factor: int | None = None,
    mask_image: InputPathType | None = None,
    rescale_intensities: typing.Literal[0, 1] | None = None,
    weight_image: InputPathType | None = None,
    convergence: N4BiasFieldCorrectionConvergenceParameters | None = None,
    bspline_fitting: N4BiasFieldCorrectionBsplineFittingParameters | None = None,
    histogram_sharpening: N4BiasFieldCorrectionHistogramSharpeningParameters | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    bias_field_path: str | None = None,
    runner: Runner | None = None,
) -> N4BiasFieldCorrectionOutputs:
    """
    N4 is a variant of the popular N3 (nonparameteric nonuniform normalization)
    retrospective bias correction algorithm. Based on the assumption that the
    corruption of the low frequency bias field can be modeled as a convolution of
    the intensity histogram by a Gaussian, the basic algorithmic protocol is to
    iterate between deconvolving the intensity histogram by a Gaussian, remapping
    the intensities, and then spatially smoothing this result by a B-spline modeling
    of the bias field itself.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        input_image: -i, --input-image inputImageFilename. A scalar image is\
            expected as input for bias correction. Since N4 log transforms the\
            intensities, negative values or values close to zero should be\
            processed prior to correction.
        corrected_image_path: The bias corrected version of the input image.
        image_dimensionality: -d, --image-dimensionality 2/3/4. This option\
            forces the image to be treated as a specified-dimensional image. If not\
            specified, N4 tries to infer the dimensionality from the input image.
        shrink_factor: -s, --shrink-factor 1/2/3/(4)/... Running N4 on large\
            images can be time consuming. To lessen computation time, the input\
            image can be resampled. The shrink factor, specified as a single\
            integer, describes this resampling. Shrink factors <= 4 are commonly\
            used. Note that the shrink factor is only applied to the first two or\
            three dimensions which we assume are spatial.
        mask_image: -x, --mask-image maskImageFilename. If a mask image is\
            specified, the final bias correction is only performed in the mask\
            region. If a weight image is not specified, only intensity values\
            inside the masked region are used during the execution of the\
            algorithm. If a weight image is specified, only the non-zero weights\
            are used in the execution of the algorithm although the mask region\
            defines where bias correction is performed in the final output.\
            Otherwise bias correction occurs over the entire image domain. See also\
            the option description for the weight image. If a mask image is *not*\
            specified then the entire image region will be used as the mask region.\
            Note that this is different than the N3 implementation which uses the\
            results of Otsu thresholding to define a mask. However, this leads to\
            unknown anatomical regions being included and excluded during the bias\
            correction.
        rescale_intensities: -r, --rescale-intensities 0/(1). At each\
            iteration, a new intensity mapping is calculated and applied but there\
            is nothing which constrains the new intensity range to be within\
            certain values. The result is that the range can "drift" from the\
            original at each iteration. This option rescales to the [min,max] range\
            of the original image intensities within the user-specified mask. A\
            mask is required to perform rescaling.
        weight_image: -w, --weight-image weightImageFilename. The weight image\
            allows the user to perform a relative weighting of specific voxels\
            during the B-spline fitting. For example, some studies have shown that\
            N3 performed on white matter segmentations improves performance. If one\
            has a spatial probability map of the white matter, one can use this map\
            to weight the b-spline fitting towards those voxels which are more\
            probabilistically classified as white matter. See also the option\
            description for the mask image.
        convergence: -c, --convergence\
            [<numberOfIterations=50x50x50x50>,<convergenceThreshold=0.0>].\
            Convergence is determined by calculating the coefficient of variation\
            between subsequent iterations. When this value is less than the\
            specified threshold from the previous iteration or the maximum number\
            of iterations is exceeded the program terminates. Multiple resolutions\
            can be specified by using 'x' between the number of iterations at each\
            resolution, e.g. 100x50x50.
        bspline_fitting: -b, --bspline-fitting\
            [splineDistance,<splineOrder=3>]. These options describe the b-spline\
            fitting parameters. The initial b-spline mesh at the coarsest\
            resolution is specified either as the number of elements in each\
            dimension, e.g. 2x2x3 for 3-D images, or it can be specified as a\
            single scalar parameter which describes the isotropic sizing of the\
            mesh elements. The latter option is typically preferred. For each\
            subsequent level, the spline distance decreases in half, or\
            equivalently, the number of mesh elements doubles Cubic splines (order\
            = 3) are typically used. The default setting is to employ a single mesh\
            element over the entire domain, i.e., -b [1x1x1,3].
        histogram_sharpening: -t, --histogram-sharpening\
            [<FWHM=0.15>,<wienerNoise=0.01>,<numberOfHistogramBins=200>]. These\
            options describe the histogram sharpening parameters, i.e. the\
            deconvolution step parameters described in the original N3 algorithm.\
            The default values have been shown to work fairly well.
        verbose: Verbose output.
        bias_field_path: Estimated bias field image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `N4BiasFieldCorrectionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(N4_BIAS_FIELD_CORRECTION_METADATA)
    params = n4_bias_field_correction_params(image_dimensionality=image_dimensionality, shrink_factor=shrink_factor, mask_image=mask_image, rescale_intensities=rescale_intensities, weight_image=weight_image, convergence=convergence, bspline_fitting=bspline_fitting, histogram_sharpening=histogram_sharpening, verbose=verbose, input_image=input_image, corrected_image_path=corrected_image_path, bias_field_path=bias_field_path)
    return n4_bias_field_correction_execute(params, execution)


__all__ = [
    "N4BiasFieldCorrectionBsplineFittingParameters",
    "N4BiasFieldCorrectionConvergenceParameters",
    "N4BiasFieldCorrectionHistogramSharpeningParameters",
    "N4BiasFieldCorrectionOutputs",
    "N4BiasFieldCorrectionParameters",
    "N4_BIAS_FIELD_CORRECTION_METADATA",
    "n4_bias_field_correction",
    "n4_bias_field_correction_bspline_fitting_params",
    "n4_bias_field_correction_convergence_params",
    "n4_bias_field_correction_histogram_sharpening_params",
    "n4_bias_field_correction_params",
]
