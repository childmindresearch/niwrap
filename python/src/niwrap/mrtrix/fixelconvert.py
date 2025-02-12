# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIXELCONVERT_METADATA = Metadata(
    id="61e22f7f494e1cc9061508aaffc5a41839e5a5fa.boutiques",
    name="fixelconvert",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
FixelconvertConfigParameters = typing.TypedDict('FixelconvertConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
FixelconvertVariousStringParameters = typing.TypedDict('FixelconvertVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
FixelconvertVariousFileParameters = typing.TypedDict('FixelconvertVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
FixelconvertVariousString1Parameters = typing.TypedDict('FixelconvertVariousString1Parameters', {
    "__STYX_TYPE__": typing.Literal["VariousString_1"],
    "obj": str,
})
FixelconvertVariousFile1Parameters = typing.TypedDict('FixelconvertVariousFile1Parameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile_1"],
    "obj": InputPathType,
})
FixelconvertParameters = typing.TypedDict('FixelconvertParameters', {
    "__STYX_TYPE__": typing.Literal["fixelconvert"],
    "name": typing.NotRequired[str | None],
    "nii": bool,
    "out_size": bool,
    "template": typing.NotRequired[InputPathType | None],
    "value": typing.NotRequired[InputPathType | None],
    "in_size": typing.NotRequired[InputPathType | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[FixelconvertConfigParameters] | None],
    "help": bool,
    "version": bool,
    "fixel_in": typing.Union[FixelconvertVariousStringParameters, FixelconvertVariousFileParameters],
    "fixel_out": typing.Union[FixelconvertVariousString1Parameters, FixelconvertVariousFile1Parameters],
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
        "fixelconvert": fixelconvert_cargs,
        "config": fixelconvert_config_cargs,
        "VariousString": fixelconvert_various_string_cargs,
        "VariousFile": fixelconvert_various_file_cargs,
        "VariousString_1": fixelconvert_various_string_1_cargs,
        "VariousFile_1": fixelconvert_various_file_1_cargs,
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
    }.get(t)


def fixelconvert_config_params(
    key: str,
    value: str,
) -> FixelconvertConfigParameters:
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


def fixelconvert_config_cargs(
    params: FixelconvertConfigParameters,
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


def fixelconvert_various_string_params(
    obj: str,
) -> FixelconvertVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def fixelconvert_various_string_cargs(
    params: FixelconvertVariousStringParameters,
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
    cargs.append(params.get("obj"))
    return cargs


def fixelconvert_various_file_params(
    obj: InputPathType,
) -> FixelconvertVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def fixelconvert_various_file_cargs(
    params: FixelconvertVariousFileParameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def fixelconvert_various_string_1_params(
    obj: str,
) -> FixelconvertVariousString1Parameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString_1",
        "obj": obj,
    }
    return params


def fixelconvert_various_string_1_cargs(
    params: FixelconvertVariousString1Parameters,
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
    cargs.append(params.get("obj"))
    return cargs


def fixelconvert_various_file_1_params(
    obj: InputPathType,
) -> FixelconvertVariousFile1Parameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile_1",
        "obj": obj,
    }
    return params


def fixelconvert_various_file_1_cargs(
    params: FixelconvertVariousFile1Parameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


class FixelconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fixelconvert_params(
    fixel_in: typing.Union[FixelconvertVariousStringParameters, FixelconvertVariousFileParameters],
    fixel_out: typing.Union[FixelconvertVariousString1Parameters, FixelconvertVariousFile1Parameters],
    name: str | None = None,
    nii: bool = False,
    out_size: bool = False,
    template: InputPathType | None = None,
    value: InputPathType | None = None,
    in_size: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> FixelconvertParameters:
    """
    Build parameters.
    
    Args:
        fixel_in: the input fixel file / directory.
        fixel_out: the output fixel file / directory.
        name: assign a different name to the value field output (Default:\
            value). Do not include the file extension.
        nii: output the index, directions and data file in NIfTI format instead\
            of .mif.
        out_size: also output the 'size' field from the old format.
        template: specify an existing fixel directory (in the new format) to\
            which the new output should conform.
        value: nominate the data file to import to the 'value' field in the old\
            format.
        in_size: import data for the 'size' field in the old format.
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
        "__STYXTYPE__": "fixelconvert",
        "nii": nii,
        "out_size": out_size,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "fixel_in": fixel_in,
        "fixel_out": fixel_out,
    }
    if name is not None:
        params["name"] = name
    if template is not None:
        params["template"] = template
    if value is not None:
        params["value"] = value
    if in_size is not None:
        params["in_size"] = in_size
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def fixelconvert_cargs(
    params: FixelconvertParameters,
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
    cargs.append("fixelconvert")
    if params.get("name") is not None:
        cargs.extend([
            "-name",
            params.get("name")
        ])
    if params.get("nii"):
        cargs.append("-nii")
    if params.get("out_size"):
        cargs.append("-out_size")
    if params.get("template") is not None:
        cargs.extend([
            "-template",
            execution.input_file(params.get("template"))
        ])
    if params.get("value") is not None:
        cargs.extend([
            "-value",
            execution.input_file(params.get("value"))
        ])
    if params.get("in_size") is not None:
        cargs.extend([
            "-in_size",
            execution.input_file(params.get("in_size"))
        ])
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
    cargs.extend(dyn_cargs(params.get("fixel_in")["__STYXTYPE__"])(params.get("fixel_in"), execution))
    cargs.extend(dyn_cargs(params.get("fixel_out")["__STYXTYPE__"])(params.get("fixel_out"), execution))
    return cargs


def fixelconvert_outputs(
    params: FixelconvertParameters,
    execution: Execution,
) -> FixelconvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FixelconvertOutputs(
        root=execution.output_file("."),
    )
    return ret


def fixelconvert_execute(
    params: FixelconvertParameters,
    execution: Execution,
) -> FixelconvertOutputs:
    """
    Convert between the old format fixel image (.msf / .msh) and the new fixel
    directory format.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FixelconvertOutputs`).
    """
    cargs = fixelconvert_cargs(params, execution)
    ret = fixelconvert_outputs(params, execution)
    execution.run(cargs)
    return ret


def fixelconvert(
    fixel_in: typing.Union[FixelconvertVariousStringParameters, FixelconvertVariousFileParameters],
    fixel_out: typing.Union[FixelconvertVariousString1Parameters, FixelconvertVariousFile1Parameters],
    name: str | None = None,
    nii: bool = False,
    out_size: bool = False,
    template: InputPathType | None = None,
    value: InputPathType | None = None,
    in_size: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> FixelconvertOutputs:
    """
    Convert between the old format fixel image (.msf / .msh) and the new fixel
    directory format.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        fixel_in: the input fixel file / directory.
        fixel_out: the output fixel file / directory.
        name: assign a different name to the value field output (Default:\
            value). Do not include the file extension.
        nii: output the index, directions and data file in NIfTI format instead\
            of .mif.
        out_size: also output the 'size' field from the old format.
        template: specify an existing fixel directory (in the new format) to\
            which the new output should conform.
        value: nominate the data file to import to the 'value' field in the old\
            format.
        in_size: import data for the 'size' field in the old format.
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
        NamedTuple of outputs (described in `FixelconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELCONVERT_METADATA)
    params = fixelconvert_params(name=name, nii=nii, out_size=out_size, template=template, value=value, in_size=in_size, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, fixel_in=fixel_in, fixel_out=fixel_out)
    return fixelconvert_execute(params, execution)


__all__ = [
    "FIXELCONVERT_METADATA",
    "FixelconvertConfigParameters",
    "FixelconvertOutputs",
    "FixelconvertParameters",
    "FixelconvertVariousFile1Parameters",
    "FixelconvertVariousFileParameters",
    "FixelconvertVariousString1Parameters",
    "FixelconvertVariousStringParameters",
    "fixelconvert",
    "fixelconvert_config_params",
    "fixelconvert_params",
    "fixelconvert_various_file_1_params",
    "fixelconvert_various_file_params",
    "fixelconvert_various_string_1_params",
    "fixelconvert_various_string_params",
]
