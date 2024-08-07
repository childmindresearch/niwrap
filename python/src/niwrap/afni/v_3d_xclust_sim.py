# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_XCLUST_SIM_METADATA = Metadata(
    id="c55ad068d6232d9ddd5f8b40583f510b109fb4d1",
    name="3dXClustSim",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dXclustSimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_xclust_sim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_mthresh: OutputPathType | None
    """Output multi-threshold files for each -ncase input"""


def v_3d_xclust_sim(
    inset: InputPathType,
    insdat: InputPathType | None = None,
    nn: float | int | None = None,
    sid: float | int | None = None,
    hpow: list[float | int] | None = None,
    ncase: list[str] | None = None,
    pthr: list[float | int] | None = None,
    fpr: float | int | None = None,
    multi_fpr: bool = False,
    minclust: float | int | None = None,
    local: bool = False,
    global_: bool = False,
    nolocal: bool = False,
    noglobal: bool = False,
    splitfrac: float | int | None = None,
    prefix: str | None = None,
    verbose: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dXclustSimOutputs:
    """
    3dXClustSim by AFNI Team.
    
    ETAC processing tool to find cluster figure of merit (FOM) thresholds.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dXClustSim.html
    
    Args:
        inset: Mask sdata file (from 3dtoXdataset or 3dttest++).
        insdat: Data files in the '.sdat' format.
        nn: Neighborhood connectivity (1, 2, or 3). Default is 2.
        sid: Sidedness: 1 (one-sided) or 2 (two-sided). Default is 2.
        hpow: H power values (can be a subset of 0, 1, 2). Default is 2.
        ncase: Number of cases with labels. Default is 1 A.
        pthr: List of p-value thresholds. Default is 0.0100 0.0056 0.0031\
            0.0018 0.0010.
        fpr: Set global FPR goal to an integer ff between 2 and 9. Default is\
            5.
        multi_fpr: Compute results for multiple FPR goals (2%, 3%, ... 9%).
        minclust: Minimum cluster size in voxels. Default is 5.
        local: Do voxel-wise (local) ETAC computations.
        global_: Do volume-wise (global) ETAC computations.
        nolocal: Do not perform voxel-wise ETAC computations.
        noglobal: Do not perform volume-wise ETAC computations.
        splitfrac: Fraction to split simulations into pieces (0.2 < F < 0.8).
        prefix: Output filename prefix.
        verbose: Be more verbose.
        quiet: Silent mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dXclustSimOutputs`).
    """
    runner = runner or get_global_runner()
    if fpr is not None and not (2 <= fpr <= 9): 
        raise ValueError(f"'fpr' must be between 2 <= x <= 9 but was {fpr}")
    if splitfrac is not None and not (0.2 <= splitfrac <= 0.8): 
        raise ValueError(f"'splitfrac' must be between 0.2 <= x <= 0.8 but was {splitfrac}")
    execution = runner.start_execution(V_3D_XCLUST_SIM_METADATA)
    cargs = []
    cargs.append("3dXClustSim")
    cargs.append(execution.input_file(inset))
    if insdat is not None:
        cargs.append(execution.input_file(insdat))
    if nn is not None:
        cargs.extend(["-NN", str(nn)])
    if sid is not None:
        cargs.extend(["-sid", str(sid)])
    if hpow is not None:
        cargs.extend(["-hpow", *map(str, hpow)])
    if ncase is not None:
        cargs.extend(["-ncase", *ncase])
    if pthr is not None:
        cargs.extend(["-pthr", *map(str, pthr)])
    if fpr is not None:
        cargs.extend(["-FPR", str(fpr)])
    if multi_fpr:
        cargs.append("-multiFPR")
    if minclust is not None:
        cargs.extend(["-minclust", str(minclust)])
    if local:
        cargs.append("-local")
    if global_:
        cargs.append("-global")
    if nolocal:
        cargs.append("-nolocal")
    if noglobal:
        cargs.append("-noglobal")
    if splitfrac is not None:
        cargs.extend(["-splitfrac", str(splitfrac)])
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if verbose:
        cargs.append("-verb")
    if quiet:
        cargs.append("-quiet")
    ret = V3dXclustSimOutputs(
        root=execution.output_file("."),
        out_mthresh=execution.output_file(f"{prefix}.mthresh.*.nii") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dXclustSimOutputs",
    "V_3D_XCLUST_SIM_METADATA",
    "v_3d_xclust_sim",
]
