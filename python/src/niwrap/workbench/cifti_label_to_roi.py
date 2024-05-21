# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_LABEL_TO_ROI_METADATA = Metadata(
    id="2dcb8e83a8a5c7e84c4bae72bcadbbcdb4676796",
    name="cifti-label-to-roi",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiLabelToRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_to_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    scalar_out: OutputPathType
    """the output cifti scalar file"""


def cifti_label_to_roi(
    label_in: InputPathType,
    scalar_out: InputPathType,
    opt_name_label_name: str | None = None,
    opt_key_label_key: float | int | None = None,
    opt_map_map: str | None = None,
    runner: Runner = None,
) -> CiftiLabelToRoiOutputs:
    """
    cifti-label-to-roi by Washington University School of Medicin.
    
    MAKE A CIFTI LABEL INTO AN ROI.
    
    For each map in <label-in>, a map is created in <scalar-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Args:
        label_in: the input cifti label file
        scalar_out: the output cifti scalar file
        opt_name_label_name: select label by name: the label name that you want
            an roi of
        opt_key_label_key: select label by key: the label key that you want an
            roi of
        opt_map_map: select a single label map to use: the map number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiLabelToRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_TO_ROI_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-to-roi")
    cargs.append(execution.input_file(label_in))
    cargs.append(execution.input_file(scalar_out))
    if opt_name_label_name is not None:
        cargs.extend(["-name", opt_name_label_name])
    if opt_key_label_key is not None:
        cargs.extend(["-key", str(opt_key_label_key)])
    if opt_map_map is not None:
        cargs.extend(["-map", opt_map_map])
    ret = CiftiLabelToRoiOutputs(
        root=execution.output_file("."),
        scalar_out=execution.output_file(f"{pathlib.Path(scalar_out).stem}"),
    )
    execution.run(cargs)
    return ret
