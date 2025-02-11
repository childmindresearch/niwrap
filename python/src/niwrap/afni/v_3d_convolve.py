# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_CONVOLVE_METADATA = Metadata(
    id="98f37303338db7321cbe065f60581ee844d011e4.boutiques",
    name="3dConvolve",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dConvolveParameters = typing.TypedDict('V3dConvolveParameters', {
    "__STYX_TYPE__": typing.Literal["3dConvolve"],
    "infile": InputPathType,
    "outfile": str,
    "options": typing.NotRequired[str | None],
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
        "3dConvolve": v_3d_convolve_cargs,
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
        "3dConvolve": v_3d_convolve_outputs,
    }.get(t)


class V3dConvolveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_convolve(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Main output file of 3dConvolve"""


def v_3d_convolve_params(
    infile: InputPathType,
    outfile: str,
    options: str | None = None,
) -> V3dConvolveParameters:
    """
    Build parameters.
    
    Args:
        infile: Input file for 3dConvolve.
        outfile: Output file for 3dConvolve.
        options: Additional options for 3dConvolve.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dConvolve",
        "infile": infile,
        "outfile": outfile,
    }
    if options is not None:
        params["options"] = options
    return params


def v_3d_convolve_cargs(
    params: V3dConvolveParameters,
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
    cargs.append("3dConvolve")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(params.get("outfile"))
    if params.get("options") is not None:
        cargs.extend([
            "-options",
            params.get("options")
        ])
    return cargs


def v_3d_convolve_outputs(
    params: V3dConvolveParameters,
    execution: Execution,
) -> V3dConvolveOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dConvolveOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("outfile")),
    )
    return ret


def v_3d_convolve_execute(
    params: V3dConvolveParameters,
    execution: Execution,
) -> V3dConvolveOutputs:
    """
    3dConvolve is no longer supported in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dConvolveOutputs`).
    """
    cargs = v_3d_convolve_cargs(params, execution)
    ret = v_3d_convolve_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_convolve(
    infile: InputPathType,
    outfile: str,
    options: str | None = None,
    runner: Runner | None = None,
) -> V3dConvolveOutputs:
    """
    3dConvolve is no longer supported in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input file for 3dConvolve.
        outfile: Output file for 3dConvolve.
        options: Additional options for 3dConvolve.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dConvolveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_CONVOLVE_METADATA)
    params = v_3d_convolve_params(infile=infile, outfile=outfile, options=options)
    return v_3d_convolve_execute(params, execution)


__all__ = [
    "V3dConvolveOutputs",
    "V3dConvolveParameters",
    "V_3D_CONVOLVE_METADATA",
    "v_3d_convolve",
    "v_3d_convolve_params",
]
