# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_PATH2LABEL_METADATA = Metadata(
    id="ac055539c26e5fa7d5b552e4523192ffbd1a7979.boutiques",
    name="mri_path2label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriPath2labelParameters = typing.TypedDict('MriPath2labelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_path2label"],
    "input_file": str,
    "output_file": str,
    "single": bool,
    "path_to_label": bool,
    "label_to_path": bool,
    "connect": typing.NotRequired[list[str] | None],
    "fill": typing.NotRequired[list[str] | None],
    "confillx": typing.NotRequired[list[str] | None],
    "confill": typing.NotRequired[list[str] | None],
    "source_file": typing.NotRequired[str | None],
    "dest_file": typing.NotRequired[str | None],
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
        "mri_path2label": mri_path2label_cargs,
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
        "mri_path2label": mri_path2label_outputs,
    }.get(t)


class MriPath2labelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_path2label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_path2label_params(
    input_file: str,
    output_file: str,
    single: bool = False,
    path_to_label: bool = False,
    label_to_path: bool = False,
    connect: list[str] | None = None,
    fill: list[str] | None = None,
    confillx: list[str] | None = None,
    confill: list[str] | None = None,
    source_file: str | None = None,
    dest_file: str | None = None,
) -> MriPath2labelParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file, either a path or label file.
        output_file: Output file, either a path or label file.
        single: Only convert a single path, and do not use sentinel values.
        path_to_label: Treat input as a path and output a label.
        label_to_path: Treat input as a label and output a path.
        connect: Connect path; input and output must be paths; requires subject\
            and hemi.
        fill: Fill already closed, connected path; input must be a path, output\
            must be a label; requires subject, hemi, and seedvtx.
        confillx: Connect and fill path; input must be a path, output must be a\
            label; requires surface_fname and seedvtx.
        confill: Connect and fill path; input must be a path, output must be a\
            label; requires subject, hemi, and seedvtx.
        source_file: The path file, if path2label.
        dest_file: The label file, if path2label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_path2label",
        "input_file": input_file,
        "output_file": output_file,
        "single": single,
        "path_to_label": path_to_label,
        "label_to_path": label_to_path,
    }
    if connect is not None:
        params["connect"] = connect
    if fill is not None:
        params["fill"] = fill
    if confillx is not None:
        params["confillx"] = confillx
    if confill is not None:
        params["confill"] = confill
    if source_file is not None:
        params["source_file"] = source_file
    if dest_file is not None:
        params["dest_file"] = dest_file
    return params


def mri_path2label_cargs(
    params: MriPath2labelParameters,
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
    cargs.append("mri_path2label")
    cargs.append(params.get("input_file"))
    cargs.append(params.get("output_file"))
    if params.get("single"):
        cargs.append("--single")
    if params.get("path_to_label"):
        cargs.append("--path2label")
    if params.get("label_to_path"):
        cargs.append("--label2path")
    if params.get("connect") is not None:
        cargs.extend([
            "--connect",
            *params.get("connect")
        ])
    if params.get("fill") is not None:
        cargs.extend([
            "--fill",
            *params.get("fill")
        ])
    if params.get("confillx") is not None:
        cargs.extend([
            "--confillx",
            *params.get("confillx")
        ])
    if params.get("confill") is not None:
        cargs.extend([
            "--confill",
            *params.get("confill")
        ])
    if params.get("source_file") is not None:
        cargs.extend([
            "--i",
            params.get("source_file")
        ])
    if params.get("dest_file") is not None:
        cargs.extend([
            "--o",
            params.get("dest_file")
        ])
    return cargs


def mri_path2label_outputs(
    params: MriPath2labelParameters,
    execution: Execution,
) -> MriPath2labelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriPath2labelOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_path2label_execute(
    params: MriPath2labelParameters,
    execution: Execution,
) -> MriPath2labelOutputs:
    """
    Converts a path file to a label or a label file to a path file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriPath2labelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_path2label_cargs(params, execution)
    ret = mri_path2label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_path2label(
    input_file: str,
    output_file: str,
    single: bool = False,
    path_to_label: bool = False,
    label_to_path: bool = False,
    connect: list[str] | None = None,
    fill: list[str] | None = None,
    confillx: list[str] | None = None,
    confill: list[str] | None = None,
    source_file: str | None = None,
    dest_file: str | None = None,
    runner: Runner | None = None,
) -> MriPath2labelOutputs:
    """
    Converts a path file to a label or a label file to a path file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input file, either a path or label file.
        output_file: Output file, either a path or label file.
        single: Only convert a single path, and do not use sentinel values.
        path_to_label: Treat input as a path and output a label.
        label_to_path: Treat input as a label and output a path.
        connect: Connect path; input and output must be paths; requires subject\
            and hemi.
        fill: Fill already closed, connected path; input must be a path, output\
            must be a label; requires subject, hemi, and seedvtx.
        confillx: Connect and fill path; input must be a path, output must be a\
            label; requires surface_fname and seedvtx.
        confill: Connect and fill path; input must be a path, output must be a\
            label; requires subject, hemi, and seedvtx.
        source_file: The path file, if path2label.
        dest_file: The label file, if path2label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriPath2labelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PATH2LABEL_METADATA)
    params = mri_path2label_params(input_file=input_file, output_file=output_file, single=single, path_to_label=path_to_label, label_to_path=label_to_path, connect=connect, fill=fill, confillx=confillx, confill=confill, source_file=source_file, dest_file=dest_file)
    return mri_path2label_execute(params, execution)


__all__ = [
    "MRI_PATH2LABEL_METADATA",
    "MriPath2labelOutputs",
    "MriPath2labelParameters",
    "mri_path2label",
    "mri_path2label_params",
]
