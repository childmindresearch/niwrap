# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

QUICKSPEC_SL_METADATA = Metadata(
    id="6ad0ef7a3cf68472db5f2c42ec5677d562d0ca24.boutiques",
    name="quickspecSL",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
QuickspecSlParameters = typing.TypedDict('QuickspecSlParameters', {
    "__STYX_TYPE__": typing.Literal["quickspecSL"],
    "surf_A": InputPathType,
    "surf_B": InputPathType,
    "surf_intermed_pref": typing.NotRequired[str | None],
    "infl_surf_A": typing.NotRequired[InputPathType | None],
    "infl_surf_B": typing.NotRequired[InputPathType | None],
    "infl_surf_intermed_pref": typing.NotRequired[str | None],
    "both_lr_flag": bool,
    "out_spec": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "quickspecSL": quickspec_sl_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "quickspecSL": quickspec_sl_outputs,
    }.get(t)


class QuickspecSlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quickspec_sl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_spec_file: OutputPathType | None
    """Output spec file"""


def quickspec_sl_params(
    surf_a: InputPathType,
    surf_b: InputPathType,
    surf_intermed_pref: str | None = None,
    infl_surf_a: InputPathType | None = None,
    infl_surf_b: InputPathType | None = None,
    infl_surf_intermed_pref: str | None = None,
    both_lr_flag: bool = False,
    out_spec: str | None = None,
) -> QuickspecSlParameters:
    """
    Build parameters.
    
    Args:
        surf_a: Inner (anatomically-correct) boundary surface dataset (e.g.\
            smoothwm.gii).
        surf_b: Outer (anatomically-correct) boundary surface dataset (e.g.\
            pial.gii).
        surf_intermed_pref: Prefix for (anatomically-correct) intermediate\
            surfaces, typically output by SurfLayers (default: isurf).
        infl_surf_a: Inner (inflated) boundary surface dataset (e.g.\
            infl.smoothwm.gii).
        infl_surf_b: Outer (inflated) boundary surface dataset (e.g.\
            infl.pial.gii).
        infl_surf_intermed_pref: Prefix for (inflated) intermediate surfaces,\
            typically output by SurfLayers (default: infl.isurf).
        both_lr_flag: Specify an output spec for both hemispheres if surfaces\
            for both exist.
        out_spec: Name for output *.spec file (default: newspec.spec).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "quickspecSL",
        "surf_A": surf_a,
        "surf_B": surf_b,
        "both_lr_flag": both_lr_flag,
    }
    if surf_intermed_pref is not None:
        params["surf_intermed_pref"] = surf_intermed_pref
    if infl_surf_a is not None:
        params["infl_surf_A"] = infl_surf_a
    if infl_surf_b is not None:
        params["infl_surf_B"] = infl_surf_b
    if infl_surf_intermed_pref is not None:
        params["infl_surf_intermed_pref"] = infl_surf_intermed_pref
    if out_spec is not None:
        params["out_spec"] = out_spec
    return params


def quickspec_sl_cargs(
    params: QuickspecSlParameters,
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
    cargs.append("quickspecSL")
    cargs.extend([
        "-surf_A",
        execution.input_file(params.get("surf_A"))
    ])
    cargs.extend([
        "-surf_B",
        execution.input_file(params.get("surf_B"))
    ])
    if params.get("surf_intermed_pref") is not None:
        cargs.extend([
            "-surf_intermed_pref",
            params.get("surf_intermed_pref")
        ])
    if params.get("infl_surf_A") is not None:
        cargs.extend([
            "-infl_surf_A",
            execution.input_file(params.get("infl_surf_A"))
        ])
    if params.get("infl_surf_B") is not None:
        cargs.extend([
            "-infl_surf_B",
            execution.input_file(params.get("infl_surf_B"))
        ])
    if params.get("infl_surf_intermed_pref") is not None:
        cargs.extend([
            "-infl_surf_intermed_pref",
            params.get("infl_surf_intermed_pref")
        ])
    if params.get("both_lr_flag"):
        cargs.append("-both_lr")
    if params.get("out_spec") is not None:
        cargs.extend([
            "-out_spec",
            params.get("out_spec")
        ])
    return cargs


def quickspec_sl_outputs(
    params: QuickspecSlParameters,
    execution: Execution,
) -> QuickspecSlOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = QuickspecSlOutputs(
        root=execution.output_file("."),
        output_spec_file=execution.output_file(params.get("out_spec")) if (params.get("out_spec") is not None) else None,
    )
    return ret


def quickspec_sl_execute(
    params: QuickspecSlParameters,
    execution: Execution,
) -> QuickspecSlOutputs:
    """
    This program makes a *.spec file after a set of intermediate surfaces have been
    generated with SurfLayers. It can also make a *.spec file that relates inflated
    surfaces to anatomically-correct surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `QuickspecSlOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = quickspec_sl_cargs(params, execution)
    ret = quickspec_sl_outputs(params, execution)
    execution.run(cargs)
    return ret


def quickspec_sl(
    surf_a: InputPathType,
    surf_b: InputPathType,
    surf_intermed_pref: str | None = None,
    infl_surf_a: InputPathType | None = None,
    infl_surf_b: InputPathType | None = None,
    infl_surf_intermed_pref: str | None = None,
    both_lr_flag: bool = False,
    out_spec: str | None = None,
    runner: Runner | None = None,
) -> QuickspecSlOutputs:
    """
    This program makes a *.spec file after a set of intermediate surfaces have been
    generated with SurfLayers. It can also make a *.spec file that relates inflated
    surfaces to anatomically-correct surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        surf_a: Inner (anatomically-correct) boundary surface dataset (e.g.\
            smoothwm.gii).
        surf_b: Outer (anatomically-correct) boundary surface dataset (e.g.\
            pial.gii).
        surf_intermed_pref: Prefix for (anatomically-correct) intermediate\
            surfaces, typically output by SurfLayers (default: isurf).
        infl_surf_a: Inner (inflated) boundary surface dataset (e.g.\
            infl.smoothwm.gii).
        infl_surf_b: Outer (inflated) boundary surface dataset (e.g.\
            infl.pial.gii).
        infl_surf_intermed_pref: Prefix for (inflated) intermediate surfaces,\
            typically output by SurfLayers (default: infl.isurf).
        both_lr_flag: Specify an output spec for both hemispheres if surfaces\
            for both exist.
        out_spec: Name for output *.spec file (default: newspec.spec).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuickspecSlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUICKSPEC_SL_METADATA)
    params = quickspec_sl_params(surf_a=surf_a, surf_b=surf_b, surf_intermed_pref=surf_intermed_pref, infl_surf_a=infl_surf_a, infl_surf_b=infl_surf_b, infl_surf_intermed_pref=infl_surf_intermed_pref, both_lr_flag=both_lr_flag, out_spec=out_spec)
    return quickspec_sl_execute(params, execution)


__all__ = [
    "QUICKSPEC_SL_METADATA",
    "QuickspecSlOutputs",
    "QuickspecSlParameters",
    "quickspec_sl",
    "quickspec_sl_params",
]
