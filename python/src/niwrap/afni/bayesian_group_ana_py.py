# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BAYESIAN_GROUP_ANA_PY_METADATA = Metadata(
    id="e49086bdbe64c248fa7b140fd8ae072e880fa9a7.boutiques",
    name="BayesianGroupAna.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
BayesianGroupAnaPyParameters = typing.TypedDict('BayesianGroupAnaPyParameters', {
    "__STYX_TYPE__": typing.Literal["BayesianGroupAna.py"],
    "dataTable": InputPathType,
    "y_variable": str,
    "prefix": typing.NotRequired[str | None],
    "x_variables": typing.NotRequired[list[str] | None],
    "no_center": bool,
    "iterations": typing.NotRequired[float | None],
    "chains": typing.NotRequired[float | None],
    "control_list": typing.NotRequired[str | None],
    "plot": bool,
    "more_plots": typing.NotRequired[list[str] | None],
    "RData": bool,
    "seed": typing.NotRequired[float | None],
    "overwrite": bool,
    "help": bool,
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
        "BayesianGroupAna.py": bayesian_group_ana_py_cargs,
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
        "BayesianGroupAna.py": bayesian_group_ana_py_outputs,
    }.get(t)


class BayesianGroupAnaPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bayesian_group_ana_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    summary: OutputPathType | None
    """Summary of the brmsfit object from R."""
    rhats: OutputPathType | None
    """Rhats for each effect and x variable combination."""
    intercept_table: OutputPathType | None
    """Table with the MedianEst, StdDev, 2.50%, 5%, 50%, 95%, and 97.50% of each
    ROI for the Intercept term."""
    x_var_table: OutputPathType | None
    """The same table as the Intercept but for the specified x variable."""


def bayesian_group_ana_py_params(
    data_table: InputPathType,
    y_variable: str,
    prefix: str | None = None,
    x_variables: list[str] | None = None,
    no_center: bool = False,
    iterations: float | None = None,
    chains: float | None = None,
    control_list: str | None = None,
    plot: bool = False,
    more_plots: list[str] | None = None,
    rdata: bool = False,
    seed: float | None = None,
    overwrite: bool = False,
    help_: bool = False,
) -> BayesianGroupAnaPyParameters:
    """
    Build parameters.
    
    Args:
        data_table: Input text file containing the data table.
        y_variable: Column name for the y variable.
        prefix: Name of the output file.
        x_variables: Column name(s) for the x variables. If not specified, only\
            the intercept will be added.
        no_center: Disable centering on the x variables. Maybe useful if you\
            centered manually.
        iterations: Number of total iterations per chain including warmup.\
            Default [1000].
        chains: Number of Markov chains. Default [4].
        control_list: Comma separated list of control parameters to pass to the\
            brm function. Default is the brm function defaults.
        plot: Output box, fit, and posterior prediction plots.
        more_plots: Output 'stanplots' given different types of plot names.
        rdata: Save the R session workspace and data.
        seed: Seed to generate random number. Default [1234].
        overwrite: Overwrites the output files.
        help_: Show help message and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "BayesianGroupAna.py",
        "dataTable": data_table,
        "y_variable": y_variable,
        "no_center": no_center,
        "plot": plot,
        "RData": rdata,
        "overwrite": overwrite,
        "help": help_,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if x_variables is not None:
        params["x_variables"] = x_variables
    if iterations is not None:
        params["iterations"] = iterations
    if chains is not None:
        params["chains"] = chains
    if control_list is not None:
        params["control_list"] = control_list
    if more_plots is not None:
        params["more_plots"] = more_plots
    if seed is not None:
        params["seed"] = seed
    return params


def bayesian_group_ana_py_cargs(
    params: BayesianGroupAnaPyParameters,
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
    cargs.append("BayesianGroupAna.py")
    cargs.append(execution.input_file(params.get("dataTable")))
    cargs.append(params.get("y_variable"))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("x_variables") is not None:
        cargs.extend([
            "-x",
            *params.get("x_variables")
        ])
    if params.get("no_center"):
        cargs.append("-no_center")
    if params.get("iterations") is not None:
        cargs.extend([
            "-iterations",
            str(params.get("iterations"))
        ])
    if params.get("chains") is not None:
        cargs.extend([
            "-chains",
            str(params.get("chains"))
        ])
    if params.get("control_list") is not None:
        cargs.extend([
            "-control_list",
            params.get("control_list")
        ])
    if params.get("plot"):
        cargs.append("-plot")
    if params.get("more_plots") is not None:
        cargs.extend([
            "-more_plots",
            *params.get("more_plots")
        ])
    if params.get("RData"):
        cargs.append("-RData")
    if params.get("seed") is not None:
        cargs.extend([
            "-seed",
            str(params.get("seed"))
        ])
    if params.get("overwrite"):
        cargs.append("-overwrite")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def bayesian_group_ana_py_outputs(
    params: BayesianGroupAnaPyParameters,
    execution: Execution,
) -> BayesianGroupAnaPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BayesianGroupAnaPyOutputs(
        root=execution.output_file("."),
        summary=execution.output_file(params.get("prefix") + "_summary.txt") if (params.get("prefix") is not None) else None,
        rhats=execution.output_file(params.get("prefix") + "_rhats.csv") if (params.get("prefix") is not None) else None,
        intercept_table=execution.output_file(params.get("prefix") + "_Intercept_table.csv") if (params.get("prefix") is not None) else None,
        x_var_table=execution.output_file(params.get("prefix") + "_table.csv") if (params.get("prefix") is not None) else None,
    )
    return ret


def bayesian_group_ana_py_execute(
    params: BayesianGroupAnaPyParameters,
    execution: Execution,
) -> BayesianGroupAnaPyOutputs:
    """
    This program conducts Bayesian Group Analysis (BGA) on a list of regions of
    interest (ROIs). Compared to the conventional univariate GLM, BGA pools and
    shares the information across the ROIs in a multilevel system.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BayesianGroupAnaPyOutputs`).
    """
    cargs = bayesian_group_ana_py_cargs(params, execution)
    ret = bayesian_group_ana_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def bayesian_group_ana_py(
    data_table: InputPathType,
    y_variable: str,
    prefix: str | None = None,
    x_variables: list[str] | None = None,
    no_center: bool = False,
    iterations: float | None = None,
    chains: float | None = None,
    control_list: str | None = None,
    plot: bool = False,
    more_plots: list[str] | None = None,
    rdata: bool = False,
    seed: float | None = None,
    overwrite: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> BayesianGroupAnaPyOutputs:
    """
    This program conducts Bayesian Group Analysis (BGA) on a list of regions of
    interest (ROIs). Compared to the conventional univariate GLM, BGA pools and
    shares the information across the ROIs in a multilevel system.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        data_table: Input text file containing the data table.
        y_variable: Column name for the y variable.
        prefix: Name of the output file.
        x_variables: Column name(s) for the x variables. If not specified, only\
            the intercept will be added.
        no_center: Disable centering on the x variables. Maybe useful if you\
            centered manually.
        iterations: Number of total iterations per chain including warmup.\
            Default [1000].
        chains: Number of Markov chains. Default [4].
        control_list: Comma separated list of control parameters to pass to the\
            brm function. Default is the brm function defaults.
        plot: Output box, fit, and posterior prediction plots.
        more_plots: Output 'stanplots' given different types of plot names.
        rdata: Save the R session workspace and data.
        seed: Seed to generate random number. Default [1234].
        overwrite: Overwrites the output files.
        help_: Show help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BayesianGroupAnaPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BAYESIAN_GROUP_ANA_PY_METADATA)
    params = bayesian_group_ana_py_params(data_table=data_table, y_variable=y_variable, prefix=prefix, x_variables=x_variables, no_center=no_center, iterations=iterations, chains=chains, control_list=control_list, plot=plot, more_plots=more_plots, rdata=rdata, seed=seed, overwrite=overwrite, help_=help_)
    return bayesian_group_ana_py_execute(params, execution)


__all__ = [
    "BAYESIAN_GROUP_ANA_PY_METADATA",
    "BayesianGroupAnaPyOutputs",
    "BayesianGroupAnaPyParameters",
    "bayesian_group_ana_py",
    "bayesian_group_ana_py_params",
]
