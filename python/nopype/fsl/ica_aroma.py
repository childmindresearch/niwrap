# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:56.041054

import typing

from ..styxdefs import *


ICA_AROMA_METADATA = Metadata(
    id="de4547d02600becf49ef09b070f91bbb67382d0c",
    name="ICA_AROMA",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class IcaAromaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ica_aroma(...)`.
    """
    aggr_denoised_file: OutputPathType
    """If generated: aggressively denoised volume."""
    nonaggr_denoised_file: OutputPathType
    """If generated: non aggressively denoised volume."""
    out_dir_outfile: OutputPathType
    """file or string representing an existing directory. Directory contains (in addition to the denoised files): melodic.ica + classified_motion_components + classification_overview + feature_scores + melodic_ic_mni)."""


def ica_aroma(
    runner: Runner,
    feat_dir: InputPathType,
    in_file: InputPathType,
    motion_parameters: InputPathType,
    tr: float | int | None = None,
    denoise_type: typing.Literal["nonaggr", "aggr", "both", "no"] = "nonaggr",
    dim: int | None = None,
    fnirt_warp_file: InputPathType | None = None,
    mask: InputPathType | None = None,
    mat_file: InputPathType | None = None,
    melodic_dir: InputPathType | None = None,
    out_dir: InputPathType = "out",
) -> IcaAromaOutputs:
    """
    ICA_AROMA, as implemented in Nipype (module: nipype.interfaces.fsl.aroma,
    interface: ICA_AROMA).
    
    Interface for the ICA_AROMA.py script.
    ICA-AROMA (i.e. 'ICA-based Automatic Removal Of Motion Artifacts') concerns
    a data-driven method to identify and remove motion-related independent
    components from fMRI data. To that end it exploits a small, but robust set
    of theoretically motivated features, preventing the need for classifier
    re-training and therefore providing direct and easy applicability.
    See link for further documentation: https://github.com/rhr-pruim/ICA-AROMA
    Example -------
    >>> from nipype.interfaces.fsl import ICA_AROMA >>> from nipype.testing
    import example_data >>> AROMA_obj = ICA_AROMA() >>> AROMA_obj.inputs.in_file
    = 'functional.nii' >>> AROMA_obj.inputs.mat_file = 'func_to_struct.mat' >>>
    AROMA_obj.inputs.fnirt_warp_file = 'warpfield.nii' >>>
    AROMA_obj.inputs.motion_parameters = 'fsl_mcflirt_movpar.txt' >>>
    AROMA_obj.inputs.mask = 'mask.nii.gz' >>> AROMA_obj.inputs.denoise_type =
    'both' >>> AROMA_obj.inputs.out_dir = 'ICA_testout' >>> AROMA_obj.cmdline #
    doctest: +ELLIPSIS 'ICA_AROMA.py -den both -warp warpfield.nii -i
    functional.nii -m mask.nii.gz -affmat func_to_struct.mat -mc
    fsl_mcflirt_movpar.txt -o .../ICA_testout'
    
    Args:
        runner: Command runner
        feat_dir: file or string representing an existing directory. If a feat
            directory exists and temporal filtering has not been run yet, ica_aroma
            can use the files in this directory.
        in_file: Volume to be denoised.
        motion_parameters: Motion parameters file.
        tr: Tr in seconds. if this is not specified the tr will be extracted
            from the header of the fmri nifti file.
        denoise_type: 'nonaggr' or 'aggr' or 'both' or 'no'. Type of denoising
            strategy:-no: only classification, no denoising-nonaggr (default):
            non-aggresssive denoising, i.e. partial component regression-aggr:
            aggressive denoising, i.e. full component regression-both: both
            aggressive and non-aggressive denoising (two outputs).
        dim: Dimensionality reduction when running melodic (default is automatic
            estimation).
        fnirt_warp_file: File name of the warp-file describing the non-linear
            registration (e.g. fsl fnirt) of the structural data to mni152 space
            (.nii.gz).
        mask: Path/name volume mask.
        mat_file: Path/name of the mat-file describing the affine registration
            (e.g. fsl flirt) of the functional data to structural space (.mat file).
        melodic_dir: file or string representing an existing directory. Path to
            melodic directory if melodic has already been run.
        out_dir: file or string representing a directory. Output directory.
    Returns:
        NamedTuple of outputs (described in `IcaAromaOutputs`).
    """
    if (
        (fnirt_warp_file is not None) +
        (motion_parameters is not None) +
        (mat_file is not None) +
        (in_file is not None) +
        (feat_dir is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "fnirt_warp_file,\n"
            "motion_parameters,\n"
            "mat_file,\n"
            "in_file,\n"
            "feat_dir"
        )
    if (
        (in_file is not None) +
        (feat_dir is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "in_file,\n"
            "feat_dir"
        )
    if (
        (mask is not None) +
        (feat_dir is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "mask,\n"
            "feat_dir"
        )
    if (
        (feat_dir is not None) +
        (mat_file is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "feat_dir,\n"
            "mat_file"
        )
    if (
        (fnirt_warp_file is not None) +
        (feat_dir is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "fnirt_warp_file,\n"
            "feat_dir"
        )
    if (
        (feat_dir is not None) +
        (motion_parameters is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "feat_dir,\n"
            "motion_parameters"
        )
    execution = runner.start_execution(ICA_AROMA_METADATA)
    cargs = []
    cargs.append("ICA_AROMA")
    if tr is not None:
        cargs.extend(["-tr", str(tr)])
    cargs.append("[ARGS]")
    cargs.extend(["-den", denoise_type])
    if dim is not None:
        cargs.extend(["-dim", str(dim)])
    cargs.append("[ENVIRON]")
    cargs.extend(["-feat", execution.input_file(feat_dir)])
    if fnirt_warp_file is not None:
        cargs.extend(["-warp", execution.input_file(fnirt_warp_file)])
    cargs.extend(["-i", execution.input_file(in_file)])
    if mask is not None:
        cargs.extend(["-m", execution.input_file(mask)])
    if mat_file is not None:
        cargs.extend(["-affmat", execution.input_file(mat_file)])
    if melodic_dir is not None:
        cargs.extend(["-meldir", execution.input_file(melodic_dir)])
    cargs.extend(["-mc", execution.input_file(motion_parameters)])
    cargs.extend(["-o", execution.input_file(out_dir)])
    ret = IcaAromaOutputs(
        aggr_denoised_file=execution.output_file(f"out\denoised_func_data_aggr.nii.gz", optional=True),
        nonaggr_denoised_file=execution.output_file(f"out\denoised_func_data_nonaggr.nii.gz", optional=True),
        out_dir_outfile=execution.output_file(f"out", optional=True),
    )
    execution.run(cargs)
    return ret
