# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1D_DW_GRAD_O_MAT___METADATA = Metadata(
    id="46eee009ed5251cf0654dc7e2305bcbaecf3782b.boutiques",
    name="1dDW_Grad_o_Mat++",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dDwGradOMatParameters = typing.TypedDict('V1dDwGradOMatParameters', {
    "__STYX_TYPE__": typing.Literal["1dDW_Grad_o_Mat++"],
    "in_row_vec": InputPathType,
    "in_col_vec": InputPathType,
    "in_col_matA": InputPathType,
    "in_col_matT": InputPathType,
    "flip_x": bool,
    "flip_y": bool,
    "flip_z": bool,
    "no_flip": bool,
    "out_row_vec": str,
    "out_col_vec": str,
    "out_col_matA": str,
    "out_col_matT": str,
    "in_bvals": typing.NotRequired[InputPathType | None],
    "out_col_bval": bool,
    "out_row_bval_sep": typing.NotRequired[str | None],
    "out_col_bval_sep": typing.NotRequired[str | None],
    "unit_mag_out": bool,
    "check_abs_min": typing.NotRequired[float | None],
    "bref_mean_top": bool,
    "put_zeros_top": bool,
    "bmax_ref": typing.NotRequired[float | None],
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
        "1dDW_Grad_o_Mat++": v_1d_dw_grad_o_mat___cargs,
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
        "1dDW_Grad_o_Mat++": v_1d_dw_grad_o_mat___outputs,
    }.get(t)


class V1dDwGradOMatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_dw_grad_o_mat__(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file of gradients or matrices"""
    out_row_bval_file: OutputPathType | None
    """Output b-values file in a single row"""
    out_col_bval_file: OutputPathType | None
    """Output b-values file in a single column"""


def v_1d_dw_grad_o_mat___params(
    in_row_vec: InputPathType,
    in_col_vec: InputPathType,
    in_col_mat_a: InputPathType,
    in_col_mat_t: InputPathType,
    out_row_vec: str,
    out_col_vec: str,
    out_col_mat_a: str,
    out_col_mat_t: str,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    no_flip: bool = False,
    in_bvals: InputPathType | None = None,
    out_col_bval: bool = False,
    out_row_bval_sep: str | None = None,
    out_col_bval_sep: str | None = None,
    unit_mag_out: bool = False,
    check_abs_min: float | None = None,
    bref_mean_top: bool = False,
    put_zeros_top: bool = False,
    bmax_ref: float | None = None,
) -> V1dDwGradOMatParameters:
    """
    Build parameters.
    
    Args:
        in_row_vec: Input file of 3 rows of gradients (e.g., dcm2nii-format\
            output).
        in_col_vec: Input file of 3 columns of gradients.
        in_col_mat_a: Input file of 6 columns of b- or g-matrix in 'A(FNI)'\
            diagonal first format.
        in_col_mat_t: Input file of 6 columns of b- or g-matrix in 'T(ORTOISE)'\
            row first format.
        out_row_vec: Output file of 3 rows of gradients.
        out_col_vec: Output file of 3 columns of gradients.
        out_col_mat_a: Output file of 6 columns of b- or g-matrix in 'A(FNI)'\
            diagonal first format.
        out_col_mat_t: Output file of 6 columns of b- or g-matrix in\
            'T(ORTOISE)' row first format.
        flip_x: Change sign of first column of gradients (or of the x-component\
            parts of the matrix).
        flip_y: Change sign of second column of gradients (or of the\
            y-component parts of the matrix).
        flip_z: Change sign of third column of gradients (or of the z-component\
            parts of the matrix).
        no_flip: Don't change any gradient/matrix signs (default behavior).
        in_bvals: BVAL_FILE is a file of b-values either in a single row or a\
            single column.
        out_col_bval: Switch to put a column of the bvalues as the first column\
            in the output data.
        out_row_bval_sep: Output a file of bvalues in a single row.
        out_col_bval_sep: Output a file of bvalues in a single column.
        unit_mag_out: Switch to scale each vector/matrix from the INFILE to\
            either unit or zero magnitude.
        check_abs_min: Specify the threshold to replace small negative diagonal\
            elements with zero in the input matrix.
        bref_mean_top: When averaging the reference 'b0' values, represent the\
            mean of X values in the top row.
        put_zeros_top: Add a row at the top with all zeros in the output format.
        bmax_ref: THRESH is a scalar number below which b-values are considered\
            zero or reference.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dDW_Grad_o_Mat++",
        "in_row_vec": in_row_vec,
        "in_col_vec": in_col_vec,
        "in_col_matA": in_col_mat_a,
        "in_col_matT": in_col_mat_t,
        "flip_x": flip_x,
        "flip_y": flip_y,
        "flip_z": flip_z,
        "no_flip": no_flip,
        "out_row_vec": out_row_vec,
        "out_col_vec": out_col_vec,
        "out_col_matA": out_col_mat_a,
        "out_col_matT": out_col_mat_t,
        "out_col_bval": out_col_bval,
        "unit_mag_out": unit_mag_out,
        "bref_mean_top": bref_mean_top,
        "put_zeros_top": put_zeros_top,
    }
    if in_bvals is not None:
        params["in_bvals"] = in_bvals
    if out_row_bval_sep is not None:
        params["out_row_bval_sep"] = out_row_bval_sep
    if out_col_bval_sep is not None:
        params["out_col_bval_sep"] = out_col_bval_sep
    if check_abs_min is not None:
        params["check_abs_min"] = check_abs_min
    if bmax_ref is not None:
        params["bmax_ref"] = bmax_ref
    return params


def v_1d_dw_grad_o_mat___cargs(
    params: V1dDwGradOMatParameters,
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
    cargs.append("1dDW_Grad_o_Mat++")
    cargs.extend([
        "-in_row_vec",
        execution.input_file(params.get("in_row_vec"))
    ])
    cargs.extend([
        "-in_col_vec",
        execution.input_file(params.get("in_col_vec"))
    ])
    cargs.extend([
        "-in_col_matA",
        execution.input_file(params.get("in_col_matA"))
    ])
    cargs.extend([
        "-in_col_matT",
        execution.input_file(params.get("in_col_matT"))
    ])
    if params.get("flip_x"):
        cargs.append("-flip_x")
    if params.get("flip_y"):
        cargs.append("-flip_y")
    if params.get("flip_z"):
        cargs.append("-flip_z")
    if params.get("no_flip"):
        cargs.append("-no_flip")
    cargs.extend([
        "-out_row_vec",
        params.get("out_row_vec")
    ])
    cargs.extend([
        "-out_col_vec",
        params.get("out_col_vec")
    ])
    cargs.extend([
        "-out_col_matA",
        params.get("out_col_matA")
    ])
    cargs.extend([
        "-out_col_matT",
        params.get("out_col_matT")
    ])
    if params.get("in_bvals") is not None:
        cargs.extend([
            "-in_bvals",
            execution.input_file(params.get("in_bvals"))
        ])
    if params.get("out_col_bval"):
        cargs.append("-out_col_bval")
    if params.get("out_row_bval_sep") is not None:
        cargs.extend([
            "-out_row_bval_sep",
            params.get("out_row_bval_sep")
        ])
    if params.get("out_col_bval_sep") is not None:
        cargs.extend([
            "-out_col_bval_sep",
            params.get("out_col_bval_sep")
        ])
    if params.get("unit_mag_out"):
        cargs.append("-unit_mag_out")
    if params.get("check_abs_min") is not None:
        cargs.extend([
            "-check_abs_min",
            str(params.get("check_abs_min"))
        ])
    if params.get("bref_mean_top"):
        cargs.append("-bref_mean_top")
    if params.get("put_zeros_top"):
        cargs.append("-put_zeros_top")
    if params.get("bmax_ref") is not None:
        cargs.extend([
            "-bmax_ref",
            str(params.get("bmax_ref"))
        ])
    return cargs


def v_1d_dw_grad_o_mat___outputs(
    params: V1dDwGradOMatParameters,
    execution: Execution,
) -> V1dDwGradOMatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dDwGradOMatOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("out_row_vec")),
        out_row_bval_file=execution.output_file(params.get("out_row_bval_sep")) if (params.get("out_row_bval_sep") is not None) else None,
        out_col_bval_file=execution.output_file(params.get("out_row_bval_sep")) if (params.get("out_row_bval_sep") is not None) else None,
    )
    return ret


def v_1d_dw_grad_o_mat___execute(
    params: V1dDwGradOMatParameters,
    execution: Execution,
) -> V1dDwGradOMatOutputs:
    """
    Manipulation of diffusion-weighted (DW) gradient vector files, b-value files,
    and b- or g-matrices with various input and output configurations.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dDwGradOMatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_1d_dw_grad_o_mat___cargs(params, execution)
    ret = v_1d_dw_grad_o_mat___outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_dw_grad_o_mat__(
    in_row_vec: InputPathType,
    in_col_vec: InputPathType,
    in_col_mat_a: InputPathType,
    in_col_mat_t: InputPathType,
    out_row_vec: str,
    out_col_vec: str,
    out_col_mat_a: str,
    out_col_mat_t: str,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    no_flip: bool = False,
    in_bvals: InputPathType | None = None,
    out_col_bval: bool = False,
    out_row_bval_sep: str | None = None,
    out_col_bval_sep: str | None = None,
    unit_mag_out: bool = False,
    check_abs_min: float | None = None,
    bref_mean_top: bool = False,
    put_zeros_top: bool = False,
    bmax_ref: float | None = None,
    runner: Runner | None = None,
) -> V1dDwGradOMatOutputs:
    """
    Manipulation of diffusion-weighted (DW) gradient vector files, b-value files,
    and b- or g-matrices with various input and output configurations.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_row_vec: Input file of 3 rows of gradients (e.g., dcm2nii-format\
            output).
        in_col_vec: Input file of 3 columns of gradients.
        in_col_mat_a: Input file of 6 columns of b- or g-matrix in 'A(FNI)'\
            diagonal first format.
        in_col_mat_t: Input file of 6 columns of b- or g-matrix in 'T(ORTOISE)'\
            row first format.
        out_row_vec: Output file of 3 rows of gradients.
        out_col_vec: Output file of 3 columns of gradients.
        out_col_mat_a: Output file of 6 columns of b- or g-matrix in 'A(FNI)'\
            diagonal first format.
        out_col_mat_t: Output file of 6 columns of b- or g-matrix in\
            'T(ORTOISE)' row first format.
        flip_x: Change sign of first column of gradients (or of the x-component\
            parts of the matrix).
        flip_y: Change sign of second column of gradients (or of the\
            y-component parts of the matrix).
        flip_z: Change sign of third column of gradients (or of the z-component\
            parts of the matrix).
        no_flip: Don't change any gradient/matrix signs (default behavior).
        in_bvals: BVAL_FILE is a file of b-values either in a single row or a\
            single column.
        out_col_bval: Switch to put a column of the bvalues as the first column\
            in the output data.
        out_row_bval_sep: Output a file of bvalues in a single row.
        out_col_bval_sep: Output a file of bvalues in a single column.
        unit_mag_out: Switch to scale each vector/matrix from the INFILE to\
            either unit or zero magnitude.
        check_abs_min: Specify the threshold to replace small negative diagonal\
            elements with zero in the input matrix.
        bref_mean_top: When averaging the reference 'b0' values, represent the\
            mean of X values in the top row.
        put_zeros_top: Add a row at the top with all zeros in the output format.
        bmax_ref: THRESH is a scalar number below which b-values are considered\
            zero or reference.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dDwGradOMatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_DW_GRAD_O_MAT___METADATA)
    params = v_1d_dw_grad_o_mat___params(in_row_vec=in_row_vec, in_col_vec=in_col_vec, in_col_mat_a=in_col_mat_a, in_col_mat_t=in_col_mat_t, flip_x=flip_x, flip_y=flip_y, flip_z=flip_z, no_flip=no_flip, out_row_vec=out_row_vec, out_col_vec=out_col_vec, out_col_mat_a=out_col_mat_a, out_col_mat_t=out_col_mat_t, in_bvals=in_bvals, out_col_bval=out_col_bval, out_row_bval_sep=out_row_bval_sep, out_col_bval_sep=out_col_bval_sep, unit_mag_out=unit_mag_out, check_abs_min=check_abs_min, bref_mean_top=bref_mean_top, put_zeros_top=put_zeros_top, bmax_ref=bmax_ref)
    return v_1d_dw_grad_o_mat___execute(params, execution)


__all__ = [
    "V1dDwGradOMatOutputs",
    "V1dDwGradOMatParameters",
    "V_1D_DW_GRAD_O_MAT___METADATA",
    "v_1d_dw_grad_o_mat__",
    "v_1d_dw_grad_o_mat___params",
]
