# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DIRGEN_METADATA = Metadata(
    id="111662ebc02bd748b7609e8b39562fb928767bbb.boutiques",
    name="dirgen",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
DirgenConfigParameters = typing.TypedDict('DirgenConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
DirgenParameters = typing.TypedDict('DirgenParameters', {
    "__STYX_TYPE__": typing.Literal["dirgen"],
    "power": typing.NotRequired[int | None],
    "niter": typing.NotRequired[int | None],
    "restarts": typing.NotRequired[int | None],
    "unipolar": bool,
    "cartesian": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[DirgenConfigParameters] | None],
    "help": bool,
    "version": bool,
    "ndir": int,
    "dirs": str,
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
        "dirgen": dirgen_cargs,
        "config": dirgen_config_cargs,
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
        "dirgen": dirgen_outputs,
        "config": dirgen_config_outputs,
    }.get(t)


def dirgen_config_params(
    key: str,
    value: str,
) -> DirgenConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def dirgen_config_cargs(
    params: DirgenConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class DirgenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dirgen(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dirs: OutputPathType
    """the text file to write the directions to, as [ az el ] pairs."""


def dirgen_params(
    ndir: int,
    dirs: str,
    power: int | None = None,
    niter: int | None = None,
    restarts: int | None = None,
    unipolar: bool = False,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirgenConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> DirgenParameters:
    """
    Build parameters.
    
    Args:
        ndir: the number of directions to generate.
        dirs: the text file to write the directions to, as [ az el ] pairs.
        power: specify exponent to use for repulsion power law (default: 1).\
            This must be a power of 2 (i.e. 1, 2, 4, 8, 16, ...).
        niter: specify the maximum number of iterations to perform (default:\
            10000).
        restarts: specify the number of restarts to perform (default: 10).
        unipolar: optimise assuming a unipolar electrostatic repulsion model\
            rather than the bipolar model normally assumed in DWI.
        cartesian: Output the directions in Cartesian coordinates [x y z]\
            instead of [az el].
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dirgen",
        "unipolar": unipolar,
        "cartesian": cartesian,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "ndir": ndir,
        "dirs": dirs,
    }
    if power is not None:
        params["power"] = power
    if niter is not None:
        params["niter"] = niter
    if restarts is not None:
        params["restarts"] = restarts
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dirgen_cargs(
    params: DirgenParameters,
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
    cargs.append("dirgen")
    if params.get("power") is not None:
        cargs.extend([
            "-power",
            str(params.get("power"))
        ])
    if params.get("niter") is not None:
        cargs.extend([
            "-niter",
            str(params.get("niter"))
        ])
    if params.get("restarts") is not None:
        cargs.extend([
            "-restarts",
            str(params.get("restarts"))
        ])
    if params.get("unipolar"):
        cargs.append("-unipolar")
    if params.get("cartesian"):
        cargs.append("-cartesian")
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(str(params.get("ndir")))
    cargs.append(params.get("dirs"))
    return cargs


def dirgen_outputs(
    params: DirgenParameters,
    execution: Execution,
) -> DirgenOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DirgenOutputs(
        root=execution.output_file("."),
        dirs=execution.output_file(params.get("dirs")),
    )
    return ret


def dirgen_execute(
    params: DirgenParameters,
    execution: Execution,
) -> DirgenOutputs:
    """
    Generate a set of uniformly distributed directions using a bipolar electrostatic
    repulsion model.
    
    Directions are distributed by analogy to an electrostatic repulsion system,
    with each direction corresponding to a single electrostatic charge (for
    -unipolar), or a pair of diametrically opposed charges (for the default
    bipolar case). The energy of the system is determined based on the Coulomb
    repulsion, which assumes the form 1/r^power, where r is the distance between
    any pair of charges, and p is the power assumed for the repulsion law
    (default: 1). The minimum energy state is obtained by gradient descent.
    
    References:
    
    Jones, D.; Horsfield, M. & Simmons, A. Optimal strategies for measuring
    diffusion in anisotropic systems by magnetic resonance imaging. Magnetic
    Resonance in Medicine, 1999, 42: 515-525
    
    Papadakis, N. G.; Murrills, C. D.; Hall, L. D.; Huang, C. L.-H. & Adrian
    Carpenter, T. Minimal gradient encoding for robust estimation of diffusion
    anisotropy. Magnetic Resonance Imaging, 2000, 18: 671-679.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DirgenOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dirgen_cargs(params, execution)
    ret = dirgen_outputs(params, execution)
    execution.run(cargs)
    return ret


def dirgen(
    ndir: int,
    dirs: str,
    power: int | None = None,
    niter: int | None = None,
    restarts: int | None = None,
    unipolar: bool = False,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirgenConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DirgenOutputs:
    """
    Generate a set of uniformly distributed directions using a bipolar electrostatic
    repulsion model.
    
    Directions are distributed by analogy to an electrostatic repulsion system,
    with each direction corresponding to a single electrostatic charge (for
    -unipolar), or a pair of diametrically opposed charges (for the default
    bipolar case). The energy of the system is determined based on the Coulomb
    repulsion, which assumes the form 1/r^power, where r is the distance between
    any pair of charges, and p is the power assumed for the repulsion law
    (default: 1). The minimum energy state is obtained by gradient descent.
    
    References:
    
    Jones, D.; Horsfield, M. & Simmons, A. Optimal strategies for measuring
    diffusion in anisotropic systems by magnetic resonance imaging. Magnetic
    Resonance in Medicine, 1999, 42: 515-525
    
    Papadakis, N. G.; Murrills, C. D.; Hall, L. D.; Huang, C. L.-H. & Adrian
    Carpenter, T. Minimal gradient encoding for robust estimation of diffusion
    anisotropy. Magnetic Resonance Imaging, 2000, 18: 671-679.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        ndir: the number of directions to generate.
        dirs: the text file to write the directions to, as [ az el ] pairs.
        power: specify exponent to use for repulsion power law (default: 1).\
            This must be a power of 2 (i.e. 1, 2, 4, 8, 16, ...).
        niter: specify the maximum number of iterations to perform (default:\
            10000).
        restarts: specify the number of restarts to perform (default: 10).
        unipolar: optimise assuming a unipolar electrostatic repulsion model\
            rather than the bipolar model normally assumed in DWI.
        cartesian: Output the directions in Cartesian coordinates [x y z]\
            instead of [az el].
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DirgenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIRGEN_METADATA)
    params = dirgen_params(power=power, niter=niter, restarts=restarts, unipolar=unipolar, cartesian=cartesian, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, ndir=ndir, dirs=dirs)
    return dirgen_execute(params, execution)


__all__ = [
    "DIRGEN_METADATA",
    "DirgenConfigParameters",
    "DirgenOutputs",
    "DirgenParameters",
    "dirgen",
    "dirgen_config_params",
    "dirgen_params",
]
