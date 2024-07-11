# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

DWI2FOD_METADATA = Metadata(
    id="117bc926fe935262045a3438c6b148ea44779ec3",
    name="dwi2fod",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Dwi2fodFslgrad:
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


@dataclasses.dataclass
class Dwi2fodConfig:
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


class Dwi2fodOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwi2fod(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    predicted_signal: OutputPathType | None
    """output the predicted dwi image. """


def dwi2fod(
    algorithm: typing.Literal["algorithm"],
    dwi: InputPathType,
    response_odf: list[str],
    grad: InputPathType | None = None,
    fslgrad: Dwi2fodFslgrad | None = None,
    shells: list[float | int] = None,
    directions: InputPathType | None = None,
    lmax: list[int] = None,
    mask: InputPathType | None = None,
    filter_: InputPathType | None = None,
    neg_lambda: float | int | None = None,
    norm_lambda: float | int | None = None,
    threshold: float | int | None = None,
    niter: int | None = None,
    norm_lambda_: float | int | None = None,
    neg_lambda_: float | int | None = None,
    predicted_signal: str | None = None,
    strides: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2fodConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Dwi2fodOutputs:
    """
    dwi2fod by J-Donald Tournier (jdtournier@gmail.com) and Ben Jeurissen
    (ben.jeurissen@uantwerpen.be).
    
    Estimate fibre orientation distributions from diffusion data using spherical
    deconvolution.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    * If using csd algorithm:
    Tournier, J.-D.; Calamante, F. & Connelly, A. Robust determination of the
    fibre orientation distribution in diffusion MRI: Non-negativity constrained
    super-resolved spherical deconvolution. NeuroImage, 2007, 35, 1459-1472
    
    * If using msmt_csd algorithm:
    Jeurissen, B; Tournier, J-D; Dhollander, T; Connelly, A & Sijbers, J.
    Multi-tissue constrained spherical deconvolution for improved analysis of
    multi-shell diffusion MRI data. NeuroImage, 2014, 103, 411-426
    
    Tournier, J.-D.; Calamante, F., Gadian, D.G. & Connelly, A. Direct
    estimation of the fiber orientation density function from diffusion-weighted
    MRI data using spherical deconvolution. NeuroImage, 2004, 23, 1176-1185.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/dwi2fod.html
    
    Args:
        algorithm: the algorithm to use for FOD estimation. (options are:\
            csd,msmt_csd).
        dwi: the input diffusion-weighted image.
        response_odf: pairs of input tissue response and output ODF images.
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
        directions: specify the directions over which to apply the\
            non-negativity constraint (by default, the built-in 300 direction set\
            is used). These should be supplied as a text file containing [ az el ]\
            pairs for the directions.
        lmax: the maximum spherical harmonic order for the output FOD(s).For\
            algorithms with multiple outputs, this should be provided as a\
            comma-separated list of integers, one for each output image; for\
            single-output algorithms, only a single integer should be provided. If\
            omitted, the command will use the lmax of the corresponding response\
            function (i.e based on its number of coefficients), up to a maximum of\
            8.
        mask: only perform computation within the specified binary brain mask\
            image.
        filter_: the linear frequency filtering parameters used for the initial\
            linear spherical deconvolution step (default = [ 1 1 1 0 0 ]). These\
            should be supplied as a text file containing the filtering coefficients\
            for each even harmonic order.
        neg_lambda: the regularisation parameter lambda that controls the\
            strength of the non-negativity constraint (default = 1).
        norm_lambda: the regularisation parameter lambda that controls the\
            strength of the constraint on the norm of the solution (default = 1).
        threshold: the threshold below which the amplitude of the FOD is\
            assumed to be zero, expressed as an absolute amplitude (default = 0).
        niter: the maximum number of iterations to perform for each voxel\
            (default = 50). Use '-niter 0' for a linear unconstrained spherical\
            deconvolution.
        norm_lambda_: the regularisation parameter lambda that controls the\
            strength of the constraint on the norm of the solution (default =\
            1e-10).
        neg_lambda_: the regularisation parameter lambda that controls the\
            strength of the non-negativity constraint (default = 1e-10).
        predicted_signal: output the predicted dwi image.
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
        NamedTuple of outputs (described in `Dwi2fodOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWI2FOD_METADATA)
    cargs = []
    cargs.append("dwi2fod")
    if grad is not None:
        cargs.extend(["-grad", execution.input_file(grad)])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
    if shells is not None:
        cargs.extend(["-shells", ",".join(map(str, shells))])
    if directions is not None:
        cargs.extend(["-directions", execution.input_file(directions)])
    if lmax is not None:
        cargs.extend(["-lmax", ",".join(map(str, lmax))])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if filter_ is not None:
        cargs.extend(["-filter", execution.input_file(filter_)])
    if neg_lambda is not None:
        cargs.extend(["-neg_lambda", str(neg_lambda)])
    if norm_lambda is not None:
        cargs.extend(["-norm_lambda", str(norm_lambda)])
    if threshold is not None:
        cargs.extend(["-threshold", str(threshold)])
    if niter is not None:
        cargs.extend(["-niter", str(niter)])
    if norm_lambda_ is not None:
        cargs.extend(["-norm_lambda", str(norm_lambda_)])
    if neg_lambda_ is not None:
        cargs.extend(["-neg_lambda", str(neg_lambda_)])
    if predicted_signal is not None:
        cargs.extend(["-predicted_signal", predicted_signal])
    if strides is not None:
        cargs.extend(["-strides", strides])
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
    cargs.append(algorithm)
    cargs.append(execution.input_file(dwi))
    cargs.extend(response_odf)
    ret = Dwi2fodOutputs(
        root=execution.output_file("."),
        predicted_signal=execution.output_file(f"{predicted_signal}") if predicted_signal is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DWI2FOD_METADATA",
    "Dwi2fodConfig",
    "Dwi2fodFslgrad",
    "Dwi2fodOutputs",
    "dwi2fod",
]
