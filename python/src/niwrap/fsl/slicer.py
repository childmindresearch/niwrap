# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SLICER_METADATA = Metadata(
    id="e29bda2d3989ff405f9246f4f13b3294b6506919",
    name="Slicer",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SlicerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sagittal_slice_outfile: OutputPathType | None
    """Output sagittal slice."""
    axial_slice_outfile: OutputPathType | None
    """Output axial slice."""
    coronal_slice_outfile: OutputPathType | None
    """Output coronal slice."""
    single_image_outfile: OutputPathType | None
    """Output mid-sagittal, -coronal, and -axial slices into one image."""
    all_axial_slices_outfile: OutputPathType | None
    """File name of every <sample'th> axial slice output image."""


def slicer(
    in_file: InputPathType,
    overlay_file: InputPathType | None = None,
    label_slices: bool = False,
    colour_map: InputPathType | None = None,
    scaling: float | int | None = None,
    intensity_range: list[float | int] = None,
    threshold_edges: float | int | None = None,
    dither_edges: bool = False,
    nearest_neighbour: bool = False,
    show_orientation: bool = False,
    red_dot_marker: bool = False,
    output_single_image: str | None = None,
    output_sagittal_slice: bool = False,
    output_sagittal_slice_fname: str | None = None,
    output_axial_slice: bool = False,
    output_axial_slice_fname: str | None = None,
    output_coronal_slice: bool = False,
    output_coronal_slice_fname: str | None = None,
    output_all_axial_slices: bool = False,
    output_all_axial_slices_fname: str | None = None,
    output_sample_axial_slices: bool = False,
    output_sample_axial_slices_width: str | None = None,
    output_sample_axial_slices_fname: str | None = None,
    runner: Runner = None,
) -> SlicerOutputs:
    """
    Slicer by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    the main program which takes in one or two input images and produces as many
    separate output pictures of slices as are requested. The basic output
    options (-x, -y and -z) produce single slice pictures. The more advanced
    options (-a, -A and -S) produce montages of various slices. slicer outputs
    PPM format pictures.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Miscvis
    
    Args:
        in_file: Input volume.
        overlay_file: Overlay volume.
        label_slices: Label slices with slice number.
        colour_map: Use different colour map from that specified in the header.
        scaling: Image scale.
        intensity_range: Specify intensity min and max for display range.
        threshold_edges: Use specified threshold for edges (if >0 use this
            proportion of max-min, if <0, use the absolute value)
        dither_edges: Produce semi-transparent (dithered) edges.
        nearest_neighbour: Use nearest neighbor interpolation for output.
        show_orientation: Do not put left-right labels in output
        red_dot_marker: Add a red dot marker to topright of image.
        output_single_image: Output mid-sagittal, -coronal, and -axial slices
            into one image.
        output_sagittal_slice: Output sagittal slice (if slice >0, it is a
            fraction of image dimension, if <0, it is absolute slice number).
        output_sagittal_slice_fname: Output file name sagittal slice.
        output_axial_slice: Output axial slice (if slice >0, it is a fraction of
            image dimension, if <0, it is absolute slice number).
        output_axial_slice_fname: Output file name axial slice.
        output_coronal_slice: Output coronal slice (if slice >0, it is a
            fraction of image dimension, if <0, it is absolute slice number).
        output_coronal_slice_fname: Output file name coronal slice.
        output_all_axial_slices: Maximum width of image of all axial slices.
        output_all_axial_slices_fname: File name of all axial slice output
            image.
        output_sample_axial_slices: Ouput every <sample>'th axial slice.
        output_sample_axial_slices_width: Width of every <sample'th> axial slice
            output image.
        output_sample_axial_slices_fname: File name of every <sample'th> axial
            slice output image.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SlicerOutputs`).
    """
    runner = runner or get_global_runner()
    if intensity_range is not None and (len(intensity_range) != 2): 
        raise ValueError(f"Length of 'intensity_range' must be 2 but was {len(intensity_range)}")
    if not (
        output_sagittal_slice ==
        (output_sagittal_slice_fname is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "output_sagittal_slice,\n"
            "output_sagittal_slice_fname"
        )
    if not (
        output_axial_slice ==
        (output_axial_slice_fname is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "output_axial_slice,\n"
            "output_axial_slice_fname"
        )
    if not (
        output_coronal_slice ==
        (output_coronal_slice_fname is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "output_coronal_slice,\n"
            "output_coronal_slice_fname"
        )
    if not (
        output_all_axial_slices ==
        (output_all_axial_slices_fname is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "output_all_axial_slices,\n"
            "output_all_axial_slices_fname"
        )
    if not (
        output_sample_axial_slices ==
        (output_sample_axial_slices_width is not None) ==
        (output_sample_axial_slices_fname is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "output_sample_axial_slices,\n"
            "output_sample_axial_slices_width,\n"
            "output_sample_axial_slices_fname"
        )
    execution = runner.start_execution(SLICER_METADATA)
    cargs = []
    cargs.append("slicer")
    cargs.append(execution.input_file(in_file))
    if overlay_file is not None:
        cargs.append(execution.input_file(overlay_file))
    if label_slices:
        cargs.append("-L")
    if colour_map is not None:
        cargs.extend(["-l", execution.input_file(colour_map)])
    if scaling is not None:
        cargs.extend(["-s", str(scaling)])
    if intensity_range is not None:
        cargs.extend(["-i", *map(str, intensity_range)])
    if threshold_edges is not None:
        cargs.extend(["-e", str(threshold_edges)])
    if dither_edges:
        cargs.append("-t")
    if nearest_neighbour:
        cargs.append("-n")
    if show_orientation:
        cargs.append("-u")
    if red_dot_marker:
        cargs.append("-c")
    cargs.append("...slices...")
    if output_single_image is not None:
        cargs.extend(["-a", output_single_image])
    if output_sagittal_slice:
        cargs.append("-x")
    if output_sagittal_slice_fname is not None:
        cargs.append(output_sagittal_slice_fname)
    if output_axial_slice:
        cargs.append("-y")
    if output_axial_slice_fname is not None:
        cargs.append(output_axial_slice_fname)
    if output_coronal_slice:
        cargs.append("-z")
    if output_coronal_slice_fname is not None:
        cargs.append(output_coronal_slice_fname)
    if output_all_axial_slices:
        cargs.append("-A")
    if output_all_axial_slices_fname is not None:
        cargs.append(output_all_axial_slices_fname)
    if output_sample_axial_slices:
        cargs.append("-S")
    if output_sample_axial_slices_width is not None:
        cargs.append(output_sample_axial_slices_width)
    if output_sample_axial_slices_fname is not None:
        cargs.append(output_sample_axial_slices_fname)
    ret = SlicerOutputs(
        root=execution.output_file("."),
        sagittal_slice_outfile=execution.output_file(f"{output_sagittal_slice_fname}", optional=True) if output_sagittal_slice_fname is not None else None,
        axial_slice_outfile=execution.output_file(f"{output_axial_slice_fname}", optional=True) if output_axial_slice_fname is not None else None,
        coronal_slice_outfile=execution.output_file(f"{output_coronal_slice_fname}", optional=True) if output_coronal_slice_fname is not None else None,
        single_image_outfile=execution.output_file(f"{output_single_image}", optional=True) if output_single_image is not None else None,
        all_axial_slices_outfile=execution.output_file(f"{output_sample_axial_slices_fname}", optional=True) if output_sample_axial_slices_fname is not None else None,
    )
    execution.run(cargs)
    return ret
