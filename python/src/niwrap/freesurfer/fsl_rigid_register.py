# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_RIGID_REGISTER_METADATA = Metadata(
    id="86ae5f77c79298b854bf775bed382049d793e4ae.boutiques",
    name="fsl_rigid_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FslRigidRegisterParameters = typing.TypedDict('FslRigidRegisterParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_rigid_register"],
    "refvol": InputPathType,
    "inputvol": InputPathType,
    "outputvol": str,
    "fslmat": typing.NotRequired[str | None],
    "regmat": typing.NotRequired[str | None],
    "xfmmat": typing.NotRequired[str | None],
    "ltamat": typing.NotRequired[str | None],
    "noinitgeom": bool,
    "applyxfm": typing.NotRequired[InputPathType | None],
    "applyinitxfm": bool,
    "initxfm": typing.NotRequired[InputPathType | None],
    "maxangle": typing.NotRequired[float | None],
    "interp": typing.NotRequired[str | None],
    "dof": typing.NotRequired[float | None],
    "bins": typing.NotRequired[float | None],
    "cost": typing.NotRequired[str | None],
    "tmpdir": typing.NotRequired[str | None],
    "nocleanup": bool,
    "cleanup": bool,
    "subject": typing.NotRequired[str | None],
    "version": bool,
    "help": bool,
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
        "fsl_rigid_register": fsl_rigid_register_cargs,
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
        "fsl_rigid_register": fsl_rigid_register_outputs,
    }.get(t)


class FslRigidRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_rigid_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fslmat_output: OutputPathType
    """The registration matrix in FSL format."""


def fsl_rigid_register_params(
    refvol: InputPathType,
    inputvol: InputPathType,
    outputvol: str,
    fslmat: str | None = None,
    regmat: str | None = None,
    xfmmat: str | None = None,
    ltamat: str | None = None,
    noinitgeom: bool = False,
    applyxfm: InputPathType | None = None,
    applyinitxfm: bool = False,
    initxfm: InputPathType | None = None,
    maxangle: float | None = None,
    interp: str | None = None,
    dof: float | None = None,
    bins: float | None = None,
    cost: str | None = None,
    tmpdir: str | None = None,
    nocleanup: bool = False,
    cleanup: bool = False,
    subject: str | None = None,
    version: bool = False,
    help_: bool = False,
) -> FslRigidRegisterParameters:
    """
    Build parameters.
    
    Args:
        refvol: Reference/Target volume.
        inputvol: Input/Moveable volume.
        outputvol: Input resampled to reference.
        fslmat: Specifies explicitly where to store the FSL registration\
            matrix.
        regmat: Get registration matrix in register.dat file format.
        xfmmat: Get registration matrix as MNI xfm file.
        ltamat: Get registration matrix as MGH lta file.
        noinitgeom: Do not initialize matrix based on geometry.
        applyxfm: Apply a transformation file to the input without\
            registration.
        applyinitxfm: Apply initial transformation to the input without\
            registration.
        initxfm: Use this as an initial matrix for registration.
        maxangle: Only search over +/- max angle degrees.
        interp: Interpolation method: trilinear, nearestneighbour, sinc.
        dof: Use degrees of freedom instead of 6.
        bins: Number of bins to use (default 256).
        cost: Objective function: mutualinfo, corratio (default), normcorr,\
            normmi, leastsq.
        tmpdir: Specify temporary directory.
        nocleanup: Do not delete temporary files.
        cleanup: Delete temporary files (default).
        subject: Only puts it in the register.dat file.
        version: Print version and exit.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_rigid_register",
        "refvol": refvol,
        "inputvol": inputvol,
        "outputvol": outputvol,
        "noinitgeom": noinitgeom,
        "applyinitxfm": applyinitxfm,
        "nocleanup": nocleanup,
        "cleanup": cleanup,
        "version": version,
        "help": help_,
    }
    if fslmat is not None:
        params["fslmat"] = fslmat
    if regmat is not None:
        params["regmat"] = regmat
    if xfmmat is not None:
        params["xfmmat"] = xfmmat
    if ltamat is not None:
        params["ltamat"] = ltamat
    if applyxfm is not None:
        params["applyxfm"] = applyxfm
    if initxfm is not None:
        params["initxfm"] = initxfm
    if maxangle is not None:
        params["maxangle"] = maxangle
    if interp is not None:
        params["interp"] = interp
    if dof is not None:
        params["dof"] = dof
    if bins is not None:
        params["bins"] = bins
    if cost is not None:
        params["cost"] = cost
    if tmpdir is not None:
        params["tmpdir"] = tmpdir
    if subject is not None:
        params["subject"] = subject
    return params


def fsl_rigid_register_cargs(
    params: FslRigidRegisterParameters,
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
    cargs.append("fsl_rigid_register")
    cargs.extend([
        "-r",
        execution.input_file(params.get("refvol"))
    ])
    cargs.extend([
        "-i",
        execution.input_file(params.get("inputvol"))
    ])
    cargs.extend([
        "-o",
        params.get("outputvol")
    ])
    if params.get("fslmat") is not None:
        cargs.extend([
            "-fslmat",
            params.get("fslmat")
        ])
    if params.get("regmat") is not None:
        cargs.extend([
            "-regmat",
            params.get("regmat")
        ])
    if params.get("xfmmat") is not None:
        cargs.extend([
            "-xfmmat",
            params.get("xfmmat")
        ])
    if params.get("ltamat") is not None:
        cargs.extend([
            "-ltamat",
            params.get("ltamat")
        ])
    if params.get("noinitgeom"):
        cargs.append("-noinitgeom")
    if params.get("applyxfm") is not None:
        cargs.extend([
            "-applyxfm",
            execution.input_file(params.get("applyxfm"))
        ])
    if params.get("applyinitxfm"):
        cargs.append("-applyinitxfm")
    if params.get("initxfm") is not None:
        cargs.extend([
            "-initxfm",
            execution.input_file(params.get("initxfm"))
        ])
    if params.get("maxangle") is not None:
        cargs.extend([
            "-maxangle",
            str(params.get("maxangle"))
        ])
    if params.get("interp") is not None:
        cargs.extend([
            "-interp",
            params.get("interp")
        ])
    if params.get("dof") is not None:
        cargs.extend([
            "-dof",
            str(params.get("dof"))
        ])
    if params.get("bins") is not None:
        cargs.extend([
            "-bins",
            str(params.get("bins"))
        ])
    if params.get("cost") is not None:
        cargs.extend([
            "-cost",
            params.get("cost")
        ])
    if params.get("tmpdir") is not None:
        cargs.extend([
            "-tmpdir",
            params.get("tmpdir")
        ])
    if params.get("nocleanup"):
        cargs.append("-nocleanup")
    if params.get("cleanup"):
        cargs.append("-cleanup")
    if params.get("subject") is not None:
        cargs.extend([
            "-subject",
            params.get("subject")
        ])
    if params.get("version"):
        cargs.append("-version")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def fsl_rigid_register_outputs(
    params: FslRigidRegisterParameters,
    execution: Execution,
) -> FslRigidRegisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslRigidRegisterOutputs(
        root=execution.output_file("."),
        fslmat_output=execution.output_file(params.get("outputvol") + ".fslmat"),
    )
    return ret


def fsl_rigid_register_execute(
    params: FslRigidRegisterParameters,
    execution: Execution,
) -> FslRigidRegisterOutputs:
    """
    A front-end tool for FSL's FLIRT that computes a rigid registration matrix and
    resamples the input volume to the reference volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslRigidRegisterOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsl_rigid_register_cargs(params, execution)
    ret = fsl_rigid_register_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_rigid_register(
    refvol: InputPathType,
    inputvol: InputPathType,
    outputvol: str,
    fslmat: str | None = None,
    regmat: str | None = None,
    xfmmat: str | None = None,
    ltamat: str | None = None,
    noinitgeom: bool = False,
    applyxfm: InputPathType | None = None,
    applyinitxfm: bool = False,
    initxfm: InputPathType | None = None,
    maxangle: float | None = None,
    interp: str | None = None,
    dof: float | None = None,
    bins: float | None = None,
    cost: str | None = None,
    tmpdir: str | None = None,
    nocleanup: bool = False,
    cleanup: bool = False,
    subject: str | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> FslRigidRegisterOutputs:
    """
    A front-end tool for FSL's FLIRT that computes a rigid registration matrix and
    resamples the input volume to the reference volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        refvol: Reference/Target volume.
        inputvol: Input/Moveable volume.
        outputvol: Input resampled to reference.
        fslmat: Specifies explicitly where to store the FSL registration\
            matrix.
        regmat: Get registration matrix in register.dat file format.
        xfmmat: Get registration matrix as MNI xfm file.
        ltamat: Get registration matrix as MGH lta file.
        noinitgeom: Do not initialize matrix based on geometry.
        applyxfm: Apply a transformation file to the input without\
            registration.
        applyinitxfm: Apply initial transformation to the input without\
            registration.
        initxfm: Use this as an initial matrix for registration.
        maxangle: Only search over +/- max angle degrees.
        interp: Interpolation method: trilinear, nearestneighbour, sinc.
        dof: Use degrees of freedom instead of 6.
        bins: Number of bins to use (default 256).
        cost: Objective function: mutualinfo, corratio (default), normcorr,\
            normmi, leastsq.
        tmpdir: Specify temporary directory.
        nocleanup: Do not delete temporary files.
        cleanup: Delete temporary files (default).
        subject: Only puts it in the register.dat file.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslRigidRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_RIGID_REGISTER_METADATA)
    params = fsl_rigid_register_params(refvol=refvol, inputvol=inputvol, outputvol=outputvol, fslmat=fslmat, regmat=regmat, xfmmat=xfmmat, ltamat=ltamat, noinitgeom=noinitgeom, applyxfm=applyxfm, applyinitxfm=applyinitxfm, initxfm=initxfm, maxangle=maxangle, interp=interp, dof=dof, bins=bins, cost=cost, tmpdir=tmpdir, nocleanup=nocleanup, cleanup=cleanup, subject=subject, version=version, help_=help_)
    return fsl_rigid_register_execute(params, execution)


__all__ = [
    "FSL_RIGID_REGISTER_METADATA",
    "FslRigidRegisterOutputs",
    "FslRigidRegisterParameters",
    "fsl_rigid_register",
    "fsl_rigid_register_params",
]
