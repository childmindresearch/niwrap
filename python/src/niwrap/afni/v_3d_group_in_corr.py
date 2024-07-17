# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_GROUP_IN_CORR_METADATA = Metadata(
    id="494cb5b5d59b2264a2ef671b4756fcdcdd14e389",
    name="3dGroupInCorr",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dGroupInCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_group_in_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Results from analysis"""


def v_3d_group_in_corr(
    set_a: InputPathType,
    set_b: InputPathType | None = None,
    apair: bool = False,
    label_a: str | None = None,
    label_b: str | None = None,
    pooled: bool = False,
    unpooled: bool = False,
    paired: bool = False,
    nosix: bool = False,
    covariates_file: InputPathType | None = None,
    center: str | None = None,
    seed_radius: float | int | None = None,
    sendall: bool = False,
    donocov: bool = False,
    dospcov: bool = False,
    cluster: str | None = None,
    read: bool = False,
    ztest: bool = False,
    ah: str | None = None,
    port_offset: float | int | None = None,
    port_offset_quiet: float | int | None = None,
    port_bloc: float | int | None = None,
    suma: bool = False,
    quiet: bool = False,
    verbose: bool = False,
    very_verbose: bool = False,
    debug: bool = False,
    batch: str | None = None,
    runner: Runner | None = None,
) -> V3dGroupInCorrOutputs:
    """
    3dGroupInCorr by AFNI Team.
    
    Functional connectivity analysis in group of subjects.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dGroupInCorr.html
    
    Args:
        set_a: Setup file describing the first dataset collection.
        set_b: Setup file describing the second dataset collection for\
            two-sample t-test analysis.
        apair: Use -setA collection again but with different seed locations;\
            produce paired t-test.
        label_a: Label for sub-bricks corresponding to setA.
        label_b: Label for sub-bricks corresponding to setB.
        pooled: Use pooled variance estimator for two-sample un-paired t-test.
        unpooled: Use unpooled variance estimator for two-sample un-paired\
            t-test.
        paired: Use a two-sample paired t-test.
        nosix: Suppress the individual 1-sample t-tests and only return the\
            difference 2-sample t-test.
        covariates_file: File containing covariate values for each dataset.
        center: Option for centering covariates.
        seed_radius: Radius for seed voxel time series averaging (mm).
        sendall: Send all individual subject results to AFNI along with group\
            statistics.
        donocov: Compute results both with and without covariates.
        dospcov: Compute Spearman (rank) correlation coefficient of subject\
            correlation results vs each covariate.
        cluster: Input results from a 3dClustSim run to interface with AFNI.
        read: Force program to read data into memory instead of memory mapping.
        ztest: Debugging option to test if input data is all zero.
        ah: Connect to AFNI/SUMA on a remote host.
        port_offset: Provide a port offset.
        port_offset_quiet: Provide a port offset, with less verbose output.
        port_bloc: Provide a port offset bloc.
        suma: Talk to SUMA instead of AFNI.
        quiet: Suppress informational messages.
        verbose: Print extra informational messages.
        very_verbose: Print even more detailed informational messages.
        debug: Enable internal testing.
        batch: Run program in batch mode with specified METHOD and command\
            file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dGroupInCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_GROUP_IN_CORR_METADATA)
    cargs = []
    cargs.append("3dGroupInCorr")
    cargs.extend(["-setA", execution.input_file(set_a)])
    if set_b is not None:
        cargs.extend(["-setB", execution.input_file(set_b)])
    if apair:
        cargs.append("-Apair")
    if label_a is not None:
        cargs.extend(["-labelA", label_a])
    if label_b is not None:
        cargs.extend(["-labelB", label_b])
    if pooled:
        cargs.append("-pooled")
    if unpooled:
        cargs.append("-unpooled")
    if paired:
        cargs.append("-paired")
    if nosix:
        cargs.append("-nosix")
    if covariates_file is not None:
        cargs.extend(["-covariates", execution.input_file(covariates_file)])
    if center is not None:
        cargs.extend(["-center", center])
    if seed_radius is not None:
        cargs.extend(["-seedrad", str(seed_radius)])
    if sendall:
        cargs.append("-sendall")
    if donocov:
        cargs.append("-donocov")
    if dospcov:
        cargs.append("-dospcov")
    if cluster is not None:
        cargs.extend(["-clust", cluster])
    if read:
        cargs.append("-read")
    if ztest:
        cargs.append("-ztest")
    if ah is not None:
        cargs.extend(["-ah", ah])
    if port_offset is not None:
        cargs.extend(["-np", str(port_offset)])
    if port_offset_quiet is not None:
        cargs.extend(["-npq", str(port_offset_quiet)])
    if port_bloc is not None:
        cargs.extend(["-npb", str(port_bloc)])
    if suma:
        cargs.append("-suma")
    if quiet:
        cargs.append("-quiet")
    if verbose:
        cargs.append("-verb")
    if very_verbose:
        cargs.append("-VERB")
    if debug:
        cargs.append("-debug")
    if batch is not None:
        cargs.extend(["-batch", batch])
    ret = V3dGroupInCorrOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{pathlib.Path(set_a).name}.results.nii"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dGroupInCorrOutputs",
    "V_3D_GROUP_IN_CORR_METADATA",
    "v_3d_group_in_corr",
]
