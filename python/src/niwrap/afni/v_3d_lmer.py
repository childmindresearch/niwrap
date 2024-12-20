# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LMER_METADATA = Metadata(
    id="02e68dcb59ede0c18ce18893dd5aa84a50513efe.boutiques",
    name="3dLMEr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


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
    cargs = []
    cargs.append("3dLMEr")
    if bound_lower is not None:
        cargs.append(str(bound_lower))
    if bound_upper is not None:
        cargs.append(str(bound_upper))
    if cio:
        cargs.append("-cio")
    cargs.extend([
        "-dataTable",
        execution.input_file(data_table)
    ])
    if debug_args:
        cargs.append("-dbgArgs")
    if glf_code is not None:
        cargs.extend([
            "-glfCode",
            glf_code
        ])
    if glt_code is not None:
        cargs.extend([
            "-gltCode",
            glt_code
        ])
    if help_:
        cargs.append("-help")
    if input_file_column is not None:
        cargs.extend([
            "-IF",
            input_file_column
        ])
    if jobs is not None:
        cargs.extend([
            "-jobs",
            str(jobs)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    cargs.extend([
        "-model",
        model
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if qvar_centers is not None:
        cargs.extend([
            "-qVarCenters",
            qvar_centers
        ])
    if qvars is not None:
        cargs.extend([
            "-qVars",
            qvars
        ])
    if resid is not None:
        cargs.extend([
            "-resid",
            resid
        ])
    if rio:
        cargs.append("-Rio")
    if show_options:
        cargs.append("-show_allowed_options")
    if ss_type is not None:
        cargs.extend([
            "-SS_type",
            str(ss_type)
        ])
    if trr:
        cargs.append("-TRR")
    if vvar_centers is not None:
        cargs.extend([
            "-vVarCenters",
            vvar_centers
        ])
    if vvars is not None:
        cargs.extend([
            "-vVars",
            vvars
        ])
    ret = V3dLmerOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(prefix + ".nii.gz"),
        residuals_file=execution.output_file(resid + ".nii.gz") if (resid is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLmerOutputs",
    "V_3D_LMER_METADATA",
    "v_3d_lmer",
]
