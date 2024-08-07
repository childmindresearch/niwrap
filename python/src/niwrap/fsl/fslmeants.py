# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLMEANTS_METADATA = Metadata(
    id="b3d1684f561c850de7920686f8bc9d35a1b93866",
    name="fslmeants",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslmeantsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmeants(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_text_matrix: OutputPathType | None
    """Output text matrix from fslmeants"""


def fslmeants(
    input_image: InputPathType,
    output: str | None = None,
    mask: InputPathType | None = None,
    coordinates: list[float | int] | None = None,
    usemm_flag: bool = False,
    showall_flag: bool = False,
    eigenv_flag: bool = False,
    eigenvariates_order: float | int | None = None,
    no_bin_flag: bool = False,
    label_image: InputPathType | None = None,
    transpose_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    weighted_mean_flag: bool = False,
    runner: Runner | None = None,
) -> FslmeantsOutputs:
    """
    fslmeants by University of Oxford (Mark Jenkinson, Christian F. Beckmann).
    
    Prints average timeseries (intensities) to the screen (or saves to a file).
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        input_image: Input 4D image.
        output: Output text matrix.
        mask: Input 3D mask.
        coordinates: Requested spatial coordinate (instead of mask). Must have\
            exactly three numerical entries in the list (3-vector).
        usemm_flag: Use mm instead of voxel coordinates (for -c option).
        showall_flag: Show all voxel time series (within mask) instead of\
            averaging.
        eigenv_flag: Calculate Eigenvariate(s) instead of mean (output will\
            have 0 mean).
        eigenvariates_order: Select number of Eigenvariates (default 1).
        no_bin_flag: Do not binarise the mask for calculation of Eigenvariates.
        label_image: Input 3D label image (generate separate mean for each\
            integer label value - cannot be used with showall).
        transpose_flag: Output results in transpose format (one row per\
            voxel/mean).
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display the help message.
        weighted_mean_flag: Output weighted mean, using mask values as weights,\
            and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmeantsOutputs`).
    """
    runner = runner or get_global_runner()
    if coordinates is not None and (len(coordinates) != 3): 
        raise ValueError(f"Length of 'coordinates' must be 3 but was {len(coordinates)}")
    execution = runner.start_execution(FSLMEANTS_METADATA)
    cargs = []
    cargs.append("fslmeants")
    cargs.append("-i")
    cargs.extend(["-i", execution.input_file(input_image)])
    if output is not None:
        cargs.extend(["-o", output])
    if mask is not None:
        cargs.extend(["-m", execution.input_file(mask)])
    if coordinates is not None:
        cargs.extend(["-c", *map(str, coordinates)])
    if usemm_flag:
        cargs.append("--usemm")
    if showall_flag:
        cargs.append("--showall")
    if eigenv_flag:
        cargs.append("--eig")
    if eigenvariates_order is not None:
        cargs.extend(["--order", str(eigenvariates_order)])
    if no_bin_flag:
        cargs.append("--no_bin")
    if label_image is not None:
        cargs.extend(["--label", execution.input_file(label_image)])
    if transpose_flag:
        cargs.append("--transpose")
    if weighted_mean_flag:
        cargs.append("-w")
    if verbose_flag:
        cargs.append("-v")
    ret = FslmeantsOutputs(
        root=execution.output_file("."),
        output_text_matrix=execution.output_file(f"{output}", optional=True) if output is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLMEANTS_METADATA",
    "FslmeantsOutputs",
    "fslmeants",
]
