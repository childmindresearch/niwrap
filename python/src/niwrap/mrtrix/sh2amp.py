# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


SH2AMP_METADATA = Metadata(
    id="45b05c0a8f0911a8731afd6f2a99c25b291d4485",
    name="sh2amp",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Sh2ampFslgrad:
    """
    Provide the diffusion-weighted gradient scheme used in the acquisition in FSL bvecs/bvals format files. If a diffusion gradient scheme is present in the input image header, the data provided with this option will be instead used.
    """
    bvecs: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    bvals: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-fslgrad")
        cargs.extend(["", execution.input_file(self.bvecs)])
        cargs.extend(["", execution.input_file(self.bvals)])
        return cargs


@dataclasses.dataclass
class Sh2ampConfig:
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
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.extend(["", self.key])
        cargs.extend(["", self.value])
        return cargs


class Sh2ampOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sh2amp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image consisting of the amplitude of the SH functions along the specified directions."""


def sh2amp(
    input_: InputPathType,
    directions: InputPathType,
    output: InputPathType,
    nonnegative: bool = False,
    grad: InputPathType | None = None,
    fslgrad: Sh2ampFslgrad | None = None,
    strides: str | None = None,
    datatype: typing.Literal["spec"] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Sh2ampConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Sh2ampOutputs:
    """
    sh2amp by David Raffelt (david.raffelt@florey.edu.au) and J-Donald Tournier
    (jdtournier@gmail.com).
    
    Evaluate the amplitude of an image of spherical harmonic functions along
    specified directions.
    
    The input image should consist of a 4D or 5D image, with SH coefficients
    along the 4th dimension according to the convention below. If 4D (or size 1
    along the 5th dimension), the program expects to be provided with a single
    shell of directions. If 5D, each set of coefficients along the 5th dimension
    is understood to correspond to a different shell.
    
    The directions can be provided as:
    - a 2-column ASCII text file contained azimuth / elevation pairs (as
    produced by dirgen)
    - a 3-column ASCII text file containing x, y, z Cartesian direction vectors
    (as produced by dirgen -cart)
    - a 4-column ASCII text file containing the x, y, z, b components of a full
    DW encoding scheme (in MRtrix format, see main documentation for details).
    - an image file whose header contains a valid DW encoding scheme
    
    If a full DW encoding is provided, the number of shells needs to match those
    found in the input image of coefficients (i.e. its size along the 5th
    dimension). If needed, the -shell option can be used to pick out the
    specific shell(s) of interest.
    
    If the input image contains multiple shells (its size along the 5th
    dimension is greater than one), the program will expect the direction set to
    contain multiple shells, which can only be provided as a full DW encodings
    (the last two options in the list above).
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/sh2amp.html
    
    Args:
        input_: the input image consisting of spherical harmonic (SH)
            coefficients.
        directions: the list of directions along which the SH functions will be
            sampled, generated using the dirgen command
        output: the output image consisting of the amplitude of the SH functions
            along the specified directions.
        nonnegative: cap all negative amplitudes to zero
        grad: Provide the diffusion-weighted gradient scheme used in the
            acquisition in a text file. This should be supplied as a 4xN text file
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe
            the direction of the applied gradient, and b gives the b-value in units
            of s/mm^2. If a diffusion gradient scheme is present in the input image
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient
            scheme is present in the input image header, the data provided with this
            option will be instead used.
        strides: specify the strides of the output data in memory; either as a
            comma-separated list of (signed) integers, or as a template image from
            which the strides shall be extracted and used. The actual strides
            produced will depend on whether the output image format can support it.
        datatype: specify output image data type. Valid choices are: float32,
            float32le, float32be, float64, float64le, float64be, int64, uint64,
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,
            int8, uint8, bit.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `Sh2ampOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SH2AMP_METADATA)
    cargs = []
    cargs.append("sh2amp")
    if nonnegative:
        cargs.append("-nonnegative")
    if grad is not None:
        cargs.extend(["-grad", execution.input_file(grad)])
    if fslgrad is not None:
        cargs.extend(["-fslgrad", *fslgrad.run(execution)])
    if strides is not None:
        cargs.extend(["-strides", strides])
    if datatype is not None:
        cargs.extend(["-datatype", datatype])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend(["-config", *[a for c in [s.run(execution) for s in config] for a in c]])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(["", execution.input_file(input_)])
    cargs.extend(["", execution.input_file(directions)])
    cargs.extend(["", execution.input_file(output)])
    ret = Sh2ampOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SH2AMP_METADATA",
    "Sh2ampConfig",
    "Sh2ampFslgrad",
    "Sh2ampOutputs",
    "sh2amp",
]