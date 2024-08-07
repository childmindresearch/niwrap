# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_LSS_METADATA = Metadata(
    id="693a1475ddc6ecf782a257e16ff0134339f983ea",
    name="3dLSS",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dLssOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lss(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset containing the LSS estimates of the beta weights for the '-stim_times_IM' stimuli."""
    save1_d_output: OutputPathType | None
    """Estimator vectors saved in a 1D formatted file."""


def v_3d_lss(
    matrix: InputPathType,
    input_: InputPathType | None = None,
    nodata: bool = False,
    mask: InputPathType | None = None,
    automask: bool = False,
    prefix: str | None = None,
    save1_d: str | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dLssOutputs:
    """
    3dLSS by AFNI Team.
    
    Least-Squares-Sum (LSS) estimation tool from a -stim_times_IM matrix for
    multivoxel pattern classification analyses.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLSS.html
    
    Args:
        matrix: Read the matrix 'mmm', which should have been output from\
            3dDeconvolve via the '-x1D' option. It should have included exactly one\
            '-stim_times_IM' option.
        input_: Read time series dataset 'ddd'.
        nodata: Just compute the estimator matrix -- to be saved with\
            '-save1D'.
        mask: Dataset 'MMM' will be used as a mask for the input; voxels\
            outside the mask will not be fit by the regression model.
        automask: If you don't know what this does by now, please don't use\
            this program.
        prefix: Prefix name for the output dataset; this dataset will contain\
            ONLY the LSS estimates of the beta weights for the '-stim_times_IM'\
            stimuli.
        save1_d: Save the estimator vectors to a 1D formatted file named 'qqq'.
        verbose: Write out progress reports.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLssOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LSS_METADATA)
    cargs = []
    cargs.append("3dLSS")
    cargs.append("[OPTIONS]")
    ret = V3dLssOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(f"LSSout+orig.HEAD"),
        save1_d_output=execution.output_file(f"{save1_d}", optional=True) if save1_d is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLssOutputs",
    "V_3D_LSS_METADATA",
    "v_3d_lss",
]
