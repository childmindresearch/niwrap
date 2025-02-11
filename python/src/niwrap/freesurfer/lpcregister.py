# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LPCREGISTER_METADATA = Metadata(
    id="e5a5971735d364dfe8f37cf7d53f26828a5b15b4.boutiques",
    name="lpcregister",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
LpcregisterParameters = typing.TypedDict('LpcregisterParameters', {
    "__STYX_TYPE__": typing.Literal["lpcregister"],
    "subject_id": str,
    "mov_volume": str,
    "reg_file": str,
    "dof_9": bool,
    "dof_12": bool,
    "frame_number": typing.NotRequired[float | None],
    "mid_frame": bool,
    "fsvol": typing.NotRequired[str | None],
    "output_volume": typing.NotRequired[str | None],
    "tmp_dir": typing.NotRequired[str | None],
    "no_cleanup": bool,
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
        "lpcregister": lpcregister_cargs,
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
        "lpcregister": lpcregister_outputs,
    }.get(t)


class LpcregisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `lpcregister(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_reg_file: OutputPathType
    """Output registration file in FreeSurfer format."""
    resampled_volume: OutputPathType | None
    """The resampled movable volume if --o is specified."""


def lpcregister_params(
    subject_id: str,
    mov_volume: str,
    reg_file: str,
    dof_9: bool = False,
    dof_12: bool = False,
    frame_number: float | None = None,
    mid_frame: bool = False,
    fsvol: str | None = None,
    output_volume: str | None = None,
    tmp_dir: str | None = None,
    no_cleanup: bool = False,
    version: bool = False,
    help_: bool = False,
) -> LpcregisterParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject ID found in SUBJECTS_DIR. The reference volume is\
            the mri/brain volume (modifiable with --fsvol). Converted to analyze\
            using mri_convert.
        mov_volume: Volume identifier of the movable volume. Must be specified\
            suitably for mri_convert. Uses first frame unless --frame is specified.
        reg_file: Output registration file mapping RAS in the reference to RAS\
            in the movable. The file/matrix format is understood by freesurfer.
        dof_9: Use 9 degrees of freedom; default is 6.
        dof_12: Use 12 degrees of freedom; default is 6.
        frame_number: Specify the frame number other than the first. For SPM\
            analyze, specify the file corresponding to the desired frame as each\
            file only has one frame.
        mid_frame: Register to the middle frame of the mov volume as the\
            template. Cannot be used with --frame.
        fsvol: Use FreeSurfer volume id; default is brainmask.
        output_volume: Output volume file for resampled mov.
        tmp_dir: Specify temporary directory (implies --nocleanup).
        no_cleanup: Do not delete temporary files.
        version: Print the version and exit.
        help_: Print help information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "lpcregister",
        "subject_id": subject_id,
        "mov_volume": mov_volume,
        "reg_file": reg_file,
        "dof_9": dof_9,
        "dof_12": dof_12,
        "mid_frame": mid_frame,
        "no_cleanup": no_cleanup,
        "version": version,
        "help": help_,
    }
    if frame_number is not None:
        params["frame_number"] = frame_number
    if fsvol is not None:
        params["fsvol"] = fsvol
    if output_volume is not None:
        params["output_volume"] = output_volume
    if tmp_dir is not None:
        params["tmp_dir"] = tmp_dir
    return params


def lpcregister_cargs(
    params: LpcregisterParameters,
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
    cargs.append("lpcregister")
    cargs.extend([
        "--s",
        params.get("subject_id")
    ])
    cargs.extend([
        "--mov",
        params.get("mov_volume")
    ])
    cargs.extend([
        "--reg",
        params.get("reg_file")
    ])
    if params.get("dof_9"):
        cargs.append("--9")
    if params.get("dof_12"):
        cargs.append("--12")
    if params.get("frame_number") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame_number"))
        ])
    if params.get("mid_frame"):
        cargs.append("--mid-frame")
    if params.get("fsvol") is not None:
        cargs.extend([
            "--fsvol",
            params.get("fsvol")
        ])
    if params.get("output_volume") is not None:
        cargs.extend([
            "--o",
            params.get("output_volume")
        ])
    if params.get("tmp_dir") is not None:
        cargs.extend([
            "--tmp",
            params.get("tmp_dir")
        ])
    if params.get("no_cleanup"):
        cargs.append("--nocleanup")
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def lpcregister_outputs(
    params: LpcregisterParameters,
    execution: Execution,
) -> LpcregisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LpcregisterOutputs(
        root=execution.output_file("."),
        output_reg_file=execution.output_file("register.dat"),
        resampled_volume=execution.output_file(params.get("output_volume")) if (params.get("output_volume") is not None) else None,
    )
    return ret


def lpcregister_execute(
    params: LpcregisterParameters,
    execution: Execution,
) -> LpcregisterOutputs:
    """
    Registers a volume to its FreeSurfer anatomical using Local Pearson Correlation
    (LPC) (the AFNI lpc_align.py program). Creates a FreeSurfer register.dat file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LpcregisterOutputs`).
    """
    cargs = lpcregister_cargs(params, execution)
    ret = lpcregister_outputs(params, execution)
    execution.run(cargs)
    return ret


def lpcregister(
    subject_id: str,
    mov_volume: str,
    reg_file: str,
    dof_9: bool = False,
    dof_12: bool = False,
    frame_number: float | None = None,
    mid_frame: bool = False,
    fsvol: str | None = None,
    output_volume: str | None = None,
    tmp_dir: str | None = None,
    no_cleanup: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> LpcregisterOutputs:
    """
    Registers a volume to its FreeSurfer anatomical using Local Pearson Correlation
    (LPC) (the AFNI lpc_align.py program). Creates a FreeSurfer register.dat file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject ID found in SUBJECTS_DIR. The reference volume is\
            the mri/brain volume (modifiable with --fsvol). Converted to analyze\
            using mri_convert.
        mov_volume: Volume identifier of the movable volume. Must be specified\
            suitably for mri_convert. Uses first frame unless --frame is specified.
        reg_file: Output registration file mapping RAS in the reference to RAS\
            in the movable. The file/matrix format is understood by freesurfer.
        dof_9: Use 9 degrees of freedom; default is 6.
        dof_12: Use 12 degrees of freedom; default is 6.
        frame_number: Specify the frame number other than the first. For SPM\
            analyze, specify the file corresponding to the desired frame as each\
            file only has one frame.
        mid_frame: Register to the middle frame of the mov volume as the\
            template. Cannot be used with --frame.
        fsvol: Use FreeSurfer volume id; default is brainmask.
        output_volume: Output volume file for resampled mov.
        tmp_dir: Specify temporary directory (implies --nocleanup).
        no_cleanup: Do not delete temporary files.
        version: Print the version and exit.
        help_: Print help information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LpcregisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LPCREGISTER_METADATA)
    params = lpcregister_params(subject_id=subject_id, mov_volume=mov_volume, reg_file=reg_file, dof_9=dof_9, dof_12=dof_12, frame_number=frame_number, mid_frame=mid_frame, fsvol=fsvol, output_volume=output_volume, tmp_dir=tmp_dir, no_cleanup=no_cleanup, version=version, help_=help_)
    return lpcregister_execute(params, execution)


__all__ = [
    "LPCREGISTER_METADATA",
    "LpcregisterOutputs",
    "LpcregisterParameters",
    "lpcregister",
    "lpcregister_params",
]
