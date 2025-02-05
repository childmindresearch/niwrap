# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RSFGEN_METADATA = Metadata(
    id="42de4c95300ddfa6a27f2ddbc5b6d9dc63cdd292.boutiques",
    name="RSFgen",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
RsfgenParameters = typing.TypedDict('RsfgenParameters', {
    "__STYX_TYPE__": typing.Literal["RSFgen"],
    "length": int,
    "num_experimental_conditions": int,
    "block_length": typing.NotRequired[str | None],
    "random_seed": typing.NotRequired[float | None],
    "suppress_output_flag": bool,
    "single_file_flag": bool,
    "single_column_flag": bool,
    "output_prefix": typing.NotRequired[str | None],
    "num_reps": typing.NotRequired[str | None],
    "permutation_seed": typing.NotRequired[float | None],
    "markov_file": typing.NotRequired[InputPathType | None],
    "prob_zero": typing.NotRequired[float | None],
    "input_table": typing.NotRequired[InputPathType | None],
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
        "RSFgen": rsfgen_cargs,
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
        "RSFgen": rsfgen_outputs,
    }
    return vt.get(t)


class RsfgenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rsfgen(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """Output .1D stimulus function files prefixed with the provided output
    prefix."""


def rsfgen_params(
    length: int,
    num_experimental_conditions: int,
    block_length: str | None = None,
    random_seed: float | None = None,
    suppress_output_flag: bool = False,
    single_file_flag: bool = False,
    single_column_flag: bool = False,
    output_prefix: str | None = None,
    num_reps: str | None = None,
    permutation_seed: float | None = None,
    markov_file: InputPathType | None = None,
    prob_zero: float | None = None,
    input_table: InputPathType | None = None,
) -> RsfgenParameters:
    """
    Build parameters.
    
    Args:
        length: Length of time series.
        num_experimental_conditions: Number of input stimuli (experimental\
            conditions).
        block_length: Block length for stimulus. Must specify stimulus index\
            and length. Example: -nblock 1 5.
        random_seed: Random number seed.
        suppress_output_flag: Flag to suppress screen output.
        single_file_flag: Place stimulus functions into a single .1D file.
        single_column_flag: Write stimulus functions as a single column of\
            decimal integers.
        output_prefix: Prefix for output .1D stimulus functions.
        num_reps: Number of repetitions for stimulus.
        permutation_seed: Stim label permutation random number seed.
        markov_file: File containing the transition probability matrix.
        prob_zero: Probability of a zero (i.e., null) state (default: 0).
        input_table: Filename of column or table of numbers. All other input\
            options (except -seed and -prefix) are ignored with this option.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "RSFgen",
        "length": length,
        "num_experimental_conditions": num_experimental_conditions,
        "suppress_output_flag": suppress_output_flag,
        "single_file_flag": single_file_flag,
        "single_column_flag": single_column_flag,
    }
    if block_length is not None:
        params["block_length"] = block_length
    if random_seed is not None:
        params["random_seed"] = random_seed
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if num_reps is not None:
        params["num_reps"] = num_reps
    if permutation_seed is not None:
        params["permutation_seed"] = permutation_seed
    if markov_file is not None:
        params["markov_file"] = markov_file
    if prob_zero is not None:
        params["prob_zero"] = prob_zero
    if input_table is not None:
        params["input_table"] = input_table
    return params


def rsfgen_cargs(
    params: RsfgenParameters,
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
    cargs.append("RSFgen")
    cargs.extend([
        "-nt",
        str(params.get("length"))
    ])
    cargs.extend([
        "-num_stimts",
        str(params.get("num_experimental_conditions"))
    ])
    if params.get("block_length") is not None:
        cargs.extend([
            "-nblock",
            params.get("block_length")
        ])
    if params.get("random_seed") is not None:
        cargs.extend([
            "-seed",
            str(params.get("random_seed"))
        ])
    if params.get("suppress_output_flag"):
        cargs.append("-quiet")
    if params.get("single_file_flag"):
        cargs.append("-one_file")
    if params.get("single_column_flag"):
        cargs.append("-one_col")
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("num_reps") is not None:
        cargs.extend([
            "-nreps",
            params.get("num_reps")
        ])
    if params.get("permutation_seed") is not None:
        cargs.extend([
            "-pseed",
            str(params.get("permutation_seed"))
        ])
    if params.get("markov_file") is not None:
        cargs.extend([
            "-markov",
            execution.input_file(params.get("markov_file"))
        ])
    if params.get("prob_zero") is not None:
        cargs.extend([
            "-pzero",
            str(params.get("prob_zero"))
        ])
    if params.get("input_table") is not None:
        cargs.extend([
            "-table",
            execution.input_file(params.get("input_table"))
        ])
    return cargs


def rsfgen_outputs(
    params: RsfgenParameters,
    execution: Execution,
) -> RsfgenOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RsfgenOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(params.get("output_prefix") + "1.1D") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def rsfgen_execute(
    params: RsfgenParameters,
    execution: Execution,
) -> RsfgenOutputs:
    """
    Program to generate random stimulus functions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RsfgenOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = rsfgen_cargs(params, execution)
    ret = rsfgen_outputs(params, execution)
    execution.run(cargs)
    return ret


def rsfgen(
    length: int,
    num_experimental_conditions: int,
    block_length: str | None = None,
    random_seed: float | None = None,
    suppress_output_flag: bool = False,
    single_file_flag: bool = False,
    single_column_flag: bool = False,
    output_prefix: str | None = None,
    num_reps: str | None = None,
    permutation_seed: float | None = None,
    markov_file: InputPathType | None = None,
    prob_zero: float | None = None,
    input_table: InputPathType | None = None,
    runner: Runner | None = None,
) -> RsfgenOutputs:
    """
    Program to generate random stimulus functions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        length: Length of time series.
        num_experimental_conditions: Number of input stimuli (experimental\
            conditions).
        block_length: Block length for stimulus. Must specify stimulus index\
            and length. Example: -nblock 1 5.
        random_seed: Random number seed.
        suppress_output_flag: Flag to suppress screen output.
        single_file_flag: Place stimulus functions into a single .1D file.
        single_column_flag: Write stimulus functions as a single column of\
            decimal integers.
        output_prefix: Prefix for output .1D stimulus functions.
        num_reps: Number of repetitions for stimulus.
        permutation_seed: Stim label permutation random number seed.
        markov_file: File containing the transition probability matrix.
        prob_zero: Probability of a zero (i.e., null) state (default: 0).
        input_table: Filename of column or table of numbers. All other input\
            options (except -seed and -prefix) are ignored with this option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RsfgenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RSFGEN_METADATA)
    params = rsfgen_params(length=length, num_experimental_conditions=num_experimental_conditions, block_length=block_length, random_seed=random_seed, suppress_output_flag=suppress_output_flag, single_file_flag=single_file_flag, single_column_flag=single_column_flag, output_prefix=output_prefix, num_reps=num_reps, permutation_seed=permutation_seed, markov_file=markov_file, prob_zero=prob_zero, input_table=input_table)
    return rsfgen_execute(params, execution)


__all__ = [
    "RSFGEN_METADATA",
    "RsfgenOutputs",
    "RsfgenParameters",
    "rsfgen",
    "rsfgen_params",
]
