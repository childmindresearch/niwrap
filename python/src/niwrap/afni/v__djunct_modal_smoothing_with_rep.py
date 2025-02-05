# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DJUNCT_MODAL_SMOOTHING_WITH_REP_METADATA = Metadata(
    id="3dfe64fe4b416974b4aa2cc3b180143c7a5ada1d.boutiques",
    name="@djunct_modal_smoothing_with_rep",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDjunctModalSmoothingWithRepParameters = typing.TypedDict('VDjunctModalSmoothingWithRepParameters', {
    "__STYX_TYPE__": typing.Literal["@djunct_modal_smoothing_with_rep"],
    "input_file": InputPathType,
    "output_prefix": str,
    "modesmooth": typing.NotRequired[float | None],
    "help_view": bool,
    "help": bool,
    "version": bool,
    "overwrite": bool,
    "no_clean": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "@djunct_modal_smoothing_with_rep": v__djunct_modal_smoothing_with_rep_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "@djunct_modal_smoothing_with_rep": v__djunct_modal_smoothing_with_rep_outputs,
    }
    return vt.get(t)


class VDjunctModalSmoothingWithRepOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_modal_smoothing_with_rep(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file_head: OutputPathType
    """Output dataset after modal smoothing"""
    output_file_brik: OutputPathType
    """Output dataset after modal smoothing"""


def v__djunct_modal_smoothing_with_rep_params(
    input_file: InputPathType,
    output_prefix: str,
    modesmooth: float | None = None,
    help_view: bool = False,
    help_: bool = False,
    version: bool = False,
    overwrite: bool = False,
    no_clean: bool = False,
) -> VDjunctModalSmoothingWithRepParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input dataset (assumes < 10^5 subbricks).
        output_prefix: Prefix for output dataset.
        modesmooth: Fill in X in: 3dLocalstat -nbhd "SPHERE(-X)" ...
        help_view: Display help in a viewable format.
        help_: Display help information.
        version: Display version information.
        overwrite: Overwrite existing output files.
        no_clean: Do not clean up intermediate files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@djunct_modal_smoothing_with_rep",
        "input_file": input_file,
        "output_prefix": output_prefix,
        "help_view": help_view,
        "help": help_,
        "version": version,
        "overwrite": overwrite,
        "no_clean": no_clean,
    }
    if modesmooth is not None:
        params["modesmooth"] = modesmooth
    return params


def v__djunct_modal_smoothing_with_rep_cargs(
    params: VDjunctModalSmoothingWithRepParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("@djunct_modal_smoothing_with_rep")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_prefix"))
    if params.get("modesmooth") is not None:
        cargs.extend([
            "-modesmooth",
            str(params.get("modesmooth"))
        ])
    if params.get("help_view"):
        cargs.append("-hview")
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-ver")
    if params.get("overwrite"):
        cargs.append("-overwrite")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    return cargs


def v__djunct_modal_smoothing_with_rep_outputs(
    params: VDjunctModalSmoothingWithRepParameters,
    execution: Execution,
) -> VDjunctModalSmoothingWithRepOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDjunctModalSmoothingWithRepOutputs(
        root=execution.output_file("."),
        output_file_head=execution.output_file(params.get("output_prefix") + "+tlrc.HEAD"),
        output_file_brik=execution.output_file(params.get("output_prefix") + "+tlrc.BRIK"),
    )
    return ret


def v__djunct_modal_smoothing_with_rep_execute(
    params: VDjunctModalSmoothingWithRepParameters,
    execution: Execution,
) -> VDjunctModalSmoothingWithRepOutputs:
    """
    A script to perform modal smoothing of ROI maps and check for eliminated ROIs.
    If any ROIs are eliminated during smoothing, they are restored, potentially in a
    degraded form.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDjunctModalSmoothingWithRepOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__djunct_modal_smoothing_with_rep_cargs(params, execution)
    ret = v__djunct_modal_smoothing_with_rep_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__djunct_modal_smoothing_with_rep(
    input_file: InputPathType,
    output_prefix: str,
    modesmooth: float | None = None,
    help_view: bool = False,
    help_: bool = False,
    version: bool = False,
    overwrite: bool = False,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> VDjunctModalSmoothingWithRepOutputs:
    """
    A script to perform modal smoothing of ROI maps and check for eliminated ROIs.
    If any ROIs are eliminated during smoothing, they are restored, potentially in a
    degraded form.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input dataset (assumes < 10^5 subbricks).
        output_prefix: Prefix for output dataset.
        modesmooth: Fill in X in: 3dLocalstat -nbhd "SPHERE(-X)" ...
        help_view: Display help in a viewable format.
        help_: Display help information.
        version: Display version information.
        overwrite: Overwrite existing output files.
        no_clean: Do not clean up intermediate files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctModalSmoothingWithRepOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_MODAL_SMOOTHING_WITH_REP_METADATA)
    params = v__djunct_modal_smoothing_with_rep_params(input_file=input_file, output_prefix=output_prefix, modesmooth=modesmooth, help_view=help_view, help_=help_, version=version, overwrite=overwrite, no_clean=no_clean)
    return v__djunct_modal_smoothing_with_rep_execute(params, execution)


__all__ = [
    "VDjunctModalSmoothingWithRepOutputs",
    "VDjunctModalSmoothingWithRepParameters",
    "V__DJUNCT_MODAL_SMOOTHING_WITH_REP_METADATA",
    "v__djunct_modal_smoothing_with_rep",
    "v__djunct_modal_smoothing_with_rep_params",
]
