# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SIMULATE_MOTION_METADATA = Metadata(
    id="5fc17ce508dbb62923e813f5cff61e70e1accb2d.boutiques",
    name="@simulate_motion",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VSimulateMotionParameters = typing.TypedDict('VSimulateMotionParameters', {
    "__STYX_TYPE__": typing.Literal["@simulate_motion"],
    "epi": InputPathType,
    "motion_file": InputPathType,
    "epi_timing": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "save_workdir": bool,
    "test": bool,
    "verb_level": typing.NotRequired[float | None],
    "vr_base": typing.NotRequired[float | None],
    "warp_method": typing.NotRequired[str | None],
    "warp_1D": typing.NotRequired[InputPathType | None],
    "warp_master": typing.NotRequired[InputPathType | None],
    "wsinc5": bool,
    "help": bool,
    "hist": bool,
    "todo": bool,
    "ver": bool,
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
        "@simulate_motion": v__simulate_motion_cargs,
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
        "@simulate_motion": v__simulate_motion_outputs,
    }.get(t)


class VSimulateMotionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__simulate_motion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    simulated_motion_output: OutputPathType | None
    """Motion simulated EPI time series"""


def v__simulate_motion_params(
    epi: InputPathType,
    motion_file: InputPathType,
    epi_timing: InputPathType | None = None,
    prefix: str | None = None,
    save_workdir: bool = False,
    test: bool = False,
    verb_level: float | None = None,
    vr_base: float | None = None,
    warp_method: str | None = None,
    warp_1_d: InputPathType | None = None,
    warp_master: InputPathType | None = None,
    wsinc5: bool = False,
    help_: bool = False,
    hist: bool = False,
    todo: bool = False,
    ver: bool = False,
) -> VSimulateMotionParameters:
    """
    Build parameters.
    
    Args:
        epi: Input EPI volume or time series (only a volreg base is needed,\
            though more is okay).
        motion_file: Motion parameter file (as output by 3dvolreg).
        epi_timing: Provide EPI dataset with slice timing.
        prefix: Prefix for data results (default = motion_sim.NUM_TRS).
        save_workdir: Do not remove the 'work' directory.
        test: Only test running the program, do not create a simulated motion\
            dataset.
        verb_level: Specify a verbose level (default = 1).
        vr_base: 0-based index of volreg base in EPI dataset.
        warp_method: Specify a method for forward alignment/transform.
        warp_1_d: Specify a 12 parameter affine transformation.
        warp_master: Specify a grid master dataset for the -warp_1D transform.
        wsinc5: Use wsinc5 interpolation in 3dAllineate.
        help_: Show help message.
        hist: Show program modification history.
        todo: Show current todo list.
        ver: Show program version.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@simulate_motion",
        "epi": epi,
        "motion_file": motion_file,
        "save_workdir": save_workdir,
        "test": test,
        "wsinc5": wsinc5,
        "help": help_,
        "hist": hist,
        "todo": todo,
        "ver": ver,
    }
    if epi_timing is not None:
        params["epi_timing"] = epi_timing
    if prefix is not None:
        params["prefix"] = prefix
    if verb_level is not None:
        params["verb_level"] = verb_level
    if vr_base is not None:
        params["vr_base"] = vr_base
    if warp_method is not None:
        params["warp_method"] = warp_method
    if warp_1_d is not None:
        params["warp_1D"] = warp_1_d
    if warp_master is not None:
        params["warp_master"] = warp_master
    return params


def v__simulate_motion_cargs(
    params: VSimulateMotionParameters,
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
    cargs.append("@simulate_motion")
    cargs.extend([
        "-epi",
        execution.input_file(params.get("epi"))
    ])
    cargs.extend([
        "-motion_file",
        execution.input_file(params.get("motion_file"))
    ])
    if params.get("epi_timing") is not None:
        cargs.extend([
            "-epi_timing",
            execution.input_file(params.get("epi_timing"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("save_workdir"):
        cargs.append("-save_workdir")
    if params.get("test"):
        cargs.append("-test")
    if params.get("verb_level") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verb_level"))
        ])
    if params.get("vr_base") is not None:
        cargs.extend([
            "-vr_base",
            str(params.get("vr_base"))
        ])
    if params.get("warp_method") is not None:
        cargs.extend([
            "-warp_method",
            params.get("warp_method")
        ])
    if params.get("warp_1D") is not None:
        cargs.extend([
            "-warp_1D",
            execution.input_file(params.get("warp_1D"))
        ])
    if params.get("warp_master") is not None:
        cargs.extend([
            "-warp_master",
            execution.input_file(params.get("warp_master"))
        ])
    if params.get("wsinc5"):
        cargs.append("-wsinc5")
    if params.get("help"):
        cargs.append("-help")
    if params.get("hist"):
        cargs.append("-hist")
    if params.get("todo"):
        cargs.append("-todo")
    if params.get("ver"):
        cargs.append("-ver")
    return cargs


def v__simulate_motion_outputs(
    params: VSimulateMotionParameters,
    execution: Execution,
) -> VSimulateMotionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSimulateMotionOutputs(
        root=execution.output_file("."),
        simulated_motion_output=execution.output_file(params.get("prefix") + "_simulated_motion.nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def v__simulate_motion_execute(
    params: VSimulateMotionParameters,
    execution: Execution,
) -> VSimulateMotionOutputs:
    """
    Create simulated motion time series in an EPI dataset based on the provided
    motion parameters and an input volume.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSimulateMotionOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__simulate_motion_cargs(params, execution)
    ret = v__simulate_motion_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__simulate_motion(
    epi: InputPathType,
    motion_file: InputPathType,
    epi_timing: InputPathType | None = None,
    prefix: str | None = None,
    save_workdir: bool = False,
    test: bool = False,
    verb_level: float | None = None,
    vr_base: float | None = None,
    warp_method: str | None = None,
    warp_1_d: InputPathType | None = None,
    warp_master: InputPathType | None = None,
    wsinc5: bool = False,
    help_: bool = False,
    hist: bool = False,
    todo: bool = False,
    ver: bool = False,
    runner: Runner | None = None,
) -> VSimulateMotionOutputs:
    """
    Create simulated motion time series in an EPI dataset based on the provided
    motion parameters and an input volume.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        epi: Input EPI volume or time series (only a volreg base is needed,\
            though more is okay).
        motion_file: Motion parameter file (as output by 3dvolreg).
        epi_timing: Provide EPI dataset with slice timing.
        prefix: Prefix for data results (default = motion_sim.NUM_TRS).
        save_workdir: Do not remove the 'work' directory.
        test: Only test running the program, do not create a simulated motion\
            dataset.
        verb_level: Specify a verbose level (default = 1).
        vr_base: 0-based index of volreg base in EPI dataset.
        warp_method: Specify a method for forward alignment/transform.
        warp_1_d: Specify a 12 parameter affine transformation.
        warp_master: Specify a grid master dataset for the -warp_1D transform.
        wsinc5: Use wsinc5 interpolation in 3dAllineate.
        help_: Show help message.
        hist: Show program modification history.
        todo: Show current todo list.
        ver: Show program version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSimulateMotionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SIMULATE_MOTION_METADATA)
    params = v__simulate_motion_params(epi=epi, motion_file=motion_file, epi_timing=epi_timing, prefix=prefix, save_workdir=save_workdir, test=test, verb_level=verb_level, vr_base=vr_base, warp_method=warp_method, warp_1_d=warp_1_d, warp_master=warp_master, wsinc5=wsinc5, help_=help_, hist=hist, todo=todo, ver=ver)
    return v__simulate_motion_execute(params, execution)


__all__ = [
    "VSimulateMotionOutputs",
    "VSimulateMotionParameters",
    "V__SIMULATE_MOTION_METADATA",
    "v__simulate_motion",
    "v__simulate_motion_params",
]
