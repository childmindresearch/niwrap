# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKGLOBAL_METADATA = Metadata(
    id="83ed2ed5059d206686d68bca5253e7191f588b5d.boutiques",
    name="tckglobal",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TckglobalRiso:
    """
    set one or more isotropic response functions. (multiple allowed).
    """
    response: InputPathType
    """set one or more isotropic response functions. (multiple allowed)"""
    
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
        cargs.append("-riso")
        cargs.append(execution.input_file(self.response))
        return cargs


@dataclasses.dataclass
class TckglobalConfig:
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


class TckglobalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckglobal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tracks: OutputPathType
    """the output file containing the tracks generated."""
    fod: OutputPathType | None
    """Predicted fibre orientation distribution function (fODF).
    This fODF is estimated as part of the global track optimization, and
    therefore incorporates the spatial regularization that it imposes.
    Internally, the fODF is represented as a discrete sum of apodized point
    spread functions (aPSF) oriented along the directions of all particles in
    the voxel, used to predict the DWI signal from the particle configuration.
    """
    fiso: OutputPathType | None
    """Predicted isotropic fractions of the tissues for which response functions
    were provided with -riso. Typically, these are CSF and GM. """
    eext: OutputPathType | None
    """Residual external energy in every voxel. """
    etrend: OutputPathType | None
    """internal and external energy trend and cooling statistics. """


def tckglobal(
    source: InputPathType,
    response: InputPathType,
    tracks: str,
    grad: InputPathType | None = None,
    mask: InputPathType | None = None,
    riso: list[TckglobalRiso] | None = None,
    lmax: int | None = None,
    length: float | None = None,
    weight: float | None = None,
    ppot: float | None = None,
    cpot: float | None = None,
    t0: float | None = None,
    t1: float | None = None,
    niter: int | None = None,
    fod: str | None = None,
    noapo: bool = False,
    fiso: str | None = None,
    eext: str | None = None,
    etrend: str | None = None,
    balance: float | None = None,
    density: float | None = None,
    prob: list[float] | None = None,
    beta: float | None = None,
    lambda_: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckglobalConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckglobalOutputs:
    """
    Multi-Shell Multi-Tissue Global Tractography.
    
    This command will reconstruct the global white matter fibre tractogram that
    best explains the input DWI data, using a multi-tissue spherical convolution
    model.
    
    Example use:
    
    $ tckglobal dwi.mif wmr.txt -riso csfr.txt -riso gmr.txt -mask mask.mif
    -niter 1e9 -fod fod.mif -fiso fiso.mif tracks.tck
    
    in which dwi.mif is the input image, wmr.txt is an anisotropic, multi-shell
    response function for WM, and csfr.txt and gmr.txt are isotropic response
    functions for CSF and GM. The output tractogram is saved to tracks.tck.
    Optional output images fod.mif and fiso.mif contain the predicted WM fODF
    and isotropic tissue fractions of CSF and GM respectively, estimated as part
    of the global optimization and thus affected by spatial regularization.
    
    References:
    
    Christiaens, D.; Reisert, M.; Dhollander, T.; Sunaert, S.; Suetens, P. &
    Maes, F. Global tractography of multi-shell diffusion-weighted imaging data
    using a multi-tissue model. NeuroImage, 2015, 123, 89-101.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        source: the image containing the raw DWI data.
        response: the response of a track segment on the DWI signal.
        tracks: the output file containing the tracks generated.
        grad: specify the diffusion encoding scheme (required if not supplied\
            in the header).
        mask: only reconstruct the tractogram within the specified brain mask\
            image.
        riso: set one or more isotropic response functions. (multiple allowed).
        lmax: set the maximum harmonic order for the output series. (default =\
            8).
        length: set the length of the particles (fibre segments). (default =\
            1mm).
        weight: set the weight by which particles contribute to the model.\
            (default = 0.1).
        ppot: set the particle potential, i.e., the cost of adding one segment,\
            relative to the particle weight. (default = 0.05).
        cpot: set the connection potential, i.e., the energy term that drives\
            two segments together. (default = 0.5).
        t0: set the initial temperature of the metropolis hastings optimizer.\
            (default = 0.1).
        t1: set the final temperature of the metropolis hastings optimizer.\
            (default = 0.001).
        niter: set the number of iterations of the metropolis hastings\
            optimizer. (default = 10M).
        fod: Predicted fibre orientation distribution function (fODF).\
            This fODF is estimated as part of the global track optimization,\
            and therefore incorporates the spatial regularization that it\
            imposes. Internally, the fODF is represented as a discrete sum of\
            apodized point spread functions (aPSF) oriented along the\
            directions of all particles in the voxel, used to predict the DWI\
            signal from the particle configuration.
        noapo: disable spherical convolution of fODF with apodized PSF, to\
            output a sum of delta functions rather than a sum of aPSFs.
        fiso: Predicted isotropic fractions of the tissues for which response\
            functions were provided with -riso. Typically, these are CSF and GM.
        eext: Residual external energy in every voxel.
        etrend: internal and external energy trend and cooling statistics.
        balance: balance internal and external energy. (default = 0)\
            Negative values give more weight to the internal energy, positive\
            to the external energy.
        density: set the desired density of the free Poisson process. (default\
            = 1).
        prob: set the probabilities of generating birth, death, randshift,\
            optshift and connect proposals respectively. (default =\
            0.25,0.05,0.25,0.1,0.35).
        beta: set the width of the Hanning interpolation window. (in [0, 1],\
            default = 0)\
            If used, a mask is required, and this mask must keep at least one\
            voxel distance to the image bounding box.
        lambda_: set the weight of the internal energy directly. (default = 1)\
            If provided, any value of -balance will be ignored.
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
        NamedTuple of outputs (described in `TckglobalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKGLOBAL_METADATA)
    cargs = []
    cargs.append("tckglobal")
    if grad is not None:
        cargs.extend([
            "-grad",
            execution.input_file(grad)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if riso is not None:
        cargs.extend([a for c in [s.run(execution) for s in riso] for a in c])
    if lmax is not None:
        cargs.extend([
            "-lmax",
            str(lmax)
        ])
    if length is not None:
        cargs.extend([
            "-length",
            str(length)
        ])
    if weight is not None:
        cargs.extend([
            "-weight",
            str(weight)
        ])
    if ppot is not None:
        cargs.extend([
            "-ppot",
            str(ppot)
        ])
    if cpot is not None:
        cargs.extend([
            "-cpot",
            str(cpot)
        ])
    if t0 is not None:
        cargs.extend([
            "-t0",
            str(t0)
        ])
    if t1 is not None:
        cargs.extend([
            "-t1",
            str(t1)
        ])
    if niter is not None:
        cargs.extend([
            "-niter",
            str(niter)
        ])
    if fod is not None:
        cargs.extend([
            "-fod",
            fod
        ])
    if noapo:
        cargs.append("-noapo")
    if fiso is not None:
        cargs.extend([
            "-fiso",
            fiso
        ])
    if eext is not None:
        cargs.extend([
            "-eext",
            eext
        ])
    if etrend is not None:
        cargs.extend([
            "-etrend",
            etrend
        ])
    if balance is not None:
        cargs.extend([
            "-balance",
            str(balance)
        ])
    if density is not None:
        cargs.extend([
            "-density",
            str(density)
        ])
    if prob is not None:
        cargs.extend([
            "-prob",
            *map(str, prob)
        ])
    if beta is not None:
        cargs.extend([
            "-beta",
            str(beta)
        ])
    if lambda_ is not None:
        cargs.extend([
            "-lambda",
            str(lambda_)
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
    cargs.append(execution.input_file(source))
    cargs.append(execution.input_file(response))
    cargs.append(tracks)
    ret = TckglobalOutputs(
        root=execution.output_file("."),
        tracks=execution.output_file(tracks),
        fod=execution.output_file(fod) if (fod is not None) else None,
        fiso=execution.output_file(fiso) if (fiso is not None) else None,
        eext=execution.output_file(eext) if (eext is not None) else None,
        etrend=execution.output_file(etrend) if (etrend is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKGLOBAL_METADATA",
    "TckglobalConfig",
    "TckglobalOutputs",
    "TckglobalRiso",
    "tckglobal",
]
