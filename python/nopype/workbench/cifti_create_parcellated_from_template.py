# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:56.004276

import typing

from ..styxdefs import *


CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA = Metadata(
    id="fa6ba63e581f13ad8fa42b68527d270d22985ae6",
    name="cifti-create-parcellated-from-template",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiCreateParcellatedFromTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_parcellated_from_template(...)`.
    """
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_parcellated_from_template(
    runner: Runner,
    cifti_template: InputPathType,
    modify_direction: str,
    cifti_out: InputPathType,
    opt_fill_value_value: float | int | None = None,
    opt_cifti_cifti_in: InputPathType | None = None,
) -> CiftiCreateParcellatedFromTemplateOutputs:
    """
    MATCH PARCELS TO TEMPLATE BY NAME.
    
    For each parcel name in the template mapping, find that name in an input
    cifti file and use its data in the output file. All input cifti files must
    have a parcels mapping along <modify-direction> and matching mappings along
    other dimensions. The direction can be either an integer starting from 1, or
    the strings 'ROW' or 'COLUMN'.
    
    Args:
        runner: Command runner
        cifti_template: a cifti file with the template parcel mapping along
            column
        modify_direction: which dimension of the output file should match the
            template (integer, 'ROW', or 'COLUMN')
        cifti_out: the output cifti file
        opt_fill_value_value: specify value to be used in parcels that don't
            match: value to use (default 0)
        opt_cifti_cifti_in: specify an input cifti file: the input parcellated
            cifti file
    Returns:
        NamedTuple of outputs (described in `CiftiCreateParcellatedFromTemplateOutputs`).
    """
    execution = runner.start_execution(CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-parcellated-from-template")
    cargs.append(execution.input_file(cifti_template))
    cargs.append(modify_direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_fill_value_value is not None:
        cargs.extend(["-fill-value", str(opt_fill_value_value)])
    if opt_cifti_cifti_in is not None:
        cargs.extend(["-cifti", execution.input_file(opt_cifti_cifti_in)])
    ret = CiftiCreateParcellatedFromTemplateOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret
