# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TBSS_3_POSTREG_METADATA = Metadata(
    id="8629f29c3ee03810baedd803bec842f121834cff.boutiques",
    name="tbss_3_postreg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Tbss3PostregParameters = typing.TypedDict('Tbss3PostregParameters', {
    "__STYX_TYPE__": typing.Literal["tbss_3_postreg"],
    "derive_mean_from_study": bool,
    "use_fmrib58": bool,
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
        "tbss_3_postreg": tbss_3_postreg_cargs,
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
        "tbss_3_postreg": tbss_3_postreg_outputs,
    }.get(t)


class Tbss3PostregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_3_postreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tbss_3_postreg_params(
    derive_mean_from_study: bool = False,
    use_fmrib58: bool = False,
) -> Tbss3PostregParameters:
    """
    Build parameters.
    
    Args:
        derive_mean_from_study: Derive mean_FA and mean_FA_skeleton from mean\
            of all subjects in study (recommended).
        use_fmrib58: Use FMRIB58_FA and its skeleton instead of study-derived\
            mean and skeleton.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tbss_3_postreg",
        "derive_mean_from_study": derive_mean_from_study,
        "use_fmrib58": use_fmrib58,
    }
    return params


def tbss_3_postreg_cargs(
    params: Tbss3PostregParameters,
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
    cargs.append("tbss_3_postreg")
    if params.get("derive_mean_from_study"):
        cargs.append("-S")
    if params.get("use_fmrib58"):
        cargs.append("-T")
    return cargs


def tbss_3_postreg_outputs(
    params: Tbss3PostregParameters,
    execution: Execution,
) -> Tbss3PostregOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Tbss3PostregOutputs(
        root=execution.output_file("."),
    )
    return ret


def tbss_3_postreg_execute(
    params: Tbss3PostregParameters,
    execution: Execution,
) -> Tbss3PostregOutputs:
    """
    TBSS post-registration processing.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Tbss3PostregOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tbss_3_postreg_cargs(params, execution)
    ret = tbss_3_postreg_outputs(params, execution)
    execution.run(cargs)
    return ret


def tbss_3_postreg(
    derive_mean_from_study: bool = False,
    use_fmrib58: bool = False,
    runner: Runner | None = None,
) -> Tbss3PostregOutputs:
    """
    TBSS post-registration processing.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        derive_mean_from_study: Derive mean_FA and mean_FA_skeleton from mean\
            of all subjects in study (recommended).
        use_fmrib58: Use FMRIB58_FA and its skeleton instead of study-derived\
            mean and skeleton.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tbss3PostregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_3_POSTREG_METADATA)
    params = tbss_3_postreg_params(derive_mean_from_study=derive_mean_from_study, use_fmrib58=use_fmrib58)
    return tbss_3_postreg_execute(params, execution)


__all__ = [
    "TBSS_3_POSTREG_METADATA",
    "Tbss3PostregOutputs",
    "Tbss3PostregParameters",
    "tbss_3_postreg",
    "tbss_3_postreg_params",
]
