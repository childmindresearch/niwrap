# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIGNAL2IMAGE_METADATA = Metadata(
    id="c966356e7e749d29ae76a10e34270ee060241613.boutiques",
    name="signal2image",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Signal2imageParameters = typing.TypedDict('Signal2imageParameters', {
    "__STYX_TYPE__": typing.Literal["signal2image"],
    "pulse_sequence": InputPathType,
    "input_signal": typing.NotRequired[InputPathType | None],
    "output_image": typing.NotRequired[str | None],
    "kspace_coordinates": typing.NotRequired[InputPathType | None],
    "output_kspace": typing.NotRequired[str | None],
    "abs_flag": bool,
    "homodyne_flag": bool,
    "verbose_flag": bool,
    "apodize_flag": bool,
    "cutoff": typing.NotRequired[float | None],
    "rolloff": typing.NotRequired[float | None],
    "save_flag": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "signal2image": signal2image_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "signal2image": signal2image_outputs,
    }
    return vt.get(t)


class Signal2imageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `signal2image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """The resultant image file from the input signal and pulse sequence."""
    kspace_outfile: OutputPathType | None
    """The resultant k-space file."""


def signal2image_params(
    pulse_sequence: InputPathType,
    input_signal: InputPathType | None = None,
    output_image: str | None = None,
    kspace_coordinates: InputPathType | None = None,
    output_kspace: str | None = None,
    abs_flag: bool = False,
    homodyne_flag: bool = False,
    verbose_flag: bool = False,
    apodize_flag: bool = False,
    cutoff: float | None = 100,
    rolloff: float | None = 10,
    save_flag: bool = False,
) -> Signal2imageParameters:
    """
    Build parameters.
    
    Args:
        pulse_sequence: 8-column pulse_sequence matrix. Expects to find all\
            other pulse sequence files in the same directory.
        input_signal: Input signal file.
        output_image: Output image file.
        kspace_coordinates: K-space coordinates file.
        output_kspace: Output k-space file.
        abs_flag: Save absolute magnitude and phase.
        homodyne_flag: Do the homodyne reconstruction.
        verbose_flag: Switch on diagnostic messages.
        apodize_flag: Do apodization.
        cutoff: Apodization with this cutoff; default 100.
        rolloff: Apodization with this rolloff; default 10.
        save_flag: Save window as ASCII matrix (DEBUG!).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "signal2image",
        "pulse_sequence": pulse_sequence,
        "abs_flag": abs_flag,
        "homodyne_flag": homodyne_flag,
        "verbose_flag": verbose_flag,
        "apodize_flag": apodize_flag,
        "save_flag": save_flag,
    }
    if input_signal is not None:
        params["input_signal"] = input_signal
    if output_image is not None:
        params["output_image"] = output_image
    if kspace_coordinates is not None:
        params["kspace_coordinates"] = kspace_coordinates
    if output_kspace is not None:
        params["output_kspace"] = output_kspace
    if cutoff is not None:
        params["cutoff"] = cutoff
    if rolloff is not None:
        params["rolloff"] = rolloff
    return params


def signal2image_cargs(
    params: Signal2imageParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("signal2image")
    cargs.extend([
        "-p",
        execution.input_file(params.get("pulse_sequence"))
    ])
    if params.get("input_signal") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("input_signal"))
        ])
    if params.get("output_image") is not None:
        cargs.extend([
            "-o",
            params.get("output_image")
        ])
    if params.get("kspace_coordinates") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("kspace_coordinates"))
        ])
    if params.get("output_kspace") is not None:
        cargs.extend([
            "-k",
            params.get("output_kspace")
        ])
    if params.get("abs_flag"):
        cargs.append("-a")
    if params.get("homodyne_flag"):
        cargs.append("--homo")
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("apodize_flag"):
        cargs.append("-z")
    if params.get("cutoff") is not None:
        cargs.extend([
            "-l",
            str(params.get("cutoff"))
        ])
    if params.get("rolloff") is not None:
        cargs.extend([
            "-r",
            str(params.get("rolloff"))
        ])
    if params.get("save_flag"):
        cargs.append("-s")
    return cargs


def signal2image_outputs(
    params: Signal2imageParameters,
    execution: Execution,
) -> Signal2imageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Signal2imageOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("output_image")) if (params.get("output_image") is not None) else None,
        kspace_outfile=execution.output_file(params.get("output_kspace")) if (params.get("output_kspace") is not None) else None,
    )
    return ret


def signal2image_execute(
    params: Signal2imageParameters,
    execution: Execution,
) -> Signal2imageOutputs:
    """
    A tool for converting MR signal data to images using specified k-space
    coordinates and pulse sequences.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Signal2imageOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = signal2image_cargs(params, execution)
    ret = signal2image_outputs(params, execution)
    execution.run(cargs)
    return ret


def signal2image(
    pulse_sequence: InputPathType,
    input_signal: InputPathType | None = None,
    output_image: str | None = None,
    kspace_coordinates: InputPathType | None = None,
    output_kspace: str | None = None,
    abs_flag: bool = False,
    homodyne_flag: bool = False,
    verbose_flag: bool = False,
    apodize_flag: bool = False,
    cutoff: float | None = 100,
    rolloff: float | None = 10,
    save_flag: bool = False,
    runner: Runner | None = None,
) -> Signal2imageOutputs:
    """
    A tool for converting MR signal data to images using specified k-space
    coordinates and pulse sequences.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        pulse_sequence: 8-column pulse_sequence matrix. Expects to find all\
            other pulse sequence files in the same directory.
        input_signal: Input signal file.
        output_image: Output image file.
        kspace_coordinates: K-space coordinates file.
        output_kspace: Output k-space file.
        abs_flag: Save absolute magnitude and phase.
        homodyne_flag: Do the homodyne reconstruction.
        verbose_flag: Switch on diagnostic messages.
        apodize_flag: Do apodization.
        cutoff: Apodization with this cutoff; default 100.
        rolloff: Apodization with this rolloff; default 10.
        save_flag: Save window as ASCII matrix (DEBUG!).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Signal2imageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIGNAL2IMAGE_METADATA)
    params = signal2image_params(pulse_sequence=pulse_sequence, input_signal=input_signal, output_image=output_image, kspace_coordinates=kspace_coordinates, output_kspace=output_kspace, abs_flag=abs_flag, homodyne_flag=homodyne_flag, verbose_flag=verbose_flag, apodize_flag=apodize_flag, cutoff=cutoff, rolloff=rolloff, save_flag=save_flag)
    return signal2image_execute(params, execution)


__all__ = [
    "SIGNAL2IMAGE_METADATA",
    "Signal2imageOutputs",
    "Signal2imageParameters",
    "signal2image",
    "signal2image_params",
]
