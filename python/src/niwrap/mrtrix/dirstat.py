# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


DIRSTAT_METADATA = Metadata(
    id="23d54a9eb34a7b46332442cb22042095b35f0bfc",
    name="dirstat",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class FslgradOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Fslgrad.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Fslgrad:
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
        cargs.append(execution.input_file(self.bvecs))
        cargs.append(execution.input_file(self.bvals))
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> FslgradOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `FslgradOutputs`).
        """
        ret = FslgradOutputs(
            root=execution.output_file("."),
        )
        return ret


class ConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Config.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Config:
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
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> ConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ConfigOutputs`).
        """
        ret = ConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class DirstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dirstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fslgrad: FslgradOutputs
    """Subcommand outputs"""
    config: ConfigOutputs
    """Subcommand outputs"""


def dirstat(
    dirs: InputPathType,
    output: str | None = None,
    shells: list[float | int] = None,
    grad: InputPathType | None = None,
    fslgrad: Fslgrad | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Config] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> DirstatOutputs:
    """
    dirstat by J-Donald Tournier (jdtournier@gmail.com).
    
    Report statistics on a direction set.
    
    This command will accept as inputs:
    
    - directions file in spherical coordinates (ASCII text, [ az el ]
    space-separated values, one per line);
    
    - directions file in Cartesian coordinates (ASCII text, [ x y z ]
    space-separated values, one per line);
    
    - DW gradient files (MRtrix format: ASCII text, [ x y z b ] space-separated
    values, one per line);
    
    - image files, using the DW gradient scheme found in the header (or provided
    using the appropriate command line options below).
    
    By default, this produces all relevant metrics for the direction set
    provided. If the direction set contains multiple shells, metrics are
    provided for each shell separately.
    
    Metrics are produced assuming a unipolar or bipolar electrostatic repulsion
    model, producing the potential energy (total, mean, min & max), and the
    nearest-neighbour angles (mean, min & max). The condition number is also
    produced for the spherical harmonic fits up to the highest harmonic order
    supported by the number of volumes. Finally, the norm of the mean direction
    vector is provided as a measure of the overall symmetry of the direction set
    (important with respect to eddy-current resilience).
    
    Specific metrics can also be queried independently via the "-output" option,
    using these shorthands:
    U/B for unipolar/bipolar model,
    E/N for energy and nearest-neighbour respectively,
    t/-/+ for total/min/max respectively (mean implied otherwise);
    SHn for condition number of SH fit at order n (with n an even integer);
    ASYM for asymmetry index (norm of mean direction vector);
    N for the number of directions.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/dirstat.html
    
    Args:
        dirs: the text file or image containing the directions.
        output: output selected metrics as a space-delimited list, suitable for
            use in scripts. This will produce one line of values per selected shell.
            Valid metrics are as specified in the description above.
        shells: specify one or more b-values to use during processing, as a
            comma-separated list of the desired approximate b-values (b-values are
            clustered to allow for small deviations). Note that some commands are
            incompatible with multiple b-values, and will report an error if more
            than one b-value is provided.
            WARNING: note that, even though the b=0 volumes are never
            referred to as shells in the literature, they still have to
            be explicitly included in the list of b-values as provided
            to the -shell option! Several algorithms which include the
            b=0 volumes in their computations may otherwise return an
            undesired result.
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
        NamedTuple of outputs (described in `DirstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIRSTAT_METADATA)
    cargs = []
    cargs.append("dirstat")
    if output is not None:
        cargs.extend(["-output", output])
    if shells is not None:
        cargs.extend(["-shells", *map(str, shells)])
    if grad is not None:
        cargs.extend(["-grad", execution.input_file(grad)])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
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
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(dirs))
    ret = DirstatOutputs(
        root=execution.output_file("."),
        fslgrad=fslgrad.outputs(execution),
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "Config",
    "ConfigOutputs",
    "DIRSTAT_METADATA",
    "DirstatOutputs",
    "Fslgrad",
    "FslgradOutputs",
    "dirstat",
]
