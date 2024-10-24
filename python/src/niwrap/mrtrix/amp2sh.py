# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AMP2SH_METADATA = Metadata(
    id="739c6dd01d401b453eb41eade05065e6c9fd17b3.boutiques",
    name="amp2sh",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Amp2shFslgrad:
    """
    Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used.
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-fslgrad")
        cargs.append(execution.input_file(self.bvecs))
        cargs.append(execution.input_file(self.bvals))
        return cargs


@dataclasses.dataclass
class Amp2shVariousString:
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
class Amp2shVariousFile:
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
class Amp2shConfig:
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


class Amp2shOutputs(typing.NamedTuple):
    """
    Output object returned when calling `amp2sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sh: OutputPathType
    """the output spherical harmonics coefficients image."""


def amp2sh(
    amp: InputPathType,
    sh: str,
    lmax: int | None = None,
    normalise: bool = False,
    directions: InputPathType | None = None,
    rician: InputPathType | None = None,
    grad: InputPathType | None = None,
    fslgrad: Amp2shFslgrad | None = None,
    shells: list[float] | None = None,
    strides: typing.Union[Amp2shVariousString, Amp2shVariousFile] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Amp2shConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Amp2shOutputs:
    """
    Convert a set of amplitudes (defined along a set of corresponding directions) to
    their spherical harmonic representation.
    
    The spherical harmonic decomposition is calculated by least-squares linear
    fitting to the amplitude data.
    
    The directions can be defined either as a DW gradient scheme (for example to
    compute the SH representation of the DW signal), a set of [az el] pairs as
    output by the dirgen command, or a set of [ x y z ] directions in Cartesian
    coordinates. The DW gradient scheme or direction set can be supplied within
    the input image header or using the -gradient or -directions option. Note
    that if a direction set and DW gradient scheme can be found, the direction
    set will be used by default.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        amp: the input amplitude image.
        sh: the output spherical harmonics coefficients image.
        lmax: set the maximum harmonic order for the output series. By default,\
            the program will use the highest possible lmax given the number of\
            diffusion-weighted images, up to a maximum of 8.
        normalise: normalise the DW signal to the b=0 image.
        directions: the directions corresponding to the input amplitude image\
            used to sample AFD. By default this option is not required providing\
            the direction set is supplied in the amplitude image. This should be\
            supplied as a list of directions [az el], as generated using the dirgen\
            command, or as a list of [ x y z ] Cartesian coordinates.
        rician: correct for Rician noise induced bias, using noise map supplied.
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        shells: specify one or more b-values to use during processing, as a\
            comma-separated list of the desired approximate b-values (b-values are\
            clustered to allow for small deviations). Note that some commands are\
            incompatible with multiple b-values, and will report an error if more\
            than one b-value is provided.\
            WARNING: note that, even though the b=0 volumes are never referred\
            to as shells in the literature, they still have to be explicitly\
            included in the list of b-values as provided to the -shell option!\
            Several algorithms which include the b=0 volumes in their\
            computations may otherwise return an undesired result.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
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
        NamedTuple of outputs (described in `Amp2shOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AMP2SH_METADATA)
    cargs = []
    cargs.append("amp2sh")
    if lmax is not None:
        cargs.extend([
            "-lmax",
            str(lmax)
        ])
    if normalise:
        cargs.append("-normalise")
    if directions is not None:
        cargs.extend([
            "-directions",
            execution.input_file(directions)
        ])
    if rician is not None:
        cargs.extend([
            "-rician",
            execution.input_file(rician)
        ])
    if grad is not None:
        cargs.extend([
            "-grad",
            execution.input_file(grad)
        ])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
    if shells is not None:
        cargs.extend([
            "-shells",
            ",".join(map(str, shells))
        ])
    if strides is not None:
        cargs.extend([
            "-strides",
            *strides.run(execution)
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
    cargs.append(execution.input_file(amp))
    cargs.append(sh)
    ret = Amp2shOutputs(
        root=execution.output_file("."),
        sh=execution.output_file(sh),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AMP2SH_METADATA",
    "Amp2shConfig",
    "Amp2shFslgrad",
    "Amp2shOutputs",
    "Amp2shVariousFile",
    "Amp2shVariousString",
    "amp2sh",
]
