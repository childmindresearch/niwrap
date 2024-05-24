# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


SH2PEAKS_METADATA = Metadata(
    id="22cf835bd8055e83c00084e360a525f009a55eaf",
    name="sh2peaks",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Sh2peaksDirection:
    """
    the direction of a peak to estimate. The algorithm will attempt to find the same number of peaks as have been specified using this option.
    """
    phi: float | int
    """the direction of a peak to estimate. The algorithm will attempt to find
    the same number of peaks as have been specified using this option."""
    theta: float | int
    """the direction of a peak to estimate. The algorithm will attempt to find
    the same number of peaks as have been specified using this option."""
    
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
        cargs.append("-direction")
        cargs.extend(["", str(self.phi)])
        cargs.extend(["", str(self.theta)])
        return cargs


@dataclasses.dataclass
class Sh2peaksConfig:
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


class Sh2peaksOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sh2peaks(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image. Each volume corresponds to the x, y & z component of each peak direction vector in turn."""


def sh2peaks(
    sh: InputPathType,
    output: InputPathType,
    num: int | None = None,
    direction: list[Sh2peaksDirection] = None,
    peaks: InputPathType | None = None,
    threshold: float | int | None = None,
    seeds: InputPathType | None = None,
    mask: InputPathType | None = None,
    fast: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Sh2peaksConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Sh2peaksOutputs:
    """
    sh2peaks by J-Donald Tournier (jdtournier@gmail.com).
    
    Extract the peaks of a spherical harmonic function in each voxel.
    
    Peaks of the spherical harmonic function in each voxel are located by
    commencing a Newton search along each of a set of pre-specified directions
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    Jeurissen, B.; Leemans, A.; Tournier, J.-D.; Jones, D.K.; Sijbers, J.
    Investigating the prevalence of complex fiber configurations in white matter
    tissue with diffusion magnetic resonance imaging. Human Brain Mapping, 2013,
    34(11), 2747-2766.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/sh2peaks.html
    
    Args:
        sh: the input image of SH coefficients.
        output: the output image. Each volume corresponds to the x, y & z
            component of each peak direction vector in turn.
        num: the number of peaks to extract (default: 3).
        direction: the direction of a peak to estimate. The algorithm will
            attempt to find the same number of peaks as have been specified using
            this option.
        peaks: the program will try to find the peaks that most closely match
            those in the image provided.
        threshold: only peak amplitudes greater than the threshold will be
            considered.
        seeds: specify a set of directions from which to start the multiple
            restarts of the optimisation (by default, the built-in 60 direction set
            is used)
        mask: only perform computation within the specified binary brain mask
            image.
        fast: use lookup table to compute associated Legendre polynomials
            (faster, but approximate).
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
        NamedTuple of outputs (described in `Sh2peaksOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SH2PEAKS_METADATA)
    cargs = []
    cargs.append("sh2peaks")
    if num is not None:
        cargs.extend(["-num", str(num)])
    if direction is not None:
        cargs.extend(["-direction", *[a for c in [s.run(execution) for s in direction] for a in c]])
    if peaks is not None:
        cargs.extend(["-peaks", execution.input_file(peaks)])
    if threshold is not None:
        cargs.extend(["-threshold", str(threshold)])
    if seeds is not None:
        cargs.extend(["-seeds", execution.input_file(seeds)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if fast:
        cargs.append("-fast")
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
    cargs.extend(["", execution.input_file(sh)])
    cargs.extend(["", execution.input_file(output)])
    ret = Sh2peaksOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SH2PEAKS_METADATA",
    "Sh2peaksConfig",
    "Sh2peaksDirection",
    "Sh2peaksOutputs",
    "sh2peaks",
]