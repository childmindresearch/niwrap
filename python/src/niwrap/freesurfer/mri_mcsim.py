# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_MCSIM_METADATA = Metadata(
    id="c93d6e308a5345c3826d6a5f805dbcd44a658fe1.boutiques",
    name="mri_mcsim",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriMcsimParameters = typing.TypedDict('MriMcsimParameters', {
    "__STYX_TYPE__": typing.Literal["mri_mcsim"],
    "top_output_dir": str,
    "base_name": str,
    "surface": list[str],
    "num_repetitions": float,
    "fwhm_values": typing.NotRequired[list[float] | None],
    "fwhm_max": typing.NotRequired[float | None],
    "avg_vertex_area": bool,
    "random_seed": typing.NotRequired[float | None],
    "label_file": typing.NotRequired[InputPathType | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "no_label": bool,
    "no_save_mask": bool,
    "surface_name": typing.NotRequired[str | None],
    "log_file": typing.NotRequired[str | None],
    "done_file": typing.NotRequired[str | None],
    "stop_file": typing.NotRequired[str | None],
    "save_file": typing.NotRequired[str | None],
    "save_iter": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "debug": bool,
    "check_opts": bool,
    "help": bool,
    "version": bool,
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
        "mri_mcsim": mri_mcsim_cargs,
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
        "mri_mcsim": mri_mcsim_outputs,
    }.get(t)


class MriMcsimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_mcsim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    csd_output: OutputPathType
    """Output CSD files based on the base name"""
    done_output: OutputPathType | None
    """Done file created upon completion"""
    iteration_save: OutputPathType | None
    """Iteration save file"""
    log_output: OutputPathType | None
    """Log file generated during execution"""


def mri_mcsim_params(
    top_output_dir: str,
    base_name: str,
    surface: list[str],
    num_repetitions: float,
    fwhm_values: list[float] | None = None,
    fwhm_max: float | None = None,
    avg_vertex_area: bool = False,
    random_seed: float | None = None,
    label_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    no_label: bool = False,
    no_save_mask: bool = False,
    surface_name: str | None = None,
    log_file: str | None = None,
    done_file: str | None = None,
    stop_file: str | None = None,
    save_file: str | None = None,
    save_iter: bool = False,
    subjects_dir: str | None = None,
    debug: bool = False,
    check_opts: bool = False,
    help_: bool = False,
    version: bool = False,
) -> MriMcsimParameters:
    """
    Build parameters.
    
    Args:
        top_output_dir: Top output directory.
        base_name: Base name for CSD files.
        surface: Subject name and hemisphere for the surface (e.g., subjectname\
            lh).
        num_repetitions: Number of repetitions for the simulation.
        fwhm_values: Full Width at Half Maximum values for smoothing.
        fwhm_max: Maximum FWHM for simulation (default 30).
        avg_vertex_area: Report cluster area based on average vertex area.
        random_seed: Random seed value (default is based on Time of Day).
        label_file: Label file for masking (default is ?h.cortex.label).
        mask_file: Mask file instead of label.
        no_label: Do not use a label to mask.
        no_save_mask: Do not save mask to output.
        surface_name: Surface name (default is white).
        log_file: Log file for the output.
        done_file: Done file to create when finished.
        stop_file: Stop file (default is ourdir/mri_mcsim.stop).
        save_file: Save file (default is ourdir/mri_mcsim.save).
        save_iter: Save output after each iteration.
        subjects_dir: Subjects directory.
        debug: Turn on debugging.
        check_opts: Check options do not run.
        help_: Display help message.
        version: Display version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_mcsim",
        "top_output_dir": top_output_dir,
        "base_name": base_name,
        "surface": surface,
        "num_repetitions": num_repetitions,
        "avg_vertex_area": avg_vertex_area,
        "no_label": no_label,
        "no_save_mask": no_save_mask,
        "save_iter": save_iter,
        "debug": debug,
        "check_opts": check_opts,
        "help": help_,
        "version": version,
    }
    if fwhm_values is not None:
        params["fwhm_values"] = fwhm_values
    if fwhm_max is not None:
        params["fwhm_max"] = fwhm_max
    if random_seed is not None:
        params["random_seed"] = random_seed
    if label_file is not None:
        params["label_file"] = label_file
    if mask_file is not None:
        params["mask_file"] = mask_file
    if surface_name is not None:
        params["surface_name"] = surface_name
    if log_file is not None:
        params["log_file"] = log_file
    if done_file is not None:
        params["done_file"] = done_file
    if stop_file is not None:
        params["stop_file"] = stop_file
    if save_file is not None:
        params["save_file"] = save_file
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    return params


def mri_mcsim_cargs(
    params: MriMcsimParameters,
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
    cargs.append("mri_mcsim")
    cargs.extend([
        "--o",
        params.get("top_output_dir")
    ])
    cargs.extend([
        "--base",
        params.get("base_name")
    ])
    cargs.extend([
        "--surface",
        *params.get("surface")
    ])
    cargs.extend([
        "--nreps",
        str(params.get("num_repetitions"))
    ])
    if params.get("fwhm_values") is not None:
        cargs.extend([
            "--fwhm",
            *map(str, params.get("fwhm_values"))
        ])
    if params.get("fwhm_max") is not None:
        cargs.extend([
            "--fwhm-max",
            str(params.get("fwhm_max"))
        ])
    if params.get("avg_vertex_area"):
        cargs.append("--avgvtxarea")
    if params.get("random_seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("random_seed"))
        ])
    if params.get("label_file") is not None:
        cargs.extend([
            "--label",
            execution.input_file(params.get("label_file"))
        ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("no_label"):
        cargs.append("--no-label")
    if params.get("no_save_mask"):
        cargs.append("--no-save-mask")
    if params.get("surface_name") is not None:
        cargs.extend([
            "--surfname",
            params.get("surface_name")
        ])
    if params.get("log_file") is not None:
        cargs.extend([
            "--log",
            params.get("log_file")
        ])
    if params.get("done_file") is not None:
        cargs.extend([
            "--done",
            params.get("done_file")
        ])
    if params.get("stop_file") is not None:
        cargs.extend([
            "--stop",
            params.get("stop_file")
        ])
    if params.get("save_file") is not None:
        cargs.extend([
            "--save",
            params.get("save_file")
        ])
    if params.get("save_iter"):
        cargs.append("--save-iter")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("check_opts"):
        cargs.append("--checkopts")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mri_mcsim_outputs(
    params: MriMcsimParameters,
    execution: Execution,
) -> MriMcsimOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMcsimOutputs(
        root=execution.output_file("."),
        csd_output=execution.output_file(params.get("top_output_dir") + "/" + params.get("base_name") + ".csd"),
        done_output=execution.output_file(params.get("top_output_dir") + "/done/" + params.get("done_file")) if (params.get("done_file") is not None) else None,
        iteration_save=execution.output_file(params.get("top_output_dir") + "/" + params.get("save_file")) if (params.get("save_file") is not None) else None,
        log_output=execution.output_file(params.get("top_output_dir") + "/log/" + params.get("log_file")) if (params.get("log_file") is not None) else None,
    )
    return ret


def mri_mcsim_execute(
    params: MriMcsimParameters,
    execution: Execution,
) -> MriMcsimOutputs:
    """
    Monte Carlo simulation tool for surface-based multiple comparisons.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMcsimOutputs`).
    """
    cargs = mri_mcsim_cargs(params, execution)
    ret = mri_mcsim_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_mcsim(
    top_output_dir: str,
    base_name: str,
    surface: list[str],
    num_repetitions: float,
    fwhm_values: list[float] | None = None,
    fwhm_max: float | None = None,
    avg_vertex_area: bool = False,
    random_seed: float | None = None,
    label_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    no_label: bool = False,
    no_save_mask: bool = False,
    surface_name: str | None = None,
    log_file: str | None = None,
    done_file: str | None = None,
    stop_file: str | None = None,
    save_file: str | None = None,
    save_iter: bool = False,
    subjects_dir: str | None = None,
    debug: bool = False,
    check_opts: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriMcsimOutputs:
    """
    Monte Carlo simulation tool for surface-based multiple comparisons.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        top_output_dir: Top output directory.
        base_name: Base name for CSD files.
        surface: Subject name and hemisphere for the surface (e.g., subjectname\
            lh).
        num_repetitions: Number of repetitions for the simulation.
        fwhm_values: Full Width at Half Maximum values for smoothing.
        fwhm_max: Maximum FWHM for simulation (default 30).
        avg_vertex_area: Report cluster area based on average vertex area.
        random_seed: Random seed value (default is based on Time of Day).
        label_file: Label file for masking (default is ?h.cortex.label).
        mask_file: Mask file instead of label.
        no_label: Do not use a label to mask.
        no_save_mask: Do not save mask to output.
        surface_name: Surface name (default is white).
        log_file: Log file for the output.
        done_file: Done file to create when finished.
        stop_file: Stop file (default is ourdir/mri_mcsim.stop).
        save_file: Save file (default is ourdir/mri_mcsim.save).
        save_iter: Save output after each iteration.
        subjects_dir: Subjects directory.
        debug: Turn on debugging.
        check_opts: Check options do not run.
        help_: Display help message.
        version: Display version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMcsimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MCSIM_METADATA)
    params = mri_mcsim_params(top_output_dir=top_output_dir, base_name=base_name, surface=surface, num_repetitions=num_repetitions, fwhm_values=fwhm_values, fwhm_max=fwhm_max, avg_vertex_area=avg_vertex_area, random_seed=random_seed, label_file=label_file, mask_file=mask_file, no_label=no_label, no_save_mask=no_save_mask, surface_name=surface_name, log_file=log_file, done_file=done_file, stop_file=stop_file, save_file=save_file, save_iter=save_iter, subjects_dir=subjects_dir, debug=debug, check_opts=check_opts, help_=help_, version=version)
    return mri_mcsim_execute(params, execution)


__all__ = [
    "MRI_MCSIM_METADATA",
    "MriMcsimOutputs",
    "MriMcsimParameters",
    "mri_mcsim",
    "mri_mcsim_params",
]
