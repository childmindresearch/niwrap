# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_AFNITO_ANALYZE_METADATA = Metadata(
    id="8e009ca0525a816d98d8d648c7fbae2324df58e2.boutiques",
    name="3dAFNItoANALYZE",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAfnitoAnalyzeParameters = typing.TypedDict('V3dAfnitoAnalyzeParameters', {
    "__STYX_TYPE__": typing.Literal["3dAFNItoANALYZE"],
    "4d_option": bool,
    "orient_option": typing.NotRequired[str | None],
    "output_name": str,
    "afni_dataset": InputPathType,
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
        "3dAFNItoANALYZE": v_3d_afnito_analyze_cargs,
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
        "3dAFNItoANALYZE": v_3d_afnito_analyze_outputs,
    }
    return vt.get(t)


class V3dAfnitoAnalyzeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_afnito_analyze(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_hdr_file: OutputPathType
    """ANALYZE header file for each sub-brick"""
    output_img_file: OutputPathType
    """ANALYZE image file for each sub-brick"""
    output_4d_hdr_file: OutputPathType
    """Single ANALYZE header file if using -4D option"""
    output_4d_img_file: OutputPathType
    """Single ANALYZE image file if using -4D option"""


def v_3d_afnito_analyze_params(
    output_name: str,
    afni_dataset: InputPathType,
    v_4d_option: bool = False,
    orient_option: str | None = None,
) -> V3dAfnitoAnalyzeParameters:
    """
    Build parameters.
    
    Args:
        output_name: Output ANALYZE file base name (e.g., aname).
        afni_dataset: Input AFNI dataset.
        v_4d_option: Write all data to one big ANALYZE file pair named\
            aname.hdr/aname.img.
        orient_option: Flip the dataset to a different orientation when writing\
            to ANALYZE files (e.g., LPI).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dAFNItoANALYZE",
        "4d_option": v_4d_option,
        "output_name": output_name,
        "afni_dataset": afni_dataset,
    }
    if orient_option is not None:
        params["orient_option"] = orient_option
    return params


def v_3d_afnito_analyze_cargs(
    params: V3dAfnitoAnalyzeParameters,
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
    cargs.append("3dAFNItoANALYZE")
    if params.get("4d_option"):
        cargs.append("-4D")
    if params.get("orient_option") is not None:
        cargs.extend([
            "-orient",
            params.get("orient_option")
        ])
    cargs.append(params.get("output_name"))
    cargs.append(execution.input_file(params.get("afni_dataset")))
    return cargs


def v_3d_afnito_analyze_outputs(
    params: V3dAfnitoAnalyzeParameters,
    execution: Execution,
) -> V3dAfnitoAnalyzeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAfnitoAnalyzeOutputs(
        root=execution.output_file("."),
        output_hdr_file=execution.output_file(params.get("output_name") + "_[INDEX].hdr"),
        output_img_file=execution.output_file(params.get("output_name") + "_[INDEX].img"),
        output_4d_hdr_file=execution.output_file(params.get("output_name") + ".hdr"),
        output_4d_img_file=execution.output_file(params.get("output_name") + ".img"),
    )
    return ret


def v_3d_afnito_analyze_execute(
    params: V3dAfnitoAnalyzeParameters,
    execution: Execution,
) -> V3dAfnitoAnalyzeOutputs:
    """
    Writes AFNI dataset to ANALYZE 7.5 format .hdr/.img file pairs.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoAnalyzeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_afnito_analyze_cargs(params, execution)
    ret = v_3d_afnito_analyze_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_afnito_analyze(
    output_name: str,
    afni_dataset: InputPathType,
    v_4d_option: bool = False,
    orient_option: str | None = None,
    runner: Runner | None = None,
) -> V3dAfnitoAnalyzeOutputs:
    """
    Writes AFNI dataset to ANALYZE 7.5 format .hdr/.img file pairs.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        output_name: Output ANALYZE file base name (e.g., aname).
        afni_dataset: Input AFNI dataset.
        v_4d_option: Write all data to one big ANALYZE file pair named\
            aname.hdr/aname.img.
        orient_option: Flip the dataset to a different orientation when writing\
            to ANALYZE files (e.g., LPI).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoAnalyzeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AFNITO_ANALYZE_METADATA)
    params = v_3d_afnito_analyze_params(v_4d_option=v_4d_option, orient_option=orient_option, output_name=output_name, afni_dataset=afni_dataset)
    return v_3d_afnito_analyze_execute(params, execution)


__all__ = [
    "V3dAfnitoAnalyzeOutputs",
    "V3dAfnitoAnalyzeParameters",
    "V_3D_AFNITO_ANALYZE_METADATA",
    "v_3d_afnito_analyze",
    "v_3d_afnito_analyze_params",
]
