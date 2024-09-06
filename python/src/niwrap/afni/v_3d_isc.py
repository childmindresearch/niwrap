# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ISC___VOXELWISE_INTER_SUBJECT_CORRELATION_ANALYSIS_METADATA = Metadata(
    id="5448278573a62576b1e10cadc9938751ba7be38f",
    name="3dISC - Voxelwise Inter-Subject Correlation Analysis",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dIscVoxelwiseInterSubjectCorrelationAnalysisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_isc___voxelwise_inter_subject_correlation_analysis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    isc_output: OutputPathType
    """Main output ISC file"""
    tstat_output: OutputPathType
    """T-statistic of ISC"""


def v_3d_isc___voxelwise_inter_subject_correlation_analysis(
    outfile_prefix: str,
    model_structure: str,
    data_table: str,
    num_jobs: float | int | None = None,
    mask_file: InputPathType | None = None,
    qvar_centers: str | None = None,
    quantitative_vars: str | None = None,
    fisher_transform: bool = False,
    io_functions: typing.Literal["AFNI", "R"] | None = None,
    runner: Runner | None = None,
) -> V3dIscVoxelwiseInterSubjectCorrelationAnalysisOutputs:
    """
    3dISC - Voxelwise Inter-Subject Correlation Analysis by AFNI Team.
    
    Program for Voxelwise Inter-Subject Correlation (ISC) Analysis using linear
    mixed-effects modeling.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dISC.html
    
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
        NamedTuple of outputs (described in `V3dIscVoxelwiseInterSubjectCorrelationAnalysisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ISC___VOXELWISE_INTER_SUBJECT_CORRELATION_ANALYSIS_METADATA)
    cargs = []
    cargs.append("3dISC")
    cargs.extend(["-prefix", outfile_prefix])
    if num_jobs is not None:
        cargs.extend(["-jobs", str(num_jobs)])
    if mask_file is not None:
        cargs.extend(["-mask", execution.input_file(mask_file)])
    cargs.extend(["-model", model_structure])
    if qvar_centers is not None:
        cargs.extend(["-qVarCenters", qvar_centers])
    if quantitative_vars is not None:
        cargs.extend(["-qVars", quantitative_vars])
    if fisher_transform:
        cargs.append("-r2z")
    if io_functions is not None:
        cargs.extend(["-cio", io_functions])
    cargs.extend(["-dataTable", data_table])
    ret = V3dIscVoxelwiseInterSubjectCorrelationAnalysisOutputs(
        root=execution.output_file("."),
        isc_output=execution.output_file(f"{outfile_prefix}_ISC.nii"),
        tstat_output=execution.output_file(f"{outfile_prefix}_tstat.nii", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dIscVoxelwiseInterSubjectCorrelationAnalysisOutputs",
    "V_3D_ISC___VOXELWISE_INTER_SUBJECT_CORRELATION_ANALYSIS_METADATA",
    "v_3d_isc___voxelwise_inter_subject_correlation_analysis",
]