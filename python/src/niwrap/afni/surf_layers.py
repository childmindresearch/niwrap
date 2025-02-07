# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_LAYERS_METADATA = Metadata(
    id="e966c2d7b51c012df1e75b107d18f44f83eac9a4.boutiques",
    name="SurfLayers",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfLayersParameters = typing.TypedDict('SurfLayersParameters', {
    "__STYX_TYPE__": typing.Literal["SurfLayers"],
    "spec_dset": typing.NotRequired[InputPathType | None],
    "outdir": typing.NotRequired[str | None],
    "states": typing.NotRequired[str | None],
    "hemi": typing.NotRequired[str | None],
    "n_intermed_surfs": typing.NotRequired[float | None],
    "surf_a": typing.NotRequired[InputPathType | None],
    "surf_b": typing.NotRequired[InputPathType | None],
    "surf_intermed_pref": typing.NotRequired[str | None],
    "echo": bool,
    "no_clean": bool,
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
        "SurfLayers": surf_layers_cargs,
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
        "SurfLayers": surf_layers_outputs,
    }.get(t)


class SurfLayersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_layers(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    interpolated_surfaces: OutputPathType | None
    """Interpolated surfaces files"""
    additional_spec_files: OutputPathType | None
    """Additional files if -spec option was used"""
    run_view_script: OutputPathType | None
    """Run script to view output directly"""


def surf_layers_params(
    spec_dset: InputPathType | None = None,
    outdir: str | None = None,
    states: str | None = None,
    hemi: str | None = None,
    n_intermed_surfs: float | None = None,
    surf_a: InputPathType | None = None,
    surf_b: InputPathType | None = None,
    surf_intermed_pref: str | None = None,
    echo: bool = False,
    no_clean: bool = False,
) -> SurfLayersParameters:
    """
    Build parameters.
    
    Args:
        spec_dset: Dataset that is the SUMA specification file describing input\
            surfaces.
        outdir: New directory for output (default: surflayers).
        states: Typically smoothwm, pial states to describe inner and outer\
            surfaces (default: 'smoothwm pial').
        hemi: Choose hemisphere: 'lh', 'rh', or 'lh rh' (for both).
        n_intermed_surfs: Total number of intermediate surfaces to create.
        surf_a: Inner boundary surface by filename (e.g., smoothwm.gii).
        surf_b: Outer boundary surface by filename (e.g., pial.gii).
        surf_intermed_pref: Name for interpolated surfaces (default: isurf).
        echo: Run script with 'set echo' (i.e., verbosely).
        no_clean: Do not remove temp files (probably just for testing).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfLayers",
        "echo": echo,
        "no_clean": no_clean,
    }
    if spec_dset is not None:
        params["spec_dset"] = spec_dset
    if outdir is not None:
        params["outdir"] = outdir
    if states is not None:
        params["states"] = states
    if hemi is not None:
        params["hemi"] = hemi
    if n_intermed_surfs is not None:
        params["n_intermed_surfs"] = n_intermed_surfs
    if surf_a is not None:
        params["surf_a"] = surf_a
    if surf_b is not None:
        params["surf_b"] = surf_b
    if surf_intermed_pref is not None:
        params["surf_intermed_pref"] = surf_intermed_pref
    return params


def surf_layers_cargs(
    params: SurfLayersParameters,
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
    cargs.append("SurfLayers")
    if params.get("spec_dset") is not None:
        cargs.extend([
            "-spec",
            execution.input_file(params.get("spec_dset"))
        ])
    if params.get("outdir") is not None:
        cargs.extend([
            "-outdir",
            params.get("outdir")
        ])
    if params.get("states") is not None:
        cargs.extend([
            "-states",
            params.get("states")
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "-hemi",
            params.get("hemi")
        ])
    if params.get("n_intermed_surfs") is not None:
        cargs.extend([
            "-n_intermed_surfs",
            str(params.get("n_intermed_surfs"))
        ])
    if params.get("surf_a") is not None:
        cargs.extend([
            "-surf_A",
            execution.input_file(params.get("surf_a"))
        ])
    if params.get("surf_b") is not None:
        cargs.extend([
            "-surf_B",
            execution.input_file(params.get("surf_b"))
        ])
    if params.get("surf_intermed_pref") is not None:
        cargs.extend([
            "-surf_intermed_pref",
            params.get("surf_intermed_pref")
        ])
    if params.get("echo"):
        cargs.append("-echo")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    return cargs


def surf_layers_outputs(
    params: SurfLayersParameters,
    execution: Execution,
) -> SurfLayersOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfLayersOutputs(
        root=execution.output_file("."),
        interpolated_surfaces=execution.output_file(params.get("outdir") + "/isurf." + params.get("hemi") + ".*.gii") if (params.get("outdir") is not None and params.get("hemi") is not None) else None,
        additional_spec_files=execution.output_file(params.get("outdir") + "/*") if (params.get("outdir") is not None) else None,
        run_view_script=execution.output_file(params.get("outdir") + "/run*tcsh") if (params.get("outdir") is not None) else None,
    )
    return ret


def surf_layers_execute(
    params: SurfLayersParameters,
    execution: Execution,
) -> SurfLayersOutputs:
    """
    Compute intermediate equi-distant surfaces between two boundary surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfLayersOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surf_layers_cargs(params, execution)
    ret = surf_layers_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_layers(
    spec_dset: InputPathType | None = None,
    outdir: str | None = None,
    states: str | None = None,
    hemi: str | None = None,
    n_intermed_surfs: float | None = None,
    surf_a: InputPathType | None = None,
    surf_b: InputPathType | None = None,
    surf_intermed_pref: str | None = None,
    echo: bool = False,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> SurfLayersOutputs:
    """
    Compute intermediate equi-distant surfaces between two boundary surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec_dset: Dataset that is the SUMA specification file describing input\
            surfaces.
        outdir: New directory for output (default: surflayers).
        states: Typically smoothwm, pial states to describe inner and outer\
            surfaces (default: 'smoothwm pial').
        hemi: Choose hemisphere: 'lh', 'rh', or 'lh rh' (for both).
        n_intermed_surfs: Total number of intermediate surfaces to create.
        surf_a: Inner boundary surface by filename (e.g., smoothwm.gii).
        surf_b: Outer boundary surface by filename (e.g., pial.gii).
        surf_intermed_pref: Name for interpolated surfaces (default: isurf).
        echo: Run script with 'set echo' (i.e., verbosely).
        no_clean: Do not remove temp files (probably just for testing).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfLayersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_LAYERS_METADATA)
    params = surf_layers_params(spec_dset=spec_dset, outdir=outdir, states=states, hemi=hemi, n_intermed_surfs=n_intermed_surfs, surf_a=surf_a, surf_b=surf_b, surf_intermed_pref=surf_intermed_pref, echo=echo, no_clean=no_clean)
    return surf_layers_execute(params, execution)


__all__ = [
    "SURF_LAYERS_METADATA",
    "SurfLayersOutputs",
    "SurfLayersParameters",
    "surf_layers",
    "surf_layers_params",
]
