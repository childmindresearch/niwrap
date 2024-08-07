# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

EDDY_METADATA = Metadata(
    id="c332a1202ba54010ec187db71d0687c41e40cb96",
    name="eddy",
    container_image_type="docker",
    container_image_tag="fnndsc/fsl:6.0.5.1-cuda9.1",
)


class EddyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """Output file containing the corrected images"""


def eddy(
    imain: InputPathType,
    mask: InputPathType,
    index: InputPathType,
    acqp: InputPathType,
    bvecs: InputPathType,
    bvals: InputPathType,
    implementation: typing.Literal["", "_openmp", "_cuda", "_cuda10.2", "_cuda9.1", "_cuda8.0"] = "",
    out: str = "eddy_corrected",
    mb: float | int | None = None,
    mb_offs: float | int | None = None,
    slspec: InputPathType | None = None,
    json_: InputPathType | None = None,
    mporder: float | int | None = None,
    s2v_lambda: float | int | None = None,
    topup: str | None = None,
    field: InputPathType | None = None,
    field_mat: InputPathType | None = None,
    flm: typing.Literal["movement", "linear", "quadratic", "cubic"] | None = None,
    slm: typing.Literal["none", "linear", "quadratic"] | None = None,
    fwhm: float | int | None = None,
    niter: float | int | None = None,
    s2v_niter: float | int | None = None,
    cnr_maps: bool = False,
    residuals: bool = False,
    fep: bool = False,
    interp: typing.Literal["spline", "trilinear"] | None = None,
    s2v_interp: typing.Literal["spline", "trilinear"] | None = None,
    resamp: typing.Literal["jac", "lsr"] | None = None,
    nvoxhp: float | int | None = None,
    initrand: float | int | None = None,
    ff: float | int | None = None,
    repol: bool = False,
    ol_nstd: float | int | None = None,
    ol_nvox: float | int | None = None,
    ol_type: typing.Literal["sw", "gw", "both"] | None = None,
    ol_pos: bool = False,
    ol_sqr: bool = False,
    estimate_move_by_susceptibility: bool = False,
    mbs_niter: float | int | None = None,
    mbs_lambda: float | int | None = None,
    mbs_ksp: float | int | None = None,
    dont_sep_offs_move: bool = False,
    dont_peas: bool = False,
    data_is_shelled: bool = False,
    verbose: bool = False,
    runner: Runner | None = None,
) -> EddyOutputs:
    """
    eddy by Jesper Andersson (University of Oxford).
    
    A tool for correcting eddy currents and movements in diffusion data.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/eddy
    
    Args:
        imain: File containing all the images to estimate distortions for.
        mask: Mask to indicate brain.
        index: File containing indices for all volumes in --imain into --acqp\
            and --topup.
        acqp: File containing acquisition parameters.
        bvecs: File containing the b-vectors for all volumes in --imain.
        bvals: File containing the b-values for all volumes in --imain.
        implementation: Choose the implementation to use.
        out: Basename for output.
        mb: Multi-band factor.
        mb_offs: Multi-band offset (-1 if bottom slice removed, 1 if top slice\
            removed).
        slspec: Name of text file completely specifying slice/group acuistion.\
            N.B. --slspec and --json are mutually exclusive.
        json_: Name of .json text file with information about slice timing.\
            N.B. --json and --slspec are mutually exclusive.
        mporder: Order of slice-to-vol movement model (default 0, i.e.\
            vol-to-vol.
        s2v_lambda: Regularisation weight for slice-to-vol movement. (default\
            1, reasonable range 1--10).
        topup: Base name for output files from topup.
        field: Name of file with susceptibility field (in Hz).
        field_mat: Name of rigid body transform for susceptibility field.
        flm: First level EC model (movement/linear/quadratic/cubic, default\
            quadratic).
        slm: Second level EC model (none/linear/quadratic, default none).
        fwhm: FWHM for conditioning filter when estimating the parameters\
            (default 0).
        niter: Number of iterations (default 5).
        s2v_niter: Number of iterations for slice-to-vol (default 5).
        cnr_maps: Write shell-wise cnr-maps (default false).
        residuals: Write residuals (between GP and observations), (default\
            false).
        fep: Fill empty planes in x- or y-directions (default false).
        interp: Interpolation model for estimation step (spline/trilinear,\
            default spline).
        s2v_interp: Slice-to-vol interpolation model for estimation step\
            (spline/trilinear, default trilinear).
        resamp: Final resampling method (jac/lsr, default jac).
        nvoxhp: # of voxels used to estimate the hyperparameters (default 1000).
        initrand: Seeds rand for when selecting voxels (default 0=no seeding).
        ff: Fudge factor for hyperparameter error variance (default 10.0).
        repol: Detect and replace outlier slices (default false)).
        ol_nstd: Number of std off to qualify as outlier (default 4).
        ol_nvox: Min # of voxels in a slice for inclusion in outlier detection\
            (default 250).
        ol_type: Type of outliers, slicewise (sw), groupwise (gw) or both\
            (both). (default sw).
        ol_pos: Consider both positive and negative outliers if set (default\
            false).
        ol_sqr: Consider outliers among sums-of-squared differences if set\
            (default false).
        estimate_move_by_susceptibility: Estimate how susceptibility field\
            changes with subject movement (default false).
        mbs_niter: Number of iterations for MBS estimation (default 10).
        mbs_lambda: Weighting of regularisation for MBS estimation (default 10).
        mbs_ksp: Knot-spacing for MBS field estimation (default 10mm).
        dont_sep_offs_move: Do NOT attempt to separate field offset from\
            subject movement (default false).
        dont_peas: Do NOT perform a post-eddy alignment of shells (default\
            false).
        data_is_shelled: Assume, don't check, that data is shelled (default\
            false).
        verbose: switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EddyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_METADATA)
    cargs = []
    cargs.append(
        "eddy" +
        implementation +
        ""
    )
    cargs.extend(["--imain", execution.input_file(imain)])
    cargs.extend(["--mask", execution.input_file(mask)])
    cargs.extend(["--index", execution.input_file(index)])
    cargs.extend(["--acqp", execution.input_file(acqp)])
    cargs.extend(["--bvecs", execution.input_file(bvecs)])
    cargs.extend(["--bvals", execution.input_file(bvals)])
    cargs.extend(["--out", out])
    if mb is not None:
        cargs.extend(["--mb", str(mb)])
    if mb_offs is not None:
        cargs.extend(["--mb_offs", str(mb_offs)])
    if slspec is not None:
        cargs.extend(["--slspec", execution.input_file(slspec)])
    if json_ is not None:
        cargs.extend(["--json", execution.input_file(json_)])
    if mporder is not None:
        cargs.extend(["--mporder", str(mporder)])
    if s2v_lambda is not None:
        cargs.extend(["--s2v_lambda", str(s2v_lambda)])
    if topup is not None:
        cargs.extend(["--topup", topup])
    if field is not None:
        cargs.extend(["--field", execution.input_file(field)])
    if field_mat is not None:
        cargs.extend(["--field_mat", execution.input_file(field_mat)])
    if flm is not None:
        cargs.extend(["--flm", flm])
    if slm is not None:
        cargs.extend(["--slm", slm])
    if fwhm is not None:
        cargs.extend(["--fwhm", str(fwhm)])
    if niter is not None:
        cargs.extend(["--niter", str(niter)])
    if s2v_niter is not None:
        cargs.extend(["--s2v_niter", str(s2v_niter)])
    if cnr_maps:
        cargs.append("--cnr_maps")
    if residuals:
        cargs.append("--residuals")
    if fep:
        cargs.append("--fep")
    if interp is not None:
        cargs.extend(["--interp", interp])
    if s2v_interp is not None:
        cargs.extend(["--s2v_interp", s2v_interp])
    if resamp is not None:
        cargs.extend(["--resamp", resamp])
    if nvoxhp is not None:
        cargs.extend(["--nvoxhp", str(nvoxhp)])
    if initrand is not None:
        cargs.extend(["--initrand", str(initrand)])
    if ff is not None:
        cargs.extend(["--ff", str(ff)])
    if repol:
        cargs.append("--repol")
    if ol_nstd is not None:
        cargs.extend(["--ol_nstd", str(ol_nstd)])
    if ol_nvox is not None:
        cargs.extend(["--ol_nvox", str(ol_nvox)])
    if ol_type is not None:
        cargs.extend(["--ol_type", ol_type])
    if ol_pos:
        cargs.append("--ol_pos")
    if ol_sqr:
        cargs.append("--ol_sqr")
    if estimate_move_by_susceptibility:
        cargs.append("--estimate_move_by_susceptibility")
    if mbs_niter is not None:
        cargs.extend(["--mbs_niter", str(mbs_niter)])
    if mbs_lambda is not None:
        cargs.extend(["--mbs_lambda", str(mbs_lambda)])
    if mbs_ksp is not None:
        cargs.extend(["--mbs_ksp", str(mbs_ksp)])
    if dont_sep_offs_move:
        cargs.append("--dont_sep_offs_move")
    if dont_peas:
        cargs.append("--dont_peas")
    if data_is_shelled:
        cargs.append("--data_is_shelled")
    if verbose:
        cargs.append("-v")
    ret = EddyOutputs(
        root=execution.output_file("."),
        out=execution.output_file(f"{out}.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EDDY_METADATA",
    "EddyOutputs",
    "eddy",
]
