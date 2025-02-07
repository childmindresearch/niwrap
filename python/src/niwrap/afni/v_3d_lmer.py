# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_LMER_METADATA = Metadata(
    id="02e68dcb59ede0c18ce18893dd5aa84a50513efe.boutiques",
    name="3dLMEr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dLmerParameters = typing.TypedDict('V3dLmerParameters', {
    "__STYX_TYPE__": typing.Literal["3dLMEr"],
    "bound_lower": typing.NotRequired[float | None],
    "bound_upper": typing.NotRequired[float | None],
    "cio": bool,
    "data_table": InputPathType,
    "debug_args": bool,
    "glf_code": typing.NotRequired[str | None],
    "glt_code": typing.NotRequired[str | None],
    "help": bool,
    "input_file_column": typing.NotRequired[str | None],
    "jobs": typing.NotRequired[float | None],
    "mask": typing.NotRequired[InputPathType | None],
    "model": str,
    "prefix": str,
    "qvar_centers": typing.NotRequired[str | None],
    "qvars": typing.NotRequired[str | None],
    "resid": typing.NotRequired[str | None],
    "rio": bool,
    "show_options": bool,
    "ss_type": typing.NotRequired[float | None],
    "trr": bool,
    "vvar_centers": typing.NotRequired[str | None],
    "vvars": typing.NotRequired[str | None],
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
        "3dLMEr": v_3d_lmer_cargs,
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
        "3dLMEr": v_3d_lmer_outputs,
    }.get(t)


class V3dLmerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lmer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file"""
    residuals_file: OutputPathType | None
    """Output residuals file"""


def v_3d_lmer_params(
    data_table: InputPathType,
    model: str,
    prefix: str,
    bound_lower: float | None = None,
    bound_upper: float | None = None,
    cio: bool = False,
    debug_args: bool = False,
    glf_code: str | None = None,
    glt_code: str | None = None,
    help_: bool = False,
    input_file_column: str | None = None,
    jobs: float | None = None,
    mask: InputPathType | None = None,
    qvar_centers: str | None = None,
    qvars: str | None = None,
    resid: str | None = None,
    rio: bool = False,
    show_options: bool = False,
    ss_type: float | None = None,
    trr: bool = False,
    vvar_centers: str | None = None,
    vvars: str | None = None,
) -> V3dLmerParameters:
    """
    Build parameters.
    
    Args:
        data_table: List the data structure with a header as the first line.
        model: Specify the model structure for all the variables.
        prefix: Output file name.
        bound_lower: Specify the lower and upper bounds for outlier removal.
        bound_upper: Specify the lower and upper bounds for outlier removal.
        cio: Use AFNI's C io functions.
        debug_args: Enable R to save the parameters for debugging.
        glf_code: Specify a general linear F-style (GLF) formulation.
        glt_code: Specify the label and weights of interest in a general linear\
            t-style (GLT) formulation.
        help_: Display the help message.
        input_file_column: Specify the column name for input files of effect\
            estimate.
        jobs: Number of jobs for parallel computing.
        mask: Process voxels inside this mask only.
        qvar_centers: Specify centering values for quantitative variables.
        qvars: Identify quantitative variables (or covariates).
        resid: Output file name for the residuals.
        rio: Use R's io functions.
        show_options: List of allowed options.
        ss_type: Specify the type for sums of squares in the F-statistics.
        trr: Perform test-retest reliability analysis.
        vvar_centers: Specify centering values for voxel-wise covariates.
        vvars: Identify voxel-wise covariates.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dLMEr",
        "cio": cio,
        "data_table": data_table,
        "debug_args": debug_args,
        "help": help_,
        "model": model,
        "prefix": prefix,
        "rio": rio,
        "show_options": show_options,
        "trr": trr,
    }
    if bound_lower is not None:
        params["bound_lower"] = bound_lower
    if bound_upper is not None:
        params["bound_upper"] = bound_upper
    if glf_code is not None:
        params["glf_code"] = glf_code
    if glt_code is not None:
        params["glt_code"] = glt_code
    if input_file_column is not None:
        params["input_file_column"] = input_file_column
    if jobs is not None:
        params["jobs"] = jobs
    if mask is not None:
        params["mask"] = mask
    if qvar_centers is not None:
        params["qvar_centers"] = qvar_centers
    if qvars is not None:
        params["qvars"] = qvars
    if resid is not None:
        params["resid"] = resid
    if ss_type is not None:
        params["ss_type"] = ss_type
    if vvar_centers is not None:
        params["vvar_centers"] = vvar_centers
    if vvars is not None:
        params["vvars"] = vvars
    return params


def v_3d_lmer_cargs(
    params: V3dLmerParameters,
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
    cargs.append("3dLMEr")
    if params.get("bound_lower") is not None:
        cargs.append(str(params.get("bound_lower")))
    if params.get("bound_upper") is not None:
        cargs.append(str(params.get("bound_upper")))
    if params.get("cio"):
        cargs.append("-cio")
    cargs.extend([
        "-dataTable",
        execution.input_file(params.get("data_table"))
    ])
    if params.get("debug_args"):
        cargs.append("-dbgArgs")
    if params.get("glf_code") is not None:
        cargs.extend([
            "-glfCode",
            params.get("glf_code")
        ])
    if params.get("glt_code") is not None:
        cargs.extend([
            "-gltCode",
            params.get("glt_code")
        ])
    if params.get("help"):
        cargs.append("-help")
    if params.get("input_file_column") is not None:
        cargs.extend([
            "-IF",
            params.get("input_file_column")
        ])
    if params.get("jobs") is not None:
        cargs.extend([
            "-jobs",
            str(params.get("jobs"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    cargs.extend([
        "-model",
        params.get("model")
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("qvar_centers") is not None:
        cargs.extend([
            "-qVarCenters",
            params.get("qvar_centers")
        ])
    if params.get("qvars") is not None:
        cargs.extend([
            "-qVars",
            params.get("qvars")
        ])
    if params.get("resid") is not None:
        cargs.extend([
            "-resid",
            params.get("resid")
        ])
    if params.get("rio"):
        cargs.append("-Rio")
    if params.get("show_options"):
        cargs.append("-show_allowed_options")
    if params.get("ss_type") is not None:
        cargs.extend([
            "-SS_type",
            str(params.get("ss_type"))
        ])
    if params.get("trr"):
        cargs.append("-TRR")
    if params.get("vvar_centers") is not None:
        cargs.extend([
            "-vVarCenters",
            params.get("vvar_centers")
        ])
    if params.get("vvars") is not None:
        cargs.extend([
            "-vVars",
            params.get("vvars")
        ])
    return cargs


def v_3d_lmer_outputs(
    params: V3dLmerParameters,
    execution: Execution,
) -> V3dLmerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dLmerOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".nii.gz"),
        residuals_file=execution.output_file(params.get("resid") + ".nii.gz") if (params.get("resid") is not None) else None,
    )
    return ret


def v_3d_lmer_execute(
    params: V3dLmerParameters,
    execution: Execution,
) -> V3dLmerOutputs:
    """
    Program for Voxelwise Linear Mixed-Effects (LME) Analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dLmerOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_lmer_cargs(params, execution)
    ret = v_3d_lmer_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_lmer(
    data_table: InputPathType,
    model: str,
    prefix: str,
    bound_lower: float | None = None,
    bound_upper: float | None = None,
    cio: bool = False,
    debug_args: bool = False,
    glf_code: str | None = None,
    glt_code: str | None = None,
    help_: bool = False,
    input_file_column: str | None = None,
    jobs: float | None = None,
    mask: InputPathType | None = None,
    qvar_centers: str | None = None,
    qvars: str | None = None,
    resid: str | None = None,
    rio: bool = False,
    show_options: bool = False,
    ss_type: float | None = None,
    trr: bool = False,
    vvar_centers: str | None = None,
    vvars: str | None = None,
    runner: Runner | None = None,
) -> V3dLmerOutputs:
    """
    Program for Voxelwise Linear Mixed-Effects (LME) Analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        data_table: List the data structure with a header as the first line.
        model: Specify the model structure for all the variables.
        prefix: Output file name.
        bound_lower: Specify the lower and upper bounds for outlier removal.
        bound_upper: Specify the lower and upper bounds for outlier removal.
        cio: Use AFNI's C io functions.
        debug_args: Enable R to save the parameters for debugging.
        glf_code: Specify a general linear F-style (GLF) formulation.
        glt_code: Specify the label and weights of interest in a general linear\
            t-style (GLT) formulation.
        help_: Display the help message.
        input_file_column: Specify the column name for input files of effect\
            estimate.
        jobs: Number of jobs for parallel computing.
        mask: Process voxels inside this mask only.
        qvar_centers: Specify centering values for quantitative variables.
        qvars: Identify quantitative variables (or covariates).
        resid: Output file name for the residuals.
        rio: Use R's io functions.
        show_options: List of allowed options.
        ss_type: Specify the type for sums of squares in the F-statistics.
        trr: Perform test-retest reliability analysis.
        vvar_centers: Specify centering values for voxel-wise covariates.
        vvars: Identify voxel-wise covariates.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLmerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LMER_METADATA)
    params = v_3d_lmer_params(bound_lower=bound_lower, bound_upper=bound_upper, cio=cio, data_table=data_table, debug_args=debug_args, glf_code=glf_code, glt_code=glt_code, help_=help_, input_file_column=input_file_column, jobs=jobs, mask=mask, model=model, prefix=prefix, qvar_centers=qvar_centers, qvars=qvars, resid=resid, rio=rio, show_options=show_options, ss_type=ss_type, trr=trr, vvar_centers=vvar_centers, vvars=vvars)
    return v_3d_lmer_execute(params, execution)


__all__ = [
    "V3dLmerOutputs",
    "V3dLmerParameters",
    "V_3D_LMER_METADATA",
    "v_3d_lmer",
    "v_3d_lmer_params",
]
