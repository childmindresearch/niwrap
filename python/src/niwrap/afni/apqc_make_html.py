# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

APQC_MAKE_HTML_METADATA = Metadata(
    id="a958dc9e454decaf99b430f63930ca86b1108a1f.boutiques",
    name="apqc_make_html",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ApqcMakeHtmlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apqc_make_html(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def apqc_make_html(
    qc_dir: str,
    runner: Runner | None = None,
) -> ApqcMakeHtmlOutputs:
    """
    Tool to generate HTML reports.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        qc_dir: Directory where QC files will be saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApqcMakeHtmlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APQC_MAKE_HTML_METADATA)
    cargs = []
    cargs.append("apqc_make_html.py")
    cargs.extend([
        "-qc_dir",
        qc_dir
    ])
    ret = ApqcMakeHtmlOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APQC_MAKE_HTML_METADATA",
    "ApqcMakeHtmlOutputs",
    "apqc_make_html",
]
