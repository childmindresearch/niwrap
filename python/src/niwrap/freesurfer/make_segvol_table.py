# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_SEGVOL_TABLE_METADATA = Metadata(
    id="584e18cf5964aa90ad96025eab578f07dcec865b.boutiques",
    name="make-segvol-table",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MakeSegvolTableParameters = typing.TypedDict('MakeSegvolTableParameters', {
    "__STYX_TYPE__": typing.Literal["make-segvol-table"],
    "subjects": list[str],
    "subject_file": InputPathType,
    "outfile": str,
    "idmap": typing.NotRequired[InputPathType | None],
    "structure_ids": typing.NotRequired[list[str] | None],
    "segdir": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
    "umask": typing.NotRequired[str | None],
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
        "make-segvol-table": make_segvol_table_cargs,
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
        "make-segvol-table": make_segvol_table_outputs,
    }.get(t)


class MakeSegvolTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_segvol_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_table: OutputPathType
    """Output text file containing the table of subcortical structure
    volumes."""


def make_segvol_table_params(
    subjects: list[str],
    subject_file: InputPathType,
    outfile: str,
    idmap: InputPathType | None = None,
    structure_ids: list[str] | None = None,
    segdir: str | None = None,
    subjects_dir: str | None = None,
    umask: str | None = None,
    version: bool = False,
    help_: bool = False,
) -> MakeSegvolTableParameters:
    """
    Build parameters.
    
    Args:
        subjects: List of subject IDs. Each subject should be specified with a\
            separate -s flag.
        subject_file: Path to a file containing a list of subjects.
        outfile: Output file where the table will be saved.
        idmap: File with structure name and id number. Default is\
            FREESURFER_HOME/tkmeditColorsCMA.
        structure_ids: Names of structures to include in the table. Defaults to\
            all structures.
        segdir: Segmentation subdirectory name. Default is 'aseg'.
        subjects_dir: Path to the subjects directory. Default is SUBJECTS_DIR\
            environment variable.
        umask: Set UNIX file permission mask.
        version: Print version and exit.
        help_: Display help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make-segvol-table",
        "subjects": subjects,
        "subject_file": subject_file,
        "outfile": outfile,
        "version": version,
        "help": help_,
    }
    if idmap is not None:
        params["idmap"] = idmap
    if structure_ids is not None:
        params["structure_ids"] = structure_ids
    if segdir is not None:
        params["segdir"] = segdir
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if umask is not None:
        params["umask"] = umask
    return params


def make_segvol_table_cargs(
    params: MakeSegvolTableParameters,
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
    cargs.append("make-segvol-table")
    cargs.extend([
        "-s",
        *params.get("subjects")
    ])
    cargs.extend([
        "-sf",
        execution.input_file(params.get("subject_file"))
    ])
    cargs.extend([
        "-o",
        params.get("outfile")
    ])
    if params.get("idmap") is not None:
        cargs.extend([
            "-idmap",
            execution.input_file(params.get("idmap"))
        ])
    if params.get("structure_ids") is not None:
        cargs.extend([
            "-id",
            *params.get("structure_ids")
        ])
    if params.get("segdir") is not None:
        cargs.extend([
            "-segdir",
            params.get("segdir")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-sd",
            params.get("subjects_dir")
        ])
    if params.get("umask") is not None:
        cargs.extend([
            "-umask",
            params.get("umask")
        ])
    if params.get("version"):
        cargs.append("-version")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def make_segvol_table_outputs(
    params: MakeSegvolTableParameters,
    execution: Execution,
) -> MakeSegvolTableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeSegvolTableOutputs(
        root=execution.output_file("."),
        output_table=execution.output_file(params.get("outfile")),
    )
    return ret


def make_segvol_table_execute(
    params: MakeSegvolTableParameters,
    execution: Execution,
) -> MakeSegvolTableOutputs:
    """
    Creates a table of volumes of subcortical structures for a given list of
    subjects using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeSegvolTableOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = make_segvol_table_cargs(params, execution)
    ret = make_segvol_table_outputs(params, execution)
    execution.run(cargs)
    return ret


def make_segvol_table(
    subjects: list[str],
    subject_file: InputPathType,
    outfile: str,
    idmap: InputPathType | None = None,
    structure_ids: list[str] | None = None,
    segdir: str | None = None,
    subjects_dir: str | None = None,
    umask: str | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MakeSegvolTableOutputs:
    """
    Creates a table of volumes of subcortical structures for a given list of
    subjects using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subject IDs. Each subject should be specified with a\
            separate -s flag.
        subject_file: Path to a file containing a list of subjects.
        outfile: Output file where the table will be saved.
        idmap: File with structure name and id number. Default is\
            FREESURFER_HOME/tkmeditColorsCMA.
        structure_ids: Names of structures to include in the table. Defaults to\
            all structures.
        segdir: Segmentation subdirectory name. Default is 'aseg'.
        subjects_dir: Path to the subjects directory. Default is SUBJECTS_DIR\
            environment variable.
        umask: Set UNIX file permission mask.
        version: Print version and exit.
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeSegvolTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_SEGVOL_TABLE_METADATA)
    params = make_segvol_table_params(subjects=subjects, subject_file=subject_file, outfile=outfile, idmap=idmap, structure_ids=structure_ids, segdir=segdir, subjects_dir=subjects_dir, umask=umask, version=version, help_=help_)
    return make_segvol_table_execute(params, execution)


__all__ = [
    "MAKE_SEGVOL_TABLE_METADATA",
    "MakeSegvolTableOutputs",
    "MakeSegvolTableParameters",
    "make_segvol_table",
    "make_segvol_table_params",
]
