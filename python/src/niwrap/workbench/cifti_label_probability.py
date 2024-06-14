# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CIFTI_LABEL_PROBABILITY_METADATA = Metadata(
    id="e43d37fd5a640c812f6bd48c8ee4a67decd06f70",
    name="cifti-label-probability",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiLabelProbabilityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_probability(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    probability_dscalar_out: OutputPathType
    """the relative frequencies of each label at each vertex/voxel"""


def cifti_label_probability(
    label_maps: InputPathType,
    probability_dscalar_out: InputPathType,
    opt_exclude_unlabeled: bool = False,
    runner: Runner = None,
) -> CiftiLabelProbabilityOutputs:
    """
    cifti-label-probability by Washington University School of Medicin.
    
    Find frequency of cifti labels.
    
    This command outputs a set of soft ROIs, one for each label in the input,
    where the value is how many of the input maps had that label at that
    vertex/voxel, divided by the number of input maps.
    
    Args:
        label_maps: cifti dlabel file containing individual label maps from\
            many subjects.
        probability_dscalar_out: the relative frequencies of each label at each\
            vertex/voxel.
        opt_exclude_unlabeled: don't make a probability map of the unlabeled\
            key.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelProbabilityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_PROBABILITY_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-probability")
    cargs.append(execution.input_file(label_maps))
    cargs.append(execution.input_file(probability_dscalar_out))
    if opt_exclude_unlabeled:
        cargs.append("-exclude-unlabeled")
    ret = CiftiLabelProbabilityOutputs(
        root=execution.output_file("."),
        probability_dscalar_out=execution.output_file(f"{pathlib.Path(probability_dscalar_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_LABEL_PROBABILITY_METADATA",
    "CiftiLabelProbabilityOutputs",
    "cifti_label_probability",
]