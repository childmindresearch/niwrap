# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DJUNCT_SSW_INTERMED_EDGE_IMGS_METADATA = Metadata(
    id="e230f79426f6158216707401554de44362bbaefe.boutiques",
    name="@djunct_ssw_intermed_edge_imgs",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDjunctSswIntermedEdgeImgsParameters = typing.TypedDict('VDjunctSswIntermedEdgeImgsParameters', {
    "__STYX_TYPE__": typing.Literal["@djunct_ssw_intermed_edge_imgs"],
    "prefix": str,
    "ulay": InputPathType,
    "olay": InputPathType,
    "box_focus_slices": typing.NotRequired[str | None],
    "montgap": typing.NotRequired[str | None],
    "cbar": typing.NotRequired[str | None],
    "ulay_range": typing.NotRequired[str | None],
    "montx": typing.NotRequired[str | None],
    "monty": typing.NotRequired[str | None],
    "help_view": bool,
    "help": bool,
    "version": bool,
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
        "@djunct_ssw_intermed_edge_imgs": v__djunct_ssw_intermed_edge_imgs_cargs,
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
    vt = {}
    return vt.get(t)


class VDjunctSswIntermedEdgeImgsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_ssw_intermed_edge_imgs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__djunct_ssw_intermed_edge_imgs_params(
    prefix: str,
    ulay: InputPathType,
    olay: InputPathType,
    box_focus_slices: str | None = None,
    montgap: str | None = None,
    cbar: str | None = None,
    ulay_range: str | None = None,
    montx: str | None = None,
    monty: str | None = None,
    help_view: bool = False,
    help_: bool = False,
    version: bool = False,
    no_clean: bool = False,
) -> VDjunctSswIntermedEdgeImgsParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix for generated output files.
        ulay: Underlay dataset.
        olay: Overlay dataset.
        box_focus_slices: Slices of interest for focus box.
        montgap: Gap between montage slices.
        cbar: Color bar specification for AFNI.
        ulay_range: Range for underlay data mapping.
        montx: Number of slices along x dimension in montage.
        monty: Number of slices along y dimension in montage.
        help_view: View help file in viewer.
        help_: Displays help information.
        version: Displays version information.
        no_clean: Don't clean up intermediate files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@djunct_ssw_intermed_edge_imgs",
        "prefix": prefix,
        "ulay": ulay,
        "olay": olay,
        "help_view": help_view,
        "help": help_,
        "version": version,
        "no_clean": no_clean,
    }
    if box_focus_slices is not None:
        params["box_focus_slices"] = box_focus_slices
    if montgap is not None:
        params["montgap"] = montgap
    if cbar is not None:
        params["cbar"] = cbar
    if ulay_range is not None:
        params["ulay_range"] = ulay_range
    if montx is not None:
        params["montx"] = montx
    if monty is not None:
        params["monty"] = monty
    return params


def v__djunct_ssw_intermed_edge_imgs_cargs(
    params: VDjunctSswIntermedEdgeImgsParameters,
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
    cargs.append("@djunct_ssw_intermed_edge_imgs")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.extend([
        "-ulay",
        execution.input_file(params.get("ulay"))
    ])
    cargs.extend([
        "-olay",
        execution.input_file(params.get("olay"))
    ])
    if params.get("box_focus_slices") is not None:
        cargs.extend([
            "-box_focus_slices",
            params.get("box_focus_slices")
        ])
    if params.get("montgap") is not None:
        cargs.extend([
            "-montgap",
            params.get("montgap")
        ])
    if params.get("cbar") is not None:
        cargs.extend([
            "-cbar",
            params.get("cbar")
        ])
    if params.get("ulay_range") is not None:
        cargs.extend([
            "-ulay_range",
            params.get("ulay_range")
        ])
    if params.get("montx") is not None:
        cargs.extend([
            "-montx",
            params.get("montx")
        ])
    if params.get("monty") is not None:
        cargs.extend([
            "-monty",
            params.get("monty")
        ])
    if params.get("help_view"):
        cargs.append("-hview")
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-ver")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    return cargs


def v__djunct_ssw_intermed_edge_imgs_outputs(
    params: VDjunctSswIntermedEdgeImgsParameters,
    execution: Execution,
) -> VDjunctSswIntermedEdgeImgsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDjunctSswIntermedEdgeImgsOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__djunct_ssw_intermed_edge_imgs_execute(
    params: VDjunctSswIntermedEdgeImgsParameters,
    execution: Execution,
) -> VDjunctSswIntermedEdgeImgsOutputs:
    """
    Helper script to generate intermediate edge images for SSW-related processing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDjunctSswIntermedEdgeImgsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__djunct_ssw_intermed_edge_imgs_cargs(params, execution)
    ret = v__djunct_ssw_intermed_edge_imgs_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__djunct_ssw_intermed_edge_imgs(
    prefix: str,
    ulay: InputPathType,
    olay: InputPathType,
    box_focus_slices: str | None = None,
    montgap: str | None = None,
    cbar: str | None = None,
    ulay_range: str | None = None,
    montx: str | None = None,
    monty: str | None = None,
    help_view: bool = False,
    help_: bool = False,
    version: bool = False,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> VDjunctSswIntermedEdgeImgsOutputs:
    """
    Helper script to generate intermediate edge images for SSW-related processing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for generated output files.
        ulay: Underlay dataset.
        olay: Overlay dataset.
        box_focus_slices: Slices of interest for focus box.
        montgap: Gap between montage slices.
        cbar: Color bar specification for AFNI.
        ulay_range: Range for underlay data mapping.
        montx: Number of slices along x dimension in montage.
        monty: Number of slices along y dimension in montage.
        help_view: View help file in viewer.
        help_: Displays help information.
        version: Displays version information.
        no_clean: Don't clean up intermediate files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctSswIntermedEdgeImgsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_SSW_INTERMED_EDGE_IMGS_METADATA)
    params = v__djunct_ssw_intermed_edge_imgs_params(prefix=prefix, ulay=ulay, olay=olay, box_focus_slices=box_focus_slices, montgap=montgap, cbar=cbar, ulay_range=ulay_range, montx=montx, monty=monty, help_view=help_view, help_=help_, version=version, no_clean=no_clean)
    return v__djunct_ssw_intermed_edge_imgs_execute(params, execution)


__all__ = [
    "VDjunctSswIntermedEdgeImgsOutputs",
    "V__DJUNCT_SSW_INTERMED_EDGE_IMGS_METADATA",
    "v__djunct_ssw_intermed_edge_imgs",
    "v__djunct_ssw_intermed_edge_imgs_params",
]
