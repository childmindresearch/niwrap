# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLCHFILETYPE_METADATA = Metadata(
    id="916aef0203b0edb3702a23c5484e8e0a82f6b98d.boutiques",
    name="fslchfiletype",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslchfiletypeParameters = typing.TypedDict('FslchfiletypeParameters', {
    "__STYX_TYPE__": typing.Literal["fslchfiletype"],
    "filetype": str,
    "filename": InputPathType,
    "filename2": typing.NotRequired[str | None],
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
        "fslchfiletype": fslchfiletype_cargs,
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
        "fslchfiletype": fslchfiletype_outputs,
    }.get(t)


class FslchfiletypeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslchfiletype(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Output file with the new file type."""


def fslchfiletype_params(
    filetype: str,
    filename: InputPathType,
    filename2: str | None = None,
) -> FslchfiletypeParameters:
    """
    Build parameters.
    
    Args:
        filetype: The type of the file to convert to. Valid values include:\
            ANALYZE, ANALYZE_GZ, NIFTI, NIFTI_GZ, NIFTI_PAIR, NIFTI_PAIR_GZ,\
            NIFTI2, NIFTI2_GZ, NIFTI2_PAIR, NIFTI2_PAIR_GZ.
        filename: The name of the input image file.
        filename2: The name of the output image file (optional).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslchfiletype",
        "filetype": filetype,
        "filename": filename,
    }
    if filename2 is not None:
        params["filename2"] = filename2
    return params


def fslchfiletype_cargs(
    params: FslchfiletypeParameters,
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
    cargs.append("fslchfiletype")
    cargs.append(params.get("filetype"))
    cargs.append(execution.input_file(params.get("filename")))
    if params.get("filename2") is not None:
        cargs.append(params.get("filename2"))
    return cargs


def fslchfiletype_outputs(
    params: FslchfiletypeParameters,
    execution: Execution,
) -> FslchfiletypeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslchfiletypeOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("filename2")) if (params.get("filename2") is not None) else None,
    )
    return ret


def fslchfiletype_execute(
    params: FslchfiletypeParameters,
    execution: Execution,
) -> FslchfiletypeOutputs:
    """
    Tool to change the file type of an image file or copy it to a new file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslchfiletypeOutputs`).
    """
    params = execution.params(params)
    cargs = fslchfiletype_cargs(params, execution)
    ret = fslchfiletype_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslchfiletype(
    filetype: str,
    filename: InputPathType,
    filename2: str | None = None,
    runner: Runner | None = None,
) -> FslchfiletypeOutputs:
    """
    Tool to change the file type of an image file or copy it to a new file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        filetype: The type of the file to convert to. Valid values include:\
            ANALYZE, ANALYZE_GZ, NIFTI, NIFTI_GZ, NIFTI_PAIR, NIFTI_PAIR_GZ,\
            NIFTI2, NIFTI2_GZ, NIFTI2_PAIR, NIFTI2_PAIR_GZ.
        filename: The name of the input image file.
        filename2: The name of the output image file (optional).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslchfiletypeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCHFILETYPE_METADATA)
    params = fslchfiletype_params(filetype=filetype, filename=filename, filename2=filename2)
    return fslchfiletype_execute(params, execution)


__all__ = [
    "FSLCHFILETYPE_METADATA",
    "FslchfiletypeOutputs",
    "FslchfiletypeParameters",
    "fslchfiletype",
    "fslchfiletype_params",
]
