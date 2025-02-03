# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__BUILD_AFNI_XLIB_METADATA = Metadata(
    id="335ac2386eff0dba38cfaae81dacca730457f4a7.boutiques",
    name="@build_afni_Xlib",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VBuildAfniXlibParameters = typing.TypedDict('VBuildAfniXlibParameters', {
    "__STYX_TYPE__": typing.Literal["@build_afni_Xlib"],
    "localinstall": bool,
    "debug_symbols": bool,
    "lib64": bool,
    "packages": list[str],
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
        "@build_afni_Xlib": v__build_afni_xlib_cargs,
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


class VBuildAfniXlibOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__build_afni_xlib(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__build_afni_xlib_params(
    packages: list[str],
    localinstall: bool = False,
    debug_symbols: bool = False,
    lib64: bool = False,
) -> VBuildAfniXlibParameters:
    """
    Build parameters.
    
    Args:
        packages: Packages to compile and install (e.g., lesstif, openmotif,\
            libXt).
        localinstall: Install under each package directory.
        debug_symbols: Compile with -g to add symbols.
        lib64: Install libs under lib64 (default is lib).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@build_afni_Xlib",
        "localinstall": localinstall,
        "debug_symbols": debug_symbols,
        "lib64": lib64,
        "packages": packages,
    }
    return params


def v__build_afni_xlib_cargs(
    params: VBuildAfniXlibParameters,
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
    cargs.append("@build_afni_Xlib")
    if params.get("localinstall"):
        cargs.append("-localinstall")
    if params.get("debug_symbols"):
        cargs.append("-g")
    if params.get("lib64"):
        cargs.append("-lib64")
    cargs.extend(params.get("packages"))
    return cargs


def v__build_afni_xlib_outputs(
    params: VBuildAfniXlibParameters,
    execution: Execution,
) -> VBuildAfniXlibOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VBuildAfniXlibOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__build_afni_xlib_execute(
    params: VBuildAfniXlibParameters,
    execution: Execution,
) -> VBuildAfniXlibOutputs:
    """
    Compile and install lesstif, openmotif, and/or libXt.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VBuildAfniXlibOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__build_afni_xlib_cargs(params, execution)
    ret = v__build_afni_xlib_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__build_afni_xlib(
    packages: list[str],
    localinstall: bool = False,
    debug_symbols: bool = False,
    lib64: bool = False,
    runner: Runner | None = None,
) -> VBuildAfniXlibOutputs:
    """
    Compile and install lesstif, openmotif, and/or libXt.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        packages: Packages to compile and install (e.g., lesstif, openmotif,\
            libXt).
        localinstall: Install under each package directory.
        debug_symbols: Compile with -g to add symbols.
        lib64: Install libs under lib64 (default is lib).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VBuildAfniXlibOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__BUILD_AFNI_XLIB_METADATA)
    params = v__build_afni_xlib_params(localinstall=localinstall, debug_symbols=debug_symbols, lib64=lib64, packages=packages)
    return v__build_afni_xlib_execute(params, execution)


__all__ = [
    "VBuildAfniXlibOutputs",
    "V__BUILD_AFNI_XLIB_METADATA",
    "v__build_afni_xlib",
    "v__build_afni_xlib_params",
]
