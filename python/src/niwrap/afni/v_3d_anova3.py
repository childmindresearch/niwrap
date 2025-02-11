# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ANOVA3_METADATA = Metadata(
    id="fe7391c6cb7a9865c9618e3aa5f2eb36c7ee57f4.boutiques",
    name="3dANOVA3",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAnova3Parameters = typing.TypedDict('V3dAnova3Parameters', {
    "__STYX_TYPE__": typing.Literal["3dANOVA3"],
    "type": int,
    "alevels": int,
    "blevels": int,
    "clevels": int,
    "dsets": list[str],
    "voxel_num": typing.NotRequired[int | None],
    "diskspace": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "anova_options": typing.NotRequired[list[str] | None],
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
        "3dANOVA3": v_3d_anova3_cargs,
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
        "3dANOVA3": v_3d_anova3_outputs,
    }.get(t)


class V3dAnova3Outputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_anova3(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_fa: OutputPathType
    """Output file for the main ANOVA result."""
    outfile_fb: OutputPathType
    """Output file for the main B ANOVA result."""
    outfile_fc: OutputPathType
    """Output file for the main C ANOVA result."""
    outfile_fab: OutputPathType
    """Output file for the interaction between A and B."""
    outfile_fac: OutputPathType
    """Output file for the interaction between A and C."""
    outfile_fbc: OutputPathType
    """Output file for the interaction between B and C."""
    outfile_fabc: OutputPathType
    """Output file for the interaction between A, B, and C."""
    outfile_amean: OutputPathType
    """Output file for the A mean results."""
    outfile_bmean: OutputPathType
    """Output file for the B mean results."""


def v_3d_anova3_params(
    type_: int,
    alevels: int,
    blevels: int,
    clevels: int,
    dsets: list[str],
    voxel_num: int | None = None,
    diskspace: bool = False,
    mask: InputPathType | None = None,
    anova_options: list[str] | None = None,
) -> V3dAnova3Parameters:
    """
    Build parameters.
    
    Args:
        type_: Type of ANOVA model to be used. k = 1: A,B,C fixed; AxBxC, k =\
            2: A,B,C random; AxBxC, k = 3: A fixed; B,C random; AxBxC, k = 4: A,B\
            fixed; C random; AxBxC, k = 5: A,B fixed; C random; AxB,BxC,C(A).
        alevels: Number of levels for factor A.
        blevels: Number of levels for factor B.
        clevels: Number of levels for factor C.
        dsets: Input data sets for specific levels of factors A, B, and C.
        voxel_num: Screen output for specified voxel number.
        diskspace: Print out disk space required for program execution.
        mask: Use sub-brick #0 of dataset to define which voxels to process.
        anova_options: Modified ANOVA computation options. See:\
            https://afni.nimh.nih.gov/sscc/gangc/ANOVA_Mod.html.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dANOVA3",
        "type": type_,
        "alevels": alevels,
        "blevels": blevels,
        "clevels": clevels,
        "dsets": dsets,
        "diskspace": diskspace,
    }
    if voxel_num is not None:
        params["voxel_num"] = voxel_num
    if mask is not None:
        params["mask"] = mask
    if anova_options is not None:
        params["anova_options"] = anova_options
    return params


def v_3d_anova3_cargs(
    params: V3dAnova3Parameters,
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
    cargs.append("3dANOVA3")
    cargs.extend([
        "-type",
        str(params.get("type"))
    ])
    cargs.extend([
        "-alevels",
        str(params.get("alevels"))
    ])
    cargs.extend([
        "-blevels",
        str(params.get("blevels"))
    ])
    cargs.extend([
        "-clevels",
        str(params.get("clevels"))
    ])
    cargs.extend([
        "-dset",
        *params.get("dsets")
    ])
    if params.get("voxel_num") is not None:
        cargs.extend([
            "-voxel",
            str(params.get("voxel_num"))
        ])
    if params.get("diskspace"):
        cargs.append("-diskspace")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    cargs.append("[OUTFILES]")
    if params.get("anova_options") is not None:
        cargs.extend([
            "-old_method -OK -assume_sph",
            *params.get("anova_options")
        ])
    return cargs


def v_3d_anova3_outputs(
    params: V3dAnova3Parameters,
    execution: Execution,
) -> V3dAnova3Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAnova3Outputs(
        root=execution.output_file("."),
        outfile_fa=execution.output_file("[OUTFILE_FA]"),
        outfile_fb=execution.output_file("[OUTFILE_FB]"),
        outfile_fc=execution.output_file("[OUTFILE_FC]"),
        outfile_fab=execution.output_file("[OUTFILE_FAB]"),
        outfile_fac=execution.output_file("[OUTFILE_FAC]"),
        outfile_fbc=execution.output_file("[OUTFILE_FBC]"),
        outfile_fabc=execution.output_file("[OUTFILE_FABC]"),
        outfile_amean=execution.output_file("[OUTFILE_AMEAN]"),
        outfile_bmean=execution.output_file("[OUTFILE_BMEAN]"),
    )
    return ret


def v_3d_anova3_execute(
    params: V3dAnova3Parameters,
    execution: Execution,
) -> V3dAnova3Outputs:
    """
    Performs three-factor ANOVA on 3D data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAnova3Outputs`).
    """
    cargs = v_3d_anova3_cargs(params, execution)
    ret = v_3d_anova3_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_anova3(
    type_: int,
    alevels: int,
    blevels: int,
    clevels: int,
    dsets: list[str],
    voxel_num: int | None = None,
    diskspace: bool = False,
    mask: InputPathType | None = None,
    anova_options: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dAnova3Outputs:
    """
    Performs three-factor ANOVA on 3D data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        type_: Type of ANOVA model to be used. k = 1: A,B,C fixed; AxBxC, k =\
            2: A,B,C random; AxBxC, k = 3: A fixed; B,C random; AxBxC, k = 4: A,B\
            fixed; C random; AxBxC, k = 5: A,B fixed; C random; AxB,BxC,C(A).
        alevels: Number of levels for factor A.
        blevels: Number of levels for factor B.
        clevels: Number of levels for factor C.
        dsets: Input data sets for specific levels of factors A, B, and C.
        voxel_num: Screen output for specified voxel number.
        diskspace: Print out disk space required for program execution.
        mask: Use sub-brick #0 of dataset to define which voxels to process.
        anova_options: Modified ANOVA computation options. See:\
            https://afni.nimh.nih.gov/sscc/gangc/ANOVA_Mod.html.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAnova3Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ANOVA3_METADATA)
    params = v_3d_anova3_params(type_=type_, alevels=alevels, blevels=blevels, clevels=clevels, dsets=dsets, voxel_num=voxel_num, diskspace=diskspace, mask=mask, anova_options=anova_options)
    return v_3d_anova3_execute(params, execution)


__all__ = [
    "V3dAnova3Outputs",
    "V3dAnova3Parameters",
    "V_3D_ANOVA3_METADATA",
    "v_3d_anova3",
    "v_3d_anova3_params",
]
