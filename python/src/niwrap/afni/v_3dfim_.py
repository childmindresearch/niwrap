# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DFIM__METADATA = Metadata(
    id="ed6c39905af4f754185b395fbb536977b06338b9.boutiques",
    name="3dfim+",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dfimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dfim_(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_tlrc_head: OutputPathType | None
    """Output bucket dataset containing fit parameters, in TLRC space."""
    outfile_tlrc_brk: OutputPathType | None
    """Output bucket dataset containing fit parameters, in TLRC space."""
    outfile_orig_head: OutputPathType | None
    """Output bucket dataset containing fit parameters, in original space."""
    outfile_orig_brk: OutputPathType | None
    """Output bucket dataset containing fit parameters, in original space."""


def v_3dfim_(
    infile: InputPathType,
    ideal_file: InputPathType,
    input1dfile: InputPathType | None = None,
    maskfile: InputPathType | None = None,
    first_image: float | None = None,
    last_image: float | None = None,
    baseline_polynomial: float | None = None,
    threshold: float | None = None,
    cdisp_value: float | None = None,
    ort_file: InputPathType | None = None,
    output_params: list[str] | None = None,
    output_bucket: str | None = None,
    runner: Runner | None = None,
) -> V3dfimOutputs:
    """
    Program to calculate the cross-correlation of an ideal reference waveform with
    the measured FMRI time series for each voxel.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dfim+.html
    
    Args:
        infile: Filename of input 3d+time dataset.
        ideal_file: Input ideal time series file name. Can be used multiple\
            times.
        input1dfile: Filename of single (fMRI) .1D time series.
        maskfile: Filename of 3d mask dataset.
        first_image: Number of first dataset image to use in the\
            cross-correlation procedure (default = 0).
        last_image: Number of last dataset image to use in the\
            cross-correlation procedure (default = last).
        baseline_polynomial: Degree of polynomial corresponding to the baseline\
            model (default: 1). Use -1 for no baseline model.
        threshold: FIM internal mask threshold value (0 <= p <= 1) to get rid\
            of low intensity voxels (default: 0.0999).
        cdisp_value: Write (to screen) results for voxels whose correlation\
            stat. > cval (0 <= cval <= 1; default: disabled).
        ort_file: Input ort time series file name. Can be used multiple times.
        output_params: Output the specified parameter. Can be used multiple\
            times. Possible values are: 'Fit Coef', 'Best Index', '% Change',\
            'Baseline', 'Correlation', '% From Ave', 'Average', '% From Top',\
            'Topline', 'Sigma Resid', 'All', 'Spearman CC', 'Quadrant CC'.
        output_bucket: Create one AFNI 'bucket' dataset containing the\
            parameters of interest, as specified by the '-out' commands. The output\
            'bucket' dataset is written to a file with the prefix name bprefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dfimOutputs`).
    """
    if threshold is not None and not (0 <= threshold <= 1): 
        raise ValueError(f"'threshold' must be between 0 <= x <= 1 but was {threshold}")
    if cdisp_value is not None and not (0 <= cdisp_value <= 1): 
        raise ValueError(f"'cdisp_value' must be between 0 <= x <= 1 but was {cdisp_value}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DFIM__METADATA)
    cargs = []
    cargs.append("3dfim+")
    cargs.append("-input")
    cargs.append(execution.input_file(infile))
    if input1dfile is not None:
        cargs.extend([
            "-input1D",
            execution.input_file(input1dfile)
        ])
    if maskfile is not None:
        cargs.extend([
            "-mask",
            execution.input_file(maskfile)
        ])
    if first_image is not None:
        cargs.extend([
            "-nfirst",
            str(first_image)
        ])
    if last_image is not None:
        cargs.extend([
            "-nlast",
            str(last_image)
        ])
    if baseline_polynomial is not None:
        cargs.extend([
            "-polort",
            str(baseline_polynomial)
        ])
    if threshold is not None:
        cargs.extend([
            "-fim_thr",
            str(threshold)
        ])
    if cdisp_value is not None:
        cargs.extend([
            "-cdisp",
            str(cdisp_value)
        ])
    if ort_file is not None:
        cargs.extend([
            "-ort_file",
            execution.input_file(ort_file)
        ])
    cargs.append("-ideal_file")
    cargs.extend([
        "-ideal_file",
        execution.input_file(ideal_file)
    ])
    if output_params is not None:
        cargs.extend([
            "-out",
            *output_params
        ])
    cargs.append("-bucket")
    if output_bucket is not None:
        cargs.extend([
            "-bucket",
            output_bucket
        ])
    ret = V3dfimOutputs(
        root=execution.output_file("."),
        outfile_tlrc_head=execution.output_file(output_bucket + "+tlrc.HEAD") if (output_bucket is not None) else None,
        outfile_tlrc_brk=execution.output_file(output_bucket + "+tlrc.BRIK") if (output_bucket is not None) else None,
        outfile_orig_head=execution.output_file(output_bucket + "+orig.HEAD") if (output_bucket is not None) else None,
        outfile_orig_brk=execution.output_file(output_bucket + "+orig.BRIK") if (output_bucket is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dfimOutputs",
    "V_3DFIM__METADATA",
    "v_3dfim_",
]