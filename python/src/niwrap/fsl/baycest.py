# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BAYCEST_METADATA = Metadata(
    id="ffa911443435512ed82ba839a63fc8ccf60823bc.boutiques",
    name="baycest",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
BaycestParameters = typing.TypedDict('BaycestParameters', {
    "__STYX_TYPE__": typing.Literal["baycest"],
    "data_file": InputPathType,
    "mask_file": InputPathType,
    "output_dir": str,
    "pools_file": InputPathType,
    "spec_file": InputPathType,
    "ptrain_file": InputPathType,
    "spatial_flag": bool,
    "t12prior_flag": bool,
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
        "baycest": baycest_cargs,
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
        "baycest": baycest_outputs,
    }.get(t)


class BaycestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `baycest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Main output file"""


def baycest_params(
    data_file: InputPathType,
    mask_file: InputPathType,
    output_dir: str,
    pools_file: InputPathType,
    spec_file: InputPathType,
    ptrain_file: InputPathType,
    spatial_flag: bool = False,
    t12prior_flag: bool = False,
) -> BaycestParameters:
    """
    Build parameters.
    
    Args:
        data_file: Specify data file (nifti image).
        mask_file: Specify mask file (nifti image).
        output_dir: Specify output directory name.
        pools_file: Specify pools to be included in model (ascii matrix).
        spec_file: Data specification (ascii matrix).
        ptrain_file: Specify pulse shape (ascii matrix).
        spatial_flag: Use spatial prior (appropriate for in vivo data).
        t12prior_flag: Include uncertainty in T1 and T2 values.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "baycest",
        "data_file": data_file,
        "mask_file": mask_file,
        "output_dir": output_dir,
        "pools_file": pools_file,
        "spec_file": spec_file,
        "ptrain_file": ptrain_file,
        "spatial_flag": spatial_flag,
        "t12prior_flag": t12prior_flag,
    }
    return params


def baycest_cargs(
    params: BaycestParameters,
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
    cargs.append("baycest")
    cargs.append("--data=" + execution.input_file(params.get("data_file")))
    cargs.append("--mask=" + execution.input_file(params.get("mask_file")))
    cargs.append("--output=" + params.get("output_dir"))
    cargs.append("--pools=" + execution.input_file(params.get("pools_file")))
    cargs.append("--spec=" + execution.input_file(params.get("spec_file")))
    cargs.append("--ptrain=" + execution.input_file(params.get("ptrain_file")))
    if params.get("spatial_flag"):
        cargs.append("--spatial")
    if params.get("t12prior_flag"):
        cargs.append("--t12prior")
    return cargs


def baycest_outputs(
    params: BaycestParameters,
    execution: Execution,
) -> BaycestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BaycestOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_dir") + "/output_file.nii.gz"),
    )
    return ret


def baycest_execute(
    params: BaycestParameters,
    execution: Execution,
) -> BaycestOutputs:
    """
    Bayesian analysis for chemical exchange saturation transfer z-spectra.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BaycestOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = baycest_cargs(params, execution)
    ret = baycest_outputs(params, execution)
    execution.run(cargs)
    return ret


def baycest(
    data_file: InputPathType,
    mask_file: InputPathType,
    output_dir: str,
    pools_file: InputPathType,
    spec_file: InputPathType,
    ptrain_file: InputPathType,
    spatial_flag: bool = False,
    t12prior_flag: bool = False,
    runner: Runner | None = None,
) -> BaycestOutputs:
    """
    Bayesian analysis for chemical exchange saturation transfer z-spectra.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        data_file: Specify data file (nifti image).
        mask_file: Specify mask file (nifti image).
        output_dir: Specify output directory name.
        pools_file: Specify pools to be included in model (ascii matrix).
        spec_file: Data specification (ascii matrix).
        ptrain_file: Specify pulse shape (ascii matrix).
        spatial_flag: Use spatial prior (appropriate for in vivo data).
        t12prior_flag: Include uncertainty in T1 and T2 values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BaycestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BAYCEST_METADATA)
    params = baycest_params(data_file=data_file, mask_file=mask_file, output_dir=output_dir, pools_file=pools_file, spec_file=spec_file, ptrain_file=ptrain_file, spatial_flag=spatial_flag, t12prior_flag=t12prior_flag)
    return baycest_execute(params, execution)


__all__ = [
    "BAYCEST_METADATA",
    "BaycestOutputs",
    "BaycestParameters",
    "baycest",
    "baycest_params",
]
