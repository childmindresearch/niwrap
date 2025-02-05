# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA = Metadata(
    id="56ab9aee6d0be0b2fb7ecc7bcc331cfd24c3bb57.boutiques",
    name="cifti-parcel-mapping-to-label",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiParcelMappingToLabelParameters = typing.TypedDict('CiftiParcelMappingToLabelParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-parcel-mapping-to-label"],
    "cifti_in": InputPathType,
    "direction": str,
    "template_cifti": InputPathType,
    "dlabel_out": str,
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
        "cifti-parcel-mapping-to-label": cifti_parcel_mapping_to_label_cargs,
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
        "cifti-parcel-mapping-to-label": cifti_parcel_mapping_to_label_outputs,
    }
    return vt.get(t)


class CiftiParcelMappingToLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_parcel_mapping_to_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dlabel_out: OutputPathType
    """the output dense label file"""


def cifti_parcel_mapping_to_label_params(
    cifti_in: InputPathType,
    direction: str,
    template_cifti: InputPathType,
    dlabel_out: str,
) -> CiftiParcelMappingToLabelParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the input parcellated file.
        direction: which dimension to take the parcel map from, ROW or COLUMN.
        template_cifti: a cifti file with the desired dense mapping along\
            column.
        dlabel_out: the output dense label file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-parcel-mapping-to-label",
        "cifti_in": cifti_in,
        "direction": direction,
        "template_cifti": template_cifti,
        "dlabel_out": dlabel_out,
    }
    return params


def cifti_parcel_mapping_to_label_cargs(
    params: CiftiParcelMappingToLabelParameters,
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
    cargs.append("-cifti-parcel-mapping-to-label")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(params.get("direction"))
    cargs.append(execution.input_file(params.get("template_cifti")))
    cargs.append(params.get("dlabel_out"))
    return cargs


def cifti_parcel_mapping_to_label_outputs(
    params: CiftiParcelMappingToLabelParameters,
    execution: Execution,
) -> CiftiParcelMappingToLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiParcelMappingToLabelOutputs(
        root=execution.output_file("."),
        dlabel_out=execution.output_file(params.get("dlabel_out")),
    )
    return ret


def cifti_parcel_mapping_to_label_execute(
    params: CiftiParcelMappingToLabelParameters,
    execution: Execution,
) -> CiftiParcelMappingToLabelOutputs:
    """
    Create dlabel from parcellated file.
    
    This command will output a dlabel file, useful for doing the same
    parcellation to another dense file.
    
    For ptseries, pscalar, plabel, pconn, and pdconn, using COLUMN for
    <direction> will work.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiParcelMappingToLabelOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_parcel_mapping_to_label_cargs(params, execution)
    ret = cifti_parcel_mapping_to_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_parcel_mapping_to_label(
    cifti_in: InputPathType,
    direction: str,
    template_cifti: InputPathType,
    dlabel_out: str,
    runner: Runner | None = None,
) -> CiftiParcelMappingToLabelOutputs:
    """
    Create dlabel from parcellated file.
    
    This command will output a dlabel file, useful for doing the same
    parcellation to another dense file.
    
    For ptseries, pscalar, plabel, pconn, and pdconn, using COLUMN for
    <direction> will work.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the input parcellated file.
        direction: which dimension to take the parcel map from, ROW or COLUMN.
        template_cifti: a cifti file with the desired dense mapping along\
            column.
        dlabel_out: the output dense label file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiParcelMappingToLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA)
    params = cifti_parcel_mapping_to_label_params(cifti_in=cifti_in, direction=direction, template_cifti=template_cifti, dlabel_out=dlabel_out)
    return cifti_parcel_mapping_to_label_execute(params, execution)


__all__ = [
    "CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA",
    "CiftiParcelMappingToLabelOutputs",
    "CiftiParcelMappingToLabelParameters",
    "cifti_parcel_mapping_to_label",
    "cifti_parcel_mapping_to_label_params",
]
