# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_RF_LONG_TRAIN_METADATA = Metadata(
    id="6aa2bd3c51dac0579c817b9ebcdd083599ca7cf8.boutiques",
    name="mri_rf_long_train",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriRfLongTrainParameters = typing.TypedDict('MriRfLongTrainParameters', {
    "__STYX_TYPE__": typing.Literal["mri_rf_long_train"],
    "seg_dir": str,
    "xform": str,
    "mask": typing.NotRequired[str | None],
    "node_spacing": typing.NotRequired[float | None],
    "prior_spacing": typing.NotRequired[float | None],
    "input_data": typing.NotRequired[list[str] | None],
    "check": bool,
    "subjects": list[str],
    "output_rfa": str,
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
        "mri_rf_long_train": mri_rf_long_train_cargs,
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
        "mri_rf_long_train": mri_rf_long_train_outputs,
    }
    return vt.get(t)


class MriRfLongTrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_rf_long_train(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_rfa_file: OutputPathType
    """The output RFA file generated by the tool"""


def mri_rf_long_train_params(
    seg_dir: str,
    xform: str,
    subjects: list[str],
    output_rfa: str,
    mask: str | None = None,
    node_spacing: float | None = None,
    prior_spacing: float | None = None,
    input_data: list[str] | None = None,
    check: bool = False,
) -> MriRfLongTrainParameters:
    """
    Build parameters.
    
    Args:
        seg_dir: Path to the segmentation volume directory, relative to\
            $subject/mri.
        xform: Atlas transform path relative to $subject/mri/transforms.
        subjects: List of subjects for training.
        output_rfa: Output RFA filename.
        mask: Volume name to use as a mask, path relative to $subject/mri.
        node_spacing: Spacing of classifiers in canonical space.
        prior_spacing: Spacing of class priors in canonical space.
        input_data: Specify training data, path relative to $subject/mri. Can\
            specify multiple inputs. Defaults to 'orig' if not specified.
        check: Conduct sanity-check of labels for obvious edit errors.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_rf_long_train",
        "seg_dir": seg_dir,
        "xform": xform,
        "check": check,
        "subjects": subjects,
        "output_rfa": output_rfa,
    }
    if mask is not None:
        params["mask"] = mask
    if node_spacing is not None:
        params["node_spacing"] = node_spacing
    if prior_spacing is not None:
        params["prior_spacing"] = prior_spacing
    if input_data is not None:
        params["input_data"] = input_data
    return params


def mri_rf_long_train_cargs(
    params: MriRfLongTrainParameters,
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
    cargs.append("mri_rf_long_train")
    cargs.extend([
        "-seg",
        params.get("seg_dir")
    ])
    cargs.extend([
        "-xform",
        params.get("xform")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            params.get("mask")
        ])
    if params.get("node_spacing") is not None:
        cargs.extend([
            "-node_spacing",
            str(params.get("node_spacing"))
        ])
    if params.get("prior_spacing") is not None:
        cargs.extend([
            "-prior_spacing",
            str(params.get("prior_spacing"))
        ])
    if params.get("input_data") is not None:
        cargs.extend([
            "-input",
            *params.get("input_data")
        ])
    if params.get("check"):
        cargs.append("-check")
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_rfa"))
    return cargs


def mri_rf_long_train_outputs(
    params: MriRfLongTrainParameters,
    execution: Execution,
) -> MriRfLongTrainOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriRfLongTrainOutputs(
        root=execution.output_file("."),
        output_rfa_file=execution.output_file(params.get("output_rfa") + ".rfa"),
    )
    return ret


def mri_rf_long_train_execute(
    params: MriRfLongTrainParameters,
    execution: Execution,
) -> MriRfLongTrainOutputs:
    """
    Trains GCA data with multiple subjects for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriRfLongTrainOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_rf_long_train_cargs(params, execution)
    ret = mri_rf_long_train_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_rf_long_train(
    seg_dir: str,
    xform: str,
    subjects: list[str],
    output_rfa: str,
    mask: str | None = None,
    node_spacing: float | None = None,
    prior_spacing: float | None = None,
    input_data: list[str] | None = None,
    check: bool = False,
    runner: Runner | None = None,
) -> MriRfLongTrainOutputs:
    """
    Trains GCA data with multiple subjects for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        seg_dir: Path to the segmentation volume directory, relative to\
            $subject/mri.
        xform: Atlas transform path relative to $subject/mri/transforms.
        subjects: List of subjects for training.
        output_rfa: Output RFA filename.
        mask: Volume name to use as a mask, path relative to $subject/mri.
        node_spacing: Spacing of classifiers in canonical space.
        prior_spacing: Spacing of class priors in canonical space.
        input_data: Specify training data, path relative to $subject/mri. Can\
            specify multiple inputs. Defaults to 'orig' if not specified.
        check: Conduct sanity-check of labels for obvious edit errors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRfLongTrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RF_LONG_TRAIN_METADATA)
    params = mri_rf_long_train_params(seg_dir=seg_dir, xform=xform, mask=mask, node_spacing=node_spacing, prior_spacing=prior_spacing, input_data=input_data, check=check, subjects=subjects, output_rfa=output_rfa)
    return mri_rf_long_train_execute(params, execution)


__all__ = [
    "MRI_RF_LONG_TRAIN_METADATA",
    "MriRfLongTrainOutputs",
    "MriRfLongTrainParameters",
    "mri_rf_long_train",
    "mri_rf_long_train_params",
]
