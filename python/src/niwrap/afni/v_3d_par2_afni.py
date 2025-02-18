# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_PAR2_AFNI_METADATA = Metadata(
    id="955afce507c339e4fbf43caaf056ad39a659f439.boutiques",
    name="3dPAR2AFNI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dPar2AfniParameters = typing.TypedDict('V3dPar2AfniParameters', {
    "__STYX_TYPE__": typing.Literal["3dPAR2AFNI"],
    "input_file": InputPathType,
    "skip_outliers_test": bool,
    "output_analyze": bool,
    "output_dir": typing.NotRequired[str | None],
    "verbose_flag": bool,
    "gzip_files": bool,
    "byte_swap_4": bool,
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
        "3dPAR2AFNI": v_3d_par2_afni_cargs,
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
        "3dPAR2AFNI": v_3d_par2_afni_outputs,
    }.get(t)


class V3dPar2AfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_par2_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Converted output files"""


def v_3d_par2_afni_params(
    input_file: InputPathType,
    skip_outliers_test: bool = False,
    output_analyze: bool = False,
    output_dir: str | None = None,
    verbose_flag: bool = False,
    gzip_files: bool = False,
    byte_swap_4: bool = False,
) -> V3dPar2AfniParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input PAR file (e.g., subject1.PAR).
        skip_outliers_test: Skip the outliers test when converting 4D files.\
            The default is to perform the outliers test.
        output_analyze: Output ANALYZE files instead of HEAD/BRIK.
        output_dir: The name of the directory where the created files should be\
            placed. If this directory does not exist, the program exits without\
            performing any conversion.
        verbose_flag: Be verbose in operation.
        gzip_files: Gzip the files created. The default is not to gzip the\
            files.
        byte_swap_4: 4-Byte-swap the files created. The default is not to 4\
            byte-swap.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dPAR2AFNI",
        "input_file": input_file,
        "skip_outliers_test": skip_outliers_test,
        "output_analyze": output_analyze,
        "verbose_flag": verbose_flag,
        "gzip_files": gzip_files,
        "byte_swap_4": byte_swap_4,
    }
    if output_dir is not None:
        params["output_dir"] = output_dir
    return params


def v_3d_par2_afni_cargs(
    params: V3dPar2AfniParameters,
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
    cargs.append("3dPAR2AFNI.pl")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("skip_outliers_test"):
        cargs.append("-s")
    if params.get("output_analyze"):
        cargs.append("-a")
    if params.get("output_dir") is not None:
        cargs.extend([
            "-o",
            params.get("output_dir")
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("gzip_files"):
        cargs.append("-g")
    if params.get("byte_swap_4"):
        cargs.append("-4")
    return cargs


def v_3d_par2_afni_outputs(
    params: V3dPar2AfniParameters,
    execution: Execution,
) -> V3dPar2AfniOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dPar2AfniOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(pathlib.Path(params.get("input_file")).name + "_converted"),
    )
    return ret


def v_3d_par2_afni_execute(
    params: V3dPar2AfniParameters,
    execution: Execution,
) -> V3dPar2AfniOutputs:
    """
    Convert Philips PAR/REC files to AFNI's BRIK/HEAD, NIfTI, or ANALYZE format.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dPar2AfniOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_par2_afni_cargs(params, execution)
    ret = v_3d_par2_afni_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_par2_afni(
    input_file: InputPathType,
    skip_outliers_test: bool = False,
    output_analyze: bool = False,
    output_dir: str | None = None,
    verbose_flag: bool = False,
    gzip_files: bool = False,
    byte_swap_4: bool = False,
    runner: Runner | None = None,
) -> V3dPar2AfniOutputs:
    """
    Convert Philips PAR/REC files to AFNI's BRIK/HEAD, NIfTI, or ANALYZE format.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input PAR file (e.g., subject1.PAR).
        skip_outliers_test: Skip the outliers test when converting 4D files.\
            The default is to perform the outliers test.
        output_analyze: Output ANALYZE files instead of HEAD/BRIK.
        output_dir: The name of the directory where the created files should be\
            placed. If this directory does not exist, the program exits without\
            performing any conversion.
        verbose_flag: Be verbose in operation.
        gzip_files: Gzip the files created. The default is not to gzip the\
            files.
        byte_swap_4: 4-Byte-swap the files created. The default is not to 4\
            byte-swap.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dPar2AfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_PAR2_AFNI_METADATA)
    params = v_3d_par2_afni_params(input_file=input_file, skip_outliers_test=skip_outliers_test, output_analyze=output_analyze, output_dir=output_dir, verbose_flag=verbose_flag, gzip_files=gzip_files, byte_swap_4=byte_swap_4)
    return v_3d_par2_afni_execute(params, execution)


__all__ = [
    "V3dPar2AfniOutputs",
    "V3dPar2AfniParameters",
    "V_3D_PAR2_AFNI_METADATA",
    "v_3d_par2_afni",
    "v_3d_par2_afni_params",
]
