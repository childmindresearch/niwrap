# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BMEDITS2SURF_METADATA = Metadata(
    id="be18624e39ce9efc3a4eb4744be1016b11c9fa5f.boutiques",
    name="bmedits2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Bmedits2surfParameters = typing.TypedDict('Bmedits2surfParameters', {
    "__STYX_TYPE__": typing.Literal["bmedits2surf"],
    "subject": str,
    "self": bool,
    "overwrite": bool,
    "tmp_dir": typing.NotRequired[str | None],
    "cleanup": bool,
    "no_cleanup": bool,
    "debug": bool,
    "left_hemisphere": bool,
    "right_hemisphere": bool,
    "no_surfs": bool,
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
        "bmedits2surf": bmedits2surf_cargs,
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
        "bmedits2surf": bmedits2surf_outputs,
    }
    return vt.get(t)


class Bmedits2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bmedits2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lh_bmerase: OutputPathType
    """Binary mask of erased surface locations for the left hemisphere in
    fsaverage space."""
    rh_bmerase: OutputPathType
    """Binary mask of erased surface locations for the right hemisphere in
    fsaverage space."""
    lh_bmclone: OutputPathType
    """Binary mask of cloned surface locations for the left hemisphere in
    fsaverage space."""
    rh_bmclone: OutputPathType
    """Binary mask of cloned surface locations for the right hemisphere in
    fsaverage space."""
    bmclone_stats: OutputPathType
    """Statistics about the number of voxels cloned."""
    bmerase_stats: OutputPathType
    """Statistics about the number of voxels erased."""


def bmedits2surf_params(
    subject: str,
    self: bool = False,
    overwrite: bool = False,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
    debug: bool = False,
    left_hemisphere: bool = False,
    right_hemisphere: bool = False,
    no_surfs: bool = False,
) -> Bmedits2surfParameters:
    """
    Build parameters.
    
    Args:
        subject: The subject for which the binary map will be computed.
        overwrite: Force overwriting of existing results.
        tmp_dir: Temporary directory.
        cleanup: Clean up temporary files.
        no_cleanup: Do not clean up temporary files.
        debug: Enable debug mode.
        left_hemisphere: Perform operation only on the left hemisphere.
        right_hemisphere: Perform operation only on the right hemisphere.
        no_surfs: Do not compute surfaces, only statistics.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bmedits2surf",
        "subject": subject,
        "self": self,
        "overwrite": overwrite,
        "cleanup": cleanup,
        "no_cleanup": no_cleanup,
        "debug": debug,
        "left_hemisphere": left_hemisphere,
        "right_hemisphere": right_hemisphere,
        "no_surfs": no_surfs,
    }
    if tmp_dir is not None:
        params["tmp_dir"] = tmp_dir
    return params


def bmedits2surf_cargs(
    params: Bmedits2surfParameters,
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
    cargs.append("bmedits2surf")
    cargs.extend([
        "-s",
        "-" + params.get("subject")
    ])
    if params.get("self"):
        cargs.append("--self")
    if params.get("overwrite"):
        cargs.append("--overwrite")
    if params.get("tmp_dir") is not None:
        cargs.extend([
            "--tmp",
            params.get("tmp_dir")
        ])
    if params.get("cleanup"):
        cargs.append("--cleanup")
    if params.get("no_cleanup"):
        cargs.append("--no-cleanup")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("left_hemisphere"):
        cargs.append("--lh")
    if params.get("right_hemisphere"):
        cargs.append("--rh")
    if params.get("no_surfs"):
        cargs.append("--no-surfs")
    return cargs


def bmedits2surf_outputs(
    params: Bmedits2surfParameters,
    execution: Execution,
) -> Bmedits2surfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Bmedits2surfOutputs(
        root=execution.output_file("."),
        lh_bmerase=execution.output_file(params.get("subject") + "/surf/lh.bmerase.fsa.mgh"),
        rh_bmerase=execution.output_file(params.get("subject") + "/surf/rh.bmerase.fsa.mgh"),
        lh_bmclone=execution.output_file(params.get("subject") + "/surf/lh.bmclone.fsa.mgh"),
        rh_bmclone=execution.output_file(params.get("subject") + "/surf/rh.bmclone.fsa.mgh"),
        bmclone_stats=execution.output_file(params.get("subject") + "/stats/bmclone.dat"),
        bmerase_stats=execution.output_file(params.get("subject") + "/stats/bmerase.dat"),
    )
    return ret


def bmedits2surf_execute(
    params: Bmedits2surfParameters,
    execution: Execution,
) -> Bmedits2surfOutputs:
    """
    Computes a binary map of surface locations where the brainmask.mgz has been
    edited.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Bmedits2surfOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = bmedits2surf_cargs(params, execution)
    ret = bmedits2surf_outputs(params, execution)
    execution.run(cargs)
    return ret


def bmedits2surf(
    subject: str,
    self: bool = False,
    overwrite: bool = False,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
    debug: bool = False,
    left_hemisphere: bool = False,
    right_hemisphere: bool = False,
    no_surfs: bool = False,
    runner: Runner | None = None,
) -> Bmedits2surfOutputs:
    """
    Computes a binary map of surface locations where the brainmask.mgz has been
    edited.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject for which the binary map will be computed.
        overwrite: Force overwriting of existing results.
        tmp_dir: Temporary directory.
        cleanup: Clean up temporary files.
        no_cleanup: Do not clean up temporary files.
        debug: Enable debug mode.
        left_hemisphere: Perform operation only on the left hemisphere.
        right_hemisphere: Perform operation only on the right hemisphere.
        no_surfs: Do not compute surfaces, only statistics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Bmedits2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BMEDITS2SURF_METADATA)
    params = bmedits2surf_params(subject=subject, self=self, overwrite=overwrite, tmp_dir=tmp_dir, cleanup=cleanup, no_cleanup=no_cleanup, debug=debug, left_hemisphere=left_hemisphere, right_hemisphere=right_hemisphere, no_surfs=no_surfs)
    return bmedits2surf_execute(params, execution)


__all__ = [
    "BMEDITS2SURF_METADATA",
    "Bmedits2surfOutputs",
    "Bmedits2surfParameters",
    "bmedits2surf",
    "bmedits2surf_params",
]
