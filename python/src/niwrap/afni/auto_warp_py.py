# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AUTO_WARP_PY_METADATA = Metadata(
    id="a6e140162bdb60ac7b3f82c488330c94eee4e2ab.boutiques",
    name="auto_warp.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AutoWarpPyParameters = typing.TypedDict('AutoWarpPyParameters', {
    "__STYX_TYPE__": typing.Literal["auto_warp.py"],
    "base": InputPathType,
    "input": InputPathType,
    "skull_strip_input": bool,
    "qblur": typing.NotRequired[str | None],
    "qworkhard": typing.NotRequired[str | None],
    "qw_opts": typing.NotRequired[str | None],
    "keep_rm_files": bool,
    "prep_only": bool,
    "help": bool,
    "hview": bool,
    "limited_help": bool,
    "option_help": bool,
    "version": bool,
    "ver": bool,
    "verb": bool,
    "save_script": bool,
    "skip_affine": bool,
    "skull_strip_base": bool,
    "ex_mode": typing.NotRequired[str | None],
    "overwrite": bool,
    "suffix": typing.NotRequired[str | None],
    "child_anat": typing.NotRequired[str | None],
    "warp_dxyz": typing.NotRequired[float | None],
    "affine_dxyz": typing.NotRequired[float | None],
    "affine_input_xmat": typing.NotRequired[str | None],
    "smooth_anat": bool,
    "smooth_base": bool,
    "unifize_input": bool,
    "output_dir": typing.NotRequired[str | None],
    "followers": typing.NotRequired[str | None],
    "affine_followers_xmat": typing.NotRequired[str | None],
    "skullstrip_opts": typing.NotRequired[str | None],
    "at_opts": typing.NotRequired[str | None],
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
        "auto_warp.py": auto_warp_py_cargs,
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


class AutoWarpPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `auto_warp_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def auto_warp_py_params(
    base: InputPathType,
    input_: InputPathType,
    skull_strip_input: bool = False,
    qblur: str | None = None,
    qworkhard: str | None = None,
    qw_opts: str | None = None,
    keep_rm_files: bool = False,
    prep_only: bool = False,
    help_: bool = False,
    hview: bool = False,
    limited_help: bool = False,
    option_help: bool = False,
    version: bool = False,
    ver: bool = False,
    verb: bool = False,
    save_script: bool = False,
    skip_affine: bool = False,
    skull_strip_base: bool = False,
    ex_mode: str | None = None,
    overwrite: bool = False,
    suffix: str | None = None,
    child_anat: str | None = None,
    warp_dxyz: float | None = None,
    affine_dxyz: float | None = None,
    affine_input_xmat: str | None = None,
    smooth_anat: bool = False,
    smooth_base: bool = False,
    unifize_input: bool = False,
    output_dir: str | None = None,
    followers: str | None = None,
    affine_followers_xmat: str | None = None,
    skullstrip_opts: str | None = None,
    at_opts: str | None = None,
) -> AutoWarpPyParameters:
    """
    Build parameters.
    
    Args:
        base: Name of reference or template volume.
        input_: Name of dataset to be registered.
        skull_strip_input: Do not skullstrip input dataset.
        qblur: Specify 3dQwarp blurs for base and source volumes.
        qworkhard: Set the two values for 3dQwarp's -workhard option.
        qw_opts: Pass all of OPTS as extra options directly to 3dQwarp.
        keep_rm_files: Don't delete any of the temporary files created.
        prep_only: Do preprocessing steps only without alignment.
        help_: Display help message.
        hview: Display help message in a text editor.
        limited_help: Display limited help message.
        option_help: Display help for all available options.
        version: Show version number and exit.
        ver: Show version number and exit.
        verb: Be verbose in messages and options.
        save_script: Save executed script in given file.
        skip_affine: Skip the affine registration process.
        skull_strip_base: Do not skullstrip base/template dataset.
        ex_mode: Command execution mode: quiet, echo, dry_run, script.
        overwrite: Overwrite existing files.
        suffix: Suffix to add to output files.
        child_anat: Names of child anatomical datasets.
        warp_dxyz: Resolution used for computing warp (cubic only).
        affine_dxyz: Resolution used for computing initial transform (cubic\
            only).
        affine_input_xmat: Affine transform to put input in standard space.\
            Special values are: 'AUTO' to use @auto_tlrc, 'ID' to do nothing,\
            'FILE.1D' for a pre-computed matrix FILE.1D.
        smooth_anat: Smooth anatomy before registration.
        smooth_base: Smooth template before registration.
        unifize_input: Unifize the input or not.
        output_dir: Set directory for output datasets.
        followers: Specify follower datasets.
        affine_followers_xmat: Specify follower datasets' affine transforms.
        skullstrip_opts: 3dSkullstrip miscellaneous options.
        at_opts: @auto_tlrc miscellaneous options.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "auto_warp.py",
        "base": base,
        "input": input_,
        "skull_strip_input": skull_strip_input,
        "keep_rm_files": keep_rm_files,
        "prep_only": prep_only,
        "help": help_,
        "hview": hview,
        "limited_help": limited_help,
        "option_help": option_help,
        "version": version,
        "ver": ver,
        "verb": verb,
        "save_script": save_script,
        "skip_affine": skip_affine,
        "skull_strip_base": skull_strip_base,
        "overwrite": overwrite,
        "smooth_anat": smooth_anat,
        "smooth_base": smooth_base,
        "unifize_input": unifize_input,
    }
    if qblur is not None:
        params["qblur"] = qblur
    if qworkhard is not None:
        params["qworkhard"] = qworkhard
    if qw_opts is not None:
        params["qw_opts"] = qw_opts
    if ex_mode is not None:
        params["ex_mode"] = ex_mode
    if suffix is not None:
        params["suffix"] = suffix
    if child_anat is not None:
        params["child_anat"] = child_anat
    if warp_dxyz is not None:
        params["warp_dxyz"] = warp_dxyz
    if affine_dxyz is not None:
        params["affine_dxyz"] = affine_dxyz
    if affine_input_xmat is not None:
        params["affine_input_xmat"] = affine_input_xmat
    if output_dir is not None:
        params["output_dir"] = output_dir
    if followers is not None:
        params["followers"] = followers
    if affine_followers_xmat is not None:
        params["affine_followers_xmat"] = affine_followers_xmat
    if skullstrip_opts is not None:
        params["skullstrip_opts"] = skullstrip_opts
    if at_opts is not None:
        params["at_opts"] = at_opts
    return params


def auto_warp_py_cargs(
    params: AutoWarpPyParameters,
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
    cargs.append("auto_warp.py")
    cargs.extend([
        "-base",
        execution.input_file(params.get("base"))
    ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("input"))
    ])
    if params.get("skull_strip_input"):
        cargs.append("-skull_strip_input")
    if params.get("qblur") is not None:
        cargs.extend([
            "-qblur",
            params.get("qblur")
        ])
    if params.get("qworkhard") is not None:
        cargs.extend([
            "-qworkhard",
            params.get("qworkhard")
        ])
    if params.get("qw_opts") is not None:
        cargs.extend([
            "-qw_opts",
            params.get("qw_opts")
        ])
    if params.get("keep_rm_files"):
        cargs.append("-keep_rm_files")
    if params.get("prep_only"):
        cargs.append("-prep_only")
    if params.get("help"):
        cargs.append("-help")
    if params.get("hview"):
        cargs.append("-hview")
    if params.get("limited_help"):
        cargs.append("-limited_help")
    if params.get("option_help"):
        cargs.append("-option_help")
    if params.get("version"):
        cargs.append("-version")
    if params.get("ver"):
        cargs.append("-ver")
    if params.get("verb"):
        cargs.append("-verb")
    if params.get("save_script"):
        cargs.append("-save_script")
    if params.get("skip_affine"):
        cargs.append("-skip_affine")
    if params.get("skull_strip_base"):
        cargs.append("-skull_strip_base")
    if params.get("ex_mode") is not None:
        cargs.extend([
            "-ex_mode",
            params.get("ex_mode")
        ])
    if params.get("overwrite"):
        cargs.append("-overwrite")
    if params.get("suffix") is not None:
        cargs.extend([
            "-suffix",
            params.get("suffix")
        ])
    if params.get("child_anat") is not None:
        cargs.extend([
            "-child_anat",
            params.get("child_anat")
        ])
    if params.get("warp_dxyz") is not None:
        cargs.extend([
            "-warp_dxyz",
            str(params.get("warp_dxyz"))
        ])
    if params.get("affine_dxyz") is not None:
        cargs.extend([
            "-affine_dxyz",
            str(params.get("affine_dxyz"))
        ])
    if params.get("affine_input_xmat") is not None:
        cargs.extend([
            "-affine_input_xmat",
            params.get("affine_input_xmat")
        ])
    if params.get("smooth_anat"):
        cargs.append("-smooth_anat")
    if params.get("smooth_base"):
        cargs.append("-smooth_base")
    if params.get("unifize_input"):
        cargs.append("-unifize_input")
    if params.get("output_dir") is not None:
        cargs.extend([
            "-output_dir",
            params.get("output_dir")
        ])
    if params.get("followers") is not None:
        cargs.extend([
            "-followers",
            params.get("followers")
        ])
    if params.get("affine_followers_xmat") is not None:
        cargs.extend([
            "-affine_followers_xmat",
            params.get("affine_followers_xmat")
        ])
    if params.get("skullstrip_opts") is not None:
        cargs.extend([
            "-skullstrip_opts",
            params.get("skullstrip_opts")
        ])
    if params.get("at_opts") is not None:
        cargs.extend([
            "-at_opts",
            params.get("at_opts")
        ])
    return cargs


def auto_warp_py_outputs(
    params: AutoWarpPyParameters,
    execution: Execution,
) -> AutoWarpPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AutoWarpPyOutputs(
        root=execution.output_file("."),
    )
    return ret


def auto_warp_py_execute(
    params: AutoWarpPyParameters,
    execution: Execution,
) -> AutoWarpPyOutputs:
    """
    Nonlinear registration tool.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AutoWarpPyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = auto_warp_py_cargs(params, execution)
    ret = auto_warp_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def auto_warp_py(
    base: InputPathType,
    input_: InputPathType,
    skull_strip_input: bool = False,
    qblur: str | None = None,
    qworkhard: str | None = None,
    qw_opts: str | None = None,
    keep_rm_files: bool = False,
    prep_only: bool = False,
    help_: bool = False,
    hview: bool = False,
    limited_help: bool = False,
    option_help: bool = False,
    version: bool = False,
    ver: bool = False,
    verb: bool = False,
    save_script: bool = False,
    skip_affine: bool = False,
    skull_strip_base: bool = False,
    ex_mode: str | None = None,
    overwrite: bool = False,
    suffix: str | None = None,
    child_anat: str | None = None,
    warp_dxyz: float | None = None,
    affine_dxyz: float | None = None,
    affine_input_xmat: str | None = None,
    smooth_anat: bool = False,
    smooth_base: bool = False,
    unifize_input: bool = False,
    output_dir: str | None = None,
    followers: str | None = None,
    affine_followers_xmat: str | None = None,
    skullstrip_opts: str | None = None,
    at_opts: str | None = None,
    runner: Runner | None = None,
) -> AutoWarpPyOutputs:
    """
    Nonlinear registration tool.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        base: Name of reference or template volume.
        input_: Name of dataset to be registered.
        skull_strip_input: Do not skullstrip input dataset.
        qblur: Specify 3dQwarp blurs for base and source volumes.
        qworkhard: Set the two values for 3dQwarp's -workhard option.
        qw_opts: Pass all of OPTS as extra options directly to 3dQwarp.
        keep_rm_files: Don't delete any of the temporary files created.
        prep_only: Do preprocessing steps only without alignment.
        help_: Display help message.
        hview: Display help message in a text editor.
        limited_help: Display limited help message.
        option_help: Display help for all available options.
        version: Show version number and exit.
        ver: Show version number and exit.
        verb: Be verbose in messages and options.
        save_script: Save executed script in given file.
        skip_affine: Skip the affine registration process.
        skull_strip_base: Do not skullstrip base/template dataset.
        ex_mode: Command execution mode: quiet, echo, dry_run, script.
        overwrite: Overwrite existing files.
        suffix: Suffix to add to output files.
        child_anat: Names of child anatomical datasets.
        warp_dxyz: Resolution used for computing warp (cubic only).
        affine_dxyz: Resolution used for computing initial transform (cubic\
            only).
        affine_input_xmat: Affine transform to put input in standard space.\
            Special values are: 'AUTO' to use @auto_tlrc, 'ID' to do nothing,\
            'FILE.1D' for a pre-computed matrix FILE.1D.
        smooth_anat: Smooth anatomy before registration.
        smooth_base: Smooth template before registration.
        unifize_input: Unifize the input or not.
        output_dir: Set directory for output datasets.
        followers: Specify follower datasets.
        affine_followers_xmat: Specify follower datasets' affine transforms.
        skullstrip_opts: 3dSkullstrip miscellaneous options.
        at_opts: @auto_tlrc miscellaneous options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AutoWarpPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AUTO_WARP_PY_METADATA)
    params = auto_warp_py_params(base=base, input_=input_, skull_strip_input=skull_strip_input, qblur=qblur, qworkhard=qworkhard, qw_opts=qw_opts, keep_rm_files=keep_rm_files, prep_only=prep_only, help_=help_, hview=hview, limited_help=limited_help, option_help=option_help, version=version, ver=ver, verb=verb, save_script=save_script, skip_affine=skip_affine, skull_strip_base=skull_strip_base, ex_mode=ex_mode, overwrite=overwrite, suffix=suffix, child_anat=child_anat, warp_dxyz=warp_dxyz, affine_dxyz=affine_dxyz, affine_input_xmat=affine_input_xmat, smooth_anat=smooth_anat, smooth_base=smooth_base, unifize_input=unifize_input, output_dir=output_dir, followers=followers, affine_followers_xmat=affine_followers_xmat, skullstrip_opts=skullstrip_opts, at_opts=at_opts)
    return auto_warp_py_execute(params, execution)


__all__ = [
    "AUTO_WARP_PY_METADATA",
    "AutoWarpPyOutputs",
    "auto_warp_py",
    "auto_warp_py_params",
]
