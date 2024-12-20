# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__CHAUFFEUR_AFNI_METADATA = Metadata(
    id="7bd1968eb762331f9eaee48a7484852a7e447634.boutiques",
    name="@chauffeur_afni",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VChauffeurAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__chauffeur_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Generated montage image"""
    cluster_report: OutputPathType
    """Clusterization report"""
    whereami_report: OutputPathType
    """Whereami report for clusterized data"""


def v__chauffeur_afni(
    ulay: InputPathType,
    prefix: str,
    olay: InputPathType | None = None,
    runner: Runner | None = None,
) -> VChauffeurAfniOutputs:
    """
    Automated QC snapshots generator in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ulay: Name of underlay dataset (required); can be 3D or 4D set.
        prefix: Prefix for output files (required).
        olay: Name of overlay dataset (optional).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VChauffeurAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CHAUFFEUR_AFNI_METADATA)
    cargs = []
    cargs.append("@chauffeur_afni")
    cargs.append(execution.input_file(ulay))
    if olay is not None:
        cargs.append(execution.input_file(olay))
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.append("[options]")
    ret = VChauffeurAfniOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(prefix + ".png"),
        cluster_report=execution.output_file(prefix + "_clust_rep.txt"),
        whereami_report=execution.output_file(prefix + "_clust_whereami.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VChauffeurAfniOutputs",
    "V__CHAUFFEUR_AFNI_METADATA",
    "v__chauffeur_afni",
]
