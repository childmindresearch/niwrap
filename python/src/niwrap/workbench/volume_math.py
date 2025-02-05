# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_MATH_METADATA = Metadata(
    id="8ce76040a93a4bb768859018a157e27a98748e59.boutiques",
    name="volume-math",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeMathVarParameters = typing.TypedDict('VolumeMathVarParameters', {
    "__STYX_TYPE__": typing.Literal["var"],
    "name": str,
    "volume": InputPathType,
    "opt_subvolume_subvol": typing.NotRequired[str | None],
    "opt_repeat": bool,
})
VolumeMathParameters = typing.TypedDict('VolumeMathParameters', {
    "__STYX_TYPE__": typing.Literal["volume-math"],
    "expression": str,
    "volume_out": str,
    "opt_fixnan_replace": typing.NotRequired[float | None],
    "var": typing.NotRequired[list[VolumeMathVarParameters] | None],
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
        "volume-math": volume_math_cargs,
        "var": volume_math_var_cargs,
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
    vt = {
        "volume-math": volume_math_outputs,
    }
    return vt.get(t)


def volume_math_var_params(
    name: str,
    volume: InputPathType,
    opt_subvolume_subvol: str | None = None,
    opt_repeat: bool = False,
) -> VolumeMathVarParameters:
    """
    Build parameters.
    
    Args:
        name: the name of the variable, as used in the expression.
        volume: the volume file to use as this variable.
        opt_subvolume_subvol: select a single subvolume: the subvolume number\
            or name.
        opt_repeat: reuse a single subvolume for each subvolume of calculation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "var",
        "name": name,
        "volume": volume,
        "opt_repeat": opt_repeat,
    }
    if opt_subvolume_subvol is not None:
        params["opt_subvolume_subvol"] = opt_subvolume_subvol
    return params


def volume_math_var_cargs(
    params: VolumeMathVarParameters,
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
    cargs.append("-var")
    cargs.append(params.get("name"))
    cargs.append(execution.input_file(params.get("volume")))
    if params.get("opt_subvolume_subvol") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvol")
        ])
    if params.get("opt_repeat"):
        cargs.append("-repeat")
    return cargs


class VolumeMathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_math(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_math_params(
    expression: str,
    volume_out: str,
    opt_fixnan_replace: float | None = None,
    var: list[VolumeMathVarParameters] | None = None,
) -> VolumeMathParameters:
    """
    Build parameters.
    
    Args:
        expression: the expression to evaluate, in quotes.
        volume_out: the output volume.
        opt_fixnan_replace: replace NaN results with a value: value to replace\
            NaN with.
        var: a volume file to use as a variable.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-math",
        "expression": expression,
        "volume_out": volume_out,
    }
    if opt_fixnan_replace is not None:
        params["opt_fixnan_replace"] = opt_fixnan_replace
    if var is not None:
        params["var"] = var
    return params


def volume_math_cargs(
    params: VolumeMathParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-math")
    cargs.append(params.get("expression"))
    cargs.append(params.get("volume_out"))
    if params.get("opt_fixnan_replace") is not None:
        cargs.extend([
            "-fixnan",
            str(params.get("opt_fixnan_replace"))
        ])
    if params.get("var") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("var")] for a in c])
    return cargs


def volume_math_outputs(
    params: VolumeMathParameters,
    execution: Execution,
) -> VolumeMathOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeMathOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_math_execute(
    params: VolumeMathParameters,
    execution: Execution,
) -> VolumeMathOutputs:
    """
    Evaluate expression on volume files.
    
    This command evaluates <expression> at each voxel independently. There must
    be at least one -var option (to get the volume space from), even if the
    <name> specified in it isn't used in <expression>. All volumes must have the
    same volume space. Filenames are not valid in <expression>, use a variable
    name and a -var option with matching <name> to specify an input file. If the
    -subvolume option is given to any -var option, only one subvolume is used
    from that file. If -repeat is specified, the file must either have only one
    subvolume, or have the -subvolume option specified. All files that don't use
    -repeat must have the same number of subvolumes requested to be used. The
    format of <expression> is as follows:
    
    Expressions consist of constants, variables, operators, parentheses, and
    functions, in infix notation, such as 'exp(-x + 3) * scale'. Variables are
    strings of any length, using the characters a-z, A-Z, 0-9, and _, but may
    not take the name of a named constant. Currently, there is only one named
    constant, PI. The operators are +, -, *, /, ^, >, <, >=, <=, ==, !=, !, &&,
    ||. These behave as in C, except that ^ is exponentiation, i.e. pow(x, y),
    and takes higher precedence than other binary operators (also, '-3^-4^-5'
    means '-(3^(-(4^-5)))'). The <=, >=, ==, and != operators are given a small
    amount of wiggle room, equal to one millionth of the smaller of the absolute
    values of the values being compared.
    
    Comparison and logical operators return 0 or 1, you can do masking with
    expressions like 'x * (mask > 0)'. For all logical operators, an input is
    considered true iff it is greater than 0. The expression '0 < x < 5' is not
    syntactically wrong, but it will NOT do what is desired, because it is
    evaluated left to right, i.e. '((0 < x) < 5)', which will always return 1,
    as both possible results of a comparison are less than 5. A warning is
    generated if an expression of this type is detected. Use something like 'x >
    0 && x < 5' to get the desired behavior.
    
    Whitespace between elements is ignored, ' sin ( 2 * x ) ' is equivalent to
    'sin(2*x)', but 's in(2*x)' is an error. Implied multiplication is not
    allowed, the expression '2x' will be parsed as a variable. Parentheses are
    (), do not use [] or {}. Functions require parentheses, the expression 'sin
    x' is an error.
    
    The following functions are supported:
    
    sin: 1 argument, the sine of the argument (units are radians)
    cos: 1 argument, the cosine of the argument (units are radians)
    tan: 1 argument, the tangent of the argument (units are radians)
    asin: 1 argument, the inverse of sine of the argument, in radians
    acos: 1 argument, the inverse of cosine of the argument, in radians
    atan: 1 argument, the inverse of tangent of the argument, in radians
    atan2: 2 arguments, atan2(y, x) returns the inverse of tangent of (y/x), in
    radians, determining quadrant by the sign of both arguments
    sinh: 1 argument, the hyperbolic sine of the argument
    cosh: 1 argument, the hyperbolic cosine of the argument
    tanh: 1 argument, the hyperbolic tangent of the argument
    asinh: 1 argument, the inverse hyperbolic sine of the argument
    acosh: 1 argument, the inverse hyperbolic cosine of the argument
    atanh: 1 argument, the inverse hyperbolic tangent of the argument
    sinc: 1 argument, sinc(0) = 1, sin(x) / x otherwise
    ln: 1 argument, the natural logarithm of the argument
    exp: 1 argument, the constant e raised to the power of the argument
    log: 1 argument, the base 10 logarithm of the argument
    log2: 1 argument, the base 2 logarithm of the argument
    sqrt: 1 argument, the square root of the argument
    abs: 1 argument, the absolute value of the argument
    floor: 1 argument, the largest integer not greater than the argument
    round: 1 argument, the nearest integer, with ties rounded away from zero
    ceil: 1 argument, the smallest integer not less than the argument
    min: 2 arguments, min(x, y) returns y if (x > y), x otherwise
    max: 2 arguments, max(x, y) returns y if (x < y), x otherwise
    mod: 2 arguments, mod(x, y) = x - y * floor(x / y), or 0 if y == 0
    clamp: 3 arguments, clamp(x, low, high) = min(max(x, low), high)
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeMathOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = volume_math_cargs(params, execution)
    ret = volume_math_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_math(
    expression: str,
    volume_out: str,
    opt_fixnan_replace: float | None = None,
    var: list[VolumeMathVarParameters] | None = None,
    runner: Runner | None = None,
) -> VolumeMathOutputs:
    """
    Evaluate expression on volume files.
    
    This command evaluates <expression> at each voxel independently. There must
    be at least one -var option (to get the volume space from), even if the
    <name> specified in it isn't used in <expression>. All volumes must have the
    same volume space. Filenames are not valid in <expression>, use a variable
    name and a -var option with matching <name> to specify an input file. If the
    -subvolume option is given to any -var option, only one subvolume is used
    from that file. If -repeat is specified, the file must either have only one
    subvolume, or have the -subvolume option specified. All files that don't use
    -repeat must have the same number of subvolumes requested to be used. The
    format of <expression> is as follows:
    
    Expressions consist of constants, variables, operators, parentheses, and
    functions, in infix notation, such as 'exp(-x + 3) * scale'. Variables are
    strings of any length, using the characters a-z, A-Z, 0-9, and _, but may
    not take the name of a named constant. Currently, there is only one named
    constant, PI. The operators are +, -, *, /, ^, >, <, >=, <=, ==, !=, !, &&,
    ||. These behave as in C, except that ^ is exponentiation, i.e. pow(x, y),
    and takes higher precedence than other binary operators (also, '-3^-4^-5'
    means '-(3^(-(4^-5)))'). The <=, >=, ==, and != operators are given a small
    amount of wiggle room, equal to one millionth of the smaller of the absolute
    values of the values being compared.
    
    Comparison and logical operators return 0 or 1, you can do masking with
    expressions like 'x * (mask > 0)'. For all logical operators, an input is
    considered true iff it is greater than 0. The expression '0 < x < 5' is not
    syntactically wrong, but it will NOT do what is desired, because it is
    evaluated left to right, i.e. '((0 < x) < 5)', which will always return 1,
    as both possible results of a comparison are less than 5. A warning is
    generated if an expression of this type is detected. Use something like 'x >
    0 && x < 5' to get the desired behavior.
    
    Whitespace between elements is ignored, ' sin ( 2 * x ) ' is equivalent to
    'sin(2*x)', but 's in(2*x)' is an error. Implied multiplication is not
    allowed, the expression '2x' will be parsed as a variable. Parentheses are
    (), do not use [] or {}. Functions require parentheses, the expression 'sin
    x' is an error.
    
    The following functions are supported:
    
    sin: 1 argument, the sine of the argument (units are radians)
    cos: 1 argument, the cosine of the argument (units are radians)
    tan: 1 argument, the tangent of the argument (units are radians)
    asin: 1 argument, the inverse of sine of the argument, in radians
    acos: 1 argument, the inverse of cosine of the argument, in radians
    atan: 1 argument, the inverse of tangent of the argument, in radians
    atan2: 2 arguments, atan2(y, x) returns the inverse of tangent of (y/x), in
    radians, determining quadrant by the sign of both arguments
    sinh: 1 argument, the hyperbolic sine of the argument
    cosh: 1 argument, the hyperbolic cosine of the argument
    tanh: 1 argument, the hyperbolic tangent of the argument
    asinh: 1 argument, the inverse hyperbolic sine of the argument
    acosh: 1 argument, the inverse hyperbolic cosine of the argument
    atanh: 1 argument, the inverse hyperbolic tangent of the argument
    sinc: 1 argument, sinc(0) = 1, sin(x) / x otherwise
    ln: 1 argument, the natural logarithm of the argument
    exp: 1 argument, the constant e raised to the power of the argument
    log: 1 argument, the base 10 logarithm of the argument
    log2: 1 argument, the base 2 logarithm of the argument
    sqrt: 1 argument, the square root of the argument
    abs: 1 argument, the absolute value of the argument
    floor: 1 argument, the largest integer not greater than the argument
    round: 1 argument, the nearest integer, with ties rounded away from zero
    ceil: 1 argument, the smallest integer not less than the argument
    min: 2 arguments, min(x, y) returns y if (x > y), x otherwise
    max: 2 arguments, max(x, y) returns y if (x < y), x otherwise
    mod: 2 arguments, mod(x, y) = x - y * floor(x / y), or 0 if y == 0
    clamp: 3 arguments, clamp(x, low, high) = min(max(x, low), high)
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        expression: the expression to evaluate, in quotes.
        volume_out: the output volume.
        opt_fixnan_replace: replace NaN results with a value: value to replace\
            NaN with.
        var: a volume file to use as a variable.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeMathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_MATH_METADATA)
    params = volume_math_params(expression=expression, volume_out=volume_out, opt_fixnan_replace=opt_fixnan_replace, var=var)
    return volume_math_execute(params, execution)


__all__ = [
    "VOLUME_MATH_METADATA",
    "VolumeMathOutputs",
    "VolumeMathParameters",
    "VolumeMathVarParameters",
    "volume_math",
    "volume_math_params",
    "volume_math_var_params",
]
