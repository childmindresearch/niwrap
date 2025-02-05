# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_WARPFIELD_METADATA = Metadata(
    id="e0f48a3f4d002bf731b7f13e5d1964bc0562c643.boutiques",
    name="convert-warpfield",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
ConvertWarpfieldFromWorldParameters = typing.TypedDict('ConvertWarpfieldFromWorldParameters', {
    "__STYX_TYPE__": typing.Literal["from_world"],
    "input": str,
    "opt_absolute": bool,
})
ConvertWarpfieldFromFnirtParameters = typing.TypedDict('ConvertWarpfieldFromFnirtParameters', {
    "__STYX_TYPE__": typing.Literal["from_fnirt"],
    "input": str,
    "source_volume": str,
    "opt_absolute": bool,
})
ConvertWarpfieldToFnirtParameters = typing.TypedDict('ConvertWarpfieldToFnirtParameters', {
    "__STYX_TYPE__": typing.Literal["to_fnirt"],
    "output": str,
    "source_volume": str,
})
ConvertWarpfieldParameters = typing.TypedDict('ConvertWarpfieldParameters', {
    "__STYX_TYPE__": typing.Literal["convert-warpfield"],
    "from_world": typing.NotRequired[ConvertWarpfieldFromWorldParameters | None],
    "opt_from_itk_input": typing.NotRequired[str | None],
    "from_fnirt": typing.NotRequired[ConvertWarpfieldFromFnirtParameters | None],
    "opt_to_world_output": typing.NotRequired[str | None],
    "opt_to_itk_output": typing.NotRequired[str | None],
    "to_fnirt": typing.NotRequired[list[ConvertWarpfieldToFnirtParameters] | None],
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
        "convert-warpfield": convert_warpfield_cargs,
        "from_world": convert_warpfield_from_world_cargs,
        "from_fnirt": convert_warpfield_from_fnirt_cargs,
        "to_fnirt": convert_warpfield_to_fnirt_cargs,
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
    vt = {}
    return vt.get(t)


def convert_warpfield_from_world_params(
    input_: str,
    opt_absolute: bool = False,
) -> ConvertWarpfieldFromWorldParameters:
    """
    Build parameters.
    
    Args:
        input_: the input warpfield.
        opt_absolute: warpfield was written in absolute convention, rather than\
            relative.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "from_world",
        "input": input_,
        "opt_absolute": opt_absolute,
    }
    return params


def convert_warpfield_from_world_cargs(
    params: ConvertWarpfieldFromWorldParameters,
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
    cargs.append("-from-world")
    cargs.append(params.get("input"))
    if params.get("opt_absolute"):
        cargs.append("-absolute")
    return cargs


def convert_warpfield_from_fnirt_params(
    input_: str,
    source_volume: str,
    opt_absolute: bool = False,
) -> ConvertWarpfieldFromFnirtParameters:
    """
    Build parameters.
    
    Args:
        input_: the input warpfield.
        source_volume: the source volume used when generating the input\
            warpfield.
        opt_absolute: warpfield was written in absolute convention, rather than\
            relative.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "from_fnirt",
        "input": input_,
        "source_volume": source_volume,
        "opt_absolute": opt_absolute,
    }
    return params


def convert_warpfield_from_fnirt_cargs(
    params: ConvertWarpfieldFromFnirtParameters,
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
    cargs.append("-from-fnirt")
    cargs.append(params.get("input"))
    cargs.append(params.get("source_volume"))
    if params.get("opt_absolute"):
        cargs.append("-absolute")
    return cargs


def convert_warpfield_to_fnirt_params(
    output: str,
    source_volume: str,
) -> ConvertWarpfieldToFnirtParameters:
    """
    Build parameters.
    
    Args:
        output: output - the output warpfield.
        source_volume: the volume you want to apply the warpfield to.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "to_fnirt",
        "output": output,
        "source_volume": source_volume,
    }
    return params


def convert_warpfield_to_fnirt_cargs(
    params: ConvertWarpfieldToFnirtParameters,
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
    cargs.append("-to-fnirt")
    cargs.append(params.get("output"))
    cargs.append(params.get("source_volume"))
    return cargs


class ConvertWarpfieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_warpfield(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def convert_warpfield_params(
    from_world: ConvertWarpfieldFromWorldParameters | None = None,
    opt_from_itk_input: str | None = None,
    from_fnirt: ConvertWarpfieldFromFnirtParameters | None = None,
    opt_to_world_output: str | None = None,
    opt_to_itk_output: str | None = None,
    to_fnirt: list[ConvertWarpfieldToFnirtParameters] | None = None,
) -> ConvertWarpfieldParameters:
    """
    Build parameters.
    
    Args:
        from_world: input is a NIFTI 'world' warpfield.
        opt_from_itk_input: input is an ITK warpfield: the input warpfield.
        from_fnirt: input is a fnirt warpfield.
        opt_to_world_output: write output as a NIFTI 'world' warpfield: output\
            - the output warpfield.
        opt_to_itk_output: write output as an ITK warpfield: output - the\
            output warpfield.
        to_fnirt: write output as a fnirt warpfield.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "convert-warpfield",
    }
    if from_world is not None:
        params["from_world"] = from_world
    if opt_from_itk_input is not None:
        params["opt_from_itk_input"] = opt_from_itk_input
    if from_fnirt is not None:
        params["from_fnirt"] = from_fnirt
    if opt_to_world_output is not None:
        params["opt_to_world_output"] = opt_to_world_output
    if opt_to_itk_output is not None:
        params["opt_to_itk_output"] = opt_to_itk_output
    if to_fnirt is not None:
        params["to_fnirt"] = to_fnirt
    return params


def convert_warpfield_cargs(
    params: ConvertWarpfieldParameters,
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
    cargs.append("-convert-warpfield")
    if params.get("from_world") is not None:
        cargs.extend(dyn_cargs(params.get("from_world")["__STYXTYPE__"])(params.get("from_world"), execution))
    if params.get("opt_from_itk_input") is not None:
        cargs.extend([
            "-from-itk",
            params.get("opt_from_itk_input")
        ])
    if params.get("from_fnirt") is not None:
        cargs.extend(dyn_cargs(params.get("from_fnirt")["__STYXTYPE__"])(params.get("from_fnirt"), execution))
    if params.get("opt_to_world_output") is not None:
        cargs.extend([
            "-to-world",
            params.get("opt_to_world_output")
        ])
    if params.get("opt_to_itk_output") is not None:
        cargs.extend([
            "-to-itk",
            params.get("opt_to_itk_output")
        ])
    if params.get("to_fnirt") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("to_fnirt")] for a in c])
    return cargs


def convert_warpfield_outputs(
    params: ConvertWarpfieldParameters,
    execution: Execution,
) -> ConvertWarpfieldOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertWarpfieldOutputs(
        root=execution.output_file("."),
    )
    return ret


def convert_warpfield_execute(
    params: ConvertWarpfieldParameters,
    execution: Execution,
) -> ConvertWarpfieldOutputs:
    """
    Convert a warpfield between conventions.
    
    NIFTI world warpfields can be used directly on mm coordinates via sampling
    the three subvolumes at the coordinate and adding the sampled values to the
    coordinate vector. They use the NIFTI coordinate system, that is, X is left
    to right, Y is posterior to anterior, and Z is inferior to superior.
    
    NOTE: this command does not invert the warpfield, and to warp a surface, you
    must use the inverse of the warpfield that warps the corresponding volume.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-fnirt may be specified more than once.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertWarpfieldOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = convert_warpfield_cargs(params, execution)
    ret = convert_warpfield_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_warpfield(
    from_world: ConvertWarpfieldFromWorldParameters | None = None,
    opt_from_itk_input: str | None = None,
    from_fnirt: ConvertWarpfieldFromFnirtParameters | None = None,
    opt_to_world_output: str | None = None,
    opt_to_itk_output: str | None = None,
    to_fnirt: list[ConvertWarpfieldToFnirtParameters] | None = None,
    runner: Runner | None = None,
) -> ConvertWarpfieldOutputs:
    """
    Convert a warpfield between conventions.
    
    NIFTI world warpfields can be used directly on mm coordinates via sampling
    the three subvolumes at the coordinate and adding the sampled values to the
    coordinate vector. They use the NIFTI coordinate system, that is, X is left
    to right, Y is posterior to anterior, and Z is inferior to superior.
    
    NOTE: this command does not invert the warpfield, and to warp a surface, you
    must use the inverse of the warpfield that warps the corresponding volume.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-fnirt may be specified more than once.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        from_world: input is a NIFTI 'world' warpfield.
        opt_from_itk_input: input is an ITK warpfield: the input warpfield.
        from_fnirt: input is a fnirt warpfield.
        opt_to_world_output: write output as a NIFTI 'world' warpfield: output\
            - the output warpfield.
        opt_to_itk_output: write output as an ITK warpfield: output - the\
            output warpfield.
        to_fnirt: write output as a fnirt warpfield.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertWarpfieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_WARPFIELD_METADATA)
    params = convert_warpfield_params(from_world=from_world, opt_from_itk_input=opt_from_itk_input, from_fnirt=from_fnirt, opt_to_world_output=opt_to_world_output, opt_to_itk_output=opt_to_itk_output, to_fnirt=to_fnirt)
    return convert_warpfield_execute(params, execution)


__all__ = [
    "CONVERT_WARPFIELD_METADATA",
    "ConvertWarpfieldFromFnirtParameters",
    "ConvertWarpfieldFromWorldParameters",
    "ConvertWarpfieldOutputs",
    "ConvertWarpfieldParameters",
    "ConvertWarpfieldToFnirtParameters",
    "convert_warpfield",
    "convert_warpfield_from_fnirt_params",
    "convert_warpfield_from_world_params",
    "convert_warpfield_params",
    "convert_warpfield_to_fnirt_params",
]
