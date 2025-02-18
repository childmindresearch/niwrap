# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1D_NLFIT_METADATA = Metadata(
    id="278b48af705917ecf316b95eb2c3d2075a15c475.boutiques",
    name="1dNLfit",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dNlfitParameters = typing.TypedDict('V1dNlfitParameters', {
    "__STYX_TYPE__": typing.Literal["1dNLfit"],
    "expression": str,
    "independent_variable": str,
    "parameters": list[str],
    "dependent_data": InputPathType,
    "method": typing.NotRequired[int | None],
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
        "1dNLfit": v_1d_nlfit_cargs,
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
        "1dNLfit": v_1d_nlfit_outputs,
    }.get(t)


class V1dNlfitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_nlfit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fit_results: OutputPathType
    """Results (fitted time series models) are written to stdout. Should be
    saved by '>' redirection."""


def v_1d_nlfit_params(
    expression: str,
    independent_variable: str,
    parameters: list[str],
    dependent_data: InputPathType,
    method: int | None = None,
) -> V1dNlfitParameters:
    """
    Build parameters.
    
    Args:
        expression: The expression for the fit. It must contain one symbol from\
            'a' to 'z' which is marked as the independent variable by option\
            '-indvar', and at least one more symbol which is a parameter to be\
            estimated.
        independent_variable: Indicates which variable in '-expr' is the\
            independent variable. All other symbols are parameters, which are\
            either fixed (constants) or variables to be estimated. Read the values\
            of the independent variable from 1D file.
        parameters: Set fixed value or estimating range for a particular\
            symbol. For a fixed value, it takes the form 'a=3.14'. For an estimated\
            parameter, it takes the form 'q=-sqrt(2):sqrt(2)'. All symbols in\
            '-expr' must have a corresponding '-param' option, EXCEPT for the\
            '-indvar' symbol.
        dependent_data: Read the values of the dependent variable (to be fitted\
            to '-expr') from 1D file. The file must have the same number of rows as\
            the '-indvar' file.
        method: Set the method for fitting: '1' for L1, '2' for L2 (default is\
            L2).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dNLfit",
        "expression": expression,
        "independent_variable": independent_variable,
        "parameters": parameters,
        "dependent_data": dependent_data,
    }
    if method is not None:
        params["method"] = method
    return params


def v_1d_nlfit_cargs(
    params: V1dNlfitParameters,
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
    cargs.append("1dNLfit")
    cargs.extend([
        "-expr",
        params.get("expression")
    ])
    cargs.extend([
        "-indvar",
        params.get("independent_variable")
    ])
    cargs.extend([
        "-param",
        *params.get("parameters")
    ])
    cargs.extend([
        "-depdata",
        execution.input_file(params.get("dependent_data"))
    ])
    if params.get("method") is not None:
        cargs.extend([
            "-meth",
            str(params.get("method"))
        ])
    return cargs


def v_1d_nlfit_outputs(
    params: V1dNlfitParameters,
    execution: Execution,
) -> V1dNlfitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dNlfitOutputs(
        root=execution.output_file("."),
        fit_results=execution.output_file("stdout"),
    )
    return ret


def v_1d_nlfit_execute(
    params: V1dNlfitParameters,
    execution: Execution,
) -> V1dNlfitOutputs:
    """
    Program to fit a model to a vector of data. The model is given by a symbolic
    expression, with parameters to be estimated.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dNlfitOutputs`).
    """
    params = execution.params(params)
    cargs = v_1d_nlfit_cargs(params, execution)
    ret = v_1d_nlfit_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_nlfit(
    expression: str,
    independent_variable: str,
    parameters: list[str],
    dependent_data: InputPathType,
    method: int | None = None,
    runner: Runner | None = None,
) -> V1dNlfitOutputs:
    """
    Program to fit a model to a vector of data. The model is given by a symbolic
    expression, with parameters to be estimated.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        expression: The expression for the fit. It must contain one symbol from\
            'a' to 'z' which is marked as the independent variable by option\
            '-indvar', and at least one more symbol which is a parameter to be\
            estimated.
        independent_variable: Indicates which variable in '-expr' is the\
            independent variable. All other symbols are parameters, which are\
            either fixed (constants) or variables to be estimated. Read the values\
            of the independent variable from 1D file.
        parameters: Set fixed value or estimating range for a particular\
            symbol. For a fixed value, it takes the form 'a=3.14'. For an estimated\
            parameter, it takes the form 'q=-sqrt(2):sqrt(2)'. All symbols in\
            '-expr' must have a corresponding '-param' option, EXCEPT for the\
            '-indvar' symbol.
        dependent_data: Read the values of the dependent variable (to be fitted\
            to '-expr') from 1D file. The file must have the same number of rows as\
            the '-indvar' file.
        method: Set the method for fitting: '1' for L1, '2' for L2 (default is\
            L2).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dNlfitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_NLFIT_METADATA)
    params = v_1d_nlfit_params(expression=expression, independent_variable=independent_variable, parameters=parameters, dependent_data=dependent_data, method=method)
    return v_1d_nlfit_execute(params, execution)


__all__ = [
    "V1dNlfitOutputs",
    "V1dNlfitParameters",
    "V_1D_NLFIT_METADATA",
    "v_1d_nlfit",
    "v_1d_nlfit_params",
]
