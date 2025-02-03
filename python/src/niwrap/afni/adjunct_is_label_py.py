# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_IS_LABEL_PY_METADATA = Metadata(
    id="fd161fa6ffe35fb86b826e60d07e867baeceef7c.boutiques",
    name="adjunct_is_label.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AdjunctIsLabelPyParameters = typing.TypedDict('AdjunctIsLabelPyParameters', {
    "__STYX_TYPE__": typing.Literal["adjunct_is_label.py"],
    "infile": InputPathType,
    "label": str,
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
        "adjunct_is_label.py": adjunct_is_label_py_cargs,
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


class AdjunctIsLabelPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_is_label_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_is_label_py_params(
    infile: InputPathType,
    label: str,
) -> AdjunctIsLabelPyParameters:
    """
    Build parameters.
    
    Args:
        infile: Input file for the adjunct_is_label script.
        label: Output label generated by the script.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "adjunct_is_label.py",
        "infile": infile,
        "label": label,
    }
    return params


def adjunct_is_label_py_cargs(
    params: AdjunctIsLabelPyParameters,
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
    cargs.append("adjunct_is_label.py")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(params.get("label"))
    return cargs


def adjunct_is_label_py_outputs(
    params: AdjunctIsLabelPyParameters,
    execution: Execution,
) -> AdjunctIsLabelPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AdjunctIsLabelPyOutputs(
        root=execution.output_file("."),
    )
    return ret


def adjunct_is_label_py_execute(
    params: AdjunctIsLabelPyParameters,
    execution: Execution,
) -> AdjunctIsLabelPyOutputs:
    """
    A subsidiary script of the chauffeur_afni suite for label functionalities.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AdjunctIsLabelPyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = adjunct_is_label_py_cargs(params, execution)
    ret = adjunct_is_label_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def adjunct_is_label_py(
    infile: InputPathType,
    label: str,
    runner: Runner | None = None,
) -> AdjunctIsLabelPyOutputs:
    """
    A subsidiary script of the chauffeur_afni suite for label functionalities.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input file for the adjunct_is_label script.
        label: Output label generated by the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctIsLabelPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_IS_LABEL_PY_METADATA)
    params = adjunct_is_label_py_params(infile=infile, label=label)
    return adjunct_is_label_py_execute(params, execution)


__all__ = [
    "ADJUNCT_IS_LABEL_PY_METADATA",
    "AdjunctIsLabelPyOutputs",
    "adjunct_is_label_py",
    "adjunct_is_label_py_params",
]
