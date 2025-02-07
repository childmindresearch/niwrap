# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_MATRIX_MULTIPLY_METADATA = Metadata(
    id="e27af9270450150cf8e376927c002e9ad9bce68e.boutiques",
    name="mri_matrix_multiply",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriMatrixMultiplyParameters = typing.TypedDict('MriMatrixMultiplyParameters', {
    "__STYX_TYPE__": typing.Literal["mri_matrix_multiply"],
    "input_matrices": list[InputPathType],
    "inverted_input_matrices": typing.NotRequired[list[InputPathType] | None],
    "output_matrix": str,
    "verbose": bool,
    "fsl": bool,
    "binarize": bool,
    "subject_name": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_matrix_multiply": mri_matrix_multiply_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_matrix_multiply": mri_matrix_multiply_outputs,
    }.get(t)


class MriMatrixMultiplyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_matrix_multiply(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix_file: OutputPathType
    """Output matrix file resulting from the matrix multiplication."""


def mri_matrix_multiply_params(
    input_matrices: list[InputPathType],
    output_matrix: str,
    inverted_input_matrices: list[InputPathType] | None = None,
    verbose: bool = False,
    fsl: bool = False,
    binarize: bool = False,
    subject_name: str | None = None,
) -> MriMatrixMultiplyParameters:
    """
    Build parameters.
    
    Args:
        input_matrices: Input matrix files for multiplication.
        output_matrix: Output matrix file.
        inverted_input_matrices: Input matrix files to be inverted before\
            multiplication.
        verbose: Verbose output.
        fsl: Assume input/output are FSL-style matrix files.
        binarize: 'Binarize' the output matrix.
        subject_name: Subject name for output reg.dat files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_matrix_multiply",
        "input_matrices": input_matrices,
        "output_matrix": output_matrix,
        "verbose": verbose,
        "fsl": fsl,
        "binarize": binarize,
    }
    if inverted_input_matrices is not None:
        params["inverted_input_matrices"] = inverted_input_matrices
    if subject_name is not None:
        params["subject_name"] = subject_name
    return params


def mri_matrix_multiply_cargs(
    params: MriMatrixMultiplyParameters,
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
    cargs.append("mri_matrix_multiply")
    cargs.extend([
        "-im",
        *[execution.input_file(f) for f in params.get("input_matrices")]
    ])
    if params.get("inverted_input_matrices") is not None:
        cargs.extend([
            "-iim",
            *[execution.input_file(f) for f in params.get("inverted_input_matrices")]
        ])
    cargs.extend([
        "-om",
        params.get("output_matrix")
    ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("fsl"):
        cargs.append("-fsl")
    if params.get("binarize"):
        cargs.append("-bin")
    if params.get("subject_name") is not None:
        cargs.extend([
            "-s",
            params.get("subject_name")
        ])
    return cargs


def mri_matrix_multiply_outputs(
    params: MriMatrixMultiplyParameters,
    execution: Execution,
) -> MriMatrixMultiplyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMatrixMultiplyOutputs(
        root=execution.output_file("."),
        output_matrix_file=execution.output_file(params.get("output_matrix")),
    )
    return ret


def mri_matrix_multiply_execute(
    params: MriMatrixMultiplyParameters,
    execution: Execution,
) -> MriMatrixMultiplyOutputs:
    """
    Command-line tool for multiplying and manipulating MRI transformation matrices.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMatrixMultiplyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_matrix_multiply_cargs(params, execution)
    ret = mri_matrix_multiply_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_matrix_multiply(
    input_matrices: list[InputPathType],
    output_matrix: str,
    inverted_input_matrices: list[InputPathType] | None = None,
    verbose: bool = False,
    fsl: bool = False,
    binarize: bool = False,
    subject_name: str | None = None,
    runner: Runner | None = None,
) -> MriMatrixMultiplyOutputs:
    """
    Command-line tool for multiplying and manipulating MRI transformation matrices.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_matrices: Input matrix files for multiplication.
        output_matrix: Output matrix file.
        inverted_input_matrices: Input matrix files to be inverted before\
            multiplication.
        verbose: Verbose output.
        fsl: Assume input/output are FSL-style matrix files.
        binarize: 'Binarize' the output matrix.
        subject_name: Subject name for output reg.dat files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMatrixMultiplyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MATRIX_MULTIPLY_METADATA)
    params = mri_matrix_multiply_params(input_matrices=input_matrices, inverted_input_matrices=inverted_input_matrices, output_matrix=output_matrix, verbose=verbose, fsl=fsl, binarize=binarize, subject_name=subject_name)
    return mri_matrix_multiply_execute(params, execution)


__all__ = [
    "MRI_MATRIX_MULTIPLY_METADATA",
    "MriMatrixMultiplyOutputs",
    "MriMatrixMultiplyParameters",
    "mri_matrix_multiply",
    "mri_matrix_multiply_params",
]
