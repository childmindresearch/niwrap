# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRGRID_METADATA = Metadata(
    id="38b5784d2ea0ffb125cf48797846326fbc4d3517.boutiques",
    name="mrgrid",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrgridAxis:
    """
    pad or crop the input image along the provided axis (defined by index). The
    specifier argument defines the number of voxels added or removed on the
    lower or upper end of the axis (-axis index delta_lower,delta_upper) or acts
    as a voxel selection range (-axis index start:stop). In both modes, values
    are relative to the input image (overriding all other extent-specifying
    options). Negative delta specifier values trigger the inverse operation (pad
    instead of crop and vice versa) and negative range specifier trigger
    padding. Note that the deprecated commands 'mrcrop' and 'mrpad' used
    range-based and delta-based -axis indices, respectively.
    """
    index: int
    """pad or crop the input image along the provided axis (defined by index).
    The specifier argument defines the number of voxels added or removed on the
    lower or upper end of the axis (-axis index delta_lower,delta_upper) or acts
    as a voxel selection range (-axis index start:stop). In both modes, values
    are relative to the input image (overriding all other extent-specifying
    options). Negative delta specifier values trigger the inverse operation (pad
    instead of crop and vice versa) and negative range specifier trigger
    padding. Note that the deprecated commands 'mrcrop' and 'mrpad' used
    range-based and delta-based -axis indices, respectively."""
    spec: str
    """pad or crop the input image along the provided axis (defined by index).
    The specifier argument defines the number of voxels added or removed on the
    lower or upper end of the axis (-axis index delta_lower,delta_upper) or acts
    as a voxel selection range (-axis index start:stop). In both modes, values
    are relative to the input image (overriding all other extent-specifying
    options). Negative delta specifier values trigger the inverse operation (pad
    instead of crop and vice versa) and negative range specifier trigger
    padding. Note that the deprecated commands 'mrcrop' and 'mrpad' used
    range-based and delta-based -axis indices, respectively."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-axis")
        cargs.append(str(self.index))
        cargs.append(self.spec)
        return cargs


@dataclasses.dataclass
class MrgridVariousString:
    obj: str
    """String object."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append(self.obj)
        return cargs


@dataclasses.dataclass
class MrgridVariousFile:
    obj: InputPathType
    """File object."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append(execution.input_file(self.obj))
        return cargs


@dataclasses.dataclass
class MrgridConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class MrgridOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrgrid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""


def mrgrid(
    input_: InputPathType,
    operation: str,
    output: str,
    template: InputPathType | None = None,
    size: list[int] | None = None,
    voxel: list[float] | None = None,
    scale: list[float] | None = None,
    interp: str | None = None,
    oversample: list[int] | None = None,
    as_: InputPathType | None = None,
    uniform: int | None = None,
    mask: InputPathType | None = None,
    crop_unbound: bool = False,
    axis: list[MrgridAxis] | None = None,
    all_axes: bool = False,
    fill: float | None = None,
    strides: typing.Union[MrgridVariousString, MrgridVariousFile] | None = None,
    datatype: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrgridConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrgridOutputs:
    """
    Modify the grid of an image without interpolation (cropping or padding) or by
    regridding to an image grid with modified orientation, location and or
    resolution. The image content remains in place in real world coordinates..
    
    - regrid: This operation performs changes of the voxel grid that require
    interpolation of the image such as changing the resolution or location and
    orientation of the voxel grid. If the image is down-sampled, the appropriate
    smoothing is automatically applied using Gaussian smoothing unless nearest
    neighbour interpolation is selected or oversample is changed explicitly. The
    resolution can only be changed for spatial dimensions.
    
    - crop: The image extent after cropping, can be specified either manually
    for each axis dimensions, or via a mask or reference image. The image can be
    cropped to the extent of a mask. This is useful for axially-acquired brain
    images, where the image size can be reduced by a factor of 2 by removing the
    empty space on either side of the brain. Note that cropping does not extend
    the image beyond the original FOV unless explicitly specified (via
    -crop_unbound or negative -axis extent).
    
    - pad: Analogously to cropping, padding increases the FOV of an image
    without image interpolation. Pad and crop can be performed simultaneously by
    specifying signed specifier argument values to the -axis option.
    
    This command encapsulates and extends the functionality of the superseded
    commands 'mrpad', 'mrcrop' and 'mrresize'. Note the difference in -axis
    convention used for 'mrcrop' and 'mrpad' (see -axis option description).
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: input image to be regridded.
        operation: the operation to be performed, one of: regrid, crop, pad.
        output: the output image.
        template: match the input image grid (voxel spacing, image size, header\
            transformation) to that of a reference image. The image resolution\
            relative to the template image can be changed with one of -size,\
            -voxel, -scale.
        size: define the size (number of voxels) in each spatial dimension for\
            the output image. This should be specified as a comma-separated list.
        voxel: define the new voxel size for the output image. This can be\
            specified either as a single value to be used for all spatial\
            dimensions, or as a comma-separated list of the size for each voxel\
            dimension.
        scale: scale the image resolution by the supplied factor. This can be\
            specified either as a single value to be used for all dimensions, or as\
            a comma-separated list of scale factors for each dimension.
        interp: set the interpolation method to use when reslicing (choices:\
            nearest, linear, cubic, sinc. Default: cubic).
        oversample: set the amount of over-sampling (in the target space) to\
            perform when regridding. This is particularly relevant when downsamping\
            a high-resolution image to a low-resolution image, to avoid aliasing\
            artefacts. This can consist of a single integer, or a comma-separated\
            list of 3 integers if different oversampling factors are desired along\
            the different axes. Default is determined from ratio of voxel\
            dimensions (disabled for nearest-neighbour interpolation).
        as_: pad or crop the input image on the upper bound to match the\
            specified reference image grid. This operation ignores differences in\
            image transformation between input and reference image.
        uniform: pad or crop the input image by a uniform number of voxels on\
            all sides.
        mask: crop the input image according to the spatial extent of a mask\
            image. The mask must share a common voxel grid with the input image but\
            differences in image transformations are ignored. Note that even though\
            only 3 dimensions are cropped when using a mask, the bounds are\
            computed by checking the extent for all dimensions. Note that by\
            default a gap of 1 voxel is left at all edges of the image to allow\
            valid trilinear interpolation. This gap can be modified with the\
            -uniform option but by default it does not extend beyond the FOV unless\
            -crop_unbound is used.
        crop_unbound: Allow padding beyond the original FOV when cropping.
        axis: pad or crop the input image along the provided axis (defined by\
            index). The specifier argument defines the number of voxels added or\
            removed on the lower or upper end of the axis (-axis index\
            delta_lower,delta_upper) or acts as a voxel selection range (-axis\
            index start:stop). In both modes, values are relative to the input\
            image (overriding all other extent-specifying options). Negative delta\
            specifier values trigger the inverse operation (pad instead of crop and\
            vice versa) and negative range specifier trigger padding. Note that the\
            deprecated commands 'mrcrop' and 'mrpad' used range-based and\
            delta-based -axis indices, respectively.
        all_axes: Crop or pad all, not just spatial axes.
        fill: Use number as the out of bounds value. nan, inf and -inf are\
            valid arguments. (Default: 0.0).
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrgridOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRGRID_METADATA)
    cargs = []
    cargs.append("mrgrid")
    if template is not None:
        cargs.extend([
            "-template",
            execution.input_file(template)
        ])
    if size is not None:
        cargs.extend([
            "-size",
            ",".join(map(str, size))
        ])
    if voxel is not None:
        cargs.extend([
            "-voxel",
            ",".join(map(str, voxel))
        ])
    if scale is not None:
        cargs.extend([
            "-scale",
            ",".join(map(str, scale))
        ])
    if interp is not None:
        cargs.extend([
            "-interp",
            interp
        ])
    if oversample is not None:
        cargs.extend([
            "-oversample",
            ",".join(map(str, oversample))
        ])
    if as_ is not None:
        cargs.extend([
            "-as",
            execution.input_file(as_)
        ])
    if uniform is not None:
        cargs.extend([
            "-uniform",
            str(uniform)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if crop_unbound:
        cargs.append("-crop_unbound")
    if axis is not None:
        cargs.extend([a for c in [s.run(execution) for s in axis] for a in c])
    if all_axes:
        cargs.append("-all_axes")
    if fill is not None:
        cargs.extend([
            "-fill",
            str(fill)
        ])
    if strides is not None:
        cargs.extend([
            "-strides",
            *strides.run(execution)
        ])
    if datatype is not None:
        cargs.extend([
            "-datatype",
            datatype
        ])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(input_))
    cargs.append(operation)
    cargs.append(output)
    ret = MrgridOutputs(
        root=execution.output_file("."),
        output=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRGRID_METADATA",
    "MrgridAxis",
    "MrgridConfig",
    "MrgridOutputs",
    "MrgridVariousFile",
    "MrgridVariousString",
    "mrgrid",
]
