# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


V_3D_BANDPASS_METADATA = Metadata(
    id="3fe63cdedb0a12b3606b55f4b73dcb3d07646ec9",
    name="3dBandpass",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dBandpassOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_bandpass(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output file from 3dbandpass."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_bandpass(
    highpass: float | int,
    in_file: InputPathType,
    lowpass: float | int,
    automask: bool = False,
    blur: float | int | None = None,
    despike: bool = False,
    local_pv: float | int | None = None,
    mask: InputPathType | None = None,
    nfft: int | None = None,
    no_detrend: bool = False,
    normalize: bool = False,
    notrans: bool = False,
    num_threads: int | None = 1,
    orthogonalize_dset: InputPathType | None = None,
    orthogonalize_file: list[InputPathType] = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    tr: float | int | None = None,
    runner: Runner = None,
) -> V3dBandpassOutputs:
    """
    3dBandpass by Nipype (interface).
    
    Program to lowpass and/or highpass each voxel time series in a dataset,
    offering more/different options than Fourier.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dBandpass.html
    
    Args:
        highpass: Highpass.
        in_file: Input file to 3dbandpass.
        lowpass: Lowpass.
        automask: Create a mask from the input dataset.
        blur: Blur (inside the mask only) with a filter width (fwhm) of 'fff'
            millimeters.
        despike: Despike each time series before other processing. hopefully,
            you don't actually need to do this, which is why it is optional.
        local_pv: Replace each vector by the local principal vector (aka first
            singular vector) from a neighborhood of radius 'rrr' millimeters. note
            that the pv time series is l2 normalized. this option is mostly for bob
            cox to have fun with.
        mask: Mask file.
        nfft: Set the fft length [must be a legal value].
        no_detrend: Skip the quadratic detrending of the input that occurs
            before the fft-based bandpassing. you would only want to do this if the
            dataset had been detrended already in some other program.
        normalize: Make all output time series have l2 norm = 1 (i.e., sum of
            squares = 1).
        notrans: Don't check for initial positive transients in the data. the
            test is a little slow, so skipping it is ok, if you know the data time
            series are transient-free.
        num_threads: Set number of threads.
        orthogonalize_dset: Orthogonalize each voxel to the corresponding voxel
            time series in dataset 'fset', which must have the same spatial and
            temporal grid structure as the main input dataset. at present, only one
            '-dsort' option is allowed.
        orthogonalize_file: Also orthogonalize input to columns in f.1d.
            multiple '-ort' options are allowed.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        tr: Set time step (tr) in sec [default=from dataset header].
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dBandpassOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BANDPASS_METADATA)
    cargs = []
    cargs.append("3dBandpass")
    cargs.append(str(highpass))
    cargs.append(str(lowpass))
    cargs.append("[OUT_FILE]")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    cargs.append(execution.input_file(in_file))
    if automask:
        cargs.append("-automask")
    if blur is not None:
        cargs.extend(["-blur", str(blur)])
    if despike:
        cargs.append("-despike")
    if local_pv is not None:
        cargs.extend(["-localPV", str(local_pv)])
    if nfft is not None:
        cargs.extend(["-nfft", str(nfft)])
    if no_detrend:
        cargs.append("-nodetrend")
    if normalize:
        cargs.append("-norm")
    if notrans:
        cargs.append("-notrans")
    if num_threads is not None:
        cargs.append(str(num_threads))
    if orthogonalize_dset is not None:
        cargs.extend(["-dsort", execution.input_file(orthogonalize_dset)])
    if orthogonalize_file is not None:
        cargs.extend(["-ort", *[execution.input_file(f) for f in orthogonalize_file]])
    if outputtype is not None:
        cargs.append(outputtype)
    if tr is not None:
        cargs.extend(["-dt", str(tr)])
    ret = V3dBandpassOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).stem}_bp", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret
