# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_LABEL_IMPORT_METADATA = Metadata(
    id="dde3112ce19a06b1bb86a1f6f785ca6b9271992e.boutiques",
    name="volume-label-import",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeLabelImportParameters = typing.TypedDict('VolumeLabelImportParameters', {
    "__STYX_TYPE__": typing.Literal["volume-label-import"],
    "input": InputPathType,
    "label_list_file": str,
    "output": str,
    "opt_discard_others": bool,
    "opt_unlabeled_value_value": typing.NotRequired[int | None],
    "opt_subvolume_subvol": typing.NotRequired[str | None],
    "opt_drop_unused_labels": bool,
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
        "volume-label-import": volume_label_import_cargs,
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
        "volume-label-import": volume_label_import_outputs,
    }.get(t)


class VolumeLabelImportOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_import(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output workbench label volume"""


def volume_label_import_params(
    input_: InputPathType,
    label_list_file: str,
    output: str,
    opt_discard_others: bool = False,
    opt_unlabeled_value_value: int | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_drop_unused_labels: bool = False,
) -> VolumeLabelImportParameters:
    """
    Build parameters.
    
    Args:
        input_: the input volume file.
        label_list_file: text file containing the values and names for labels.
        output: the output workbench label volume.
        opt_discard_others: set any voxels with values not mentioned in the\
            label list to the ??? label.
        opt_unlabeled_value_value: set the value that will be interpreted as\
            unlabeled: the numeric value for unlabeled (default 0).
        opt_subvolume_subvol: select a single subvolume to import: the\
            subvolume number or name.
        opt_drop_unused_labels: remove any unused label values from the label\
            table.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-label-import",
        "input": input_,
        "label_list_file": label_list_file,
        "output": output,
        "opt_discard_others": opt_discard_others,
        "opt_drop_unused_labels": opt_drop_unused_labels,
    }
    if opt_unlabeled_value_value is not None:
        params["opt_unlabeled_value_value"] = opt_unlabeled_value_value
    if opt_subvolume_subvol is not None:
        params["opt_subvolume_subvol"] = opt_subvolume_subvol
    return params


def volume_label_import_cargs(
    params: VolumeLabelImportParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-label-import")
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("label_list_file"))
    cargs.append(params.get("output"))
    if params.get("opt_discard_others"):
        cargs.append("-discard-others")
    if params.get("opt_unlabeled_value_value") is not None:
        cargs.extend([
            "-unlabeled-value",
            str(params.get("opt_unlabeled_value_value"))
        ])
    if params.get("opt_subvolume_subvol") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvol")
        ])
    if params.get("opt_drop_unused_labels"):
        cargs.append("-drop-unused-labels")
    return cargs


def volume_label_import_outputs(
    params: VolumeLabelImportParameters,
    execution: Execution,
) -> VolumeLabelImportOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeLabelImportOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def volume_label_import_execute(
    params: VolumeLabelImportParameters,
    execution: Execution,
) -> VolumeLabelImportOutputs:
    """
    Import a label volume to workbench format.
    
    Creates a label volume from an integer-valued volume file. The label name
    and color information is stored in the volume header in a nifti extension,
    with a similar format as in caret5, see -volume-help. You may specify the
    empty string (use "") for <label-list-file>, which will be treated as if it
    is an empty file. The label list file must have the following format (2
    lines per label):
    
    <labelname>
    <key> <red> <green> <blue> <alpha>
    ...
    
    Label names are specified on a separate line from their value and color, in
    order to let label names contain spaces. Whitespace is trimmed from both
    ends of the label name, but is kept if it is in the middle of a label. Do
    not specify the "unlabeled" key in the file, it is assumed that 0 means not
    labeled unless -unlabeled-value is specified. The value of <key> specifies
    what value in the imported file should be used as this label (these same key
    values are also used in the output file). The values of <red>, <green>,
    <blue> and <alpha> must be integers from 0 to 255, and will specify the
    color the label is drawn as (alpha of 255 means fully opaque, which is
    probably what you want).
    
    By default, it will create new label names with names like LABEL_5 for any
    values encountered that are not mentioned in the list file, specify
    -discard-others to instead set these values to the "unlabeled" key.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelImportOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = volume_label_import_cargs(params, execution)
    ret = volume_label_import_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_label_import(
    input_: InputPathType,
    label_list_file: str,
    output: str,
    opt_discard_others: bool = False,
    opt_unlabeled_value_value: int | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_drop_unused_labels: bool = False,
    runner: Runner | None = None,
) -> VolumeLabelImportOutputs:
    """
    Import a label volume to workbench format.
    
    Creates a label volume from an integer-valued volume file. The label name
    and color information is stored in the volume header in a nifti extension,
    with a similar format as in caret5, see -volume-help. You may specify the
    empty string (use "") for <label-list-file>, which will be treated as if it
    is an empty file. The label list file must have the following format (2
    lines per label):
    
    <labelname>
    <key> <red> <green> <blue> <alpha>
    ...
    
    Label names are specified on a separate line from their value and color, in
    order to let label names contain spaces. Whitespace is trimmed from both
    ends of the label name, but is kept if it is in the middle of a label. Do
    not specify the "unlabeled" key in the file, it is assumed that 0 means not
    labeled unless -unlabeled-value is specified. The value of <key> specifies
    what value in the imported file should be used as this label (these same key
    values are also used in the output file). The values of <red>, <green>,
    <blue> and <alpha> must be integers from 0 to 255, and will specify the
    color the label is drawn as (alpha of 255 means fully opaque, which is
    probably what you want).
    
    By default, it will create new label names with names like LABEL_5 for any
    values encountered that are not mentioned in the list file, specify
    -discard-others to instead set these values to the "unlabeled" key.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_: the input volume file.
        label_list_file: text file containing the values and names for labels.
        output: the output workbench label volume.
        opt_discard_others: set any voxels with values not mentioned in the\
            label list to the ??? label.
        opt_unlabeled_value_value: set the value that will be interpreted as\
            unlabeled: the numeric value for unlabeled (default 0).
        opt_subvolume_subvol: select a single subvolume to import: the\
            subvolume number or name.
        opt_drop_unused_labels: remove any unused label values from the label\
            table.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelImportOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_IMPORT_METADATA)
    params = volume_label_import_params(input_=input_, label_list_file=label_list_file, output=output, opt_discard_others=opt_discard_others, opt_unlabeled_value_value=opt_unlabeled_value_value, opt_subvolume_subvol=opt_subvolume_subvol, opt_drop_unused_labels=opt_drop_unused_labels)
    return volume_label_import_execute(params, execution)


__all__ = [
    "VOLUME_LABEL_IMPORT_METADATA",
    "VolumeLabelImportOutputs",
    "VolumeLabelImportParameters",
    "volume_label_import",
    "volume_label_import_params",
]
