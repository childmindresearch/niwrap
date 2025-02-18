# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SUMA_REPREFIXIZE_SPEC_METADATA = Metadata(
    id="79a14c14207eea4a930de74235d137c817b02f37.boutiques",
    name="@suma_reprefixize_spec",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VSumaReprefixizeSpecParameters = typing.TypedDict('VSumaReprefixizeSpecParameters', {
    "__STYX_TYPE__": typing.Literal["@suma_reprefixize_spec"],
    "input_file": InputPathType,
    "prefix": str,
    "output_dir": str,
    "work_dir": str,
    "no_clean": bool,
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
        "@suma_reprefixize_spec": v__suma_reprefixize_spec_cargs,
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
        "@suma_reprefixize_spec": v__suma_reprefixize_spec_outputs,
    }.get(t)


class VSumaReprefixizeSpecOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_reprefixize_spec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    prefixed_spec_files: OutputPathType
    """Prefixed SUMA specification files"""


def v__suma_reprefixize_spec_params(
    input_file: InputPathType,
    prefix: str,
    output_dir: str,
    work_dir: str,
    no_clean: bool = False,
) -> VSumaReprefixizeSpecParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input SUMA specification file.
        prefix: Prefix to be added to the file names.
        output_dir: Output directory where the prefixed files will be saved.
        work_dir: Working directory for temporary files.
        no_clean: Flag to avoid cleaning temporary files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@suma_reprefixize_spec",
        "input_file": input_file,
        "prefix": prefix,
        "output_dir": output_dir,
        "work_dir": work_dir,
        "no_clean": no_clean,
    }
    return params


def v__suma_reprefixize_spec_cargs(
    params: VSumaReprefixizeSpecParameters,
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
    cargs.append("@suma_reprefixize_spec")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-preprefix",
        params.get("prefix")
    ])
    cargs.extend([
        "-odir",
        params.get("output_dir")
    ])
    cargs.extend([
        "-workdir",
        params.get("work_dir")
    ])
    if params.get("no_clean"):
        cargs.append("-no_clean")
    return cargs


def v__suma_reprefixize_spec_outputs(
    params: VSumaReprefixizeSpecParameters,
    execution: Execution,
) -> VSumaReprefixizeSpecOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSumaReprefixizeSpecOutputs(
        root=execution.output_file("."),
        prefixed_spec_files=execution.output_file(params.get("output_dir") + "/*.spec"),
    )
    return ret


def v__suma_reprefixize_spec_execute(
    params: VSumaReprefixizeSpecParameters,
    execution: Execution,
) -> VSumaReprefixizeSpecOutputs:
    """
    A tool for prefixing and working with SUMA specification files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSumaReprefixizeSpecOutputs`).
    """
    params = execution.params(params)
    cargs = v__suma_reprefixize_spec_cargs(params, execution)
    ret = v__suma_reprefixize_spec_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__suma_reprefixize_spec(
    input_file: InputPathType,
    prefix: str,
    output_dir: str,
    work_dir: str,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> VSumaReprefixizeSpecOutputs:
    """
    A tool for prefixing and working with SUMA specification files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input SUMA specification file.
        prefix: Prefix to be added to the file names.
        output_dir: Output directory where the prefixed files will be saved.
        work_dir: Working directory for temporary files.
        no_clean: Flag to avoid cleaning temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaReprefixizeSpecOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_REPREFIXIZE_SPEC_METADATA)
    params = v__suma_reprefixize_spec_params(input_file=input_file, prefix=prefix, output_dir=output_dir, work_dir=work_dir, no_clean=no_clean)
    return v__suma_reprefixize_spec_execute(params, execution)


__all__ = [
    "VSumaReprefixizeSpecOutputs",
    "VSumaReprefixizeSpecParameters",
    "V__SUMA_REPREFIXIZE_SPEC_METADATA",
    "v__suma_reprefixize_spec",
    "v__suma_reprefixize_spec_params",
]
