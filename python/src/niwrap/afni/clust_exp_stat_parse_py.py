# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CLUST_EXP_STAT_PARSE_PY_METADATA = Metadata(
    id="5722f63fe412fec07ef18b10adae7246e4c062b4.boutiques",
    name="ClustExp_StatParse.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ClustExpStatParsePyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `clust_exp_stat_parse_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    table_mean: OutputPathType | None
    """Table with all data extracted from all subjects."""
    group_table: OutputPathType | None
    """Table with information parsed from the statistics data set history."""
    v_3dclust_output: OutputPathType | None
    """Output directly from 3dclust."""
    clusters_output: OutputPathType | None
    """Cleaned up version of the whereami output."""
    statinfo_output: OutputPathType | None
    """Summary info for the shiny app."""
    thresholded_dataset: OutputPathType | None
    """A new data set from input statistics, thresholded at uncorrected p
    value."""
    thresholded_mask_dataset: OutputPathType | None
    """Integer labeled mask of the thresholded image with cluster sizes at least
    as big as the -MinVox."""
    master_copy: OutputPathType | None
    """A NIfTI copy of the master file provided that may have been resampled."""


def clust_exp_stat_parse_py(
    statdset: InputPathType,
    meanbrik: float,
    threshbrik: float,
    subjdset: InputPathType,
    subjtable: InputPathType,
    master: InputPathType,
    prefix: str | None = None,
    pval: float | None = None,
    minvox: float | None = None,
    atlas: str | None = None,
    session: str | None = None,
    noshiny: bool = False,
    overwrite: bool = False,
    runner: Runner | None = None,
) -> ClustExpStatParsePyOutputs:
    """
    Parser for statistical data sets and subject data sets, generating several
    outputs for further analysis.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/ClustExp_StatParse.py.html
    
    Args:
        statdset: Statistics dataset.
        meanbrik: Mean subbrik (integer >= 0).
        threshbrik: Threshold subbrik. Might be the same as MeanBrik (integer\
            >= 0).
        subjdset: Labeled dataset with all subjects (from @ClustExp_CatLab).
        subjtable: Table with subject labels and input datasets.
        master: Master data set for underlay.
        prefix: Name for output (no path).
        pval: Uncorrected p value for thresholding.
        minvox: Minimum voxels in cluster.
        atlas: Atlas name for lookup (list at: whereami -help).
        session: Output parent folder if you don't want the current working\
            directory.
        noshiny: Do not create shiny app.
        overwrite: Remove previous folder with same PREFIX.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ClustExpStatParsePyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CLUST_EXP_STAT_PARSE_PY_METADATA)
    cargs = []
    cargs.append("ClustExp_StatParse.py")
    cargs.extend([
        "-StatDSET",
        execution.input_file(statdset)
    ])
    cargs.extend([
        "-MeanBrik",
        str(meanbrik)
    ])
    cargs.extend([
        "-ThreshBrik",
        str(threshbrik)
    ])
    cargs.extend([
        "-SubjDSET",
        execution.input_file(subjdset)
    ])
    cargs.extend([
        "-SubjTable",
        execution.input_file(subjtable)
    ])
    cargs.extend([
        "-master",
        execution.input_file(master)
    ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if pval is not None:
        cargs.extend([
            "-p",
            str(pval)
        ])
    if minvox is not None:
        cargs.extend([
            "-MinVox",
            str(minvox)
        ])
    if atlas is not None:
        cargs.extend([
            "-atlas",
            atlas
        ])
    if session is not None:
        cargs.extend([
            "-session",
            session
        ])
    if noshiny:
        cargs.append("-NoShiny")
    if overwrite:
        cargs.append("-overwrite")
    ret = ClustExpStatParsePyOutputs(
        root=execution.output_file("."),
        table_mean=execution.output_file(prefix + "_p_uncor_" + str(pval) + "_mean.csv") if (prefix is not None and pval is not None) else None,
        group_table=execution.output_file(prefix + "_GroupTable.csv") if (prefix is not None) else None,
        v_3dclust_output=execution.output_file(prefix + "_p_uncor_" + str(pval) + "_3dclust.1D") if (prefix is not None and pval is not None) else None,
        clusters_output=execution.output_file(prefix + "_p_uncor_" + str(pval) + "_clusters.csv") if (prefix is not None and pval is not None) else None,
        statinfo_output=execution.output_file(prefix + "_StatInfo.csv") if (prefix is not None) else None,
        thresholded_dataset=execution.output_file(prefix + "_p_uncor_" + str(pval) + ".nii.gz") if (prefix is not None and pval is not None) else None,
        thresholded_mask_dataset=execution.output_file(prefix + "_p_uncor_" + str(pval) + "_mask.nii.gz") if (prefix is not None and pval is not None) else None,
        master_copy=execution.output_file(prefix + "_master.nii.gz") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CLUST_EXP_STAT_PARSE_PY_METADATA",
    "ClustExpStatParsePyOutputs",
    "clust_exp_stat_parse_py",
]