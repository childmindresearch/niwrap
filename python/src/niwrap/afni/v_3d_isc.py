# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ISC_METADATA = Metadata(
    id="d937806e40a345507430d710b195292450cd9998.boutiques",
    name="3dISC",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dIscParameters = typing.TypedDict('V3dIscParameters', {
    "__STYX_TYPE__": typing.Literal["3dISC"],
    "outfile_prefix": str,
    "num_jobs": typing.NotRequired[float | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "model_structure": str,
    "qvar_centers": typing.NotRequired[str | None],
    "quantitative_vars": typing.NotRequired[str | None],
    "fisher_transform": bool,
    "io_functions": typing.NotRequired[typing.Literal["AFNI", "R"] | None],
    "data_table": str,
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
        "3dISC": v_3d_isc_cargs,
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
        "3dISC": v_3d_isc_outputs,
    }.get(t)


class V3dIscOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_isc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    isc_output: OutputPathType
    """Main output ISC file"""
    tstat_output: OutputPathType
    """T-statistic of ISC"""


def v_3d_isc_params(
    outfile_prefix: str,
    model_structure: str,
    data_table: str,
    num_jobs: float | None = None,
    mask_file: InputPathType | None = None,
    qvar_centers: str | None = None,
    quantitative_vars: str | None = None,
    fisher_transform: bool = False,
    io_functions: typing.Literal["AFNI", "R"] | None = None,
) -> V3dIscParameters:
    """
    Build parameters.
    
    Args:
        outfile_prefix: Output file name. For AFNI format, provide prefix only,\
            with no view+suffix needed.
        model_structure: Specify the model structure for all the variables. The\
            expression FORMULA with more than one variable has to be surrounded\
            within quotes.
        data_table: List the data structure with a header as the first line.\
            Has to occur last in the script.
        num_jobs: Specify the number of jobs to run concurrently. Choose 1 for\
            a single-processor computer.
        mask_file: Process voxels inside this mask only. Default is no masking.
        qvar_centers: Specify centering values for quantitative variables\
            identified under -qVars. Multiple centers are separated by commas\
            without spaces and should be within quotes.
        quantitative_vars: Identify quantitative variables (or covariates). The\
            list should be comma-separated and within quotes.
        fisher_transform: Perform Fisher transformation on the response\
            variable (input files) if it is a correlation value.
        io_functions: Use AFNI's C io functions (default) or R's io functions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dISC",
        "outfile_prefix": outfile_prefix,
        "model_structure": model_structure,
        "fisher_transform": fisher_transform,
        "data_table": data_table,
    }
    if num_jobs is not None:
        params["num_jobs"] = num_jobs
    if mask_file is not None:
        params["mask_file"] = mask_file
    if qvar_centers is not None:
        params["qvar_centers"] = qvar_centers
    if quantitative_vars is not None:
        params["quantitative_vars"] = quantitative_vars
    if io_functions is not None:
        params["io_functions"] = io_functions
    return params


def v_3d_isc_cargs(
    params: V3dIscParameters,
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
    cargs.append("3dISC")
    cargs.extend([
        "-prefix",
        params.get("outfile_prefix")
    ])
    if params.get("num_jobs") is not None:
        cargs.extend([
            "-jobs",
            str(params.get("num_jobs"))
        ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_file"))
        ])
    cargs.extend([
        "-model",
        params.get("model_structure")
    ])
    if params.get("qvar_centers") is not None:
        cargs.extend([
            "-qVarCenters",
            params.get("qvar_centers")
        ])
    if params.get("quantitative_vars") is not None:
        cargs.extend([
            "-qVars",
            params.get("quantitative_vars")
        ])
    if params.get("fisher_transform"):
        cargs.append("-r2z")
    if params.get("io_functions") is not None:
        cargs.extend([
            "-cio",
            params.get("io_functions")
        ])
    cargs.extend([
        "-dataTable",
        params.get("data_table")
    ])
    return cargs


def v_3d_isc_outputs(
    params: V3dIscParameters,
    execution: Execution,
) -> V3dIscOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dIscOutputs(
        root=execution.output_file("."),
        isc_output=execution.output_file(params.get("outfile_prefix") + "_ISC.nii"),
        tstat_output=execution.output_file(params.get("outfile_prefix") + "_tstat.nii"),
    )
    return ret


def v_3d_isc_execute(
    params: V3dIscParameters,
    execution: Execution,
) -> V3dIscOutputs:
    """
    Program for Voxelwise Inter-Subject Correlation (ISC) Analysis using linear
    mixed-effects modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dIscOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_isc_cargs(params, execution)
    ret = v_3d_isc_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_isc(
    outfile_prefix: str,
    model_structure: str,
    data_table: str,
    num_jobs: float | None = None,
    mask_file: InputPathType | None = None,
    qvar_centers: str | None = None,
    quantitative_vars: str | None = None,
    fisher_transform: bool = False,
    io_functions: typing.Literal["AFNI", "R"] | None = None,
    runner: Runner | None = None,
) -> V3dIscOutputs:
    """
    Program for Voxelwise Inter-Subject Correlation (ISC) Analysis using linear
    mixed-effects modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        outfile_prefix: Output file name. For AFNI format, provide prefix only,\
            with no view+suffix needed.
        model_structure: Specify the model structure for all the variables. The\
            expression FORMULA with more than one variable has to be surrounded\
            within quotes.
        data_table: List the data structure with a header as the first line.\
            Has to occur last in the script.
        num_jobs: Specify the number of jobs to run concurrently. Choose 1 for\
            a single-processor computer.
        mask_file: Process voxels inside this mask only. Default is no masking.
        qvar_centers: Specify centering values for quantitative variables\
            identified under -qVars. Multiple centers are separated by commas\
            without spaces and should be within quotes.
        quantitative_vars: Identify quantitative variables (or covariates). The\
            list should be comma-separated and within quotes.
        fisher_transform: Perform Fisher transformation on the response\
            variable (input files) if it is a correlation value.
        io_functions: Use AFNI's C io functions (default) or R's io functions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dIscOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ISC_METADATA)
    params = v_3d_isc_params(outfile_prefix=outfile_prefix, num_jobs=num_jobs, mask_file=mask_file, model_structure=model_structure, qvar_centers=qvar_centers, quantitative_vars=quantitative_vars, fisher_transform=fisher_transform, io_functions=io_functions, data_table=data_table)
    return v_3d_isc_execute(params, execution)


__all__ = [
    "V3dIscOutputs",
    "V3dIscParameters",
    "V_3D_ISC_METADATA",
    "v_3d_isc",
    "v_3d_isc_params",
]
